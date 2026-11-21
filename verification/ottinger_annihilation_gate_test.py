import unittest
from fractions import Fraction as F
from ottinger_annihilation_gate import amplitude_a, amplitude_b, limit_shape, simpson, run


class AnnihilationGateTest(unittest.TestCase):
    def test_full_gate(self):
        self.assertEqual(run()['exact_rational_comparisons'], 36)

    def test_specific_nontrivial_value(self):
        self.assertEqual(amplitude_a(F(1), F(0)), F(3, 2))
        self.assertEqual(amplitude_b(F(1), F(0)), F(3, 2))

    def test_small_and_forward(self):
        self.assertEqual(amplitude_b(F(0), F(3, 4)), 1)
        self.assertEqual(amplitude_b(F(2), F(1)), 9)

    def test_integrator_validation(self):
        with self.assertRaises(ValueError):
            simpson(limit_shape, 0.5, 3)

    def test_moving_angle(self):
        x = F(10000)
        u = 1-1/(x*x)
        self.assertLess(abs(float(amplitude_b(x, u)/(x*x))-2/3), 1e-7)


if __name__ == '__main__':
    unittest.main()
