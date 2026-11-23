"""Exact checks for a conditional five-ray conservation / qubit-effects bridge.

No empirical probability, physical interaction, consciousness or zero foundation
is assumed to have been established by these checks.
"""
import itertools
import unittest
from fractions import Fraction as F

from verification.zero_sphere_five_ray_conservation import (
    cofactor_null_relation, center_frame_energy_numerators, scale,
)
from verification.zero_sphere_relative_orientation import lorentz_dot


def ray(x, y=0):
    x, y = F(x), F(y)
    return (1+x*x+y*y, 2*x, 2*y, x*x+y*y-1)


def bridge(rays):
    result = cofactor_null_relation(rays)
    coeff = result['coefficients']
    nums, mass2 = center_frame_energy_numerators(rays, coeff, result['pair'])
    p = [scale(abs(c), k) for c, k in zip(coeff, rays)]
    q = [x / mass2 for x in nums]
    # Center-frame unit-direction scalar products; no square roots required.
    dots = [[1 + lorentz_dot(p[i], p[j])*mass2/(nums[i]*nums[j])
             for j in range(5)] for i in range(5)]
    return result, q, dots


def boost(v):
    # Exact proper Lorentz boost with velocity 3/5, gamma 5/4.
    t, x, y, z = v
    return ((5*t-3*x)/4, (5*x-3*t)/4, y, z)


class ConservationBornBridgeTests(unittest.TestCase):
    def setUp(self):
        self.rays = [ray(0), ray(2), ray(1), ray(0, 1), ray(0, -1)]
        self.result, self.q, self.dots = bridge(self.rays)

    def test_exact_intrinsic_energy_weights(self):
        self.assertEqual(self.result['pair'], [0, 1])
        self.assertEqual(self.result['triple'], [2, 3, 4])
        self.assertEqual(self.q, [F(1,2), F(1,2), F(1,3), F(1,3), F(1,3)])

    def test_each_side_has_unit_weight_and_zero_bloch_vector(self):
        for side in ('pair', 'triple'):
            indices = self.result[side]
            self.assertEqual(sum(self.q[i] for i in indices), 1)
            # Zero vector iff its squared Euclidean norm is zero.
            norm2 = sum(self.q[i]*self.q[j]*self.dots[i][j]
                        for i in indices for j in indices)
            self.assertEqual(norm2, 0)

    def test_both_groups_form_povms_and_born_weights_in_maximally_mixed_state(self):
        for side in ('pair', 'triple'):
            for i in self.result[side]:
                # E_i=2q_i Π_i. Its nonzero eigenvalue must not exceed one.
                self.assertGreater(2*self.q[i], 0)
                self.assertLessEqual(2*self.q[i], 1)
                # tr[(I/2) E_i] = q_i, since tr Π_i = 1.
                self.assertEqual(F(1,2)*2*self.q[i], self.q[i])
            # Their sum is I because Σq_i=1 and Σq_i n_i=0 (prior test).

    def test_signed_axis_balances_on_each_side(self):
        axis = self.result['pair'][0]
        self.assertEqual(self.dots[axis], [1, -1, F(-1,2), F(1,4), F(1,4)])
        for side in ('pair', 'triple'):
            self.assertEqual(sum(self.q[i]*self.dots[axis][i]
                                 for i in self.result[side]), 0)

    def test_asymmetric_example_needs_intrinsic_weights(self):
        rays = [ray(0), ray(1), ray(3), ray(0,1), ray(0,2)]
        result, q, dots = bridge(rays)
        self.assertEqual(result['pair'], [2,3])
        self.assertEqual(q, [F(1,8),F(2,5),F(1,2),F(1,2),F(19,40)])
        axis = result['pair'][0]
        triple = result['triple']
        self.assertEqual(sum(q[i]*dots[axis][i] for i in triple), 0)
        self.assertEqual(sum(dots[axis][i] for i in triple), F(-13,190))

    def test_boost_rescaling_and_permutation_preserve_weights_and_angles(self):
        transformed = [boost(scale(s, v)) for s, v in zip((1,2,3,4,5), self.rays)]
        _, q, dots = bridge(transformed)
        self.assertEqual(q, self.q)
        self.assertEqual(dots, self.dots)
        for perm in itertools.permutations(range(5)):
            _, qp, dp = bridge([transformed[i] for i in perm])
            self.assertEqual(qp, [self.q[i] for i in perm])
            self.assertEqual(dp, [[self.dots[i][j] for j in perm] for i in perm])

    def test_state_is_extra_input_not_fixed_by_povm_alone(self):
        # For pair projectors, maximally mixed gives 1/2 each; the pure
        # first projector gives 1 and 0. The POVM itself is unchanged.
        q0 = self.q[self.result['pair'][0]]
        self.assertEqual(q0, F(1,2))
        pure_born_first = F(1,2)*(1+self.dots[0][0])
        pure_born_second = F(1,2)*(1+self.dots[0][1])
        self.assertEqual((pure_born_first, pure_born_second), (1,0))

    def test_effect_noncontextual_individual_zero_one_value_impossible(self):
        # POVM (I/2,I/2): normalization and equal value for equal effects
        # demand 2v=1, so no v in {0,1}. This says nothing against
        # deterministic contextual responses or nontrivial ensemble weights.
        self.assertFalse(any(2*v == 1 for v in (0,1)))
        self.assertEqual(2*F(1,2), 1)


if __name__ == '__main__':
    unittest.main()
