"""Relational molecular chirality and a finite-reservoir Frank-type model.

The geometric L/D calibration is a Fischer projection embedding, not a quantum
chemistry calculation. The reaction network is an illustrative modified
Frank model, not a fit or a reproduction of the full Higgs–Blackmond network.
The material ledger is not a physical energy or a GR constraint.
"""
from dataclasses import dataclass
from math import sqrt
import unittest
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

from verification.zero_three_frame_chirality import invariants, gauge_tree

# Standard Fischer orientation: horizontal bonds toward viewer, vertical away.
FISCHER_L={
    'N':np.array([-1.,0.,1.]), 'C':np.array([0.,1.,-1.]),
    'R':np.array([0.,-1.,-1.]), 'H':np.array([1.,0.,1.]),
}


def molecular_vectors(points):
    h=points['H']
    return tuple(points[name]-h for name in ('N','C','R'))


def frame_chirality(points):
    return invariants(molecular_vectors(points),np.eye(3),np.eye(3))[3]


def transform(points, matrix, translation):
    return {k:matrix@v+translation for k,v in points.items()}


@dataclass(frozen=True)
class Params:
    k:float=1.
    k0:float=.01
    gamma:float=1.
    d:float=1.
    da:float=1.
    r:float=.05
    dp:float=1.
    feed:float=1661/500
    bias:float=0.


def rates(y,p):
    """State (A,L,D,P,R,Q); supply R, waste Q measured in monomer units.

    This selected constant feed applies only while R remains positive. Q lumps
    outflows and does not model their chemical species or energy.
    """
    A,L,D,P,R,Q=y
    k,k0,g,d,da,r,dp,J,h=(p.k,p.k0,p.gamma,p.d,p.da,p.r,p.dp,p.feed,p.bias)
    autoL=k*A*L;autoD=k*A*D
    spL=k0*A*(1+h);spD=k0*A*(1-h)
    inhibition=g*L*D
    return np.array([J-da*A-autoL-autoD-spL-spD,
                     spL+autoL-inhibition-d*L+r*(D-L),
                     spD+autoD-inhibition-d*D+r*(L-D),
                     inhibition-dp*P,
                     -J, da*A+d*(L+D)+2*dp*P])


def excess(y):
    return (y[1]-y[2])/(y[1]+y[2])


def solve(initial,p=Params(),stop=120.,samples=None):
    if abs(p.bias)>1: raise ValueError('bias must give nonnegative spontaneous rates')
    if initial[4] < p.feed*stop: raise ValueError('finite feed reservoir exhausted')
    r=solve_ivp(lambda t,y:rates(y,p),(0.,stop),initial,
                t_eval=samples,rtol=2e-10,atol=1e-12,method='DOP853')
    if not r.success: raise RuntimeError(r.message)
    return r


def material(y):
    return y[0]+y[1]+y[2]+2*y[3]+y[4]+y[5]


def analytic_broken():
    """For defaults: A=11/10, total enantiomers=2, L*D=111/1000."""
    A=1.1; H=2.; delta=sqrt(889/250)
    L=(H+delta)/2; D=(H-delta)/2; P=L*D
    return A,L,D,P


def jacobian_ald(A,L,D,p):
    return np.array([
       [-p.da-p.k*(L+D)-2*p.k0,-p.k*A,-p.k*A],
       [p.k0*(1+p.bias)+p.k*L,p.k*A-p.gamma*D-p.d-p.r,-p.gamma*L+p.r],
       [p.k0*(1-p.bias)+p.k*D,-p.gamma*D+p.r,p.k*A-p.gamma*L-p.d-p.r]])


