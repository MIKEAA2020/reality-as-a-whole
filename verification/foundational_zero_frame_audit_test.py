import unittest
from fractions import Fraction
from verification import foundational_zero_frame_audit as audit


class FoundationalZeroFrameAuditTests(unittest.TestCase):
    def test_one_current_subject_frame_power_vanishes(self):
        self.assertEqual(audit.observer_field_power(1,2,0),0)

    def test_same_event_opposite_observer_congruence_signs(self):
        self.assertAlmostEqual(audit.observer_field_power(1,1,.6),.75)
        self.assertAlmostEqual(audit.observer_field_power(1,1,-.6),-.75)
        with self.assertRaises(ValueError): audit.observer_field_power(1,1,1)

    def test_lab_energy_alignment_is_not_subject_energy_frame(self):
        E,B=1.,.5
        lab=audit.em_energy_current(E,B,0)
        beta=lab[1]/lab[0]
        self.assertAlmostEqual(beta,.8)
        subject=audit.em_energy_current(E,B,beta)
        self.assertAlmostEqual(subject[0],.375)
        self.assertAlmostEqual(subject[1],0)
        self.assertNotAlmostEqual(subject[1]/subject[0],beta)
        landau=audit.em_energy_current(E,B,.5)
        self.assertAlmostEqual(landau[1]/landau[0],.5)

    def test_identical_friedmann_zero_constraint_distinct_curvature(self):
        one=audit.flrw_data(1)
        two=audit.flrw_data(2)
        self.assertAlmostEqual(one['constraint'],0)
        self.assertAlmostEqual(two['constraint'],0)
        self.assertAlmostEqual(one['ricci'],-1)
        self.assertAlmostEqual(two['ricci'],-4)
        self.assertAlmostEqual(one['density'],.5)
        self.assertAlmostEqual(two['density'],2.)
        self.assertAlmostEqual(two['hubble']/one['hubble'],2)

    def test_passive_ohmic_model_has_no_positive_values(self):
        vals=[audit.ohmic_candidate_valence(e,conductivity=2,incidence_density=3) for e in (-2,-1,0,1,2)]
        self.assertTrue(all(v<=0 for v in vals))
        self.assertTrue(all(v<0 for v in vals if v!=0))
        self.assertEqual(vals[2],0)
        with self.assertRaises(ValueError): audit.ohmic_candidate_valence(1,-1)

    def test_every_interior_negative_fraction_can_balance(self):
        for r in (Fraction(1,10),Fraction(1,3),Fraction(1,2),Fraction(9,10)):
            plus=audit.balanced_positive_intensity(r)
            self.assertEqual(-r+(1-r)*plus,0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError): audit.flrw_data(0)
        with self.assertRaises(ValueError): audit.flrw_data(1,volume=0)
        with self.assertRaises(ValueError): audit.balanced_positive_intensity(1)


if __name__=='__main__': unittest.main()
