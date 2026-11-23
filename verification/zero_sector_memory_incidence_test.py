"""Zero-spin pointer/memory model and conditional record-incidence accounting.

Records and signs are physical/model labels, not demonstrated subjects or valence.
"""
from collections import defaultdict
from fractions import Fraction as F
import math
import unittest
from verification.zero_spin_constitution_test import X, Y, Z, add, eye, mm, rank, scale
from verification.zero_invariant_sphere_instrument_test import instrument_unitary
from verification.zero_sphere_conservation_born_bridge_test import bridge, ray

Q=(F(1,8),F(2,5),F(19,40))
S=(F(-1,5),F(1,2),F(-7,19))
N=((1,0,0),(.5,math.sqrt(3)/2,0),(-13/19,-8*math.sqrt(3)/19,0))


def ks():
    out=[]
    for q,(x,y,z) in zip(Q,N):
        # K_i= sqrt(2q_i) Π_i
        out.append(scale(math.sqrt(2*float(q))/2,
                         add(eye(2),add(add(scale(x,X),scale(y,Y)),scale(z,Z)))))
    return out


def instrument():
    u=instrument_unitary(ks())
    # State key order (logical A, logical B, pointer, memory 1, memory 2).
    out=defaultdict(complex)
    for a,b,amp in ((0,1,1/math.sqrt(2)),(1,0,-1/math.sqrt(2))):
        for ap in range(2):
            for r in range(5): out[(ap,b,r,0,0)]+=amp*u[5*ap+r][5*a]
    return {k:v for k,v in out.items() if abs(v)>1e-13}


def copy_all(state, inverse=False):
    out=defaultdict(complex)
    for (a,b,r,m,n),v in state.items():
        out[(a,b,r,(m+(-r if inverse else r))%5,n)]+=v
    return dict(out)


def copy_flag(state, inverse=False):
    out=defaultdict(complex)
    for (a,b,r,m,n),v in state.items():
        shift=int(r==1)*(-1 if inverse else 1)
        out[(a,b,r,m,(n+shift)%5)]+=v
    return dict(out)


def marginal(state, axes):
    by_env=defaultdict(list)
    rest=[i for i in range(5) if i not in axes]
    for key,v in state.items():
        by_env[tuple(key[i] for i in rest)].append((tuple(key[i] for i in axes),v))
    rho=defaultdict(complex)
    for terms in by_env.values():
        for a,x in terms:
            for b,y in terms: rho[(a,b)]+=x*y.conjugate()
    return dict(rho)


def close_dict(test,a,b):
    for key in set(a)|set(b): test.assertAlmostEqual(abs(a.get(key,0)-b.get(key,0)),0)


def norm2(state): return sum(abs(v)**2 for v in state.values())

