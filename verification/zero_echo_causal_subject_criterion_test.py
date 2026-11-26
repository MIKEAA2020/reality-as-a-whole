"""Intervention-grain, code-transport and overlap tests on the sphere echo."""
from fractions import Fraction as F
from itertools import product,permutations
import unittest
import numpy as np

from verification.zero_echo_causal_subject_criterion import (
    NAMES,CIRCUIT,ENC_NAMES,ENC_CIRCUIT,QUALITY_NAMES,NOW_REPORT,ECHO_REPORT,run,states,influence,gate_support,
    local_candidates,unit_graph,quotient_graph,encode,anchor_records,target,access_probability,minimal_access,subject_overlap,split_canonical,
)
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints
from verification.zero_internal_reference_subject_valence_candidates_test import b_project,j_project
from verification.zero_internal_contextual_reference_test import value_history
from verification.zero_quantum_angular_echo import pulse
from verification.zero_joint_quality_incidence_root import R,J
from verification.zero_persistent_sphere_subject_selection_test import norm2


def subset(*x):return frozenset(x)


def index(names,d):
    n=0
    for name in names:n=2*n+d[name]
    return n


def permutation(names,circuit):
    size=2**len(names);u=np.zeros((size,size),complex)
    for x in states(names):u[index(names,run(names,circuit,x)),index(names,x)]=1
    return u


