#!/usr/bin/env python3
"""Finite accounting controls, not evidence for shared experiential tokens."""
from fractions import Fraction as F
from itertools import product
import unittest


def owners(fields, event):
    return tuple(s for s, events in fields.items() if event in events)


def allocate(fields, q, shares):
    """Shares keyed by (subject, token); reject unowned or non-conserved tokens."""
    result = {s: F(0) for s in fields}
    for event, value in q.items():
        found = owners(fields, event)
        if not found:
            raise ValueError('unowned token needs a separate account')
        weights = [shares[(s, event)] for s in found]
        if any(w < 0 for w in weights) or sum(weights) != 1:
            raise ValueError('allocations must be nonnegative and sum to one')
        for s, weight in zip(found, weights):
            result[s] += weight*value
    return result


def equal_shares(fields, q):
    return {(s, event): F(1, len(owners(fields, event)))
            for event in q for s in owners(fields, event)}


def role_shares(fields, q):
    """Example only: shared event favors its positive-exclusive owner at 1/4."""
    result = {}
    for event in q:
        found = owners(fields, event)
        if len(found) == 1:
            result[(found[0], event)] = F(1)
        elif len(found) == 2:
            positive_owner = [s for s in found if any(
                q[e] > 0 and len(owners(fields, e)) == 1 for e in fields[s])]
            if len(positive_owner) != 1:
                raise ValueError('example requires exactly one positive-exclusive owner')
            for s in found:
                result[(s, event)] = F(1, 4) if s == positive_owner[0] else F(3, 4)
        else:
            raise ValueError('example supports one or two owners')
    return result


class SubjectAccountingTests(unittest.TestCase):
    def setUp(self):
        self.fields = {'A': {'P', 'C'}, 'B': {'N', 'C'}}
        self.q = {'P': F(2), 'N': F(-1), 'C': F(-1)}

    def test_token_and_incidence_totals_are_distinct(self):
        token = sum(self.q.values())
        incidence = sum(len(owners(self.fields, e))*v for e, v in self.q.items())
        self.assertEqual(token, 0)
        self.assertEqual(incidence, -1)
        self.assertEqual(sum(sum(self.q[e] for e in es) for es in self.fields.values()), incidence)

    def test_any_valid_shared_allocation_conserves_token_total(self):
        for alpha in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
            shares = {('A', 'P'): F(1), ('B', 'N'): F(1),
                      ('A', 'C'): alpha, ('B', 'C'): 1-alpha}
            values = allocate(self.fields, self.q, shares)
            self.assertEqual(values, {'A': 2-alpha, 'B': -2+alpha})
            self.assertEqual(sum(values.values()), sum(self.q.values()))

    def test_equal_and_role_based_rules_are_distinct_and_covariant(self):
        for rule, expected in ((equal_shares, (F(3, 2), F(-3, 2))),
                               (role_shares, (F(7, 4), F(-7, 4)))):
            original = allocate(self.fields, self.q, rule(self.fields, self.q))
            self.assertEqual((original['A'], original['B']), expected)
            subject_map = {'A': 'second', 'B': 'first'}
            event_map = {'P': 'z', 'N': 'x', 'C': 'y'}
            renamed_fields = {subject_map[s]: {event_map[e] for e in es}
                              for s, es in self.fields.items()}
            renamed_q = {event_map[e]: value for e, value in self.q.items()}
            transformed = allocate(renamed_fields, renamed_q, rule(renamed_fields, renamed_q))
            self.assertEqual(transformed, {subject_map[s]: value for s, value in original.items()})

    def test_equal_owner_only_function_is_forced_by_conservation(self):
        for count in range(1, 9):
            share = F(1, count)
            self.assertEqual(sum([share]*count), 1)
            for alternative in (share+F(1, 17), share-F(1, 17)):
                self.assertNotEqual(sum([alternative]*count), 1)

    def test_private_tokens_are_not_shared_token(self):
        private_fields = {'A': {'P', 'C_A'}, 'B': {'N', 'C_B'}}
        private_q = {'P': F(2), 'N': F(-1), 'C_A': F(-1), 'C_B': F(-1)}
        self.assertEqual(sum(private_q.values()), -1)
        values = allocate(private_fields, private_q, equal_shares(private_fields, private_q))
        self.assertEqual(sum(values.values()), -1)
        self.assertNotEqual(sum(private_q.values()), sum(self.q.values()))

    def test_unowned_and_invalid_shares_are_not_silently_discarded(self):
        q = dict(self.q, outside=F(2))
        with self.assertRaises(ValueError):
            allocate(self.fields, q, equal_shares(self.fields, q))
        for bad in (F(-1), F(2)):
            shares = {('A', 'P'): F(1), ('B', 'N'): F(1),
                      ('A', 'C'): bad, ('B', 'C'): 1-bad}
            with self.assertRaises(ValueError):
                allocate(self.fields, self.q, shares)

    def test_finite_conservation_does_not_depend_on_zero(self):
        for values in product(map(F, range(-2, 3)), repeat=3):
            q = dict(zip(('P', 'N', 'C'), values))
            accounts = allocate(self.fields, q, equal_shares(self.fields, q))
            self.assertEqual(sum(accounts.values()), sum(q.values()))


if __name__ == '__main__':
    unittest.main()
