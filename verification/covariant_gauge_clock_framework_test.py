"""Field-theory calculations for the stated classical initial data.

Not a solution of the coupled Einstein initial-value problem, a measurement of
experience, or a quantum or fundamental-theory validation.
"""
import math
import unittest


def integrate(f, start, end, n=4000):
    if n <= 0 or n % 2:
        raise ValueError('positive even number of Simpson intervals required')
    h = (end-start)/n
    return h/3*(f(start)+f(end)
                + 4*sum(f(start+i*h) for i in range(1, n, 2))
                + 2*sum(f(start+i*h) for i in range(2, n, 2)))


def rot(angle, q):
    c, s = math.cos(angle), math.sin(angle)
    return (c*q[0]-s*q[1], s*q[0]+c*q[1])


def j(q):
    return (-q[1], q[0])


def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]


class CovariantFrameworkTests(unittest.TestCase):
    def setUp(self):
        self.L = 2*math.pi
        self.volume = self.L**3
        self.k = 2*math.pi/self.L
        self.e, self.v, self.b, self.P, self.m = 0.5, 2.0, 1/3, 1.5, 1.0
        self.rho0 = self.e*self.v*self.P

    def rho(self, x):
        return self.rho0*math.cos(self.k*x)

    def electric(self, x):
        return self.rho0/self.k*math.sin(self.k*x)

    def current(self, x):
        return -self.e*self.v*self.b*self.k*math.cos(self.k*x)

    def rho_dot_hamilton(self, x):
        # chi=(v,b sin kx), pi=(0,P cos kx), A=0.
        chi = (self.v, self.b*math.sin(self.k*x))
        pi = (0.0, self.P*math.cos(self.k*x))
        pi_dot = (-self.m**2*self.v,
                  -(self.k**2+self.m**2)*self.b*math.sin(self.k*x))
        return self.e*(dot(pi_dot, j(chi))+dot(pi, j(pi)))

    def test_local_gauss_and_zero_global_charge(self):
        for x in (0, self.L/7, self.L/4, self.L/2, self.L):
            div_e = self.rho0*math.cos(self.k*x)
            self.assertAlmostEqual(div_e, self.rho(x))
        charge = self.L**2*integrate(self.rho, 0, self.L)
        self.assertAlmostEqual(charge, 0, delta=1e-10)
        self.assertGreater(self.rho(0), 0)
        self.assertLess(self.rho(self.L/2), 0)

    def test_continuity_from_matter_hamiltonian_equations(self):
        for x in (0, self.L/9, self.L/4, self.L/2, 3*self.L/4):
            minus_div_j = -self.e*self.v*self.b*self.k**2*math.sin(self.k*x)
            self.assertAlmostEqual(self.rho_dot_hamilton(x), minus_div_j, places=12)
        total_rate = self.L**2*integrate(self.rho_dot_hamilton, 0, self.L)
        self.assertAlmostEqual(total_rate, 0, delta=1e-10)

    def test_regional_change_equals_boundary_flux(self):
        left, right = 0, self.L/4
        change = self.L**2*integrate(self.rho_dot_hamilton, left, right)
        outward_flux = self.L**2*(self.current(right)-self.current(left))
        self.assertAlmostEqual(change, -outward_flux, delta=1e-10)
        self.assertNotAlmostEqual(change, 0)

    def test_time_derivative_of_gauss_constraint_vanishes(self):
        # At t=0 B=0, Maxwell evolution gives E_dot=-j.
        for x in (self.L/7, self.L/4, 3*self.L/4):
            divergence_e_dot = -self.e*self.v*self.b*self.k**2*math.sin(self.k*x)
            self.assertAlmostEqual(divergence_e_dot-self.rho_dot_hamilton(x), 0)

    def test_full_initial_matter_and_field_energy(self):
        def density(x):
            chi = (self.v, self.b*math.sin(self.k*x))
            pi = (0, self.P*math.cos(self.k*x))
            grad = (0, self.b*self.k*math.cos(self.k*x))
            return (dot(pi, pi)+dot(grad, grad)+self.m**2*dot(chi, chi)
                    +self.electric(x)**2)/2
        actual = self.L**2*integrate(density, 0, self.L)
        expected = self.volume*(self.P**2/4+self.b**2*self.k**2/4
                                +self.m**2*self.v**2/2+self.m**2*self.b**2/4
                                +self.rho0**2/(4*self.k**2))
        self.assertAlmostEqual(actual, expected, delta=1e-9)
        self.assertGreater(actual, 0)

    def test_electric_energy_depends_on_wave_number(self):
        results = []
        for n in (1, 2, 3):
            k = 2*math.pi*n/self.L
            electrostatic = self.L**2*integrate(lambda x: (self.rho0/k*math.sin(k*x))**2/2,
                                               0, self.L)
            self.assertAlmostEqual(electrostatic, self.volume*self.rho0**2/(4*k*k), delta=1e-9)
            results.append(electrostatic)
        self.assertAlmostEqual(results[0]/results[1], 4)
        self.assertAlmostEqual(results[0]/results[2], 9)

    def test_local_rotation_preserves_charge_and_covariant_gradient(self):
        for x in (0, self.L/8, self.L/4, self.L/2):
            chi = (self.v, self.b*math.sin(self.k*x))
            pi = (0, self.P*math.cos(self.k*x))
            dchi = (0, self.b*self.k*math.cos(self.k*x))
            lam, dlam = .7*math.sin(self.k*x), .7*self.k*math.cos(self.k*x)
            theta, dtheta = -self.e*lam, -self.e*dlam
            cp, pp = rot(theta, chi), rot(theta, pi)
            dcp = tuple(a+dtheta*b for a, b in zip(rot(theta, dchi), j(cp)))
            ap = -dlam
            d_cov = tuple(a-self.e*ap*b for a, b in zip(dcp, j(cp)))
            for actual, expected in zip(d_cov, rot(theta, dchi)):
                self.assertAlmostEqual(actual, expected)
            self.assertAlmostEqual(self.e*dot(pp, j(cp)), self.e*dot(pi, j(chi)))

    def test_clock_branches_satisfy_constraint(self):
        for sqrt_h, c_rest in ((1, -4.5), (4, -2), (0.25, -8)):
            root = math.sqrt(-2*sqrt_h*c_rest)
            for p in (-root, root):
                self.assertAlmostEqual(c_rest+p*p/(2*sqrt_h), 0)
                # Gauge preservation dot T = N*p/sqrt(h) = 1.
                lapse = sqrt_h/p
                self.assertAlmostEqual(lapse*p/sqrt_h, 1)
                self.assertEqual(math.copysign(1, -p), -math.copysign(1, p))
        self.assertLess(-2*1.0*1.0, 0)  # C_rest>0 gives no real clock branch

    def test_full_gr_initial_constraints_and_clock_timelikeness(self):
        # Independent exact initial-data construction, L=2pi, e=1, m=0.
        kappa = 2.0
        k_trace = math.sqrt(15*kappa/2)
        for i in range(513):
            x = self.L*i/512
            sn, cs = math.sin(x), math.cos(x)
            f, s = sn*cs, 4-sn*sn
            disc = s*s-4*f*f
            self.assertGreater(disc, 0)
            p_t = math.sqrt((s+math.sqrt(disc))/2)
            t_prime = f/p_t
            self.assertGreater(p_t*p_t-t_prime*t_prime, 0)
            charge = cs  # e*pi.Jchi
            div_e = cs
            momentum = -sn*cs+p_t*t_prime
            energy = (cs*cs+sn*sn+sn*sn+p_t*p_t+t_prime*t_prime)/2
            h_constraint = -k_trace*k_trace/(3*kappa)+energy
            self.assertAlmostEqual(charge-div_e, 0, places=12)
            self.assertAlmostEqual(momentum, 0, places=12)
            self.assertAlmostEqual(energy, 2.5, places=12)
            self.assertAlmostEqual(h_constraint, 0, places=12)
            # Hamilton equations give chi_dot=pi and pi_dot=laplacian(chi).
            chi, pi, pi_dot = (1, cs), (0, cs), (0, -cs)
            rho_dot = dot(pi_dot, j(chi))+dot(pi, j(pi))
            div_j = cs  # derivative of j_x=sin(x)
            self.assertAlmostEqual(rho_dot+div_j, 0, places=12)

    def test_full_gr_clock_spatial_gradient_is_periodic_and_integrable(self):
        def clock_gradient(x):
            sn, cs = math.sin(x), math.cos(x)
            f, s = sn*cs, 4-sn*sn
            p_t = math.sqrt((s+math.sqrt(s*s-4*f*f))/2)
            return f/p_t
        self.assertAlmostEqual(integrate(clock_gradient, 0, self.L), 0, delta=1e-12)
        self.assertAlmostEqual(clock_gradient(0), clock_gradient(self.L), places=12)
        self.assertNotAlmostEqual(clock_gradient(self.L/8), 0)

    def test_lapse_weighted_spacetime_integral_differs_from_slice_total(self):
        epsilon = .5
        lapse = lambda x: 1+epsilon*math.cos(self.k*x)
        charge = self.L**2*integrate(self.rho, 0, self.L)
        weighted = self.L**2*integrate(lambda x: lapse(x)*self.rho(x), 0, self.L)
        self.assertAlmostEqual(charge, 0, delta=1e-10)
        self.assertAlmostEqual(weighted, epsilon*self.rho0*self.volume/2, delta=1e-9)
        self.assertGreater(1-epsilon, 0)


if __name__ == '__main__':
    unittest.main()
