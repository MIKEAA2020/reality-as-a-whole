"""Conditional local-quality selection in the actual 20-step sphere echo.

This tests physical observables and counterfactual quality hypotheses. It does
not establish subjecthood, phenomenality, incidence weights, or cosmic energy.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import I, X, Z, kron
from verification.zero_internal_contextual_reference_test import Bs, Zj, P, eye
from verification.zero_persistent_sphere_subject_selection_test import Q
from verification.zero_joint_constitution_incidence_echo_test import coarse_table
from verification.zero_sphere_local_constitution_echo_test import twenty_tick_path
from verification.zero_clock_finite_reservoir_reuse_test import Q as THERMAL
from verification.zero_internal_connection_flag_access_balance_test import ensemble


def current_and_recovered(s,j_bit,r_bit):
    return s*(-1)**j_bit, s*(-1)**(j_bit+r_bit)


def simple_paths():
    # The pulse's b,z,r actions are independent of all source and thermal
    # labels. Its joint Born law is obtained from the actual old state.
    for (b,z,s),w in coarse_table().items():
        path=twenty_tick_path(int(b<0),(0,0,0),(0,0,0),(0,),((1,),(0,)),int(z<0))
        yield b,z,s,w,path


def disagreement_by_tick():
    out=[F(0) for _ in range(21)]
    for b,z,s,w,path in simple_paths():
        for t,(_,j,r) in enumerate(path):
            current,recovered=current_and_recovered(s,j,r)
            if current!=recovered:out[t]+=w
    return out


class EchoIntrinsicConstitutionTests(unittest.TestCase):
    def test_exact_actual_quantum_echo_observable_transport(self):
        # Real old Hilbert space, echo qubit, and valid-sector projector;
        # coherent quantum calculation, not only a classical label update.
        t=kron((eye+Zj)/2,I)+kron((eye-Zj)/2,X)
        echo=t@kron(Q,I)@t
        p=kron(P,I)
        for before,after in ((kron(Zj,Z),kron(Zj,Z)),
                             (kron(Zj,I),kron(Bs@Zj,I)),
                             (kron(eye,Z),kron(Bs,Z))):
            np.testing.assert_allclose(p@echo.conj().T@before@echo@p,
                                       p@after@p,atol=1e-13)
        np.testing.assert_allclose(p@echo.conj().T@echo@p,p,atol=1e-13)
        # M is a separate sign pointer; identity transport of M multiplies
        # each displayed operator without changing these relations.

    def test_unique_diagonal_rule_from_explicit_calibration_and_echo_neutrality(self):
        # Enumerate all 2^8 signed local rules on (s,j,r). A rule is unique
        # only in this Boolean diagonal algebra and under BOTH premises:
        # f(s,j,+)=s*j and invariance under full echo (j,r)->(b*j,b*r).
        keys=list(product((1,-1),repeat=3));survivors=[]
        for vals in product((1,-1),repeat=len(keys)):
            rule=dict(zip(keys,vals))
            if not all(rule[s,j,1]==s*j for s,j in product((1,-1),repeat=2)):
                continue
            if not all(rule[s,j,r]==rule[s,b*j,b*r]
                       for s,j,r,b in product((1,-1),repeat=4)):
                continue
            survivors.append(rule)
        self.assertEqual(len(survivors),1)
        for s,j,r in keys:self.assertEqual(survivors[0][s,j,r],s*j*r)
        # The stronger all-sector invariance is not needed: the same
        # uniqueness follows solely from the actual positive Born support at
        # the ready input and its composite-echo output.
        supported=[]
        for vals in product((1,-1),repeat=len(keys)):
            rule=dict(zip(keys,vals))
            if not all(rule[s,j,1]==s*j for s,j in product((1,-1),repeat=2)):
                continue
            if not all(rule[s,z,1]==rule[s,b*z,b] for b,z,s in coarse_table()):
                continue
            supported.append(rule)
        self.assertEqual(supported,survivors)
        # Symmetry and zero balance did not provide the calibration or the
        # phenomenological echo-neutrality premise.

    def test_composite_neutrality_does_not_mean_each_gate_is_neutral(self):
        # For actual b=-, both j signs at blank r have positive Born weight.
        tab=coarse_table()
        self.assertTrue(all(tab[-1,z,s]>0 for z,s in product((1,-1),repeat=2)))
        # Q flips j for b=- and leaves blank r unchanged, taking calibrated
        # states to calibrated states with opposite signs. Thus requiring Q
        # itself to be quality-neutral is incompatible with the calibration.
        for s,j in product((1,-1),repeat=2):
            self.assertNotEqual(s*j,s*(-j))
        for b,z,s,w,path in simple_paths():
            if (b,z)==(-1,1):
                # Actual Q, ticks 8->9, changes a calibrated blank-r local
                # state into the other calibrated blank-r local state.
                self.assertEqual(path[8][1:],(0,0))
                self.assertEqual(path[9][1:],(1,0))
        # The recovered composite f=s*j*r is conserved under the full echo,
        # but not under T or Q separately on all supported inputs.
        for b,z,s,w,path in simple_paths():
            j7,r7=path[7][1:];j10,r10=path[10][1:]
            self.assertEqual(current_and_recovered(s,j7,r7)[1],
                             current_and_recovered(s,j10,r10)[1])
        changes=[]
        for t in range(7,13):
            p=F(0)
            for b,z,s,w,path in simple_paths():
                u=current_and_recovered(s,*path[t][1:])[1]
                v=current_and_recovered(s,*path[t+1][1:])[1]
                if u!=v:p+=w
            changes.append(p)
        self.assertEqual(changes,[F(1,4),F(1,2),F(1,4),F(1,4),F(1,2),F(1,4)])

    def test_actual_all_tick_born_law_and_counterpart_balance(self):
        expected=[F(0)]*8+[F(1,4),F(1,4),F(1,2),F(1,4),F(1,4)]+[F(0)]*8
        self.assertEqual(disagreement_by_tick(),expected)
        for aux in (F(0),THERMAL):
            for t in range(21):
                match=F(0);means=[F(0),F(0)];cells=defaultdict(lambda:[F(0),F(0)])
                for b,z,s,x,f,e,st,j,r,w in ensemble(t,aux):
                    a,c=current_and_recovered(s,j,r)
                    if a!=c:match+=w
                    means[0]+=w*a;means[1]+=w*c
                    cells[(r,x[0])][0]+=w*a;cells[(r,x[0])][1]+=w*c
                self.assertEqual(match,expected[t])
                self.assertEqual(means,[0,0])
                self.assertTrue(all(v==[0,0] for v in cells.values()))
        # The symmetric physical Born law is not automatically an
        # experiential-incidence measure, and s-selected cells need not sum 0.

    def test_stationary_reference_conditioning_does_not_select_quality(self):
        disagree=disagreement_by_tick()
        self.assertEqual(sum(disagree[:20])/20,F(3,40))
        for q,want in ((1,F(1,10)),(2,F(1,20))):
            ts=[t for t in range(20) if q*t%4==2]
            self.assertEqual(sum(disagree[t] for t in ts)/len(ts),want)
            cells=defaultdict(lambda:[F(0),F(0),F(0)])
            for b,z,s,w,path in simple_paths():
                for t in ts:
                    _,j,r=path[t]
                    a,c=current_and_recovered(s,j,r)
                    v=cells[r];v[0]+=w;v[1]+=w*a;v[2]+=w*c
            for mass,a,c in cells.values():
                if mass:self.assertEqual((a,c),(0,0))
        # q=1 and q=2 are different extra joint physical reference setups,
        # not different coordinates for exactly the same experiment.

    def test_balanced_plenitude_does_not_fix_incidence_weights(self):
        # Born law is physical. mu_alt is a hypothetical SUBJECT-incidence
        # weighting on the same positive support, not a second Born law.
        tab=coarse_table()
        alt={(b,z,s):w*(F(3,2) if b==1 else F(1,2))
             for (b,z,s),w in tab.items()}
        self.assertEqual(sum(alt.values()),1)
        for law in (tab,alt):
            self.assertTrue(all(law[k]>0 for k in tab))
            self.assertEqual(sum(w*s*z for (b,z,s),w in law.items()),0)
            self.assertTrue(all(law[b,z,s]==law[b,z,-s] for b,z,s in law))
        self.assertEqual(sum(w for (b,z,s),w in tab.items() if b==-1),F(1,2))
        self.assertEqual(sum(w for (b,z,s),w in alt.items() if b==-1),F(1,4))
        # End-of-composite current vs recovered differ iff b=-.
        self.assertEqual(sum(w for (b,z,s),w in tab.items() if b==-1),F(1,2))
        self.assertEqual(sum(w for (b,z,s),w in alt.items() if b==-1),F(1,4))

if __name__=='__main__':unittest.main()
