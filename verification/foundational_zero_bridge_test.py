"""Logical and finite-structure diagnostics, not metaphysical proofs."""
import itertools
import unittest


def reverse_labels(labels):
    return tuple(reversed(labels))


def orbit(labels):
    return frozenset((tuple(labels), reverse_labels(labels)))


def path_distance(labels):
    return abs(labels.index(-1)-labels.index(1))


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

    def test_zero_property_and_experiential_presence_do_not_imply_experiential_uniqueness(self):
        structures = [(-1, 1, 0, 0), (-1, 0, 1, 0)]
        for x in structures:
            self.assertEqual(sum(x), 0)
            self.assertIn(-1, x)
            self.assertIn(1, x)
        self.assertNotEqual(orbit(structures[0]), orbit(structures[1]))


if __name__ == '__main__':
    unittest.main()
