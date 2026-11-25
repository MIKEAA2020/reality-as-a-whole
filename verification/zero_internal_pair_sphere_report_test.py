"""Source the charged report pair from the original paired lab state.

The chosen factorization and pointer/circuit operations are stipulated.
The reference qubits are distributed across labs; no local interface or
objective cosmic-energy conclusion is assumed.
"""
import math
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    decomposition,local_charges,HA,HB,I256,CODE,PCODE,J,kron,
    original_effects,bob_effects,active_base,output,full_state,
    remainder_base,relative_read,i_r_m_table
)
from verification.zero_energy_sphere_work_incidence_test import I,X,Y,Z
from verification.zero_relational_chirality_report_test import (
    initial,apply64,outcome_tables,C,LL,SING
)
from verification.zero_relative_gauge_invariant_report_test import (
    V,VP,VM,G,SOURCE
)
from verification.zero_five_ray_record_current_unification_test import q


BLOCKS=((0,1),(1,0),(1,1))
SIG=(X,Y,Z)


def sector(paths):
    m=len(paths);d=paths[0].shape[1];k=m//4;t=k*d
    F=np.column_stack(paths[:4*k])
    # Basis order sphere, reference, multiplicity/irrep spectator.
    bob=F.conj()@kron(I,J.T,np.eye(t))
    return m,d,k,t,F,bob


def local_lift(F,t,op):return F@kron(op,np.eye(t))@F.conj().T


def physical_operators(F,bob,t):
    ka=[f/math.sqrt(np.trace(f).real) for f in original_effects()]
    kb=[J.conj().T@f@J for f in bob_effects()]
    alice=[local_lift(F,t,kron(x,I)) for x in ka]
    bobops=[local_lift(bob,t,kron(x,I)) for x in kb]
    d=[local_lift(F,t,kron(I,x)) for x in SIG]
    e=[local_lift(bob,t,kron(I,x)) for x in SIG]
    return ka,kb,alice,bobops,d,e


class InternalPairSphereReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.blocks=decomposition()[3]
        cls.items=[sector(cls.blocks[k]) for k in BLOCKS]
        cls.g=local_charges()

    def test_representation_capacity_and_unchanged_whole_state(self):
        weights={}
        for key,paths in self.blocks.items():
            paths=paths[2:] if key==(0,0) else paths
            m=len(paths);d=paths[0].shape[1]
            weights[key]=4*(m//4)*d
        self.assertEqual(sum(weights.values()),96)
        self.assertEqual({k:v for k,v in weights.items() if v},
                         {(0,1):12,(1,0):12,(1,1):72})
        projectors=[]
        for _,_,_,t,F,bob in self.items:
            p=F@F.conj().T;projectors.append(p)
            np.testing.assert_allclose(F.conj().T@F,np.eye(4*t),atol=1e-12)
            np.testing.assert_allclose(bob@bob.conj().T,p.conj(),atol=1e-12)
            np.testing.assert_allclose(PCODE@p,0,atol=1e-12)
            for g in self.g:np.testing.assert_allclose(g@p-p@g,0,atol=1e-12)
            for h in (HA,HB):np.testing.assert_allclose(h@p-p@h,0,atol=1e-12)
        active=sum(projectors);rest=I256-PCODE-active
        np.testing.assert_allclose(rest@rest,rest,atol=1e-12)
        self.assertAlmostEqual(np.trace(active).real,96,places=10)
        self.assertAlmostEqual(np.trace(rest).real,158,places=10)
        for g in self.g:np.testing.assert_allclose(g@rest-rest@g,0,atol=1e-12)
        for h in (HA,HB):np.testing.assert_allclose(h@rest-rest@h,0,atol=1e-12)
        # Original (not re-prepared) global amplitude from the old report.
        whole=(CODE@J@CODE.T+I256-PCODE).T/16
        code=PCODE@whole
        np.testing.assert_allclose(whole,code+sum(projectors)/16+rest/16,atol=1e-12)
        # The two labs agree on the matching sector without communicating.
        # A local coherent flag controlled by active preserves every sector;
        # its |0> and |1> amplitudes add back to the unchanged input.
        for p in (PCODE,active,rest):
            np.testing.assert_allclose(p@whole,whole@p.conj().T,atol=1e-12)
        flag1=active@whole;flag0=(I256-active)@whole
        np.testing.assert_allclose(flag0+flag1,whole,atol=1e-12)
        self.assertAlmostEqual(np.linalg.norm(flag1)**2,3/8,places=12)
        self.assertAlmostEqual(np.linalg.norm(flag0)**2,5/8,places=12)
        self.assertAlmostEqual(np.vdot(flag0,flag1).real,0,places=12)
        self.assertAlmostEqual(np.linalg.norm(code)**2,2/256,places=12)
        self.assertAlmostEqual(sum(np.linalg.norm(p/16)**2 for p in projectors),96/256,places=12)
        self.assertAlmostEqual(np.linalg.norm(rest/16)**2,158/256,places=12)
        # The 96 upper bound is for an exact 2⊗2 multiplicity factor while
        # leaving the energy-split original code separate, not all POVMs.

    def test_actual_state_contains_sphere_and_singlet_reference_factors(self):
        for _,_,_,t,F,bob in self.items:
            p=F@F.conj().T
            input_matrix=p/16
            coords=F.conj().T@input_matrix@bob.conj()
            expected=kron(I,J.T,np.eye(t))/16
            np.testing.assert_allclose(coords,expected,atol=1e-12)
            # Coordinates equal |Phi_2>_sphere |singlet>_ref |Phi_t>
            # times sqrt(4t/256), up to the displayed basis convention.
            factored=math.sqrt(4*t/256)*kron(I/math.sqrt(2),SING,np.eye(t)/math.sqrt(t))
            np.testing.assert_allclose(coords,factored,atol=1e-12)

    def test_physical_sphere_operations_leave_the_internal_singlet_untouched(self):
        for _,_,_,t,F,bob in self.items:
            ka,kb,alice,bobops,d,e=physical_operators(F,bob,t)
            pa=F@F.conj().T;pb=bob@bob.conj().T
            np.testing.assert_allclose(sum(k.conj().T@k for k in alice),pa,atol=1e-12)
            np.testing.assert_allclose(sum(k.conj().T@k for k in bobops),pb,atol=1e-12)
            e0=alice[0].conj().T@alice[0];e1=alice[1].conj().T@alice[1]
            self.assertGreater(np.linalg.norm(e0@e1-e1@e0),0.01)
            for op in alice+bobops+d+e:
                for g in self.g:np.testing.assert_allclose(g@op-op@g,0,atol=1e-12)
                for h in (HA,HB):np.testing.assert_allclose(h@op-op@h,0,atol=1e-12)
            for op in alice:
                for x in d:np.testing.assert_allclose(op@x-x@op,0,atol=1e-12)
            for op in bobops:
                for x in e:np.testing.assert_allclose(op@x-x@op,0,atol=1e-12)
            for ops,p in ((d,pa),(e,pb)):
                for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
                    np.testing.assert_allclose(ops[i]@ops[j]-ops[j]@ops[i],2j*ops[k],atol=1e-12)
                    np.testing.assert_allclose(ops[i]@ops[i],p,atol=1e-12)
            src=pa/16
            for i,a in enumerate(alice):
                for j,b in enumerate(bobops):
                    branch=a@src@b.T
                    # It is the *same* post-instrument quantum amplitude,
                    # not just the same 3x2 outcome probability.
                    coord=F.conj().T@branch@bob.conj()
                    expected=kron(ka[i],I,np.eye(t))@kron(I,J.T,np.eye(t))@kron(kb[j].T,I,np.eye(t))/16
                    np.testing.assert_allclose(coord,expected,atol=1e-12)
                    np.testing.assert_allclose(F@coord@bob.T,branch,atol=1e-12)
                    for x,y in zip(d,e):
                        np.testing.assert_allclose(x@branch+branch@y.T,0,atol=1e-12)
            # Every Alice/Bob pointer branch retains the pairwise zero of
            # the internally encoded spin reference, with no conditional
            # reference preparation or replacement.

    def test_measuring_the_reference_qubit_itself_destroys_the_exact_singlet(self):
        # The Alice rank-one sphere Kraus operators do not preserve a
        # shared reference singlet when applied to the same logical qubit.
        for f,qi in zip(original_effects(),q):
            k=f/math.sqrt(np.trace(f).real)
            branch=k@SING
            p=np.vdot(branch,branch).real
            self.assertAlmostEqual(p,qi,places=13)
            self.assertAlmostEqual(abs(np.vdot(SING,branch))**2/p,.5,places=12)
            self.assertEqual(np.linalg.matrix_rank(branch,tol=1e-12),1)
        # More generally if a local isometry outputs the same pure singlet
        # and a pointer for this full-Schmidt-rank input, the pointer state is
        # independent of the input qubit. Hence its POVM effects are scalar.
        # Feedback, nonlocal operations or a disturbed reference are different
        # resources and are not excluded by this statement.

    def test_extracted_reference_reuses_entire_relative_report_circuit(self):
        # The coordinate identities above prove that after tracing the
        # spectator |Phi_t> the same tensor = sphere output ⊗ singlet DE.
        # This is exactly the previous test's 'initial' tensor, now with a
        # physical encoding in the original labs on 96 dimensions.
        state=output(active_base())
        for label in range(16):
            old=relative_read(state,4,labels=(label,))[0]
            v=initial(old);mass=np.linalg.norm(v)**2
            np.testing.assert_allclose(apply64(SOURCE,v),v,atol=1e-13)
            np.testing.assert_allclose(apply64(V@V,v),v,atol=1e-13)
            branches,table=outcome_tables(v)
            np.testing.assert_allclose(table,np.array(q)[:,None]*mass/2*np.ones((1,2)),atol=1e-13)
            for p,branch in zip((VP,VM),branches):
                np.testing.assert_allclose(apply64(p,v),branch,atol=1e-13)
                for c in C:self.assertLess(np.linalg.norm(apply64(c,branch)),1e-12)
                np.testing.assert_allclose(apply64(LL,branch),branch,atol=1e-13)
                np.testing.assert_allclose(apply64(G,branch),branch,atol=1e-13)
        # Previous operator commutators ensure persistence through all phases
        # of the later clock. Joint lab interaction/access is NOT supplied.

    def test_retained_all_sectors_and_explicit_validity_probability(self):
        # Original code=2, internally resourced=96, rest=158, of 256.
        # Remaining complement uses neutral state-independent pointer
        # rotations, not a claim of genuine sphere behavior on that sector.
        states=[full_state(4),output(active_base()),output(remainder_base())]
        weights=[2/256,96/256,158/256]
        for labels in (tuple(range(16)),(15,0,1)):
            tables=[i_r_m_table(relative_read(s,4,labels=labels)) for s in states]
            p=len(labels)/16
            total=sum(w*t for w,t in zip(weights,tables))
            np.testing.assert_allclose(total.sum(axis=(1,2))/p,q,atol=1e-12)
            np.testing.assert_allclose(total[:,:,0],total[:,:,1],atol=1e-13)
            self.assertAlmostEqual(total[:,0,1].sum(),p/4,places=12)
            self.assertAlmostEqual(weights[1]*tables[1].sum(),p*3/8,places=12)
            self.assertAlmostEqual(weights[1]*tables[1].sum()/2,p*3/16,places=12)
        # A coherent neutral validity flag can be controlled by the
        # charge-commuting matching block projector; inactive is retained,
        # not mislabelled as an actual sign outcome.

if __name__=='__main__':unittest.main()