class EchoCausalSubjectCriterionTests(unittest.TestCase):
    def test_actual_echo_logical_gate_path_and_temporal_grain(self):
        expected=(({'J','R'},('J','R')),({'B','J'},('B','J')))
        for edge,c in expected:
            self.assertEqual(influence(NAMES,(c,)),{c})
        self.assertEqual(influence(NAMES,CIRCUIT[1:4]),{('B','J'),('B','R')})
        self.assertEqual(influence(NAMES,CIRCUIT[1:4]+CIRCUIT[1:4]),set())
        self.assertIn(('J','R'),influence(NAMES,(CIRCUIT[1],)))
        self.assertNotIn(('J','R'),influence(NAMES,CIRCUIT[1:4]))
        self.assertEqual(influence(NAMES,CIRCUIT),
                         {('B','J'),('B','R'),('B','H'),('J','L'),('L','H')})
        for x in states(NAMES):
            out=run(NAMES,CIRCUIT,x)
            self.assertEqual(out['J'],x['J']^x['B'])
            self.assertEqual(out['R'],x['R']^x['B'])
            self.assertEqual(out['L'],x['L']^x['J'])
            self.assertEqual(out['H'],x['H']^x['L']^x['B'])

    def test_reduced_echo_signs_match_original_complex_vectors(self):
        root=output(active_base())
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            _,total,checkpoints=quantum_echo_checkpoints(x,s,4)
            for i in range(4):
                b=R[i];z=b*J[i]
                state={'B':int(b==-1),'J':int(z==-1),'R':0,'L':0,'H':0}
                for n in range(4):
                    if n:state=run(NAMES,(CIRCUIT[n],),state)
                    j=1-2*state['J'];r=1-2*state['R']
                    vector=checkpoints[n][0 if r==1 else 1][i]
                    wrong=checkpoints[n][1 if r==1 else 0][i]
                    self.assertLess(norm2(wrong)/total,1e-23)
                    self.assertLess(norm2(b_project(vector,b)-vector)/total,1e-23)
                    self.assertLess(norm2(j_project(vector,j)-vector)/total,1e-23)
        # This checks support and actual coherent vectors, not physical
        # admissibility of every formal bit-clamp used in the channel graph.

    def test_direction_discarding_makes_overlapping_modules(self):
        graph=unit_graph(CIRCUIT)
        self.assertEqual(gate_support(CIRCUIT),{
            subset('B','J'),subset('J','R'),subset('J','L'),subset('J','H'),subset('L','H')})
        expected={subset('J','L','H'),subset('B','J','L','R'),subset('B','J','H','R')}
        self.assertEqual(local_candidates(NAMES,graph),expected)
        # The primitive causal support is acyclic, with no opposite edge.
        directed=set(CIRCUIT)
        self.assertTrue(all((b,a) not in directed for a,b in directed))
        order={name:i for i,name in enumerate(('B','J','L','R','H'))}
        self.assertTrue(all(order[a]<order[b] for a,b in directed))
        # Pointer M has no edge in this reduced circuit and is not selected.
        self.assertEqual(local_candidates(NAMES+('M',),graph),expected)
        self.assertTrue(all('M' not in x for x in expected))

    def test_quality_report_coupling_changes_the_candidate_graph(self):
        old=local_candidates(NAMES,unit_graph(CIRCUIT))
        now=local_candidates(QUALITY_NAMES,unit_graph(NOW_REPORT))
        echo=local_candidates(QUALITY_NAMES,unit_graph(ECHO_REPORT))
        self.assertEqual(len(now),10)
        self.assertEqual(len(echo),5)
        self.assertTrue(all(s not in now for s in old))
        self.assertEqual(sum('M' in s for s in now),5)
        self.assertEqual(sum('M' in s for s in echo),2)
        for x in states(QUALITY_NAMES):
            if x['K']!=0:continue
            a=run(QUALITY_NAMES,NOW_REPORT,x)
            b=run(QUALITY_NAMES,ECHO_REPORT,x)
            self.assertEqual(a['K'],x['M']^a['J'])
            self.assertEqual(b['K'],x['M']^b['J']^b['R'])
        # The extra K coupling is a real change of physical protocol, not a
        # passive relabeling and not proof of changed or unchanged subjects.

    def test_candidate_graph_is_covariant_under_relabeling(self):
        graph=unit_graph(CIRCUIT);original=local_candidates(NAMES,graph)
        for names in permutations(NAMES):
            perm=dict(zip(NAMES,names))
            moved={frozenset(perm[v] for v in e):w for e,w in graph.items()}
            expected={frozenset(perm[v] for v in s) for s in original}
            self.assertEqual(local_candidates(NAMES,moved),expected)
        # Mere relabeling transports sites and edges; code refinement is a
        # different question, involving an additional physical register.

    def test_actual_ready_record_access_has_redundancy_and_overlapping_supports(self):
        self.assertEqual(minimal_access('B'),{subset('B'),subset('R'),subset('H'),subset('J','L')})
        self.assertEqual(minimal_access('now'),{
            subset('M','J'),subset('M','B','L'),subset('M','R','L'),subset('M','H','L')})
        self.assertEqual(minimal_access('echo'),{
            subset('M','L'),subset('M','B','J'),subset('M','R','J'),subset('M','H','J')})
        self.assertEqual(access_probability(('B','J','R','L','H'),'now'),F(1,2))
        self.assertEqual(access_probability(('B','J','R','L','H'),'echo'),F(1,2))
        self.assertEqual(sum(p for row,p in anchor_records()),1)
        # M and L/H must be physically available; exact success is conditional
        # on the specified ready records and state family, not all states.

    def test_code_equivalent_classical_records_are_not_quantum_clones(self):
        # W maps the reduced input B,J plus ready R,L,H into the actual
        # output of the coherent reversible report circuit.
        u=permutation(NAMES,CIRCUIT);w=np.zeros((32,4),complex)
        for b,j in product((0,1),repeat=2):
            source={'B':b,'J':j,'R':0,'L':0,'H':0}
            w[:,2*b+j]=u[:,index(NAMES,source)]
        for fields in (('B',),('R',),('H',),('J','L')):
            diagonal=np.array([(-1)**sum(x[v] for v in fields) for x in states(NAMES)])
            logical=np.diag([1,1,-1,-1])
            np.testing.assert_allclose(diagonal[:,None]*w,w@logical,atol=1e-14)
        # Fix logical J=0; B=|+> and |-> have different quantum phases.
        # Every perfect classical B access set below loses that phase when
        # the complement is traced. Classical record redundancy != cloning.
        plus=(w[:,0]+w[:,2])/np.sqrt(2);minus=(w[:,0]-w[:,2])/np.sqrt(2)
        def reduced(v,fields):
            axes=[NAMES.index(a) for a in fields]
            axes+= [i for i in range(len(NAMES)) if i not in axes]
            matrix=v.reshape((2,)*len(NAMES)).transpose(axes).reshape(2**len(fields),-1)
            return matrix@matrix.conj().T
        for fields in (('B',),('R',),('H',),('J','L')):
            np.testing.assert_allclose(reduced(plus,fields),reduced(minus,fields),atol=1e-14)
        # Outside the ready code even the basic equations can fail.
        x={'B':0,'J':0,'R':0,'L':1,'H':0}
        self.assertNotEqual(run(NAMES,CIRCUIT,x)['H'],x['B'])

    def test_disconnected_system_does_not_change_local_candidates(self):
        base=unit_graph(CIRCUIT);original=local_candidates(NAMES,base)
        for w in (F(1),F(17),F(100)):
            g={**base,subset('X','Y'):w}
            all_candidates=local_candidates(NAMES+('X','Y'),g)
            self.assertEqual(all_candidates,original|{subset('X','Y')})

    def test_coherent_encoding_preserves_full_logical_channel(self):
        v=np.zeros((64,32),complex)
        for x in states(NAMES):v[index(ENC_NAMES,encode(x)),index(NAMES,x)]=1
        u=permutation(NAMES,CIRCUIT);ue=permutation(ENC_NAMES,ENC_CIRCUIT)
        np.testing.assert_allclose(v.conj().T@v,np.eye(32),atol=1e-14)
        np.testing.assert_allclose(ue.conj().T@ue,np.eye(64),atol=1e-14)
        np.testing.assert_allclose(ue@v,v@u,atol=1e-14)
        # Equality of isometries covers arbitrary coherences and entanglement
        # with a reference, not just classical diagonal probabilities.
        for x in states(NAMES):
            code=encode(x)
            bad=dict(code);bad['J1']^=1
            self.assertNotEqual(bad['J1'],bad['J2'])
            good=dict(bad);good['J2']^=1
            self.assertEqual(good['J1'],good['J2'])

    def test_encoded_j_register_intertwines_actual_complex_echo_gates(self):
        root=output(active_base())
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            _,total,checkpoints=quantum_echo_checkpoints(x,s,4)
            for rows in checkpoints:
                for i in range(4):
                    for v in (rows[0][i],rows[1][i]):
                        parts={z:j_project(v,z) for z in (1,-1)}
                        for z in (1,-1):
                            # Actual Q on the old carrier, then B-controlled
                            # X on the encoded copy, equals copy after Q.
                            got=(b_project(value_history(parts[z]),1)+
                                 b_project(value_history(parts[-z]),-1))
                            want=j_project(value_history(v),z)
                            self.assertLess(norm2(got-want)/total,1e-23)
                    oldpair=(rows[0][i],rows[1][i])
                    for z in (1,-1):
                        p=tuple(j_project(v,z) for v in oldpair)
                        # J-copy-controlled T vs original J-controlled T.
                        got=p if z==1 else (p[1],p[0])
                        # pulse accepts one-element angular rows.
                        target=pulse(([p[0]],[p[1]]),'T')
                        self.assertLess(sum(norm2(a-b[0]) for a,b in zip(got,target))/total,1e-23)
        # Physical isometry tested on the original complex history support;
        # full unconstrained Hilbert-space equality is not asserted.

    def test_naive_independent_share_graph_changes_modules(self):
        old=local_candidates(NAMES,unit_graph(CIRCUIT))
        refined_graph=unit_graph(ENC_CIRCUIT)
        refined=local_candidates(ENC_NAMES,refined_graph)
        expected={subset('B','J1','J2','R'),subset('B','H','J1','R'),
                  subset('B','H','J2','L'),subset('H','J1','L','R')}
        self.assertEqual(refined,expected)
        collapse=lambda s:frozenset('J' if i in ('J1','J2') else i for i in s)
        self.assertNotEqual({collapse(s) for s in refined},old)
        # If J1,J2 are *stipulated* to be one logical site and parallel
        # logical gates are deduplicated, select after quotient, not before.
        logical=quotient_graph(refined_graph)
        self.assertEqual(logical,unit_graph(CIRCUIT))
        self.assertEqual(local_candidates(NAMES,logical),old)
        # The encoded device really has an extra factor: treating it as
        # a harmless subject refinement is a further constitution premise.

    def test_overlapping_candidates_need_nontrivial_incidence_sharing(self):
        candidates=local_candidates(NAMES,unit_graph(CIRCUIT))
        multiplicity=subject_overlap(candidates,NAMES)
        self.assertEqual(multiplicity,{'B':2,'J':3,'R':2,'L':2,'H':2})
        rates={'B':-1,'J':1,'R':0,'L':0,'H':0}
        totals={s:sum(rates[i] for i in s) for s in candidates}
        self.assertEqual(sum(rates.values()),0)
        self.assertEqual(sum(totals.values()),1)
        split=split_canonical(rates,candidates)
        self.assertEqual(split[subset('J','L','H')],F(1,3))
        self.assertEqual(split[subset('B','J','L','R')],F(-1,6))
        self.assertEqual(split[subset('B','J','H','R')],F(-1,6))
        self.assertEqual(sum(split.values()),0)
        # This is an abstract formal flow on a candidate graph. It is not a
        # quantum-energy or felt-valence calculation for the echo.

if __name__=='__main__':unittest.main()
