"""Exact finite tests of a proposed symmetry and incidence interface."""
from fractions import Fraction as F
from itertools import product
import unittest
from verification.zero_stationary_battery_bridge import (
    STATES,TICKS,PREFIX,advance,initial_amplitudes,stationary_weights,
    relational_effect,expectation,predicates,
)
from verification.zero_stationary_subject_incidence import (
    ANCHOR,anchor_flip,stationary_flip,quality_at_anchor,incidence_weights,joint_swap,
)


class StationarySubjectIncidenceTests(unittest.TestCase):
    def test_physical_active_flip_swaps_quality_on_each_anchor_label(self):
        for b,j,r,s in STATES:
            x=(b,j,r,s);y=anchor_flip(x)
            self.assertEqual(anchor_flip(y),x)
            self.assertEqual((y[0],y[2],y[3]),(b,r,s))
            self.assertEqual(y[3]*y[1],s*j*r)
            self.assertEqual(y[3]*y[1]*y[2],s*j)

    def test_stationary_lift_commutes_with_clock_and_preserves_pure_reduced_state(self):
        # Global clock-conditional unitary: permutation on the full 320 basis
        # states, not asserted implementable or local in the full physical model.
        for n,x in product(range(TICKS),STATES):
            y=stationary_flip(n,x)
            self.assertEqual(stationary_flip(n,y),x)
            self.assertEqual(advance(n,y),stationary_flip((n+1)%TICKS,advance(n,x)))
        amps=initial_amplitudes()
        for x in STATES:
            a=amps.get(x,0.0)
            y=stationary_flip(0,x)
            self.assertAlmostEqual(a,amps.get(y,0.0),places=14)
        for p in ('now','echo'):
            other='echo' if p=='now' else 'now'
            for n,x in product(range(TICKS),STATES):
                self.assertEqual(quality_at_anchor(n,stationary_flip(n,x),p),
                                 quality_at_anchor(n,x,other))
        w=stationary_weights()
        for n,x in product(range(TICKS),STATES):
            self.assertEqual(w[n][x],w[n][stationary_flip(n,x)])

    def test_fixed_target_and_ready_controls_unchanged(self):
        # The swap is a genuine nontrivial physical change: it flips J on
        # R=- while preserving these specific benchmark predicates.
        for name,t in (('normal_correct',10),('normal_error',10),('ready',7)):
            eff=relational_effect(t,predicates()[name])
            for n,x in product(range(TICKS),STATES):
                self.assertEqual(eff[n][x],eff[n][stationary_flip(n,x)])
        self.assertTrue(any(stationary_flip(n,x)!=x for n,x in product(range(TICKS),STATES)))
        self.assertEqual(expectation(stationary_weights(),relational_effect(10,predicates()['normal_correct'])),1)

    def test_symmetry_selects_equal_type_weights_given_extra_invariance(self):
        # Within the strong product extension m(type,E)=alpha_type Born(E),
        # requiring invariance under the *combined active* swap forces 1/2.
        for a in (F(1,4),F(1,2),F(3,4)):
            w=incidence_weights(a)
            inv=all(w[k]==w[joint_swap(*k)] for k in w)
            self.assertEqual(inv,a==F(1,2))
            self.assertEqual(sum(w.values()),1)
            self.assertEqual(sum(v for (n,x,p),v in w.items() if p=='now'),a)
            for n,x in product(range(TICKS),STATES):
                self.assertEqual(sum(w[n,x,p] for p in ('now','echo')),stationary_weights()[n][x])
        # Relabeling with the measure transformed is not the invariance premise.

    def test_shared_physical_outcomes_and_actual_candidate_quality(self):
        for a in (F(1,4),F(1,2),F(3,4)):
            w=incidence_weights(a)
            sign={v:sum(weight for (n,x,p),weight in w.items() if quality_at_anchor(n,x,p)==v)
                  for v in (1,-1)}
            self.assertEqual(sign,{1:F(1,2),-1:F(1,2)})
            diff=sum(weight for (n,x,p),weight in w.items()
                     if quality_at_anchor(n,x,'now')!=quality_at_anchor(n,x,'echo'))
            self.assertEqual(diff,F(1,2))
            # Balance is an ensemble/model property, not destruction of a
            # negative occurrence, physical energy or evidence of feeling.

    def test_symmetry_not_all_operators_nor_each_pulse(self):
        # D genuinely changes J and does not commute with first T, so it is
        # not a symmetry of every primitive local operation of the old model.
        found=False
        for x in STATES:
            if anchor_flip(advance(7,x)) != advance(7,anchor_flip(x)):
                found=True
        self.assertTrue(found)
        self.assertTrue(any(anchor_flip(x)[1]!=x[1] for x in STATES))

if __name__=='__main__':unittest.main()
