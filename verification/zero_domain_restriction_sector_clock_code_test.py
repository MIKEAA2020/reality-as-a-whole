"""Sector versus restricted-domain clock access in the sphere detector model.

Checks an encoded two-level subsystem, its explicit environment recovery,
and the earlier autonomous pointer history. No real subject, higher realm,
spacetime-local detector, or objective total energy is asserted.
"""
import cmath
import math
import unittest

from verification.zero_five_ray_record_current_unification_test import (
    joint_state,index,norm2,work
)
from verification.zero_sphere_mismatch_experience_comparison_test import (
    phase_flip,subject_density
)
from verification.zero_sphere_autonomous_detector_constraint_test import (
    mesh,effects,translated,channel,p_pointer_one,dot,apply
)
from verification.zero_sphere_interacting_clock_spectral_test import build
from verification.zero_spin_constitution_test import close,inner


def vectors(context='triple'):
    plus=joint_state(context)
    return plus,phase_flip(plus)


def environment_vectors(context='triple'):
    """e_(r,h)=sqrt(2) <r|encoded h>, with the prior S/E factorization.

    r=1,2, h=0,1. Environment order is a,b,sphere label i,work w.
    """
    states=vectors(context);out={}
    for r in (1,2):
        for h in (0,1):
            out[r,h]=[math.sqrt(2)*states[h][index(a,b,i,r,w)]
                      for a in range(2) for b in range(2)
                      for i in range(5) for w in range(16)]
    return out


def rho_s_ref(env,coeff):
    """Trace the actual 320-dimensional sphere/work environment from a
    joint logical/reference pure state coeff[h][a]. S basis is r=1,2."""
    na=len(coeff[0]); dim=len(env[1,0]); out=[[0j]*(2*na) for _ in range(2*na)]
    for k in range(dim):
        u=[sum(coeff[h][a]*env[r,h][k] for h in (0,1))/math.sqrt(2)
           for r in (1,2) for a in range(na)]
        for i in range(2*na):
            for j in range(2*na):out[i][j]+=u[i]*u[j].conjugate()
    return out


def recover_from_environment(env,coeff):
    """Trace S after explicit isometric environmental decoding, returning
    rho of (logical h, reference a)."""
    na=len(coeff[0]); dim=len(env[1,0]); size=2*na
    out=[[0j]*size for _ in range(size)]
    for r in (1,2):
        # amplitudes after projecting environment onto |e_(g,h)>;
        # the recovery writes (g,h), and then discards gauge g and S.
        for g in (1,2):
            u=[sum(env[g,h][k].conjugate()*
                   sum(coeff[kh][a]*env[r,kh][k] for kh in (0,1))/math.sqrt(2)
                   for k in range(dim)) for h in (0,1) for a in range(na)]
            for i in range(size):
                for j in range(size):out[i][j]+=u[i]*u[j].conjugate()
    return out


def rho_reference(coeff):
    na=len(coeff[0])
    return [[sum(coeff[h][a]*coeff[h][b].conjugate() for h in (0,1))
             for b in range(na)] for a in range(na)]


def rho_logical_reference(coeff):
    na=len(coeff[0]);v=[coeff[h][a] for h in (0,1) for a in range(na)]
    return [[x*y.conjugate() for y in v] for x in v]


def rho_sd_from_detector(env,ch):
    """Exact finite quadrature contraction for S={r} and pointer D."""
    cs=(1/math.sqrt(2),1j/math.sqrt(2));n=len(ch[0][0])
    out=[[0j]*4 for _ in range(4)]
    for r in (1,2):
        for d in (0,1):
            for rp in (1,2):
                for dp in (0,1):
                    value=0j
                    for h in (0,1):
                        for hp in (0,1):
                            overlap=inner(env[rp,hp],env[r,h])
                            amp=sum(ch[h][d][i]*ch[hp][dp][i].conjugate() for i in range(n))
                            value+=cs[h]*cs[hp].conjugate()*overlap*amp/2
                    out[(r-1)*2+d][(rp-1)*2+dp]=value
    return out


def rho_d(ch):
    return [[sum(dot(ch[h][dp],ch[h][d])/2 for h in (0,1))
             for dp in (0,1)] for d in (0,1)]


def s_times_d(pointer):
    return [[pointer[d][dp]/2 if r==rp else 0j
             for rp in (0,1) for dp in (0,1)] for r in (0,1) for d in (0,1)]


class DomainRestrictionSectorClockCodeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env=environment_vectors()
        cls.plus,cls.minus=vectors()
        cls.p,cls.f,cls.dp=mesh(40)
        cls.E=effects(cls.p,cls.dp)[0][0]
        cls.f=translated(cls.f,cls.p)
        cls.at0=channel(cls.p,cls.E,cls.f,0)
        cls.at40=channel(cls.p,cls.E,cls.f,40)
        cls.at100=channel(cls.p,cls.E,cls.f,100)

    def test_exact_record_schmidt_and_environment_orthogonality(self):
        self.assertAlmostEqual(norm2(self.plus),1)
        self.assertAlmostEqual(norm2(self.minus),1)
        for r in (1,2):
            for h in (0,1):
                for rp in (1,2):
                    for hp in (0,1):
                        target=float(r==rp and h==hp)
                        self.assertAlmostEqual(abs(inner(self.env[r,h],self.env[rp,hp])-target),0)
        expected=[[0j]*16 for _ in range(16)]
        expected[2][2]=expected[4][4]=.5
        close(self,subject_density(self.plus),expected)
        close(self,subject_density(self.minus),expected)

    def test_orthogonality_has_record_spin_and_work_structure(self):
        # Each record has a Bob-spin eigenstate and an equal-weight work
        # superposition. Z_M1 makes the two work states orthogonal.
        xis=[]
        for r in (1,2):
            w=work[1 if r==1 else -1]
            z=[x*(1-2*(j>>3)) for j,x in enumerate(w)]
            self.assertAlmostEqual(inner(w,w).real,1)
            self.assertAlmostEqual(abs(inner(w,z)),0)
            e=self.env[r,0]
            xi=[sum(w[j].conjugate()*e[16*k+j] for j in range(16))
                for k in range(len(e)//16)]
            self.assertAlmostEqual(inner(xi,xi).real,1)
            for k in range(len(xi)):
                for j in range(16):
                    self.assertAlmostEqual(abs(e[16*k+j]-xi[k]*w[j]),0)
                    self.assertAlmostEqual(abs(self.env[r,1][16*k+j]-xi[k]*z[j]),0)
            xis.append(xi)
        self.assertAlmostEqual(abs(inner(xis[0],xis[1])),0)

    def test_entangled_reference_is_independent_of_confined_domain(self):
        # Includes maximally entangled and asymmetric complex logical/reference states.
        examples=[[[1/math.sqrt(2),0],[0,1/math.sqrt(2)]],
                  [[math.sqrt(.1),1j*math.sqrt(.2)],[math.sqrt(.3),-1j*math.sqrt(.4)]]]
        for coeff in examples:
            actual=rho_s_ref(self.env,coeff); ref=rho_reference(coeff)
            expected=[[ref[a][b]/2 if r==rp else 0j
                       for rp in (0,1) for b in (0,1)]
                      for r in (0,1) for a in (0,1)]
            close(self,actual,expected)

    def test_environment_decoding_recovers_quantum_reference_correlations(self):
        for coeff in ([[1/math.sqrt(2),0],[0,1/math.sqrt(2)]],
                      [[math.sqrt(.1),1j*math.sqrt(.2)],[math.sqrt(.3),-1j*math.sqrt(.4)]]):
            recovered=recover_from_environment(self.env,coeff)
            close(self,recovered,rho_logical_reference(coeff))
        # E also retains the r label; this is an isometry on the code support,
        # not cloning an arbitrary unknown state.

    def test_confined_record_and_sphere_environment_are_not_independent(self):
        # S has 1/2 on each r. Given r, the environmental gauge is the same r;
        # joint probability 1/2 differs from the product 1/4.
        for r in (1,2):
            joint=abs(inner(self.env[r,0],self.env[r,0]))**2/2
            self.assertAlmostEqual(joint,.5)
            self.assertNotAlmostEqual(joint,.25)
        # The decoupling theorem applies to external reference A, not E itself.

    def test_optional_cross_domain_coupling_can_make_logical_bit_visible(self):
        # For each orthonormal environmental |e_(r,h)>, apply either I or
        # the S-label swap depending on (r−1) XOR h. This is a permutation
        # of the eight orthonormal |s_k>|e_(r,h)> basis states; extend by I
        # on the orthogonal complement to obtain a unitary.
        images=[(k ^ ((r-1)^h),r,h)
                for k in (0,1) for r in (1,2) for h in (0,1)]
        self.assertEqual(len(set(images)),8)
        leaked=[]
        for h in (0,1):
            v=[0j]*(2*2*5*4*16);j=0
            for a in range(2):
                for b in range(2):
                    for i in range(5):
                        for w in range(16):
                            v[index(a,b,i,h+1,w)]=(self.env[1,h][j]+self.env[2,h][j])/math.sqrt(2)
                            j+=1
            self.assertAlmostEqual(norm2(v),1)
            rho=subject_density(v)
            self.assertAlmostEqual(rho[2*(h+1)][2*(h+1)].real,1)
            leaked.append(rho)
        self.assertAlmostEqual(leaked[0][2][2].real,1)
        self.assertAlmostEqual(leaked[1][2][2].real,0)
        # This is an optional, generally nonlocal unitary in finite kinematics;
        # it has NOT been shown compatible with the cosmological constraint.

    def test_detector_pointer_changes_while_s_and_pointer_are_product(self):
        for ch in (self.at0,self.at40,self.at100):
            rho=rho_sd_from_detector(self.env,ch)
            close(self,rho,s_times_d(rho_d(ch)))
        self.assertAlmostEqual(p_pointer_one(self.at0),0,places=11)
        self.assertAlmostEqual(p_pointer_one(self.at100),.9588977733075672,places=10)
        # P(r,D=1)=P(r) P(D=1), despite changed pointer output.
        rho=rho_sd_from_detector(self.env,self.at100)
        for r in (0,1):
            self.assertAlmostEqual(rho[2*r+1][2*r+1].real,.5*p_pointer_one(self.at100))

    def test_information_access_differs_without_inventing_other_realm(self):
        # Equal-prior discrimination: S sees identical density at both readings.
        def s_reduction(ch):
            sd=rho_sd_from_detector(self.env,ch)
            return [[sum(sd[2*r+d][2*rp+d] for d in (0,1))
                     for rp in (0,1)] for r in (0,1)]
        early,late=s_reduction(self.at0),s_reduction(self.at100)
        close(self,early,late)  # their trace distance is zero; optimal success=1/2
        p=p_pointer_one(self.at100)
        success=(1+p)/2  # D_z: guess late if 1; early otherwise
        self.assertAlmostEqual(success,.9794488866537836,places=10)
        self.assertGreater(success,.97)
        # This is access to a stipulated pointer, not proof of experienced time.

    def test_bound_and_incident_preparations_have_same_s_restriction(self):
        # The regulator has a normalized bound eigenmode in d=+ and h=0.
        p,f,E,data=build(40);matrix,values,V=data[1]
        bound=[V[i][0] for i in range(len(p))]
        self.assertAlmostEqual(dot(bound,bound).real,1)
        residual=[x-values[0]*y for x,y in zip(apply(matrix,bound),bound)]
        self.assertLess(dot(residual,residual).real,1e-22)
        # Bound h=0, d=+ is stationary: D_z reads 1 with probability 1/2.
        # A different, incident preparation gives the changing pointer below,
        # yet both have the same full confined density.
        self.assertAlmostEqual(.5*dot(bound,bound).real,.5)
        for t in (0,40,100):
            v=[cmath.exp(1j*math.sqrt(values[0])*t)*x for x in self.plus]
            close(self,subject_density(v),subject_density(self.plus))
        close(self,subject_density(self.plus),subject_density(self.minus))
        for ch in (self.at0,self.at100):close(self,rho_sd_from_detector(self.env,ch),s_times_d(rho_d(ch)))
        # Finite interior eigenvalues are not claimed to be scattering states.

    def test_pair_and_triple_share_confined_code_but_differ_environment(self):
        env_pair=environment_vectors('pair')
        for r in (1,2):
            for h in (0,1):
                self.assertAlmostEqual(inner(env_pair[r,h],env_pair[r,h]).real,1)
        for h in (0,1):
            close(self,subject_density(vectors('pair')[h]),subject_density(vectors('triple')[h]))
        self.assertAlmostEqual(abs(inner(env_pair[1,0],self.env[1,0])),math.sqrt(.05))
        self.assertLess(abs(inner(env_pair[1,0],self.env[1,0])),.3)
        # Contexts remain alternative settings, not simultaneous outcomes.

if __name__=='__main__':unittest.main()
