"""Closed 12-tick history on the actual internal-reference record ensemble.

A finite auxiliary clock and memory circuit are specified, not derived. A
Born label is not an actual subject or an experiential incidence. We work in
orthogonal source sectors to avoid storing gigantic redundant tensors.
"""
from fractions import Fraction as F
from itertools import product
from math import log2
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import (
    I,Z,kron,active_base,output,relative_read
)
from verification.zero_relational_chirality_report_test import initial,apply64,C,LL,SWAP
from verification.zero_relative_gauge_invariant_report_test import G
from verification.zero_invariant_all_history_record_clock_test import XL,ZL
from verification.zero_spin_reversal_sign_selection_test import physical_old_to_canonical
from verification.zero_internal_contextual_reference_test import (
    B,Gint,Bs,Zj,P,value_history,gauge_history
)
from verification.zero_internal_reference_subject_valence_candidates_test import b_project,j_project

# Ordered source bits z,b,s, then working bit A and 3 tape bits.
SOURCES=list(product((0,1),repeat=3))
MEMORIES=list(product((0,1),repeat=4))
CLOCKS=12
# Each forward operation is its own inverse; reverse the list to close.
FORWARD=(('copy',0),('swap',1),('copy',1),('swap',2),('copy',2),('swap',3))
GATES=FORWARD+FORWARD[::-1]
EXPECTED={
    (0,0,0):F(1,4),(0,0,1):F(1,4),
    (0,1,0):F(1,8),(0,1,1):F(1,8),
    (1,1,0):F(1,8),(1,1,1):F(1,8),
}


def norm(v):return np.vdot(v,v).real


def gate(source,memory,instruction):
    op,k=instruction;m=list(memory)
    if op=='copy':m[0]^=source[k]
    elif op=='swap':m[0],m[k]=m[k],m[0]
    else:raise ValueError(op)
    return tuple(m)


def trajectory(source,initial=(0,0,0,0)):
    m=initial;out=[m]
    for instruction in GATES:
        m=gate(source,m,instruction);out.append(m)
    return out


def distribution(clock,subsystem):
    # Exact joint source/readout distribution at one conditional clock tick.
    out={}
    for source,p in EXPECTED.items():
        m=trajectory(source)[clock]
        record=tuple(m[k] for k in subsystem)
        out[source,record]=out.get((source,record),F(0))+p
    return out


def shannon(masses):
    return -sum(float(p)*log2(float(p)) for p in masses if p)


def marginal_records(d):
    out={}
    for (_,record),p in d.items():out[record]=out.get(record,F(0))+p
    return out


def guesses(clock,subsystem):
    d=distribution(clock,subsystem);rec=marginal_records(d);results=[]
    for i in range(3):
        score=F(0)
        for r in rec:
            groups=[sum(p for (source,rr),p in d.items() if rr==r and source[i]==v) for v in (0,1)]
            score+=max(groups)
        results.append(score)
    return tuple(results)


def transported_counterpart(t,source,memory):
    # K_t = U_t K_0 U_t^†; K_0 flips the sign-pointer source s.
    m=memory
    for ins in reversed(GATES[:t]):m=gate(source,m,ins)
    newsource=(source[0],source[1],1-source[2])
    for ins in GATES[:t]:m=gate(newsource,m,ins)
    return newsource,m


def permutation():
    # Exact unitary A on clock ⊗ three commuting source-sign sectors ⊗ memory.
    # The actual source includes further spectator degrees; A is identity on
    # those, so this permutation tests every source sign and memory basis.
    allstates=list(product(range(CLOCKS),range(8),range(16)))
    index={key:i for i,key in enumerate(allstates)}
    p=np.empty(len(allstates),int)
    for k,(t,si,mi) in enumerate(allstates):
        newmem=gate(SOURCES[si],MEMORIES[mi],GATES[t])
        p[k]=index[((t+1)%CLOCKS,si,MEMORIES.index(newmem))]
    return p,index


def apply_perm(p,v):
    result=np.zeros_like(v);result[p]=v;return result


