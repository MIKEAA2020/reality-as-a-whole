"""Deriving a canonical conditional zero-penalty, and testing missing inputs.

This continues the actual finite all-sector circuit. It does not assert that
its charges, active subspace, phase-sensitive observable, clock, or selection
rules are derived from metaphysical zero, or establish consciousness.
"""
import math
import unittest
import numpy as np
from verification.zero_all_sector_branchwise_balance_test import (
    U8,U64,L64,Q64,PACT,H64,V16,J16,P16,I2,apply
)
from verification.zero_all_sector_record_involution_test import event_probs
from verification.zero_all_sector_sphere_clock_work_test import complement_state
from verification.zero_energy_sphere_work_incidence_test import (
    X,Y,Z,Jactive,full_state,relative_read,project_h,
    i_r_m_table,reduced_record,reduced_work,embed_records_and_work,target_memory
)
from verification.zero_reciprocal_subject_exchange_test import n, g
from verification.zero_dual_pair_sphere_energy_instrument_test import dual_output

I64=np.eye(64,dtype=complex)
I16=np.eye(16,dtype=complex)
X16=V16-(I16-P16)
Z16=np.zeros((16,16),complex)
Z16[6,6]=1
Z16[9,9]=-1


def vtheta(theta):
    return I16-P16+math.cos(theta)*X16+math.sin(theta)*Z16


def dtheta(theta):
    return I16-P16+math.cos(theta/2)*P16-1j*math.sin(theta/2)*J16


def utheta(theta):
    return -np.kron(np.kron(Z,vtheta(theta)),X)


def physical_rotation(theta):
    return np.kron(np.kron(I2,dtheta(theta)),I2)


def pplus(theta):
    return (PACT+L64)@(I64+utheta(theta))/4


def pminus(theta):
    return (PACT+L64)@(I64-utheta(theta))/4


def rotate_work(v,theta):
    d=math.cos(theta/2)*I2-1j*math.sin(theta/2)*Jactive
    return np.einsum('wu,...rut->...rwt',d,v,optimize=True)


def charges64():
    # Two concrete, commuting SU(2) representations acting on work and
    # record-target. Their relative orientation is explicitly stipulated.
    a=[np.kron(np.kron(I2,x),I2) for x in (J16,X16,Z16)]
    b=[-np.kron(np.kron(Z,P16),Z),
        np.kron(np.kron(Z,P16),X),
       -np.kron(np.kron(I2,P16),Y)]
    return a,b,[x+y for x,y in zip(a,b)]


class ZeroConstitutionHamiltonianPhaseGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.states=(full_state(4),complement_state(4))
        cls.clocks=[relative_read(v,4,labels=tuple(range(16))) for v in cls.states]

    def test_zero_constraint_alone_has_large_kernel_even_with_involution(self):
        ev=np.linalg.eigvalsh(Q64)
        self.assertEqual(np.count_nonzero(abs(ev)<1e-12),60)
        # Q has eigenvalues ±2 and 0, so this is exactly its zero projector.
        p0=I64-Q64@Q64/4
        np.testing.assert_allclose(p0@p0,p0,atol=1e-14)
        common=p0@(I64+U64)/2
        np.testing.assert_allclose(common@common,common,atol=1e-14)
        self.assertAlmostEqual(np.trace(common).real,30,places=13)
        active=common@PACT
        self.assertAlmostEqual(np.trace(active).real,2,places=13)
        self.assertAlmostEqual(np.trace(common@(I64-PACT)).real,28,places=13)
        # The prior rank-two statement explicitly assumed active work. Q=0
        # and U=+1 alone do not exclude the 28 inactive work-sector states.

    def test_ground_projector_and_canonical_flat_hamiltonian(self):
        P=pplus(0)
        np.testing.assert_allclose(P.conj().T,P,atol=1e-14)
        np.testing.assert_allclose(P@P,P,atol=1e-14)
        self.assertAlmostEqual(np.trace(P).real,2,places=13)
        np.testing.assert_allclose(Q64@P,0,atol=1e-14)
        np.testing.assert_allclose(U64@P,P,atol=1e-14)
        H=I64-P
        np.testing.assert_allclose(H@H,H,atol=1e-14)
        np.testing.assert_allclose(H@Q64,Q64@H,atol=1e-14)
        np.testing.assert_allclose(H@U64,U64@H,atol=1e-14)
        np.testing.assert_allclose(np.linalg.eigvalsh(H),[0]*2+[1]*62,atol=1e-13)
        for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
            nums=np.asarray(n,complex)
            N=np.kron(np.kron(I2,sum(nums[k] for k in inds)),I2)
            np.testing.assert_allclose(H@N,N@H,atol=1e-14)
        # Given the selected subspace, I-P is the unique orthogonal projector
        # with that kernel. Its choice as a physical H and energy scale are
        # additional assumptions. It is zero on its entire ground space.

    def test_selected_ground_space_does_not_select_excited_dynamics(self):
        P=pplus(0);H=I64-P
        np.testing.assert_allclose(H64@P,0,atol=1e-14)
        np.testing.assert_allclose(H@P,0,atol=1e-14)
        # Both ground spaces are rank 2 but the old H has distinct positive
        # excitation eigenvalues while the projector has just one.
        old=np.unique(np.round(np.linalg.eigvalsh(H64),12))
        new=np.unique(np.round(np.linalg.eigvalsh(H),12))
        np.testing.assert_allclose(old,[0,.5,1,1.5,2],atol=1e-13)
        np.testing.assert_allclose(new,[0,1],atol=1e-13)
        self.assertGreater(np.linalg.norm(H64-H),1)

    def test_sign_of_involution_eigencondition_is_not_fixed_by_its_action(self):
        F=np.kron(np.kron(I2,I16),Z)
        np.testing.assert_allclose(F@Q64@F,Q64,atol=1e-14)
        np.testing.assert_allclose(F@L64@F,L64,atol=1e-14)
        np.testing.assert_allclose(F@U64@F,-U64,atol=1e-14)
        np.testing.assert_allclose(F@pplus(0)@F,pminus(0),atol=1e-14)
        np.testing.assert_allclose(pplus(0)@pminus(0),0,atol=1e-14)
        self.assertAlmostEqual(np.trace(pminus(0)).real,2,places=13)
        # U and -U induce identical conjugations of every observable. The
        # plus/minus subspaces are nonetheless distinguishable by a given
        # phase-sensitive joint observable; they are not declared gauge.
        rng=np.random.default_rng(319)
        O=rng.normal(size=(64,64))+1j*rng.normal(size=(64,64))
        np.testing.assert_allclose(U64@O@U64,(-U64)@O@(-U64),atol=1e-14)

    def test_continuum_of_opposite_exchanges_and_covariant_projectors(self):
        A=np.kron(np.kron(I2,J16),I2)
        B=-np.kron(np.kron(Z,P16),Z)
        record=np.kron(np.kron(Z,I16),I2)
        target=np.kron(np.kron(I2,I16),Z)
        for theta in (0,.37,math.pi/2,math.pi,2*math.pi):
            U=utheta(theta);D=physical_rotation(theta);P=pplus(theta)
            np.testing.assert_allclose(U@U,I64,atol=1e-14)
            np.testing.assert_allclose(D@D.conj().T,I64,atol=1e-14)
            np.testing.assert_allclose(D@U64@D.conj().T,U,atol=1e-14)
            np.testing.assert_allclose(D@Q64@D.conj().T,Q64,atol=1e-14)
            np.testing.assert_allclose(U@A@U,-A,atol=1e-14)
            np.testing.assert_allclose(U@B@U,-B,atol=1e-14)
            np.testing.assert_allclose(U@record@U,record,atol=1e-14)
            np.testing.assert_allclose(U@target@U,-target,atol=1e-14)
            np.testing.assert_allclose(P,D@pplus(0)@D.conj().T,atol=1e-14)
            np.testing.assert_allclose(P@P,P,atol=1e-14)
            self.assertAlmostEqual(np.trace(P).real,2,places=13)
            np.testing.assert_allclose((I64-P)@Q64,Q64@(I64-P),atol=1e-14)
        # All U_theta preserve the declared work charges. Their induced
        # physical phase action is distinct if a fixed U_0 is observable;
        # no claim is made that every possible fundamental ontology agrees.
        self.assertGreater(np.linalg.norm(utheta(.37)-U64),.1)

    def test_actual_circuit_phase_family_retains_records_but_changes_joint_witness(self):
        for state,clocks in zip(self.states,self.clocks):
            for theta in (0,math.pi/3,math.pi):
                v=rotate_work(state,theta)
                self.assertLess(np.linalg.norm(apply(
                    np.kron(np.kron(I2,Jactive),I2)-np.kron(np.kron(Z,I2),Z),v)),1e-12)
                self.assertAlmostEqual(np.vdot(v,apply(U8,v)).real,math.cos(theta),places=12)
                rot=[rotate_work(x,theta) for x in clocks]
                np.testing.assert_allclose(i_r_m_table(rot),i_r_m_table(clocks),atol=1e-13)
                for h in (0,1):
                    for orig,new in zip(clocks,rot):
                        np.testing.assert_allclose(event_probs(project_h(orig,h)),
                                                   event_probs(project_h(new,h)),atol=1e-14)
                np.testing.assert_allclose(reduced_record(rot),reduced_record(clocks),atol=1e-13)
                np.testing.assert_allclose(reduced_work(rot),reduced_work(clocks),atol=1e-13)
                if theta==math.pi:
                    self.assertAlmostEqual(abs(np.vdot(state,v)),0,places=12)
        # U0 is a specified phase-sensitive joint R-W-T probe, not an
        # automatically available operation to a confined R or T observer.

    def test_work_algebra_is_derived_from_existing_exchange_and_occupations(self):
        numbers=np.asarray(n,complex)
        exchange=np.asarray(g,complex)
        np.testing.assert_allclose(X16,exchange,atol=1e-14)
        np.testing.assert_allclose(J16,1j*(exchange@numbers[0]-numbers[0]@exchange),atol=1e-14)
        np.testing.assert_allclose(Z16,P16@(numbers[2]-numbers[0])@P16,atol=1e-14)
        np.testing.assert_allclose(1j*(J16@X16-X16@J16),-2*Z16,atol=1e-14)
        # Existing exchange and occupation yield both noncommuting partners;
        # the record-target representation and relative orientation remain inputs.

    def test_three_component_zero_derives_involution_eigencondition(self):
        a,b,g=charges64()
        for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
            np.testing.assert_allclose(a[i]@a[j]-a[j]@a[i],2j*a[k],atol=1e-14)
            np.testing.assert_allclose(b[i]@b[j]-b[j]@b[i],2j*b[k],atol=1e-14)
            np.testing.assert_allclose(g[i]@g[j]-g[j]@g[i],2j*g[k],atol=1e-14)
            np.testing.assert_allclose(a[i]@b[j],b[j]@a[i],atol=1e-14)
        np.testing.assert_allclose(g[0],Q64,atol=1e-14)
        np.testing.assert_allclose(g[1]@g[1],2*(PACT-PACT@U64),atol=1e-14)
        # Hence on active work, g2|ψ>=0 is *equivalent* to U|ψ>=|ψ>.
        # With g1=0, their commutator also forces g3|ψ>=0.
        for v,vs in zip(self.states,self.clocks):
            g8=[np.kron(np.kron(I2,Jactive),I2)-np.kron(np.kron(Z,I2),Z),
                np.kron(np.kron(I2,X),I2)+np.kron(np.kron(Z,I2),X),
                np.kron(np.kron(I2,Z),I2)-np.kron(np.kron(I2,I2),Y)]
            for state in [v]+vs:
                for op in g8:
                    np.testing.assert_allclose(apply(op,state),0,atol=2e-14)

    def test_casimir_reproduces_canonical_flat_penalty_with_no_weight_tuning(self):
        a,b,g=charges64()
        cas=sum(op@op for op in g)
        for op in g:
            np.testing.assert_allclose(cas@op,op@cas,atol=1e-14)
        H=(I64-PACT)+cas/8
        np.testing.assert_allclose(H,I64-pplus(0),atol=1e-14)
        np.testing.assert_allclose(H@H,H,atol=1e-14)
        np.testing.assert_allclose(np.linalg.eigvalsh(H),[0]*2+[1]*62,atol=1e-13)
        for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
            nums=np.asarray(n,complex)
            N=np.kron(np.kron(I2,sum(nums[k] for k in inds)),I2)
            for op in g:
                np.testing.assert_allclose(op@N,N@op,atol=1e-14)
        # The gap normalization and inactive-space penalty are conventions;
        # assuming this Casimir is the physical generator is an extra law.

    def test_rotating_relative_axes_keeps_3balance_but_changes_selected_phase(self):
        a,b,g=charges64()
        for theta in (0,.37,math.pi/2,math.pi):
            D=physical_rotation(theta)
            gt=[D@op@D.conj().T for op in g]
            np.testing.assert_allclose(gt[0],Q64,atol=1e-14)
            for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
                np.testing.assert_allclose(gt[i]@gt[j]-gt[j]@gt[i],2j*gt[k],atol=1e-14)
            H=I64-PACT+sum(x@x for x in gt)/8
            np.testing.assert_allclose(H,I64-pplus(theta),atol=1e-14)
        # Three-component balance selects a state only after its *relative*
        # representation/orientation is given; these alternatives share Q1.

    def test_complementary_zero_fixes_work_pulse_within_existing_family(self):
        g2=np.kron(np.kron(I2,X),I2)+np.kron(np.kron(Z,I2),X)
        g3=np.kron(np.kron(I2,Z),I2)-np.kron(np.kron(I2,I2),Y)
        for angle in (0,math.pi/8,math.pi/4):
            v=target_memory(embed_records_and_work(dual_output(4,4),angle),math.pi/2)
            for op in (g2,g3):
                self.assertAlmostEqual(np.linalg.norm(apply(op,v))**2,
                                       2*(1-math.sin(2*angle)),places=12)
        # Q1=0 for all angles; the other two signed balances select pi/4
        # only given their chosen relative axes and this pulse family.

    def test_phase_condition_follows_only_if_corresponding_involution_is_input(self):
        for theta in (0,.41,math.pi):
            # Check on each physically realized branch without constructing
            # the large physical lab embedding: the work isometry intertwines.
            u=-np.kron(np.kron(Z,math.cos(theta)*X+math.sin(theta)*Z),X)
            for v in self.states:
                w=rotate_work(v,theta)
                np.testing.assert_allclose(apply(u,w),w,atol=2e-14)
        # The entire family obeys identical Q=0 and opposite readout rules;
        # choosing one U_theta or declaring phase rotations gauge must be
        # justified separately, not inferred from cancellation alone.

if __name__=='__main__':
    unittest.main()
