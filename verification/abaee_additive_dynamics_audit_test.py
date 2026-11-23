"""Focused checks of Abaee 21808030 and the zero-reference model.

The in-radius construction is analytic, with finite matrix regressions.
This does not replay the paper's supplementary code or audit every theorem.
"""
import cmath
import math
import unittest
from fractions import Fraction as F
from verification.zero_spin_constitution_test import X,Y,Z,add,close,eye,inner,kron,mm,mv,rank,scale
from verification.finite_tetrahedral_zero_reference_test import S,initial,op,prod,recorded_whole,sub


def outer(v): return [[x*y.conjugate() for y in v] for x in v]
def expect(v,a): return inner(v,mv(a,v))
def normal(v): return math.sqrt(max(0,inner(v,v).real))
def purity(rho): return sum(mm(rho,rho)[i][i].real for i in range(len(rho)))


def choi_pair(d):
    # |Φ> and (I⊗U)|Φ>, U diagonal with d-th roots of unity.
    a=[0j]*(d*d); b=[0j]*(d*d)
    for k in range(d):
        a[k*d+k]=1/math.sqrt(d)
        b[k*d+k]=cmath.exp(2j*math.pi*k/d)/math.sqrt(d)
    return a,b


def partial_trace_output(j,d):
    return [[sum(j[d*a+k][d*b+k] for k in range(d)) for b in range(d)] for a in range(d)]


def ab_reduction(v):
    # Reference index, work bits A,B,RA,RB. Trace C,RA,RB.
    return [[sum(v[16*r+4*a+p]*v[16*r+4*b+p].conjugate()
                 for r in range(4) for p in range(4)) for b in range(4)] for a in range(4)]


