"""Compare formal subject/quality candidates on the actual reference gate.

Pointers and fixed accessible algebras are not assumed to be conscious.
The earlier subject-selector graph is NOT embedded or reproduced here.
"""
from fractions import Fraction as F
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import (
    I,X,Y,Z,kron,active_base,output,relative_read
)
from verification.zero_relational_chirality_report_test import initial,apply64,C,LL,SWAP
from verification.zero_relative_gauge_invariant_report_test import G
from verification.zero_conserving_sphere_handedness_report_test import bob_action,j_sign,table_ij
from verification.zero_internal_contextual_reference_test import (
    B,value_history,gauge_history,Gint,Bs,Zj,S,P
)


def j_project(v,z):return (v+z*j_sign(v))/2

def b_project(v,b):return (v+b*bob_action(B,v))/2

def reduced(v,axis):
    a=np.moveaxis(v,axis,0).reshape(2,-1)
    return a@a.conj().T

def success(a,b):
    # a,b are subnormalized density matrices with total trace one.
    return .5+.5*np.sum(abs(np.linalg.eigvalsh(a-b)))


def born_table():
    table={};p0=(F(3,40),F(1,10),F(13,40));p1=(F(1,20),F(3,10),F(3,20))
    for i in range(3):
        for s in (1,-1):
            table[i,1,1,s]=p0[i]/2
            table[i,-1,1,s]=p1[i]/4
            table[i,-1,-1,s]=p1[i]/4
    return table


def weighted_sign(tab,which):
    return sum(w*s*(z if which=='j' else b) for (i,b,z,s),w in tab.items())


