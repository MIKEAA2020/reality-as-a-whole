"""Uniform relational sphere, logical singlet and opposite encoded records.

A continuous direction reference and logical SU(2) are assumed; model checks do
not establish actual subjects, experiential valence, or metaphysical plenitude.
"""
import math
import unittest
from verification.zero_spin_constitution_test import X,Y,Z,add,close,eye,kron,mm,mv,scale,inner
from verification.zero_invariant_sphere_instrument_test import adj


def tensor(*ops):
    m=[[1]]
    for x in ops: m=kron(m,x)
    return m

def op(o,k):
    return tensor(*[o if i==k else eye(2) for i in range(4)])
def sub(a,b): return add(a,scale(-1,b))
def comm(a,b): return sub(mm(a,b),mm(b,a))
def vecnorm(v): return math.sqrt(max(0,inner(v,v).real))
def maxabs(a): return max(abs(x) for row in a for x in row)

def projector(n,sign):
    return scale(.5,add(eye(2),scale(sign,add(add(scale(n[0],X),scale(n[1],Y)),scale(n[2],Z)))))

def record_unitary(n,system,pointer):
    plus=op(projector(n,1),system)
    minus=op(projector(n,-1),system)
    return add(plus,mm(minus,op(X,pointer)))

def initial():
    # Logical A, B, RA, RB; each can be a physical four-spin singlet block.
    v=[0j]*16; v[4]=1/math.sqrt(2); v[8]=-1/math.sqrt(2)
    return v

def recorded(n):
    ua=record_unitary(n,0,2); ub=record_unitary(n,1,3)
    return mv(ub,mv(ua,initial()))

def probability(v,predicate):
    return sum(abs(amp)**2 for i,amp in enumerate(v) if predicate(tuple((i>>j)&1 for j in (3,2,1,0))))

def bloch(n): return projector(n,1)

def mat_average(states,weights):
    out=[[0j]*2 for _ in range(2)]
    for s,w in zip(states,weights): out=add(out,scale(w,s))
    return out

TETRA=[tuple(x/math.sqrt(3) for x in v)
       for v in ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))]
TRINE=[(1,0,0),(-.5,math.sqrt(3)/2,0),(-.5,-math.sqrt(3)/2,0)]
PAIR=[(0,0,1),(0,0,-1)]

