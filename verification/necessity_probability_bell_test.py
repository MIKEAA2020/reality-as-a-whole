"""Scope controls for necessary outcomes, probability weights and Bell locality.

Finite examples do not establish genuine metaphysical alternatives or a physical ontology.
"""
import itertools
import math
import unittest
from fractions import Fraction as F


def chsh(a0,a1,b0,b1):
    return a0*b0+a0*b1+a1*b0-a1*b1


class NecessityProbabilityBellTests(unittest.TestCase):
    def test_fixed_probability_rule_alone_does_not_fix_an_outcome(self):
        formal_cases=[{'weight':F(1,2),'outcome':'A'}, {'weight':F(1,2),'outcome':'B'}]
        self.assertEqual(formal_cases[0]['weight'],formal_cases[1]['weight'])
        self.assertNotEqual(formal_cases[0]['outcome'],formal_cases[1]['outcome'])
        # This is only a logical control; it asserts neither case is metaphysically possible.

    def test_fixed_outcome_can_have_uncertainty_relative_to_partial_evidence(self):
        candidates=[0,1,2,3]
        outcome=lambda x:'A' if x<2 else 'B'
        actual=1
        self.assertEqual(outcome(actual),'A')
        self.assertEqual(F(sum(outcome(x)=='A' for x in candidates),len(candidates)),F(1,2))

    def test_all_deterministic_local_assignments_have_chsh_bound(self):
        values=[chsh(*x) for x in itertools.product((-1,1),repeat=4)]
        self.assertEqual({abs(x) for x in values},{2})
        self.assertLessEqual(abs(sum(values)/len(values)),2)

    def test_settings_dependent_subensembles_can_fake_chsh_algebraically(self):
        assignments=[(1,1,1,1),(1,1,1,1),(1,1,1,1),(1,1,1,-1)]
        observed=(assignments[0][0]*assignments[0][2],
                  assignments[1][0]*assignments[1][3],
                  assignments[2][1]*assignments[2][2],
                  assignments[3][1]*assignments[3][3])
        self.assertEqual(observed,(1,1,1,-1))
        self.assertEqual(observed[0]+observed[1]+observed[2]-observed[3],4)
        self.assertNotEqual(assignments[0],assignments[3])

    def test_deterministic_settings_do_not_imply_statistical_dependence(self):
        # Product frequency distribution on seeds (local variable, settings-seed).
        seeds=list(itertools.product((-1,1),range(4)))
        for setting in range(4):
            group=[lam for lam,seed in seeds if seed==setting]
            self.assertEqual(F(group.count(1),len(group)),F(1,2))
        # Both settings and local outcomes are deterministic functions of the seed.
        self.assertEqual(len(seeds),8)

    def test_quantum_singlet_correlation_violates_classical_bound(self):
        s=1/math.sqrt(2)
        a0=(1,0); a1=(0,1); b0=(s,s); b1=(s,-s)
        E=lambda a,b: -(a[0]*b[0]+a[1]*b[1])
        value=E(a0,b0)+E(a0,b1)+E(a1,b0)-E(a1,b1)
        self.assertAlmostEqual(abs(value),2*math.sqrt(2))
        self.assertGreater(abs(value),2)

    def test_squared_amplitudes_are_weights_not_single_outcome_rule(self):
        a,b=F(3,5),F(4,5)
        weights=[a*a,b*b]
        self.assertEqual(weights,[F(9,25),F(16,25)])
        self.assertEqual(sum(weights),1)
        self.assertTrue(all(0<w<1 for w in weights))
        # Probability interpretation and actual subject/outcome are extra inputs.

    def test_plenitude_of_two_types_does_not_determine_their_weight(self):
        for p in (F(1,4),F(1,2),F(3,4)):
            self.assertGreater(p,0)
            self.assertGreater(1-p,0)
            self.assertEqual(p+(1-p),1)


if __name__=='__main__': unittest.main()
