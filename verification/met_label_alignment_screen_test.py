#!/usr/bin/env python3
"""Synthetic controls for MET parsing, fold boundaries and fallback behavior."""
import math
import unittest
import met_label_alignment_screen as m


class TestLabelScreen(unittest.TestCase):
    def test_missing_and_ranges(self):
        self.assertIsNone(m.parse_rating('0', 9))
        self.assertIsNone(m.parse_rating('', 9))
        self.assertEqual(m.parse_rating('9', 9), 9)
        for bad in ('10', '-1', '1.5', 'NaN'):
            with self.assertRaises(ValueError):
                m.parse_rating(bad, 9)

    def test_cross_disjoint(self):
        rows = [{'person':p, 'song':s, 'val':v} for p,s,v in [
            ('a','x',1), ('a','y',2), ('b','x',3), ('b','y',4), ('c','z',5)]]
        known, new = m.training_sets(rows, rows[0])
        self.assertEqual(sorted(r['val'] for r in known), [3,4,5])
        self.assertEqual(sorted(r['val'] for r in new), [4,5])
        self.assertEqual(m.predict_mean(known, lambda r:r['song']=='x'), (3,False))
        self.assertEqual(m.predict_mean(new, lambda r:r['song']=='x'), (4.5,True))

    def test_scores(self):
        a = m.scores([(2,1),(1,3)])
        self.assertEqual(a['n'], 2)
        self.assertEqual(a['mae'], 1.5)
        self.assertAlmostEqual(a['rmse'], math.sqrt(2.5))


if __name__ == '__main__':
    unittest.main()
