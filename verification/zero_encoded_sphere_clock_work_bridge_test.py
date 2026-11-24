"""Isometric integration of directional zero codes and the clock/work circuit.

The physical code factors are represented explicitly; the large environment is
kept compressed using an exact local isometry. Energy and charges are declared
finite-model operators, not a proof of cosmological energy or experience.
"""
import math
import unittest
import numpy as np
from verification.zero_three_balance_encoded_sphere_record_test import (
    CODE, PCODE, I4, I256, X, kron_all, local_charges, SINGLET
)
from verification.zero_dual_pair_sphere_energy_instrument_test import (
    sector_unitaries, roots, bob_effects
)
from verification.zero_energy_sphere_work_incidence_test import (
    full_state, relative_read, project_h, h_memory_table, i_r_m_table,
    reduced_record, reduced_work, record_work, Jactive, Z, lab_vector,
    density_frobenius_sq
)
from verification.zero_autonomous_two_window_records_test import mutual_information

P = np.diag([0., 1.]).astype(complex)
HA = CODE @ P @ CODE.conj().T
HB = CODE @ (P-np.eye(2)) @ CODE.conj().T


def logical_sphere_unitary(L, F=None):
    nout = 3 if F is None else len(F)
    out = np.zeros((2*L*nout, 2*L*nout), complex)
    for inds, block in sector_unitaries(L, F):
        ix = np.array([a*nout+p for a in inds for p in range(nout)])
        out[np.ix_(ix, ix)] = block
    return out


def lift_apply(v, U):
    """Apply (I-Pcode)⊗I+(E⊗I)U(E†⊗I) to (lab,ref,pointer)."""
    L, nout = v.shape[1:]
    z = np.einsum('xa,xrp->arp', CODE.conj(), v)
    u = (U @ z.reshape(-1)).reshape(2, L, nout)
    return v + np.einsum('xa,arp->xrp', CODE, u-z)


def lab_apply(op, v):
    return np.einsum('xy,yrp->xrp', op, v, optimize=True)


def local_energy_apply(H, v):
    return lab_apply(H, v) + v*np.arange(v.shape[1])[None, :, None]


def pair_charges():
    a = [kron_all([x, I4, I4, I4]) + kron_all([I4, x, I4, I4]) for x in X]
    b = [kron_all([I4, I4, x, I4]) + kron_all([I4, I4, I4, x]) for x in X]
    return a, b


def normalized_event_lab_a(vs, r=0, target=1, i=None):
    rho = np.zeros((2, 2), complex)
    for v in vs:
        if i is None:
            z = v[:, :, :, :, :, :, :, :, r, :, target].reshape(2, -1)
        else:
            z = v[:, :, :, :, :, :, i, :, r, :, target].reshape(2, -1)
        rho += z @ z.conj().T
    prob = np.trace(rho).real
    return rho/prob, prob


def one_body_projection(H):
    """Hilbert-Schmidt projection onto constants and all one-site terms."""
    c = np.trace(H).real/256
    ans = c*I256
    for a in range(4):
        axes = [a]+[j for j in range(4) if j != a]
        axes += [a+4]+[j+4 for j in range(4) if j != a]
        tensor = H.reshape((4,)*8).transpose(axes).reshape(4, 64, 4, 64)
        single = np.einsum('aibi->ab', tensor)/64 - c*I4
        ans += kron_all([single if j == a else I4 for j in range(4)])
    return ans


class EncodedSphereClockWorkBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.G = local_charges()
        cls.v = full_state(4)
        cls.clock = relative_read(cls.v, 4)

    def test_logical_sphere_unitaries_and_energy_conserving_dilation(self):
        rng = np.random.default_rng(207)
        for effects, Hlogical, Hphysical in ((None, P, HA),
                                            (bob_effects(), P-np.eye(2), HB)):
            L = 4
            U = logical_sphere_unitary(L, effects)
            nout = 3 if effects is None else len(effects)
            np.testing.assert_allclose(U.conj().T @ U, np.eye(2*L*nout), atol=1e-12)
            q = np.kron(np.kron(Hlogical, np.eye(L)), np.eye(nout))
            q += np.kron(np.kron(np.eye(2), np.diag(np.arange(L))), np.eye(nout))
            np.testing.assert_allclose(q@U, U@q, atol=1e-12)
            K = roots(L, effects)
            for i in range(nout):
                np.testing.assert_allclose(U.reshape(2*L,nout,2*L,nout)[:,i,:,0],
                                           K[i], atol=1e-12)
            v = rng.normal(size=(256,L,nout))+1j*rng.normal(size=(256,L,nout))
            v /= np.linalg.norm(v)
            out = lift_apply(v,U)
            self.assertAlmostEqual(np.linalg.norm(out), 1, places=12)
            np.testing.assert_allclose(local_energy_apply(Hphysical,out),
                lift_apply(local_energy_apply(Hphysical,v),U), atol=1e-13)
            for g in self.G:
                np.testing.assert_allclose(lab_apply(g,out), lift_apply(lab_apply(g,v),U),
                                           atol=1e-13)
        # The general operator identity follows because G E=0 and the
        # complement is untouched; energy is block diagonal in the code.

    def test_directional_and_logical_energy_operators_commute_exactly(self):
        np.testing.assert_allclose(CODE.conj().T@HA@CODE, P, atol=1e-14)
        np.testing.assert_allclose(CODE.conj().T@HB@CODE, P-np.eye(2), atol=1e-14)
        for g in self.G:
            for h in (HA, HB):
                np.testing.assert_allclose(g@h-h@g, 0, atol=1e-14)
        self.assertGreater(np.linalg.norm(HA), .99)

    def test_actual_clock_work_state_remains_zero_for_all_four_charges(self):
        # Isometric transport leaves every old compressed amplitude unchanged.
        # The full physical state is (E_A⊗E_B⊗I_env)|v>; no 4^8×env
        # tensor need be allocated. Test a nonzero h=1, r=0, T=1 physical slice.
        v = project_h(self.clock[0], 1)
        masked = np.zeros_like(v)
        masked[:,:,:,:,:,:,:,:,0,:,1] = v[:,:,:,:,:,:,:,:,0,:,1]
        ix = np.unravel_index(np.argmax(abs(masked)), masked.shape)
        self.assertGreater(abs(masked[ix]), 1e-6)
        _,_,ra,ca,rb,cb,i,j,r,w,m = ix
        piece = masked[:,:,ra,ca,rb,cb,i,j,r,w,m]
        physical = CODE @ piece @ CODE.T
        self.assertAlmostEqual(np.linalg.norm(physical), np.linalg.norm(piece), places=14)
        for g in self.G:
            np.testing.assert_allclose(g@physical, 0, atol=1e-14)
            np.testing.assert_allclose(physical@g.T, 0, atol=1e-14)
        # Work energy 2 cancels the stipulated +2 clock offset; all
        # other retained energy labels here are explicit, not averaged.
        qenv = ra-ca+rb-cb
        np.testing.assert_allclose(HA@physical + physical@HB.T + qenv*physical,
                                   0, atol=1e-14)
        eA = np.array([0.,1.]); eB = np.array([-1.,0.]); L=4
        e = (eA[:,None,None,None,None,None]+eB[None,:,None,None,None,None]
             +np.arange(L)[None,None,:,None,None,None]-np.arange(L)[None,None,None,:,None,None]
             +np.arange(L)[None,None,None,None,:,None]-np.arange(L)[None,None,None,None,None,:])
        for state in [self.v]+self.clock:
            self.assertLess(np.linalg.norm(state*e[:,:,:,:,:,:,None,None,None,None,None]),1e-12)
        # Since (E†E)=I and HA E=E P, HB E=E(P-I), the full tensor
        # satisfies all seven lab-directional and energy constraints, not
        # just the selected explicitly expanded physical slice.

    def test_record_and_clock_work_observables_survive_isometry(self):
        norm = sum(np.vdot(v,v).real for v in self.clock)
        self.assertAlmostEqual(norm, 3/16, places=12)
        table = i_r_m_table(self.clock)/norm
        expected = np.array([[.06917444,.05582556],[.14660452,.25339548],
                             [.28422105,.19077895]])
        np.testing.assert_allclose(table.sum(axis=2), expected, atol=6e-9)
        np.testing.assert_allclose(table[:,:,0],table[:,:,1],atol=1e-12)
        hm = h_memory_table(self.clock)/norm
        np.testing.assert_allclose(hm, [[.5,0],[0,.5]], atol=1e-12)
        self.assertAlmostEqual(mutual_information(hm),1,places=12)
        K = np.kron(Z,Jactive)
        for h in (0,1):
            b = [project_h(v,h) for v in self.clock]
            p = sum(np.vdot(x,x).real for x in b)
            np.testing.assert_allclose(reduced_record(b)/p, np.eye(2)/2, atol=1e-12)
            np.testing.assert_allclose(reduced_work(b)/p, np.eye(2)/2, atol=1e-12)
            np.testing.assert_allclose(record_work(b)/p,
                                       (np.eye(4)+(1-2*h)*K)/4, atol=1e-12)
        # These operators act on retained R,W,T and clock registers and hence
        # commute with the isometries E_A,E_B, preserving all correlations.

    def test_same_actual_branch_has_nonzero_compensated_pair_imbalance(self):
        rho, probability = normalized_event_lab_a(self.clock, 0, 1)
        self.assertAlmostEqual(probability, 3/64, places=12)
        A, B = pair_charges()
        C12 = sum(x@x for x in A)
        logical = CODE.conj().T@C12@CODE
        np.testing.assert_allclose(logical,np.diag([0.,16/5]),atol=1e-13)
        self.assertAlmostEqual(np.trace(rho@logical).real, 1.8771281292110196, places=12)
        for a,b in zip(A,B):
            np.testing.assert_allclose((a+b)@CODE, 0, atol=1e-14)
        # This is the same r=+,T=1,h=1 conditional circuit event, not an
        # inference about actual experiential incidence or selected outcomes.

    def test_no_signalling_transports_through_local_isometry(self):
        from verification.zero_dual_pair_sphere_energy_instrument_test import axis, SIGMA, I
        op = sum(x*s for x,s in zip(axis,SIGMA))
        pair = np.array([(I+op)/2, (I-op)/2])
        other = full_state(4,FA=pair)
        a = lab_vector(self.v)
        b = lab_vector(other)
        self.assertLess(density_frobenius_sq(a,b),1e-12)
        ac = np.concatenate([lab_vector(v) for v in self.clock], axis=1)
        bc = np.concatenate([lab_vector(v) for v in relative_read(other,4)], axis=1)
        self.assertAlmostEqual(np.linalg.norm(ac)**2, 3/16, places=12)
        self.assertAlmostEqual(np.linalg.norm(bc)**2, 3/16, places=12)
        self.assertLess(density_frobenius_sq(ac,bc),1e-12)
        for g in self.G: np.testing.assert_allclose(g@CODE,0,atol=1e-14)
        # The same Bob-local isometry sends equal retained density operators
        # to equal operators; an isometry of traced Alice has no effect.
        np.testing.assert_allclose(CODE.conj().T@CODE,np.eye(2),atol=1e-14)

    def test_symmetric_logical_energy_needs_multisite_interaction(self):
        np.testing.assert_allclose(one_body_projection(HA), I256/256, atol=1e-14)
        self.assertAlmostEqual(np.linalg.norm(HA-one_body_projection(HA)),
                               math.sqrt(255/256), places=12)
        # More generally, if H=sum_j h_j and [H,G_i]=0, partial-tracing all
        # but site j gives [h_j,X_i]=0. The Xi generate all M4, so h_j is
        # scalar. An invariant energy splitting cannot be only one-body.

    def test_explicit_global_pair_resource_prepares_code_by_local_flags(self):
        # Four cross-lab Phi4 pairs give Phi_256. V is a *specified* local
        # invariant logical rotation on Bob; no claim that it is forced.
        rotation = np.array([[0.,-1.],[1.,0.]])
        V = CODE@rotation@CODE.conj().T + I256-PCODE
        np.testing.assert_allclose(V.conj().T@V, I256, atol=1e-14)
        M = V.T/16  # coefficient matrix for (I⊗V)|Phi_256>
        self.assertAlmostEqual(np.linalg.norm(M),1,places=12)
        np.testing.assert_allclose(HA@M+M@HB.T,0,atol=1e-14)
        for g in self.G:
            np.testing.assert_allclose(g@V-V@g,0,atol=1e-14)
            np.testing.assert_allclose(g@M-M@g.T,0,atol=1e-14)
        projections = [I256-PCODE, PCODE]
        probabilities = np.zeros((2,2))
        branches = {}
        for a in (0,1):
            for b in (0,1):
                branch = projections[a]@M@projections[b].T
                branches[a,b]=branch
                probabilities[a,b] = np.linalg.norm(branch)**2
                np.testing.assert_allclose(HA@branch+branch@HB.T,0,atol=1e-14)
                for g in self.G:
                    np.testing.assert_allclose(g@branch-branch@g.T,0,atol=1e-14)
        np.testing.assert_allclose(probabilities,[[127/128,0],[0,1/128]],atol=1e-14)
        success = branches[1,1]/math.sqrt(1/128)
        np.testing.assert_allclose(success,CODE@SINGLET@CODE.T,atol=1e-14)
        for g in self.G:
            np.testing.assert_allclose(g@success,0,atol=1e-14)
            np.testing.assert_allclose(success@g.T,0,atol=1e-14)
        # The two-outcome measurement is an explicit local unitary with a
        # neutral flag: U=(I-P)⊗I+P⊗X, commuting with G and local energy.
        for g in self.G:
            np.testing.assert_allclose(g@PCODE-PCODE@g,0,atol=1e-14)
        for h in (HA,HB):
            np.testing.assert_allclose(h@PCODE-PCODE@h,0,atol=1e-14)
        # Unread Alice flag leaves Bob's density matrix unchanged.
        rho_b = sum((p@M).T @ (p@M).conj() for p in projections)
        np.testing.assert_allclose(rho_b, M.T@M.conj(), atol=1e-14)
        # The discarded-looking branch is part of the same coherent whole;
        # its local charge variance compensates the successful postselection.
        c = sum(g@g for g in self.G)
        self.assertAlmostEqual(np.trace(c@M@M.conj().T).real,6,places=12)
        failure=branches[0,0]
        self.assertAlmostEqual(np.trace(c@failure@failure.conj().T).real/(127/128),
                               768/127,places=12)
        _, eventprob = normalized_event_lab_a(self.clock,0,1)
        self.assertAlmostEqual(eventprob/128,3/8192,places=14)

    def test_uncorrelated_bare_pair_cannot_be_locally_encoded_for_free(self):
        # A marginal of the earlier bare Phi_4 is I4/4. Append *any*
        # uncorrelated three-site ancilla. Cross terms vanish; the initial
        # G² expectation is 3/2 + <sum_i (G_i^rest)²>.
        rest = [sum(kron_all([x if j == k else I4 for j in range(3)])
                    for k in range(3)) for x in X]
        c_rest = sum(g@g for g in rest)
        eig = np.linalg.eigvalsh(c_rest)
        self.assertAlmostEqual(eig.min(),1,places=12)
        self.assertAlmostEqual(sum(np.trace(x@x).real/4 for x in X),1.5,places=12)
        # Thus >= 5/2 for this four-site representation. Every local
        # unitary preserving each G_i preserves sum G_i², while the desired
        # encoded sector has value 0: no such free local preparation exists.

if __name__ == '__main__':
    unittest.main()