class MolecularChiralityAmplificationTests(unittest.TestCase):
    def test_calibrated_molecular_sign_matches_existing_relational_invariant(self):
        # For this ordering and standard Fischer convention only: L=+2/3.
        self.assertAlmostEqual(frame_chirality(FISCHER_L),2/3)
        reflected=transform(FISCHER_L,np.diag([-1.,1.,1.]),np.zeros(3))
        self.assertAlmostEqual(frame_chirality(reflected),-2/3)
        r=np.array([[0.,-1.,0.],[1.,0.,0.],[0.,0.,1.]])
        moved=transform(FISCHER_L,r,np.array([3.,-4.,7.]))
        self.assertAlmostEqual(frame_chirality(moved),2/3)

    def test_independent_frames_preserve_calibrated_molecular_orientation(self):
        vs=molecular_vectors(FISCHER_L)
        I=np.eye(3)
        r1=np.array([[0.,-1.,0.],[1.,0.,0.],[0.,0.,1.]])
        r2=np.diag([-1.,-1.,1.])
        r3=np.array([[1.,0.,0.],[0.,0.,-1.],[0.,1.,0.]])
        ds,l12,l13=gauge_tree(vs,I,I,(r1,r2,r3))
        np.testing.assert_allclose(invariants(ds,l12,l13),invariants(vs,I,I),atol=1e-14)
        self.assertAlmostEqual(invariants(ds,l12,l13)[3],2/3)

    def test_degenerate_geometry_and_indistinguishable_labels(self):
        # Nonzero but linearly dependent directions give zero orientation.
        points={k:v.copy() for k,v in FISCHER_L.items()}
        points['R']=points['N'].copy()
        self.assertAlmostEqual(frame_chirality(points),0)
        # If N and R were chemically indistinguishable, exchanging their
        # labels would reverse the proposed tag while leaving the chemistry
        # the same; it would therefore not be a valid physical enantiomer tag.
        exchanged=FISCHER_L.copy();exchanged['N'],exchanged['R']=exchanged['R'],exchanged['N']
        self.assertAlmostEqual(frame_chirality(exchanged),-frame_chirality(FISCHER_L))

    def test_full_material_ledger_exactly_balances_every_reaction(self):
        p=Params()
        for y in (np.array([1.,.2,.8,.5,500.,0.]),
                  np.array([2.,1.,.01,3.,200.,4.])):
            d=rates(y,p)
            self.assertAlmostEqual(material(d),0,places=13)
        # Same statement holds with racemic and biased spontaneous production.
        self.assertAlmostEqual(material(rates(np.array([1.,.2,.8,.5,500.,0.]),
                                               Params(bias=.2))),0,places=13)

    def test_exact_racemic_invariant_and_parity_equivariance(self):
        y=np.array([1.,.5,.5,0.,500.,0.]);dy=rates(y,Params())
        self.assertEqual(dy[1],dy[2])
        y=np.array([1.2,.7,.2,.1,500.,0.]); p=Params(bias=.2)
        mirror=y.copy();mirror[1],mirror[2]=y[2],y[1]
        rev=Params(bias=-.2)
        a=rates(y,p); b=rates(mirror,rev)
        np.testing.assert_allclose(b,a[[0,2,1,3,4,5]],rtol=0,atol=1e-14)

    def test_fixed_point_and_local_stability(self):
        A,L,D,P=analytic_broken()
        y=np.array([A,L,D,P,500.,0.]); p=Params()
        np.testing.assert_allclose(rates(y,p)[:4],0,atol=2e-15)
        self.assertAlmostEqual(L*D,111/1000)
        self.assertAlmostEqual(excess(y),sqrt(889/1000),places=14)
        self.assertTrue(np.all(np.real(np.linalg.eigvals(jacobian_ald(A,L,D,p)))<0))
        # P has independent eigenvalue -dp; R and Q are bookkeeping, not
        # fixed points in the continuously driven system.
        self.assertLess(-p.dp,0)

    def test_racemic_equilibrium_has_positive_antisymmetric_eigenvalue(self):
        p=Params()
        def a_of_h(h): return p.feed/(p.da+2*p.k0+2*p.k*h)
        def eq(h):
            A=a_of_h(h)
            return p.k0*A+(p.k*A-p.d)*h-p.gamma*h*h
        h=brentq(eq,.001,2)
        A=a_of_h(h)
        self.assertAlmostEqual(eq(h),0,places=12)
        growth=p.k*A-p.d-2*p.r
        self.assertGreater(growth,0)
        vec=np.array([0.,1.,-1.])
        np.testing.assert_allclose(jacobian_ald(A,h,h,p)@vec,growth*vec,atol=1e-13)

    def test_trajectories_amplify_and_mirror_without_selecting_sign(self):
        p=Params();y=np.array([1.,.505,.495,0.,500.,0.]); y2=y.copy();y2[1],y2[2]=y[2],y[1]
        a=solve(y,p,120.).y[:,-1]; b=solve(y2,p,120.).y[:,-1]
        self.assertAlmostEqual(excess(a),sqrt(889/1000),places=6)
        self.assertAlmostEqual(excess(a),-excess(b),places=11)
        np.testing.assert_allclose(a,b[[0,2,1,3,4,5]],atol=2e-8,rtol=2e-10)
        self.assertAlmostEqual(material(a),material(y),places=8)
        self.assertGreater(a[4],0)
        self.assertTrue(np.all(a>=-1e-10))

    def test_trajectory_positivity_ledger_and_numerical_convergence(self):
        p=Params(); y=np.array([1.,.505,.495,0.,500.,0.])
        times=np.linspace(0,120,241)
        a=solve(y,p,120,times)
        b=solve_ivp(lambda t,x:rates(x,p),(0,120),y,t_eval=times,
                    method='Radau',rtol=2e-11,atol=1e-13)
        self.assertTrue(b.success)
        self.assertGreaterEqual(np.min(a.y),-1e-9)
        np.testing.assert_allclose([material(x) for x in a.y.T],material(y),atol=1e-8,rtol=0)
        np.testing.assert_allclose(a.y,b.y,atol=2e-8,rtol=2e-8)
        with self.assertRaises(ValueError): solve(y,p,151.)

    def test_no_inhibition_cannot_amplify_ee_in_this_symmetric_model(self):
        y=np.array([1.,.505,.495,0.,500.,0.])
        out=solve(y,Params(gamma=0),30.,np.linspace(0,30,100))
        ees=np.array([excess(x) for x in out.y.T])
        self.assertTrue(np.all(np.diff(ees)<=1e-10))
        self.assertLess(ees[-1],ees[0])

    def test_exact_racemic_state_stays_racemic_without_bias(self):
        y=np.array([1.,.5,.5,0.,500.,0.]); out=solve(y,Params(),30.)
        self.assertAlmostEqual(excess(out.y[:,-1]),0,places=13)
        # A specified asymmetric source changes that invariant symmetry.
        z=solve(y,Params(bias=1e-3),30.).y[:,-1]
        self.assertGreater(excess(z),0)
        zrev=solve(y,Params(bias=-1e-3),30.).y[:,-1]
        self.assertAlmostEqual(excess(z),-excess(zrev),places=11)


if __name__=='__main__': unittest.main()
