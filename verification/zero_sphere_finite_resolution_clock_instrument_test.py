"""Finite-resolution physical clock effects and a two-outcome instrument.

The continuum POVM/CP instrument are analytic; midpoint Nyström matrices
check particular states and backaction. No detector Hamiltonian, inhomogeneous
constraint algebra, subject, or cosmological total energy is derived.
"""
import cmath
import math
import unittest

from verification.zero_sphere_flrw_normalizable_clock_test import (
    omega, velocity, packet, dp_ds, p_from_scalar_momentum
)
from verification.zero_sphere_relativistic_relational_time_test import (
    components, initial
)
from verification.zero_five_ray_record_current_unification_test import (
    joint_state, probabilities, local_density, norm2
)
from verification.zero_sphere_mismatch_experience_comparison_test import subject_density
from verification.zero_spin_constitution_test import close


def window_kernel(d, half_width=2., sigma=1.):
    """Fourier kernel for a Gaussian-smeared symmetric reading window."""
    if abs(d) < 1e-14:
        ratio=half_width
    else:
        ratio=math.sin(half_width*d)/d
    return ratio*math.exp(-.5*sigma*sigma*d*d)/math.pi


def mesh(n):
    dp=1/n
    p=[-7+(i+.5)*dp for i in range(n)]
    f=[packet(x)*math.sqrt(dp) for x in p]
    scale=math.sqrt(sum(v*v for v in f))
    return p, [v/scale for v in f], dp


def effects(p, dp, sigma=1.):
    alpha=[[dp*window_kernel(x-y, sigma=sigma) for y in p] for x in p]
    scalar=[]
    for h in (0,1):
        s=[omega(x,h) for x in p]
        v=[velocity(x,h) for x in p]  # |ds/dp|
        scalar.append([[dp*math.sqrt(v[i]*v[j])*window_kernel(s[i]-s[j],sigma=sigma)
                        for j in range(len(p))] for i in range(len(p))])
    return (alpha,alpha),tuple(scalar)


def apply(mat, vec):
    return [sum(a*b for a,b in zip(row,vec)) for row in mat]


def dot(x,y):
    return sum(a.conjugate()*b for a,b in zip(x,y))


def no_filter(mat, vec):
    """Apply sqrt(I-E^2) via its convergent binomial series."""
    result=list(vec); term=list(vec); coefficient=.5
    for k in range(1,101):
        term=apply(mat,apply(mat,term))
        result=[a-coefficient*b for a,b in zip(result,term)]
        if max(abs(coefficient*x) for x in term) < 1e-15:
            return result
        coefficient *= (2*k-1)/(2*(k+1))
    raise ArithmeticError('square-root series did not converge')


def branch_outputs(matrices, f):
    yes=[apply(mat,f) for mat in matrices]
    no=[no_filter(mat,f) for mat in matrices]
    return yes,no


def result(matrices, f, p, t=100):
    yes,no=branch_outputs(matrices,f)
    pyes=sum(dot(v,v).real for v in yes)/2
    pno=sum(dot(v,v).real for v in no)/2
    # Relative coherence of initial (|0>+i|1>)/sqrt(2).
    yyes=dot(yes[0],yes[1]).real
    yno=dot(no[0],no[1]).real
    signal=sum((a*b+c*d)*cmath.exp(1j*(omega(x,0)-omega(x,1))*t)
               for a,b,c,d,x in zip(yes[0],yes[1],no[0],no[1],p))
    return pyes,pno,yyes,yno,signal


class FiniteResolutionPhysicalClockInstrumentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p,cls.f,cls.dp=mesh(80)
        cls.alpha,cls.scalar=effects(cls.p,cls.dp)
        cls.alpha_result=result(cls.alpha,cls.f,cls.p)
        cls.scalar_result=result(cls.scalar,cls.f,cls.p)

    def test_povm_window_kernel_and_smearing(self):
        self.assertAlmostEqual(window_kernel(0),2/math.pi)
        self.assertAlmostEqual(window_kernel(.3),window_kernel(-.3))
        self.assertLess(window_kernel(.3,sigma=3),window_kernel(.3,sigma=1))
        # For E=V† M_g V, 0<=g<=1, hence 0<=E<=I. Test a few
        # independent complex input vectors in the discretization too.
        for mat in (self.alpha[0],self.scalar[0],self.scalar[1]):
            for v in (self.f,[complex(math.sin(i),math.cos(i)) for i in range(80)]):
                q=dot(v,apply(mat,v))
                self.assertAlmostEqual(q.imag,0,places=10)
                self.assertGreaterEqual(q.real,-1e-10)
                self.assertLessEqual(q.real,dot(v,v).real+1e-10)

    def test_finite_resolution_changes_event_probability(self):
        unblurred,_=effects(self.p,self.dp,sigma=0)
        blurred=self.alpha[0]
        pu=dot(self.f,apply(unblurred[0],self.f)).real
        pb=dot(self.f,apply(blurred,self.f)).real
        self.assertGreater(pu,pb)
        self.assertAlmostEqual(pb,.47587,places=4)
        # Event E is not the instrument's yes effect E².
        self.assertGreater(pb,self.alpha_result[0])

    def test_two_outcome_cp_instrument_completeness(self):
        for matrices in (self.alpha,self.scalar):
            for mat in matrices:
                for vec in (self.f,[complex(math.sin(i),math.cos(i))/math.sqrt(80) for i in range(80)]):
                    y=apply(mat,vec); z=no_filter(mat,vec)
                    self.assertAlmostEqual(dot(y,y).real+dot(z,z).real,
                                           dot(vec,vec).real,places=11)
            r=result(matrices,self.f,self.p)
            self.assertAlmostEqual(r[0]+r[1],1,places=11)

    def test_clock_readouts_are_different_operations(self):
        self.assertAlmostEqual(self.alpha_result[0],.25527066765986023,places=10)
        self.assertAlmostEqual(self.scalar_result[0],.06347488472904199,places=10)
        self.assertGreater(abs(self.alpha_result[0]-self.scalar_result[0]),.19)
        # No physical frame equivalence asserts equality of different effects.

    def test_clock_switch_transports_effect_and_instrument(self):
        # Independent Nyström kernels in the s_h variable: Δs=vΔp,
        # J=|dp/ds|. Transported Eα has sqrt(J_i J_j) K(p_i-p_j).
        for h in (0,1):
            s=[omega(x,h) for x in self.p]
            ds=[velocity(x,h)*self.dp for x in self.p]
            jac=[dp_ds(x,h) for x in s]
            recovered=[p_from_scalar_momentum(x,h) for x in s]
            converted=[[math.sqrt(ds[i]*ds[j]*jac[i]*jac[j])*
                        window_kernel(recovered[i]-recovered[j])
                        for j in range(len(s))] for i in range(len(s))]
            for a,b in zip(converted,self.alpha[h]):
                for x,y in zip(a,b): self.assertAlmostEqual(x,y,places=13)
            original=branch_outputs(self.alpha,self.f)
            transformed=branch_outputs((converted,converted),self.f)
            for outcome in (0,1):
                for x,y in zip(original[outcome][h],transformed[outcome][h]):
                    self.assertAlmostEqual(x,y,places=12)
        # W Y W†, unlike natural Y in the s representation, connects s_0(p)
        # with s_1(p); this is why the logical outcome is transported too.
        a=self.alpha_result
        self.assertAlmostEqual(a[2]+a[3],1,places=11)
        # Sequential yes followed by transported Y at scalar value 100.
        # In the s representation its off-diagonal map connects s_0(p_i)
        # to s_1(p_i), rather than pairing equal scalar momenta.
        yes,_=branch_outputs(self.alpha,self.f)
        direct=sum(x*y*cmath.exp(1j*(omega(p,0)-omega(p,1))*100)
                   for x,y,p in zip(yes[0],yes[1],self.p))
        scalar_s0=[omega(p,0) for p in self.p]
        scalar_s1=[omega(p,1) for p in self.p]
        transported=sum(x*y*cmath.exp(1j*(s0-s1)*100)
                        for x,y,s0,s1 in zip(yes[0],yes[1],scalar_s0,scalar_s1))
        self.assertAlmostEqual(abs(direct-transported),0,places=13)
        joint=(a[0]+transported.real)/2
        self.assertAlmostEqual(joint,.13204789074897558,places=11)

    def test_nonselective_readout_backaction_and_future_correlation(self):
        self.assertAlmostEqual(self.alpha_result[2]+self.alpha_result[3],1,places=11)
        self.assertAlmostEqual(self.scalar_result[2]+self.scalar_result[3],.9991460173963952,places=10)
        pre=sum(f*f*cmath.exp(1j*(omega(p,0)-omega(p,1))*100)
                for f,p in zip(self.f,self.p))
        self.assertAlmostEqual(pre.real,-.3233989993982147,places=10)
        self.assertAlmostEqual(self.alpha_result[4].real,-.261885954645758,places=10)
        self.assertAlmostEqual(self.scalar_result[4].real,-.305670273644523,places=10)
        self.assertGreater(abs(self.alpha_result[4]-pre),.05)
        # Backaction is that of these selected Kraus operators, not generic.

    def test_backaction_changes_momentum_but_keeps_each_output_on_constraint(self):
        for matrices in (self.alpha,self.scalar):
            yes,no=branch_outputs(matrices,self.f)
            before=sum(abs(f)**2*p*p for f,p in zip(self.f,self.p))
            after=sum((abs(yes[h][i])**2+abs(no[h][i])**2)*p*p/2
                      for h in (0,1) for i,p in enumerate(self.p))
            self.assertGreater(abs(after-before),1e-4)
            for outcome in (yes,no):
                total=sum(abs(outcome[h][i])**2*(-p*p/12+omega(p,h)**2/2+h)/2
                          for h in (0,1) for i,p in enumerate(self.p))
                self.assertAlmostEqual(total,0,places=12)
        # Momentum changes do not identify a closed detector's energy cost.

    def test_same_effect_different_postmeasurement_instrument(self):
        # Apply a logical Z phase only after a yes outcome. The yes/no effects
        # and probabilities are unchanged, but the yes-conditioned Y flips.
        pyes,pno,yyes,yno,_=self.alpha_result
        yes,_=branch_outputs(self.alpha,self.f)
        # Apply unitary diag(1,-1) to yes branch only.
        phased=[yes[0],[-z for z in yes[1]]]
        phased_prob=sum(dot(v,v).real for v in phased)/2
        phased_y=dot(phased[0],phased[1]).real
        self.assertAlmostEqual(phased_prob,pyes,places=11)
        self.assertAlmostEqual(yyes/pyes,1,places=11)
        self.assertAlmostEqual(phased_y/phased_prob,-1,places=11)
        self.assertAlmostEqual(pyes+pno,1,places=11)
        self.assertAlmostEqual(yno/pno,1,places=11)

    def test_midpoint_convergence(self):
        p,f,dp=mesh(160); alpha,scalar=effects(p,dp)
        for old,new in ((self.alpha_result,result(alpha,f,p)),
                        (self.scalar_result,result(scalar,f,p))):
            self.assertLess(abs(old[0]-new[0]),3e-5)
            self.assertLess(abs(old[4]-new[4]),7e-6)

    def test_sphere_confined_density_independent_of_logical_state(self):
        v=initial(joint_state('triple')); a,b,_=components(v)
        base=subject_density([x*math.sqrt(2) for x in a])
        base_table=probabilities([x*math.sqrt(2) for x in a])
        for c,d in ((1,0),(0,1),(1,1),(1,1j)):
            z=[c*x+d*y for x,y in zip(a,b)]; n=norm2(z)
            rho=[[x/n for x in row] for row in subject_density(z)]
            close(self,rho,base)
            table=probabilities(z)
            for key in base_table: self.assertAlmostEqual(table[key]/n,base_table[key])
        # Four polarizations determine both diagonal and cross operators;
        # integrating any physical geometry/clock instrument preserves rho_S.

    def test_pair_triple_receiver_match_for_arbitrary_logical_polarization(self):
        pair=components(initial(joint_state('pair')))
        triple=components(initial(joint_state('triple')))
        for c,d in ((1,0),(0,1),(1,1),(1,1j)):
            vp=[c*x+d*y for x,y in zip(pair[0],pair[1])]
            vt=[c*x+d*y for x,y in zip(triple[0],triple[1])]
            close(self,local_density(vp),local_density(vt))
        # Determines the reduced density for any logical density matrix,
        # including the conditional outputs of these h-diagonal instruments.

if __name__=='__main__':
    unittest.main()
