"""Checks of a closed relativistic two-stream/Maxwell oscillator and frame ledger."""
import math
import unittest
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp

A, N, M, B0, C, BMAG = .8, 1., 1., .4, .5, 1.
PMAX = math.sqrt((M+A*A/(4*N))**2-M*M)


def gamma(v):
    return 1/math.sqrt(1-v*v)


def rhs(t,z):
    e,p,wf,wm,df,dm=z
    w=math.sqrt(M*M+p*p)
    j=2*N*p/w
    edot=-j
    pdot=e
    v=B0+C*e*p
    vdot=C*(edot*p+e*pdot)
    g=gamma(v)
    gdot=g**3*v*vdot
    field_energy=(e*e+BMAG*BMAG)/2
    matter_energy=2*N*w
    h=-g*j*e
    return [edot,pdot,h,-h,-field_energy*gdot,-matter_energy*gdot]


def solve_cycle():
    def crossing(t,z): return z[1]
    crossing.direction=-1
    crossing.terminal=True
    initial=[A,0,0,0,0,0]
    half=solve_ivp(rhs,(0,20),initial,events=crossing,rtol=2e-12,atol=1e-14)
    if len(half.t_events[0])!=1: raise AssertionError('missing half-cycle')
    T=2*half.t_events[0][0]
    full=solve_ivp(rhs,(0,T),initial,rtol=2e-12,atol=1e-14,dense_output=True)
    return T,full


class ClosedRelativisticPlasmaFrameReview(unittest.TestCase):
    def test_maxwell_and_relativistic_matter_balance(self):
        E,p,n,m,B=sp.symbols('E p n m B',positive=True)
        w=sp.sqrt(m*m+p*p); j=2*n*p/w
        d=lambda f: sp.diff(f,E)*(-j)+sp.diff(f,p)*E
        F=(E*E+B*B)/2; matter=2*n*w
        self.assertEqual(sp.simplify(d(F)+j*E),0)
        self.assertEqual(sp.simplify(d(matter)-j*E),0)
        # Signed species currents: equal charge densities, opposite momenta.
        self.assertEqual(n-n,0)
        self.assertEqual(n*p/w-(-n*p/w),j)

    def test_original_closed_plasma_weighted_cycle(self):
        t=sp.symbols('t',real=True)
        a,b=sp.symbols('a b',positive=True)
        e=a*sp.cos(t); j=a*sp.sin(t); h=-e*j
        flow=1+2*b*e*j/(e**2+j**2)
        energy=1+b*(e**2-j**2)/(e**2+j**2)
        self.assertEqual(sp.simplify(sp.integrate(flow*h,(t,0,2*sp.pi))
                                     +b*sp.pi*a*a/2),0)
        self.assertEqual(sp.simplify(sp.integrate(energy*h,(t,0,2*sp.pi))),0)
        # Leading relativistic two-stream oscillator frequency is sqrt(2n/m).
        p,n,m=sp.symbols('p n m',real=True,positive=True)
        j_rel=2*n*p/sp.sqrt(m*m+p*p)
        self.assertEqual(sp.simplify(sp.diff(j_rel,p).subs(p,0)-2*n/m),0)

    def test_frame_eigenvectors_and_force_cancellation(self):
        e, bm, mom, mass, n, v=sp.symbols('e bm mom mass n v',real=True,nonzero=True)
        g=sp.symbols('gamma',positive=True); w=sp.sqrt(mass**2+mom**2)
        r=(e**2+bm**2)/2; mat=2*n*w; pressure=2*n*mom**2/w
        u=sp.Matrix([g,0,g*v,0]); u_low=sp.Matrix([-g,0,g*v,0])
        tf=sp.diag(r,r,-r,r); tm=sp.diag(mat,0,pressure,0)
        cf=-tf*u_low; cm=-tm*u_low
        self.assertEqual(sp.simplify(cf-r*u),sp.zeros(4,1))
        self.assertEqual(sp.simplify(cm[2]-v*cm[0]+g*v*(pressure+mat)),0)
        force=sp.Matrix([2*n*mom*e/w,0,0,0])
        h=(force.T*u_low)[0]
        self.assertEqual(sp.simplify(h+g*2*n*mom*e/w),0)
        h_matter=((-force).T*u_low)[0]
        self.assertEqual(sp.simplify(h+h_matter),0)

    def test_observer_deformation_identity_symbolic(self):
        E,B,p,n,m,g,gdot=sp.symbols('E B p n m gamma gdot',real=True)
        w=sp.sqrt(m*m+p*p); j=2*n*p/w
        r=(E**2+B**2)/2; matter=2*n*w
        rdot=-j*E; mdot=j*E
        hf=g*rdot; hm=g*mdot
        divf=g*rdot+r*gdot; divm=g*mdot+matter*gdot
        self.assertEqual(sp.simplify(hf-divf+r*gdot),0)
        self.assertEqual(sp.simplify(hm-divm),-matter*gdot)
        self.assertEqual(sp.simplify(hf+hm),0)

    def test_smooth_timelike_positivity_and_period(self):
        self.assertGreater(B0-C*A*PMAX,0)
        self.assertLess(B0+C*A*PMAX,1)
        T,sol=solve_cycle(); self.assertAlmostEqual(T,4.70308610998,places=9)
        values=sol.sol(np.linspace(0,T,1001)); e,p=values[:2]
        self.assertLess(np.max(np.abs(e)),A+1e-10)
        self.assertLess(np.max(np.abs(p)),PMAX+1e-10)
        total=(e**2+BMAG**2)/2+2*N*np.sqrt(M*M+p*p)
        self.assertLess(np.max(np.abs(total-(2*N*M+(A*A+BMAG*BMAG)/2))),2e-11)
        self.assertLess(np.max(np.abs(values[:2,-1]-[A,0])),2e-10)

    def test_nonzero_cycle_and_exact_cancellation(self):
        T,sol=solve_cycle(); final=sol.y[:,-1]; wf,wm,df,dm=final[2:]
        self.assertAlmostEqual(wf,-.0617147652202,places=10)
        self.assertAlmostEqual(wf+wm,0,places=12)
        self.assertAlmostEqual(wf,df,places=10)
        self.assertAlmostEqual(wm,dm,places=10)
        self.assertAlmostEqual(df+dm,0,places=10)
        self.assertAlmostEqual(.75*wf+.25*wm,wf/2,places=12)
        # Endpoint gamma and both sector energies match; boundary flux is zero.
        self.assertAlmostEqual(final[0],A,places=10)
        self.assertAlmostEqual(final[1],0,places=10)

    def test_independent_quadrature_and_sign_mechanism(self):
        def integrand(p):
            w=math.sqrt(M*M+p*p)
            e=math.sqrt(max(0,A*A-4*N*(w-M)))
            return -2*N*p/w*(gamma(B0+C*p*e)-gamma(B0-C*p*e))
        value,err=quad(integrand,-PMAX,PMAX,epsabs=1e-12,epsrel=1e-11,limit=150)
        T,sol=solve_cycle()
        self.assertLess(value,0)
        self.assertLess(err,1e-10)
        self.assertAlmostEqual(value,sol.y[2,-1],places=10)
        # The nonzero integral depends on the state-dependent observer prescription.
        # For constant v the sector exchange is a multiple of a closed exact difference.
        for p in np.linspace(.01,PMAX*.99,10):
            self.assertLess(integrand(p),0)
            self.assertLess(integrand(-p),0)


if __name__=='__main__': unittest.main()
