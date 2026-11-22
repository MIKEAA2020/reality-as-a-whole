import math
import unittest

try:
    from . import gravity_clock_duration_calibration as c
    from .gravitating_clock_probe import scatter
except ImportError:
    import gravity_clock_duration_calibration as c
    from gravitating_clock_probe import scatter


class CalibrationTests(unittest.TestCase):
    def test_parent_response_and_band_controls(self):
        result = c.check()
        self.assertEqual(len(result['examples']), 5)
        self.assertLess(result['bounds']['total_duration_error'], .049)

    def test_confidence_worst_case_on_probability_endpoints(self):
        b=c.constants()
        eps=b['statistical_probability_error']
        for start in (2, 3, 5, 7.99):
            p=c.band_probability(start)
            target=c.tau(start+c.WIDTH/2)
            for observed in (max(0,p-eps),min(1,p+eps)):
                self.assertLessEqual(abs(c.estimate_from_frequency(observed)-target),
                                     b['total_duration_error'])

    def test_clipping_and_domain_validation(self):
        b=c.constants()
        self.assertAlmostEqual(c.estimate_from_frequency(0),b['phase_upper']/c.OMEGA)
        self.assertAlmostEqual(c.estimate_from_frequency(1),b['phase_lower']/c.OMEGA)
        for value in (-.1,1.1):
            with self.assertRaises(ValueError): c.estimate_from_frequency(value)
        with self.assertRaises(ValueError): c.band_probability(1.999)
        with self.assertRaises(ValueError): c.band_probability(8)
        with self.assertRaises(ValueError): c.constants(0)
        with self.assertRaises(ValueError): c.constants(alpha=1)

    def test_uncalibrated_phase_and_alias_fail(self):
        k=4
        z=scatter(k,c.KAP1)*scatter(k,c.KAP0).conjugate()
        rotated=z*complex(math.cos(.8), math.sin(.8))
        observed=(1+rotated.real)/2
        # Unmodelled reference error can invalidate the claimed confidence bound.
        self.assertGreater(abs(c.estimate_from_frequency(observed)-c.tau(k)),
                           c.constants()['total_duration_error'])
        self.assertAlmostEqual(math.cos(1.1),math.cos(1.1+2*math.pi))

    def test_weak_sample_size_is_not_hidden(self):
        self.assertGreater(c.constants(n=100)['total_duration_error'], 0.6)
        self.assertGreater(c.constants(alpha=.001)['total_duration_error'],
                           c.constants(alpha=.05)['total_duration_error'])

if __name__ == '__main__':
    unittest.main()
