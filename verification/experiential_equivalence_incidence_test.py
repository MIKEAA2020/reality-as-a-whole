#!/usr/bin/env python3
"""Finite annotated-structure controls, not actual experience or subjecthood."""
from itertools import permutations
import unittest


def canonical(q, blocks, order=(), anchor=None):
    return (tuple(q), tuple(sorted(tuple(sorted(block)) for block in blocks)),
            tuple(sorted(order)), anchor)


def relabel(world, pi):
    """pi maps old occurrence indices to new indices; all annotations travel."""
    q, blocks, order, anchor = world
    new_q = [None]*len(q)
    for old, new in enumerate(pi):
        new_q[new] = q[old]
    new_blocks = [tuple(pi[i] for i in block) for block in blocks]
    new_order = [(pi[i], pi[j]) for i, j in order]
    return canonical(new_q, new_blocks, new_order, None if anchor is None else pi[anchor])


def orbit(world):
    return frozenset(relabel(world, pi) for pi in permutations(range(len(world[0]))))


def all_partitions(elements):
    if not elements:
        yield ()
        return
    first, *rest = elements
    for partition in all_partitions(rest):
        yield ((first,),) + partition
        for index in range(len(partition)):
            yield partition[:index] + ((first,)+partition[index],) + partition[index+1:]


def subject_totals(world):
    q, blocks, _, _ = world
    return tuple(sorted(sum(q[i] for i in block) for block in blocks))


class ExperientialEquivalenceTests(unittest.TestCase):
    def setUp(self):
        self.q = (1, -1, 0)  # stipulated positive, negative, neutral roles
        self.parts = [canonical(self.q, p)[1] for p in all_partitions([0, 1, 2])]

    def test_five_nonisomorphic_incidence_organizations(self):
        self.assertEqual(len(self.parts), 5)
        worlds = [canonical(self.q, p) for p in self.parts]
        orbits = [orbit(w) for w in worlds]
        for i in range(len(orbits)):
            for j in range(i):
                self.assertTrue(orbits[i].isdisjoint(orbits[j]))
        self.assertEqual(len(set().union(*orbits)), 30)
        self.assertTrue(all(sum(w[0]) == 0 for w in worlds))

    def test_same_subject_totals_not_same_incidence(self):
        p_neutral = canonical(self.q, ((0, 2), (1,)))
        n_neutral = canonical(self.q, ((1, 2), (0,)))
        self.assertEqual(subject_totals(p_neutral), (-1, 1))
        self.assertEqual(subject_totals(p_neutral), subject_totals(n_neutral))
        self.assertNotIn(n_neutral, orbit(p_neutral))

    def test_a_relabelling_preserves_every_incidence(self):
        w = canonical(self.q, ((0, 2), (1,)), ((0, 1),), 0)
        perm = (1, 2, 0)
        renamed = relabel(w, perm)
        self.assertEqual(renamed[0], (0, 1, -1))
        self.assertEqual(renamed[1], ((0, 1), (2,)))
        self.assertEqual(renamed[2], ((1, 2),))
        self.assertEqual(renamed[3], 1)
        self.assertEqual(subject_totals(renamed), subject_totals(w))
        self.assertEqual(sum(renamed[0]), sum(w[0]))

    def test_opposite_temporal_relations_are_distinct(self):
        earlier_positive = canonical(self.q, ((0, 1, 2),), ((0, 1),))
        earlier_negative = canonical(self.q, ((0, 1, 2),), ((1, 0),))
        self.assertEqual(subject_totals(earlier_positive), subject_totals(earlier_negative))
        self.assertNotIn(earlier_negative, orbit(earlier_positive))

    def test_anchor_restricts_equivalence(self):
        singles = ((0,), (1,), (2,))
        worlds = [canonical(q, singles, anchor=0) for q in permutations(self.q)]
        classes = {orbit(w) for w in worlds}
        self.assertEqual(len(classes), 3)
        self.assertEqual({w[0][w[3]] for w in worlds}, {-1, 0, 1})
        # Unanchored the same labelled q arrangements lie in one orbit.
        unanchored = [canonical(q, singles) for q in permutations(self.q)]
        self.assertEqual(len({orbit(w) for w in unanchored}), 1)

    def test_sign_roles_are_not_erased_by_permutation(self):
        w = canonical(self.q, ((0,), (1,), (2,)))
        other = relabel(w, (1, 0, 2))
        self.assertEqual(other[0], (-1, 1, 0))
        self.assertEqual(other[0][1], w[0][0])  # old positive remains positive
        self.assertEqual(other[0][0], w[0][1])  # old negative remains negative


if __name__ == '__main__':
    unittest.main()
