"""Backreacting oscillator geometry coupled to the actual sphere h-code.

Finite Fock truncations, ideal internal clock, and deliberately chosen dynamics.
No assumption of irreversible records, experiencing qubits, or GR derivation.
"""
import math
import unittest
import numpy as np
from verification.zero_integrated_sphere_clock_experience_test import sphere, gram_ir
from verification.zero_autonomous_two_window_records_test import mutual_information

I=np.eye(2,dtype=complex)
Y=np.array([[0,-1j],[1j,0]],complex)
P=np.diag([0.,1.]).astype(complex)
PLUSY=np.array([1,1j])/math.sqrt(2)
YV=np.column_stack(([1,-1j],[1,1j]))/math.sqrt(2)  # columns s=-1,+1
SIGNS=(-1,1)


def entropy(rho):
    vals=np.linalg.eigvalsh((rho+rho.conj().T)/2)
    return -sum(float(x)*math.log2(float(x)) for x in vals if x>1e-14)


class Model:
    def __init__(self,n=24,alpha=-1.4,lam=.5,k1=.65,k2=.65,kb=.4):
        self.n=n; self.alpha=alpha
        a=np.diag(np.sqrt(np.arange(1,n)),1);q=(a+a.T)/math.sqrt(2)
        self.q=q; self.number=np.diag(np.arange(n,dtype=float))
        x,U=np.linalg.eigh(q)
        self.scale=(U*np.exp(.3*x))@U.T
        self.windows=[(U*np.exp(-.5*((x-c)/.7)**2))@U.T for c in (-1.,0.,1.)]
        self.ham={};self.spec={}
        for h in (0,1):
            for s1 in SIGNS:
                for s2 in SIGNS:
                    for sb in SIGNS:
                        w0,w1,w2=self.windows
                        H=np.kron(self.number,I)+h*np.eye(2*n)
                        H+=lam*np.kron(w0,Y)+np.kron(k1*s1*w1+k2*s2*w2,P)
                        H+=kb*h*sb*np.kron(w2,I)
                        self.ham[h,s1,s2,sb]=H
                        self.spec[h,s1,s2,sb]=np.linalg.eigh(H)
        coh=np.array([alpha**k/math.sqrt(math.factorial(k)) for k in range(n)],complex)
        self.coherent=coh/np.linalg.norm(coh)

    def state(self,h,t,delta=0.,pointer='y'):
        # Returns normalized conditional h state in oscillator,D,M1,M2,B basis.
        pointer_state=PLUSY if pointer=='y' else np.array([1.,0.])
        base=np.kron(self.coherent,pointer_state)
        out=np.zeros((self.n,2,2,2,2),complex)
        for s1 in SIGNS:
            for s2 in SIGNS:
                for sb in SIGNS:
                    val,U=self.spec[h,s1,s2,sb]
                    v=(U@(np.exp(-1j*t*val)*(U.conj().T@base))).reshape(self.n,2)
                    # M1,M2=0; B=cos δ|0>+sin δ|1> initially.
                    coeff=np.exp(-1j*sb*delta)/math.sqrt(8)
                    out+=coeff*np.einsum('nd,i,j,k->ndijk',v,YV[:,(s1+1)//2],YV[:,(s2+1)//2],YV[:,(sb+1)//2])
        return out

    def propagate(self,h,v,t):
        out=np.zeros_like(v)
        for s1 in SIGNS:
            for s2 in SIGNS:
                for sb in SIGNS:
                    y1,y2,yb=(YV[:,(s+1)//2] for s in (s1,s2,sb))
                    u=np.einsum('i,j,k,ndijk->nd',y1.conj(),y2.conj(),yb.conj(),v)
                    val,U=self.spec[h,s1,s2,sb]
                    w=(U@(np.exp(-1j*t*val)*(U.conj().T@u.ravel()))).reshape(self.n,2)
                    out+=np.einsum('nd,i,j,k->ndijk',w,y1,y2,yb)
        return out

    def sequential(self,t1,t2,prep='center'):
        # Projectively sample B_z at t1 and t2, including first-read backaction.
        table=np.zeros((2,2,2))
        pointer='y' if prep=='baseline' else 'zero'
        for h in (0,1):
            v=self.state(h,t1,math.pi*h/2 if prep=='center' else 0,pointer)
            for b in (0,1):
                w=np.zeros_like(v);w[...,b]=v[...,b]
                w=self.propagate(h,w,t2-t1)
                table[h,b,:]=np.sum(abs(w)**2,axis=(0,1,2,3))/2
        return table

    def observables(self,t,delta=0.,prep='baseline'):
        pointer='y' if prep=='baseline' else 'zero'
        vs=[self.state(h,t,(math.pi/2*h if prep=='center' else delta),pointer) for h in (0,1)]
        joint=np.array([np.sum(abs(v)**2,axis=(0,1,2,3))/2 for v in vs])
        rhoB=sum(v.reshape(-1,2).T@v.reshape(-1,2).conj()/2 for v in vs)
        rhoG=sum(v.reshape(self.n,-1)@v.reshape(self.n,-1).conj().T/2 for v in vs)
        return {'a':np.trace(rhoG@self.scale).real,'q':np.trace(rhoG@self.q).real,
                'joint':joint,'mi':mutual_information(joint),'SB':entropy(rhoB),
                'SG':entropy(rhoG),'rhoB':rhoB,'rhoG':rhoG,'states':vs}

    def find_t(self,target,lo,hi,delta=0.):
        f=lambda t:self.observables(t,delta)['a']-target
        flo=f(lo);fhi=f(hi)
        if flo*fhi>=0:raise ValueError((flo,fhi))
        for _ in range(38):
            mid=(lo+hi)/2;fm=f(mid)
            if flo*fm<=0:hi=mid
            else:lo=mid;flo=fm
        return (lo+hi)/2


class RecollapseSphereMemoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=Model(24)

    def test_constraint_hermitian_and_conserved_code(self):
        for H in self.m.ham.values():
            self.assertLess(np.linalg.norm(H-H.conj().T),1e-12)
        eps=1e-5
        for h in (0,1):
            for t in (.8,3.2):
                dv=(self.m.state(h,t+eps)-self.m.state(h,t-eps))/(2*eps)
                # Independent full action reconstructed in conserved Y channels.
                v=self.m.state(h,t); expected=np.zeros_like(v)
                for s1 in SIGNS:
                    for s2 in SIGNS:
                        for sb in SIGNS:
                            u=np.einsum('i,j,k,ndijk->nd',YV[:,(s1+1)//2].conj(),YV[:,(s2+1)//2].conj(),YV[:,(sb+1)//2].conj(),v)
                            hu=(self.m.ham[h,s1,s2,sb]@u.ravel()).reshape(self.m.n,2)
                            expected+=np.einsum('nd,i,j,k->ndijk',hu,YV[:,(s1+1)//2],YV[:,(s2+1)//2],YV[:,(sb+1)//2])
                self.assertLess(np.linalg.norm(-1j*dv+expected),1e-8)
                self.assertAlmostEqual(np.linalg.norm(v),1,places=12)

    def test_actual_sphere_state_and_record_reductions(self):
        v=sphere('triple');g=gram_ir(v)
        self.assertLess(np.linalg.norm(g[:,:,0,1]),1e-13)
        self.assertLess(np.linalg.norm(g[:,:,0,0]-g[:,:,1,1]),1e-13)
        for delta in (0.,math.pi/4):
            a=self.m.observables(2.2,delta)
            # Because sphere record cross operators vanish, its full reduction
            # factors from any conditional h-channel apparatus output.
            whole=np.einsum('habirw,hndmjk,h->abirwndmjk',v,np.array(a['states']),np.array([1,1j])/math.sqrt(2))
            mat=whole.transpose(3,9,0,1,2,4,5,6,7,8).reshape(8,-1)
            rho=mat@mat.conj().T
            self.assertLess(np.linalg.norm(rho-np.kron(np.diag([0,.5,.5,0]),a['rhoB'])),1e-12)
        m=Model(24,alpha=1.4)
        for prep in ('center','tilted'):
            a=m.observables(1.,prep=prep)
            whole=np.einsum('habirw,hndmjk,h->abirwndmjk',v,np.array(a['states']),np.array([1,1j])/math.sqrt(2))
            mat=whole.transpose(3,9,0,1,2,4,5,6,7,8).reshape(8,-1)
            self.assertLess(np.linalg.norm(mat@mat.conj().T-np.kron(np.diag([0,.5,.5,0]),a['rhoB'])),1e-12)

    def test_geometric_operator_positive_and_backreaction(self):
        self.assertGreater(np.linalg.eigvalsh(self.m.scale).min(),0)
        no=Model(24,lam=0,k1=0,k2=0,kb=0)
        for t in (0,.8,1.8,3.14,4.4,6.1):
            self.assertAlmostEqual(no.observables(t)['q'],math.sqrt(2)*self.m.alpha*math.cos(t),places=8)
        self.assertGreater(abs(self.m.observables(2.2)['q']-no.observables(2.2)['q']),.01)

    def test_same_scale_different_branches_and_boundary_states(self):
        target=1.1
        for delta in (0.,math.pi/4):
            left=self.m.find_t(target,.3,2.8,delta);right=self.m.find_t(target,3.5,6.2,delta)
            self.assertLess(left,3);self.assertGreater(right,3)
            L=self.m.observables(left,delta);R=self.m.observables(right,delta)
            self.assertAlmostEqual(L['a'],R['a'],places=10)
            self.assertGreater(abs(L['mi']-R['mi']),.005)
            self.assertGreater(abs(L['SB']-R['SB']),.005)
            dl=(self.m.observables(left+1e-5,delta)['a']-self.m.observables(left-1e-5,delta)['a'])/2e-5
            dr=(self.m.observables(right+1e-5,delta)['a']-self.m.observables(right-1e-5,delta)['a'])/2e-5
            self.assertGreater(dl,.5);self.assertLess(dr,-.5)
            for v in (L,R):
                variance=np.trace(v['rhoG']@self.m.scale@self.m.scale).real-v['a']**2
                self.assertGreater(math.sqrt(variance),.25)

    def test_target_memory_ideal_specificity_and_boundary_dependence(self):
        for t in (0.,1.,2.,4.,6.):
            x=self.m.observables(t,0.)
            self.assertLess(x['joint'][0,1],1e-25)
            self.assertAlmostEqual(x['joint'].sum(),1,places=12)
        # A different preparation of the same B and same H invalidates B=1 certification.
        x=self.m.observables(2.,math.pi/4)
        self.assertAlmostEqual(x['joint'][0,1],.25,places=12)

    def test_symmetric_turning_boundary_and_record_reversal_control(self):
        m=Model(24,alpha=1.4)
        # In every conserved Y channel the antiunitary is Z_D K.
        Z=np.diag([1.,-1.]);zd=np.kron(np.eye(m.n),Z)
        for H in m.ham.values():
            self.assertLess(np.linalg.norm(zd@H.conj()@zd-H),1e-12)
        # Both states and Hamiltonian are invariant under Z_D Z_M1 Z_M2 Z_B K
        # up to sector phases. Distinct center boundary preparations have
        # exactly the same geometry marginal, but opposite B/h correlations.
        center=m.observables(0,prep='center');blank=m.observables(0,prep='tilted')
        self.assertAlmostEqual(center['mi'],1,places=12)
        self.assertAlmostEqual(blank['mi'],0,places=12)
        self.assertAlmostEqual(center['SB'],1,places=12)
        self.assertAlmostEqual(blank['SB'],0,places=12)
        previous=center['a']; prev_c=center;prev_z=blank
        for t in (.5,1.,1.5,2.):
            a=m.observables(t,prep='center');z=m.observables(t,prep='tilted')
            back=m.observables(-t,prep='center')
            self.assertLess(a['a'],previous);previous=a['a']
            for key in ('a','mi','SB','SG'):
                self.assertAlmostEqual(a[key],back[key],places=11)
            self.assertLess(np.linalg.norm(a['rhoG']-z['rhoG']),1e-12)
            self.assertAlmostEqual(a['SG'],z['SG'],places=11)
            self.assertLess(a['mi'],prev_c['mi']);self.assertGreater(z['mi'],prev_z['mi'])
            self.assertLess(a['SB'],prev_c['SB']);self.assertGreater(z['SB'],prev_z['SB'])
            self.assertGreater(a['SG'],prev_c['SG'])
            prev_c=a;prev_z=z
        # Compare same specified model, same geometry state, opposite B arrows.
        c=m.observables(1.,prep='center');z=m.observables(1.,prep='tilted')
        self.assertAlmostEqual(c['mi'],.8372812,places=6)
        self.assertAlmostEqual(z['mi'],.0297655,places=6)

    def test_sequential_record_persistence_includes_backaction(self):
        m=Model(24,alpha=1.4)
        table=m.sequential(-1,0,prep='center')
        self.assertAlmostEqual(table.sum(),1,places=12)
        p=table.sum(axis=0)
        self.assertAlmostEqual(p[0,1]+p[1,0],.0291346965,places=7)
        # Measurement of B at -1 affects its distribution at the turning point.
        self.assertGreater(abs(p[:,1].sum()-m.observables(0,prep='center')['joint'][:,1].sum()),.05)
        self.assertLess(np.linalg.norm(m.propagate(1,m.state(1,.2),.7)-m.state(1,.9)),1e-12)

    def test_fock_refinement(self):
        bigger=Model(32)
        for t in (.8,2.2,3.2,4.5,6.1):
            for delta in (0.,math.pi/4):
                x=self.m.observables(t,delta);y=bigger.observables(t,delta)
                for key in ('a','q','mi','SB','SG'):
                    self.assertLess(abs(x[key]-y[key]),2e-5,(t,delta,key,x[key],y[key]))
                self.assertLess(np.linalg.norm(x['rhoB']-y['rhoB']),2e-5)
        c24=Model(24,alpha=1.4);c32=Model(32,alpha=1.4)
        for t in (-2.,-1.,0.,1.,2.):
            for prep in ('center','tilted'):
                x=c24.observables(t,prep=prep);y=c32.observables(t,prep=prep)
                for key in ('a','q','mi','SB','SG'):
                    self.assertLess(abs(x[key]-y[key]),2e-5,(t,prep,key))
        self.assertLess(np.linalg.norm(c24.sequential(-1,0)-c32.sequential(-1,0)),2e-5)

if __name__=='__main__':unittest.main()
