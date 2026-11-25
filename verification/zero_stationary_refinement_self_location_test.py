"""Physical refinement and conditional incidence checks for sphere echo."""
from collections import defaultdict
from fractions import Fraction as F
import unittest
from verification.zero_stationary_refinement_self_location import (
    coarse_outcomes,refine,disagreement,fractions,incidence_type_given_disagreement,
)


class StationaryRefinementSelfLocationTests(unittest.TestCase):
    def test_coarse_and_two_fine_descriptions(self):
        coarse=[(x,0,p) for x,p in coarse_outcomes()]
        plus=refine(1);minus=refine(-1)
        self.assertEqual([len(t) for t in (coarse,plus,minus)],[6,8,10])
        self.assertEqual([fractions(t) for t in (coarse,plus,minus)],
                         [(F(2,3),F(1,2)),(F(1,2),F(1,2)),(F(4,5),F(1,2))])
        self.assertEqual(set(p for _,_,p in plus),{F(1,8)})
        for fine in (plus,minus):
            coarsened=defaultdict(F)
            for x,label,p in fine:coarsened[x]+=p
            self.assertEqual(dict(coarsened),dict(coarse_outcomes()))

    def test_conditional_self_location_keeps_type_weight(self):
        # Product type/physical measure is the premise, not a Born theorem
        # for subjects. Disagreement is an effect with nonzero Born mass.
        for a in (F(1,4),F(1,2),F(3,4)):
            self.assertEqual(incidence_type_given_disagreement(a),a)
        self.assertEqual(sum(p for x,p in coarse_outcomes() if disagreement(x)),F(1,2))

    def test_label_refinement_does_not_create_physical_or_felt_events(self):
        self.assertEqual(sum(p for _,_,p in refine(1)),1)
        self.assertEqual(sum(p for _,_,p in refine(-1)),1)
        # Splitting a POVM effect is not proof of an actual record-producing
        # apparatus, an experiential token, or an identical lived incidence.

if __name__=='__main__':unittest.main()
