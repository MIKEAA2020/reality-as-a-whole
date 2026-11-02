import unittest
from fractions import Fraction as F
from itertools import product
from model import (BITS,PAIRS,compatible_sections,glue_sections,admissible_glue,
                   parity_family,marginal,correlation,entropy,anticorrelated_pair,
                   supported_global_assignments,uniform_pair_constraints,rref,
                   parity_readout,duplicate_occurrence_records)


class GluingTests(unittest.TestCase):
    def test_01_exact_agreeing_sections_have_unique_union(self):
        sections=({0:0,1:1},{1:1,2:0})
        self.assertTrue(compatible_sections(sections))
        self.assertEqual(glue_sections(sections),{0:0,1:1,2:0})

    def test_02_disagreeing_sections_have_no_union(self):
        sections=({0:0,1:0},{1:1,2:0})
        self.assertFalse(compatible_sections(sections))
        self.assertIsNone(glue_sections(sections))

    def test_03_exact_union_need_not_be_globally_admissible(self):
        sections=({0:0,1:0},{1:0,2:0})
        odd=tuple(s for s in BITS if sum(s)%2)
        self.assertEqual(glue_sections(sections),{0:0,1:0,2:0})
        self.assertEqual(admissible_glue(sections,odd),())

    def test_04_each_patch_can_be_individually_admissible(self):
        odd=tuple(s for s in BITS if sum(s)%2)
        self.assertTrue(admissible_glue(({0:0,1:0},),odd))
        self.assertTrue(admissible_glue(({1:0,2:0},),odd))

    def test_05_partial_cover_can_leave_global_extensions_ambiguous(self):
        self.assertEqual(len(admissible_glue(({0:0},),BITS)),4)

    def test_06_full_exact_cover_with_no_additional_constraints_is_unique(self):
        for state in BITS:
            sections=({0:state[0],1:state[1]},{1:state[1],2:state[2]})
            self.assertEqual(admissible_glue(sections,BITS),(state,))

    def test_07_frustrated_triangle_has_consistent_single_marginals(self):
        pair=anticorrelated_pair()
        singles0={i:sum(p for s,p in pair.items() if s[0]==i) for i in (0,1)}
        singles1={i:sum(p for s,p in pair.items() if s[1]==i) for i in (0,1)}
        self.assertEqual(singles0,singles1)
        self.assertEqual(singles0,{0:F(1,2),1:F(1,2)})

    def test_08_frustrated_triangle_has_no_global_support(self):
        supports={pair:{(0,1),(1,0)} for pair in PAIRS}
        self.assertEqual(supported_global_assignments(supports),())

    def test_09_every_deterministic_triple_satisfies_at_most_two_anticorrelations(self):
        counts=[sum(s[a]!=s[b] for a,b in PAIRS) for s in BITS]
        self.assertEqual(max(counts),2)

    def test_10_parity_family_is_normalized_and_nonnegative(self):
        for t in (F(-1),F(-1,2),F(0),F(1,2),F(1)):
            p=parity_family(t)
            self.assertEqual(sum(p.values()),1)
            self.assertTrue(all(v>=0 for v in p.values()))

    def test_11_all_pair_marginals_identical_throughout_family(self):
        for t in (F(-1),F(-1,2),F(0),F(1,2),F(1)):
            for pair in PAIRS:
                self.assertEqual(set(marginal(parity_family(t),pair).values()),{F(1,4)})

    def test_12_all_single_marginals_identical_throughout_family(self):
        for t in (F(-1),F(0),F(1)):
            for i in range(3):
                self.assertEqual(marginal(parity_family(t),(i,)),{(0,):F(1,2),(1,):F(1,2)})

    def test_13_even_and_odd_joint_supports_are_disjoint(self):
        even,odd=parity_family(1),parity_family(-1)
        self.assertFalse({s for s,p in even.items() if p}&{s for s,p in odd.items() if p})

    def test_14_triple_correlation_exactly_recovers_free_parameter(self):
        for t in (F(-1),F(-1,3),F(0),F(2,3),F(1)):
            self.assertEqual(correlation(parity_family(t)),t)

    def test_15_pair_constraint_matrix_has_rank_seven(self):
        _,pivots=rref(uniform_pair_constraints())
        self.assertEqual(len(pivots),7)

    def test_16_parity_direction_spans_remaining_nullity(self):
        rows=uniform_pair_constraints()
        direction=[(-1)**sum(s) for s in BITS]
        self.assertTrue(all(sum(a*b for a,b in zip(row,direction))==0 for row in rows))
        self.assertEqual(len(BITS)-len(rref(rows)[1]),1)

    def test_17_triple_constraint_closes_rank(self):
        rows=uniform_pair_constraints()+[[F((-1)**sum(s)) for s in BITS]]
        self.assertEqual(len(rref(rows)[1]),8)

    def test_18_independence_selects_zero_correlation_as_extra_assumption(self):
        independent={s:F(1,8) for s in BITS}
        self.assertEqual(parity_family(0),independent)
        self.assertNotEqual(parity_family(1),independent)
        for pair in PAIRS:
            self.assertEqual(marginal(parity_family(1),pair),marginal(independent,pair))

    def test_19_maximum_entropy_selection_is_not_marginal_entailment(self):
        self.assertAlmostEqual(entropy(parity_family(0)),3)
        self.assertAlmostEqual(entropy(parity_family(1)),2)
        self.assertGreater(entropy(parity_family(0)),entropy(parity_family(F(1,2))))
        for pair in PAIRS:
            self.assertEqual(marginal(parity_family(0),pair),marginal(parity_family(1),pair))

    def test_20_physical_parity_readout_distinguishes_joint_models(self):
        even=parity_family(1)
        odd=parity_family(-1)
        even_probability=sum(w for s,w in even.items() if parity_readout(s)==0)
        odd_probability=sum(w for s,w in odd.items() if parity_readout(s)==0)
        self.assertEqual((even_probability,odd_probability),(1,0))

    def test_21_unique_joint_description_does_not_fix_occurrence_multiplicity(self):
        record=tuple(sorted(parity_family(0).items()))
        one=duplicate_occurrence_records(record,1)
        two=duplicate_occurrence_records(record,2)
        self.assertEqual(one[0][1],two[0][1])
        self.assertEqual(len(two),2)
        self.assertNotEqual(two[0][0],two[1][0])

    def test_22_glued_value_tuple_does_not_choose_episode_assignment(self):
        values=glue_sections(({0:0,1:1},{1:1,2:0}))
        self.assertEqual(values,{0:0,1:1,2:0})
        # The value function contains no incidence relation selecting these.
        joint=frozenset({frozenset({0,1,2})})
        separate=frozenset({frozenset({0}),frozenset({1}),frozenset({2})})
        self.assertNotEqual(joint,separate)

    def test_23_passive_coordinate_permutation_preserves_uniform_pair_data(self):
        p=parity_family(F(1,2))
        moved={(s[2],s[0],s[1]):w for s,w in p.items()}
        self.assertEqual(p,moved)
        self.assertEqual(correlation(moved),F(1,2))

    def test_24_inconsistent_parameter_is_rejected(self):
        with self.assertRaises(ValueError):
            parity_family(F(3,2))

if __name__=='__main__':
    unittest.main(verbosity=2)