class ZeroSectorMemoryTests(unittest.TestCase):
    def setUp(self):
        self.measured=instrument()
        self.one=copy_all(self.measured)
        self.two=copy_flag(self.one)

    def test_weights_and_directions_really_come_from_prior_five_ray_example(self):
        rays=[ray(0),ray(1),ray(3),ray(0,1),ray(0,2)]
        result,q,dots=bridge(rays)
        self.assertEqual(tuple(q[i] for i in result['triple']),Q)
        self.assertEqual(tuple(dots[result['pair'][0]][i] for i in result['triple']),S)
        self.assertEqual(sum(q*s for q,s in zip(Q,S)),0)

    def test_measurement_and_two_copy_steps_preserve_norm(self):
        for state in (self.measured,self.one,self.two): self.assertAlmostEqual(norm2(state),1)
        for state in (self.measured,self.one,self.two):
            p=[sum(abs(v)**2 for k,v in state.items() if k[2]==i) for i in range(3)]
            for actual,expected in zip(p,Q): self.assertAlmostEqual(actual,float(expected))
        # Both controlled shifts are permutations of 5x5 logical record states;
        # all factors are in independently zero-spin encoded sectors.
        for control in range(5):
            self.assertEqual(len({(m+control)%5 for m in range(5)}),5)
            self.assertEqual(len({(m+int(control==1))%5 for m in range(5)}),5)

    def test_universal_copy_is_a_perfect_repeatable_record(self):
        self.assertTrue(all(k[2]==k[3] for k,v in self.one.items() if abs(v)>1e-12))
        for i in range(3):
            prob=sum(abs(v)**2 for k,v in self.one.items() if k[2]==i and k[3]==i)
            self.assertAlmostEqual(prob,float(Q[i]))
        # Rereading both sharp pointer/memory observables yields the same label.

    def test_copying_first_memory_decoheres_pointer_locally(self):
        before=marginal(self.measured,(2,)); after=marginal(self.one,(2,))
        self.assertGreater(abs(before.get(((0,),(1,)),0)),1e-4)
        for i in range(3):
            for j in range(3):
                if i!=j: self.assertAlmostEqual(abs(after.get(((i,),(j,)),0)),0)
                else: self.assertAlmostEqual(after.get(((i,),(i,)),0).real,float(Q[i]))

    def test_selective_copy_leaves_individual_records_but_changes_joint_state(self):
        close_dict(self,marginal(self.one,(2,)),marginal(self.two,(2,)))
        close_dict(self,marginal(self.one,(3,)),marginal(self.two,(3,)))
        old=marginal(self.one,(2,3)); new=marginal(self.two,(2,3))
        self.assertGreater(abs(old.get(((0,0),(1,1)),0)),1e-4)
        self.assertAlmostEqual(abs(new.get(((0,0),(1,1)),0)),0)
        self.assertAlmostEqual(sum(abs(v)**2 for k,v in self.two.items() if k[4]==1),float(Q[1]))

    def test_redundancy_is_reversible_not_irreversible_experience(self):
        close_dict(self,copy_all(copy_flag(self.two,inverse=True),inverse=True),self.measured)

    def test_storage_hamiltonian_has_mismatch_gap_but_not_logical_protection(self):
        # H/Δ is 0 on equal pointer/memory labels and 1 on mismatches.
        h=[[complex(i==j and i//5!=i%5) for j in range(25)] for i in range(25)]
        self.assertEqual(mm(h,h),h)
        self.assertEqual(rank(h),20)
        self.assertTrue(all(h[5*i+i][5*i+i]==0 for i in range(5)))
        # Simultaneously swapping 0 and 1 in both registers changes the stored
        # label while preserving H: a gap for mismatch is not a full memory.
        permutation=[1,0,2,3,4]
        both=[[complex((i//5)==permutation[j//5] and (i%5)==permutation[j%5])
               for j in range(25)] for i in range(25)]
        self.assertEqual(mm(h,both),mm(both,h))
        self.assertEqual(both[6][0],1)

    def test_opposite_record_observables_cancel_in_each_branch(self):
        # Define V_R=s(R), V_M=-s(M); correlated sharp record labels have
        # opposite nonzero eigenvalues and their sum annihilates the state.
        for key,amp in self.two.items():
            if abs(amp)>1e-12:
                self.assertEqual(S[key[2]]-S[key[3]],0)
                self.assertNotEqual(S[key[2]],0)
        # A common identical local rule instead gives twice the same sign.
        same_rule_norm=sum(abs(amp)**2 * float(2*S[key[2]])**2
                           for key,amp in self.two.items())
        self.assertGreater(same_rule_norm,0)

    def test_copy_operation_supplies_a_directional_causal_role(self):
        # Intervene on computational input labels with the other input fixed.
        # r is invariant while m changes by r modulo five, not conversely.
        out=lambda r,m:(r,(r+m)%5)
        self.assertNotEqual(out(0,0)[1],out(1,0)[1])
        self.assertEqual(out(2,0)[0],out(2,1)[0])
        for r in range(5):
            for m in range(5): self.assertEqual(out(r,m)[0],r)

    def test_exchange_symmetry_forbids_opposite_signs_from_identical_local_rule(self):
        swapped={(a,b,m,r,n):v for (a,b,r,m,n),v in self.two.items()}
        close_dict(self,swapped,self.two)
        close_dict(self,marginal(self.two,(2,)),marginal(self.two,(3,)))
        # A common functional of identical local states assigns the same
        # number; the separate +s and -s operators require a role distinction.
        for i in range(3): self.assertNotEqual(S[i],-S[i])

    def test_record_multiplicity_can_break_conservation_weighted_balance(self):
        # Pointer plus the complete first copy: m=2 for every branch. The
        # second register is *stipulated* to count as an extra occurrence
        # only when its flag is activated. Nothing says it is a subject.
        m=(2,3,2)
        self.assertEqual(sum(q*s for q,s in zip(Q,S)),0)
        self.assertEqual(sum(q*mi*s for q,mi,s in zip(Q,m,S)),F(1,5))
        self.assertEqual(sum(q*mi for q,mi in zip(Q,m)),F(12,5))
        self.assertEqual(sum(q*mi*s for q,mi,s in zip(Q,m,S))/sum(q*mi for q,mi in zip(Q,m)),F(1,12))
        self.assertEqual([2+int(i==1) for i in range(3)],list(m))

    def test_single_axis_and_all_axis_balance_are_distinct(self):
        # Exact single-axis condition is -m0+8m1-7m2=0.
        for m in ((1,1,1),(9,2,1),(2,3,2),(5,2,3)):
            balance=sum(q*mi*s for q,mi,s in zip(Q,m,S))
            self.assertEqual(40*balance,-m[0]+8*m[1]-7*m[2])
        # n0 and n1 are nonparallel, and q0*n0+q1*n1+q2*n2=0:
        # a vector balance for m requires m0=m1=m2, unlike one-axis balance.
        self.assertNotAlmostEqual(N[0][0]*N[1][1]-N[0][1]*N[1][0],0)
        for j in range(3): self.assertAlmostEqual(sum(float(q)*n[j] for q,n in zip(Q,N)),0)
        m=(9,2,1)
        self.assertEqual(sum(q*mi*s for q,mi,s in zip(Q,m,S)),0)
        self.assertGreater(sum(abs(sum(float(q)*mi*n[j] for q,mi,n in zip(Q,m,N))) for j in range(3)),.1)

    def test_same_born_frequencies_do_not_determine_record_order(self):
        first=[0]*5+[1]*16+[2]*19
        second=list(reversed(first))
        self.assertNotEqual(first,second)
        for word in (first,second):
            self.assertEqual(tuple(F(word.count(i),len(word)) for i in range(3)),Q)
        # Example of non-uniqueness of formal sequences, not a mechanism or
        # an assertion that both are genuinely possible complete realities.

    def test_opposite_sign_interpretations_have_same_physical_statistics(self):
        rho=marginal(self.two,(2,))
        weights=[rho.get(((i,),(i,)),0).real for i in range(3)]
        for p,q in zip(weights,Q): self.assertAlmostEqual(p,float(q))
        positive=dict(zip(range(3),S)); negative={i:-v for i,v in positive.items()}
        self.assertNotEqual(positive,negative)
        # This checks underdetermination by the specified physical statistics,
        # not that either assignment is a real experiential identity.
        self.assertEqual(sum(q*positive[i] for i,q in enumerate(Q)),0)
        self.assertEqual(sum(q*negative[i] for i,q in enumerate(Q)),0)

if __name__=='__main__': unittest.main()
