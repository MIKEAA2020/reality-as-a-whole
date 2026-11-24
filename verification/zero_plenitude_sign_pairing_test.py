"""Intrinsic sign-pairing checks on the existing zero-energy sphere model.

Pairing physical energy labels is not evidence that experiences are paired.
The matching clock and encoded swap are assumed constructions, not derived laws.
"""
import math
import unittest
import numpy as np
from verification.zero_energy_recollapse_clock_test import BalancedRecollapse
from verification.zero_recollapse_sphere_memory_test import entropy
from verification.zero_autonomous_two_window_records_test import mutual_information


def diagnostics(model,phase,t):
    v=np.einsum('k,k...->...',phase*np.exp(1j*model.energies*t),model.bins)
    joint=np.sum(abs(v)**2,axis=(1,2,3,4))
    m=v.transpose(1,0,2,3,4,5).reshape(model.n,-1)
    rhoG=m@m.conj().T
    b=v.reshape(-1,2);rhoB=b.T@b.conj()
    return {'a':np.trace(rhoG@model.m.scale).real,'mi':mutual_information(joint),
            'joint':joint,'SG':entropy(rhoG),'SB':entropy(rhoB),'v':v}


class PlenitudeSignPairingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m=BalancedRecollapse(24,.02,'center')
        cls.alt=np.where(cls.m.ticks%3==0,-1.,1.)

    def test_actual_rest_eigenmode_encoding_is_isometric(self):
        m=self.m
        self.assertGreater(m.weights.min(),0)
        modes=m.bins.reshape(len(m.ticks),-1)/np.sqrt(m.weights[:,None])
        np.testing.assert_allclose(modes.conj()@modes.T,np.eye(len(m.ticks)),atol=4e-13)
        for i in range(len(m.ticks)):
            mode=m.bins[i]/math.sqrt(m.weights[i])
            self.assertLess(np.linalg.norm(m.quantized_apply(mode)-m.energies[i]*mode),1e-10)

    def test_encoded_swap_is_a_true_sign_reversing_involution(self):
        m=self.m;d=len(m.ticks)
        diff=m.energies[:,None]-m.energies[None,:]
        rng=np.random.default_rng(204)
        M=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        # An encoded ket's coefficients are M_ij. Swapping C and the
        # matching-energy rest code transposes M, with no complex conjugation.
        swap=lambda X:X.T
        np.testing.assert_array_equal(swap(swap(M)),M)
        self.assertAlmostEqual(np.linalg.norm(swap(M)),np.linalg.norm(M),places=10)
        self.assertLess(np.linalg.norm(diff*swap(M)+swap(diff*M)),1e-10)
        # Individual sector energy terms are interchanged with their negatives.
        np.testing.assert_allclose(np.broadcast_to(m.energies[:,None],(d,d)).T,
                                   np.broadcast_to(m.energies[None,:],(d,d)))

    def test_every_joint_energy_outcome_cancels_per_component(self):
        m=self.m
        for sign in (np.ones(len(m.ticks)),self.alt):
            A=np.diag(np.sqrt(m.weights)*sign)
            self.assertLess(np.linalg.norm(A-A.T),1e-15)
            diff=m.energies[:,None]-m.energies[None,:]
            self.assertLess(np.linalg.norm(diff*A),1e-15)
            # Both local energy readouts have the same E_k, and the rest
            # contribution to H_total is -E_k. There is no actual-outcome claim.
            plus=float(np.sum(m.weights*m.energies));minus=-plus
            self.assertAlmostEqual(plus,4.661137499938421,places=10)
            self.assertAlmostEqual(plus+minus,0,places=14)
            self.assertAlmostEqual(np.sum(abs(A)**2),1,places=11)

    def test_swap_even_does_not_imply_exact_zero_eigenstate(self):
        # E=(0,1), symmetric off-diagonal Bell-like state has mean zero
        # but nonzero energy variance; no measurement interpretation assumed.
        H=np.diag([0.,-1.,1.,0.])
        state=np.array([0.,1.,1.,0.])/math.sqrt(2)
        self.assertAlmostEqual(np.vdot(state,H@state),0)
        self.assertAlmostEqual(np.linalg.norm(H@state),1)
        self.assertLess(np.linalg.norm(state.reshape(2,2)-state.reshape(2,2).T),1e-14)

    def test_symmetric_full_support_states_same_marginals_different_history(self):
        m=self.m; w=m.weights
        a=np.diag(np.sqrt(w));b=np.diag(np.sqrt(w)*self.alt)
        # Same physical swap, exact zero support, same clock and rest density
        # matrices in this fixed encoded basis; all weights strictly positive.
        for v in (a,b):
            self.assertLess(np.linalg.norm(v-v.T),1e-14)
            np.testing.assert_allclose(v@v.conj().T,np.diag(w),atol=1e-14)
            np.testing.assert_allclose(v.T@v.conj(),np.diag(w),atol=1e-14)
        for t in (-2.,-1.,0.,1.,2.):
            x=diagnostics(m,np.ones(len(w)),t);y=diagnostics(m,self.alt,t)
            if t==0.:
                self.assertAlmostEqual(x['a'],1.8523770314,places=8)
                self.assertAlmostEqual(y['a'],1.0997783301,places=8)
                self.assertAlmostEqual(x['mi'],1,places=10)
                self.assertAlmostEqual(y['mi'],.3004793525,places=8)
            # The new preparation remains reflection-symmetric in t on this
            # fixed POVM; it is not simply an oriented clock swap.
            z=diagnostics(m,self.alt,-t)
            for key in ('a','mi','SB','SG'):
                self.assertAlmostEqual(y[key],z[key],places=10)
        # Relative phases on three consecutive populated ticks cannot equal
        # a global phase times exp(i*k*δ*t0), i.e. just a clock-origin shift.
        ix=[int(np.where(m.ticks==k)[0][0]) for k in (213,214,215)]
        self.assertTrue(all(w[i]>1e-10 for i in ix))
        np.testing.assert_array_equal(self.alt[ix],[-1,1,1])
        self.assertNotEqual(self.alt[ix[1]]/self.alt[ix[0]],self.alt[ix[2]]/self.alt[ix[1]])

    def test_canonical_equal_mode_pair_and_remaining_phase_choice(self):
        m=self.m;d=len(m.ticks)
        # This chooses the maximally entangled identity vector using the
        # isometry defined by the old boundary state's spectral projections.
        canonical=np.ones(d)/math.sqrt(d)
        alternative=canonical*self.alt
        a=np.diag(canonical);b=np.diag(alternative)
        I=np.eye(d)/d
        for z in (a,b):
            np.testing.assert_allclose(z@z.conj().T,I,atol=1e-15)
            np.testing.assert_allclose(z.T@z.conj(),I,atol=1e-15)
            self.assertLess(np.linalg.norm(z-z.T),1e-15)
            self.assertLess(np.linalg.norm((m.energies[:,None]-m.energies[None,:])*z),1e-15)
        # Convert coefficients in normalized modes to coefficients in bins.
        fac=1/np.sqrt(d*m.weights)
        x=diagnostics(m,fac,0);y=diagnostics(m,fac*self.alt,0)
        self.assertAlmostEqual(x['a'],2.6622652378,places=8)
        self.assertAlmostEqual(y['a'],1.4884110570,places=8)
        self.assertAlmostEqual(diagnostics(m,fac,1)['a'],2.0188902941,places=8)
        self.assertAlmostEqual(float(np.mean(m.energies)),13.314368421,places=8)
        # Explicit finite cutoff dependence; no continuum convergence claim.
        small=BalancedRecollapse(16,.02,'center')
        smallfac=1/np.sqrt(len(small.ticks)*small.weights)
        self.assertGreater(abs(diagnostics(small,smallfac,0)['a']-x['a']),.1)

    def test_full_unitary_invariance_requires_more_than_energy_symmetry(self):
        # U⊗conj(U) acts on coefficient matrices as A -> U A U†.
        # All U leave I fixed; if A=diag(1,-1), a Hadamard does not.
        U=np.array([[1.,1.],[1.,-1.]])/math.sqrt(2)
        identity=np.eye(2)/math.sqrt(2);different=np.diag([1.,-1.])/math.sqrt(2)
        np.testing.assert_allclose(U@identity@U.conj().T,identity,atol=1e-15)
        self.assertGreater(np.linalg.norm(U@different@U.conj().T-different),1)
        H=np.diag([0.,1.])
        self.assertGreater(np.linalg.norm(U@H-H@U),.9)
        # But unitaries commuting with the fixed nondegenerate energy are
        # diagonal phases: U A U†=A for every diagonal A, not just identity.
        D=np.diag([np.exp(.3j),np.exp(-.9j)])
        np.testing.assert_allclose(D@different@D.conj().T,different,atol=1e-15)
        np.testing.assert_allclose(D@H@D.conj().T,H,atol=1e-15)

    def test_pairing_need_not_make_all_energy_weights_equal(self):
        m=self.m
        self.assertGreater(m.weights.max(),1000*m.weights.min())
        # Incidence weights of +E_k and -E_k can match for each k while
        # different k carry different weights; no equal-prior assumption.
        mu=np.stack([m.weights,m.weights],axis=1)
        value=np.stack([m.energies,-m.energies],axis=1)
        self.assertLess(abs(np.sum(mu*value)),1e-13)
        self.assertLess(np.max(abs(mu[:,0]-mu[:,1])),1e-15)

    def test_paired_qualities_cannot_choose_sign_by_balance_alone(self):
        # Formal rival rules on the same h=1, r=+1 event. They obey the
        # same partner-swap oddness and zero sum, but differ locally.
        for r in (-1,1):
            first=np.array([r,-r]);second=-first
            for candidate in (first,second):
                np.testing.assert_array_equal(candidate[::-1],-candidate)
                self.assertEqual(candidate.sum(),0)
            self.assertFalse(np.array_equal(first,second))
        x=diagnostics(self.m,np.ones(len(self.m.ticks)),1)
        # B=1 certifies h=1 in this prepared model; r is balanced in each h.
        self.assertLess(x['joint'][0,1],1e-20)
        self.assertAlmostEqual(x['joint'][1,1]/2,.235380474,places=7)

if __name__=='__main__':unittest.main()
