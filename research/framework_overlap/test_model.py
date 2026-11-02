import unittest
from model import *


class FrameworkOverlapTests(unittest.TestCase):
    def test_01_isometry(self):
        self.assertEqual(mul(adjoint(V),V),I2)
        self.assertEqual(mul(adjoint(CNOT),CNOT),I4)

    def test_02_preparations_are_normalized_projectors(self):
        for rho in (prepare(ZERO),prepare(ONE),BELL_PLUS,BELL_MINUS):
            self.assertEqual(trace(rho),1)
            self.assertEqual(mul(rho,rho),rho)
            self.assertEqual(adjoint(rho),rho)

    def test_03_channel_linearity_on_mixture(self):
        self.assertEqual(prepare(scale(.5,add(ZERO,ONE))),CLASSICAL_MIXTURE)
        for rho in (ZERO,ONE,PLUS,MINUS,scale(.5,I2)):
            self.assertEqual(prepare(rho),dilated_prepare(rho))

    def test_04_state_observable_duality(self):
        for rho in (ZERO,ONE,PLUS,MINUS):
            for op in PAULI.values():
                self.assertEqual(trace(mul(prepare(rho),op)),trace(mul(rho,pullback(op))))

    def test_05_pullback_is_unital(self):
        self.assertEqual(pullback(I4),I2)

    def test_06_pullback_not_multiplicative(self):
        self.assertEqual(pullback(PAULI['XI']),scale(0,I2))
        self.assertEqual(pullback(PAULI['IX']),scale(0,I2))
        self.assertEqual(pullback(PAULI['XX']),P1['X'])
        self.assertNotEqual(pullback(mul(PAULI['XI'],PAULI['IX'])),
                            mul(pullback(PAULI['XI']),pullback(PAULI['IX'])))

    def test_07_net_dimensions(self):
        self.assertEqual([len(net_basis(r)) for r in ((),('B',),('C',),('B','C'))],[1,4,4,16])

    def test_08_net_isotony(self):
        regions=(frozenset(),frozenset({'B'}),frozenset({'C'}),frozenset({'B','C'}))
        for r,s in product(regions,repeat=2):
            if r<=s:
                self.assertTrue(net_basis(r)<=net_basis(s))

    def test_09_separate_output_algebras_commute(self):
        for p in net_basis({'B'}):
            for q in net_basis({'C'}):
                self.assertTrue(commutes(p,q))

    def test_10_causal_fork_is_strict_partial_order(self):
        self.assertTrue(all(a!=b for a,b in PRECEDES))
        self.assertTrue(all((a,d) in PRECEDES for a,b in PRECEDES for c,d in PRECEDES if b==c))
        self.assertNotIn(('b','c'),PRECEDES)
        self.assertNotIn(('c','b'),PRECEDES)

    def test_11_classical_basis_copying(self):
        self.assertEqual(prepare(ZERO),kron(ZERO,ZERO))
        self.assertEqual(prepare(ONE),kron(ONE,ONE))

    def test_12_not_general_cloning_or_broadcasting(self):
        self.assertNotEqual(BELL_PLUS,kron(PLUS,PLUS))
        self.assertNotEqual(reduced(BELL_PLUS,'B'),PLUS)
        self.assertNotEqual(reduced(BELL_PLUS,'C'),PLUS)

    def test_13_same_reduced_states_do_not_determine_joint_state(self):
        for rho in (BELL_PLUS,BELL_MINUS,CLASSICAL_MIXTURE):
            for side in ('B','C'):
                self.assertEqual(reduced(rho,side),scale(.5,I2))
        self.assertEqual(len({BELL_PLUS,BELL_MINUS,CLASSICAL_MIXTURE}),3)

    def test_14_joint_correlations_distinguish_states(self):
        self.assertEqual([expectation(rho,'XX') for rho in (BELL_PLUS,BELL_MINUS,CLASSICAL_MIXTURE)],[1,-1,0])
        self.assertTrue(all(expectation(rho,'ZZ')==1 for rho in (BELL_PLUS,BELL_MINUS,CLASSICAL_MIXTURE)))

    def test_15_product_observables_reconstruct_joint_state(self):
        for rho in (BELL_PLUS,BELL_MINUS,CLASSICAL_MIXTURE,scale(.25,I4)):
            self.assertEqual(tomography(rho),rho)

    def test_16_context_counts(self):
        self.assertEqual(len(CONTEXTS),31)
        self.assertEqual([sum(len(c)==n for c in CONTEXTS) for n in (0,1,3)],[1,15,15])

    def test_17_all_contexts_commute(self):
        for context in CONTEXTS:
            self.assertTrue(all(commutes(p,q) for p,q in combinations(context,2)))

    def test_18_character_counts(self):
        for context in CONTEXTS:
            self.assertEqual(len(outcomes(context)),{0:1,1:2,3:4}[len(context)])

    def test_19_projectors_are_orthogonal_and_complete(self):
        for context in CONTEXTS:
            result=scale(0,I4)
            projectors=[projector for character,projector in outcomes(context)]
            for p in projectors:
                self.assertEqual(mul(p,p),p)
                self.assertEqual(adjoint(p),p)
                result=add(result,p)
            self.assertEqual(result,I4)
            for p,q in combinations(projectors,2):
                self.assertEqual(mul(p,q),scale(0,I4))

    def test_20_characters_match_projector_eigenvalues(self):
        for context in CONTEXTS:
            for character,projector in outcomes(context):
                for label,value in character:
                    self.assertEqual(mul(PAULI[label],projector),scale(value,projector))

    def test_21_restrictions_are_valid_characters(self):
        for small,large in product(CONTEXTS,repeat=2):
            if small<=large:
                allowed={c for c,p in outcomes(small)}
                for character,projector in outcomes(large):
                    self.assertIn(restrict(character,small),allowed)

    def test_22_presheaf_identity_and_composition(self):
        for large in CONTEXTS:
            for character,p in outcomes(large):
                self.assertEqual(restrict(character,large),character)
                for middle in CONTEXTS:
                    if middle<=large:
                        for small in CONTEXTS:
                            if small<=middle:
                                self.assertEqual(restrict(restrict(character,middle),small),restrict(character,small))

    def test_23_probabilities_nonnegative_and_normalized(self):
        for rho in (BELL_PLUS,BELL_MINUS,CLASSICAL_MIXTURE,scale(.25,I4)):
            for context in CONTEXTS:
                probabilities=distribution(rho,context)
                self.assertEqual(sum(probabilities.values()),1)
                self.assertTrue(all(p>=0 for p in probabilities.values()))

    def test_24_probabilities_agree_under_restriction(self):
        for rho in (BELL_PLUS,BELL_MINUS,CLASSICAL_MIXTURE):
            for small,large in product(CONTEXTS,repeat=2):
                if small<=large:
                    self.assertEqual(restrict_distribution(distribution(rho,large),small),distribution(rho,small))

    def test_25_mermin_contexts_are_available(self):
        for context in MERMIN_ROWS+MERMIN_COLUMNS:
            self.assertIn(frozenset(context),CONTEXTS)

    def test_26_mermin_parity_products(self):
        self.assertEqual([context_product(c) for c in MERMIN_ROWS],[I4,I4,I4])
        self.assertEqual([context_product(c) for c in MERMIN_COLUMNS],[I4,I4,scale(-1,I4)])

    def test_27_no_global_deterministic_valuation(self):
        self.assertEqual(global_valuations(),())
        # Exhausts 2^15 assignments; the report also gives the parity proof.

    def test_28_local_reset_does_not_signal_to_other_output(self):
        changed=local_reset_B(BELL_PLUS)
        self.assertEqual(trace(changed),1)
        self.assertEqual(reduced(changed,'C'),reduced(BELL_PLUS,'C'))
        self.assertEqual(reduced(changed,'B'),ZERO)
        self.assertNotEqual(changed,BELL_PLUS)

    def test_29_selective_conditioning_not_outward_signaling(self):
        p0,rho0=selective_z_B(BELL_PLUS,0)
        p1,rho1=selective_z_B(BELL_PLUS,1)
        self.assertEqual((p0,p1),(Fraction(1,2),Fraction(1,2)))
        self.assertEqual(reduced(rho0,'C'),ZERO)
        self.assertEqual(reduced(rho1,'C'),ONE)
        averaged=add(scale(float(p0),rho0),scale(float(p1),rho1))
        self.assertEqual(reduced(averaged,'C'),scale(.5,I2))

    def test_30_invalid_domains_not_silently_identified(self):
        with self.assertRaises(ValueError):
            net_basis({'a'})
        with self.assertRaises(ValueError):
            reduced(BELL_PLUS,'a')
        with self.assertRaises(ValueError):
            outcomes(frozenset({'XI','ZI'}))
        with self.assertRaises(ValueError):
            signed_product('XI','ZI')

if __name__=='__main__':
    unittest.main(verbosity=2)
