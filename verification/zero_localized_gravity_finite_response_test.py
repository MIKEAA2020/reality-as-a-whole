"""3D-localized, first-order detector response in the GR clock/rod model.

Fourier-collocation source and RK4 evolution of detector modes on the exact
homogeneous gravitating reference background. This is first order in field
amplitude and coupling, NOT nonlinear Einstein evolution or an actual record.
Requires numpy; no network or random data.
"""
import math
import unittest
import numpy as np

TAU=1.5
F_ROD=0.5
END=0.4
FINAL=0.8
WIDTH=1.4
B=2.0


def bump(s):
    if 0.0 < s < 1.0:
        return math.exp(-1.0/(s*(1.0-s)))
    return 0.0


def pulse_normalization(n=2000):
    # Simpson rule; n even.
    h=1.0/n
    return h/3.0*(sum((4 if i%2 else 2)*bump(i*h) for i in range(1,n)))

NORM=pulse_normalization()


def localized_bump(x):
    """Smooth periodic bump: x in [-pi,pi), support |x|<WIDTH."""
    out=np.zeros_like(x)
    mask=np.abs(x)<WIDTH
    v=x[mask]/WIDTH
    out[mask]=np.exp(1-1/(1-v*v))
    return out


def run(n,steps,lam=1.0, width=WIDTH):
    """Response to +epsilon*B*cos(z), divided by epsilon.

    Two signs with the same detector initialization have half-difference
    epsilon times this response, to first order in lambda and epsilon.
    Signal feedback, field-induced metric changes and nonlinearities omitted.
    """
    if width!=WIDTH: raise ValueError('WIDTH is part of this example')
    if n%2 or steps%4: raise ValueError('use even n and steps divisible by 4')
    x=2*math.pi*np.fft.fftfreq(n) # sample coordinates in [-pi,pi)
    one=localized_bump(x)
    w=one[:,None,None]*one[None,:,None]*one[None,None,:]
    source=w*np.cos(x)[None,None,:]
    shat=np.fft.fftn(source)/n**3
    what=np.fft.fftn(w)/n**3
    k=np.fft.fftfreq(n,d=1/n)
    k2=k[:,None,None]**2+k[None,:,None]**2+k[None,None,:]**2
    c=np.zeros((n,n,n),dtype=complex)
    d=np.zeros_like(c)
    a=1.0; u=1.0; du=0.0
    dt=FINAL/steps
    def rhs(t,a,u,du,c,d):
        pulse=bump(t/END)/NORM if 0<t<END else 0.0
        adot=a**3/TAU*math.sqrt(F_ROD**2/4+TAU**2/(12*a**4))
        return (adot,du,-a**4/TAU**2*u,d,
                -a**4/TAU**2*k2*c-lam*a**6/TAU**2*pulse*B*u*shat)
    def vals(t,a,u,du,c,d):
        point=np.sum(c)
        point_slope=np.sum(d)
        weighted=np.sum(c*np.conjugate(what))/what[0,0,0].real
        assert abs(point.imag)<1e-10 and abs(weighted.imag)<1e-10
        return {'a':a,'u':u,'point':point.real,'point_slope':point_slope.real,
                'local_weighted':weighted.real,'time':t}
    observations={}
    marks={steps//2:'0.4',3*steps//4:'0.6',steps:'0.8'}
    for i in range(steps):
        t=i*dt
        q1=rhs(t,a,u,du,c,d)
        q2=rhs(t+dt/2,a+dt*q1[0]/2,u+dt*q1[1]/2,du+dt*q1[2]/2,c+dt*q1[3]/2,d+dt*q1[4]/2)
        q3=rhs(t+dt/2,a+dt*q2[0]/2,u+dt*q2[1]/2,du+dt*q2[2]/2,c+dt*q2[3]/2,d+dt*q2[4]/2)
        q4=rhs(t+dt,a+dt*q3[0],u+dt*q3[1],du+dt*q3[2],c+dt*q3[3],d+dt*q3[4])
        a+=dt*(q1[0]+2*q2[0]+2*q3[0]+q4[0])/6
        u+=dt*(q1[1]+2*q2[1]+2*q3[1]+q4[1])/6
        du+=dt*(q1[2]+2*q2[2]+2*q3[2]+q4[2])/6
        c+=dt*(q1[3]+2*q2[3]+2*q3[3]+q4[3])/6
        d+=dt*(q1[4]+2*q2[4]+2*q3[4]+q4[4])/6
        if i+1 in marks:
            observations[marks[i+1]]=vals((i+1)*dt,a,u,du,c,d)
    return observations


class LocalizedFiniteResponseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.coarse=run(16,400)
        cls.middle=run(24,600)
        cls.fine=run(32,800)
        cls.zero=run(16,400,lam=0)
        cls.negative=run(16,400,lam=-1)

    def test_spatial_bump_is_localized_and_even(self):
        x=np.array([-math.pi,-WIDTH,0,WIDTH,math.pi])
        np.testing.assert_allclose(localized_bump(x),[0,0,1,0,0],atol=1e-15)
        x=np.linspace(-3,3,301)
        np.testing.assert_allclose(localized_bump(x),localized_bump(-x),atol=1e-15)
        self.assertEqual(bump(0),0); self.assertEqual(bump(1),0)
        self.assertGreater(bump(.5),0)

    def test_sign_difference_persists_after_pulse_on_sampled_window(self):
        for t in ('0.4','0.6','0.8'):
            self.assertLess(self.fine[t]['point'],-1e-5)
            self.assertLess(self.fine[t]['local_weighted'],-1e-5)
            self.assertGreater(self.fine[t]['u'],0)
        # This verifies samples only; it is not a stability theorem.

    def test_resolution_and_time_refinement(self):
        for t in ('0.4','0.6','0.8'):
            for key in ('point','local_weighted'):
                # Relative to the fine value; no rigorous continuum bound.
                v=self.fine[t][key]
                self.assertLess(abs(self.middle[t][key]-v),0.02*abs(v))
                self.assertLess(abs(self.coarse[t][key]-v),0.12*abs(v))
        twice=run(24,1200)
        for t in ('0.4','0.6','0.8'):
            self.assertLess(abs(twice[t]['point']-self.middle[t]['point']),1e-9)

    def test_zero_and_reversed_coupling(self):
        for t in ('0.4','0.6','0.8'):
            for key in ('point','local_weighted'):
                self.assertEqual(self.zero[t][key],0)
                self.assertAlmostEqual(self.coarse[t][key],-self.negative[t][key],places=13)

    def test_common_background_is_not_flat_spacetime(self):
        for t in ('0.4','0.6','0.8'):
            self.assertGreater(self.fine[t]['a'],1)


if __name__=='__main__': unittest.main()
