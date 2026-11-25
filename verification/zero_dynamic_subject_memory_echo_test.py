"""Boundary diagnostics and exact coherent memory echo on the same gate.

Gate-support co-occurrence is not a causal influence or integration measure.
All subject selections and Born-to-incidence interpretations are conditional.
"""
from fractions import Fraction as F
from itertools import combinations,permutations,product
from pathlib import Path
import sys
import unittest
import numpy as np

sys.path.insert(0,str(Path(__file__).resolve().parent))
from competing_subject_constitution_rules import connected_components,overlapping_local_maxima
from causal_influence_subject_gate import score
from verification.zero_all_sector_noncommuting_sphere_test import (
    I,X,Z,kron,active_base,output,relative_read
)
from verification.zero_relational_chirality_report_test import initial,apply64,C,LL
from verification.zero_relative_gauge_invariant_report_test import G
from verification.zero_internal_contextual_reference_test import (
    B,Bs,Zj,S,P,O,Gint,eye,value_history,gauge_history
)
from verification.zero_internal_reference_subject_valence_candidates_test import b_project,j_project,born_table
from verification.zero_persistent_sphere_subject_selection_test import Q,W,norm2
from verification.zero_conserving_sphere_handedness_report_test import bob_action,j_sign

# Semantic factor labels: K is the entire old 64-dimensional factor; B, j,
# M, R are qubits. A hyperedge is gate support, NOT an all-pairs influence.
K,SPHERE,J,M,R=range(5)
NODES=frozenset(range(5))
SIGN=frozenset((K,SPHERE,J,M))
MEM=frozenset((J,R))
USE=frozenset((M,R))
PULSE=frozenset((K,SPHERE,J))


def pair_table(events):
    pair={ij:F(0) for ij in combinations(sorted(NODES),2)}
    for event,weight in events:
        for ij in combinations(sorted(event),2):pair[ij]+=weight
    return pair


def sel(events):
    p=pair_table(events)
    return connected_components(NODES,p),overlapping_local_maxima(NODES,p),p


def jwrite(v0,v1):
    # Controlled-NOT from j into R on two R amplitude slices.
    return j_project(v0,1)+j_project(v1,-1),j_project(v0,-1)+j_project(v1,1)


