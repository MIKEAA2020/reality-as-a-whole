"""Finite bath, battery and fresh sources in the actual sphere history.

All sources and thermal purifications are chosen inputs. The added signed
energy is a constructed finite charge, not an objective cosmological energy.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import log,log2
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import I,kron,active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial,apply64,C,LL,SWAP
from verification.zero_relative_gauge_invariant_report_test import G
from verification.zero_invariant_all_history_record_clock_test import XL,ZL
from verification.zero_spin_reversal_sign_selection_test import physical_old_to_canonical
from verification.zero_internal_contextual_reference_test import Gint,Bs,P,value_history,gauge_history
from verification.zero_internal_reference_subject_valence_candidates_test import b_project

N=3
Q=F(1,4)
LEVELS=7
INITIAL_N=3
CLOCKS=14
BITS3=list(product((0,1),repeat=N))
MACHINE=list(product((0,1),repeat=N+1)) # A,R0,R1,R2
# Interface flips all source qubits iff B=-1. Source/reference parities
# then encode the old sphere sign; sources themselves remain unbiased.
FORWARD=(('interface',0),)+tuple(z for i in range(N) for z in (('write',i),('swap',i)))
GATES=FORWARD+FORWARD[::-1]


def norm(v):return np.vdot(v,v).real


def write(xbit,a,n):
    # Finite battery n=0,...,6: exchange |A=0,n> ↔ |A=1,n-1>
    # for n=1,...,6, fixing the two unpaired endpoint states.
    if not xbit:return a,n
    if a==0 and n>0:return 1,n-1
    if a==1 and n<LEVELS-1:return 0,n+1
    return a,n


def gate(bbit,y,memory,n,op):
    typ,i=op;m=list(memory)
    if typ=='interface':y=tuple(v^bbit for v in y)
    elif typ=='write':m[0],n=write(y[i],m[0],n)
    elif typ=='swap':m[0],m[i+1]=m[i+1],m[0]
    else:raise ValueError(op)
    return y,tuple(m),n


def path(bbit,x,f):
    y=x;memory=(0,)+f;n=INITIAL_N;states=[(y,memory,n)]
    for op in GATES:
        y,memory,n=gate(bbit,y,memory,n,op);states.append((y,memory,n))
    return states


def weight(b,x,f,q=Q):
    p=F(1,2**(N+1)) # old B is unbiased, independent prepared source refs
    for bit in f:p*=q if bit else 1-q
    return p


def ensemble(t,q=Q):
    for b,x,f in product((0,1),BITS3,BITS3):
        w=weight(b,x,f,q)
        if w:yield b,x,f,*path(b,x,f)[t],w


def energy(memory,n,f):
    return n-INITIAL_N+memory[0]+sum(memory[1:])-sum(f)


def shannon(probs):
    return -sum(float(p)*log2(float(p)) for p in probs if p)


def marginal(t,key,q=Q):
    d=defaultdict(F)
    for b,x,f,y,m,n,w in ensemble(t,q):d[key(b,x,f,y,m,n)]+=w
    return dict(d)


def avg(t,fun,q=Q):
    return sum((w*fun(b,x,f,y,m,n) for b,x,f,y,m,n,w in ensemble(t,q)),F(0))


def original_source(b,x):return tuple(v^b for v in x)


def best_from_bath(t,i,q=Q):
    # Reduced bath states conditional on source labels are diagonal after
    # tracing orthogonal source/reference and reservoir purifiers.
    d=defaultdict(lambda:[F(0),F(0)])
    for b,x,f,y,m,n,w in ensemble(t,q):d[m[1:]][original_source(b,x)[i]]+=w
    return sum((max(values) for values in d.values()),F(0))


def full_guess(t,q=Q):
    d=defaultdict(lambda:defaultdict(F))
    for b,x,f,y,m,n,w in ensemble(t,q):d[m[1:]][original_source(b,x)]+=w
    return sum((max(values.values()) for values in d.values()),F(0))


def permutation():
    # B, each source reference x and each reservoir purifier f are fixed
    # by the clock gates. x,f are kept as spectator indices in the history.
    basis=list(product(range(CLOCKS),range(2),range(8),range(16),range(LEVELS)))
    idx={item:k for k,item in enumerate(basis)}
    p=np.empty(len(basis),int)
    for k,(t,b,yi,mi,n) in enumerate(basis):
        y2,m2,n2=gate(b,BITS3[yi],MACHINE[mi],n,GATES[t])
        p[k]=idx[((t+1)%CLOCKS,b,BITS3.index(y2),MACHINE.index(m2),n2)]
    return p,idx,basis


def apply_perm(p,v):
    r=np.zeros_like(v);r[p]=v;return r


class FiniteReservoirClockTests(unittest.TestCase):
    def test_finite_battery_gate_exactly_unitary_and_energy_conserving(self):
        for x in (0,1):
            images=set()
            for a,n in product((0,1),range(LEVELS)):
                aa,nn=write(x,a,n)
                images.add((aa,nn));self.assertEqual(write(x,aa,nn),(a,n))
                self.assertEqual(a+n,aa+nn)
            self.assertEqual(len(images),2*LEVELS)
        for b,y,m,n in product((0,1),BITS3,MACHINE,range(LEVELS)):
            for op in GATES:
                yy,mm,nn=gate(b,y,m,n,op)
                self.assertEqual(gate(b,yy,mm,nn,op),(y,m,n))
                self.assertEqual(n+sum(m),nn+sum(mm))

    def test_source_interface_gauge_and_actual_dephasing(self):
        for a in (Gint,P):np.testing.assert_allclose(Bs@a-a@Bs,0,atol=1e-13)
        for old in (LL,G,*C,kron(XL,I,I),kron(ZL,I,I)):
            a=kron(physical_old_to_canonical(old),I,I)
            np.testing.assert_allclose(Bs@a-a@Bs,0,atol=1e-13)
        # After controlled flipping, each source-reference Z parity is B.
        for b,x in product((0,1),BITS3):
            y=original_source(b,x)
            self.assertTrue(all(y[i]^x[i]==b for i in range(3)))
        # The two possible three-pair states encode b in orthogonal
        # subspaces. The actual old state has b weights 1/2 each, hence
        # tracing the source pairs causes fidelity=1/2, trace distance=1/2.
        state=output(active_base())
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0]);mass=norm(x)
            masses=[]
            for b in (1,-1):
                block=0.
                for s in (1,-1):
                    v=b_project((x+s*value_history(x))/2,b)
                    block+=norm(v)
                    self.assertAlmostEqual(norm(v)/mass,.25,places=12)
                    np.testing.assert_allclose(gauge_history(v),v,atol=1e-13)
                    np.testing.assert_allclose(apply64(LL,v),v,atol=1e-13)
                    np.testing.assert_allclose(apply64(G,v),v,atol=1e-13)
                    for c in C:np.testing.assert_allclose(apply64(c,v),0,atol=1e-13)
                    other=b_project((x-s*value_history(x))/2,b)
                    np.testing.assert_allclose(apply64(SWAP,v),-other,atol=1e-13)
                masses.append(block/mass)
            np.testing.assert_allclose(masses,[.5,.5],atol=1e-13)
            self.assertAlmostEqual(sum(p*p for p in masses),.5,places=12)
            self.assertAlmostEqual(np.sqrt(masses[0]*masses[1]),.5,places=12)
        # Fidelity is for the complete old post-W state including M, not for
        # a sign-selected classical mixture. The new coupling is not invisible.

    def test_exact_stationary_clock_and_zero_added_charge(self):
        p,idx,basis=permutation()
        self.assertEqual(len(set(p)),len(p))
        ids=np.arange(len(p));p14=ids.copy()
        for _ in range(CLOCKS):p14=p[p14]
        np.testing.assert_array_equal(p14,ids)
        for k,(t,b,yi,mi,n) in enumerate(basis):
            tt,bb,yy,mm,nn=basis[p[k]]
            self.assertEqual(b,bb)
            self.assertEqual(n+sum(MACHINE[mi]),nn+sum(MACHINE[mm]))
        # Old B sectors and the source/ref and bath/purifier sectors are
        # orthogonal physical states, compressed isometrically here.
        h=np.zeros((len(p),8,8),complex)
        for b,x,f in product((0,1),BITS3,BITS3):
            w=weight(b,x,f);xi=BITS3.index(x);fi=BITS3.index(f)
            for t in range(CLOCKS):
                y,m,n=path(b,x,f)[t]
                h[idx[t,b,BITS3.index(y),MACHINE.index(m),n],xi,fi]=np.sqrt(float(w)/CLOCKS)
                self.assertEqual(energy(m,n,f),0)
        self.assertAlmostEqual(norm(h),1,places=12)
        np.testing.assert_allclose(apply_perm(p,h),h,atol=1e-13)
        inv=np.argsort(p)
        np.testing.assert_allclose(2*h-apply_perm(p,h)-apply_perm(inv,h),0,atol=1e-13)
        for t in range(CLOCKS):
            self.assertAlmostEqual(sum(w for b,x,f,y,m,n,w in ensemble(t))/CLOCKS,1/CLOCKS,places=12)

    def test_uncompute_control_and_pristine_retention(self):
        # Uncompute each working bit directly using its still-available
        # source; restores both A and battery without retaining a record.
        for y in BITS3:
            a=0;n=INITIAL_N
            for bit in y:
                a,n=write(bit,a,n);a,n=write(bit,a,n)
                self.assertEqual((a,n),(0,INITIAL_N))
        # Separate q=0 blank-reservoir control: full reliable source record.
        for b,x,f,y,m,n,w in ensemble(7,F(0)):
            self.assertEqual(m[0],0);self.assertEqual(m[1:],original_source(b,x))
            self.assertEqual(energy(m,n,f),0)
        self.assertEqual(full_guess(7,F(0)),1)
        self.assertEqual(avg(7,lambda b,x,f,y,m,n:n,F(0)),F(3,2))

    def test_thermal_record_reliability_and_old_sphere_access(self):
        for b,x,f,y,m,n,w in ensemble(7):
            source=original_source(b,x)
            self.assertEqual(y,source);self.assertEqual(m[0],f[2])
            self.assertEqual(m[1:],(source[0],source[1]^f[0],source[2]^f[1]))
            self.assertEqual(energy(m,n,f),0)
        self.assertEqual([best_from_bath(7,i) for i in range(3)],[F(1),F(3,4),F(3,4)])
        self.assertEqual(full_guess(7),F(9,16))
        # R alone carries no information about old b. Access to the matched
        # source reference turns its record into a sphere-sign report.
        self.assertEqual(marginal(7,lambda b,x,f,y,m,n:(b,m[1])),
                         {(0,0):F(1,4),(0,1):F(1,4),(1,0):F(1,4),(1,1):F(1,4)})
        for i,target in enumerate((F(1),F(3,4),F(3,4))):
            correct=sum(w for b,x,f,y,m,n,w in ensemble(7) if (m[i+1]^x[i])==b)
            self.assertEqual(correct,target)
        # Inferring b this way requires joint access to R_i and source ref i.
        self.assertEqual(marginal(7,lambda b,x,f,y,m,n:m[1:]),{x:F(1,8) for x in BITS3})
        self.assertEqual(marginal(7,lambda b,x,f,y,m,n:m[0]),{0:F(3,4),1:F(1,4)})
        self.assertEqual(marginal(7,lambda b,x,f,y,m,n:n),{
            0:F(9,128),1:F(33,128),2:F(23,64),3:F(15,64),4:F(9,128),5:F(1,128)})

    def test_energy_entropy_and_landauer_identity_per_reset(self):
        self.assertEqual(avg(7,lambda b,x,f,y,m,n:n),F(2))
        self.assertEqual(avg(7,lambda b,x,f,y,m,n:m[0]),F(1,4))
        self.assertEqual(avg(7,lambda b,x,f,y,m,n:sum(m[1:])),F(3,2))
        self.assertEqual(avg(0,lambda b,x,f,y,m,n:sum(m[1:])),F(3,4))
        # In ε units: ΔE_battery=-1, ΔE_A=1/4, ΔE_R=3/4.
        self.assertEqual(avg(7,lambda b,x,f,y,m,n:energy(m,n,f)),0)
        h=-.25*log2(.25)-.75*log2(.75)
        self.assertAlmostEqual(shannon(marginal(7,lambda b,x,f,y,m,n:m[1:]).values()),3,places=12)
        self.assertAlmostEqual(shannon(marginal(7,lambda b,x,f,y,m,n:n).values()),2.118638876471338,places=12)
        self.assertAlmostEqual(shannon(marginal(0,lambda b,x,f,y,m,n:m[1:]).values()),3*h,places=12)
        joint=marginal(7,lambda b,x,f,y,m,n:(original_source(b,x),m[1:]))
        mutual=6-shannon(joint.values()) # both source and R have entropy 3
        self.assertAlmostEqual(mutual,1+2*(1-h),places=12)
        beta=log(3);qheat=.25
        delta_memory_nats=log(2)-(-.25*log(.25)-.75*log(.75))
        relative_entropy=.5*log(4/3)
        self.assertAlmostEqual(beta*qheat,delta_memory_nats+relative_entropy,places=12)

    def test_record_reliability_and_energy_at_every_clock_tick(self):
        half=F(1,2);threequarters=F(3,4)
        no=(half,half,half);one=(F(1),half,half)
        two=(F(1),threequarters,half);three=(F(1),threequarters,threequarters)
        guesses=[no,no,no,one,one,two,two,three,two,two,one,one,no,no,no]
        ns=[3,3,F(5,2),F(5,2),F(9,4),F(9,4),2,2,2,F(9,4),F(9,4),F(5,2),F(5,2),3,3]
        a=[0,0,half,F(1,4),half,F(1,4),half,F(1,4),half,F(1,4),half,F(1,4),half,0,0]
        r=[F(3,4),F(3,4),F(3,4),1,1,F(5,4),F(5,4),F(3,2),F(5,4),F(5,4),1,1,F(3,4),F(3,4),F(3,4)]
        for t in range(CLOCKS+1):
            self.assertEqual(tuple(best_from_bath(t,i) for i in range(3)),guesses[t])
            self.assertEqual(avg(t,lambda b,x,f,y,m,n:n),ns[t])
            self.assertEqual(avg(t,lambda b,x,f,y,m,n:m[0]),a[t])
            self.assertEqual(avg(t,lambda b,x,f,y,m,n:sum(m[1:])),r[t])
            self.assertEqual(avg(t,lambda b,x,f,y,m,n:energy(m,n,f)),0)
        for b,x,f in product((0,1),BITS3,BITS3):
            self.assertEqual(path(b,x,f)[14],(x,(0,)+f,INITIAL_N))
            for i in range(3):
                y,m,n=path(b,x,f)[1+2*i]
                if y[i]:self.assertNotIn((m[0],n),((0,0),(1,LEVELS-1)))

    def test_two_qubit_tape_ceiling_for_independent_three_bit_label(self):
        # 8 equiprobable source labels into dimension 4, no other side info:
        # the POVM trace bound gives 4/8. Four orthogonal encodings attain it.
        self.assertEqual(F(4,8),F(1,2))

if __name__=='__main__':unittest.main()
