import unittest
from fractions import Fraction as F
from verification import internal_simulation_probability as model


class InternalSimulationProbabilityTests(unittest.TestCase):
    def test_bostrom_finite_ratio(self):
        self.assertEqual(model.sampled_observer_probability(100, 1000), F(10,11))

    def test_relevant_evidence_changes_the_probability(self):
        self.assertEqual(model.sampled_observer_probability(100, 900), F(9,10))
        self.assertEqual(model.sampled_observer_probability(100, 900, F(9,10), F(1,10)), F(1,2))

    def test_world_sampling_not_ratio_of_expected_counts(self):
        worlds=[(F(1,2),1,0),(F(1,2),1,99)]
        self.assertEqual(model.worlds_probability(worlds), F(99,200))
        self.assertEqual(model.worlds_probability(worlds, True), F(99,101))

    def test_bounded_nested_simulations_vary_with_resources(self):
        self.assertEqual(model.nested_fraction(F(1,2), 3), F(7,15))
        self.assertEqual(model.nested_fraction(1, 3), F(3,4))
        self.assertEqual(model.nested_fraction(2, 3), F(14,15))
        self.assertEqual(model.nested_fraction(0, 3), 0)

    def test_copying_experiential_contribution_changes_balance(self):
        original=[-1,2,-1]
        replicated=[-1,2,2,2,2,-1]
        self.assertEqual(model.total_valence(original), 0)
        self.assertEqual(model.total_valence(replicated), 6)
        self.assertEqual(model.total_valence([-7,2,2,2,2,-1]), 0)
        self.assertEqual(model.sampled_observer_probability(1,2), F(2,3))
        self.assertEqual(model.sampled_observer_probability(1,5), F(5,6))

    def test_observer_weight_steering_control(self):
        self.assertEqual(model.steering_marginals(3,1), (F(3,4),F(1,2)))
        self.assertEqual(model.steering_marginals(1,1), (F(1,2),F(1,2)))

    def test_invalid_reference_class_and_likelihood(self):
        with self.assertRaises(ValueError): model.sampled_observer_probability(0,0)
        with self.assertRaises(ValueError): model.sampled_observer_probability(1,1,2,1)
        with self.assertRaises(ValueError): model.worlds_probability([(1,0,0)])
        with self.assertRaises(ValueError): model.nested_fraction(-1,3)


if __name__ == '__main__':
    unittest.main()
