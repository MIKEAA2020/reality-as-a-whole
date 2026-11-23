"""Paired memory counterflow on the selected tetrahedral zero-record state.

Physical results concern an explicitly specified finite quantum system.
Candidate subjects, actual incidence and signed phenomenal identity are hypotheses.
"""
import math
import unittest
from verification.zero_spin_constitution_test import add,close,eye,kron,mm,mv,scale,inner
from verification.zero_invariant_sphere_instrument_test import adj
from verification.zero_spherical_plenitude_opposite_records_test import vecnorm
from verification.finite_tetrahedral_zero_reference_test import recorded_whole,maxabs,comm
from verification.zero_relational_stabilizer_constitution_test import (
    H, K, Q, P, apply_base, tetra_control, embed_blank, pointwise_close,
)


def basis(i,n=16): return [complex(j==i) for j in range(n)]
def outer(a,b): return [[x*y.conjugate() for y in b] for x in a]
def sub(a,b): return add(a,scale(-1,b))
def mat_sum(*mats):
    a=scale(0,mats[0])
    for m in mats: a=add(a,m)
    return a

def diag(f): return [[complex(f(i) if i==j else 0) for j in range(16)] for i in range(16)]
def bit(i,k): return (i>>(3-k))&1
n=[diag(lambda i,k=k:bit(i,k)) for k in range(4)]
a,b=basis(6),basis(9) # |0110> and |1001> in M1,W1,M2,W2 order
proj=add(outer(a,a),outer(b,b))
g=add(outer(a,b),outer(b,a))
id16=eye(16)
swap=sub(add(id16,g),proj)
pair_swap=[[complex(i==((bit(j,2)<<3)|(bit(j,3)<<2)|(bit(j,0)<<1)|bit(j,1)))
            for j in range(16)] for i in range(16)]
J=[scale(1j,comm(g,x)) for x in n]


def apply_work(mat,v):
    out=[0j]*len(v)
    for base in range(64):
        for i,x in enumerate(mv(mat,v[16*base:16*(base+1)])): out[16*base+i]=x
    return out


def embed(v,work):
    out=[0j]*1024
    for i,x in enumerate(v): out[16*i+work]=x
    return out


def prep(v):
    # Controlled on R_A=1: exchange |0110> and |1001> only.
    out=list(v)
    for base in range(64):
        if (base>>1)&1: out[16*base+6],out[16*base+9]=v[16*base+9],v[16*base+6]
    return out


def exchange(t):
    return mat_sum(id16,scale(math.cos(t)-1,proj),scale(-1j*math.sin(t),g))


def state(t): return apply_work(exchange(t),prep(embed(recorded_whole(),6)))


def expct(v,mat): return inner(v,apply_work(mat,v)).real

