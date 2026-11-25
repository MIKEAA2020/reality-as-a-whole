"""Incidence redescription and conditional Born reconstruction.

Equal-labelled slots are not assumed to be actual subjects. Effect
noncontextuality and state certainty are hypotheses, not consequences of zero.
"""
import unittest
import numpy as np
from verification.zero_integrated_experience_necessity_test import incidence_distribution

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1.,-1.]).astype(complex)
H2=np.array([[1,1],[1,-1]],complex)/np.sqrt(2)
H4=np.kron(H2,H2)


def refine(mu,split_zero):
    # Same fixed spectator state |0>, described in a k-dependent basis.
    # This is an algebraic refinement, not an assumed physical measurement
    # or the production of distinct actual subjects.
    basis=np.eye(4,dtype=complex)
    ket=basis[:,0]
    out=np.zeros(mu.shape+(4,))
    for i,k in enumerate((-1,0,1)):
        change=(k==0)==split_zero
        u=H4 if change else basis
        probabilities=abs(u.conj().T@ket)**2
        out[i]=mu[i,:,:,None]*probabilities
    return out


def slot_count_k0(table):
    mask=table>1e-12
    return int(mask[1].sum()),int(mask.sum())


class IncidenceRefinementBornTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.labels,cls.weights,cls.mu=incidence_distribution()

    def test_original_ten_incidence_count_and_physical_weights(self):
        np.testing.assert_allclose(self.labels,[-1,0,1])
        self.assertEqual(np.count_nonzero(self.mu>1e-12),10)
        self.assertEqual(np.count_nonzero(self.mu[1]>1e-12),2)
        self.assertAlmostEqual(self.mu[1].sum(),.5,places=13)
        self.assertAlmostEqual(2/10,.2,places=13)
        actual=self.mu[self.mu>1e-12]
        np.testing.assert_allclose(sorted(actual),[1/16]*8+[1/4]*2,atol=1e-14)

    def test_equal_probability_refinement_makes_unit_counts_match_born(self):
        fine=refine(self.mu,True)
        np.testing.assert_allclose(fine.sum(axis=3),self.mu,atol=1e-14)
        self.assertEqual(slot_count_k0(fine),(8,16))
        np.testing.assert_allclose(fine[fine>1e-12],np.ones(16)/16,atol=1e-14)
        self.assertAlmostEqual(8/16,self.mu[1].sum(),places=13)
        # The spectator is in the same physical |0> state in both bases.
        # Equal effect probabilities do not imply 16 actual subject instances.
        np.testing.assert_allclose(H4.conj().T@H4,np.eye(4),atol=1e-14)

    def test_different_basis_refinement_changes_naive_counts_not_coarse_state(self):
        fine=refine(self.mu,False)
        np.testing.assert_allclose(fine.sum(axis=3),self.mu,atol=1e-14)
        self.assertEqual(slot_count_k0(fine),(2,34))
        self.assertAlmostEqual(2/34,1/17,places=13)
        self.assertAlmostEqual(fine[1].sum(),.5,places=13)
        for v in (self.mu[:,:,:,None],refine(self.mu,True),fine):
            np.testing.assert_allclose(v,v[:,::-1,::-1,:],atol=1e-14)
        # The three slot ratios 1/5, 1/2, 1/17 are not predictions of
        # three physically identical actual-subject ontologies.

    def test_one_effect_in_two_contexts_has_same_born_but_different_slot_counts(self):
        ket=np.array([1.,1.])/np.sqrt(2)
        rho=np.outer(ket,ket.conj())
        e=np.diag([.5,0.])
        c1=(e,I-e)
        c2=(e,e,I-2*e)
        for context in (c1,c2):
            np.testing.assert_allclose(sum(context),I,atol=1e-14)
            for op in context:self.assertGreaterEqual(np.linalg.eigvalsh(op)[0],-1e-14)
        self.assertAlmostEqual(np.trace(rho@c1[0]).real,.25,places=13)
        self.assertAlmostEqual(np.trace(rho@c2[0]).real,.25,places=13)
        self.assertNotEqual(1/2,1/3)
        # Repeated effects are separate outcome labels; identifying them as
        # the same first-person incidence is a substantive extra premise.

    def test_effect_probabilities_reconstruct_given_qubit_state(self):
        ket=np.array([1.,1j])/np.sqrt(2)
        rho=np.outer(ket,ket.conj())
        observables=(X,Y,Z)
        probs=[np.trace(rho@(I+a)/2).real for a in observables]
        reconstructed=(I+sum((2*p-1)*a for p,a in zip(probs,observables)))/2
        np.testing.assert_allclose(reconstructed,rho,atol=1e-14)
        proj=rho
        self.assertAlmostEqual(np.trace(reconstructed@proj).real,1,places=13)
        # In arbitrary finite dimension, effect additivity gives a density σ;
        # Tr(σ|ψ><ψ|)=1 forces σ=|ψ><ψ|. This numerical qubit is only an
        # illustration of the analytic proof, not a test over all effects.

    def test_mixed_support_certainty_alone_does_not_fix_weights(self):
        rho=np.diag([.8,.2]);sigma=np.diag([.3,.7]);p=I
        self.assertAlmostEqual(np.trace(rho@p).real,1,places=13)
        self.assertAlmostEqual(np.trace(sigma@p).real,1,places=13)
        self.assertNotAlmostEqual(rho[0,0],sigma[0,0],places=4)
        # Purifying ρ permits a pure-state certainty condition only if the
        # relevant global projector and its incidence interpretation exist.

if __name__=='__main__':unittest.main()
