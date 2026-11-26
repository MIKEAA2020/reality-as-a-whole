"""Exact modal scope and positive-witness controls on the old echo."""
from fractions import Fraction as F
from itertools import product
import unittest

from verification.zero_modal_acquaintance_why import (
    CELLS,Completion,powerset,diamond,box,modal_collapse,
    observational_equivalence,necessarily_sufficient_reason,
)
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_typed_echo_process import record_components,joint_quality_slices
from verification.zero_quantum_angular_echo import mass
from verification.zero_persistent_sphere_subject_selection_test import norm2


class ModalAcquaintanceWhyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_complement_closed_scope_collapse_iff_accessible_agreement(self):
        worlds=(0,1,2);props=powerset(worlds)
        for reachable in product((False,True),repeat=3):
            acc={w:{v for v,on in zip(worlds,reachable) if on} for w in worlds}
            for w in worlds:
                self.assertEqual(modal_collapse(w,acc,props),
                                 observational_equivalence(w,acc,props))
                self.assertEqual(modal_collapse(w,acc,props),acc[w]=={w})
        # For a non-separating Boolean scope, multiple worlds can remain.
        coarse=(frozenset(),frozenset(worlds),frozenset({0,1}),frozenset({2}))
        acc={0:{0,1},1:{0,1},2:{2}}
        self.assertTrue(modal_collapse(0,acc,coarse))
        self.assertTrue(observational_equivalence(0,acc,coarse))
        self.assertFalse(modal_collapse(0,acc,props))
        self.assertTrue(diamond(0,acc,frozenset({1})))
        # Without closure under negation, the equivalence need not hold.
        positive_only=(frozenset(worlds),frozenset({0}))
        self.assertTrue(modal_collapse(0,acc,positive_only))
        self.assertFalse(observational_equivalence(0,acc,positive_only))

    def test_necessary_sufficient_condition_is_not_itself_grounding(self):
        worlds=(0,1,2);props=powerset(worlds)
        for mask in product((False,True),repeat=3):
            acc={w:{v for v,on in zip(worlds,mask) if on} for w in worlds}
            for w in worlds:
                for p in props:
                    self.assertEqual(necessarily_sufficient_reason(w,acc,props,p),
                                     box(w,acc,p))
                    # q=p is always an available purely logical witness
                    # when □p; this does not establish q grounds p.
        # No assumption about the possibility or impossibility of a genuine
        # self-explanatory identity is encoded in this propositional test.

    def test_two_separate_satisfiers_do_not_prove_a_joint_satisfier(self):
        candidates=('a','b')
        s={'a'};e={'b'}
        self.assertTrue(s and e)
        self.assertFalse(s & e)
        e.add('a')
        self.assertTrue(s & e)
        # A set control for a quantifier inference, not a model of whether
        # genuine structural and experiential intelligibility are compatible.

    def test_first_person_witness_is_the_same_with_extra_private_hypotheses(self):
        simple,plural=Completion(False),Completion(True)
        self.assertEqual(simple.reporter_field(),plural.reporter_field())
        self.assertTrue(simple.witness() and plural.witness())
        self.assertEqual(simple.visible(),plural.visible())
        self.assertEqual(sum(simple.visible().values()),1)
        self.assertEqual(len(simple.fields()),1)
        self.assertEqual(len(plural.fields()),3)
        self.assertTrue(simple.fields()['reporter'].isdisjoint(plural.fields()['private_N']))
        # Distinct private tokens are stipulated; no literal token sharing,
        # positive extra subjecthood or operational indistinguishability under
        # every possible intervention is claimed.

    def test_strong_collapse_in_each_formal_completion_does_not_select_one(self):
        simple,plural=Completion(False),Completion(True)
        worlds=(simple,plural);props=powerset(worlds)
        for actual in worlds:
            acc={simple:{simple},plural:{plural}}
            self.assertTrue(modal_collapse(actual,acc,props))
            self.assertTrue(box(actual,acc,frozenset(worlds)))  # common witness
            self.assertEqual(box(actual,acc,frozenset({plural})),actual==plural)
        # One actual world is used in each formal comparison; this does not
        # assert that both are genuinely possible or concretely instantiated.

    def test_actual_echo_cell_distribution_not_a_reporter_population(self):
        for label in (0,7,15):
            x=initial(relative_read(self.root,4,labels=(label,))[0]);total=norm2(x)
            cells={c:0. for c in CELLS}
            for (_,_,_,n,k),rows in joint_quality_slices(record_components(x)).items():
                cells[n,k]+=mass(rows)/total
            for c in CELLS:
                self.assertAlmostEqual(cells[c],0.25,places=12)
                self.assertEqual(Completion(False).visible()[c,True],F(1,4))
        # The Y and reporter-field values were hypothesized; they are not
        # extracted from the physical quantum amplitudes or actual people.

if __name__=='__main__':unittest.main()
