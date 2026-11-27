"""A second, semibounded quantum clock for the same support instrument.

The clock POVM and product preparation are specified, not derived from zero.
The full continuum error bound is analytical; selected small-grid chiral
instrument evaluations and quadratures here are numerical controls.
"""
import math
import unittest
import numpy as np
from scipy.integrate import quad
from numpy.polynomial.legendre import leggauss

from verification.zero_two_window_autonomous_cursor_reader_test import (
    N,G,C,MASS,END,RET,error_bounds)
from verification.zero_two_window_cursor_instrument_test import (
    regulated_instrument,branch,target,trace_distance,channel_budget)

BAND=5000.
CENTER=10000.
BIN=1e-4
R=(END+RET)/2
SIGMA=math.sqrt((math.pi/(2*BAND))**2+BIN**2/12)


def scaled_clock_density(y):
    # In y=BAND*u units, density w(u)/BAND. np.sinc(z)=sin(pi*z)/(pi*z).
    s=np.sinc(y/math.pi-.5)+np.sinc(y/math.pi+.5)
    return float(s*s/(2*math.pi))


def tail_bound(r=R,bin_width=BIN):
    margin=min(r-END,RET-r)-bin_width/2
    Y=BAND*margin
    if Y<=math.pi/2: return 1.
    return min(1.,math.pi/(3*Y**3*(1-(math.pi/(2*Y))**2)**2))


def switch_bound():
    K,_,pulse,_=error_bounds()
    omega=math.sqrt(49/6+7.2/math.pi)
    eta=math.sin(G*1e-6)**N
    dynamical=N*G*C*(R**2+SIGMA**2)/2
    dispersion=K*(R+SIGMA)/(2*MASS)
    clock_uncertainty=omega*SIGMA
    return dynamical+pulse+dispersion+clock_uncertainty+tail_bound()+math.sqrt(2)*eta


class SecondClockTests(unittest.TestCase):
    def test_clock_profile_normalization_and_time_variance(self):
        # Frequency amplitude β(k) = cos(π(k-k0)/(2b))/sqrt(b).
        f=lambda x:math.cos(math.pi*x/2)
        fp=lambda x:-(math.pi/2)*math.sin(math.pi*x/2)
        self.assertAlmostEqual(quad(lambda x:f(x)**2,-1,1)[0],1.,places=13)
        self.assertAlmostEqual(quad(lambda x:fp(x)**2,-1,1)[0],math.pi**2/4,places=13)
        self.assertGreater(CENTER-BAND,0.)
        # Fourier density agrees with normalization up to an explicitly
        # bounded tail outside |y|=200.
        integr=quad(scaled_clock_density,-200,200,limit=1000)[0]
        y=200.;tail=math.pi/(3*y**3*(1-(math.pi/(2*y))**2)**2)
        self.assertLessEqual(abs(1-integr),tail+1e-10)

    def test_bin_convolution_tail_and_full_channel_budget(self):
        self.assertLess(SIGMA,.000316)
        self.assertGreater(BAND*(min(R-END,RET-R)-BIN/2),math.pi/2)
        bound=tail_bound()
        self.assertLess(bound,.0000177)
        self.assertLess(switch_bound(),.0394)
        self.assertLess(.01849+bound,.01851)
        # Numerical density tail lies below its analytic envelope bound.
        y=BAND*(min(R-END,RET-R)-BIN/2)
        tail=2*quad(scaled_clock_density,y,1000,limit=1000)[0]
        self.assertLess(tail,bound)

    def test_same_autonomous_instrument_under_clock_smearing(self):
        # Numerically sample a normalized Gaussian quadrature over a finite
        # window around r, not the full continuum/physical cursor model.
        nodes,weights=leggauss(9)
        sigma0=math.pi/(2*BAND)
        ts=R+nodes*4*sigma0
        self.assertGreater(ts.min(),END); self.assertLess(ts.max(),RET)
        ws=np.array([w*scaled_clock_density(BAND*(t-R)) for t,w in zip(ts,weights)])
        ws/=ws.sum()
        rho=np.array([[.5,.5],[.5,.5]],complex)
        out=[None,None]
        p_direct=np.zeros(2)
        for t,w in zip(ts,ws):
            vec,basis,U=regulated_instrument(output_time=float(t))
            for m in (0,1):
                x=branch(vec,rho,m)
                out[m]=w*x if out[m] is None else out[m]+w*x
                p_direct[m]+=w*np.trace(x).real
        np.testing.assert_allclose([np.trace(x).real for x in out],p_direct,atol=1e-13)
        self.assertAlmostEqual(sum(p_direct),1.,places=9)
        v0,b0,U0=regulated_instrument(output_time=R)
        ideal=[target(b0,U0,rho,m) for m in (0,1)]
        self.assertLess(sum(trace_distance(a,b) for a,b in zip(out,ideal)),switch_bound()+1e-9)
        sharp=[branch(v0,rho,m) for m in (0,1)]
        # Smearing is not a different measurement or a new initial state.
        self.assertLess(sum(trace_distance(a,b) for a,b in zip(out,sharp)),.01)

    def test_clock_neutral_effect_normalization_and_covariance(self):
        # A finite cyclic analogue controls the twirl algebra. This is NOT the
        # semibounded continuum clock or the interacting two-window model.
        n=8; I=np.eye(2); X=np.array([[0,1],[1,0]])
        shift=np.roll(np.eye(n),1,axis=0); U=np.kron(X,shift)
        E=np.zeros((n,n)); E[0,0]=1
        projectors=(np.diag([1.,0.]),np.diag([0.,1.]))
        effects=[]
        for p in projectors:
            f=np.zeros((2*n,2*n),complex)
            for t in range(n):
                Ut=np.linalg.matrix_power(U,t)
                f+=Ut.conj().T@np.kron(p,E)@Ut
            effects.append(f)
            np.testing.assert_allclose(f@U,U@f,atol=1e-14)
            self.assertGreaterEqual(np.linalg.eigvalsh(f).min(),-1e-14)
        np.testing.assert_allclose(sum(effects),np.eye(2*n),atol=1e-14)
        beta=np.zeros(n);beta[:2]=1/math.sqrt(2)
        psi=np.kron(np.array([1.,0.]),beta)
        probs=[float(np.vdot(psi,f@psi).real) for f in effects]
        np.testing.assert_allclose(probs,[.5,.5],atol=1e-14)

    def test_clock_smearing_is_not_a_sharp_reading_in_general(self):
        # A frequency gap equal to the clock bandwidth has characteristic
        # overlap 1/pi, not 1. This is a separate simple qubit control.
        overlap=quad(lambda x:math.cos(math.pi*x/2)*math.cos(math.pi*(x+1)/2),-1,0)[0]
        self.assertAlmostEqual(overlap,1/math.pi,places=13)
        self.assertLess(overlap,.4)


if __name__=='__main__':unittest.main()
