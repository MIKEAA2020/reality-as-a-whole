"""Perturbative local memory of the reference-relative gravity candidate.

Two clock-local profiles drive a new memory scalar at order epsilon squared.
Finite pseudospectral/RK4 evolution; no nonlinear Einstein evolution, physical
noise model, quantum measurement or experiential inference. Requires NumPy.
"""
import math
import unittest
import numpy as np

from verification.zero_localized_gravity_finite_response_test import (
    TAU,F_ROD,END,NORM,bump,localized_bump)

MEMORY_END=.6
FINAL=1.0


def evolve(n,steps,lam=.1,mu=.08,nu=1.0):
    """Return local memory difference basis for F0 and F1.

    Field system is leading order in epsilon, full in lambda and mu. Memory
    source is leading order epsilon²; no feedback or gravitational perturbations.
    Profiles F0=B(s)/I and F1=(2s-1)F0, s=(T-.4)/.2.
    """
    if n%2 or steps%10: raise ValueError('even n and steps divisible by 10')
    x=2*math.pi*np.fft.fftfreq(n); one=localized_bump(x)
    w=one[:,None,None]*one[None,:,None]*one[None,None,:]
    k=np.fft.fftfreq(n,d=1/n); kz=np.fft.rfftfreq(n,d=1/n)
    ksq=k[:,None,None]**2+k[None,:,None]**2+kz[None,None,:]**2
    # Common reference and differential signal, each (Phi,chi,sigma).
    y=np.zeros((2,3,n,n,n)); y[0,2]=w; y[1,0]=2*np.cos(x)[None,None,:]
    v=np.zeros_like(y)
    # Two independent memory responses to temporal basis profiles, each
    # already representing M_+ - M_- divided by epsilon².
    m=np.zeros((2,n,n,n)); d=np.zeros_like(m)
    a=1.; dt=FINAL/steps
    def lap(q):
        return np.fft.irfftn(-ksq*np.fft.rfftn(q,axes=(-3,-2,-1)),
                             s=(n,n,n),axes=(-3,-2,-1))
    def rhs(t,a,y,v,m,d):
        pulse1=bump(t/END)/NORM if 0<t<END else 0.
        q=(t-END)/(MEMORY_END-END)
        pulse2=bump(q)/NORM if 0<q<1 else 0.
        fac=a**6/TAU**2
        wave=a**4/TAU**2
        fy=np.empty_like(y)
        fy[:,0]=-fac*pulse1*w*lam*y[:,1]
        fy[:,1]=-fac*pulse1*w*(lam*y[:,0]+mu*y[:,2])
        fy[:,2]=-fac*pulse1*w*mu*y[:,1]
        # (sigma+ chi+ - sigma- chi-)/epsilon².
        contrast=2*(y[0,2]*y[1,1]+y[1,2]*y[0,1])
        base=-fac*nu*w*pulse2*contrast
        profiles=np.stack((base,(2*q-1)*base))
        return (a**3/TAU*math.sqrt(F_ROD**2/4+TAU**2/(12*a**4)),
                v,wave*lap(y)+fy,d,wave*lap(m)+profiles)
    def sample(a,m,d):
        return {'a':a,'value':np.sum(m*w,axis=(1,2,3))/w.sum(),
                'slope':np.sum(d*w,axis=(1,2,3))/w.sum(),
                'point':m[:,0,0,0].copy()}
    out={}; marks={round(steps*t/FINAL):str(t) for t in (.4,.6,.7,.8,.9,1.)}
    for i in range(steps):
        t=i*dt
        k1=rhs(t,a,y,v,m,d)
        k2=rhs(t+dt/2,*[z+dt*k/2 for z,k in zip((a,y,v,m,d),k1)])
        k3=rhs(t+dt/2,*[z+dt*k/2 for z,k in zip((a,y,v,m,d),k2)])
        k4=rhs(t+dt,*[z+dt*k for z,k in zip((a,y,v,m,d),k3)])
        a,y,v,m,d=[z+dt*(u+2*w2+2*w3+w4)/6
                     for z,u,w2,w3,w4 in zip((a,y,v,m,d),k1,k2,k3,k4)]
        if i+1 in marks: out[marks[i+1]]=sample(a,m,d)
    return out


def tuned(results):
    """Choose c so profile F0+cF1 has zero sampled local slope at T=.6."""
    s=results['0.6']['slope']
    if abs(s[1])<1e-14: raise ValueError('singular pulse basis')
    c=-s[0]/s[1]
    return c,{t:{name:float(v[name][0]+c*v[name][1])
                  for name in ('value','slope','point')}
              for t,v in results.items()}


class LocalMemoryPulseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.coarse=evolve(12,200)
        cls.medium=evolve(16,320)
        cls.fine=evolve(20,400)
        cls.no_signal=evolve(12,200,lam=0)
        cls.no_memory=evolve(12,200,nu=0)

    def test_no_memory_before_second_window(self):
        for key in ('value','slope','point'):
            np.testing.assert_allclose(self.fine['0.4'][key],[0,0],atol=1e-13)

    def test_tuned_profile_creates_nonzero_locally_stationary_difference(self):
        c,values=tuned(self.fine)
        self.assertTrue(math.isfinite(c))
        self.assertGreater(abs(values['0.6']['value']),1e-5)
        self.assertLess(abs(values['0.6']['slope']),1e-12)
        for t in ('0.7','0.8','0.9','1.0'):
            self.assertGreater(abs(values[t]['value']),1e-5)

    def test_pulse_and_signal_controls(self):
        for case in (self.no_signal,self.no_memory):
            for t in ('0.6','0.8','1.0'):
                np.testing.assert_allclose(case[t]['value'],[0,0],atol=1e-13)

    def test_fixed_fine_tuning_and_spatial_convergence(self):
        c,fine=tuned(self.fine)
        # Same physical pulse on all grids, not retuning each one.
        for t in ('0.6','0.8','1.0'):
            def val(r): return float(r[t]['value'][0]+c*r[t]['value'][1])
            self.assertLess(abs(val(self.medium)-fine[t]['value']),.08*abs(fine[t]['value']))
            self.assertLess(abs(val(self.coarse)-fine[t]['value']),.3*abs(fine[t]['value']))
        timefine=evolve(16,640)
        for t in ('0.6','0.8','1.0'):
            np.testing.assert_allclose(timefine[t]['value'],self.medium[t]['value'],atol=1e-9,rtol=0)

    def test_tuning_is_a_single_explicit_common_pulse(self):
        c,v=tuned(self.fine)
        # No claim that point and weighted-average slopes vanish simultaneously.
        self.assertNotEqual(c,0)
        self.assertNotEqual(v['0.6']['value'],0)
        self.assertNotEqual(v['1.0']['slope'],0)


if __name__=='__main__': unittest.main()
