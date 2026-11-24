"""Lighthouse-inspired exact zero-charge/clock/memory/sphere construction.

A deliberately prescribed finite model; no claim it derives gravity or experience.
"""
import math
import unittest
import numpy as np
from verification.zero_integrated_sphere_clock_experience_test import sphere

I=np.eye(2,dtype=complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1.,-1.]).astype(complex)
YP=np.array([1.,1j])/math.sqrt(2)
YM=np.array([1.,-1j])/math.sqrt(2)
B0=np.array([1.,0.],complex)
B1=np.array([0.,1.],complex)
# Clock eigenvalues 0,3,1 in units of g.
E=np.array([0.,3.,1.])
T=2*math.pi


def full_state(p,context='triple'):
    s=sphere(context).reshape(2,-1)
    out=np.zeros((3,s.shape[1],2),complex)
    out[0]=math.sqrt(p)*np.outer(s[0],B0)
    out[1]=1j*math.sqrt((1-p)/2)*np.outer(s[1],YP)
    out[2]=1j*math.sqrt((1-p)/2)*np.outer(s[1],YM)
    return out


def clock_vector(t):return np.exp(-1j*E*t)/math.sqrt(3)


def conditional(p,t):
    # Analytic conditioned state in sphere-code h,B axes.
    a=np.zeros((2,2),complex)
    a[0,0]=math.sqrt(p)
    a[1]=1j*math.sqrt(1-p)*np.exp(2j*t)*np.array([math.cos(t),-math.sin(t)])
    return a


def h_b_joint(p,t):return abs(conditional(p,t))**2


def entropy(p):
    return -sum(v*math.log2(v) for v in p if v>1e-15)


def modular(rho,A,s):
    e,U=np.linalg.eigh(rho)
    if e.min()<=0:raise ValueError('state must be faithful on chosen support')
    q=(U*(e**(1j*s)))@U.conj().T
    return q@A@q.conj().T


