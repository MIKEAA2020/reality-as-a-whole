"""Controls for the continuum Mourre and unique exterior-eigenvalue argument.

The note contains the analytic proof. Finite Nyström matrices cannot prove
absence of singular-continuous spectrum or embedded continuum eigenvalues.
"""
import math
import unittest
from verification.zero_sphere_interacting_clock_spectral_test import build
from verification.zero_sphere_finite_resolution_clock_instrument_test import apply,dot,window_kernel

C=7/(3*math.pi)
COUPLING=.8


def bump(p):
    u=p+7
    if u<=0 or u>=1:return 0.
    return math.exp(4-1/(u*(1-u)))


def bump_prime(p):
    u=p+7
    if u<=0 or u>=1:return 0.
    return bump(p)*(1-2*u)/(u*u*(1-u)*(1-u))


def kernel_prime(d):
    if abs(d)<1e-4:
        return 2/math.pi*(-7*d/3+71*d**3/30)
    return math.exp(-d*d/2)/math.pi*(2*math.cos(2*d)/d-math.sin(2*d)/d**2-math.sin(2*d))


def commutator_kernel(p,q):
    return -(bump(p)-bump(q))*kernel_prime(p-q) - .5*(bump_prime(p)+bump_prime(q))*window_kernel(p-q)


def samples(n): return [-7+(i+.5)/n for i in range(n)]


def cmul(c,v):return [c*x for x in v]


class InteractingClockMourreSpectrumTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data={n:build(n) for n in (40,80,160)}

    def test_gaussian_smeared_window_second_moment(self):
        # g is indicator[-2,2] convolved with variance-one Gaussian.
        # ∫x²g dx = ∫_{−2}² (r²+1)dr = 28/3.
        second_moment=2*(8/3+2)
        self.assertAlmostEqual(second_moment,28/3)
        self.assertAlmostEqual(second_moment/(4*math.pi),C)
        self.assertLess(COUPLING*C,2)
        self.assertLess(COUPLING*C,13/6)

    def test_zero_mean_exterior_form_bound_for_multiple_vectors(self):
        for n,(p,f,E,S) in self.data.items():
            for kind in range(5):
                if kind==0:v=[1+0j for _ in p]
                elif kind==1:v=[complex(x+6.5,0) for x in p]
                elif kind==2:v=[complex(math.sin(6*x),math.cos(4*x)) for x in p]
                elif kind==3:v=[complex(math.cos(20*x),math.sin(3*x)) for x in p]
                else:v=[complex((x+6.5)**2,(x+6.5)**3) for x in p]
                mean=sum(v)/n;v=[x-mean for x in v]
                if dot(v,v).real<1e-20:continue
                ev=dot(v,apply(E,v)).real
                low=sum((-6-x)*abs(z)**2 for x,z in zip(p,v))
                high=sum((x+7)*abs(z)**2 for x,z in zip(p,v))
                self.assertGreaterEqual(ev,-1e-12)
                self.assertLessEqual(ev,C*low+1e-12)
                self.assertLessEqual(ev,C*high+1e-12)
                for d,edge in ((1,6),(-1,49/6)):
                    mat=S[d][0]
                    q=dot(v,apply(mat,v)).real
                    signed=q-edge*dot(v,v).real
                    self.assertGreater(signed if d==1 else -signed,0)

    def test_nystrom_has_one_exterior_level_in_each_channel(self):
        # This is numerical support, not the continuum uniqueness proof.
        for p,f,E,S in self.data.values():
            self.assertEqual(sum(x<6 for x in S[1][1]),1)
            self.assertEqual(sum(x>49/6 for x in S[-1][1]),1)
            self.assertEqual(sum(x>49/6 for x in S[1][1]),0)
            self.assertEqual(sum(x<6 for x in S[-1][1]),0)

    def test_conjugate_vector_field_and_free_commutator_positive(self):
        for p in (-6.95,-6.8,-6.5,-6.2,-6.05):
            self.assertGreater(bump(p),0)
            self.assertGreater(-bump(p)*p/3,0)
            eps=1e-6
            self.assertAlmostEqual((bump(p+eps)-bump(p-eps))/(2*eps),bump_prime(p),places=8)
        self.assertEqual(bump(-7),0);self.assertEqual(bump(-6),0)

    def test_kernel_derivative_and_commutator_symmetry(self):
        for d in (-1,-.7,-.1,0,.1,.7,1):
            e=1e-5
            self.assertAlmostEqual((window_kernel(d+e)-window_kernel(d-e))/(2*e),kernel_prime(d),places=9)
        for p in (-6.9,-6.7,-6.5,-6.2):
            for q in (-6.95,-6.75,-6.4,-6.1):
                self.assertAlmostEqual(commutator_kernel(p,q),commutator_kernel(q,p),places=12)

    def test_commutator_kernel_matches_integrated_action(self):
        # Check [E,iA]f by integration-by-parts vs explicit kernel. The flow
        # vanishes at endpoints; quadrature is a control, not an operator proof.
        n=600;p=samples(n);delta=1/n
        f=lambda x: math.sin(math.pi*(x+7))+.3*math.sin(3*math.pi*(x+7))
        df=lambda x: math.pi*math.cos(math.pi*(x+7))+.9*math.pi*math.cos(3*math.pi*(x+7))
        for x in (-6.9,-6.6,-6.3):
            direct=sum((window_kernel(x-y)*(bump(y)*df(y)+.5*bump_prime(y)*f(y))
                       - (bump(x)*kernel_prime(x-y)+.5*bump_prime(x)*window_kernel(x-y))*f(y))
                       *delta for y in p)
            kernel=sum(commutator_kernel(x,y)*f(y)*delta for y in p)
            self.assertAlmostEqual(direct,kernel,places=8)

    def test_free_middle_interval_lower_bound(self):
        # T preimage p in [-6.8,-6.2] lies away from endpoints and v>0.
        vals=[-bump(x)*x/3 for x in samples(4000) if -6.8<=x<=-6.2]
        self.assertGreater(min(vals),.2)

if __name__=='__main__':unittest.main()
