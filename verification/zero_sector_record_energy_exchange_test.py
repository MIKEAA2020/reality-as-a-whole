"""Conserved energy transfer writes records in encoded physical-spin-zero blocks.

Finite model only: no subject, phenomenology, local field theory or cosmic energy
zero is assumed to follow from the encoded registers and their interactions.
"""
import math
import unittest
from fractions import Fraction as F
from verification.zero_spin_constitution_test import X, Y, Z, add, eye, kron, mm, mv, scale, close
from verification.zero_invariant_sphere_instrument_test import adj
from verification.zero_sector_memory_incidence_test import instrument, Q


def tensor(*ops):
    a=[[1]]
    for op in ops: a=kron(a,op)
    return a

def sub(a,b): return add(a,scale(-1,b))
def comm(a,b): return sub(mm(a,b),mm(b,a))
def project(i,n=3): return [[complex(j==i and k==i) for k in range(n)] for j in range(n)]
def op(bit,which):
    ops=[eye(3),eye(2),eye(2),eye(2),eye(2)]
    ops[which]=bit
    return tensor(*ops)

def pointer(i): return tensor(project(i),eye(2),eye(2),eye(2),eye(2))

def maxabs(a): return max(abs(x) for row in a for x in row)
def expmat(v,a): return sum(x.conjugate()*y for x,y in zip(v,mv(a,v)))
N=[[0,0],[0,1]]
I=eye(48)
# Pointer R, then M1,W1,M2,W2. Physical spin-singlet logical blocks.
E=[op(N,j) for j in range(1,5)]
P=[pointer(j) for j in range(3)]
H0=add(add(E[0],E[1]),add(E[2],E[3]))

def exchange(m,w):
    return scale(.5,add(mm(op(X,m),op(X,w)),mm(op(Y,m),op(Y,w))))
def difference_sector(m,w):
    return scale(.5,sub(I,mm(op(Z,m),op(Z,w))))

FLAGS=[add(P[0],P[2]),add(P[1],P[2])]
G=[mm(FLAGS[0],exchange(1,2)),mm(FLAGS[1],exchange(3,4))]
D=[mm(FLAGS[0],difference_sector(1,2)),mm(FLAGS[1],difference_sector(3,4))]
H=add(G[0],G[1]) # g=1 and ħ=1


def unitary(t):
    u=[row[:] for row in I]
    for g,d in zip(G,D):
        step=add(I,add(scale(math.cos(t)-1,d),scale(-1j*math.sin(t),g)))
        u=mm(step,u)
    return u