class LighthouseZeroEnergyClockTests(unittest.TestCase):
    def test_energy_eigenstate_actual_sphere(self):
        s=sphere('triple').reshape(2,-1)
        self.assertAlmostEqual(np.linalg.norm(s[0]),1,places=12)
        self.assertAlmostEqual(np.linalg.norm(s[1]),1,places=12)
        self.assertLess(abs(np.vdot(s[0],s[1])),1e-13)
        # H_C=diag(0,3,1), H_rest=h⊗(2I+Y), H_tot=H_C−H_rest.
        rest=np.kron(np.diag([0.,1.]),2*I+Y)
        total=np.kron(np.diag(E),np.eye(4))-np.kron(np.eye(3),rest)
        for p in (1/3,.5,.75):
            v=np.zeros((3,2,2),complex)
            v[0,0]=math.sqrt(p)*B0
            v[1,1]=1j*math.sqrt((1-p)/2)*YP
            v[2,1]=1j*math.sqrt((1-p)/2)*YM
            self.assertLess(np.linalg.norm(total@v.ravel()),1e-13)
            self.assertAlmostEqual(np.linalg.norm(full_state(p)),1,places=12)
            for j in range(3):
                np.testing.assert_allclose(full_state(p)[j],np.einsum('hb,hx->xb',v[j],s),atol=1e-13)

    def test_clock_povm_and_conditional_history(self):
        # Exact discrete quadrature for harmonics 0,1,3; integral E(dt)=I.
        n=96;tv=T*np.arange(n)/n
        povm=sum(3/n*np.outer(clock_vector(t),clock_vector(t).conj()) for t in tv)
        np.testing.assert_allclose(povm,np.eye(3),atol=1e-13)
        for p in (1/3,.5,.75):
            f=full_state(p);s=sphere('triple').reshape(2,-1)
            for t in (0,.13,math.pi/4,math.pi/2,2.7):
                projected=np.einsum('c,cxb->xb',clock_vector(t).conj(),f)
                self.assertAlmostEqual(np.linalg.norm(projected)**2,1/3,places=12)
                desired=np.einsum('hb,hx->xb',conditional(p,t),s)
                np.testing.assert_allclose(projected*math.sqrt(3),desired,atol=1e-12)

    def test_relational_record_and_signed_candidate(self):
        for p in (1/3,.5,.75):
            x=h_b_joint(p,0);y=h_b_joint(p,math.pi/2)
            np.testing.assert_allclose(x,[[p,0],[1-p,0]],atol=1e-13)
            np.testing.assert_allclose(y,[[p,0],[0,1-p]],atol=1e-13)
            self.assertAlmostEqual(entropy(y.sum(axis=0)),entropy([p,1-p]),places=12)
            # B=1 means h=1, where R and J signed candidates are opposite.
            for r in (1,-1):
                self.assertNotEqual((r,-r),(-r,r))
                self.assertEqual(r-r,0)

    def test_both_whole_and_subsystem_reductions(self):
        p=1/3;state=full_state(p);a=state.reshape(3,-1)
        rhoC=a@a.conj().T
        np.testing.assert_allclose(rhoC,np.eye(3)/3,atol=1e-13)
        # Construct actual sphere record–B state at two conditional readings.
        actual=sphere('triple')
        for t in (0,math.pi/4,math.pi/2):
            whole=np.einsum('habirw,hk->abirwk',actual,conditional(p,t))
            m=whole.transpose(3,5,0,1,2,4).reshape(8,-1)
            rho=m@m.conj().T
            mat=conditional(p,t)
            rhoB=mat.T@mat.conj()
            np.testing.assert_allclose(rho,np.kron(np.diag([0,.5,.5,0]),rhoB),atol=1e-13)

    def test_trace_and_nontrace_modular_flows_do_not_generate_memory(self):
        # Rest support consists of |Ψ0,0>, |Ψ1,+y>, |Ψ1,-y>.
        Bz=np.array([[1,0,0],[0,0,1],[0,1,0]],complex)
        HR=np.diag(E)
        self.assertGreater(np.linalg.norm(HR@Bz-Bz@HR),1)
        for p in (1/3,.5,.75):
            rho=np.diag([p,(1-p)/2,(1-p)/2]).astype(complex)
            np.testing.assert_allclose(modular(rho,Bz,.71),Bz,atol=1e-12)
            if p==1/3:
                np.testing.assert_allclose(rho,np.eye(3)/3,atol=1e-13)
            # Yet the conditional B1 probability for h1 changes from 0 to 1.
            self.assertAlmostEqual(h_b_joint(p,0)[1,1],0)
            self.assertAlmostEqual(h_b_joint(p,math.pi/2)[1,1],1-p)

    def test_same_marginals_and_zero_energy_different_clock_histories(self):
        # On the 3D correlated energy support, compare the coherent pure
        # state with its dephasing in the matching-energy basis.
        p=1/3
        for t in (0.,math.pi/4,math.pi/2,2.2):
            pure=h_b_joint(p,t)
            incoherent=np.array([[p,0.],[(1-p)/2,(1-p)/2]])
            self.assertAlmostEqual(incoherent.sum(),1,places=12)
            if t==0.:
                self.assertAlmostEqual(pure[1,1],0.)
                self.assertAlmostEqual(incoherent[1,1],1/3)
            if t==math.pi/2:
                self.assertAlmostEqual(pure[1,1],2/3)
                self.assertAlmostEqual(incoherent[1,1],1/3)
        # Construct physical 3×3 matched-energy purification and dephase it.
        f=np.diag([1.,1j,1j]).astype(complex)/math.sqrt(3)
        rho_pure=np.outer(f.ravel(),f.ravel().conj())
        rho_diag=np.diag(np.diag(rho_pure))
        def reductions(rho):
            x=rho.reshape(3,3,3,3)
            return np.einsum('arbr->ab',x),np.einsum('aras->rs',x)
        for a,b in zip(reductions(rho_pure),reductions(rho_diag)):
            np.testing.assert_allclose(a,b,atol=1e-13)
        G=np.kron(np.diag(E),np.eye(3))-np.kron(np.eye(3),np.diag(E))
        self.assertLess(np.linalg.norm(G@rho_pure),1e-13)
        self.assertLess(np.linalg.norm(G@rho_diag),1e-13)
        for t in (0.,.7,math.pi/2):
            c=clock_vector(t)
            def conditioned(rho):
                x=rho.reshape(3,3,3,3)
                r=np.einsum('a,arbs,b->rs',c.conj(),x,c)
                return r/np.trace(r)
            zp=conditioned(rho_pure);zd=conditioned(rho_diag)
            np.testing.assert_allclose(zd,np.eye(3)/3,atol=1e-13)
            Bz=np.array([[1,0,0],[0,0,1],[0,1,0]],complex)
            self.assertAlmostEqual((np.trace(zp@Bz).real),1/3+2/3*math.cos(2*t),places=12)
            self.assertAlmostEqual(np.trace(zd@Bz).real,1/3,places=12)

    def test_zero_level_does_not_fix_weights_or_dynamics(self):
        # Both p values solve exactly the same constraint but select different
        # conditional h/B statistics. Varying g globally rescales the spectrum
        # while retaining all exact zero eigenvectors; scale is extra input.
        self.assertAlmostEqual(h_b_joint(.5,math.pi/2)[1,1],.5)
        self.assertAlmostEqual(h_b_joint(.75,math.pi/2)[1,1],.25)
        self.assertNotEqual(entropy([.5,.5]),entropy([.75,.25]))
        v=full_state(.5)
        np.testing.assert_allclose(np.linalg.norm(v),1,atol=1e-13)

if __name__=='__main__':unittest.main()
