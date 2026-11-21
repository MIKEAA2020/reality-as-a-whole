import itertools
import math
import unittest
from synaptic_preference_calibration import P, delta, interaction, logit, relabel, simultaneous_delta_interval, target_interval


class SynapticControlTests(unittest.TestCase):
    def test_exact_odds_and_positivity(self):
        self.assertTrue(all(0 < x < 1 for x in P.values()))
        self.assertAlmostEqual(interaction(P['on_minus'], P['on_plus']), math.log(6))
        self.assertAlmostEqual(interaction(P['off_minus'], P['off_plus']), math.log(7/3))
        self.assertAlmostEqual(delta(P), math.log(18/7))

    def test_interval_and_both_decisions(self):
        e, bounds = simultaneous_delta_interval(P, 10000, .05)
        self.assertAlmostEqual(e, math.sqrt(math.log(160)/20000))
        self.assertLess(bounds[0], delta(P))
        self.assertGreater(bounds[1], delta(P))
        self.assertGreater(target_interval(bounds, .3, (.5, 1))[0], 0)
        bad = target_interval(bounds, 1.2, (.5, 1))
        self.assertLess(bad[0], 0)
        self.assertGreater(bad[1], 0)

    def test_opposite_channels_same_all_arm_probabilities(self):
        d0 = interaction(P['on_minus'], P['on_plus'])
        d1 = interaction(P['off_minus'], P['off_plus'])
        for k in (1, -.25):
            r0, r1 = d0-k, d1
            self.assertLessEqual(abs(r0-r1), 1.2)
            for arm, d in (('on', k+r0), ('off', r1)):
                h = logit(P[arm+'_minus']) + d/2
                for a, label in ((-1, 'minus'), (1, 'plus')):
                    predicted = 1/(1+math.exp(-(h+d*a/2)))
                    self.assertAlmostEqual(predicted, P[arm+'_'+label])

    def test_relabel_and_q_invariance(self):
        for flip_a, flip_b in itertools.product((False, True), repeat=2):
            sign = (-1 if flip_a else 1)*(-1 if flip_b else 1)
            self.assertAlmostEqual(delta(relabel(P, flip_a, flip_b)), sign*delta(P))
            for a, b, tau in itertools.product((-1, 1), repeat=3):
                self.assertEqual((1-tau*a*b)//2, (1-(sign*tau)*((-1 if flip_a else 1)*a)*((-1 if flip_b else 1)*b))//2)

    def test_fail_closed(self):
        with self.assertRaises(ValueError):
            simultaneous_delta_interval(P, 1, .05)
        with self.assertRaises(ValueError):
            target_interval((0, 1), .3, (0, 1))
        with self.assertRaises(ValueError):
            logit(0)


if __name__ == '__main__':
    unittest.main()
