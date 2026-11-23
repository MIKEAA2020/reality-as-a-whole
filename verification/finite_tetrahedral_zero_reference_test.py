"""Finite spin-zero reference with exact opposite records and SO(3) symmetry.

Logical SO(3) on the reference multiplicity space is not a spacetime rotation;
subject, experiential sign and selection rules are not inferred from records.
"""
import math
import unittest
from verification.zero_spin_constitution_test import X,Y,Z,add,close,eye,kron,mm,mv,scale,inner
from verification.zero_invariant_sphere_instrument_test import adj,frame,pairing_vectors,singlet_pairs
from verification.zero_spherical_plenitude_opposite_records_test import (
    TETRA, initial, op, recorded, record_unitary, tensor, vecnorm,
)


def outer(a,b): return [[x*y.conjugate() for y in b] for x in a]
def sub(a,b): return add(a,scale(-1,b))
def comm(a,b): return sub(mm(a,b),mm(b,a))
def maxabs(a): return max(abs(x) for row in a for x in row)
def sum_mats(ms):
    a=scale(0,ms[0])
    for b in ms: a=add(a,b)
    return a

def vdiff(a,b): return [x-y for x,y in zip(a,b)]
def prod(a,b): return [x*y for x in a for y in b]

S=[.5+0j]*4
V=[[math.sqrt(3)*n[k]/2+0j for n in TETRA] for k in range(3)]


def rotor(axis,angle):
    l=math.sqrt(sum(x*x for x in axis)); axis=[x/l for x in axis]
    p=sum_mats([scale(x,s) for x,s in zip(axis,(X,Y,Z))])
    return add(scale(math.cos(angle/2),eye(2)),scale(-1j*math.sin(angle/2),p))

def rotation3(u):
    # U σ_a U†=Σ_b R_ba σ_b.
    pauli=(X,Y,Z)
    return [[.5*sum(mm(mm(mm(pauli[b],u),pauli[a]),adj(u))[k][k]
                     for k in range(2)).real for a in range(3)] for b in range(3)]

def ref_rotation(u):
    r=rotation3(u)
    out=outer(S,S)
    for a in range(3):
        for b in range(3): out=add(out,scale(r[b][a],outer(V[b],V[a])))
    return out

def global_rotation(u): return kron(ref_rotation(u),tensor(u,u,eye(2),eye(2)))

def controlled_gate():
    out=[[0j]*64 for _ in range(64)]
    for i,n in enumerate(TETRA):
        gate=mm(record_unitary(n,0,2),record_unitary(n,1,3))
        for r in range(16):
            for c in range(16): out[16*i+r][16*i+c]=gate[r][c]
    return out

def recorded_whole(): return [x/2 for n in TETRA for x in recorded(n)]
def prepared_whole(): return prod(S,initial())

def ref_rho(v):
    return [[sum(v[16*i+j]*v[16*k+j].conjugate() for j in range(16))
             for k in range(4)] for i in range(4)]

def local_record_rho(v,which):
    # Work bit order A,B,RA,RB; trace all including the reference.
    result=[[0j]*2 for _ in range(2)]
    shift=1 if which==0 else 0
    for ref in range(4):
        for x in range(16):
            for y in range(16):
                if (x | (1<<shift)) == (y | (1<<shift)):
                    result[(x>>shift)&1][(y>>shift)&1]+=v[16*ref+x]*v[16*ref+y].conjugate()
    return result


class FiniteTetrahedralZeroReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.init=prepared_whole(); cls.final=recorded_whole(); cls.gate=controlled_gate()
        cls.generic=rotor((.2,-.3,.7),.73)
        cls.tetra_rotation=rotor((1,1,1),2*math.pi/3)

    def test_six_spin_reference_has_five_independent_zero_states(self):
        states=frame([singlet_pairs(p) for p in pairing_vectors(list(range(6)))])
        self.assertEqual(len(states),5)
        from verification.zero_spin_constitution_test import total_spin
        for state in states:
            for sigma in (X,Y,Z): self.assertAlmostEqual(vecnorm(mv(total_spin(sigma,6),state)),0)

    def test_tetrahedron_singlet_vector_basis_and_moments(self):
        basis=[S]+V
        for i in range(4):
            for j in range(4): self.assertAlmostEqual(abs(inner(basis[i],basis[j])-(i==j)),0)
        for i in range(3):
            self.assertAlmostEqual(sum(n[i] for n in TETRA)/4,0)
            for j in range(3): self.assertAlmostEqual(sum(n[i]*n[j] for n in TETRA)/4,(i==j)/3)

    def test_finite_controlled_gate_creates_uniform_opposite_records(self):
        close(self,mm(adj(self.gate),self.gate),eye(64))
        self.assertAlmostEqual(vecnorm(vdiff(mv(self.gate,self.init),self.final)),0)
        total=kron(eye(4),add(op(Z,2),op(Z,3)))
        self.assertAlmostEqual(vecnorm(mv(total,self.final)),0)
        for i,n in enumerate(TETRA):
            v=self.final[16*i:16*(i+1)]
            p01=sum(abs(a)**2 for idx,a in enumerate(v) if idx%4==1)
            p10=sum(abs(a)**2 for idx,a in enumerate(v) if idx%4==2)
            self.assertAlmostEqual(p01,1/8); self.assertAlmostEqual(p10,1/8)

    def test_decomposition_exhibits_so3_invariant_contractions(self):
        # Ω=1/2 |s> Ψ(|01>+|10>) + 1/(2√3) Σ|v_a>σ_a Ψ(|01>−|10>).
        plus=mv(add(op(X,2),op(X,3)),initial())
        minus=mv(sub(op(X,3),op(X,2)),initial())
        v=[x/2 for x in prod(S,plus)]
        for k,sigma in enumerate((X,Y,Z)):
            term=prod(V[k],mv(op(sigma,0),minus))
            v=[x+y/(2*math.sqrt(3)) for x,y in zip(v,term)]
        self.assertAlmostEqual(vecnorm(vdiff(v,self.final)),0)

    def test_initial_and_recorded_whole_are_continuously_invariant(self):
        for u in (self.generic,self.tetra_rotation,rotor((0,0,1),math.pi/2)):
            g=global_rotation(u)
            close(self,mm(adj(g),g),eye(64))
            for v in (self.init,self.final): self.assertAlmostEqual(vecnorm(vdiff(mv(g,v),v)),0)

    def test_reference_mixed_state_is_singlet_plus_isotropic_vector(self):
        rho=ref_rho(self.final)
        expected=scale(.5,outer(S,S))
        for v in V: expected=add(expected,scale(1/6,outer(v,v)))
        close(self,rho,expected)
        for u in (self.generic,self.tetra_rotation):
            r=ref_rotation(u)
            close(self,mm(mm(r,rho),adj(r)),rho)

    def test_discrete_controlled_gate_has_tetrahedral_not_full_symmetry(self):
        rx=rotor((1,0,0),math.pi)
        generators=(self.tetra_rotation,rx)
        for u in generators: self.assertLess(maxabs(comm(global_rotation(u),self.gate)),1e-9)
        perms=[]
        for u in generators:
            r=rotation3(u)
            transformed=[tuple(sum(r[a][b]*n[b] for b in range(3)) for a in range(3)) for n in TETRA]
            perms.append(tuple(next(j for j,m in enumerate(TETRA)
                                    if sum((x-y)**2 for x,y in zip(v,m))<1e-12)
                               for v in transformed))
        group={tuple(range(4))}
        while True:
            larger=group | {tuple(p[q[i]] for i in range(4)) for p in group for q in perms}
            if larger==group: break
            group=larger
        self.assertEqual(len(group),12)
        self.assertGreater(maxabs(comm(global_rotation(self.generic),self.gate)),1e-3)
        # This gate exactly evaluates four distinct fixed-labelled PVMs,
        # not a continuum of sharp axes.

    def test_dedicated_full_so3_invariant_hamiltonian_prepares_same_state(self):
        # Initial and final are orthogonal rotational scalars. This rank-two
        # H is SO(3)-invariant but is tailored to this prepared global state,
        # and is not claimed to implement a universal measurement processor.
        h=scale(1j,sub(outer(self.final,self.init),outer(self.init,self.final)))
        close(self,h,adj(h))
        self.assertAlmostEqual(abs(inner(self.init,self.final)),0)
        for u in (self.generic,self.tetra_rotation):
            self.assertLess(maxabs(comm(global_rotation(u),h)),1e-9)
        h2=mm(h,h)
        evolution=add(sub(eye(64),h2),scale(-1j,h)) # exp(-iπH/2)
        close(self,mm(adj(evolution),evolution),eye(64))
        self.assertAlmostEqual(vecnorm(vdiff(mv(evolution,self.init),self.final)),0)

    def test_symmetry_and_spin_zero_do_not_uniquely_select_record_state(self):
        self.assertAlmostEqual(abs(inner(self.init,self.final)),0)
        # Each is invariant and physical-spin zero, but records disagree:
        # initial (RA,RB)=00; final only 01 or 10.
        for i,v in enumerate(self.init):
            if abs(v)>1e-10: self.assertEqual(i%4,0)
        for i,v in enumerate(self.final):
            if abs(v)>1e-10: self.assertIn(i%4,(1,2))
        # Formal state alternatives are not claimed to be genuinely possible
        # complete worlds under the user's actuality–necessity proposal.

    def test_even_exact_signed_zero_and_symmetry_do_not_fix_organization(self):
        # Another invariant state has the same reference/record-label joint
        # distribution and exact opposite pointer labels, but no correlation
        # between direction and the logical system.
        opposite=mv(sub(op(X,3),op(X,2)),initial())
        alternative=[x/math.sqrt(2) for x in prod(S,opposite)]
        self.assertAlmostEqual(vecnorm(alternative),1)
        self.assertAlmostEqual(abs(inner(alternative,self.final)),0)
        self.assertAlmostEqual(vecnorm(mv(kron(eye(4),add(op(Z,2),op(Z,3))),alternative)),0)
        for u in (self.generic,self.tetra_rotation):
            self.assertAlmostEqual(vecnorm(vdiff(mv(global_rotation(u),alternative),alternative)),0)
        for i in range(4):
            for pointer in (1,2):
                actual=sum(abs(alternative[16*i+j])**2 for j in range(16) if j%4==pointer)
                self.assertAlmostEqual(actual,1/8)
        singlet=scale(.25,sub(sub(sub(eye(16),mm(op(X,0),op(X,1))),
                                    mm(op(Y,0),op(Y,1))),mm(op(Z,0),op(Z,1))))
        test_op=kron(eye(4),singlet)
        self.assertAlmostEqual(inner(alternative,mv(test_op,alternative)).real,1)
        self.assertAlmostEqual(inner(self.final,mv(test_op,self.final)).real,.5)
        # This is a formal distinction, not a metaphysical possibility claim.

    def test_marginal_state_only_quality_rule_cannot_give_opposite_signs(self):
        a=local_record_rho(self.final,0); b=local_record_rho(self.final,1)
        close(self,a,scale(.5,eye(2))); close(self,b,scale(.5,eye(2)))
        self.assertAlmostEqual(sum(a[i][i]*Z[i][i] for i in range(2)).real,0)
        # A common functional of equal local marginals gives equal values;
        # if their sum must vanish, both are zero. Branch-conditioned values
        # need an actual-record account and need not satisfy this hypothesis.

    def test_eight_equal_joint_outcomes_do_not_select_history(self):
        labels=[(i,x) for i in range(4) for x in (0,1)]
        self.assertEqual(len(set(labels)),8)
        a=labels[:]; b=list(reversed(labels))
        self.assertNotEqual(a,b)
        self.assertEqual(sorted(a),sorted(b))
        self.assertEqual(math.factorial(8),40320)
        # Neither formal order is derived as a physical actual history.

if __name__=='__main__': unittest.main()