class RelationalClockReusableMemoryTests(unittest.TestCase):
    def test_gauge_and_old_constraints_on_source_controls(self):
        # Controlled copy of each source F uses (I+F)/2 ⊗ I_A +
        # (I-F)/2 ⊗ X_A. s is Z on the old sign pointer.
        for f in (Bs,Zj):
            for a in (Gint,P):np.testing.assert_allclose(f@a-a@f,0,atol=1e-13)
            for old in (LL,G,*C,kron(XL,I,I),kron(ZL,I,I)):
                a=kron(physical_old_to_canonical(old),I,I)
                np.testing.assert_allclose(f@a-a@f,0,atol=1e-13)
        # Z_M and all A/tape operations are neutral on the old factors.
        np.testing.assert_allclose(Z@Z,I,atol=1e-13)
        for source,memory in product(SOURCES,MEMORIES):
            for instruction in GATES:
                self.assertEqual(gate(source,gate(source,memory,instruction),instruction),memory)
            self.assertEqual(trajectory(source,memory)[-1],memory)

    def test_actual_six_source_weights_and_constraints_all_16_histories(self):
        raw=output(active_base())
        for label in range(16):
            x=initial(relative_read(raw,4,labels=(label,))[0]);mass=norm(x)
            self.assertGreater(mass,0)
            total=0.
            for zbit,bbit,sbit in SOURCES:
                z,b,s=[1-2*t for t in (zbit,bbit,sbit)]
                sign=(x+s*value_history(x))/2
                v=j_project(b_project(sign,b),z)
                weight=norm(v)/mass;total+=weight
                self.assertAlmostEqual(weight,float(EXPECTED.get((zbit,bbit,sbit),0)),places=12)
                if weight>1e-14:
                    np.testing.assert_allclose(gauge_history(v),v,atol=1e-13)
                    partner=j_project(b_project((x-s*value_history(x))/2,b),z)
                    np.testing.assert_allclose(apply64(SWAP,v),-partner,atol=1e-13)
                    np.testing.assert_allclose(apply64(LL,v),v,atol=1e-13)
                    np.testing.assert_allclose(apply64(G,v),v,atol=1e-13)
                    for c in C:np.testing.assert_allclose(apply64(c,v),0,atol=1e-13)
            self.assertAlmostEqual(total,1,places=12)

    def test_stationary_clock_history_and_full_unitary_closure(self):
        p,index=permutation()
        self.assertEqual(len(set(p)),len(p))
        ident=np.arange(len(p));p12=ident.copy()
        for _ in range(CLOCKS):p12=p[p12]
        np.testing.assert_array_equal(p12,ident)
        # Exact compressed representation of the actual source sectors.
        # Each chosen source basis vector is the normalized original
        # (z,b,s)-projected physical branch, including all spectators.
        history=np.zeros(len(p),complex)
        for source,prob in EXPECTED.items():
            si=SOURCES.index(source)
            for t in range(CLOCKS):
                memory=trajectory(source)[t]
                history[index[t,si,MEMORIES.index(memory)]]=np.sqrt(float(prob)/CLOCKS)
        self.assertAlmostEqual(norm(history),1,places=12)
        shifted=apply_perm(p,history)
        np.testing.assert_allclose(shifted,history,atol=1e-13)
        inv=np.argsort(p)
        np.testing.assert_allclose(2*history-shifted-apply_perm(inv,history),0,atol=1e-13)
        for t in range(CLOCKS):
            prob=sum(abs(history[index[t,si,mi]])**2 for si in range(8) for mi in range(16))
            self.assertAlmostEqual(prob,1/CLOCKS,places=12)

    def test_transported_counterpart_symmetry_and_conditional_valence_balance(self):
        p,index=permutation();inv_index={v:k for k,v in index.items()}
        kp=np.empty(len(p),int)
        for i in range(len(p)):
            t,si,mi=inv_index[i]
            src,mem=transported_counterpart(t,SOURCES[si],MEMORIES[mi])
            kp[i]=index[t,SOURCES.index(src),MEMORIES.index(mem)]
        np.testing.assert_array_equal(kp[kp],np.arange(len(p)))
        np.testing.assert_array_equal(kp[p],p[kp])
        history=np.zeros(len(p),complex)
        for source,prob in EXPECTED.items():
            si=SOURCES.index(source)
            for t in range(CLOCKS):
                mem=trajectory(source)[t]
                history[index[t,si,MEMORIES.index(mem)]]=np.sqrt(float(prob)/CLOCKS)
        np.testing.assert_allclose(apply_perm(kp,history),history,atol=1e-13)
        # Actual source weights are counterpart equal. Tape 0 does not depend
        # on s, even when the counterpart must also flip A or tape 2.
        for t in range(13):
            sums=[F(0),F(0)];disagree=F(0)
            for src,w in EXPECTED.items():
                z,b,s=(1-2*x for x in src)
                r=1-2*trajectory(src)[t][1]
                sums[0]+=w*s*b;sums[1]+=w*s*b*r
                if r==-1:disagree+=w
            self.assertEqual(sums,[0,0])
            self.assertEqual(disagree,F(1,4) if 2<=t<=10 else F(0))
        # This is Born-weight algebra, not a derivation of actual incidence.

    def test_record_guessing_each_tick_and_reversal(self):
        # Tape only: optimal guesses from its commuting diagonal conditional
        # density states, hence also optimal over all tape POVMs.
        g=[guesses(t,(1,2,3)) for t in range(13)]
        self.assertEqual(g[0],(F(3,4),F(1,2),F(1,2)))
        self.assertEqual(g[2],(F(1),F(3,4),F(1,2)))
        self.assertEqual(g[4],(F(1),F(1),F(1,2)))
        self.assertEqual(g[6],(F(1),F(1),F(1)))
        self.assertEqual(g[7],(F(1),F(1),F(1,2)))
        self.assertEqual(g[9],(F(1),F(3,4),F(1,2)))
        self.assertEqual(g[11],g[0]);self.assertEqual(g[12],g[0])
        self.assertEqual(guesses(7,(0,1,2,3)),(F(1),F(1),F(1)))
        self.assertEqual(guesses(8,(0,1,2,3)),(F(1),F(1),F(1,2)))

    def test_actual_tape_entropy_accounting_and_working_memory(self):
        h=shannon((F(3,4),F(1,4)))
        tape=[];whole=[]
        for t in range(13):
            tape.append(shannon(marginal_records(distribution(t,(1,2,3))).values()))
            whole.append(shannon(marginal_records(distribution(t,(0,1,2,3))).values()))
        np.testing.assert_allclose(tape,[0,0,h,h,1.5,1.5,2.5,1.5,1.5,h,h,0,0],atol=1e-13)
        np.testing.assert_allclose(whole,[0,h,h,1.5,1.5,2.5,2.5,2.5,1.5,1.5,h,h,0],atol=1e-13)
        self.assertAlmostEqual(h+1+1-2.5,h-.5,places=12)
        for t in (0,2,4,6,8,10,12):
            self.assertTrue(all(trajectory(src)[t][0]==0 for src in EXPECTED))

    def test_two_qubit_tape_optimal_joint_identification_bound(self):
        weights=sorted(EXPECTED.values(),reverse=True)
        self.assertEqual(sum(weights[:4]),F(3,4))
        # For any ensemble encoded into d=4 and any POVM E_i,
        # Tr(rho_i E_i) <= min(1,Tr E_i), with sum Tr E_i=4.
        # Linear optimization gives sum of the four largest priors.
        # Achieve it by orthogonally encoding the four most likely labels,
        # sending the remaining two into one already-used code state.
        labels=sorted(EXPECTED,key=lambda k:(-EXPECTED[k],k))
        code={label:min(i,3) for i,label in enumerate(labels)}
        actual=F(0)
        for symbol in range(4):
            actual+=max((EXPECTED[label] for label in labels if code[label]==symbol),default=F(0))
        self.assertEqual(actual,F(3,4))
        # No side information or extra memory allowed; original source
        # factors would change this bound if accessible.

if __name__=='__main__':unittest.main()
