"""Regression checks, not a proof of experience or of zero total energy."""
import math
import unittest
import numpy as np
import sympy as sp
from verification.zero_closed_plasma_scalar_response import solve


class ClosedScalarResponseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.positive=solve(rtol=1e-12)
        cls.negative=solve(phase=-math.pi/4,rtol=1e-12)
        cls.symmetric=solve(phase=0,rtol=1e-12)

    def test_symbolic_discrete_symmetries_and_current_sources(self):
        E,p,phi,Pi,a,P,om,d,k=sp.symbols('E p phi Pi a P om d k',real=True,nonzero=True)
        alpha=k*E*p/(a*P)*2*om*phi*Pi/d**2
        h=-2*p*E/sp.sqrt(1+p*p)
        # Charge conjugation: field and positively charged stream reverse;
        # neutral scalar is unchanged. Time reversal reverses p and Pi.
        self.assertEqual(sp.simplify(alpha.xreplace({E:-E,p:-p})-alpha),0)
        self.assertEqual(sp.simplify(alpha.xreplace({p:-p,Pi:-Pi})-alpha),0)
        self.assertEqual(sp.simplify(alpha.xreplace({phi:-phi,Pi:-Pi})-alpha),0)
        self.assertEqual(sp.simplify(h.xreplace({E:-E,p:-p})-h),0)
        self.assertEqual(sp.simplify(h.xreplace({p:-p})+h),0)
        # The two complementary currents exchange incidence: their sum is
        # conserved, but their separate time derivatives are not identically zero.
        j=2*p/sp.sqrt(1+p*p)
        alpha_dot=sp.diff(alpha,E)*(-j)+sp.diff(alpha,p)*E+sp.diff(alpha,phi)*Pi+sp.diff(alpha,Pi)*(-om**2*phi)
        at_initial=sp.simplify(alpha_dot.subs({E:a,p:0,phi:d/(sp.sqrt(2)*om),Pi:d/sp.sqrt(2)}))
        self.assertEqual(sp.simplify(at_initial-k*a/P),0)

    def test_common_rest_frame_and_weighted_product_rule(self):
        E,B,p,n,m,Pi,phi,om=sp.symbols('E B p n m Pi phi om',real=True)
        r=(E**2+B**2)/2; w=sp.sqrt(m*m+p*p)
        M=2*n*w; P=2*n*p*p/w
        S=(Pi**2+om**2*phi**2)/2; pressure=(Pi**2-om**2*phi**2)/2
        u=sp.Matrix([1,0,0,0]); ul=sp.Matrix([-1,0,0,0])
        field=sp.diag(r,r,-r,r); matter=sp.diag(M,0,P,0); scalar=sp.diag(S,pressure,pressure,pressure)
        for tensor,density in ((field,r),(matter,M),(scalar,S)):
            self.assertEqual(sp.simplify(-tensor*ul-density*u),sp.zeros(4,1))
        self.assertEqual(sp.simplify(Pi*(-om**2*phi)+om**2*phi*Pi),0)
        cf,cm,cfd,cmd,h=sp.symbols('cf cm cfd cmd h')
        weighted=cf*h+cm*(-h)
        product_derivative=cfd*r+cf*h+cmd*M+cm*(-h)
        self.assertEqual(sp.simplify(weighted-product_derivative+r*cfd+M*cmd),0)

    def test_positive_weights_common_rest_frame_and_boundary(self):
        data=self.positive; pars=data['parameters']; T=data['period']; y=data['trajectory'](np.linspace(0,T,1001))
        E,p,phi,Pi=y[:4]; a=pars['amplitude']; k=pars['contrast']; d=pars['scalar_amplitude']; om=data['scalar_mass']
        alpha=k*E*p/(a*data['pmax'])*2*om*phi*Pi/d**2
        self.assertGreaterEqual(np.min((1+alpha)/2),(1-k)/2-1e-11)
        self.assertGreaterEqual(np.min((1-alpha)/2),(1-k)/2-1e-11)
        np.testing.assert_allclose(y[:4,-1],data['start'][:4],rtol=0,atol=2e-10)
        energy=(E*E+pars['magnetic']**2)/2+2*pars['n']*np.sqrt(pars['m']**2+p*p)+(Pi*Pi+om*om*phi*phi)/2
        self.assertLess(np.ptp(energy),2e-10)
        self.assertGreater(np.min(energy),0)

    def test_dynamics_and_independent_quadrature(self):
        data=self.positive
        self.assertAlmostEqual(data['end'][4],.1471787903268,places=9)
        self.assertAlmostEqual(data['end'][4],data['quadrature'],places=10)
        self.assertLess(data['quadrature_error'],1e-9)
        self.assertAlmostEqual(data['period'],4.70308610998,places=9)

    def test_reversed_state_opposite_and_symmetric_phase_zero(self):
        a=self.positive['end'][4]; b=self.negative['end'][4]; c=self.symmetric['end'][4]
        self.assertAlmostEqual(a,-b,places=10)
        self.assertAlmostEqual(c,0,places=10)

    def test_small_amplitude_limit_supports_analytic_existence(self):
        c=.6; values=[]
        for a in [.1,.05]:
            x=solve(amplitude=a,contrast=c,rtol=1e-12)
            values.append(x['end'][4]/a**2)
        target=c*math.pi/8
        self.assertLess(abs(values[1]-target),abs(values[0]-target))
        self.assertLess(abs(values[1]-target),3e-5)

    def test_unequal_weights_are_not_individually_conserved(self):
        data=self.positive; k=data['parameters']['contrast']; a=data['parameters']['amplitude']; P=data['pmax']
        # χ_F=(1+alpha)/2, χ_M=(1-alpha)/2. At this phase χ_F' > 0.
        derivative=k*a/(2*P)
        self.assertGreater(derivative,0)
        dt=1e-6
        def chi(t):
            E,p,phi,Pi=data['trajectory'](t)[:4]
            om=data['scalar_mass']; d=data['parameters']['scalar_amplitude']
            alpha=k*E*p/(a*P)*2*om*phi*Pi/d**2
            return np.array([(1+alpha)/2,(1-alpha)/2])
        observed=(chi(dt)-chi(0))/dt
        np.testing.assert_allclose(observed,[derivative,-derivative],rtol=1e-5,atol=1e-7)
        self.assertAlmostEqual(float(np.sum(observed)),0,places=9)

    def test_bad_inputs(self):
        for kwargs in ({'amplitude':0},{'magnetic':0},{'contrast':1},{'rtol':1}):
            with self.assertRaises(ValueError): solve(**kwargs)


if __name__=='__main__': unittest.main()
