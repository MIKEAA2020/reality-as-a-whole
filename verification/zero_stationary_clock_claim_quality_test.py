"""Joined claim/error and quality-contrast checks on both old clock setups."""
from fractions import Fraction as F
import unittest
from verification.zero_stationary_clock_claim_quality import joint_at_tick,conditioned_reference
from verification.zero_internal_connection_flag_access_balance_test import ensemble
from verification.zero_clock_finite_reservoir_reuse_test import Q as THERMAL

class StationaryClockClaimQualityTests(unittest.TestCase):
    def test_each_tick_against_original_full_sphere_ledger(self):
        for t in range(20):
            tab=joint_at_tick(t)
            self.assertEqual(sum(tab.values()),1)
            for q in (F(0),THERMAL):
                for correct,contrast in ((False,False),(False,True),(True,False),(True,True)):
                    expected=sum((w for b,z,s,x,f,e,st,j,r,w in ensemble(t,q)
                                  if (((-1)**r==b)==correct and (r==1)==contrast)),F(0))
                    self.assertEqual(tab.get((correct,contrast),0),expected,(t,q,correct,contrast))
            # On the physical support, the proposed quality signs differ only
            # on successful normal physical claims; no report or feeling inferred.
            self.assertEqual(tab.get((False,True),0),0)

    def test_reference_clock_joint_tables(self):
        self.assertEqual(conditioned_reference(1,2),{
            (True,False):F(1,2),(False,False):F(2,5),
            (False,True):F(0),(True,True):F(1,10)})
        self.assertEqual(conditioned_reference(2,2),{
            (True,False):F(1,2),(False,False):F(9,20),
            (False,True):F(0),(True,True):F(1,20)})
        self.assertEqual(sum(v for (correct,_),v in conditioned_reference(1,2).items() if correct),F(3,5))
        self.assertEqual(sum(v for (correct,_),v in conditioned_reference(2,2).items() if correct),F(11,20))

    def test_zero_probability_clock_condition_is_undefined(self):
        for r in (1,3):
            with self.assertRaises(ValueError):conditioned_reference(2,r)

if __name__=='__main__':unittest.main()