def cond(v,mat,ra):
    w=[x if ((i//16>>1)&1)==ra else 0j for i,x in enumerate(v)]
    return expct(w,mat)/inner(w,w).real

def auxpen(i):
    m1,w1,m2,w2=[bit(i,k) for k in range(4)]
    return m1+(1-w1)+(1-m2)+w2


def clock_v(k,v,inverse=False):
    if k in (0,3): return list(v)
    if k==1: return prep(v)
    if inverse: return prep(apply_work(adj(exchange(math.pi/2)),v))
    return apply_work(exchange(math.pi/2),prep(v))


def clock_h(blocks):
    # K(A⊗I)K†, A adjacency of a four-cycle.
    unwound=[clock_v(k,blocks[k],True) for k in range(4)]
    return [clock_v(k,[x+y for x,y in zip(unwound[(k-1)%4],unwound[(k+1)%4])]) for k in range(4)]


def clock_solution(t):
    phi=embed(recorded_whole(),6)
    c=math.cos(t); s=math.sin(t)
    amps=(c*c,-1j*s*c,-s*s,-1j*s*c)
    return [[a*x for x in clock_v(k,phi)] for k,a in enumerate(amps)]


class ReciprocalSubjectExchangeTests(unittest.TestCase):
    def test_correlated_generator_and_unitary(self):
        close(self,g,adj(g)); close(self,mm(g,g),proj)
        close(self,mm(swap,swap),id16)
        for t in (0,.19,math.pi/4,math.pi/2,math.pi):
            u=exchange(t); close(self,mm(adj(u),u),id16)
        # exp(-i*pi/2(P−g)) gives swap on its two-state support,
        # identity elsewhere; controlled preparation is unitary and reversible.
        test=add(sub(id16,proj),g); close(self,test,swap)

    def test_all_separate_charge_identities_hold_as_operators(self):
        m1,w1,m2,w2=n
        for conserved in (add(m1,w1),add(m2,w2),add(m1,m2),add(w1,w2),mat_sum(*n)):
            self.assertLess(maxabs(comm(g,conserved)),1e-10)
            self.assertLess(maxabs(comm(swap,conserved)),1e-10)
        for j in J: close(self,j,adj(j))
        close(self,add(J[0],J[2]),scale(0,id16))
        close(self,add(J[1],J[3]),scale(0,id16))
        close(self,add(J[0],J[1]),scale(0,id16))
        close(self,add(J[2],J[3]),scale(0,id16))
        self.assertGreater(maxabs(J[0]),0)

    def test_preparation_correlates_reference_record_and_opposite_energy_origins(self):
        v=state(0)
        self.assertAlmostEqual(inner(v,v).real,1)
        for i,x in enumerate(v):
            if abs(x)>1e-10:
                self.assertEqual(i%16,6 if ((i//16>>1)&1)==0 else 9)
        pointwise_close(self,prep(prep(v)),v)
        # Coherent direction control correlates with the initial memory imbalance.
        m_diff=sub(n[0],n[2]); r=apply_base(kron(tetra_control(),eye(4)),apply_work(m_diff,v))
        pointwise_close(self,r,[-x for x in v])

    def test_conditional_currents_are_equal_opposite_in_real_time(self):
        for t in (0,.19,math.pi/8,math.pi/4,math.pi/2,3*math.pi/4,math.pi):
            v=state(t); st=math.sin(2*t)
            for r,sign in ((0,1),(1,-1)):
                self.assertAlmostEqual(cond(v,J[0],r),sign*st)
                self.assertAlmostEqual(cond(v,J[2],r),-sign*st)
                self.assertAlmostEqual(cond(v,J[1],r),-sign*st)
                self.assertAlmostEqual(cond(v,J[3],r),sign*st)
            self.assertAlmostEqual(expct(v,J[0]),0)
            zcorr=sum(x.conjugate()*y*(1-2*((i//16>>1)&1))
                      for i,(x,y) in enumerate(zip(v,apply_work(J[0],v))))
            self.assertAlmostEqual(zcorr.real,st)
            dircorr=inner(v,apply_base(kron(tetra_control(),eye(4)),apply_work(J[0],v)))
            self.assertAlmostEqual(dircorr.real,st)

    def test_endpoint_energies_and_record_correlation(self):
        v=state(math.pi/2); diff=sub(n[0],n[2])
        pointwise_close(self,apply_base(kron(tetra_control(),eye(4)),apply_work(diff,v)),v)
        for i,x in enumerate(v):
            if abs(x)>1e-10:
                self.assertEqual(i%16,9 if ((i//16>>1)&1)==0 else 6)
        for r,sign in ((0,1),(1,-1)):
            before=state(0)
            d1=cond(v,n[0],r)-cond(before,n[0],r)
            d2=cond(v,n[2],r)-cond(before,n[2],r)
            self.assertAlmostEqual(d1,sign); self.assertAlmostEqual(d2,-sign)
        # Endpoint currents vanish as expectations, not as operators.
        self.assertAlmostEqual(cond(v,J[0],0),0)
        self.assertGreater(maxabs(J[0]),0)

    def test_endpoint_change_operators_conserve_memory_and_battery_separately(self):
        u=exchange(math.pi/2)
        delta=[sub(mm(mm(adj(u),nj),u),nj) for nj in n]
        close(self,add(delta[0],delta[2]),scale(0,id16))
        close(self,add(delta[1],delta[3]),scale(0,id16))
        close(self,add(delta[0],delta[1]),scale(0,id16))
        close(self,add(delta[2],delta[3]),scale(0,id16))
        # Initial populations and endpoint changes commute; eligible initial
        # and final projective measurements are an additional protocol.
        for nj,dj in zip(n,delta): self.assertLess(maxabs(comm(nj,dj)),1e-10)

    def test_weighted_actual_incidence_is_not_fixed_by_symmetry(self):
        for r,sgn in ((0,1),(1,-1)):
            values=(sgn,-sgn)
            equal=sum(values)
            self.assertEqual(equal,0)
            eta=.3
            weights=[1+eta*x for x in values]
            self.assertTrue(all(w>0 for w in weights))
            self.assertAlmostEqual(sum(w*x for w,x in zip(weights,values)),2*eta)
            # Swapping subject labels swaps both values and weights, preserving
            # the rule; equal endpoint weights are not forced by covariance.
            self.assertEqual(weights[::-1],[1+eta*x for x in values[::-1]])

    def test_positive_covariant_history_weights_have_an_exact_residue(self):
        eta=.3; u=exchange(math.pi/2)
        d1=sub(mm(mm(adj(u),n[0]),u),n[0])
        d2=sub(mm(mm(adj(u),n[2]),u),n[2])
        close(self,d2,scale(-1,d1))
        close(self,mm(d1,d1),proj)
        w1=add(id16,scale(eta,d1)); w2=add(id16,scale(eta,d2))
        close(self,add(mm(w1,d1),mm(w2,d2)),scale(2*eta,proj))
        # All eigenvalues are 1, 1+η or 1−η, strictly positive.
        self.assertGreater(1-eta,0)
        close(self,mm(mm(pair_swap,w1),pair_swap),w2)
        close(self,mm(mm(pair_swap,d1),pair_swap),d2)
        before=state(0)
        self.assertAlmostEqual(expct(before,add(mm(w1,d1),mm(w2,d2))),2*eta)
        # The actual selected coherent state is fixed by swapping both
        # record/AB coherence (Q) and the memory–battery pairs.
        for t in (0,.4,math.pi/2):
            v=state(t)
            pointwise_close(self,apply_base(Q,apply_work(pair_swap,v)),v)

    def test_autonomous_clock_records_reciprocal_exchange(self):
        for t in (0,.23,math.pi/4,math.pi/2,math.pi):
            blocks=clock_solution(t); rhs=clock_h(blocks)
            c=math.cos(t); s=math.sin(t)
            derivatives=(-2*s*c,-1j*(c*c-s*s),-2*s*c,-1j*(c*c-s*s))
            phi=embed(recorded_whole(),6)
            for k in range(4):
                pointwise_close(self,[derivatives[k]*x for x in clock_v(k,phi)],[-1j*x for x in rhs[k]])
            self.assertAlmostEqual(sum(inner(b,b).real for b in blocks),1)
        blocks=clock_solution(math.pi/2)
        self.assertAlmostEqual(inner(blocks[2],blocks[2]).real,1)
        # At clock 2 the work is the same final state up to global phase.
        pointwise_close(self,blocks[2],[-x for x in state(math.pi/2)])
        blocks=clock_solution(math.pi)
        self.assertAlmostEqual(inner(blocks[0],blocks[0]).real,1)

    def test_coherence_moves_into_joint_work_record_operator(self):
        # U=exchange(t) prep: transported Q remains sharp on the whole.
        t=.37; v=state(t); u=exchange(t)
        undo=prep(apply_work(adj(u),v))
        pointwise_close(self,undo,embed(recorded_whole(),6))
        transformed=apply_work(u,prep(apply_base(Q,undo)))
        pointwise_close(self,transformed,v)
        # Bare Q is not the correct post-preparation observable.
        self.assertAlmostEqual(inner(v,apply_base(Q,v)).real,0)

    def test_joint_selector_retains_unique_gapped_ground_and_charges(self):
        # H_aux is a sum of four 0/1 penalties with unique ground |0110>.
        self.assertEqual([i for i in range(16) if auxpen(i)==0],[6])
        self.assertEqual(min(auxpen(i) for i in range(16) if i!=6),1)
        # Prior H has unique zero ground and gap 1. Conjugation by the
        # charge-commuting preparation and exchange preserves both features.
        self.assertAlmostEqual(vecnorm(mv(H,recorded_whole())),0)
        for t in (0,.7,math.pi/2):
            v=state(t); u=exchange(t)
            undo=prep(apply_work(adj(u),v))
            hy=apply_base(H,undo)
            hy=[z+auxpen(i%16)*undo[i] for i,z in enumerate(hy)]
            self.assertAlmostEqual(vecnorm(hy),0)
            out=apply_work(u,prep(hy))
            self.assertAlmostEqual(vecnorm(out),0)
        # Covariance and conserved-charge commutators follow because both
        # unitaries act only on scalar records and commute with charges.

if __name__=='__main__': unittest.main()
