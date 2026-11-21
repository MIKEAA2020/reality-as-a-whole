import unittest
from fractions import Fraction as F
from itertools import product
from bohn_collective_property_gate import ALL, LEFT, RIGHT, run, toy_assignments
from integrated_subject_horizon_audit import mismatch


class TestBohnCollectiveGate(unittest.TestCase):
    def test_independent_extension_and_fixed_pairs(self):
        for s in product((-1, 1), repeat=4):
            without, with_whole = toy_assignments(s)
            self.assertNotIn(ALL, without)
            self.assertIn(ALL, with_whole)
            self.assertEqual(with_whole - without, {ALL})
            for edge in (LEFT, RIGHT):
                self.assertEqual(edge in without, bool(mismatch(s, tuple(sorted(edge)))))

    def test_physical_frequency_and_relabel_checks(self):
        result = run()
        self.assertEqual(F(result['physical_q_both_one_probability']), F(1, 16))
        self.assertEqual(result['property_assignments'], 32)
        self.assertEqual(result['simultaneous_relabel_checks'], 768)


if __name__ == '__main__':
    unittest.main()
