"""Quantum parity, operational access and conditional incidence-unity tests."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_joint_unity_bridge import (
    PHYSICAL,LOGICAL,JOINT,BYPASS,SIGNS,TYPES,encode,flip_now,flip_echo,
    counterpart,swap_type,invariant_predicates,incidence,type_transform,
    physically_summed,proposed_signed_total,independent_majority_error,shared_fault_error,
)
from verification.zero_echo_causal_subject_criterion import run,states
from verification.zero_echo_causal_subject_criterion_test import index,permutation
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_typed_echo_process import record_components,joint_quality_slices
from verification.zero_internal_reference_subject_valence_candidates_test import b_project
from verification.zero_quantum_angular_echo import mass,difference_mass
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_dressed_history_pair import encode_pair


def code_isometry():
    v=np.zeros((32,16),complex)
    for x in states(LOGICAL):v[index(PHYSICAL,encode(x)),index(LOGICAL,x)]=1
    return v


class JointUnityBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_joint_and_bypass_are_the_same_full_code_channel(self):
        v=code_isometry();joint=permutation(PHYSICAL,JOINT);bypass=permutation(PHYSICAL,BYPASS)
        np.testing.assert_allclose(v.conj().T@v,np.eye(16),atol=1e-14)
        np.testing.assert_allclose(joint@v,bypass@v,atol=1e-14)
        # With untouched spectator X, equality still holds, including all
        # entanglement with X and with any additional reference.
        np.testing.assert_allclose(np.kron(joint@v,np.eye(2)),np.kron(bypass@v,np.eye(2)),atol=1e-14)
        # A deliberately off-code intervention distinguishes the circuits.
        x={'M':0,'J':1,'L':0,'B':0,'P':0}
        self.assertNotEqual(x['B'],x['J']^x['L'])
        self.assertEqual(run(PHYSICAL,JOINT,x)['P'],1)
        self.assertEqual(run(PHYSICAL,BYPASS,x)['P'],0)
        # Also an intermediate P readout can distinguish their histories.
        x={'M':0,'J':1,'L':1,'B':0,'P':0}
        self.assertEqual(run(PHYSICAL,JOINT[:2],x)['P'],1)
        self.assertEqual(run(PHYSICAL,BYPASS,x)['P'],0)
        self.assertEqual(run(PHYSICAL,JOINT,x)['P'],0)

    def test_encoded_j_implementation_preserves_the_same_logical_test(self):
        extended=('M','J1','J2','L','B','P')
        w=np.zeros((64,32),complex)
        for x in states(PHYSICAL):
            y={'M':x['M'],'J1':x['J'],'J2':x['J'],'L':x['L'],'B':x['B'],'P':x['P']}
            w[index(extended,y),index(PHYSICAL,x)]=1
        enc_joint=(('M','P'),('J1','P'),('M','P'),('L','P'))
        enc_bypass=(('B','P'),)
        u=permutation(PHYSICAL,JOINT);up=permutation(extended,enc_joint)
        b=permutation(PHYSICAL,BYPASS);bp=permutation(extended,enc_bypass)
        np.testing.assert_allclose(up@w,w@u,atol=1e-14)
        np.testing.assert_allclose(bp@w,w@b,atol=1e-14)
        np.testing.assert_allclose(up@w@code_isometry(),bp@w@code_isometry(),atol=1e-14)
        # One physical-share flip leaves the code; this equivalence is not a
        # claim that all operations on the extra share are irrelevant.

    def test_parity_on_actual_complex_vectors_and_pair(self):
        for label in (0,7,15):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            total=norm2(x);components=record_components(x);slices=joint_quality_slices(components)
            cells={(n,k):0. for n,k in product(SIGNS,repeat=2)}
            parity={p:0. for p in SIGNS}
            for (s,z,b,n,k),rows in slices.items():
                self.assertEqual(n*k,b)
                direct=tuple([b_project(v,b) for v in part] for part in components[s,z])
                self.assertLess(difference_mass(rows,direct)/total,1e-23)
                p=mass(rows)/total;cells[n,k]+=p;parity[b]+=p
                for i in range(4):
                    paired=encode_pair((rows[0][i],rows[1][i]),i,s)
                    for (a,c,z1,z2),part in paired.items():
                        if sum(norm2(v) for v in part)/total<1e-24:continue
                        self.assertEqual((a,c),(i,i))
                        self.assertEqual((z1,z2),(k,-k))
            for p in cells.values():self.assertAlmostEqual(p,.25,places=12)
            for p in parity.values():self.assertAlmostEqual(p,.5,places=12)
            # In this pure pre-report sign-pointer+saved-memory state, tracing
            # a parity report gives F=sum p(B)^2=1/2; tracing individual N,K
            # reports gives F=sum p(N,K)^2=1/4.
            self.assertAlmostEqual(sum(p*p for p in parity.values()),.5,places=12)
            self.assertAlmostEqual(sum(p*p for p in cells.values()),.25,places=12)
            for p in SIGNS:
                self.assertAlmostEqual(sum(cells[n,k] for n,k in cells if n*k==p and n==1),.25,places=12)
                self.assertAlmostEqual(sum(cells[n,k] for n,k in cells if n*k==p and n==-1),.25,places=12)
        # P alone cannot predict N or K above chance; no assertion about
        # arbitrary extra accessible records or a phenomenal report.

    def test_unity_value_rules_under_conditional_symmetries(self):
        self.assertEqual(len(invariant_predicates((swap_type,))),8)
        old=invariant_predicates((counterpart,swap_type))
        self.assertEqual(len(old),4)
        strong=invariant_predicates((flip_now,flip_echo))
        self.assertEqual(len(strong),2)
        self.assertTrue(any(all(f.values()) for f in strong))
        self.assertTrue(any(not any(f.values()) for f in strong))
        # Equality / B-dependent unity survives old symmetries but fails
        # the stronger single-sign flips. The latter are only conditional
        # identity symmetries, not established laws of consciousness.
        equality=lambda c:c[0]==c[1]
        for c in product(SIGNS,repeat=2):
            self.assertEqual(equality(c),equality(counterpart(c)))
            self.assertEqual(equality(c),equality(swap_type(c)))
            self.assertNotEqual(equality(c),equality(flip_now(c)))

    def test_conditional_first_person_witness_and_correlated_error_control(self):
        epsilon=F(1,10);n=9
        # Under the proposed report bridge, Y answers an independently
        # meaningful joint-experience truth Z with error at most epsilon.
        # U stipulates Z=1 and strict S stipulates Z=0; this is not derived
        # from the physical parity report or from the model's qubits.
        iid=independent_majority_error(n,epsilon)
        self.assertEqual(iid,F(22273,25000000))
        marginal,majority=shared_fault_error(n,epsilon)
        self.assertEqual(marginal,epsilon)
        self.assertEqual(majority,F(9,50))
        self.assertGreater(majority,100*iid)
        # Same per-trial error bound, radically different majority error:
        # a randomly placed five-trial shared failure occurs with prob 9/50.

    def test_joint_vs_split_incidence_remains_unselected(self):
        for alpha,beta in product((F(0),F(1,3),F(1)),(F(1,4),F(1,2),F(3,4))):
            table=incidence(alpha,beta)
            self.assertEqual(sum(table.values()),1)
            self.assertEqual(physically_summed(table),{(n,k):F(1,4) for n,k in product(SIGNS,repeat=2)})
            self.assertEqual(proposed_signed_total(table),(0,0))
            for (n,k,t),p in table.items():
                self.assertEqual(p,table[-n,k,t])
                self.assertEqual(p,table[n,-k,t])
            invariant=all(p==table[type_transform(n,k,t)] for (n,k,t),p in table.items())
            self.assertEqual(invariant,alpha==1 or beta==F(1,2))
        # Even after the type-swap forces beta=1/2 for nonzero split weight,
        # alpha can be arbitrary. These are proposed incidence weights, not
        # observations or a proof that all supported subjects are actual.

if __name__=='__main__':unittest.main()
