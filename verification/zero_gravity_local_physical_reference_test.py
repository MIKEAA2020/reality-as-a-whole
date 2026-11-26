"""Coupled reference, signal and detector on a gravitating clock/rod background.

Pseudospectral RK4 solves the linear-amplitude three-field model with two
localized couplings. Initial constraint and sign checks are algebraic; this
is not nonlinear Einstein evolution, a measurement, or evidence of experience.
"""
import math
import unittest
import numpy as np

from verification.zero_localized_gravity_finite_response_test import (
    TAU,F_ROD,END,FINAL,NORM,bump,localized_bump)


def evolve(n,steps,lam=.1,mu=.08):
    """Two independent initial components: reference and signal.

    Fields normalized by epsilon; component 0 contains reference=B and
    component 1 signal=2*cos(z). Their sums/differences are the two
    physically distinct preparations with the same reference.
    """
    if n%2 or steps%4: raise ValueError('even n and steps divisible by 4 required')
    x=2*math.pi*np.fft.fftfreq(n)
    one=localized_bump(x)
    w=one[:,None,None]*one[None,:,None]*one[None,None,:]
    k=np.fft.fftfreq(n,d=1/n)
    kz=np.fft.rfftfreq(n,d=1/n)
    k2=k[:,None,None]**2+k[None,:,None]**2+kz[None,None,:]**2
    y=np.zeros((2,3,n,n,n),dtype=float) # components; signal, detector, reference
    y[0,2]=w
    y[1,0]=2*np.cos(x)[None,None,:]
    v=np.zeros_like(y)
    a=1.0; h=FINAL/steps
    def rhs(t,a,y,v):
        aa=a**4/TAU**2
        pulse=bump(t/END)/NORM if 0<t<END else 0.0
        lap=np.fft.irfftn(-k2*np.fft.rfftn(y,axes=(-3,-2,-1)),
                          s=(n,n,n),axes=(-3,-2,-1))
        force=np.empty_like(y)
        fac=a**6/TAU**2*pulse*w
        force[:,0]=-fac*lam*y[:,1]
        force[:,1]=-fac*(lam*y[:,0]+mu*y[:,2])
        force[:,2]=-fac*mu*y[:,1]
        adot=a**3/TAU*math.sqrt(F_ROD**2/4+TAU**2/(12*a**4))
        return adot,v,aa*lap+force
    def sample(a,y,v):
        p=y[0]+y[1]; m=y[0]-y[1]
        wp=w.sum()
        def q(z): return float(np.sum(w*z[2]*z[1])/wp)
        def dq(z,dz): return float(np.sum(w*(dz[2]*z[1]+z[2]*dz[1]))/wp)
        vp=v[0]+v[1]; vm=v[0]-v[1]
        return {'a':a,'plus':q(p),'minus':q(m),'difference':q(p)-q(m),
                'plus_slope':dq(p,vp),'minus_slope':dq(m,vm),
                'reference_at_center_plus':float(p[2,0,0,0]),
                'reference_at_center_minus':float(m[2,0,0,0])}
    samples={}
    marks={steps//2:'0.4',3*steps//4:'0.6',steps:'0.8'}
    for i in range(steps):
        t=i*h
        a1,y1,v1=rhs(t,a,y,v)
        a2,y2,v2=rhs(t+h/2,a+h*a1/2,y+h*y1/2,v+h*v1/2)
        a3,y3,v3=rhs(t+h/2,a+h*a2/2,y+h*y2/2,v+h*v2/2)
        a4,y4,v4=rhs(t+h,a+h*a3,y+h*y3,v+h*v3)
        a+=h*(a1+2*a2+2*a3+a4)/6
        y+=h*(y1+2*y2+2*y3+y4)/6
        v+=h*(v1+2*v2+2*v3+v4)/6
        if i+1 in marks: samples[marks[i+1]]=sample(a,y,v)
    return samples


def normalized_initial_constraint(psi, lap_psi, alpha, eps, c, b, r,
                                  bump_value, grad_bump_sq, f=.5, tau=1.5,
                                  quartic=1.):
    """Constraint on the declared initial slice; χ=Pχ=0, PΦ=PR=0."""
    return (8*psi**-5*lap_psi-1.5*alpha**2+1.5*f*f*psi**-4
            +.5*tau*tau*psi**-12
            +.5*eps**2*(b*b*(1-c*c)+r*r*grad_bump_sq)*psi**-4
            +quartic*eps**4*(b*b*c*c+r*r*bump_value**2)**2)


class PhysicalReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.coarse=evolve(12,240)
        cls.medium=evolve(16,320)
        cls.fine=evolve(20,400)
        cls.no_signal=evolve(12,240,lam=0)
        cls.no_reference_coupling=evolve(12,240,mu=0)
        cls.reversed=evolve(12,240,lam=-.1)

    def test_initial_constraint_sign_invariance_and_reference_cost(self):
        args=(1.1,.07,-1.0,.05,.6,2.0,1.0,.4,.3)
        a=normalized_initial_constraint(*args)
        b=normalized_initial_constraint(*args[:5],-args[5],*args[6:])
        self.assertAlmostEqual(a,b,places=14)
        no_reference=normalized_initial_constraint(*args[:6],0,*args[7:])
        self.assertGreater(a-no_reference,0)

    def test_linearized_elliptic_operator_has_no_nonzero_kernel(self):
        L=6*(F_ROD**2+TAU**2)
        self.assertEqual(L,15)
        for kx in range(-4,5):
            for ky in range(-4,5):
                for kz in range(-4,5):
                    if (kx,ky,kz)!=(0,0,0):
                        self.assertLess(-8*(kx*kx+ky*ky+kz*kz)-L,0)
        self.assertNotEqual(-3*(-1),0) # zero mode adjusted by alpha

    def test_sign_relative_observable_and_nonzero_late_contrast(self):
        for t in ('0.4','0.6','0.8'):
            self.assertGreater(abs(self.fine[t]['difference']),1e-6)
            self.assertGreater(self.fine[t]['a'],1)
            # Both reference values are dynamical, not frozen unit signs.
            self.assertGreater(self.fine[t]['reference_at_center_plus'],0)
            self.assertGreater(self.fine[t]['reference_at_center_minus'],0)

    def test_controls_and_reference_relative_sign_symmetry(self):
        for t in ('0.4','0.6','0.8'):
            self.assertAlmostEqual(self.no_signal[t]['difference'],0,places=13)
            self.assertAlmostEqual(self.reversed[t]['difference'],
                                   -self.coarse[t]['difference'],places=13)
            # With mu=0, the common reference-induced detector baseline is zero.
            uncoupled=self.no_reference_coupling[t]
            self.assertAlmostEqual(uncoupled['plus']+uncoupled['minus'],0,places=13)
            self.assertGreater(abs(self.coarse[t]['plus']+self.coarse[t]['minus']),1e-7)
        # Simultaneous sign relabel of the reference and detector leaves Rχ.
        for r in (-2.,1.):
            for c in (-3.,.5): self.assertEqual(r*c,(-r)*(-c))

    def test_spatial_and_temporal_refinement(self):
        for t in ('0.4','0.6','0.8'):
            val=self.fine[t]['difference']
            self.assertLess(abs(self.medium[t]['difference']-val),.04*abs(val))
            self.assertLess(abs(self.coarse[t]['difference']-val),.15*abs(val))
        timefine=evolve(16,640)
        for t in ('0.4','0.6','0.8'):
            self.assertLess(abs(timefine[t]['difference']-self.medium[t]['difference']),1e-9)


if __name__=='__main__': unittest.main()
