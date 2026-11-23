import itertools
import math
import unittest


def wedge(a,b): return a[0]*b[1]-a[1]*b[0]


def cross_ratio(points):
    if len(points)!=4 or any(wedge(points[i],points[j])==0 for i in range(4) for j in range(i+1,4)):
        raise ValueError('four distinct nonzero projective rays required')
    a,b,c,d=points
    return wedge(a,b)*wedge(c,d)/(wedge(a,c)*wedge(b,d))


def chirality(points):
    x=cross_ratio(points)
    return x.imag/(1+abs(x)**2+abs(1-x)**2)


def transform(m,p): return (m[0][0]*p[0]+m[0][1]*p[1],m[1][0]*p[0]+m[1][1]*p[1])


def parity(p):
    inversions=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return (-1)**inversions


class IntrinsicSphereOrientationTests(unittest.TestCase):
    def setUp(self): self.points=[(0j,1),(1,1),(2,1),(1j,1)]

    def test_exact_example_and_mobius_invariance(self):
        self.assertAlmostEqual(cross_ratio(self.points),.75+.25j)
        self.assertAlmostEqual(chirality(self.points),1/7)
        m=((2,1),(1,1))
        transformed=[transform(m,p) for p in self.points]
        self.assertAlmostEqual(cross_ratio(transformed),cross_ratio(self.points))
        self.assertAlmostEqual(chirality(transformed),chirality(self.points))

    def test_all_24_permutations_alternate(self):
        original=chirality(self.points)
        for p in itertools.permutations(range(4)):
            self.assertAlmostEqual(chirality([self.points[i] for i in p]),parity(p)*original)

    def test_projective_scalings_and_infinity(self):
        pts=[(0,1),(1,1),(1,0),(1j,1)]
        scaled=[(c*p[0],c*p[1]) for c,p in zip([2,1j,3-1j,-4],pts)]
        self.assertAlmostEqual(cross_ratio(pts),cross_ratio(scaled))
        self.assertAlmostEqual(chirality(pts),chirality(scaled))

    def test_orientation_reverse_and_cocircular_zero(self):
        conjugates=[(a.conjugate(),complex(b).conjugate()) for a,b in self.points]
        self.assertAlmostEqual(chirality(conjugates),-chirality(self.points))
        real=[(z,1) for z in [0,1,2,3]]
        self.assertEqual(chirality(real),0)

    def test_bound_and_equilateral_maximum(self):
        x=complex(.5,math.sqrt(3)/2)
        y=x.imag/(1+abs(x)**2+abs(1-x)**2)
        self.assertAlmostEqual(y,math.sqrt(3)/6)
        for a in range(-5,6):
            for b in range(-5,6):
                z=complex(a/3,b/3)
                y=z.imag/(1+abs(z)**2+abs(1-z)**2)
                self.assertLessEqual(abs(y),math.sqrt(3)/6+1e-14)

    def test_sign_pair_does_not_determine_intensity_or_incidence(self):
        a=chirality(self.points)
        self.assertAlmostEqual((1/3)*2*a+(2/3)*(-a),0)
        self.assertNotAlmostEqual(a,a**3)
        self.assertNotAlmostEqual(a,-a)

    def test_invalid_configuration_rejected(self):
        with self.assertRaises(ValueError): cross_ratio(self.points[:3])
        with self.assertRaises(ValueError): cross_ratio(self.points[:3]+[self.points[0]])
        with self.assertRaises(ValueError): cross_ratio([(0,0)]+self.points[1:])


if __name__=='__main__': unittest.main()