class InternalReferenceSubjectValenceCandidatesTests(unittest.TestCase):
    def test_candidate_operators_have_required_declared_symmetries(self):
        # Input factors order: old 64, Bob sphere, Bob j, sign pointer M.
        vj=kron(Zj,Z);vb=kron(Bs,Z)
        gauge=kron(Gint,I);counterpart=kron(S,X);valid=kron(P,I)
        for v in (vj,vb):
            np.testing.assert_allclose(gauge@v@gauge.conj().T,v,atol=1e-13)
            np.testing.assert_allclose(counterpart@v@counterpart,-v,atol=1e-13)
            np.testing.assert_allclose(valid@v-v@valid,0,atol=1e-13)
        np.testing.assert_allclose(vj@vb,vb@vj,atol=1e-13)
        self.assertGreater(np.linalg.norm((vj-vb)@valid),1)
        # These are physical pointer parities, not intrinsically felt valence.

    def test_both_candidate_parities_have_neutral_qnd_report_gates(self):
        valid=kron(P,I);gauge=kron(Gint,I)
        # The already-written sign M and the final j and sphere B commute.
        for op in (kron(Zj,Z),kron(Bs,Z)):
            value=valid@op
            neg=(valid-value)/2
            np.testing.assert_allclose(neg@neg,neg,atol=1e-13)
            for preserved in (gauge,kron(Zj,I),kron(Bs,I),kron(np.eye(256),Z)):
                np.testing.assert_allclose(neg@preserved-preserved@neg,0,atol=1e-13)
            # For any neutral ready readout qubit R,
            # U=(I-neg)⊗I+neg⊗X is unitary and inherits those commutators.
            np.testing.assert_allclose((np.eye(512)-neg)@(np.eye(512)-neg)+neg@neg,
                                       np.eye(512),atol=1e-13)
            np.testing.assert_allclose((np.eye(512)-neg)@neg,0,atol=1e-13)

    def test_actual_full_joint_table_and_candidate_disagreement_all_clocks(self):
        state=output(active_base());expected=born_table()
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0]);mass=np.linalg.norm(x)**2
            np.testing.assert_allclose(bob_action(B,j_sign(x)),x,atol=1e-13)
            branches={s:(x+s*value_history(x))/2 for s in (1,-1)}
            for s in (1,-1):
                np.testing.assert_allclose(apply64(SWAP,branches[s]),-branches[-s],atol=1e-13)
                for b in (1,-1):
                    for z in (1,-1):
                        part=j_project(b_project(branches[s],b),z)
                        tab=table_ij(part).sum(axis=1)/mass
                        for i in range(3):
                            self.assertAlmostEqual(tab[i],float(expected.get((i,b,z,s),0)),places=12)
                        np.testing.assert_allclose(gauge_history(part),part,atol=1e-13)
                        np.testing.assert_allclose(apply64(LL,part),part,atol=1e-13)
                        np.testing.assert_allclose(apply64(G,part),part,atol=1e-13)
                        for c in C:np.testing.assert_allclose(apply64(c,part),0,atol=1e-13)
            mismatch=sum(w for (i,b,z,s),w in expected.items() if b!=z)
            self.assertEqual(mismatch,F(1,4))
            self.assertEqual(weighted_sign(expected,'j'),0)
            self.assertEqual(weighted_sign(expected,'b'),0)
            for which in ('j','b'):
                minus=sum(w for (i,b,z,s),w in expected.items() if s*(z if which=='j' else b)==-1)
                self.assertEqual(minus,F(1,2))

    def test_confined_quantum_inference_for_both_candidate_algebras(self):
        # First register the sign pointer s, so its two outcomes are
        # dephased. The two binary ensembles are the conditional density
        # operators on the specified local factor plus sign pointer.
        state=output(active_base())
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0]);mass=np.linalg.norm(x)**2
            r_b=[np.zeros((4,4),complex),np.zeros((4,4),complex)]
            r_j=[np.zeros((4,4),complex),np.zeros((4,4),complex)]
            for m,s in enumerate((1,-1)):
                v=(x+s*value_history(x))/2
                flag=np.diag([int(m==0),int(m==1)])
                for b in (1,-1):
                    # Infer h_B=s*b from arbitrary POVM on j and recorded M.
                    rho=reduced(b_project(v,b),7)/mass
                    r_b[0 if s*b==1 else 1]+=kron(rho,flag)
                for z in (1,-1):
                    # Infer h_j=s*z from arbitrary POVM on Bob sphere and M.
                    rho=reduced(j_project(v,z),1)/mass
                    r_j[0 if s*z==1 else 1]+=kron(rho,flag)
            for pair in (r_b,r_j):
                self.assertAlmostEqual(np.trace(pair[0]+pair[1]).real,1,places=12)
                self.assertAlmostEqual(success(*pair),.75,places=12)
            # Its native candidate is perfectly readable in each interface;
            # neither result supplies a physical delivery path for M.

    def test_alice_record_adds_information_only_if_joint_access_exists(self):
        tab=born_table()
        # h_B from recorded M,Zj and Alice i: optimum per (i,z) is maximum
        # over b. s is independent of (i,b,z) in this actual table.
        correct=F(0)
        for i in range(3):
            for z in (1,-1):
                group=[sum(w for (ii,b,zz,s),w in tab.items() if ii==i and zz==z and b==target)
                       for target in (1,-1)]
                correct+=max(group)
        self.assertEqual(correct,F(4,5))
        # No claim that Bob automatically has Alice's record.

    def test_balance_candidates_and_noninvariant_incidence_counterexample(self):
        tab=born_table();self.assertEqual(sum(tab.values()),1)
        for key,w in tab.items():
            i,b,z,s=key;self.assertEqual(w,tab[i,b,z,-s])
        self.assertEqual(weighted_sign(tab,'j'),0)
        self.assertEqual(weighted_sign(tab,'b'),0)
        # Mismatch-only valence is -1 for negative binary parity, else 0.
        for which in ('j','b'):
            val=sum(-w for (i,b,z,s),w in tab.items() if s*(z if which=='j' else b)==-1)
            self.assertEqual(val,F(-1,2))
        # An alternative *incidence* weighting on exactly the same labels,
        # not an alternative Born state: preserve total and both signed
        # means, but break equal weights between counterpart sign branches.
        mu=dict(tab);delta=F(1,200)
        for b,z in ((1,1),(-1,-1)):
            mu[0,b,z,1]+=delta/2;mu[0,b,z,-1]-=delta/2
        self.assertEqual(sum(mu.values()),1)
        self.assertTrue(all(x>0 for x in mu.values()))
        self.assertEqual(weighted_sign(mu,'j'),0)
        self.assertEqual(weighted_sign(mu,'b'),0)
        self.assertNotEqual(mu[0,1,1,1],mu[0,1,1,-1])
        self.assertNotEqual(mu[0,-1,-1,1],mu[0,-1,-1,-1])


if __name__=='__main__':unittest.main()
