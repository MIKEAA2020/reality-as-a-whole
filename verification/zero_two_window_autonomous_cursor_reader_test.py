"""A positive-H autonomous cursor reads the prior two-window flag.

The continuum estimate is analytic and conditional on the nonlocal Q coupling,
initial cursor preparation and the previous exact commutator certificate. The
finite-grid integration below checks a chiral comparison, not the full unbounded
massive cursor or experimental apparatus. Scalar-clock access is assumed.
"""
import math
import unittest
import numpy as np
from scipy.integrate import solve_ivp, quad

from verification.zero_two_window_autonomous_support_dynamics_test import system
from verification.zero_two_window_commutator_certificate import verify
from verification.zero_two_window_redundant_flag_hold_test import collective_y

N=8; G=100.; A=1e-6; WIDTH=1e-6; V=1.; MASS=1e16
KAPPA=math.pi/2
T0=math.pi/(2*G)
START=T0-(A+WIDTH)/V
END=T0+(A+WIDTH)/V
RET=math.pi/G
C=.419/(2*1.3)


def error_bounds():
    df=15/(8*WIDTH)
    ddf=10/(math.sqrt(3)*WIDTH**2)
    a1=KAPPA*df
    a2=KAPPA*ddf+a1*a1
    k2=math.sqrt(63/2)/A**2+2*math.sqrt(3)/A*a1+a2
    dynamical=N*G*C*END**2/2
    finite_pulse=2*KAPPA*G*N*WIDTH/V
    dispersion=RET*k2/(2*MASS)
    return k2,dynamical,finite_pulse,dispersion


def pulse_scaled(u):
    # WIDTH*f(WIDTH*u); weak derivatives are integrable at endpoints.
    return 15/16*(1-u*u)**2 if abs(u)<=1 else 0.


def chiral_grid_simulation(h=0,inside=False,offset=0.,strength=1.):
    """Single initial cursor position x0 (not a cursor wavepacket)."""
    _,B,P,Q,O,_=system(4,h)
    dim=len(Q); S=collective_y(N);sy=np.array([[0,-1j],[1j,0]])
    hsys=np.kron(O,np.eye(N+1))+G*np.kron(Q,S)
    vals,W=np.linalg.eigh(hsys)
    if inside:
        psi=B[:,0]
    else:
        rng=np.random.default_rng(2026)
        psi=Q@(rng.normal(size=dim)+1j*rng.normal(size=dim))
        psi/=np.linalg.norm(psi)
    ready=np.zeros(N+1);ready[0]=1
    z=np.kron(psi,ready)
    center=T0-offset/V
    t_begin=center-WIDTH/V
    z=W@(np.exp(1j*vals*t_begin)*(W.conj().T@z))
    state=np.zeros((dim,N+1,2),complex);state[:,:,0]=z.reshape(dim,N+1)
    flag=np.ones(N+1);flag[0]=0
    # u=(t-center)*V/WIDTH; pulse has support [-1,1].
    def rhs(u,y):
        a=y.reshape(dim,N+1,2)
        flat=hsys@a.reshape(dim*(N+1),2)
        free=flat.reshape(dim,N+1,2)
        read=(a*flag[None,:,None])@sy.T
        return (1j*((WIDTH/V)*free+strength*KAPPA*pulse_scaled(u)*read)).ravel()
    r=solve_ivp(rhs,(-1.,1.),state.ravel(),method='DOP853',rtol=2e-10,atol=1e-12)
    if not r.success:raise RuntimeError(r.message)
    post=r.y[:,-1].reshape(dim*(N+1),2)
    q0=float(np.linalg.norm(post[:,1])**2)
    # Evolve without readout until RET; memory is a spectator.
    t_after=RET-(center+WIDTH/V)
    after=W@(np.exp(1j*vals*t_after)[:,None]*(W.conj().T@post))
    r3=after.reshape(dim,N+1,2)
    qret=float(np.sum(abs(r3[:,:,1])**2))
    flagret=float(np.sum(abs(r3[:,1:,:])**2))
    return q0,qret,flagret


class AutonomousCursorReaderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert=verify()

    def test_positive_root_and_continuum_error_budget(self):
        self.assertLess(self.cert['commutator_squared_upper'],(.419)**2)
        K,dyn,pulse,disp=error_bounds()
        self.assertLess(K,3.357e13)
        self.assertLess(dyn,.01592)
        self.assertLess(pulse,.002514)
        self.assertLess(disp,.0000528)
        err=dyn+pulse+disp
        self.assertLess(err,.01849)
        self.assertLess((math.sin(G*A/V)**N+err)**2,.000343)
        self.assertLess(err**2,.000343)
        self.assertGreater(START,0)
        self.assertLess(END,RET)
        self.assertGreater(T0-A/V,math.pi/(4*G))
        self.assertLess(T0+A/V,3*math.pi/(4*G))
        # B=Ng+κv||f||∞+1 makes H ≥ Ω+1 > 2.3.
        offset=N*G+KAPPA*V*(15/(16*WIDTH))+1
        self.assertAlmostEqual(offset-N*G-KAPPA*V*(15/(16*WIDTH)),1.)

    def test_pulse_norm_and_derivative_integrals(self):
        # Integrals for f_b and normalized compact cursor envelope ψ_a.
        f=lambda u:15/16*(1-u*u)**2
        fp=lambda u:-15/4*u*(1-u*u)
        fpp=lambda u:-15/4*(1-3*u*u)
        self.assertAlmostEqual(quad(f,-1,1)[0],1.,places=13)
        self.assertAlmostEqual(quad(lambda x:abs(fp(x)),-1,1,points=[0])[0],15/8,places=13)
        self.assertAlmostEqual(quad(lambda x:abs(fpp(x)),-1,1,
                points=[-1/math.sqrt(3),1/math.sqrt(3)])[0],10/math.sqrt(3),places=12)
        norm=math.sqrt(315/256)
        self.assertAlmostEqual(quad(lambda x:(norm*(1-x*x)**2)**2,-1,1)[0],1.,places=13)
        self.assertAlmostEqual(quad(lambda x:(norm*(-4*x*(1-x*x)))**2,-1,1)[0],3.,places=13)
        self.assertAlmostEqual(quad(lambda x:(norm*(-4+12*x*x))**2,-1,1)[0],63/2,places=12)

    def test_chiral_reader_captures_and_retains_through_flag_reversal(self):
        _,dyn,pulse,disp=error_bounds();err=dyn+pulse+disp
        for inside in (True,False):
            for offset in (-A/2,0.,A/2):
                q,qret,flagret=chiral_grid_simulation(0,inside,offset)
                self.assertAlmostEqual(q,qret,places=10)
                if inside:self.assertLess(q,err**2+1e-10)
                else:
                    self.assertLess(1-q,(math.sin(G*A/V)**N+err)**2+1e-10)
                    self.assertLess(flagret,.01)

    def test_no_record_without_reader_coupling(self):
        q,qret,_=chiral_grid_simulation(0,False,0.,strength=0.)
        self.assertLess(q,1e-20)
        self.assertLess(qret,1e-20)


if __name__=='__main__':unittest.main()
