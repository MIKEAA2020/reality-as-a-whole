"""Ciupa observer claim tested in the actual all-sector paired construction.

A global charge-neutral rank-two probe distinguishes a pure, flag-entangled
state from an explicitly dephased flag state. It is not a subject model.
"""
import math
import unittest
import numpy as np
from verification.zero_three_balance_encoded_sphere_record_test import (
    CODE, PCODE, I256, SINGLET, local_charges
)
from verification.zero_encoded_sphere_clock_work_bridge_test import HA, HB
from verification.zero_all_sector_sphere_clock_work_test import complement_state
from verification.zero_energy_sphere_work_incidence_test import (
    full_state, relative_read, i_r_m_table, h_memory_table
)

P_CODE=1/128
P_OTHER=127/128
PHI0=(I256-PCODE)/math.sqrt(254) # A,B matrix for complement branch
PHI1=CODE@SINGLET@CODE.T         # A,B matrix for encoded branch
A=np.array([math.sqrt(P_OTHER),math.sqrt(P_CODE)],complex)
RHO=np.outer(A,A.conj())
DEPHASED=np.diag(np.diag(RHO))
W=np.array([[0.,1.],[1.,0.]],complex)


class CiupaZeroObserverPairedCoherenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.g=local_charges()
        cls.v0=complement_state(4)
        cls.v1=full_state(4)
        # Keep every relative-clock label: this is not the earlier three-label
        # postselection. Relative POVM roots form a complete isometry.
        cls.cl0=relative_read(cls.v0,4,labels=tuple(range(16)))
        cls.cl1=relative_read(cls.v1,4,labels=tuple(range(16)))

    def test_both_distinct_physical_branches_obey_global_charges(self):
        self.assertAlmostEqual(np.linalg.norm(PHI0),1,places=12)
        self.assertAlmostEqual(np.linalg.norm(PHI1),1,places=12)
        self.assertAlmostEqual(abs(np.vdot(PHI0,PHI1)),0,places=12)
        for phi in (PHI0,PHI1):
            np.testing.assert_allclose(HA@phi+phi@HB.T,0,atol=1e-13)
            for g in self.g:
                np.testing.assert_allclose(g@phi-phi@g.T,0,atol=1e-13)
        # Rank-two W=|branch0,00><branch1,11|+h.c. is supported entirely
        # in the simultaneous kernels of the paired directional and energy
        # operators. Their self-adjointness then gives [Q,W]=[D_i,W]=0.

    def test_global_interference_distinguishes_flag_dephasing(self):
        self.assertAlmostEqual(np.trace(RHO@W).real,math.sqrt(127)/64,places=14)
        self.assertAlmostEqual(np.trace(DEPHASED@W).real,0,places=14)
        self.assertAlmostEqual(np.sum(abs(np.linalg.eigvalsh(RHO-DEPHASED)))/2,
                               math.sqrt(127)/128,places=14)
        self.assertAlmostEqual(np.trace(RHO).real,1,places=14)
        # W commutes with the *global* constraints, but in general not with
        # the individual lab generators; measuring it is a joint operation.

    def test_the_global_probe_is_not_a_strictly_local_conserving_report(self):
        self.assertAlmostEqual(np.linalg.norm(self.g[0]@PHI1),0,places=12)
        self.assertAlmostEqual(np.linalg.norm(self.g[0]@PHI0)**2,256/127,places=12)
        # Thus the rank-two global W mixes local-charge sectors and cannot
        # commute with G_A; access to W must not be attributed to either lab.

    def test_actual_all_label_clock_record_probabilities_survive_dephasing(self):
        for arr in (self.cl0,self.cl1):
            self.assertAlmostEqual(sum(np.vdot(v,v).real for v in arr),1,places=12)
            np.testing.assert_allclose(h_memory_table(arr),[[.5,0],[0,.5]],atol=1e-12)
            table=i_r_m_table(arr)
            self.assertAlmostEqual(table.sum(),1,places=12)
            np.testing.assert_allclose(table.sum(axis=(0,2)),[.5,.5],atol=1e-12)
        t0=i_r_m_table(self.cl0); t1=i_r_m_table(self.cl1)
        for i in range(3):
            for r in range(2):
                for m in range(2):
                    # A record probability is represented in the orthogonal
                    # flag-sector span by a diagonal effect. The off-diagonal
                    # flag coherence therefore cannot change its value.
                    effect=np.diag([t0[i,r,m],t1[i,r,m]])
                    self.assertAlmostEqual(np.trace(RHO@effect).real,
                                           np.trace(DEPHASED@effect).real,places=14)
        self.assertAlmostEqual(np.sum(P_OTHER*t0+P_CODE*t1),1,places=12)

    def test_window_and_target_event_same_but_global_coherence_differs(self):
        c0=relative_read(self.v0,4);c1=relative_read(self.v1,4)
        for x in (c0,c1):
            self.assertAlmostEqual(sum(np.vdot(v,v).real for v in x),3/16,places=12)
            self.assertAlmostEqual(i_r_m_table(x)[:,0,1].sum(),3/64,places=12)
        event=np.diag([3/64,3/64])
        self.assertAlmostEqual(np.trace(RHO@event).real,3/64,places=14)
        self.assertAlmostEqual(np.trace(DEPHASED@event).real,3/64,places=14)
        self.assertGreater(np.trace(RHO@W).real,.17)
        # No single record statistic here establishes global collapse or
        # consciousness; both descriptions have the same event weights.

    def test_local_flag_access_cannot_reveal_cross_branch_phase(self):
        # Both flag copies are |00> or |11>; tracing either flag removes the
        # off-diagonal term. Any experiment confined to the other copy and its
        # local lab is insensitive to the global relative phase.
        rho_a0=PHI0@PHI0.conj().T
        rho_a1=PHI1@PHI1.conj().T
        rho_b0=PHI0.T@PHI0.conj()
        rho_b1=PHI1.T@PHI1.conj()
        for rho in (rho_a0,rho_a1,rho_b0,rho_b1):
            self.assertAlmostEqual(np.trace(rho).real,1,places=12)
        # Trace the inaccessible other flag: <0|1>=0 removes the cross
        # branch terms even when its lab is retained in the whole state.
        alice=np.zeros((512,512),complex)
        alice[:256,:256]=P_OTHER*rho_a0
        alice[256:,256:]=P_CODE*rho_a1
        self.assertAlmostEqual(np.trace(alice).real,1,places=12)
        np.testing.assert_array_equal(alice[:256,256:],0)
        # The same block-diagonal local density arises for a dephased flag.

if __name__=='__main__':
    unittest.main()
