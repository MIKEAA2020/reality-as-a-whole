"""Stationary-scattering checks for the two-window continuum slice argument.

The companion proof is analytic. Product integration approximates the
principal value, and cannot establish a continuum theorem by itself.
"""
import math
import unittest
import numpy as np
from numpy.polynomial.legendre import leggauss
from verification.zero_autonomous_two_window_records_test import make_model,theta_apply

SY=np.array([[0,-1j],[1j,0]])
P1=np.diag([0.,1.])


def K(x):
    return np.exp(-x*x/2)*2/np.pi*np.sinc(2*x/np.pi)


def kernel(p,q,m1,m2):
    d=np.asarray(p)[:,None]-np.asarray(q)[None,:]
    base=K(d)
    return (-1.*(base*np.exp(5j*d))[:,:,None,None]*SY
            -1.3*(m1*base+m2*base*np.exp(-5j*d))[:,:,None,None]*P1)


def stationary(n,p0,m1,m2):
    """Solve u=V(.,p0)-V R0(E+i0)u, including on-shell value."""
    x,w=leggauss(n);p=-6.5+x/2;w=w/2
    points=np.r_[p,p0];d=p-p0
    # R0= (T-E-i0)^-1 = [6/(p+p0)]/(p-p0+i0).
    r=6*w/(p+p0)/d
    r0=(3/p0)*(np.log((-6-p0)/(p0+7))-np.sum(w/d)-1j*np.pi)
    weights=np.r_[r,r0]
    V=kernel(points,points,m1,m2)
    mat=np.eye(2*(n+1),dtype=complex)+(V*weights[None,:,None,None]).transpose(0,2,1,3).reshape(2*(n+1),2*(n+1))
    rhs=V[:,-1,:,:].reshape(2*(n+1),2)
    u=np.linalg.solve(mat,rhs).reshape(n+1,2,2)
    return points,weights,u


def slice_matrix(points,weights,u,alpha):
    phase=np.exp(1j*points*alpha)
    return np.exp(1j*points[-1]*alpha)*np.eye(2)-np.einsum('q,q,qij->ij',phase,weights,u)


class TwoWindowContinuumSliceTests(unittest.TestCase):
    def test_memory_y_block_matches_full_operator(self):
        model=make_model(32);p=model[0];rng=np.random.default_rng(4)
        y={s:np.array([1,1j*s])/math.sqrt(2) for s in (-1,1)}
        for m1 in (-1,1):
            for m2 in (-1,1):
                v=rng.normal(size=(2,len(p)))+1j*rng.normal(size=(2,len(p)))
                full=np.einsum('ip,j,k->ijkp',v,y[m1],y[m2])
                result=theta_apply(model,full,0)
                E=model[2]
                expected=p[None,:]**2/6*v-2*.5*(SY@v)@E[0].T
                expected-=2*(P1@v)@(m1*.65*E[1]+m2*.65*E[2]).T
                wanted=np.einsum('ip,j,k->ijkp',expected,y[m1],y[m2])
                self.assertLess(np.linalg.norm(result-wanted),1e-11)

    def test_stationary_kernel_hermiticity(self):
        p=np.array([-6.95,-6.72,-6.4,-6.09])
        for a in (-1,1):
            for b in (-1,1):
                V=kernel(p,p,a,b)
                self.assertLess(np.linalg.norm(V-V.transpose(1,0,3,2).conj()),1e-13)

    def test_free_limit_and_scattering_asymptotic(self):
        for signs in ((1,1),(-1,1),(1,-1),(-1,-1)):
            p,w,u=stationary(120,-6.5,*signs)
            F=slice_matrix(p,w,u,70)*np.exp(1j*6.5*70)
            self.assertLess(np.linalg.norm(F-np.eye(2)),.025)
            self.assertGreater(abs(np.linalg.det(F)),.97)

    def test_on_shell_scattering_matrix_is_unitary(self):
        for signs in ((1,1),(-1,1),(1,-1),(-1,-1)):
            p,w,u=stationary(100,-6.5,*signs)
            S=np.eye(2)-2j*np.pi*(3/6.5)*u[-1]
            self.assertLess(np.linalg.norm(S.conj().T@S-np.eye(2)),1e-11)

    def test_invertible_slice_transport_keeps_spectral_norm(self):
        p,w,u=stationary(100,-6.5,1,-1)
        A=slice_matrix(p,w,u,0); B=slice_matrix(p,w,u,10)
        c=np.array([.3+.4j,-.2+.7j]); data=A@c
        moved=B@np.linalg.solve(A,data)
        self.assertLess(np.linalg.norm(moved-B@c),1e-12)
        self.assertAlmostEqual(np.linalg.norm(np.linalg.solve(B,moved)),np.linalg.norm(c),places=12)

    def test_edge_coupling_has_both_signs_in_every_channel(self):
        for m1 in (-1,1):
            for m2 in (-1,1):
                edge=kernel(np.array([-6.]),np.array([-6.]),m1,m2)[0,0]
                values=np.linalg.eigvalsh(edge)
                self.assertLess(values[0],0)
                self.assertGreater(values[1],0)
                self.assertAlmostEqual(np.linalg.det(edge).real,-4/np.pi**2,places=12)

    def test_exterior_edge_modes_are_present_in_grid(self):
        p,_,Es,*_=make_model(80)
        for m1 in (-1,1):
            for m2 in (-1,1):
                H=np.kron(np.eye(2),np.diag(p*p/6))-np.kron(SY,Es[0])-1.3*np.kron(P1,m1*Es[1]+m2*Es[2])
                vals=np.linalg.eigvalsh(H)
                self.assertLess(vals[0],6)
                self.assertGreater(vals[-1],49/6)

    def test_stationary_grid_converges_at_selected_slices(self):
        for signs in ((1,1),(-1,1),(1,-1),(-1,-1)):
            for p0 in (-6.8,-6.5,-6.2):
                p,w,u=stationary(60,p0,*signs)
                p2,w2,u2=stationary(100,p0,*signs)
                for alpha in (-10,0,10,30):
                    F=slice_matrix(p,w,u,alpha)
                    F2=slice_matrix(p2,w2,u2,alpha)
                    self.assertLess(np.linalg.norm(F-F2),1e-8)
                    self.assertGreater(abs(np.linalg.det(F2)),1e-5)

    def test_fourier_signal_requires_both_pointer_components(self):
        # One scalar row from a multiplicity-two fibre always has a kernel.
        p,w,u=stationary(100,-6.5,1,-1)
        F=slice_matrix(p,w,u,0)
        self.assertGreater(abs(np.linalg.det(F)),1e-5)
        null=np.array([F[0,1],-F[0,0]])
        self.assertGreater(np.linalg.norm(null),1e-5)
        self.assertLess(abs(F[0]@null),1e-13)
        self.assertGreater(np.linalg.norm(F@null),1e-5)

if __name__=='__main__':unittest.main()
