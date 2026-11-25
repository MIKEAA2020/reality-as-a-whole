"""Cross-check stationary effects, battery controls and actual echo ledger."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import unittest

from verification.zero_stationary_battery_bridge import (
    STATES,TICKS,OLD,PREFIX,advance,relational_effect,stationary_weights,
    expectation,initial_amplitudes,predicates,
)
from verification.zero_internal_connection_flag_access_balance_test import ensemble
from verification.zero_clock_finite_reservoir_reuse_test import Q as THERMAL


class StationaryBatteryBridgeTests(unittest.TestCase):
    def test_history_and_reduced_charge_sector(self):
        # All 16 reduced labels return, including the eight with non-ready R.
        self.assertEqual(PREFIX[0],PREFIX[20])
        for t in range(TICKS):
            self.assertEqual(len(set(PREFIX[t].values())),16)
            for x in STATES:self.assertEqual(PREFIX[t+1][x],advance(t,PREFIX[t][x]))
        amps=initial_amplitudes()
        self.assertAlmostEqual(sum(a*a for a in amps.values()),1,places=14)
        self.assertEqual(sum(OLD.values()),1)
        for t in range(TICKS):
            self.assertEqual(sum(stationary_weights()[t].values()),F(1,20))
        # Full signed-charge conservation resides in the earlier reservoir
        # circuit; this reduced test does not identify B,J,R,S with energy.

    def test_relational_effect_is_a_stationary_projection(self):
        # Check [W,R_t(E)]=0 as equality on every reduced basis label. Since
        # W is a permutation, this is exact on the entire Hilbert space.
        for anchor in (0,7,8,10,13,19):
            for p in predicates().values():
                eff=relational_effect(anchor,p)
                for n,x in product(range(TICKS),STATES):
                    self.assertIn(eff[n][x],(0,1))
                    self.assertEqual(eff[n][x],eff[(n+1)%TICKS][advance(n,x)])
        # Arbitrary reference labels are not thereby operationally accessible.

    def test_global_stationary_equals_actual_old_sphere_ledger(self):
        # Exact all-time, all-cell common-interface comparison against the
        # actual prior sphere/reservoir ensemble in both auxiliary states.
        weights=stationary_weights()
        for anchor in range(TICKS):
            for name,p in predicates().items():
                got=expectation(weights,relational_effect(anchor,p))
                for q in (F(0),THERMAL):
                    expected=sum((w for b,z,s,x,f,e,st,jbit,rbit,w in ensemble(anchor,q)
                                  if p((b,(-1)**jbit,(-1)**rbit,s))),F(0))
                    self.assertEqual(got,expected,(anchor,name,q))

    def test_target_claim_joint_effects_form_a_stationary_povm(self):
        # Four actual-compatible possibilities for c=r and B=b, at a fixed
        # anchor, form orthogonal projectors summing to identity on every
        # 20-clock by 16-sign basis state.
        for t in (7,8,10,13):
            cells={(b,c):relational_effect(t,lambda x,b=b,c=c:x[0]==b and x[2]==c)
                   for b,c in product((1,-1),repeat=2)}
            for n,x in product(range(TICKS),STATES):
                self.assertEqual(sum(e[n][x] for e in cells.values()),1)
            observed={(b,c):expectation(stationary_weights(),e) for (b,c),e in cells.items()}
            if t==10:self.assertEqual(observed,{(1,1):F(1,2),(1,-1):F(0),
                                                 (-1,1):F(0),(-1,-1):F(1,2)})
        # No actual laboratory experiment or subject assertion follows.

    def test_preflight_dirty_memory_and_quality_on_same_stationary_history(self):
        p=predicates();ready=relational_effect(7,p['ready'])
        clean=stationary_weights(1);dirty=stationary_weights(-1)
        self.assertEqual(expectation(clean,ready),1)
        self.assertEqual(expectation(dirty,ready),0)
        correct=relational_effect(10,p['normal_correct'])
        error=relational_effect(10,p['normal_error'])
        inverted=relational_effect(10,p['inverted_correct'])
        self.assertEqual(expectation(clean,correct),1)
        self.assertEqual(expectation(clean,error),0)
        self.assertEqual(expectation(clean,inverted),0)
        self.assertEqual(expectation(dirty,correct),0)
        self.assertEqual(expectation(dirty,error),1)
        self.assertEqual(expectation(clean,relational_effect(10,p['quality_changed'])),F(1,2))
        self.assertEqual(expectation(clean,relational_effect(10,p['now_positive'])),F(1,2))
        self.assertEqual(expectation(clean,relational_effect(10,p['echo_positive'])),F(1,2))
        # These are compatible physical event weights, not established
        # phenomenal states, self-location weights or whole-level energy.

if __name__=='__main__':unittest.main()
