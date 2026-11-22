import itertools
import math
import unittest

from subject_constitution_candidate_comparison import (
    NODES, CORES, transition, observed_edges, subjects, strongly_connected_components, binomial_upper,
)


class CandidateComparisonTests(unittest.TestCase):
    def test_edges_are_interventional_dependencies(self):
        separate = {('b','a'), ('a','b'), ('d','c'), ('c','d')}
        self.assertEqual(observed_edges(False), separate)
        self.assertEqual(observed_edges(True), separate | {('d','a'), ('b','c')})

    def test_all_three_subject_counts(self):
        for g, expected in ((False, {'maximal': 2, 'marked_local': 2, 'nested': 2}),
                            (True, {'maximal': 1, 'marked_local': 2, 'nested': 3})):
            got = subjects(NODES, observed_edges(g))
            self.assertEqual({k:len(v) for k,v in got.items()}, expected)

    def test_permutation_equivariance_all_24(self):
        for perm in itertools.permutations(NODES):
            ren = dict(zip(NODES, perm))
            for g in (False, True):
                edges = observed_edges(g)
                base = subjects(NODES, edges)
                mapped = subjects(perm, {(ren[a], ren[b]) for a,b in edges},
                                  tuple(frozenset(ren[x] for x in c) for c in CORES))
                for key in base:
                    expected = frozenset(frozenset(ren[x] for x in c) for c in base[key])
                    self.assertEqual(mapped[key], expected)

    def test_public_dynamics_do_not_depend_on_constitution_rule(self):
        for g in (False, True):
            candidates = subjects(NODES, observed_edges(g))
            for s in itertools.product((0,1), repeat=4):
                for u in itertools.product((0,1), repeat=4):
                    state, inp = dict(zip(NODES,s)), dict(zip(NODES,u))
                    expected = transition(state, inp, g)
                    for candidate in candidates:
                        # Candidate metadata is not an input to the physical update.
                        self.assertEqual(transition(state, inp, g), expected, candidate)

    def test_component_partition_and_invalid_cores(self):
        self.assertEqual(strongly_connected_components(('a','b','c'), {('a','b'),('b','a')}),
                         frozenset((frozenset(('a','b')), frozenset(('c',)))))
        with self.assertRaises(ValueError):
            subjects(NODES, observed_edges(True), (frozenset(('a','b')), frozenset(('b','c','d'))))

    def test_conditional_assay_bounds(self):
        alpha = binomial_upper(30, .1, 16)
        power = 1-binomial_upper(30, .1, 15)
        self.assertLess(alpha, .00001)
        self.assertGreater(power, .999)
        self.assertAlmostEqual(power, binomial_upper(30, .9, 16))
        self.assertAlmostEqual(binomial_upper(3, .5, 2), .5)
        self.assertTrue(math.isfinite(alpha))

if __name__ == '__main__':
    unittest.main()
