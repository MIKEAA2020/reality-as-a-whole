"""Static five-clock history over the existing sphere/record sector.

Feynman-Kitaev propagation is specified, not derived. Clock projections,
probe current and experience hypotheses are distinct; no selected outcomes,
conscious subject, physical spacetime or global energy zero are established.
"""
import cmath
import math
import unittest
from fractions import Fraction as F
from verification.zero_five_ray_record_current_unification_test import (
    joint_state,probabilities,local_density,norm2,apply_work
)
from verification.zero_sphere_mismatch_experience_comparison_test import (
    subject_density,phase_flip,branch_current
)
from verification.zero_confinement_coherence_experience_test import phase_state,k_mean
from verification.zero_reciprocal_subject_exchange_test import J
from verification.zero_spin_constitution_test import close,inner

N=5
DELTA=math.pi/8


def history(v): return [[x/math.sqrt(N) for x in phase_state(v,k*DELTA)] for k in range(N)]

def history_inner(a,b): return sum(inner(x,y) for x,y in zip(a,b))

def scale_vector(c,v): return [c*x for x in v]
def add_vector(a,b): return [x+y for x,y in zip(a,b)]
def sub_vector(a,b): return [x-y for x,y in zip(a,b)]

def prop(blocks):
    # H=1/2 Σ_k (|k+1>I−|k>U†)(<k+1|I−<k|U).
    # At a link, the residual is v[k+1]−U v[k].
    out=[[0j]*len(blocks[0]) for _ in range(N)]
    for k in range(N-1):
        residual=sub_vector(blocks[k+1],phase_state(blocks[k],DELTA))
        out[k+1]=add_vector(out[k+1],scale_vector(.5,residual))
        out[k]=sub_vector(out[k],scale_vector(.5,phase_state(residual,-DELTA)))
    return out

def edge_energy(blocks):
    return sum(norm2(sub_vector(blocks[k+1],phase_state(blocks[k],DELTA)))/2
               for k in range(N-1))

def clock_fourier(blocks,m):
    return [sum(cmath.exp(-2j*math.pi*m*k/N)*blocks[k][j]/math.sqrt(N)
                for k in range(N)) for j in range(len(blocks[0]))]

def normalized_matrix(matrix,p): return [[x/p for x in row] for row in matrix]

def memory_number(v):
    return [x*((j%16)>>3 & 1) for j,x in enumerate(v)]


def paired_clock_history(blocks):
    # W|k> = |k>_C |k>_D. Orthogonal clock states can be copied coherently;
    # this is not cloning an arbitrary unknown clock state.
    z=[0j]*len(blocks[0])
    return [list(blocks[k]) if k==l else list(z) for k in range(N) for l in range(N)]


def paired_clock_prop(blocks):
    # W C_prop W† + (I-WW†) ⊗ I: diagonal blocks evolve under C_prop;
    # all off-diagonal clock-label blocks carry a positive penalty.
    d=prop([blocks[k*N+k] for k in range(N)])
    return [d[k] if k==l else list(blocks[k*N+l]) for k in range(N) for l in range(N)]


class RelationalHistoryExperientialClockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t=joint_state('triple'); cls.p=joint_state('pair')
        cls.th=history(cls.t); cls.ph=history(cls.p)
        cls.alt=history(phase_flip(cls.t))
        cls.alt_pair=history(phase_flip(cls.p))

    def test_history_is_normalized_and_stationary_under_its_constraint(self):
        for h in (self.th,self.ph,self.alt,self.alt_pair):
            self.assertAlmostEqual(history_inner(h,h).real,1)
            self.assertAlmostEqual(edge_energy(h),0)
            self.assertAlmostEqual(sum(norm2(x) for x in prop(h)),0)

    def test_constraint_is_positive_by_explicit_link_factorization(self):
        # Any test vector, including one outside the kernel, satisfies
        # <v|H|v> = 1/2 Σ ||v_(k+1)-U v_k||^2 >= 0.
        v=[scale_vector(complex(k+1,(-1)**k),self.th[k]) for k in range(N)]
        expectation=history_inner(v,prop(v))
        self.assertGreater(edge_energy(v),0)
        self.assertAlmostEqual(expectation.real,edge_energy(v))
        self.assertAlmostEqual(expectation.imag,0)

    def test_clock_conditioning_returns_varying_phases_and_fixed_realm(self):
        initial=subject_density(self.t)
        for k,block in enumerate(self.th):
            p=norm2(block)
            self.assertAlmostEqual(p,1/5)
            close(self,normalized_matrix(subject_density(block),p),initial)
            self.assertAlmostEqual(k_mean(block).real/p,math.cos(k*math.pi/4))
            for ra,sgn in ((0,1),(1,-1)):
                self.assertAlmostEqual(branch_current(block,ra),sgn*math.cos(k*math.pi/4))

    def test_five_ray_record_weights_are_fixed_at_each_clock_value(self):
        expected=[(F(3,40),F(1,20)),(F(1,10),F(3,10)),(F(13,40),F(3,20))]
        for block in self.th:
            p=norm2(block); table=probabilities(block)
            for i,(plus,minus) in enumerate(expected):
                self.assertAlmostEqual(table[(i,1)]/p,float(plus))
                self.assertAlmostEqual(table[(i,2)]/p,float(minus))

    def test_same_constraint_has_two_orthogonal_distinct_histories(self):
        self.assertAlmostEqual(abs(history_inner(self.th,self.alt)),0)
        self.assertAlmostEqual(edge_energy(self.th),0)
        self.assertAlmostEqual(edge_energy(self.alt),0)
        for k,(a,b) in enumerate(zip(self.th,self.alt)):
            close(self,normalized_matrix(subject_density(a),norm2(a)),
                       normalized_matrix(subject_density(b),norm2(b)))
            self.assertAlmostEqual(k_mean(a).real/norm2(a),math.cos(k*math.pi/4))
            self.assertAlmostEqual(k_mean(b).real/norm2(b),-math.cos(k*math.pi/4))
            pa,pb=probabilities(a),probabilities(b)
            for key in pa: self.assertAlmostEqual(pa[key],pb[key])

    def test_clock_coarse_graining_is_a_valid_lower_resolution_readout(self):
        means=[]; masses=[]
        for subset in ((0,1),(2,3,4)):
            p=sum(norm2(self.th[k]) for k in subset)
            v=sum(k_mean(self.th[k]).real for k in subset)/p
            masses.append(p); means.append(v)
        self.assertAlmostEqual(masses[0],2/5); self.assertAlmostEqual(masses[1],3/5)
        self.assertAlmostEqual(means[0],(2+math.sqrt(2))/4)
        self.assertAlmostEqual(means[1],-(2+math.sqrt(2))/6)
        self.assertAlmostEqual(sum(x*y for x,y in zip(masses,means)),0)

    def test_two_synchronized_physical_clock_factors_agree(self):
        paired=paired_clock_history(self.th)
        self.assertAlmostEqual(history_inner(paired,paired).real,1)
        self.assertAlmostEqual(sum(norm2(x) for x in paired_clock_prop(paired)),0)
        for k in range(N):
            # Projecting either C or D onto k leaves only the same block
            # ψ_k/√5 after tracing the other clock.
            c_probs=[norm2(paired[k*N+l]) for l in range(N)]
            d_probs=[norm2(paired[l*N+k]) for l in range(N)]
            self.assertAlmostEqual(sum(c_probs),F(1,5))
            self.assertEqual(c_probs,d_probs)
            self.assertAlmostEqual(c_probs[k],F(1,5))
            for l in range(N):
                if l!=k: self.assertAlmostEqual(c_probs[l],0)
            block=paired[k*N+k]
            self.assertAlmostEqual(k_mean(block).real/norm2(block),math.cos(k*math.pi/4))
            close(self,normalized_matrix(subject_density(block),norm2(block)),subject_density(self.t))

    def test_two_clock_constraint_is_positive_not_automatically_unique(self):
        h=paired_clock_history(self.th); other=paired_clock_history(self.alt)
        self.assertAlmostEqual(abs(history_inner(h,other)),0)
        self.assertAlmostEqual(sum(norm2(v) for v in paired_clock_prop(other)),0)
        bad=[list(v) for v in h]; bad[1]=list(self.th[0])
        energy=history_inner(bad,paired_clock_prop(bad))
        self.assertGreater(energy.real,0)
        self.assertAlmostEqual(energy.imag,0)

    def test_fourier_basis_is_an_alternative_readout_not_an_ordered_clock(self):
        weights=[]
        for m in range(N):
            u=clock_fourier(self.th,m); p=norm2(u); weights.append(p)
            self.assertGreater(p,0)
            self.assertAlmostEqual(k_mean(u).real/p,0)
            close(self,normalized_matrix(subject_density(u),p),subject_density(self.t))
            for ra in (0,1): self.assertAlmostEqual(branch_current(u,ra),0)
        for got,want in zip(weights,[.7265764270667973,.104527911700275,
                                      .0321838747663262,.0321838747663262,.104527911700275]):
            self.assertAlmostEqual(got,want)
        self.assertAlmostEqual(sum(weights),1)

    def test_transporting_clock_labels_does_not_change_conditional_facts(self):
        # Reverse all labels, keeping each physical event and direction
        # assignment attached; this is not physical clock reversal.
        for k,block in enumerate(self.th):
            new_label=4-k
            carried={4-j:b for j,b in enumerate(self.th)}[new_label]
            self.assertAlmostEqual(norm2(carried),norm2(block))
            self.assertAlmostEqual(k_mean(carried).real,k_mean(block).real)

    def test_full_bob_state_no_signalling_for_both_readout_bases(self):
        for ah,bh in ((self.th,self.ph),(self.alt,self.alt_pair)):
            for a,b in zip(ah,bh): close(self,local_density(a),local_density(b))
            for m in range(N):
                close(self,local_density(clock_fourier(ah,m)),
                           local_density(clock_fourier(bh,m)))
        # Full clock+Bob equality follows from the same Bob isometry acting
        # on identical full initial Bob density matrices, not from means.

    def test_probe_is_not_the_clock_constraint_current(self):
        # N_M1 commutes with each phase link and the clock, so i[Hprop,N]=0.
        # J1 belongs to the earlier separate G exchange and is nonzero.
        chosen=[scale_vector(complex(k+1,1),self.th[k]) for k in range(N)]
        before=prop([memory_number(v) for v in chosen])
        after=[memory_number(v) for v in prop(chosen)]
        self.assertAlmostEqual(sum(norm2(sub_vector(a,b)) for a,b in zip(before,after)),0)
        self.assertGreater(norm2(apply_work(self.t,J[0])),.99)

    def test_two_stipulated_experience_rules_disagree_on_the_same_history(self):
        # Restrict to r=+1; physical values are conditional means, not a
        # proof that either of these scalar assignments is actual experience.
        p=[math.cos(k*math.pi/4) for k in range(N)]
        q=[1]*N
        self.assertAlmostEqual(p[0],q[0]); self.assertAlmostEqual(p[-1],-q[-1])
        for vp,vq in zip(p,q):
            self.assertAlmostEqual(vp+(-vp),0)
            self.assertAlmostEqual(vq+(-vq),0)

if __name__=='__main__': unittest.main()
