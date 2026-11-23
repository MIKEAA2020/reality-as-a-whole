"""Logical and finite-structure diagnostics, not metaphysical proofs."""
import itertools
import math
from fractions import Fraction as F
import unittest


def reverse_labels(labels):
    return tuple(reversed(labels))


def orbit(labels):
    return frozenset((tuple(labels), reverse_labels(labels)))


def path_distance(labels):
    return abs(labels.index(-1)-labels.index(1))


def weighted_total(q, weights):
    return sum(w*x for w, x in zip(weights, q))


def scale_mode(q, weights, c, level=F(0)):
    shift = (c-1)*(weighted_total(q, weights)-level)/sum(weights)
    return tuple(x+shift for x in q)


def chain_laplacian(q):
    # L for a three-site undirected chain with unit couplings.
    a, b, c = q
    return (a-b, 2*b-a-c, c-b)


class FoundationBridgeTests(unittest.TestCase):
    def test_dominance_equivalent_to_any_success_implies_zero_success(self):
        # Finite candidates include zero; test every possible success pattern.
        for zero, a, b in itertools.product((False, True), repeat=3):
            dominance = zero or not (zero or a or b)  # not S(Z) -> no X succeeds
            any_success_implies_zero = not (zero or a or b) or zero
            self.assertEqual(dominance, any_success_implies_zero)

    def test_dominance_does_not_prove_zero_uniqueness(self):
        zero, other = True, True
        dominance = zero or not (zero or other)
        zero_unique = zero and not other
        self.assertTrue(dominance)
        self.assertFalse(zero_unique)

    def test_success_of_zero_does_not_identify_actual_whole(self):
        # Successful candidate Z, successful candidate W, W is not Z.
        success_z, success_w, identical = True, True, False
        dominance = success_z or not (success_z or success_w)
        self.assertTrue(dominance and success_z and success_w)
        self.assertFalse(identical)

    def test_same_chain_balance_but_distinct_experiential_relations(self):
        adjacent = (-1, 1, 0, 0)
        separated = (-1, 0, 1, 0)
        self.assertEqual(sum(adjacent), 0)
        self.assertEqual(sum(separated), 0)
        self.assertEqual(sorted(adjacent), sorted(separated))
        self.assertEqual(path_distance(adjacent), 1)
        self.assertEqual(path_distance(separated), 2)
        self.assertNotIn(separated, orbit(adjacent))

    def test_all_two_sign_chain_expansions_and_relabeling_classes(self):
        assignments = set()
        for negative in range(4):
            for positive in range(4):
                if negative == positive:
                    continue
                x = [0]*4
                x[negative], x[positive] = -1, 1
                assignments.add(tuple(x))
        self.assertEqual(len(assignments), 12)
        classes = {orbit(x) for x in assignments}
        self.assertEqual(len(classes), 6)
        class_counts = {d: sum(path_distance(next(iter(c))) == d for c in classes)
                        for d in (1, 2, 3)}
        self.assertEqual(class_counts, {1: 3, 2: 2, 3: 1})
        self.assertTrue(all(sum(x) == 0 for x in assignments))

    def test_measure_preserving_positive_scaling_forces_zero_on_finite_domain(self):
        # Every permutation preserves the uniform positive measure. Exact integer
        # arithmetic checks the pointwise relation v(F(i))=2*v(i).
        vectors = list(itertools.product(range(-2, 3), repeat=3))
        for perm in itertools.permutations(range(3)):
            compatible = [v for v in vectors if all(v[perm[i]] == 2*v[i] for i in range(3))]
            self.assertEqual(compatible, [(0, 0, 0)])

    def test_collective_scaling_group_and_differences_with_unequal_weights(self):
        q, w = (F(2), F(-1), F(3)), (F(1), F(2), F(4))
        c, d, level = F(3, 2), F(5, 4), F(-2)
        q1 = scale_mode(q, w, c, level)
        self.assertEqual(weighted_total(q1, w)-level, c*(weighted_total(q, w)-level))
        self.assertEqual(scale_mode(q1, w, d, level), scale_mode(q, w, c*d, level))
        self.assertEqual(scale_mode(q1, w, 1/c, level), q)
        for i in range(3):
            for j in range(3):
                self.assertEqual(q1[i]-q1[j], q[i]-q[j])

    def test_fixed_nontrivial_configurations_at_zero_and_other_levels(self):
        w, c = (F(1),)*3, F(2)
        for level, q in ((F(0), (F(2), F(-1), F(-1))),
                         (F(1), (F(2), F(-1), F(0)))):
            self.assertEqual(weighted_total(q, w), level)
            self.assertEqual(scale_mode(q, w, c, level), q)
            self.assertNotEqual(q, (0, 0, 0))
        self.assertNotEqual(scale_mode((F(2), F(-1), F(0)), w, c), (F(2), F(-1), F(0)))

    def test_same_dynamics_equivariant_around_any_level(self):
        q, w = (F(2), F(-1), F(3)), (F(1),)*3
        velocity = tuple(-x for x in chain_laplacian(q))
        self.assertEqual(sum(velocity), 0)
        for c, level in ((F(2), F(0)), (F(3, 2), F(4)), (F(1, 2), F(-5))):
            transformed = scale_mode(q, w, c, level)
            transformed_velocity = tuple(-x for x in chain_laplacian(transformed))
            # Derivative of S applied to velocity; level is constant.
            pushed_velocity = scale_mode(velocity, w, c, F(0))
            self.assertEqual(transformed_velocity, pushed_velocity)
            self.assertEqual(transformed_velocity, velocity)

    def test_fixed_zero_does_not_select_internal_organization(self):
        a = tuple(x/math.sqrt(3) for x in (2, -1, -1))
        b = tuple(x/math.sqrt(7) for x in (3, -2, -1))
        for v in (a, b):
            self.assertAlmostEqual(sum(v), 0)
            self.assertAlmostEqual(sum(x*x for x in v), 2)
            self.assertEqual(sum(x > 0 for x in v), 1)
            self.assertEqual(sum(x < 0 for x in v), 2)
        self.assertEqual(len(set(a)), 2)
        self.assertEqual(len(set(b)), 3)
        self.assertNotEqual(sorted(a), sorted(b))

    def test_zero_property_and_experiential_presence_do_not_imply_experiential_uniqueness(self):
        structures = [(-1, 1, 0, 0), (-1, 0, 1, 0)]
        for x in structures:
            self.assertEqual(sum(x), 0)
            self.assertIn(-1, x)
            self.assertIn(1, x)
        self.assertNotEqual(orbit(structures[0]), orbit(structures[1]))


if __name__ == '__main__':
    unittest.main()