class DynamicSubjectMemoryEchoTests(unittest.TestCase):
    def test_gates_support_and_compatible_quantum_algebra(self):
        # O = chir [P_B+ I_j + P_B- X_j], hence the sign gate W
        # has support K,B,j,M, the later Q has support K,B,j.
        from verification.zero_internal_contextual_reference_test import baseC
        np.testing.assert_allclose(O,baseC@((eye+Bs)/2+(eye-Bs)/2@kron(np.eye(64),I,X)),atol=1e-13)
        for op in (P,Gint,Bs):
            np.testing.assert_allclose(Q@op-op@Q,0,atol=1e-13)
            np.testing.assert_allclose(W@kron(op,I)-kron(op,I)@W,0,atol=1e-13)
        # B controls Q despite being conserved. The two conditional actions
        # on valid support are different: the B-minus action flips j.
        np.testing.assert_allclose(P@Q@Zj@Q@P,P@Bs@Zj@P,atol=1e-13)
        self.assertGreater(np.linalg.norm(P@(Q@Zj@Q-Zj)),1)
        # Adjacent memory write is an actual controlled unitary, not merely
        # a drawn edge; it preserves j and writes r -> z*r.
        t=kron((eye+Zj)/2,I)+kron((eye-Zj)/2,X)
        np.testing.assert_allclose(t@t,np.eye(512),atol=1e-13)
        for op in (P,Gint,Bs,Zj):
            np.testing.assert_allclose(t@kron(op,I)-kron(op,I)@t,0,atol=1e-13)
        np.testing.assert_allclose(t@kron(eye,Z)@t,kron(Zj,Z),atol=1e-13)
        # Quantum coherent back-action is visible on the gauge-invariant,
        # *joint* K+B+j operator D=O P_B-, not a local j measurement.
        d=O@(eye-Bs)/2
        np.testing.assert_allclose(Gint@d@Gint,d,atol=1e-13)
        np.testing.assert_allclose(t@kron(d,I)@t,kron(d,X),atol=1e-13)
        self.assertGreater(np.linalg.norm(d),1)
        # A bare X_j is gauge-odd; local causal graph based on it is not
        # automatically an admissible physical intervention.
        xj=kron(np.eye(64),I,X)
        np.testing.assert_allclose(Gint@xj@Gint,-xj,atol=1e-13)

    def test_coherent_memory_preparation_can_influence_joint_gauge_observable(self):
        # R in X eigenstate +1 makes its CNOT act as I on j; eigenstate
        # -1 makes it act as Zj. Prepare each on the actual sign,b=- branch.
        # The global gauge-invariant D=O P_B- is then sharp with opposite
        # signs. This is not access to D by a sphere-only observer.
        state=output(active_base())
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0])
            for s in (1,-1):
                v=b_project((x+s*value_history(x))/2,-1)
                self.assertGreater(norm2(v),0)
                for rx in (1,-1):
                    after=v if rx==1 else j_sign(v)
                    np.testing.assert_allclose(gauge_history(after),after,atol=1e-13)
                    d_after=value_history(b_project(after,-1))
                    np.testing.assert_allclose(d_after,s*rx*after,atol=1e-13)

    def test_exact_coherent_echo_operator_identity(self):
        t=kron((eye+Zj)/2,I)+kron((eye-Zj)/2,X)
        qr=kron(Q,I)
        minus=P@(eye-Bs)/2
        cb=kron(eye-minus,I)+kron(minus,X)
        # All states, including the inactive complement: the latter has
        # Q=I and both memory writes cancel.
        np.testing.assert_allclose(t@qr@t,qr@cb,atol=1e-13)
        np.testing.assert_allclose(qr@cb,cb@qr,atol=1e-13)
        np.testing.assert_allclose(cb@cb,np.eye(512),atol=1e-13)
        np.testing.assert_allclose(cb@kron(Gint,I),kron(Gint,I)@cb,atol=1e-13)
        # On valid states the final R Z value equals initial R Z times B.
        valid=kron(P,I)
        actual=(t@qr@t)@kron(eye,Z)@(t@qr@t)
        np.testing.assert_allclose(valid@actual@valid,valid@kron(Bs,Z)@valid,atol=1e-13)
        # No intervening Q: the two writes exactly undo one another.
        np.testing.assert_allclose(t@t,np.eye(512),atol=1e-13)

    def test_echo_on_all_actual_clock_histories(self):
        state=output(active_base())
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0]);mass=norm2(x)
            first={1:0.,-1:0.};final={1:0.,-1:0.};mismatch=0.
            for s in (1,-1):
                v=(x+s*value_history(x))/2
                # The sign M is carried as s; R starts in |0>.
                a,b=jwrite(v,0*v)
                first[1]+=norm2(a)/mass;first[-1]+=norm2(b)/mass
                # Q is O on these valid histories. No measurement or
                # dephasing is inserted between these coherent unitaries.
                a,b=value_history(a),value_history(b)
                a,b=jwrite(a,b)
                for r,u in ((1,a),(-1,b)):
                    final[r]+=norm2(u)/mass
                    np.testing.assert_allclose(bob_action(B,u),r*u,atol=1e-13)
                    np.testing.assert_allclose(gauge_history(u),u,atol=1e-13)
                    np.testing.assert_allclose(apply64(LL,u),u,atol=1e-13)
                    np.testing.assert_allclose(apply64(G,u),u,atol=1e-13)
                    for c in C:np.testing.assert_allclose(apply64(c,u),0,atol=1e-13)
                    # s*b*r versus s*b: differ iff r=-1.
                    if r==-1:mismatch+=norm2(u)/mass
                # Strong state identity, not just matching distributions.
                np.testing.assert_allclose(a,value_history(b_project(v,1)),atol=1e-13)
                np.testing.assert_allclose(b,value_history(b_project(v,-1)),atol=1e-13)
            np.testing.assert_allclose([first[1],first[-1]],[.75,.25],atol=1e-13)
            np.testing.assert_allclose([final[1],final[-1]],[.5,.5],atol=1e-13)
            self.assertAlmostEqual(mismatch,.5,places=12)

    def test_memory_is_actually_used_and_old_sign_can_be_recovered(self):
        use=kron(I,(I+Z)/2)+kron(X,(I-Z)/2) # order M,R
        np.testing.assert_allclose(use@use,np.eye(4),atol=1e-13)
        np.testing.assert_allclose(use@kron(Z,I)@use,kron(Z,Z),atol=1e-13)
        np.testing.assert_allclose(use@kron(X,I),kron(X,I)@use,atol=1e-13)
        # Alternate protocol: between write and Q, use R as CNOT control
        # targeting M. No intermediate measurement or dephasing is needed.
        # On simultaneous initial b,z,s and ready r=+1, the final labels
        # are (b, j'=b*z, m'=s*z, r'=b); hence s=m'*r'*j'.
        state=output(active_base())
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0]);mass=norm2(x)
            signs={s:(x+s*value_history(x))/2 for s in (1,-1)}
            # Dictionary of M,R basis amplitudes.
            slices={}
            for s in (1,-1):
                a,b=jwrite(signs[s],0*signs[s]);slices[s,1]=a;slices[s,-1]=b
            # Controlled R=-1 flips M.
            used={(m,r):slices[m if r==1 else -m,r] for m,r in product((1,-1),repeat=2)}
            pulsed={key:value_history(v) for key,v in used.items()}
            final={}
            for m in (1,-1):
                final[m,1],final[m,-1]=jwrite(pulsed[m,1],pulsed[m,-1])
            for m,r in product((1,-1),repeat=2):
                expected=0*x
                for s in (1,-1):
                    z=m*s
                    expected+=value_history(j_project(b_project(signs[s],r),z))
                np.testing.assert_allclose(final[m,r],expected,atol=1e-13)
                np.testing.assert_allclose(bob_action(B,final[m,r]),r*final[m,r],atol=1e-13)
                # Reconstructed s=m*r*j' holds on the contribution from s.
                for s in (1,-1):
                    component=j_project(final[m,r],s*m*r)
                    target=value_history(j_project(b_project(signs[s],r),m*s))
                    np.testing.assert_allclose(component,target,atol=1e-13)
            self.assertAlmostEqual(sum(norm2(v) for v in final.values())/mass,1,places=12)

    def test_classical_readout_ledger_and_balanced_incidence_conditional(self):
        tab=born_table()
        joint={}
        for (i,b,z,s),w in tab.items():
            jfinal=b*z;rfinal=b
            joint[jfinal,rfinal]=joint.get((jfinal,rfinal),F(0))+w
        self.assertEqual(joint,{(1,1):F(1,2),(-1,-1):F(1,4),(1,-1):F(1,4)})
        self.assertEqual(sum(w for (i,b,z,s),w in tab.items() if b==-1),F(1,2))
        # In the final echo r=b, so v_memory = s*b*r = s.
        for b0 in (1,-1):
            self.assertEqual(sum(w*s*b for (i,b,z,s),w in tab.items() if b==b0),0)
            self.assertEqual(sum(w*s for (i,b,z,s),w in tab.items() if b==b0),0)

    def test_stagewise_graphs_and_temporal_lineage(self):
        unit=F(1)
        stages=[SIGN,MEM,USE,PULSE,MEM]
        expected=[SIGN,MEM,USE,PULSE,MEM]
        for event,target in zip(stages,expected):
            c,(wins,ties),p=sel([(event,unit)])
            self.assertEqual(c,frozenset((target,)))
            self.assertEqual(wins,frozenset((target,)))
            self.assertFalse(ties)
        # Equal gate-co-occurrence weights; this is a diagnostic convention,
        # not a quantum signalling or Hamiltonian strength measurement.
        c,(wins,ties),pair=sel([(SIGN,unit),(MEM,unit),(PULSE,unit),(MEM,unit)])
        self.assertEqual(c,frozenset((NODES,)))
        self.assertEqual(wins,frozenset((PULSE,)))
        self.assertFalse(ties)
        self.assertEqual(score(PULSE,pair),4)
        self.assertEqual(score(SIGN,pair),3)
        self.assertEqual(score(NODES,pair),2)
        # With memory use included, the instantaneous USE and PULSE sets
        # are disjoint. Strict equality fails at every stage transition.
        self.assertTrue(all(a!=b for a,b in zip(expected,expected[1:])))
        self.assertFalse(USE&PULSE)
        c2,(wins2,ties2),p2=sel([(SIGN,unit),(MEM,unit),(USE,unit),(PULSE,unit),(MEM,unit)])
        self.assertEqual(c2,frozenset((NODES,)))
        self.assertEqual(wins2,frozenset((PULSE,)))
        self.assertFalse(ties2)
        self.assertEqual(score(PULSE,p2),4)
        self.assertEqual(score(NODES,p2),3)

    def test_weight_sensitivity_and_all_factor_relabelings(self):
        for weight,expected_winners,expected_ties in (
            (F(1,10),frozenset((PULSE,)),frozenset()),
            (F(1),frozenset((PULSE,)),frozenset()),
            (F(2),frozenset(),frozenset((MEM,PULSE,PULSE|{R}))),
            (F(3),frozenset((MEM,)),frozenset()),
        ):
            c,(wins,ties),p=sel([(SIGN,F(1)),(MEM,weight),(PULSE,F(1)),(MEM,weight)])
            self.assertEqual(c,frozenset((NODES,)))
            self.assertEqual(wins,expected_winners);self.assertEqual(ties,expected_ties)
            for perm in permutations(range(5)):
                remap=lambda sets:frozenset(frozenset(perm[i] for i in s) for s in sets)
                new={tuple(sorted((perm[i],perm[j]))):w for (i,j),w in p.items()}
                c2=connected_components(NODES,new)
                w2,t2=overlapping_local_maxima(NODES,new)
                self.assertEqual(c2,remap(c));self.assertEqual(w2,remap(wins));self.assertEqual(t2,remap(ties))

if __name__=='__main__':unittest.main()
