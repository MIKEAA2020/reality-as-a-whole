"""Exact clock-energy matching for the coupled recollapsing sphere model.

Finite Fock truncation and spectral energy rounding; an explicit construction,
not a gravitational total-energy theorem or a derivation of the whole state.
"""
import math
import unittest
import numpy as np
from verification.zero_recollapse_sphere_memory_test import Model,YV,SIGNS,entropy
from verification.zero_autonomous_two_window_records_test import mutual_information
from verification.zero_integrated_sphere_clock_experience_test import sphere

SHIFT=2.2


class BalancedRecollapse:
    def __init__(self,n=24,step=.02,prep='center',alpha=1.4):
        if step<=0:raise ValueError('positive energy spacing required')
        if prep not in ('center','blank'):raise ValueError('unknown preparation')
        self.m=Model(n,alpha=alpha);self.n=n;self.step=step;self.prep=prep
        self.rounded={};bins={}
        for h in (0,1):
            delta=math.pi*h/2 if prep=='center' else 0.
            initial=self.m.state(h,0.,delta,pointer='zero')
            for s1 in SIGNS:
                for s2 in SIGNS:
                    for sb in SIGNS:
                        key=(h,s1,s2,sb)
                        y1,y2,yb=(YV[:,(s+1)//2] for s in (s1,s2,sb))
                        coeff=np.einsum('i,j,k,ndijk->nd',y1.conj(),y2.conj(),yb.conj(),initial).ravel()
                        val,U=self.m.spec[key]
                        ticks=np.rint((val+SHIFT)/step).astype(int)
                        if ticks.min()<0:raise ValueError('energy offset insufficient')
                        self.rounded[key]=(ticks,U)
                        weights=(U.conj().T@coeff)*(1 if h==0 else 1j)/math.sqrt(2)
                        for j,k in enumerate(ticks):
                            v=weights[j]*np.einsum('nd,i,j,k->ndijk',U[:,j].reshape(n,2),y1,y2,yb)
                            if k not in bins:bins[k]=np.zeros((2,n,2,2,2,2),complex)
                            bins[k][h]+=v
        self.ticks=np.array(sorted(bins));self.bins=np.array([bins[k] for k in self.ticks])
        self.weights=np.sum(abs(self.bins)**2,axis=(1,2,3,4,5,6))
        self.energies=step*self.ticks
        self.period=2*math.pi/step

    def conditional(self,t):
        return np.einsum('k,k...->...',np.exp(1j*self.energies*t),self.bins)

    def quantized_apply(self,v):
        out=np.zeros_like(v)
        for h in (0,1):
            for s1 in SIGNS:
                for s2 in SIGNS:
                    for sb in SIGNS:
                        y1,y2,yb=(YV[:,(s+1)//2] for s in (s1,s2,sb))
                        vchan=np.einsum('i,j,k,ndijk->nd',y1.conj(),y2.conj(),yb.conj(),v[h]).ravel()
                        ticks,U=self.rounded[h,s1,s2,sb]
                        w=(U@((self.step*ticks)*(U.conj().T@vchan))).reshape(self.n,2)
                        out[h]+=np.einsum('nd,i,j,k->ndijk',w,y1,y2,yb)
        return out

    def original(self,t):
        v=[]
        for h in (0,1):
            delta=math.pi*h/2 if self.prep=='center' else 0.
            v.append((1 if h==0 else 1j)*np.exp(1j*SHIFT*t)*self.m.state(h,-t,delta,pointer='zero')/math.sqrt(2))
        return np.array(v)

    def stats(self,t=None,dephased=False):
        # A dephased whole has one unnormalized rest vector per clock bin;
        # a phase POVM multiplies each by a phase that cancels in its density.
        if t is None:
            states=self.bins
        elif dephased:
            phases=np.exp(1j*self.energies*t).reshape(-1,1,1,1,1,1,1)
            states=phases*self.bins
        else:
            states=self.conditional(t)[None,...]
        joint=np.sum(abs(states)**2,axis=(0,2,3,4,5))
        mb=states.reshape(-1,2)
        rhoB=mb.T@mb.conj()
        mg=states.transpose(2,0,1,3,4,5,6).reshape(self.n,-1)
        rhoG=mg@mg.conj().T
        return {'a':np.trace(rhoG@self.m.scale).real,'SG':entropy(rhoG),
                'SB':entropy(rhoB),'mi':mutual_information(joint),'joint':joint,
                'rhoB':rhoB,'rhoG':rhoG}


class ZeroEnergyRecollapseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a=BalancedRecollapse(24,.02,'center')
        cls.b=BalancedRecollapse(24,.02,'blank')

    def test_explicit_zero_eigenstate_and_positive_energy_ledger(self):
        a=self.a
        self.assertGreaterEqual(min(a.ticks),0)
        self.assertAlmostEqual(sum(a.weights),1,places=11)
        # Orthogonality of different binned energy eigenvectors, including
        # bins that gather a degenerate eigenspace.
        V=a.bins.reshape(len(a.ticks),-1)
        gram=V.conj()@V.T
        self.assertLess(np.linalg.norm(gram-np.diag(a.weights)),1e-12)
        for idx in range(len(a.ticks)):
            v=a.bins[idx]
            self.assertLess(np.linalg.norm(a.quantized_apply(v)-a.energies[idx]*v),1e-11)
        # All elementary spectral components have exactly the matching clock
        # tick; this algebraic construction is independent of the test samples.
        for key,(ticks,U) in a.rounded.items():
            original=a.m.spec[key][0]+SHIFT
            self.assertLessEqual(np.max(abs(a.step*ticks-original)),a.step/2+1e-14)
            self.assertLess(np.linalg.norm(U.conj().T@U-np.eye(len(ticks))),1e-11)
        self.assertGreater(np.dot(a.energies,a.weights),1)

    def test_clock_povm_normalizes_for_all_populated_ticks(self):
        # Integral of exp(i(k-l)δt) over period vanishes exactly for k!=l.
        d=self.a.ticks[:,None]-self.a.ticks[None,:]
        off=d!=0
        integral=np.ones(d.shape,complex)
        integral[off]=(np.exp(2j*math.pi*d[off])-1)/(2j*math.pi*d[off])
        self.assertLess(np.max(abs(integral-np.eye(len(d)))),1e-12)
        for t in (-2.,-1.,0.,1.,2.):
            self.assertAlmostEqual(np.linalg.norm(self.a.conditional(t)),1,places=11)

    def test_rounding_closeness_to_original_model(self):
        for model in (self.a,self.b):
            for t in (-2.,-1.,0.,1.,2.):
                diff=np.linalg.norm(model.conditional(t)-model.original(t))
                self.assertLessEqual(diff,abs(t)*model.step/2+1e-12)
        # Even a more refined rounding returns a closer state; no need to
        # pretend the rounding is the original local Hamiltonian.
        fine=BalancedRecollapse(24,.01,'center')
        self.assertLess(np.linalg.norm(fine.conditional(2)-fine.original(2)),.01)

    def test_same_geometry_opposite_seeded_blank_memory_arrows(self):
        prevx=prevy=None
        for t in (0.,.5,1.,1.5,2.):
            x=self.a.stats(t);y=self.b.stats(t)
            self.assertLess(np.linalg.norm(x['rhoG']-y['rhoG']),1e-12)
            self.assertAlmostEqual(x['SG'],y['SG'],places=10)
            for mod,positive in ((self.a,x),(self.b,y)):
                negative=mod.stats(-t)
                for k in ('a','mi','SB','SG'):
                    self.assertAlmostEqual(positive[k],negative[k],places=10)
            if prevx is not None:
                self.assertLess(x['a'],prevx['a'])
                self.assertLess(x['mi'],prevx['mi'])
                self.assertGreater(y['mi'],prevy['mi'])
                self.assertGreater(x['SG'],prevx['SG'])
            prevx,prevy=x,y
        np.testing.assert_allclose(self.a.weights,self.b.weights,atol=1e-13)
        np.testing.assert_array_equal(self.a.ticks,self.b.ticks)

    def test_same_marginals_but_dephased_history_is_static(self):
        a=self.a;deph=a.stats(None)
        self.assertGreater(abs(a.stats(0)['a']-a.stats(2)['a']),.9)
        self.assertGreater(abs(a.stats(0)['a']-deph['a']),.1)
        self.assertGreater(abs(a.stats(0)['mi']-deph['mi']),.1)
        # Trace out clock: both whole density operators have rest reduction
        # sum_k |v_k><v_k|. Trace out orthogonal rest bins: both clock
        # reductions are diag(weights). Dephasing preserves these exactly.
        for t in (-2.,-1.,0.,1.,2.):
            p=np.exp(1j*a.energies*t)
            self.assertAlmostEqual(float(np.sum(a.weights*abs(p)**2)),1,places=11)
            x=a.stats(t,dephased=True)
            for key in ('a','mi','SB','SG'):
                self.assertAlmostEqual(x[key],deph[key],places=11)
            np.testing.assert_allclose(x['rhoG'],deph['rhoG'],atol=1e-13)
            np.testing.assert_allclose(x['joint'],deph['joint'],atol=1e-13)

    def test_actual_five_ray_confined_record_does_not_see_memory(self):
        s=sphere('triple')
        for model in (self.a,self.b):
            for t in (0.,1.,2.):
                u=model.conditional(t)
                whole=np.einsum('habirw,hndmjk->abirwndmjk',s,u)
                mat=whole.transpose(3,9,0,1,2,4,5,6,7,8).reshape(8,-1)
                rho=mat@mat.conj().T
                expected=np.kron(np.diag([0,.5,.5,0]),model.stats(t)['rhoB'])
                self.assertLess(np.linalg.norm(rho-expected),1e-11)

    def test_cutoff_convergence_of_observables(self):
        other=BalancedRecollapse(32,.02,'center')
        for t in (0.,1.,2.):
            x=self.a.stats(t);y=other.stats(t)
            for k in ('a','mi','SB','SG'):
                self.assertLess(abs(x[k]-y[k]),2e-4,(t,k,x[k],y[k]))

if __name__=='__main__':unittest.main()