class SphericalPlenitudeOppositeRecordsTests(unittest.TestCase):
    def test_opposite_records_hold_for_all_tested_directions(self):
        axes=PAIR+TETRA+TRINE+[(1/math.sqrt(2),0,1/math.sqrt(2))]
        total=add(op(Z,2),op(Z,3))
        for n in axes:
            v=recorded(n)
            self.assertAlmostEqual(vecnorm(v),1)
            self.assertAlmostEqual(vecnorm(mv(total,v)),0)
            self.assertAlmostEqual(probability(v,lambda b:b[2:]==(0,1)),.5)
            self.assertAlmostEqual(probability(v,lambda b:b[2:]==(1,0)),.5)
            self.assertAlmostEqual(probability(v,lambda b:b[2]==b[3]),0)

    def test_each_measurement_is_unitary_and_both_operations_commute(self):
        for n in TETRA+PAIR:
            a=record_unitary(n,0,2); b=record_unitary(n,1,3)
            close(self,mm(adj(a),a),eye(16))
            close(self,mm(adj(b),b),eye(16))
            self.assertLess(maxabs(comm(a,b)),1e-10)

    def test_autonomous_direction_controlled_record_hamiltonian(self):
        for n in PAIR+TETRA:
            hs=[]
            for system,pointer in ((0,2),(1,3)):
                h=mm(op(projector(n,-1),system),sub(eye(16),op(X,pointer)))
                close(self,mm(h,h),scale(2,h))
                # exp(-i*pi*H/2)=I-H since H has eigenvalues 0 and 2.
                close(self,sub(eye(16),h),record_unitary(n,system,pointer))
                hs.append(h)
            self.assertLess(maxabs(comm(hs[0],hs[1])),1e-10)
        # Direct-integral H(n) yields a single bounded autonomous H when a
        # continuous internal reference with measure dΩ/4π is assumed.

    def test_spin_zero_is_preserved_by_encoded_construction(self):
        # Prior zero-spin tests construct the four-dimensional physical-spin
        # encoding; logical Pauli operators act within its singlet sector.
        from verification.zero_invariant_sphere_instrument_test import logical_basis
        from verification.zero_spin_constitution_test import total_spin
        for v in logical_basis():
            for s in (X,Y,Z): self.assertAlmostEqual(vecnorm(mv(total_spin(s,4),v)),0)
        # Consequently the four encoded factors and their logical controlled
        # gates remain in physical spin zero. Reference spin is an assumption.

    def test_unequal_settings_show_marginal_no_signalling(self):
        # The invariant global reference n is common for matched settings,
        # but B's ± marginal stays 1/2 even if A uses a different setting.
        for n in TETRA:
            for m in TRINE:
                v=mv(record_unitary(m,1,3),mv(record_unitary(n,0,2),initial()))
                self.assertAlmostEqual(probability(v,lambda bits:bits[3]==0),.5)
                self.assertAlmostEqual(probability(v,lambda bits:bits[3]==1),.5)

    def test_local_direction_rotation_covariance(self):
        # 90° about z maps X→Y and Y→−X by R O R†.
        r=[[complex(math.cos(math.pi/4),-math.sin(math.pi/4)),0],
           [0,complex(math.cos(math.pi/4),math.sin(math.pi/4))]]
        for n in TETRA+TRINE:
            rotated=(-n[1],n[0],n[2])
            close(self,mm(mm(r,projector(n,1)),adj(r)),projector(rotated,1))
            ra=op(r,0)
            close(self,mm(mm(ra,record_unitary(n,0,2)),adj(ra)),record_unitary(rotated,0,2))

    def test_global_direction_controlled_state_is_covariant(self):
        r=[[complex(math.cos(math.pi/4),-math.sin(math.pi/4)),0],
           [0,complex(math.cos(math.pi/4),math.sin(math.pi/4))]]
        both=tensor(r,r,eye(2),eye(2))
        for n in TETRA+TRINE:
            rotated=(-n[1],n[0],n[2])
            a=mv(both,recorded(n)); b=recorded(rotated)
            self.assertAlmostEqual(vecnorm([x-y for x,y in zip(a,b)]),0)

    def test_all_spherical_directions_have_zero_first_moment_but_not_zero_each(self):
        # SO(3) invariance gives ∫n_i=0 and ∫n_i n_j=δij/3.
        # A tetrahedron is an exact quadrature for these first two moments.
        for i in range(3):
            self.assertAlmostEqual(sum(n[i] for n in TETRA)/4,0)
            for j in range(3):
                self.assertAlmostEqual(sum(n[i]*n[j] for n in TETRA)/4,(i==j)/3)
        self.assertNotEqual(TETRA[0][2],0)

    def test_pair_and_trine_reproduce_only_the_first_moment(self):
        for dirs in (PAIR,TRINE):
            for i in range(3): self.assertAlmostEqual(sum(n[i] for n in dirs)/len(dirs),0)
            close(self,mat_average([bloch(n) for n in dirs],[1/len(dirs)]*len(dirs)),scale(.5,eye(2)))
        self.assertAlmostEqual(sum(n[2]**2 for n in PAIR)/2,1)
        self.assertAlmostEqual(sum(n[2]**2 for n in TRINE)/3,0)
        self.assertAlmostEqual(sum(n[2]**2 for n in TETRA)/4,1/3)

    def test_uniform_covariant_effect_normalization_and_state_dependence(self):
        # F(n)dμ=(I+nσ)dμ; tetrahedral quadrature integrates this exactly.
        effects=[scale(.25,scale(2,bloch(n))) for n in TETRA]
        summed=[[0j]*2 for _ in range(2)]
        for e in effects: summed=add(summed,e)
        close(self,summed,eye(2))
        state=bloch(TETRA[0])
        p=[sum(mm(state,e)[i][i].real for i in range(2)) for e in effects]
        self.assertAlmostEqual(p[0],.5)
        for value in p[1:]: self.assertAlmostEqual(value,1/6)
        # Unlike the singlet marginal, a pure logical state gives a biased n distribution.

    def test_conditional_mean_as_accessible_quality_would_signal(self):
        # Both decompositions yield I/2; conditional z-means have different
        # distributions and even different second moments.
        for dirs in (PAIR,TETRA):
            close(self,mat_average([bloch(tuple(-x for x in n)) for n in dirs],
                                   [1/len(dirs)]*len(dirs)),scale(.5,eye(2)))
        pair_second=sum(n[2]**2 for n in PAIR)/2
        tetra_second=sum(n[2]**2 for n in TETRA)/4
        self.assertAlmostEqual(pair_second,1)
        self.assertAlmostEqual(tetra_second,1/3)
        self.assertNotAlmostEqual(pair_second,tetra_second)
        # A fixed accessible value equaling each conditional mean would reveal
        # context; local ±1 record marginals tested above remain identical.

    def test_antipodal_relabel_swaps_plus_and_minus_not_felt_quality(self):
        for n in TETRA:
            close(self,projector(n,1),projector(tuple(-x for x in n),-1))
            close(self,projector(n,-1),projector(tuple(-x for x in n),1))
        # The physics does not by itself assign either label to pleasure.

if __name__=='__main__': unittest.main()