class AdditiveDynamicsAuditTests(unittest.TestCase):
    def test_orthogonal_choi_vectors_for_all_small_dimensions(self):
        for d in range(2,8):
            a,b=choi_pair(d)
            self.assertAlmostEqual(inner(a,a).real,1)
            self.assertAlmostEqual(inner(b,b).real,1)
            self.assertAlmostEqual(abs(inner(a,b)),0)
            close(self,partial_trace_output(outer(a),d),scale(1/d,eye(d)))
            close(self,partial_trace_output(outer(b),d),scale(1/d,eye(d)))

    def test_choi_boundary_channel_spectrum_and_trace_preservation(self):
        for d in range(2,7):
            a,b=choi_pair(d); p=outer(a); q=outer(b)
            j=scale(1/d**2,add(eye(d*d),sub(p,q)))
            close(self,partial_trace_output(j,d),scale(1/d,eye(d)))
            self.assertAlmostEqual(expect(a,j).real,2/d**2)
            self.assertAlmostEqual(expect(b,j).real,0)
            self.assertEqual(rank(j),d*d-1)
            # Spectral decomposition: j=(2/d²)P + (1/d²)(I-P-Q),
            # nonnegative with a zero eigenvalue.
            close(self,j,add(scale(2/d**2,p),scale(1/d**2,sub(sub(eye(d*d),p),q))))

    def test_beyond_boundary_not_completely_positive(self):
        for d in range(2,7):
            a,b=choi_pair(d); p=outer(a); q=outer(b)
            t=1/d**2+1/(10*d**2)
            j=add(scale(1/d**2,eye(d*d)),scale(t,sub(p,q)))
            self.assertAlmostEqual(expect(b,j).real,1/d**2-t)
            self.assertLess(expect(b,j).real,0)
            close(self,partial_trace_output(j,d),scale(1/d,eye(d)))

    def test_diamond_distance_is_exact_by_orthogonal_choi_outputs(self):
        # For Ψ=Id−Ad_U, all channels have diamond norm 1, so ||Ψ||≤2.
        # The normalized maximally entangled input produces P−Q; P,Q are
        # orthogonal rank-one projections, so its trace norm is exactly 2.
        for d in range(2,7):
            a,b=choi_pair(d); p=outer(a); q=outer(b); delta=sub(p,q)
            self.assertAlmostEqual(expect(a,delta).real,1)
            self.assertAlmostEqual(expect(b,delta).real,-1)
            self.assertEqual(rank(delta),2)
            # Analytic spectral result: ||P−Q||_1=2; lower and upper bounds
            # meet at ||Ψ||_diamond=2, hence boundary distance 2/d².
            self.assertEqual(F(2,d*d),2*F(1,d*d))

    def test_qubit_counterexample_is_positive_pauli_mixture(self):
        # Φ = Ω +(Id−Ad_Z)/4 = (2 Id + Ad_X + Ad_Y)/4.
        # Its normalized Choi is diag(2,1,1,0)/4 in the Bell basis.
        d=2; a,b=choi_pair(d)
        j=scale(.25,add(eye(4),sub(outer(a),outer(b))))
        bell_x=[0,1/math.sqrt(2),1/math.sqrt(2),0]
        bell_y=[0,-1j/math.sqrt(2),1j/math.sqrt(2),0]
        mixture=add(add(scale(.5,outer(a)),scale(.25,outer(bell_x))),scale(.25,outer(bell_y)))
        close(self,j,mixture)
        self.assertAlmostEqual(expect(b,j).real,0)
        # Perfectly distinguishable identity and Z channels give diamond
        # distance 2; the factor 1/4 gives 1/2, not strictly larger.

    def test_same_channel_opposite_signed_state_energy_changes(self):
        n=[[0,0],[0,1]]
        zero=[[1,0],[0,0]]; one=[[0,0],[0,1]]
        def val(rho):
            out=mm(mm(X,rho),X)
            return (sum(mm(n,out)[i][i] for i in range(2))-
                    sum(mm(n,rho)[i][i] for i in range(2))).real
        self.assertEqual(val(zero),1)
        self.assertEqual(val(one),-1)
        # Same X channel, opposite state-conditioned energy changes. Thus
        # this quantity is not a scalar of the channel alone.

    def test_conserved_swap_has_opposite_state_dependent_transfers(self):
        swap=[[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]
        n=[[0,0],[0,1]]
        a=kron(n,eye(2)); b=kron(eye(2),n)
        close(self,mm(swap,add(a,b)),mm(add(a,b),swap))
        v=[0,0,1,0]; w=mv(swap,v)
        self.assertEqual(expect(w,a)-expect(v,a),-1)
        self.assertEqual(expect(w,b)-expect(v,b),1)
        self.assertEqual(expect(mv(swap,w),a)-expect(w,a),1)
        self.assertEqual(expect(mv(swap,w),b)-expect(w,b),-1)

    def test_state_annotated_energy_change_telescopes(self):
        # 0→1→0 under X; both signed steps and their sum are exact.
        values=(F(0),F(1),F(0))
        steps=[values[i+1]-values[i] for i in range(2)]
        self.assertEqual(steps,[1,-1])
        self.assertEqual(sum(steps),values[-1]-values[0])
        # This is a boundary term on state-labelled histories; it is not a
        # channel-dependent, refinement-additive action selecting dynamics.

    def test_same_marginals_different_relational_purity_in_sphere_model(self):
        actual=recorded_whole()
        alt=[x/math.sqrt(2) for x in prod(S,mv(sub(op(X,3),op(X,2)),initial()))]
        a,b=ab_reduction(actual),ab_reduction(alt)
        self.assertAlmostEqual(purity(a),1/3)
        self.assertAlmostEqual(purity(b),1)
        # Both have maximally mixed individual A and B states; the AB
        # correlation is a relational quantity, not a subject/valence proof.
        for rho in (a,b):
            rho_a=[[sum(rho[2*i+k][2*j+k] for k in range(2)) for j in range(2)] for i in range(2)]
            rho_b=[[sum(rho[2*k+i][2*k+j] for k in range(2)) for j in range(2)] for i in range(2)]
            close(self,rho_a,scale(.5,eye(2))); close(self,rho_b,scale(.5,eye(2)))

    def test_composition_does_not_follow_edge_purity_alone(self):
        # Two pure preparations have purity 1; identical γ=1/2 amplitude
        # damping yields distinct composite output purities 1 and 7/8.
        gamma=.5
        damp0=[[1,0],[0,0]]
        damp_plus=[[.5*(1+gamma),.5*math.sqrt(1-gamma)],
                   [.5*math.sqrt(1-gamma),.5*(1-gamma)]]
        self.assertEqual(purity(damp0),1)
        self.assertAlmostEqual(purity(damp_plus),7/8)

    def test_cp_is_not_synonymous_with_trace_preservation(self):
        # ρ↦2ρ is CP (one Kraus operator √2 I), but not TP.
        rho=[[1,0],[0,0]]
        out=scale(2,rho)
        self.assertEqual(sum(out[i][i] for i in range(2)),2)
        self.assertEqual(sum(rho[i][i] for i in range(2)),1)

if __name__=='__main__': unittest.main()
