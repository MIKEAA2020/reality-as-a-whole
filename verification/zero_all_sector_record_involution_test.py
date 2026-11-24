"""Exact record/work/target involution in the specified all-sector circuit.

The two global sectors are related to the physical labs by the isometries in
zero_all_sector_sphere_clock_work_test; no sector is postselected. This is a
finite circuit identity, not an objective cosmic-energy or subjecthood result.
"""
import math
import unittest
import numpy as np

from verification.zero_all_sector_sphere_clock_work_test import (
    complement_state, weighted_table, PLUS, MINUS, PCODE, I256
)
from verification.zero_energy_sphere_work_incidence_test import (
    X, Z, Jactive, full_state, relative_read, project_h, h_memory_table,
    i_r_m_table, reduced_record, reduced_work, record_work,
    embed_records_and_work, target_memory
)
from verification.zero_dual_pair_sphere_energy_instrument_test import dual_output
from verification.zero_reciprocal_subject_exchange_test import n, proj

I2 = np.eye(2, dtype=complex)


def transform(v):
    """-Z_R ⊗ X_work ⊗ X_target on last three active-code axes."""
    return -np.einsum('rs,wu,mt,...sut->...rwm', Z, X, X, v, optimize=True)


def event_probs(v):
    """Retain i,j,r; sum all lab/clock axes, work and target."""
    return np.sum(abs(v)**2, axis=(0, 1, 2, 3, 4, 5, 9, 10))


def target_density(vs):
    rho = np.zeros((2, 2), complex)
    for v in vs:
        a = np.moveaxis(v, -1, 0).reshape(2, -1)
        rho += a @ a.conj().T
    return rho


class AllSectorRecordInvolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.code = full_state(4)
        cls.complement = complement_state(4)
        cls.labels = tuple(range(16))
        cls.clocks = [relative_read(v, 4, labels=cls.labels)
                      for v in (cls.code, cls.complement)]

    def test_work_exchange_is_an_actual_full_operator_conserving_work_energy(self):
        # The active X is the a<->b exchange, extended by identity on the
        # other 14 four-bit states. Unlike X⊗4 it commutes with total energy
        # on the ENTIRE physical work space, not just the active subspace.
        P = np.asarray(proj, complex)
        a, b = 6, 9  # |0110>, |1001>
        V = np.eye(16, dtype=complex)-P
        V[a, b] = V[b, a] = 1
        np.testing.assert_allclose(V.conj().T, V, atol=1e-14)
        np.testing.assert_allclose(V@V, np.eye(16), atol=1e-14)
        np.testing.assert_allclose(V[np.ix_([a,b], [a,b])], X, atol=1e-14)
        numbers = np.asarray(n, complex)
        for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
            H = sum(numbers[k] for k in inds)
            np.testing.assert_allclose(V@H-H@V, 0, atol=1e-14)
        # Local occupations are not separately preserved: no claim of
        # cost-free strictly local implementation is made.
        self.assertGreater(np.linalg.norm(V@numbers[0]-numbers[0]@V), 1)

    def test_involution_reverses_relation_and_target_but_not_record(self):
        K = np.kron(Z, Jactive)
        h = (np.eye(4)-K)/2
        U = -np.kron(np.kron(Z, X), X)
        ident = np.eye(8)
        np.testing.assert_allclose(U.conj().T, U, atol=1e-14)
        np.testing.assert_allclose(U@U, ident, atol=1e-14)
        np.testing.assert_allclose(U@np.kron(K,I2)@U, -np.kron(K,I2), atol=1e-14)
        np.testing.assert_allclose(U@np.kron(h,I2)@U, np.kron(np.eye(4)-h,I2), atol=1e-14)
        np.testing.assert_allclose(U@np.kron(np.kron(Z,I2),I2)@U,
                                   np.kron(np.kron(Z,I2),I2), atol=1e-14)
        np.testing.assert_allclose(U@np.kron(np.eye(4),Z)@U,
                                   -np.kron(np.eye(4),Z), atol=1e-14)
        np.testing.assert_allclose(U@np.kron(np.kron(I2,Jactive),I2)@U,
                                   -np.kron(np.kron(I2,Jactive),I2), atol=1e-14)

    def test_each_sector_and_each_clock_label_is_invariant_as_a_vector(self):
        for v, vs in zip((self.code, self.complement), self.clocks):
            np.testing.assert_allclose(transform(v), v, atol=2e-14)
            np.testing.assert_allclose(transform(transform(v)), v, atol=2e-14)
            self.assertAlmostEqual(sum(np.vdot(x,x).real for x in vs), 1, places=12)
            for x in vs:
                np.testing.assert_allclose(transform(x), x, atol=2e-14)
                np.testing.assert_allclose(transform(project_h(x,0)), project_h(x,1), atol=2e-14)
                np.testing.assert_allclose(transform(project_h(x,1)), project_h(x,0), atol=2e-14)
        # The physical code and complement embeddings are orthogonal, and U
        # acts identically only on R,W,T. Thus any coherent superposition of
        # these physical branches, including the actual 1:127 weighted whole,
        # is invariant. This is stronger than a dephased-sector calculation.

    def test_equal_weights_for_each_clock_i_j_and_record_not_only_the_mean(self):
        for vs in self.clocks:
            for v in vs:
                p0 = event_probs(project_h(v,0))
                p1 = event_probs(project_h(v,1))
                np.testing.assert_allclose(p0,p1,atol=2e-15)
                self.assertAlmostEqual(p0.sum(), 1/32, places=13)
        # Conditioning on the common three-label clock window gives 3/32
        # per h. No selected sector, clock label, i, j or r is discarded.
        for vs in self.clocks:
            np.testing.assert_allclose(h_memory_table([vs[i] for i in (15,0,1)]),
                                       [[3/32,0],[0,3/32]],atol=1e-14)

    def test_full_state_weighted_statistics_and_r_asymmetry(self):
        cc=[self.clocks[0][i] for i in (15,0,1)]
        cd=[self.clocks[1][i] for i in (15,0,1)]
        table=weighted_table(cc,cd)/(3/16)
        np.testing.assert_allclose(table[:,:,0],table[:,:,1],atol=1e-14)
        rows=table.sum(axis=2)
        expected=np.array([[0.06546799,0.05953201],
                           [0.17625608,0.22374392],
                           [0.25827593,0.21672407]])
        np.testing.assert_allclose(rows,expected,atol=6e-9)
        bias=(rows[:,0]-rows[:,1])/rows.sum(axis=1)
        self.assertGreater(np.max(abs(bias)),.1)
        # The involution does not reverse R, so its sign need not be paired
        # at fixed Alice record i even though h and target signs are.

    def test_target_has_h_report_but_confined_r_does_not(self):
        for vs in self.clocks:
            for h in (0,1):
                branch=[project_h(v,h) for v in vs]
                p=sum(np.vdot(v,v).real for v in branch)
                self.assertAlmostEqual(p,.5,places=12)
                expected=np.diag([1.,0.]) if h==0 else np.diag([0.,1.])
                np.testing.assert_allclose(target_density(branch)/p,expected,atol=1e-13)
                np.testing.assert_allclose(reduced_record(branch)/p,I2/2,atol=1e-13)
                np.testing.assert_allclose(reduced_work(branch)/p,I2/2,atol=1e-13)
        # Target was explicitly coupled to h. This does not give R access to
        # target or make target a subject or the target operation spacetime local.

    def test_pairing_depends_on_preparation_and_gate(self):
        for angle in (0,math.pi/8,math.pi/4):
            v=target_memory(embed_records_and_work(dual_output(4,4),angle), math.pi/2)
            p0=np.linalg.norm(project_h(v,0))**2
            p1=np.linalg.norm(project_h(v,1))**2
            self.assertAlmostEqual(p0,math.cos(angle)**2,places=12)
            self.assertAlmostEqual(p1,math.sin(angle)**2,places=12)
            self.assertAlmostEqual(np.linalg.norm(transform(v)-v)**2,
                                   2-2*math.sin(2*angle),places=12)
        partial=full_state(4,tau=math.pi/4)
        self.assertGreater(np.linalg.norm(transform(partial)-partial),.1)
        # U is a symmetry of the specified final state, not generally of
        # the preparation or interaction Hamiltonian. U h U = I-h.

    def test_rank_mismatch_does_not_block_finer_record_pairing(self):
        self.assertAlmostEqual(np.trace(PLUS).real,158,places=12)
        self.assertAlmostEqual(np.trace(MINUS).real,96,places=12)
        self.assertAlmostEqual(np.trace(PCODE).real,2,places=12)
        np.testing.assert_allclose(PLUS+MINUS+PCODE,I256,atol=1e-13)
        # A unitary cannot conjugate projectors of unequal rank. Our U acts
        # on the record/work/target factors, leaving these projectors fixed.
        # Rank does not rule out pairings with other enlarged resources.

if __name__ == '__main__':
    unittest.main()
