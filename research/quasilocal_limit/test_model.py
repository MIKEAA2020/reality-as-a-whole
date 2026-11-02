import importlib.util
from itertools import product
from pathlib import Path
import sys
import unittest
from model import *

# Independent dense-matrix reference: previous finite three-site construction.
_spec=importlib.util.spec_from_file_location('dynamical_locality_reference',Path(__file__).resolve().parents[1]/'dynamical_locality'/'model.py')
old=importlib.util.module_from_spec(_spec)
sys.modules[_spec.name]=old
_spec.loader.exec_module(old)
SAMPLES=tuple(from_word(''.join(word),-1) for word in product('IXYZ',repeat=3))


class QuasiLocalTests(unittest.TestCase):
    def test_01_one_site_pauli_relations(self):
        x,y,z=(from_word(p) for p in 'XYZ')
        self.assertEqual(x*x,ONE)
        self.assertEqual(y*y,ONE)
        self.assertEqual(z*z,ONE)
        self.assertEqual(x*y,Pauli(1,z={0}))
        self.assertEqual(y*x,Pauli(3,z={0}))

    def test_02_associativity(self):
        sample=tuple(from_word(p) for p in ('I','X','Y','Z'))
        for a,b,c in product(sample,repeat=3):
            self.assertEqual((a*b)*c,a*(b*c))

    def test_03_adjoint_reverses_multiplication(self):
        for a,b in product(SAMPLES,repeat=2):
            self.assertEqual((a*b).adjoint(),b.adjoint()*a.adjoint())

    def test_04_finite_symbolic_map_matches_previous_dense_model(self):
        for word in old.PAULI:
            p=from_word(word)
            result=finite_evolve(p,1,(0,2))
            coefficient,label=result.word(range(3))
            sign,expected=old.signed_pullback(word,0,2)
            self.assertEqual((coefficient,label),(sign,expected))

    def test_05_cnot_conjugation_is_involution(self):
        for p in SAMPLES:
            for control,target in ((-1,0),(0,1),(1,0)):
                self.assertEqual(cnot_conjugate(cnot_conjugate(p,control,target),control,target),p)

    def test_06_each_infinite_layer_is_local_involution(self):
        for p in SAMPLES:
            for parity in (0,1):
                self.assertEqual(layer(layer(p,parity),parity),p)

    def test_07_automorphism_inverse(self):
        for p in SAMPLES:
            self.assertEqual(inverse_alpha(alpha(p)),p)
            self.assertEqual(alpha(inverse_alpha(p)),p)

    def test_08_multiplicativity(self):
        for a,b in product(SAMPLES,repeat=2):
            self.assertEqual(alpha(a*b),alpha(a)*alpha(b))

    def test_09_adjoint_preservation(self):
        for p in SAMPLES:
            self.assertEqual(alpha(p.adjoint()),alpha(p).adjoint())

    def test_10_identity_extension_preserves_operators_and_products(self):
        for a,b in product(SAMPLES[:12],repeat=2):
            self.assertEqual(embed(a,(-1,1),(-3,4)),a)
            self.assertEqual(embed(a*b,(-1,1),(-3,4)),embed(a,(-1,1),(-3,4))*embed(b,(-1,1),(-3,4)))

    def test_11_invalid_embeddings_rejected(self):
        with self.assertRaises(ValueError):
            embed(from_word('X',2),(0,1),(-2,3))
        with self.assertRaises(ValueError):
            embed(from_word('X'),(-1,1),(0,1))

    def test_12_unbuffered_boundaries_change_dynamics(self):
        p=from_word('Z')
        self.assertEqual(finite_evolve(p,1,(0,1)),p)
        self.assertEqual(alpha(p),Pauli(z={-2,-1,0}))
        self.assertNotEqual(finite_evolve(p,1,(0,1)),alpha(p))

    def test_13_buffered_finite_windows_reproduce_infinite_rule(self):
        for p in SAMPLES:
            for periods in (-3,-1,0,1,2,3):
                region=cone(p.support,periods)
                window=(min(region),max(region)) if region else (-1,1)
                self.assertEqual(finite_evolve(p,periods,window),evolve(p,periods))

    def test_14_bigger_buffered_windows_agree(self):
        for p in SAMPLES:
            region=cone(p.support,2)
            window=(min(region),max(region)) if region else (-1,1)
            larger=(window[0]-3,window[1]+4)
            self.assertEqual(finite_evolve(p,2,window),finite_evolve(p,2,larger))

    def test_15_cone_radius_bound(self):
        for site in range(-4,5):
            for periods in range(-4,5):
                self.assertTrue(all(abs(i-site)<=2*abs(periods) for i in cone({site},periods)))

    def test_16_one_period_cone_is_exact_for_full_site_algebra(self):
        for site in range(-5,6):
            used=set()
            for letter in 'XYZ':
                used.update(alpha(from_word(letter,site)).support)
            self.assertEqual(frozenset(used),cone({site},1))

    def test_17_arbitrary_period_support_stays_in_cone(self):
        for p in SAMPLES:
            for periods in range(-4,5):
                self.assertTrue(evolve(p,periods).support<=cone(p.support,periods))

    def test_18_translations_by_unit_cells_commute_with_dynamics(self):
        for p in SAMPLES:
            for offset in (-4,-2,2,4):
                self.assertEqual(alpha(p.translated(offset)),alpha(p).translated(offset))

    def test_19_one_site_translation_is_not_a_claimed_symmetry(self):
        p=from_word('Z')
        self.assertNotEqual(alpha(p.translated(1)),alpha(p).translated(1))

    def test_20_far_operators_commute_after_transport(self):
        for periods in range(-4,5):
            region=cone({0},periods)
            for site in set(range(-12,13))-set(region):
                for a,b in product('XYZ',repeat=2):
                    self.assertTrue(commutes(evolve(from_word(a),periods),from_word(b,site)))

    def test_21_product_state_agrees_with_dense_matrices(self):
        state=ProductState('0',((0,'+'),))
        density=old.tensor3(old.ZERO,old.PLUS,old.ZERO)
        for word,op in old.PAULI.items():
            self.assertEqual(state.expectation(from_word(word,-1)),old.expectation(density,op))

    def test_22_evolved_local_state_recovers_ghz_overlap(self):
        state=ProductState('0',((0,'+'),))
        ghz=old.evolve(old.tensor3(old.PLUS,old.ZERO,old.ZERO),0,2)
        for word,op in old.PAULI.items():
            self.assertEqual(state.evolved_expectation(from_word(word),1),old.expectation(ghz,op))

    def test_23_invariant_states_do_not_make_dynamics_trivial(self):
        for state in (ProductState('0'),ProductState('+')):
            for p in SAMPLES:
                for periods in (-2,1,3):
                    self.assertEqual(state.evolved_expectation(p,periods),state.expectation(p))
        self.assertNotEqual(alpha(from_word('Z')),from_word('Z'))

    def test_24_contextual_parity_survives_large_support_and_time(self):
        expected=(ONE,ONE,ONE,ONE,ONE,Pauli(2))
        for start in (-5,0,4):
            for periods in (-3,0,1,4):
                self.assertEqual(context_products(mermin_contexts(start),periods),expected)

    def test_25_commutation_is_preserved(self):
        for a,b in product(SAMPLES,repeat=2):
            self.assertEqual(commutes(alpha(a),alpha(b)),commutes(a,b))

    def test_26_integer_time_composition(self):
        for p in SAMPLES:
            for n,m in product(range(-2,3),repeat=2):
                self.assertEqual(evolve(evolve(p,n),m),evolve(p,n+m))

    def test_27_product_state_restrictions_do_not_depend_on_padding(self):
        state=ProductState('0',((0,'+'),))
        for p in SAMPLES:
            embedded=embed(p,(-1,1),(-5,5))
            self.assertEqual(state.expectation(embedded),state.expectation(p))
            self.assertEqual(state.evolved_expectation(embedded,2),state.evolved_expectation(p,2))

    def test_28_scalar_phases_preserved(self):
        for phase in range(4):
            p=Pauli(phase)
            for n in (-3,0,4):
                self.assertEqual(evolve(p,n),p)
                self.assertEqual(ProductState().expectation(p),(1,1j,-1,-1j)[phase])

    def test_29_invalid_states_and_parameters_rejected(self):
        with self.assertRaises(ValueError):
            ProductState('0',((0,'+'),(0,'-')))
        with self.assertRaises(ValueError):
            ProductState('unknown')
        with self.assertRaises(ValueError):
            Pauli(x={.5})
        with self.assertRaises(ValueError):
            evolve(ONE,.5)
        with self.assertRaises(ValueError):
            from_word('Q')

    def test_30_signed_nonlocal_context_translation_is_not_relabeling_support(self):
        p=from_word('Z')
        transformed=alpha(p)
        self.assertEqual(transformed.support,frozenset({-2,-1,0}))
        self.assertTrue(transformed.hermitian())
        self.assertNotEqual(len(transformed.support),len(p.support))
        self.assertEqual(evolve(from_word('YY'),1).hermitian(),True)

    def test_31_infinite_parity_products_do_not_form_a_norm_cauchy_sequence(self):
        for n in range(6):
            a=Pauli(z=range(-n,n+1))
            b=Pauli(z=range(-n-1,n+2))
            witness=ProductState('0',((-n-1,'1'),))
            self.assertEqual(witness.expectation(a),1)
            self.assertEqual(witness.expectation(b),-1)
            # Difference has norm >= 2 by this state; <= 2 by unitarity.
            self.assertEqual(witness.expectation(a)-witness.expectation(b),2)

    def test_32_fixed_period_does_not_approach_identity_by_renaming_the_clock(self):
        a=from_word('Z')
        witness=ProductState('0',((-1,'1'),))
        self.assertEqual(witness.expectation(a),1)
        self.assertEqual(witness.expectation(alpha(a)),-1)
        # Hence ||alpha(a)-a|| = 2, independent of a chosen clock label.

if __name__=='__main__':
    unittest.main(verbosity=2)
