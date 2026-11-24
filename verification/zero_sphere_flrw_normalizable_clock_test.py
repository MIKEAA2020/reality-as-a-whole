"""Normalizable positive-p_phi FLRW packet with the sphere-record clock.

Continuum model and physical norm are defined analytically; Simpson rules
check selected integrals, and full finite sphere states are evaluated at
sample momenta. This is not an inhomogeneous or full GR quantization.
"""
import cmath
import math
import unittest

from verification.zero_five_ray_record_current_unification_test import (
    joint_state, probabilities, local_density, norm2
)
from verification.zero_sphere_mismatch_experience_comparison_test import subject_density
from verification.zero_sphere_relativistic_relational_time_test import (
    initial, advance, ymean, zmean, components
)
from verification.zero_spin_constitution_test import close, inner

LEFT, RIGHT = -7.0, -6.0


def weight(p):
    if not LEFT <= p <= RIGHT:
        return 0.0
    u = p - LEFT
    return 30.0 * u*u * (1-u)*(1-u)


def packet(p):
    if not LEFT <= p <= RIGHT:
        return 0.0
    u = p - LEFT
    return math.sqrt(30) * u * (1-u)


def packet_derivative(p):
    return math.sqrt(30) * (1-2*(p-LEFT))


def omega(p, h):
    return math.sqrt(p*p/6 - 2*h)


def velocity(p, h):
    return -p/(6*omega(p, h))


def integrate(fn, n=1200):
    assert n % 2 == 0
    dx = (RIGHT-LEFT)/n
    return dx/3 * sum((1 if j in (0, n) else 4 if j % 2 else 2) *
                      fn(LEFT+j*dx) for j in range(n+1))


def avg(fn, n=1200):
    return integrate(lambda p: weight(p)*fn(p), n)


def coherence(t, n=1200):
    return avg(lambda p: cmath.exp(1j*(omega(p, 0)-omega(p, 1))*t), n)


def p_from_scalar_momentum(s, h):
    return -math.sqrt(6*s*s+12*h)


def dp_ds(s, h):
    return 6*s/abs(p_from_scalar_momentum(s,h))


def alpha_clock_coherence(alpha, n=1200):
    # Overlap of the two h-dependent scalar-momentum supports.
    lo,hi=math.sqrt(6),math.sqrt(37/6)
    dx=(hi-lo)/n
    def value(s):
        p0,p1=p_from_scalar_momentum(s,0),p_from_scalar_momentum(s,1)
        amplitude=math.sqrt(dp_ds(s,0)*dp_ds(s,1))*packet(p0)*packet(p1)
        return amplitude*cmath.exp(-1j*(abs(p0)-abs(p1))*alpha)
    return dx/3*sum((1 if j in (0,n) else 4 if j%2 else 2)*value(lo+j*dx)
                    for j in range(n+1))


def energy_spectrum(p):
    # The unused complement follows the prior finite embedding, h=1/2.
    return tuple(-omega(p, h) for h in (0, 1, .5))


def normalized(matrix, norm):
    return [[x/norm for x in row] for row in matrix]


class FLRWNormalizableClockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.triple = joint_state('triple')
        cls.pair = joint_state('pair')
        cls.v = initial(cls.triple)
        cls.vp = initial(cls.pair)

    def test_packet_normalization_and_endpoint_domain(self):
        self.assertAlmostEqual(integrate(lambda p: packet(p)**2), 1, places=10)
        self.assertEqual(packet(LEFT), 0)
        self.assertEqual(packet(RIGHT), 0)
        # Weak derivative is square integrable: packet in the H^1 domain.
        self.assertAlmostEqual(integrate(lambda p: packet_derivative(p)**2), 10)
        for p in (-7, -6.5, -6):
            for h in (0, .5, 1):
                self.assertGreater(p*p/6-2*h, 0)
                self.assertAlmostEqual(-p*p/12+omega(p,h)**2/2+h, 0)

    def test_positive_branch_kg_inner_product_and_unitarity(self):
        # Coefficients of the covariantly normalized KG modes are f/sqrt(2w).
        # The selected KG sign for p_phi>0 supplies the factor 2w.
        for t in (0, 10, 100):
            def term(p, h):
                a = packet(p)*cmath.exp(1j*omega(p,h)*t)/math.sqrt(2*omega(p,h))
                return 2*omega(p,h)*abs(a)**2
            self.assertAlmostEqual(avg(lambda p: 1), 1, places=10)
            for h in (0,1):
                self.assertAlmostEqual(integrate(lambda p: term(p,h)), 1, places=10)
        for p in (-6.9,-6.5,-6.1):
            for h in (0,1):
                e = -omega(p,h)
                self.assertAlmostEqual(e*e-p*p/6+2*h, 0)
                self.assertGreater(omega(p,h), 0)

    def test_rotor_action_hamiltonian_and_spectrum(self):
        # L_X=I a^3 dot(X)^2/(2N), P_X=I a^3 dot(X)/N;
        # N=1, a=2, dot(X)=3, I=1/2, then Legendre transform.
        a, inertia, n, dotx = 2, .5, 1, 3
        momentum = inertia*a**3*dotx/n
        lagrangian = inertia*a**3*dotx**2/(2*n)
        hamiltonian = momentum*dotx-lagrangian
        self.assertAlmostEqual(hamiltonian, n*momentum**2/(2*inertia*a**3))
        self.assertEqual([j*j/(2*inertia) for j in (0,1)], [0,1])
        self.assertGreater(4/(2*inertia), 36/12)  # n=2 not on this real branch

    def test_logical_components_are_balanced_and_unitary(self):
        a,b,c=components(self.v)
        self.assertAlmostEqual(norm2(a), .5)
        self.assertAlmostEqual(norm2(b), .5)
        self.assertAlmostEqual(norm2(c), 0)
        self.assertAlmostEqual(abs(inner(a,b)), 0)
        for p,t in ((-6.9,0),(-6.5,10),(-6.1,100)):
            v = advance(self.v,t,energy_spectrum(p))
            self.assertAlmostEqual(norm2(v), 1)
            delta=omega(p,0)-omega(p,1)
            self.assertAlmostEqual(ymean(v),math.cos(delta*t))
            self.assertAlmostEqual(zmean(v),math.sin(delta*t))

    def test_packet_constraint_terms_cancel_as_expectations(self):
        grav = avg(lambda p: -p*p/12)
        scalar = avg(lambda p: (omega(p,0)**2+omega(p,1)**2)/4)
        internal = .5
        self.assertAlmostEqual(grav, -74/21, places=10)
        self.assertAlmostEqual(scalar, 127/42, places=10)
        self.assertAlmostEqual(grav+scalar+internal, 0, places=10)
        # Equal opposite reallocations leave the very same constraint operator.
        for offset in (-2.5, .25, 3):
            self.assertAlmostEqual((grav-offset)+scalar+(internal+offset),0)

    def test_packet_clock_signal_and_purity(self):
        expected = {0: 1.0, 10: .9901109916300225,
                    50: .7748784038346918, 100: .3242863864920011,
                    200: .04145091846110285}
        for t, value in expected.items():
            c=coherence(t)
            self.assertAlmostEqual(abs(c), value, places=8)
            self.assertLessEqual(abs(c), 1.000000001)
            self.assertAlmostEqual((1+abs(c)**2)/2,
                                   .5+.5*(c.real*c.real+c.imag*c.imag))
        self.assertGreater(1-abs(coherence(100))**2, .89)

    def test_quadrature_numerical_convergence(self):
        for t in (10, 50, 100, 200):
            self.assertLess(abs(coherence(t,600)-coherence(t,1200)), 1e-8)
            self.assertLess(abs(coherence(t,1200)-coherence(t,2400)), 1e-9)

    def test_geometry_rate_backreaction_and_spread(self):
        v0=avg(lambda p: velocity(p,0))
        v1=avg(lambda p: velocity(p,1))
        self.assertAlmostEqual(v0, 1/math.sqrt(6), places=10)
        self.assertAlmostEqual(v1, .48281686991035977, places=10)
        self.assertAlmostEqual(100*(v1-v0), 7.456857944649808, places=8)
        variance=avg(lambda p:velocity(p,1)**2)-v1*v1
        self.assertAlmostEqual(variance, 3.1641408191368514e-5, places=10)
        self.assertGreater(variance, 0)
        # At t=0 an unchirped real packet has <alpha>=0, <alpha²>=10.
        # In a branch alpha(t)=alpha+t*v(p), so Var(alpha)=10+t² Var(v).
        self.assertAlmostEqual(10+100**2*variance, 10.3164140819, places=8)

    def test_hamiltonian_velocity_is_derivative(self):
        for p in (-6.9,-6.5,-6.1):
            for h in (0,1):
                eps=1e-5
                derivative=(-omega(p+eps,h)+omega(p-eps,h))/(2*eps)
                self.assertAlmostEqual(derivative,velocity(p,h), places=9)

    def test_sphere_record_and_full_confined_state_persist_pointwise(self):
        rho=subject_density(self.triple)
        expected=probabilities(self.triple)
        for p in (-6.9,-6.5,-6.1):
            for t in (0,10,100):
                v=advance(self.v,t,energy_spectrum(p))
                close(self,normalized(subject_density(v),norm2(v)),rho)
                table=probabilities(v)
                for key in expected:
                    self.assertAlmostEqual(table[key],expected[key])
        # Since equality holds for all phases in this state family, the
        # normalized momentum integral has the same marginal by linearity.

    def test_sphere_marginal_is_phase_independent_on_active_circle(self):
        # Four phases determine both quadratures of the cross term in a
        # two-eigenvalue system. Equality at these phases proves that the
        # confined marginal is constant over every phase in this orbit.
        p=-6.5
        gap=omega(p,0)-omega(p,1)
        expected=subject_density(self.triple)
        table=probabilities(self.triple)
        for phase in (0,math.pi/2,math.pi,3*math.pi/2):
            v=advance(self.v,phase/gap,energy_spectrum(p))
            close(self,subject_density(v),expected)
            actual=probabilities(v)
            for key in table: self.assertAlmostEqual(actual[key],table[key])
            # Equality of receiver states at the four phases likewise checks
            # its constant, sine and cosine coefficients for both contexts.
            vp=advance(self.vp,phase/gap,energy_spectrum(p))
            close(self,local_density(v),local_density(vp))

    def test_receiver_state_and_physical_clock_coherence_control(self):
        for p in (-6.9,-6.5,-6.1):
            for t in (0,10,100):
                close(self,local_density(advance(self.v,t,energy_spectrum(p))),
                      local_density(advance(self.vp,t,energy_spectrum(p))))
        # A matched incoherent mixture of h eigenstates has zero Y and Z at
        # all times, unlike the pure coherent preparation at t=0 and t=100.
        a,b,_=components(self.v)
        for p in (-6.9,-6.5,-6.1):
            for t in (0,100):
                aa=advance(a,t,energy_spectrum(p))
                bb=advance(b,t,energy_spectrum(p))
                self.assertAlmostEqual(ymean(aa),0)
                self.assertAlmostEqual(ymean(bb),0)
                self.assertAlmostEqual(zmean(aa),0)
                self.assertAlmostEqual(zmean(bb),0)
        self.assertGreater(abs(coherence(100)), .3)

    def test_geometric_clock_switch_unitary_jacobian_and_constraint(self):
        # Direct change-of-variable in each h sector, not a re-preparation.
        for h in (0,1):
            for p in (-6.9,-6.5,-6.1):
                s=omega(p,h)
                self.assertAlmostEqual(p_from_scalar_momentum(s,h),p)
                eps=1e-5
                jac=(p_from_scalar_momentum(s+eps,h)-p_from_scalar_momentum(s-eps,h))/(2*eps)
                self.assertAlmostEqual(abs(jac),dp_ds(s,h),places=8)
                self.assertAlmostEqual(-p*p/12+s*s/2+h,0)
            lo=omega(-6,h); hi=omega(-7,h); n=1200; dx=(hi-lo)/n
            def integrand(s):
                p=p_from_scalar_momentum(s,h)
                return dp_ds(s,h)*packet(p)**2
            norm=dx/3*sum((1 if j in (0,n) else 4 if j%2 else 2)*integrand(lo+j*dx)
                          for j in range(n+1))
            self.assertAlmostEqual(norm,1,places=10)

    def test_transport_same_qubit_observable_across_clock_representations(self):
        # Y on the phi=0 data has off-diagonal entries -i and +i.
        # WYW† connects *different* scalar momenta s_h(p) in its two rows.
        n=1200
        def contribution(h):
            lo,hi=omega(-6,h),omega(-7,h); dx=(hi-lo)/n
            def value(s):
                p=p_from_scalar_momentum(s,h)
                other=1-h
                s_other=omega(p,other)
                j_here,j_other=dp_ds(s,h),dp_ds(s_other,other)
                here=(1 if h==0 else 1j)*math.sqrt(j_here)*packet(p)/math.sqrt(2)
                there=(1j if h==0 else 1)*math.sqrt(j_other)*packet(p)/math.sqrt(2)
                transported=( -1j if h==0 else 1j)*math.sqrt(j_here/j_other)*there
                return here.conjugate()*transported
            return dx/3*sum((1 if j in (0,n) else 4 if j%2 else 2)*value(lo+j*dx)
                            for j in range(n+1))
        self.assertAlmostEqual((contribution(0)+contribution(1)).real,1,places=10)
        self.assertAlmostEqual((contribution(0)+contribution(1)).imag,0,places=10)
        self.assertLess(abs(alpha_clock_coherence(0)),.003)

    def test_alpha_and_scalar_clock_slices_are_different_conditionings(self):
        # These are different clock surfaces in the same physical state.
        # A common physical observable must be transported, not identified
        # by comparing the two reduced qubit operators without transformation.
        self.assertAlmostEqual(abs(coherence(0)),1)
        self.assertAlmostEqual(abs(alpha_clock_coherence(0)),.0021176937939937526,places=10)
        self.assertAlmostEqual(abs(alpha_clock_coherence(100)),.002054735468190868,places=10)
        self.assertLess(abs(alpha_clock_coherence(100,600)-alpha_clock_coherence(100,1200)),1e-10)

    def test_energy_shift_is_physical_if_constraint_is_held_fixed(self):
        # Shifting the h spectrum without changing C is not a mere phase gauge:
        # it changes the square root and eventually the allowed sector.
        p=-6.5
        old=omega(p,1)-omega(p,0)
        shifted=omega(p,2)-omega(p,1)
        self.assertNotAlmostEqual(old,shifted)
        self.assertLess(p*p/6-2*4,0)

if __name__ == '__main__':
    unittest.main()
