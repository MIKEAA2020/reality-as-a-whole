import math
import unittest

try:
    from . import gravity_gradient_pointer_gate as g
except ImportError:
    import gravity_gradient_pointer_gate as g


class GravityGradientPointerTests(unittest.TestCase):
    def test_end_to_end_and_complete_readout(self):
        result=g.run()
        self.assertEqual(result['status'],'passed')
        record=result['complete_finite_packet_pointer_and_ramsey_readout']['probabilities']
        self.assertEqual(len(record),4)
        self.assertTrue(all(p>0 for p in record.values()))
        self.assertAlmostEqual(sum(record.values()),1,places=7)
        self.assertGreater(record['plus_outside']+record['minus_outside'],.09)

    def test_positive_local_coupling_has_turnaround_cancellation(self):
        self.assertEqual(g.bump(-1),0)
        self.assertEqual(g.bump(1),g.A)
        for i in range(101):
            x=-1+2*i/100
            self.assertGreaterEqual(g.slope(x),0)
        self.assertGreater(g.slope(0),0)
        kap=g.kappa(0,.4)
        self.assertLess(abs(g.shift_integral(10,2,kap,8192)),2e-8)

    def test_equal_volume_crossings_retain_only_equal_extra_shift(self):
        k=2.;kap=g.kappa(0,.4);b=-.25
        r=math.sqrt(k*k+kap*kap)
        time=math.acosh((k*k/math.exp(b)+kap)/r)
        one=g.shift_integral(-time,k,kap,8192)
        two=g.shift_integral(time,k,kap,8192)
        self.assertAlmostEqual(one,two,places=7)
        self.assertAlmostEqual(one,-g.bump(b),places=7)
        self.assertNotEqual(one,0)

    def test_oscillator_and_pointer_energies_backreact(self):
        self.assertAlmostEqual(g.kappa(0,0),.2)
        self.assertAlmostEqual(g.kappa(1,0),.6)
        self.assertGreater(g.kappa(0,.4),g.kappa(0,0))
        self.assertGreater(abs(g.readout_probability(2,0)-g.readout_probability(2,.6)),.01)
        with self.assertRaises(ValueError):g.kappa(2,0)
        with self.assertRaises(ValueError):g.kappa(0,0,0)

    def test_gauged_mode_and_numerical_quadrature(self):
        for x in (-1.2,-.7,0,.5,1.2):
            self.assertLess(abs(g.ode_residual(2,.0,.4,x)),1e-9)
        a=g.finite_pointer_readout(2.005,128)
        b=g.finite_pointer_readout(2.005,256)
        self.assertLess(max(abs(a[k]-b[k]) for k in a),1e-7)

if __name__=='__main__': unittest.main()
