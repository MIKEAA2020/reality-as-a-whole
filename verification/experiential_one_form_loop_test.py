"""Line-integral controls, not experiential or physical measurements."""
import math
import unittest


def simpson(f, a, b, n=4096):
    if n <= 0 or n % 2:
        raise ValueError('n must be a positive even integer')
    h = (b-a)/n
    return h/3*(f(a)+f(b) + 4*sum(f(a+i*h) for i in range(1, n, 2))
                + 2*sum(f(a+i*h) for i in range(2, n, 2)))


def one_form_a(x, y):
    return -y/2, x/2+2


def one_form_b(x, y):
    return y/2+3, -x/2


def one_form_c(x, y):
    return 3-y/2, x/2


def top_form(x, y):
    r2 = x*x+y*y
    if not r2:
        raise ValueError('punctured plane excludes origin')
    return -y/r2, x/r2


def pullback(form, x, y, dx, dy):
    p, q = form(x, y)
    return p*dx+q*dy


def circle(form, theta, radius=1, cx=0, cy=0):
    x = cx+radius*math.cos(theta)
    y = cy+radius*math.sin(theta)
    return pullback(form, x, y, -radius*math.sin(theta), radius*math.cos(theta))


class OneFormLoopTests(unittest.TestCase):
    def test_two_histories_are_opposite_but_nonzero(self):
        qa = simpson(lambda t: circle(one_form_a, t), 0, 2*math.pi)
        qb = simpson(lambda t: circle(one_form_b, t), 0, 2*math.pi)
        self.assertAlmostEqual(qa, math.pi, places=11)
        self.assertAlmostEqual(qb, -math.pi, places=11)
        self.assertAlmostEqual(qa+qb, 0, places=11)
        self.assertGreater(circle(one_form_a, 0), 0)
        self.assertLess(circle(one_form_a, math.pi), 0)
        self.assertLess(circle(one_form_b, math.pi/2), 0)
        self.assertGreater(circle(one_form_b, 3*math.pi/2), 0)

    def test_sum_is_exact_at_multiple_points(self):
        for x, y in ((0, 0), (1, 2), (-4, 7), (0.1, -0.3)):
            a, b = one_form_a(x, y), one_form_b(x, y)
            self.assertAlmostEqual(a[0]+b[0], 3)
            self.assertAlmostEqual(a[1]+b[1], 2)

    def test_open_path_integral_is_endpoint_potential_difference(self):
        # z(t)=(t², t³), 0 to 2; Phi=3x+2y.
        def combined(t):
            x, y, dx, dy = t*t, t**3, 2*t, 3*t*t
            return pullback(one_form_a, x, y, dx, dy)+pullback(one_form_b, x, y, dx, dy)
        self.assertAlmostEqual(simpson(combined, 0, 2), 3*4+2*8, places=11)

    def test_three_history_reciprocal_network(self):
        # T12=C, T13=2C, T23=4C; C=(-y dx+x dy)/2.
        # Exact pieces dPhi are dx, dy, and d(xy), respectively.
        def s1(x, y):
            return 1-3*y/2, 3*x/2
        def s2(x, y):
            return -3*y/2, 1+3*x/2
        def s3(x, y):
            return y+3*y, x-3*x
        for x, y in ((0, 0), (1, 2), (-1, .5)):
            components = [f(x, y) for f in (s1, s2, s3)]
            self.assertAlmostEqual(sum(c[0] for c in components), 1+y)
            self.assertAlmostEqual(sum(c[1] for c in components), 1+x)
        totals = [simpson(lambda t: circle(f, t), 0, 2*math.pi) for f in (s1, s2, s3)]
        for total, multiple in zip(totals, (3, 3, -6)):
            self.assertAlmostEqual(total, multiple*math.pi, places=10)
        self.assertAlmostEqual(sum(totals), 0, places=10)

    def test_relative_subject_weight_changes_result(self):
        qa = simpson(lambda t: circle(one_form_a, t), 0, 2*math.pi)
        qb = simpson(lambda t: circle(one_form_b, t), 0, 2*math.pi)
        self.assertAlmostEqual(2*qa+qb, math.pi, places=11)

    def test_nonexact_closed_state_path_and_both_signs(self):
        self.assertAlmostEqual(simpson(lambda t: circle(one_form_c, t), 0, 2*math.pi), math.pi, places=11)
        self.assertLess(circle(one_form_c, math.pi/2), 0)
        self.assertGreater(circle(one_form_c, 3*math.pi/2), 0)
        # General circle has circulation pi*r²: Green's theorem for curl=1.
        self.assertAlmostEqual(simpson(lambda t: circle(one_form_c, t, 2), 0, 2*math.pi), 4*math.pi, places=10)

    def test_punctured_plane_topological_period(self):
        self.assertAlmostEqual(simpson(lambda t: circle(top_form, t), 0, 2*math.pi), 2*math.pi, places=11)
        self.assertAlmostEqual(simpson(lambda t: circle(top_form, t, .5, 2), 0, 2*math.pi), 0, places=11)
        with self.assertRaises(ValueError):
            top_form(0, 0)
        # Numerically verify Q_x-P_y=0 away from the puncture.
        h = 1e-5
        for x, y in ((1, 1), (2, -1), (-.5, 1)):
            qx = (top_form(x+h, y)[1]-top_form(x-h, y)[1])/(2*h)
            py = (top_form(x, y+h)[0]-top_form(x, y-h)[0])/(2*h)
            self.assertAlmostEqual(qx-py, 0, delta=1e-9)

    def test_smooth_reparameterization_preserves_both_integrals(self):
        # theta=lambda+0.3 sin(lambda) is strictly increasing, fixes endpoints.
        for form, expected in ((one_form_a, math.pi), (one_form_b, -math.pi)):
            def f(lam):
                theta = lam+0.3*math.sin(lam)
                return circle(form, theta)*(1+0.3*math.cos(lam))
            self.assertAlmostEqual(simpson(f, 0, 2*math.pi), expected, places=10)

    def test_opposite_orientation_reverses_period(self):
        self.assertAlmostEqual(simpson(lambda t: circle(one_form_a, t), 2*math.pi, 0), -math.pi, places=11)

    def test_infinite_repetitions_do_not_define_cutoff_limit(self):
        def total(l):
            return math.cos(l)-1
        for n in range(1, 10):
            self.assertAlmostEqual(total(2*math.pi*n), 0)
            self.assertAlmostEqual(total((2*n+1)*math.pi), -2)


if __name__ == '__main__':
    unittest.main()
