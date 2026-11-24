"""Targeted autonomous K-record in the integrated sphere/clock model.

Finite-grid Chebyshev propagation, with independent dense diagonalization.
The third memory is physical, not a selected outcome or experiencing subject.
"""
import math
import unittest
import numpy as np
from verification.zero_autonomous_two_window_records_test import make_model
from verification.zero_integrated_sphere_clock_experience_test import joint_k_mem,sphere
from verification.zero_two_window_continuum_slice_test import kernel,K

K3=.4
M=(1.3+math.sqrt(1.3**2+1))/2
LOW=4-2*(M+K3)
HIGH=49/6+2*(M+K3)


def initial(model):
    f=model[1];v=np.zeros((2,2,2,2,len(f)),complex)
    v[0,0,0,0]=f/math.sqrt(2);v[1,0,0,0]=1j*f/math.sqrt(2)
    return v


def theta(model,v,h,k3=K3):
    p,_,E,*_=model
    out=(p*p/6-2*h)*v
    w=np.einsum('pq,ijkbq->ijkbp',E[0],v,optimize=True)
    out[1,:,:,:]+=-1j*w[0,:,:,:];out[0,:,:,:]+=1j*w[1,:,:,:]
    w=np.einsum('pq,jkbq->jkbp',E[1],v[1],optimize=True)
    out[1,1,:,:]+=-1.3j*w[0,:,:];out[1,0,:,:]+=1.3j*w[1,:,:]
    w=np.einsum('pq,jkbq->jkbp',E[2],v[1],optimize=True)
    out[1,:,1,:]+=-1.3j*w[:,0,:];out[1,:,0,:]+=1.3j*w[:,1,:]
    if h:
        w=np.einsum('pq,ijkbq->ijkbp',E[2],v,optimize=True)
        out[:,:,:,1]+=-2j*k3*w[:,:,:,0]
        out[:,:,:,0]+= 2j*k3*w[:,:,:,1]
    return out


def evolve(model,h,t,k3=K3,degree=400,quad=900):
    mid=(LOW+HIGH)/2;radius=(HIGH-LOW)/2
    th=math.pi*(np.arange(quad)+.5)/quad
    coeff=(2/quad)*(np.cos(np.outer(np.arange(degree),th))@np.exp(1j*t*np.sqrt(mid+radius*np.cos(th))))
    def x(v):return (theta(model,v,h,k3)-mid*v)/radius
    a=initial(model);b=x(a);out=coeff[0]*a/2+coeff[1]*b
    for k in range(2,degree):
        a,b=b,2*x(b)-a
        out+=coeff[k]*b
    return out


def joint(model,t,k3=K3,degree=400):
    # h, M1, M2, targeted-memory B; h priors 1/2.
    return np.array([np.sum(abs(evolve(model,h,t,k3,degree))**2,axis=(0,4)) for h in (0,1)])/2


def mi_h_b(j):
    p=j.sum(axis=(1,2));a=p.sum(axis=1);b=p.sum(axis=0)
    return sum(x*math.log2(x/(a[i]*b[k])) for (i,k),x in np.ndenumerate(p) if x>1e-16)


class IntegratedTargetedMemoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model=make_model(80)
        cls.j30=joint(cls.model,30);cls.j100=joint(cls.model,100)

    def test_positive_bound_and_hermiticity(self):
        self.assertGreater(LOW,.25)
        rng=np.random.default_rng(9);shape=(2,2,2,2,80)
        a=rng.normal(size=shape)+1j*rng.normal(size=shape)
        b=rng.normal(size=shape)+1j*rng.normal(size=shape)
        for h in (0,1):
            self.assertLess(abs(np.vdot(a,theta(self.model,b,h))-np.vdot(theta(self.model,a,h),b)),1e-10)

    def test_independent_dense_propagation(self):
        model=make_model(12);n=12;dim=16*n
        eye=np.eye(dim,dtype=complex)
        for h in (0,1):
            mat=np.column_stack([theta(model,eye[:,j].reshape(2,2,2,2,n),h).ravel() for j in range(dim)])
            self.assertLess(np.linalg.norm(mat-mat.conj().T),1e-12)
            e,U=np.linalg.eigh(mat);self.assertGreater(e.min(),LOW)
            expected=U@(np.exp(1j*100*np.sqrt(e))*(U.conj().T@initial(model).ravel()))
            actual=evolve(model,h,100).ravel()
            self.assertLess(np.linalg.norm(expected-actual),2e-10)

    def test_convergence_degree_and_unitarity(self):
        for h in (0,1):
            a=evolve(self.model,h,100,degree=400);b=evolve(self.model,h,100,degree=500)
            self.assertLess(np.linalg.norm(a-b),1e-10)
            self.assertAlmostEqual(np.vdot(a,a).real,1,places=10)

    def test_h0_target_memory_never_fires(self):
        for j in (self.j30,self.j100):self.assertLess(j[0,:,:,1].sum(),1e-20)

    def test_tag_and_memory_backaction(self):
        j=self.j100
        hb=j.sum(axis=(1,2))
        self.assertAlmostEqual(hb[1,1],.3893561718349807,places=10)
        self.assertAlmostEqual(mi_h_b(j),.5831269237685011,places=10)
        self.assertAlmostEqual(hb[1,1]/hb[:,1].sum(),1,places=12)
        self.assertAlmostEqual(hb[1,0]/hb[:,0].sum(),.1811920845863673,places=10)
        old=joint_k_mem(self.model,100).sum(axis=0)
        tv=np.sum(abs(j.sum(axis=(0,3))-old))/2
        self.assertAlmostEqual(tv,.0153870159332046,places=10)

    def test_finite_interval_persistence_not_infinite(self):
        late=joint(self.model,150,degree=500)
        self.assertLess(np.max(abs(late.sum(axis=(1,2))-self.j100.sum(axis=(1,2)))),.00002)

    def test_new_channel_uniform_hilbert_schmidt_bound(self):
        l0=math.sqrt(28/3)/math.pi;l5=math.sqrt(328/3)/math.pi
        bound=(2*l5*l5+(.8*l5)**2+(1.3*l0+2.1*l5)**2)/4
        self.assertAlmostEqual(bound,24.342154385783065,places=11)
        self.assertLess(bound,25)
        p=self.model[0];dp=1/len(p)
        for k in (-7,-6.79,-6.503,-6.21,-6):
            for m1 in (-1,1):
                for m2 in (-1,1):
                    for b in (-1,1):
                        def potential(x):
                            base=kernel(x,p,m1,m2)
                            d=x[:,None]-p[None,:]
                            return base-.8*b*(K(d)*np.exp(-5j*d))[:,:,None,None]*np.eye(2)
                        D=(potential(p)-potential(np.array([k])))/((p*p-k*k)/6)[:,None,None,None]
                        self.assertLess(dp*dp*np.sum(abs(D)**2),bound)

    def test_actual_sphere_state_with_targeted_memory_and_record(self):
        vs=np.array([evolve(self.model,h,100) for h in (0,1)])
        c=np.array([1,1j])/math.sqrt(2)
        whole=np.einsum('habirw,hdmntp,h->abirwdmntp',sphere('triple'),vs,c,optimize=True)
        self.assertAlmostEqual(np.linalg.norm(whole),1,places=10)
        # r and B probabilities from the actual full state.
        rb=np.sum(abs(whole)**2,axis=(0,1,2,4,5,6,7,9))
        self.assertAlmostEqual(rb[1,1],.19467808591749,places=10)
        self.assertAlmostEqual(rb[2,1],rb[1,1],places=12)
        # Full reduced state on R and all three memory qubits factors.
        V=whole.transpose(3,6,7,8,0,1,2,4,5,9).reshape(32,-1)
        rho=V@V.conj().T
        mem=sum(np.einsum('dmnbp,dklcp->mnbklc',v,v.conj()).reshape(8,8)/2 for v in vs)
        self.assertLess(np.linalg.norm(rho-np.kron(np.diag([0,.5,.5,0]),mem)),1e-12)

    def test_zero_coupling_reproduces_previous(self):
        got=joint(self.model,100,k3=0).sum(axis=3)
        self.assertLess(np.max(abs(got-joint_k_mem(self.model,100))),1e-11)

    def test_grid_convergence(self):
        a=joint(make_model(40),100);b=self.j100;c=joint(make_model(160),100)
        self.assertLess(abs(mi_h_b(a)-mi_h_b(b)),.001)
        self.assertLess(abs(mi_h_b(b)-mi_h_b(c)),.001)

if __name__=='__main__':unittest.main()
