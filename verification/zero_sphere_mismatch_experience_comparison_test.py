"""Common-domain sphere-record/mismatch/subject candidate comparison.

Logical physics and stipulated formal quality assignments only; no actual
subjects, felt valence, empirical biomarkers or objective whole zero inferred.
"""
from fractions import Fraction as F
from itertools import combinations,permutations,product
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parent))
from competing_subject_constitution_rules import overlapping_local_maxima,connected_components
from verification.zero_spin_constitution_test import X,Y,Z,add,eye,kron,mm,scale,inner,close
from verification.finite_tetrahedral_zero_reference_test import maxabs,comm
from verification.zero_reciprocal_subject_exchange_test import J
from verification.zero_five_ray_record_current_unification_test import joint_state,probabilities,index,apply_work,norm2


def sub(a,b): return add(a,scale(-1,b))
def tensor(*ops):
    m=[[1]]
    for op in ops: m=kron(m,op)
    return m

def op(mat,j): return tensor(*[mat if k==j else eye(2) for k in range(4)])
def trace(a): return sum(a[i][i] for i in range(len(a)))
def paired(a,b): return mm(op(a[0],a[1]),op(b[0],b[1]))
def coeff(a,b): return (trace(mm(a,b))/16).real

# Order: H1,R1,R2,H2. H1 and H2 are +Z preparation references.
weights={(i,j):F(0) for i,j in combinations(range(4),2)}
weights.update({(0,1):F(1,2),(1,2):F(1,4),(2,3):F(1,2)})
H=scale(0,eye(16))
for (i,j),w in weights.items(): H=add(H,scale(-float(w)/2,paired((Z,i),(Z,j))))
q1=scale(.5,sub(eye(16),paired((Z,0),(Z,1))))
q2=scale(.5,sub(eye(16),paired((Z,2),(Z,3))))


def q_from_record(record): return ((record>>1)&1,record&1)
def phase_flip(v): return [x*(1-2*((i%16)>>3)) for i,x in enumerate(v)]


def subject_density(v):
    # 4 logical bits H1,R1,R2,H2; references are fixed to |0>.
    # Trace Alice, Bob signal, Alice pointer and four work qubits.
    rho=[[0j]*16 for _ in range(16)]
    for a in range(2):
        for b in range(2):
            for i in range(5):
                for w in range(16):
                    u=[0j]*16
                    for r in range(4): u[r<<1]=v[index(a,b,i,r,w)]
                    for j in range(16):
                        for k in range(16): rho[j][k]+=u[j]*u[k].conjugate()
    return rho


def branch_current(v,ra):
    jv=apply_work(v,J[0])
    idx=[index(a,b,i,r,w) for a in range(2) for b in range(2) for i in range(5)
         for r in (1,2) if ((r>>1)&1)==ra for w in range(16)]
    mass=sum(abs(v[k])**2 for k in idx)
    return sum(v[k].conjugate()*jv[k] for k in idx).real/mass


class SphereMismatchExperienceComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v=joint_state('triple'); cls.after=phase_flip(cls.v)

    def test_subject_graph_extracted_from_actual_hamiltonian_commutators(self):
        # i[H,X_j] contains exactly w_ij Z_i Y_j for each j-neighbor.
        for i,j in product(range(4),repeat=2):
            if i==j: continue
            response=scale(1j,comm(H,op(X,j)))
            extracted=coeff(response,paired((Z,i),(Y,j)))
            self.assertAlmostEqual(extracted,float(weights[tuple(sorted((i,j)))]))
        selected,ties=overlapping_local_maxima(frozenset(range(4)),weights)
        self.assertEqual(selected,frozenset((frozenset((0,1)),frozenset((2,3)))))
        self.assertFalse(ties)
        self.assertEqual(connected_components(frozenset(range(4)),weights),frozenset((frozenset(range(4)),)))
        # Cut diagnostics are assumptions about subjects; this is not IIT.

    def test_selector_and_mismatch_relabel_together(self):
        subjects,_=overlapping_local_maxima(frozenset(range(4)),weights)
        for perm in permutations(range(4)):
            edges={tuple(sorted((perm[i],perm[j]))):w for (i,j),w in weights.items()}
            selected,ties=overlapping_local_maxima(frozenset(range(4)),edges)
            expected=frozenset(frozenset(perm[i] for i in s) for s in subjects)
            self.assertEqual(selected,expected); self.assertFalse(ties)
            for s in product((-1,1),repeat=4):
                moved=[None]*4
                for i in range(4): moved[perm[i]]=s[i]
                for i,j in ((0,1),(2,3)):
                    self.assertEqual((1-s[i]*s[j])//2,(1-moved[perm[i]]*moved[perm[j]])//2)

    def test_positive_unequal_incidence_breaks_branchwise_balance(self):
        for mu1,mu2 in ((F(1),F(1)),(F(1),F(2)),(F(2),F(1))):
            for sign in (-1,1):
                total=mu1*sign+mu2*(-sign)
                self.assertEqual(total,sign*(mu1-mu2))
                self.assertEqual(total==0,mu1==mu2)
        # Equal probabilities can hide imbalance in the unconditioned average.
        self.assertEqual((F(1,2)*(F(1)-F(2))+F(1,2)*(F(2)-F(1))),0)

    def test_tie_gate_prevents_a_forced_subject_selection(self):
        flat=weights.copy(); flat[(1,2)]=F(1,2)
        selected,ties=overlapping_local_maxima(frozenset(range(4)),flat)
        self.assertFalse(selected); self.assertEqual(len(ties),6)

    def test_mismatch_observables_are_genuine_pair_relations(self):
        for q in (q1,q2): close(self,mm(q,q),q)
        self.assertLess(maxabs(comm(q1,q2)),1e-10)
        # Gauge transport of signs AND preference leaves pair mismatch intact.
        for signs in product((-1,1),repeat=4):
            for spins in product((-1,1),repeat=4):
                transformed=[signs[i]*spins[i] for i in range(4)]
                for i,j in ((0,1),(2,3)):
                    old=(1-spins[i]*spins[j])//2
                    new=(1-(signs[i]*signs[j])*transformed[i]*transformed[j])//2
                    self.assertEqual(old,new)

    def test_sphere_record_anticorrelates_mismatch_in_every_branch(self):
        p=probabilities(self.v)
        total=0
        for (i,r),weight in p.items():
            if weight<1e-12: continue
            a,b=q_from_record(r)
            self.assertEqual(a+b,1)
            total+=weight
        self.assertAlmostEqual(total,1)
        for r in (1,2): self.assertAlmostEqual(sum(p[(i,r)] for i in range(5)),.5)
        # This is NOT the prior independent heat-bath equilibrium law.

    def test_same_selector_does_not_make_the_two_state_distributions_identical(self):
        # Prior E-L heat-bath sector: 9/16,3/16,3/16,1/16.
        # The present quantum record sector: 0,1/2,1/2,0. Both use the
        # same abstract weak-link selector, not the same dynamics or state.
        old={(0,0):F(9,16),(0,1):F(3,16),(1,0):F(3,16),(1,1):F(1,16)}
        new={(0,0):F(0),(0,1):F(1,2),(1,0):F(1,2),(1,1):F(0)}
        self.assertEqual(sum(F(a+b)*p for (a,b),p in old.items()),F(1,2))
        self.assertEqual(sum(F(a+b)*p for (a,b),p in new.items()),F(1))
        for r in (1,2):
            self.assertAlmostEqual(sum(probabilities(self.v)[(i,r)] for i in range(5)),float(new[q_from_record(r)]))

    def test_subject_local_energy_is_constant_on_the_prepared_sector(self):
        # H_ref=H4; refs |0> and records 01/10: +1/8 on each.
        for r in (1,2):
            s=r<<1
            self.assertAlmostEqual(H[s][s].real,1/8)
            self.assertAlmostEqual((q1[s][s]+q2[s][s]).real,1)
        rho=subject_density(self.v)
        self.assertAlmostEqual(trace(mm(rho,H)).real,1/8)
        close(self,mm(H,rho),scale(1/8,rho))
        # This is a specific spectral value, not total-energy zero.

    def test_three_rivals_on_same_recorded_branch(self):
        # A_R: +1 on q=0, -1 on q=1; B: 0 on q=0, -1 on q=1.
        # A_J: ± current; before intervention A_R=A_J on this selected state.
        jv=apply_work(self.v,J[0]); j2v=apply_work(self.v,J[2])
        for a,b,i,r,w in product(range(2),range(2),range(5),(1,2),range(16)):
            k=index(a,b,i,r,w); x=self.v[k]; m1,m2=q_from_record(r)
            ar1,ar2=1-2*m1,1-2*m2
            self.assertEqual(ar1+ar2,0)
            self.assertEqual(-m1-m2,-1)
            self.assertAlmostEqual(abs(jv[k]-ar1*x),0)
            self.assertAlmostEqual(abs(j2v[k]-ar2*x),0)
            # When q=1 both candidates predict negative; only q=0 differs.
            self.assertEqual(ar1 if m1 else 0,-m1)
            self.assertEqual(ar2 if m2 else 0,-m2)

    def test_local_phase_pulse_dissociates_record_and_current_models(self):
        # P=Z_M1, [P,H0]=[P,H_structure]=0, holds records fixed and reverses J.
        # P physically acts on work, not either selected record-reference pair.
        self.assertAlmostEqual(norm2(self.v),norm2(self.after))
        close(self,subject_density(self.v),subject_density(self.after))
        for ra,sign in ((0,1),(1,-1)):
            self.assertAlmostEqual(branch_current(self.v,ra),sign)
            self.assertAlmostEqual(branch_current(self.after,ra),-sign)
        # Same q, subjects and record valuations; current-identity rival flips.
        self.assertEqual(probabilities(self.v),probabilities(self.after))

    def test_alice_pair_and_triple_give_same_subject_state(self):
        close(self,subject_density(joint_state('pair')),subject_density(self.v))
        # Other Bob lab outputs need full local-state check in the preceding test.

    def test_report_bridge_falsification_margin_is_conditional(self):
        # A_R says definite pleasant for q=0; B says definite neutral.
        # Shared separately calibrated yes/no error ≤ e<1/2 gives disjoint ranges.
        for e,d in ((0,0),(.1,.1),(.2,.25),(.49,0)):
            self.assertGreater(1-e-d,e+d)
        # Same measured record distribution after the pulse is checked above;
        # the report bridge is an additional condition, not an inferred fact.

if __name__=='__main__': unittest.main()