def records_state(t):
    # Output of preceding asymmetric A-B-pointer measurement, with all
    # memories blank and batteries excited; mapping via U(t) on R,M,W.
    out={}
    u=unitary(t)
    for (a,b,r,_m,_n),amp in instrument().items():
        start=5 # binary 0101: blank memories and excited batteries
        idx=r*16+start
        for j,row in enumerate(u):
            value=amp*row[idx]
            if abs(value)>1e-13:
                key=(a,b,j//16,(j%16)//8,(j%8)//4,(j%4)//2,j%2)
                out[key]=out.get(key,0)+value
    return out


def reduced_b(state):
    out=[[0j]*2 for _ in range(2)]
    vals=list(state.items())
    for k,v in vals:
        for l,w in vals:
            if k[:1]+k[2:]==l[:1]+l[2:]: out[k[1]][l[1]]+=v*w.conjugate()
    return out

def state_exp(state,which):
    return sum(abs(v)**2*k[which] for k,v in state.items())

def state_local_op_exp(state, operator):
    groups={}
    for (a,b,r,m1,w1,m2,w2),amp in state.items():
        vec=groups.setdefault((a,b),[0j]*48)
        vec[r*16+m1*8+w1*4+m2*2+w2]=amp
    return sum(expmat(v,operator) for v in groups.values())

class ZeroSectorRecordEnergyExchangeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.final=records_state(math.pi/2)
        cls.early=records_state(math.pi/6)

    def test_all_interactions_conserve_local_bare_energy_exactly(self):
        self.assertLess(maxabs(comm(H,H0)),1e-10)
        for t in (0,.3,math.pi/2):
            u=unitary(t)
            close(self,mm(adj(u),u),I)
            self.assertLess(maxabs(comm(u,H0)),1e-10)
        # [H,H0]=0, so adding H0 to the Hamiltonian only adds a common
        # phase within the H0=2 prepared sector.

    def test_two_record_channels_remain_separate(self):
        self.assertLess(maxabs(comm(G[0],G[1])),1e-10)
        # The third record activates both commuting channels.
        self.assertGreater(maxabs(mm(G[0],G[1])),.5)
        for i in range(2):
            close(self,mm(G[i],G[i]),D[i])
            close(self,mm(G[i],D[i]),G[i])

    def test_conditional_memory_and_batteries_encode_three_outcomes(self):
        p=[0.0]*3
        for (a,b,r,m1,w1,m2,w2),v in self.final.items():
            p[r]+=abs(v)**2
            self.assertEqual(m1,int(r in (0,2))); self.assertEqual(m2,int(r in (1,2)))
            self.assertEqual(w1,1-m1); self.assertEqual(w2,1-m2)
        for p_i,q in zip(p,Q): self.assertAlmostEqual(p_i,float(q))
        self.assertAlmostEqual(sum(p),1)

    def test_energy_transfer_is_opposite_in_each_record_branch(self):
        u=unitary(math.pi/2); ud=adj(u)
        for j in range(2):
            mem,battery=E[2*j],E[2*j+1]
            dm=sub(mm(mm(ud,mem),u),mem)
            dw=sub(mm(mm(ud,battery),u),battery)
            self.assertLess(maxabs(add(dm,dw)),1e-10)
            # At the full swap endpoint, initially sharp energies and their
            # differences commute; intermediate-time differences need not.
            self.assertLess(maxabs(comm(dm,mem)),1e-10)
        for (a,b,r,m1,w1,m2,w2),v in self.final.items():
            self.assertEqual(m1+w1,1); self.assertEqual(m2+w2,1)

    def test_instantaneous_currents_are_conserved_and_pointer_flag_compatible(self):
        currents=[scale(1j,comm(H,e)) for e in E]
        for j in range(2):
            close(self,add(currents[2*j],currents[2*j+1]),scale(0,I))
            close(self,mm(FLAGS[j],currents[2*j]),currents[2*j])
            self.assertLess(maxabs(comm(FLAGS[j],currents[2*j])),1e-10)
            self.assertGreater(maxabs(currents[2*j]),.5)
        # Sharp excitation-presence does not commute with its current.
        self.assertGreater(maxabs(comm(E[0],currents[0])),.5)

    def test_record_energy_and_current_have_distinct_temporal_behavior(self):
        # Expectations in the symmetric Rabi step, weighted by q of its flag.
        for t in (0,math.pi/6,math.pi/2):
            state=records_state(t)
            for j in range(2):
                flag_weight=(Q[0]+Q[2],Q[1]+Q[2])[j]
                self.assertAlmostEqual(state_exp(state,3+2*j),float(flag_weight)*math.sin(t)**2)
                self.assertAlmostEqual(state_exp(state,4+2*j),1-float(flag_weight)*math.sin(t)**2)
                current=scale(1j,comm(H,E[2*j]))
                self.assertAlmostEqual(state_local_op_exp(state,current).real,float(flag_weight)*math.sin(2*t))
            # At the endpoint the stored energy is nonzero, but its rate is
            # zero even if the interaction has not yet been switched off.
        self.assertAlmostEqual(math.sin(math.pi),0)

    def test_the_interaction_is_reversible_and_records_are_not_permanent(self):
        # At π the initial memory/battery occupations return (up to phases).
        state=records_state(math.pi)
        for (a,b,r,m1,w1,m2,w2),v in state.items():
            self.assertEqual((m1,w1,m2,w2),(0,1,0,1))
        for i in range(3):
            self.assertAlmostEqual(sum(abs(v)**2 for k,v in state.items() if k[2]==i),float(Q[i]))

    def test_remote_logical_state_is_unchanged_without_conditioning(self):
        for t in (0,math.pi/6,math.pi/2):
            close(self,reduced_b(records_state(t)),scale(.5,eye(2)))

    def test_counting_only_record_recipients_omits_battery_boundary(self):
        # Every branch gains one or two units in the memory bits while
        # their batteries lose them; taking only memories gives a positive total.
        rec=state_exp(self.final,3)+state_exp(self.final,5)
        batt=(state_exp(self.final,4)-1)+(state_exp(self.final,6)-1)
        self.assertAlmostEqual(rec,float(1+Q[2]))
        self.assertAlmostEqual(batt,-rec)
        self.assertEqual(1+Q[2],F(59,40))

if __name__=='__main__': unittest.main()
