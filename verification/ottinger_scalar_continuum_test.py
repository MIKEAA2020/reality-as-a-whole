import unittest
import mpmath as mp
from ottinger_scalar_continuum import angular_bracket, continuum_value, moment


class ScalarContinuumTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mp.mp.dps = 25

    def test_angular_integral(self):
        # Independent S^3 angular averaging with the polar angle weight sin^2(theta).
        for z in (mp.mpf('0.01'), mp.mpf('0.5'), mp.mpf('2')):
            angular = (2/mp.pi)*mp.quad(
                lambda a: mp.sin(a)**2*(1-mp.cos(z*mp.cos(a))
                                         -z**2*mp.cos(a)**2/2), [0, mp.pi])
            self.assertLess(abs(angular_bracket(z)-angular), mp.mpf('1e-23'))

    def test_small_z_leading_term(self):
        z = mp.mpf('0.0001')
        self.assertLess(abs(angular_bracket(z)/z**4+mp.mpf(1)/192), mp.mpf('2e-12'))

    def test_integral_sign_and_bound(self):
        c4 = moment(4)/(1536*mp.pi**4)
        c6 = moment(6)/(73728*mp.pi**4)
        k = mp.mpf(1)
        value = continuum_value(k)
        self.assertLess(value, 0)
        self.assertLessEqual(abs(value+c4*k**4), c6*k**6)
        self.assertLess(abs(value-mp.mpf('-0.00000235348738158933544')), mp.mpf('1e-23'))

    def test_mass_and_zero(self):
        self.assertEqual(continuum_value(0), 0)
        with self.assertRaises(ValueError):
            continuum_value(1, 0)


if __name__ == '__main__':
    unittest.main()
