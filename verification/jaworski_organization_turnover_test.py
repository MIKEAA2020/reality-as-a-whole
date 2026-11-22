#!/usr/bin/env python3
"""Independent binomial and transition checks for the finite turnover toy."""
import unittest
from fractions import Fraction as F
from itertools import product
from math import comb
from jaworski_organization_turnover import majority, replace, repair, run


class TurnoverTest(unittest.TestCase):
    def test_one_step_majority_against_other_two_bits(self):
        # If both retained bits agree they determine the output; otherwise the
        # fair newcomer determines it. This analytic formula is independent of
        # the main script's counting approach.
        for state in product((0, 1), repeat=3):
            for site in range(3):
                kept = [state[i] for i in range(3) if i != site]
                expected = F(sum(kept), 2)
                observed = F(sum(majority(replace(state, site, b)) for b in (0, 1)), 2)
                self.assertEqual(observed, expected)
                for b in (0, 1):
                    self.assertEqual(majority(repair(replace(state, site, b))),
                                     majority(replace(state, site, b)))

    def test_three_replacements_against_binomial_probabilities(self):
        # In the unrepaired case the final bits are exactly the incoming bits.
        for start in (0, 1):
            success = sum(majority(run(start, seq, False)[0]) == start
                          for seq in product((0, 1), repeat=3))
            self.assertEqual(F(success, 8), F(sum(comb(3, k) for k in (0, 1)), 8))
            for seq in product((0, 1), repeat=3):
                self.assertEqual(run(start, seq, False)[0], seq)
                self.assertEqual(run(start, seq, True)[0], (start,)*3)

    def test_burst_failure_binomial(self):
        # k distinct sites are replaced before repair. Error is two or more
        # incoming ones, regardless of the order of the independent bits.
        for k in range(4):
            failed = 0
            for seq in product((0, 1), repeat=k):
                state = (0, 0, 0)
                for i, b in enumerate(seq):
                    state = replace(state, i, b)
                failed += majority(repair(state)) != 0
            self.assertEqual(F(failed, 2**k), F(sum(comb(k, j) for j in range(2, k+1)), 2**k))

    def test_information_record_and_token_turnover(self):
        all_records = []
        for seq in product((0, 1), repeat=3):
            final, tokens, history = run(0, seq, True)
            self.assertEqual(final, (0, 0, 0))
            self.assertEqual(tokens, ('new-0', 'new-1', 'new-2'))
            recovered = tuple(row['incoming'] for row in history)
            self.assertEqual(recovered, seq)
            all_records.append(recovered)
        self.assertEqual(len(set(all_records)), 8)

    def test_coarse_state_does_not_close(self):
        self.assertEqual(majority((0, 0, 0)), majority((0, 0, 1)))
        self.assertEqual(majority(replace((0, 0, 0), 0, 1)), 0)
        self.assertEqual(majority(replace((0, 0, 1), 0, 1)), 1)


if __name__ == '__main__':
    unittest.main()
