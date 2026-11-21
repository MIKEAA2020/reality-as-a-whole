import unittest
from fractions import Fraction as F
from integrated_level_history_contrast import run
from integrated_subject_horizon_audit import mismatch


class TestLevelHistoryContrast(unittest.TestCase):
    def test_joint_and_disagreement(self):
        result = run()
        p = result['probabilities']
        self.assertEqual(sum(F(x) for x in p.values()), 1)
        self.assertEqual(F(p['0->1']), F(p['1->0']))
        self.assertEqual(F(result['level_vs_onset_disagreement']), F(p['1->1']))

    def test_full_state_error(self):
        self.assertEqual(F(run()['best_full_current_state_only_error_for_onset']), F(41, 448))

    def test_witness(self):
        w = run()['matched_current_witness']
        self.assertEqual(mismatch(w['current']), 1)
        self.assertEqual(mismatch(w['previous_aligned']), 0)
        self.assertEqual(mismatch(w['previous_mismatched']), 1)
        self.assertGreater(F(w['aligned_to_current_joint_mass']), 0)
        self.assertGreater(F(w['mismatched_to_current_joint_mass']), 0)


if __name__ == '__main__':
    unittest.main()
