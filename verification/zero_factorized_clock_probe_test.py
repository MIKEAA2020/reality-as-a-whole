"""A factorwise clock/memory probe: finite controls and bound constants.

The continuum derivation and limitations are in
ZERO_FACTORWISE_CLOCK_MEMORY_PROBE.md. The matrix tests do not simulate the
full massive two-window apparatus or prove the continuum inequalities.
"""
import math
import unittest
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.linalg import expm
from numpy.polynomial.legendre import leggauss
from verification.zero_two_window_cursor_instrument_test import regulated_instrument, branch
from verification.zero_two_window_autonomous_cursor_reader_test import (
    END, RET, MASS, error_bounds)
from verification.zero_two_window_second_clock_test import (
    BAND, CENTER, BIN, R, tail_bound, scaled_clock_density)

A=WIDTH=1e-10
MASS_PROBE=1e30
T_OUT=R+A+WIDTH
PAULIY=np.array([[0.,-1j],[1j,0.]])


def clock_hit_lower():
    y=BAND*BIN/2
    return (BAND*BIN)*8/math.pi**3*math.cos(y)**2


def budgets():
    old_K,*_=error_bounds()
    old_memory_commutator=(math.pi/2)**2*15/(16*1e-6)
    clock_commutator=math.pi*BAND
    impulse=(A+WIDTH)*(old_memory_commutator+clock_commutator)
    strength=math.pi
    d1=strength*15/(8*WIDTH)
    d2=strength*10/(math.sqrt(3)*WIDTH**2)+d1*d1
    K=(math.sqrt(63/2)/A**2+2*math.sqrt(3)/A*d1+d2)
    dispersion=T_OUT*K/(2*MASS_PROBE)
    old_readout=old_K*(R+RET)/(2*MASS)+tail_bound()
    conditional=2*(impulse+dispersion)/clock_hit_lower()+old_readout
    return impulse,dispersion,old_readout,conditional,K


def clock_matrix(n):
    # Midpoint Nyström approximation on [k0-b,k0+b].  This is a quadrature
    # control, not the exact compressed operator or a convergence proof.
    dk=2*BAND/n
    k=CENTER-BAND+(np.arange(n)+.5)*dk
    diff=k[:,None]-k[None,:]
    E=dk*BIN/(2*math.pi)*np.sinc(diff*BIN/(2*math.pi))
    beta=np.sqrt(dk/BAND)*np.cos(math.pi*(k-CENTER)/(2*BAND))
    return k,E,beta


def theta(E):
    vals,V=np.linalg.eigh(E)
    if vals.min() < -1e-10 or vals.max()>1+1e-10: raise ValueError('not an effect')
    return (V*np.arcsin(np.sqrt(np.clip(vals,0,1))))@V.conj().T


def probe_unitary(H,G,offset=0.):
    # Prescribed central chiral cursor trajectory, interaction picture relative
    # to the pulse center; the full massive-cursor claim is analytical.
    n=len(H);ds=2*n
    def f(u):
        z=u+offset
        return 15/16*(1-z*z)**2 if abs(z)<=1 else 0.
    h,V=np.linalg.eigh(H)
    Ge=V.conj().T@G@V
    def rhs(u,y):
        phases=np.exp(-1j*h*(WIDTH*u))
        gt=V@(phases[:,None]*Ge*phases.conj()[None,:])@V.conj().T
        a=np.kron(gt,PAULIY)
        return (1j*f(u)*a@y.reshape(ds,ds)).ravel()
    result=solve_ivp(rhs,(-2,2),np.eye(ds,dtype=complex).ravel(),
                     method='DOP853',rtol=1e-10,atol=1e-12,max_step=.08)
    if not result.success:raise RuntimeError(result.message)
    return result.y[:,-1].reshape(ds,ds)


class FactorwiseProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.k,cls.E,cls.beta=clock_matrix(24)
        cls.theta=theta(cls.E)

    def test_error_budget_and_calibration_window(self):
        impulse,disp,old,conditional,K=budgets()
        self.assertGreater(R-A-WIDTH,END)
        self.assertLess(T_OUT,RET)
        self.assertLess(impulse+disp,.000466)
        self.assertLess(old,.000110)
        self.assertGreater(clock_hit_lower(),.121)
        self.assertLess(conditional,.00781)
        self.assertLess(K,7.886e21)
        self.assertGreater(MASS_PROBE,0)
        actual=quad(scaled_clock_density,-BAND*BIN/2,BAND*BIN/2)[0]
        self.assertGreater(actual,clock_hit_lower())
        self.assertAlmostEqual(actual,.12849858094167343,places=12)

    def test_clock_effect_and_no_reading_are_complete(self):
        E=self.E;vals=np.linalg.eigvalsh(E)
        self.assertGreater(vals.min(),-1e-12)
        self.assertLess(vals.max(),1.)
        np.testing.assert_allclose(expm(1j*np.kron(self.theta,PAULIY))[1::2,0::2].conj().T@
                                   expm(1j*np.kron(self.theta,PAULIY))[1::2,0::2],E,atol=2e-13)
        no=np.eye(len(E))-E
        self.assertGreater(np.linalg.eigvalsh(no).min(),0.)
        self.assertAlmostEqual(np.vdot(self.beta,self.beta).real,1.,places=13)
        exact=quad(scaled_clock_density,-BAND*BIN/2,BAND*BIN/2)[0]
        e12=abs(np.vdot(clock_matrix(12)[2],clock_matrix(12)[1]@clock_matrix(12)[2]).real-exact)
        e24=abs(np.vdot(self.beta,E@self.beta).real-exact)
        k48,E48,b48=clock_matrix(48)
        e48=abs(np.vdot(b48,E48@b48).real-exact)
        self.assertGreater(e12,e24);self.assertGreater(e24,e48)
        self.assertLess(e48,5e-5)

    def test_two_actual_factor_gates_and_finite_pulse_error(self):
        # Memory Hamiltonian saturates the relevant scalar commutator bound;
        # the finite clock is a separate Nyström control of the band effect.
        h=(math.pi/2)*15/(16*1e-6)
        Hm=h*PAULIY;Gm=(math.pi/2)*np.diag([0.,1.])
        Hc=np.diag(self.k-CENTER);Gc=self.theta
        dc_bound=2*BAND*np.linalg.norm(Gc,2)*2e-10
        dm_bound=(math.pi/2)*h*2e-10
        for H,G,bound in ((Hm,Gm,dm_bound),(Hc,Gc,dc_bound)):
            ideal=expm(1j*np.kron(G,PAULIY))
            for offset in (-1.,0.,1.):
                actual=probe_unitary(H,G,offset)
                np.testing.assert_allclose(actual.conj().T@actual,np.eye(len(actual)),atol=3e-10)
                self.assertLessEqual(np.linalg.norm(actual-ideal,2),bound+2e-9)

    def test_complete_joint_outcomes_and_conditional_memory(self):
        # Product-prepared R and a nontrivial memory state at the selected
        # slice: four outcomes, including clock no-reading and memory no-record.
        C=expm(1j*np.kron(self.theta,PAULIY))
        M=expm(1j*np.kron((math.pi/2)*np.diag([0.,1.]),PAULIY))
        mem=np.array([np.sqrt(.3),1j*np.sqrt(.7)])
        pc=[];pm=[]
        for j in (0,1):
            ck=C[j::2,0::2]@self.beta;mk=M[j::2,0::2]@mem
            pc.append(np.vdot(ck,ck).real);pm.append(np.vdot(mk,mk).real)
        joint=np.outer(pc,pm)
        self.assertAlmostEqual(joint.sum(),1.,places=13)
        self.assertGreater(joint[0].sum(),.8)  # preserve clock no-reading
        np.testing.assert_allclose(joint[1]/joint[1].sum(),[.3,.7],atol=1e-13)

    def test_existing_chiral_memory_record_is_stable_under_smearing(self):
        # The actual old finite-grid Ω, Q and flag/memory dynamics, with its
        # prescribed central chiral cursor, not the massive continuum cursor.
        rho=np.array([[.5,.35j],[-.35j,.5]])
        nodes,weights=leggauss(7);sigma0=math.pi/(2*BAND)
        times=R+nodes*4*sigma0
        weights=np.array([w*scaled_clock_density(BAND*(t-R)) for t,w in zip(times,weights)])
        weights/=weights.sum()
        vec,_,_=regulated_instrument(output_time=R)
        sharp=np.array([np.trace(branch(vec,rho,m)).real for m in (0,1)])
        probs=np.zeros(2)
        for t,w in zip(times,weights):
            vec,_,_=regulated_instrument(output_time=float(t))
            probs += w*np.array([np.trace(branch(vec,rho,m)).real for m in (0,1)])
        np.testing.assert_allclose(probs,sharp,atol=3e-9)
        self.assertAlmostEqual(probs.sum(),1.,places=9)

    def test_clock_state_mismatch_is_not_silently_ignored(self):
        # An R state concentrated at the band edge has a different hit rate.
        edge=np.zeros(len(self.E));edge[0]=1
        p_edge=np.vdot(edge,self.E@edge).real
        p_beta=np.vdot(self.beta,self.E@self.beta).real
        self.assertLess(p_edge,.02)
        self.assertGreater(p_beta,.12)
        self.assertGreater(abs(p_beta-p_edge),.1)


if __name__=='__main__': unittest.main()
