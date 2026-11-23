"""Local nondemolition pointer coupling for the conserved-sphere singlet.

Tests check a stipulated finite-dimensional unitary, not an actual subject,
fundamental time, preferred foliation, or experiential identity.
"""
from math import sqrt, pi, sin, cos
import unittest


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a,b):
    return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]


def scale(s,a):
    return [[s*x for x in row] for row in a]


def eye(n):
    return [[complex(i==j) for j in range(n)] for i in range(n)]


def kron(a,b):
    return [[a[i//len(b)][j//len(b[0])]*b[i%len(b)][j%len(b[0])]
             for j in range(len(a[0])*len(b[0]))]
            for i in range(len(a)*len(b))]


def conjugate(u,rho):
    return mm(mm(u,rho),dagger(u))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def outer(v):
    return [[x*y.conjugate() for y in v] for x in v]


def projector(n):
    x,y,z=n
    return [[(1+z)/2,complex(x,-y)/2],
            [complex(x,y)/2,(1-z)/2]]


def partial_a(rho):
    # Total ordered A (2) ⊗ B (2) ⊗ R (2).
    return [[sum(rho[a*4+i][a*4+j] for a in range(2))
             for j in range(4)] for i in range(4)]


def partial_b(rho):
    return [[sum(rho[b*2+i][b*2+j] for b in range(2))
             for j in range(2)] for i in range(2)]


def assert_matrix(test,a,b,places=10):
    test.assertEqual((len(a),len(a[0])),(len(b),len(b[0])))
    for ar,br in zip(a,b):
        for x,y in zip(ar,br): test.assertAlmostEqual(abs(x-y),0,places=places)


I=eye(2)
X=[[0,1],[1,0]]
Z=[[1,0],[0,-1]]
PPLUS=projector((0,0,1))
PMINUS=projector((0,0,-1))
RECORD_U=add(kron(PPLUS,I),kron(PMINUS,X))
GENERATOR=kron(PMINUS,add(I,scale(-1,X)))
TRINE=((sqrt(3)/2,0,-.5),(-sqrt(3)/4,sqrt(3)/2,.25),
       (-sqrt(3)/4,-sqrt(3)/2,.25))


def initial():
    # |ψ−>_AB ⊗ |0>_R; ordering A,B,R.
    v=[0j]*8
    v[2],v[4]=1/sqrt(2),-1/sqrt(2)
    return outer(v)


def final_state():
    return conjugate(kron(I,RECORD_U),initial())


def nonselective_alice(state,kraus):
    out=[[0j]*8 for _ in range(8)]
    for k in kraus:
        out=add(out,conjugate(kron(k,eye(4)),state))
    return out


def joint(state,alice_effect,record_effect):
    e=kron(kron(alice_effect,I),record_effect)
    return trace(mm(state,e)).real


class LocalRecordConstitutionTests(unittest.TestCase):
    def test_record_unitary_generated_by_nonnegative_local_hamiltonian(self):
        # G²=2G gives exp(−i θG)=I+(exp(−2iθ)−1)G/2.
        assert_matrix(self,mm(GENERATOR,GENERATOR),scale(2,GENERATOR))
        theta=pi/2
        unitary=add(eye(4),scale((complex(cos(2*theta),-sin(2*theta))-1)/2,GENERATOR))
        assert_matrix(self,unitary,RECORD_U)
        assert_matrix(self,mm(dagger(unitary),unitary),eye(4))
        # G=P−⊗(I−X) has eigenvalues 0 and 2, so H=ħgG is positive for g>0.
        # It commutes with B's Z energy; R is assumed energetically degenerate.
        assert_matrix(self,mm(GENERATOR,kron(Z,I)),mm(kron(Z,I),GENERATOR))

    def test_gate_correlates_record_and_b_spin(self):
        br=partial_a(final_state())
        expected=[[0j]*4 for _ in range(4)]
        expected[0][0]=expected[3][3]=.5
        assert_matrix(self,br,expected)
        assert_matrix(self,partial_b(br),scale(.5,I))
        self.assertAlmostEqual(trace(mm(br,kron(Z,Z))).real,1)

    def test_nonselective_pair_and_trine_do_not_change_local_br_state(self):
        rho=final_state()
        pair=[PPLUS,PMINUS]
        trine=[scale(sqrt(2/3),projector(n)) for n in TRINE]
        for instrument in (pair,trine):
            total=[[0j]*2 for _ in range(2)]
            for k in instrument: total=add(total,mm(dagger(k),k))
            assert_matrix(self,total,I)
            assert_matrix(self,partial_a(nonselective_alice(rho,instrument)),partial_a(rho))

    def test_conditional_record_distributions_pair_and_trine(self):
        rho=final_state()
        self.assertAlmostEqual(joint(rho,PPLUS,PPLUS),0)
        self.assertAlmostEqual(joint(rho,PPLUS,PMINUS),.5)
        self.assertAlmostEqual(joint(rho,PMINUS,PPLUS),.5)
        self.assertAlmostEqual(joint(rho,PMINUS,PMINUS),0)
        expected_plus=(1/4,1/8,1/8)
        expected_minus=(1/12,5/24,5/24)
        for n,pp,pm in zip(TRINE,expected_plus,expected_minus):
            f=scale(2/3,projector(n))
            self.assertAlmostEqual(joint(rho,f,PPLUS),pp)
            self.assertAlmostEqual(joint(rho,f,PMINUS),pm)
        self.assertAlmostEqual(sum(expected_plus),.5)
        self.assertAlmostEqual(sum(expected_minus),.5)

    def test_full_record_distribution_is_not_the_conditional_mean(self):
        rho=final_state()
        for n in TRINE:
            effect=scale(2/3,projector(n))
            plus=joint(rho,effect,PPLUS)
            minus=joint(rho,effect,PMINUS)
            self.assertAlmostEqual(plus+minus,1/3)
            self.assertAlmostEqual((plus-minus)/(plus+minus),-n[2])
            self.assertGreater(plus,0)
            self.assertGreater(minus,0)

    def test_unsharp_signed_local_effects_are_no_signalling_but_not_unique(self):
        # E±=(I±ηZ)/2 are effects for all |η|≤1, with zero mean in I/2.
        for eta in (0,.25,.5,1):
            ep=scale(.5,add(I,scale(eta,Z)))
            em=scale(.5,add(I,scale(-eta,Z)))
            assert_matrix(self,add(ep,em),I)
            self.assertAlmostEqual(trace(ep).real/2,.5)
            self.assertAlmostEqual(trace(em).real/2,.5)
            self.assertAlmostEqual(trace(mm(PPLUS,ep)).real,(1+eta)/2)

    def test_local_incidence_can_vary_without_changing_no_signal_or_zero(self):
        for rate in (.2,.7,1):
            for sharpness in (0,.4,1):
                ep=scale(rate/2,add(I,scale(sharpness,Z)))
                em=scale(rate/2,add(I,scale(-sharpness,Z)))
                absent=scale(1-rate,I)
                assert_matrix(self,add(add(ep,em),absent),I)
                self.assertAlmostEqual(trace(ep).real/2,rate/2)
                self.assertAlmostEqual(trace(em).real/2,rate/2)
                self.assertAlmostEqual(trace(absent).real/2,1-rate)

    def test_same_signed_observable_different_full_distributions(self):
        # Scheme A: ±1 sharp. Scheme B: +3/-1 unsharp with E+=Π+/2.
        ea_plus=PPLUS
        ea_minus=PMINUS
        eb_plus=scale(.5,PPLUS)
        eb_minus=add(I,scale(-1,eb_plus))
        va=add(ea_plus,scale(-1,ea_minus))
        vb=add(scale(3,eb_plus),scale(-1,eb_minus))
        assert_matrix(self,va,Z)
        assert_matrix(self,vb,Z)
        rho=scale(.5,I)
        self.assertAlmostEqual(trace(mm(rho,ea_plus)).real,.5)
        self.assertAlmostEqual(trace(mm(rho,eb_plus)).real,.25)
        # The two outcome distributions have different second moments.
        second_a=add(ea_plus,ea_minus)
        second_b=add(scale(9,eb_plus),eb_minus)
        self.assertAlmostEqual(trace(mm(rho,second_a)).real,1)
        self.assertAlmostEqual(trace(mm(rho,second_b)).real,3)

    def test_sign_reversal_leaves_quantum_and_no_signalling_structure(self):
        br=partial_a(final_state())
        v=kron(I,Z)
        self.assertAlmostEqual(trace(mm(br,v)).real,0)
        self.assertAlmostEqual(trace(mm(br,scale(-1,v))).real,0)
        self.assertAlmostEqual(v[0][0],1)
        self.assertAlmostEqual(scale(-1,v)[0][0],-1)

    def test_clock_time_controls_the_interaction_not_an_irreversible_record(self):
        # For P− the pointer flips with sin²(g t); it returns at gt=π.
        for gt,prob in ((0,0),(pi/4,.5),(pi/2,1),(pi,0)):
            self.assertAlmostEqual(sin(gt)**2,prob)


if __name__ == '__main__': unittest.main()
