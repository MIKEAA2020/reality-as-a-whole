"""Intrinsic point tangent, coordinate-change and original echo controls."""
from fractions import Fraction as F
from itertools import product
import unittest

from verification.zero_intrinsic_point_jets import (
    jet,add,multiply,evaluate,derivative,dot,cosine_squared,diagonal,
    shear_ratio_interval,truncated_multiply,
)
from verification.zero_joint_quality_incidence_root import ANGLES,quality,R
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_quantum_angular_echo import embed
from verification.zero_persistent_sphere_subject_selection_test import norm2


class IntrinsicPointJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_one_real_point_can_have_nontrivial_formal_tangent(self):
        for n in range(4):
            eps=[jet(0,[int(i==j) for i in range(n)]) for j in range(n)]
            for a in eps:
                self.assertEqual(evaluate(a),0)
                self.assertEqual(multiply(a,a),jet(0,[0]*n))
            for i,j in product(range(n),repeat=2):
                self.assertEqual(multiply(eps[i],eps[j]),jet(0,[0]*n))
                self.assertEqual(derivative(eps[i],[int(k==j) for k in range(n)]),int(i==j))
        # An R-algebra character to R must annihilate every nilpotent;
        # the displayed basis derivations exist despite the single real point.

    def test_leibniz_rule_for_arbitrary_rational_jets(self):
        for c,d in product((-1,0,2),repeat=2):
            a=jet(c,(1,-2,3));b=jet(d,(2,1,-1));v=(F(1,2),-3,4)
            self.assertEqual(derivative(multiply(a,b),v),
                             evaluate(a)*derivative(b,v)+evaluate(b)*derivative(a,v))
            self.assertEqual(derivative(add(a,b),v),derivative(a,v)+derivative(b,v))

    def test_reverse_descriptions_cancel_but_are_not_two_occurrences(self):
        f=jet(7,(1,2,-1));u=(1,0,0);v=(0,1,0)
        difference=derivative(f,u)-derivative(f,v)
        reverse=derivative(f,v)-derivative(f,u)
        self.assertEqual((difference,reverse),(-1,1))
        self.assertEqual(difference+reverse,0)
        self.assertEqual(evaluate(f),7)
        # Counting both descriptions as actual experiences is an extra premise.

    def test_point_alone_does_not_fix_tangent_dimension_or_angle(self):
        v=(1,0,0);w=(1,1,0);anisotropy=(1,2,1)
        self.assertEqual(cosine_squared(v,w),F(1,2))
        self.assertEqual(cosine_squared(diagonal(v,anisotropy),diagonal(w,anisotropy)),F(1,5))
        # Applying the transformation only to the vectors while retaining the
        # metric is active; a passive coordinate change also transports metric.
        self.assertEqual(shear_ratio_interval(F(1,3),4),F(13,3))
        with self.assertRaises(ValueError):cosine_squared((0,0,0),w)
        with self.assertRaises(ValueError):multiply(jet(1,(1,)),jet(1,(1,0)))

    def test_same_first_order_direction_does_not_fix_higher_structure(self):
        e2=(0,1);e3=(0,1,0)
        self.assertEqual(truncated_multiply(e2,e2),(0,0))
        self.assertEqual(truncated_multiply(e3,e3),(0,0,1))
        self.assertEqual(truncated_multiply(truncated_multiply(e3,e3),e3),(0,0,0))
        # Both are pointed real algebras with one-dimensional m/m²,
        # but the second retains a nonzero second-order nilpotent.
        with self.assertRaises(ValueError):truncated_multiply((),())

    def test_actual_complex_echo_supports_four_formal_relative_angles(self):
        # The prior 4-bin construction attaches these scalar cosines to an
        # angular register. This test checks the recorded sign/mass data; it
        # does not claim the formal jet algebra has been physically realized.
        self.assertEqual(ANGLES,(F(-3,4),F(-1,4),F(1,4),F(3,4)))
        self.assertEqual(tuple(-1 if u<0 else 1 for u in ANGLES),R)
        for label in (0,7,15):
            x=initial(relative_read(self.root,4,labels=(label,))[0]);total=norm2(x)
            weights={u:0. for u in ANGLES}
            for s in (1,-1):
                _,_,rows=embed(x,s,4)
                for i,u in enumerate(ANGLES):
                    weights[u]+=sum(norm2(part[i]) for part in rows)/total
                    n,k=quality(i,s)
                    self.assertEqual(n*k,R[i])
            for u in ANGLES:self.assertAlmostEqual(weights[u],0.25,places=12)

if __name__=='__main__':unittest.main()
