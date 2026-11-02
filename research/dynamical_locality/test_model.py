import unittest
from itertools import combinations
import model as m
from model import *


class DynamicalLocalityTests(unittest.TestCase):
    def test_01_gates_and_interval_maps_unitary(self):
        for start,end in ((0,0),(0,1),(1,2),(0,2)):
            u=unitary(start,end)
            self.assertEqual(mul(adjoint(u),u),I8)
            self.assertEqual(mul(u,adjoint(u)),I8)

    def test_02_unitary_composition(self):
        self.assertEqual(unitary(0,2),mul(unitary(1,2),unitary(0,1)))

    def test_03_state_evolution_composes(self):
        for rho in (INITIAL,PLUS_INITIAL,scale(.125,I8)):
            self.assertEqual(evolve(rho,0,2),evolve(evolve(rho,0,1),1,2))

    def test_04_observable_pullback_composes_contravariantly(self):
        for op in PAULI.values():
            self.assertEqual(pullback(op,0,2),pullback(pullback(op,1,2),0,1))

    def test_05_predictions_agree_across_every_interval(self):
        for start,end in ((0,1),(1,2),(0,2)):
            for rho in (INITIAL,PLUS_INITIAL,scale(.125,I8)):
                evolved=evolve(rho,start,end)
                for op in PAULI.values():
                    self.assertEqual(expectation(evolved,op),expectation(rho,pullback(op,start,end)))

    def test_06_closed_evolution_preserves_products(self):
        chosen=[PAULI[local_label(i,p)] for i in range(3) for p in 'XYZ']
        for a,b in product(chosen,repeat=2):
            self.assertEqual(pullback(mul(a,b),0,2),mul(pullback(a,0,2),pullback(b,0,2)))

    def test_07_adjoint_and_identity_preserved(self):
        self.assertEqual(pullback(I8,0,2),I8)
        for op in PAULI.values():
            self.assertEqual(pullback(adjoint(op),0,2),adjoint(pullback(op,0,2)))

    def test_08_slice_net_dimensions(self):
        for flags in product((False,True),repeat=3):
            region={i for i,v in enumerate(flags) if v}
            self.assertEqual(len(net_basis(region)),4**len(region))

    def test_09_slice_net_isotony(self):
        regions=[frozenset(i for i,v in enumerate(flags) if v) for flags in product((False,True),repeat=3)]
        for a,b in product(regions,repeat=2):
            if a<=b:
                self.assertTrue(net_basis(a)<=net_basis(b))

    def test_10_event_order_transitive_and_strict(self):
        for a in EVENTS:
            self.assertFalse(precedes(a,a))
        for a,b,c in product(EVENTS,repeat=3):
            if precedes(a,b) and precedes(b,c):
                self.assertTrue(precedes(a,c))

    def test_11_declared_causal_relations(self):
        self.assertTrue(precedes(Event(0,0),Event(2,2)))
        self.assertFalse(precedes(Event(0,0),Event(1,2)))
        self.assertTrue(causally_disconnected(Event(1,0),Event(2,2)))

    def test_12_exact_two_tick_cones(self):
        self.assertEqual(past_cone({0},0,2),frozenset({0,1}))
        self.assertEqual(past_cone({1},0,2),frozenset({0,1,2}))
        self.assertEqual(past_cone({2},0,2),frozenset({0,1,2}))

    def test_13_all_transported_observables_stay_within_cones(self):
        for start,end in ((0,1),(1,2),(0,2)):
            for label in PAULI:
                sign,translated=signed_pullback(label,start,end)
                self.assertTrue(support(translated)<=past_cone(support(label),start,end))

    def test_14_local_algebra_support_fills_declared_cone(self):
        for time in range(3):
            for site in range(3):
                observed=set()
                for p in 'XYZ':
                    observed.update(support(signed_pullback(local_label(site,p),0,time)[1]))
                self.assertEqual(frozenset(observed),past_cone({site},0,time))

    def test_15_disconnected_event_observables_commute(self):
        for a,b in combinations(EVENTS,2):
            if causally_disconnected(a,b):
                for p,q in product('XYZ',repeat=2):
                    self.assertTrue(commute(at_origin(local_label(a.site,p),a.time),at_origin(local_label(b.site,q),b.time)))

    def test_16_timelike_cross_site_observables_need_not_commute(self):
        self.assertFalse(commute(at_origin('XII',0),at_origin('IZI',2)))

    def test_17_same_wire_at_different_times_not_an_independent_copy(self):
        self.assertFalse(commute(at_origin('XII',0),at_origin('ZII',1)))
        self.assertEqual(len(I8),8)  # Not 2^9 for nine wire-time labels.

    def test_18_whole_slice_map_is_a_basis_bijection(self):
        for time in range(3):
            labels=[signed_pullback(label,0,time)[1] for label in PAULI]
            self.assertEqual(len(set(labels)),64)

    def test_19_local_reset_is_trace_preserving(self):
        for site in range(3):
            total=scale(0,I8)
            for k in reset_kraus(site):
                total=add(total,mul(adjoint(k),k))
            self.assertEqual(total,I8)

    def test_20_unitaries_outside_input_cone_do_not_change_predictions(self):
        for time in (1,2):
            for out_site in range(3):
                outside=set(range(3))-set(past_cone({out_site},0,time))
                for site in outside:
                    for kind in ('X','Z'):
                        for rho in (INITIAL,PLUS_INITIAL):
                            baseline=evolve(rho,0,time)
                            changed=perturbed_evolve(rho,0,site,kind,time)
                            self.assertEqual(region_reduce(baseline,{out_site}),region_reduce(changed,{out_site}))

    def test_21_resets_outside_cone_do_not_change_predictions(self):
        for start,end in ((0,1),(1,2),(0,2)):
            for out_site in range(3):
                outside=set(range(3))-set(past_cone({out_site},start,end))
                for site in outside:
                    for rho in (INITIAL,PLUS_INITIAL):
                        changed=perturbed_evolve(rho,start,site,'reset',end)
                        self.assertEqual(region_reduce(changed,{out_site}),region_reduce(evolve(rho,0,end),{out_site}))

    def test_22_influence_propagates_only_after_second_gate(self):
        base1=evolve(INITIAL,0,1)
        changed1=perturbed_evolve(INITIAL,0,0,'X',1)
        self.assertEqual(expectation(base1,PAULI['IIZ']),expectation(changed1,PAULI['IIZ']))
        base2=evolve(INITIAL,0,2)
        changed2=perturbed_evolve(INITIAL,0,0,'X',2)
        self.assertEqual(expectation(base2,PAULI['IIZ']),1)
        self.assertEqual(expectation(changed2,PAULI['IIZ']),-1)

    def test_23_quantum_phase_can_influence_classical_control_wire(self):
        baseline=evolve(PLUS_INITIAL,0,1)
        changed=perturbed_evolve(PLUS_INITIAL,0,1,'Z',1)
        self.assertEqual(expectation(baseline,PAULI['XII']),1)
        self.assertEqual(expectation(changed,PAULI['XII']),-1)

    def test_24_ghz_preparation(self):
        rho=tensor3(PLUS,ZERO,ZERO)
        expected=matrix([[.5 if i in (0,7) and j in (0,7) else 0 for j in range(8)] for i in range(8)])
        self.assertEqual(evolve(rho,0,2),expected)
        self.assertEqual(trace(expected),1)
        self.assertEqual(mul(expected,expected),expected)

    def test_25_partial_trace_preserves_local_predictions(self):
        rho=evolve(tensor3(PLUS,ZERO,ZERO),0,2)
        for site in range(3):
            reduced=region_reduce(rho,{site})
            for p in 'IXYZ':
                self.assertEqual(expectation(rho,PAULI[local_label(site,p)]),exact_real(trace(mul(reduced,P1[p]))))
        self.assertEqual(region_reduce(rho,()),matrix(((1,),)))
        self.assertEqual(region_reduce(rho,{0,1,2}),rho)

    def test_26_reduced_state_does_not_close_neighbor_dependent_dynamics(self):
        a=tensor3(ZERO,ZERO,ZERO)
        b=tensor3(ZERO,ONE,ZERO)
        self.assertEqual(region_reduce(a,{2}),region_reduce(b,{2}))
        self.assertNotEqual(region_reduce(evolve(a,1,2),{2}),region_reduce(evolve(b,1,2),{2}))

    def test_27_intervention_time_changes_history(self):
        rho=tensor3(ONE,ZERO,ZERO)
        early=perturbed_evolve(rho,0,1,'reset',2)
        late=perturbed_evolve(rho,1,1,'reset',2)
        self.assertNotEqual(early,late)
        self.assertEqual(expectation(early,PAULI['IIZ']),-1)
        self.assertEqual(expectation(late,PAULI['IIZ']),1)

    def test_28_contextual_parity_obstruction_is_transport_invariant(self):
        expected=(I8,I8,I8,I8,I8,scale(-1,I8))
        for time in range(3):
            self.assertEqual(transported_mermin_products(time),expected)

    def test_29_transport_preserves_context_commutation(self):
        for time in range(3):
            for context in m._ref.MERMIN_ROWS+m._ref.MERMIN_COLUMNS:
                for p,q in combinations(context,2):
                    self.assertTrue(commute(at_origin(p+'I',time),at_origin(q+'I',time)))

    def test_30_signed_pauli_transport_retains_minus_signs(self):
        self.assertEqual(signed_pullback('YYI',0,1),(-1,'XZI'))
        for label in PAULI:
            sign,translated=signed_pullback(label,0,2)
            self.assertEqual(pullback(PAULI[label],0,2),scale(sign,PAULI[translated]))

    def test_31_first_slice_recovers_previous_bell_construction(self):
        rho=tensor3(PLUS,ZERO,ZERO)
        self.assertEqual(evolve(rho,0,1),kron(m._ref.BELL_PLUS,ZERO))

    def test_32_invalid_domains_rejected(self):
        for interval in ((-1,1),(2,1),(0,3)):
            with self.assertRaises(ValueError):
                unitary(*interval)
        with self.assertRaises(ValueError):
            Event(3,0)
        with self.assertRaises(ValueError):
            cnot(0,0)
        with self.assertRaises(ValueError):
            net_basis({3})

if __name__=='__main__':
    unittest.main(verbosity=2)
