"""Exact algebraic controls for the sphere, Satake interface and line lattices.

These tests do not prove geometric Satake, an interacting S-duality, or the
physical origin of any carrier. Exact sphere averages use the standard round
product measure and the polynomial moment formula for independent spheres.
"""
from fractions import Fraction as F
from itertools import permutations, product
import math
import unittest

N=9
ZERO=(0,)*N

def add(a,b):
    out=dict(a)
    for k,v in b.items():out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}

def scale(a,c):return {k:v*c for k,v in a.items() if v*c}

def mul(a,b):
    out={}
    for x,v in a.items():
        for y,w in b.items():
            k=tuple(i+j for i,j in zip(x,y))
            out[k]=out.get(k,F(0))+v*w
    return {k:v for k,v in out.items() if v}

def var(i,j):
    k=[0]*N;k[3*i+j]=1
    return {tuple(k):F(1)}

def dot(i,j):
    r={}
    for a in range(3):r=add(r,mul(var(i,a),var(j,a)))
    return r

def chirality():
    r={}
    for p in permutations(range(3)):
        sign=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        term={ZERO:F(sign)}
        for i in range(3):term=mul(term,var(i,p[i]))
        r=add(r,term)
    return r

def double_factorial(n):
    v=1
    for i in range(n,0,-2):v*=i
    return v

def sphere_moment(powers):
    if any(p%2 for p in powers):return F(0)
    return F(math.prod(double_factorial(p-1) for p in powers),
             double_factorial(sum(powers)+1))

def average(poly):
    return sum((v*math.prod(sphere_moment(k[i:i+3]) for i in (0,3,6))
                for k,v in poly.items()),F(0))

def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dotv(a,b):return sum(x*y for x,y in zip(a,b))
def tvalue(a,b,c):return dotv(a,cross(b,c))

def lattice(name,e,m):
    if name=='SU2':return m%2==0
    if name=='SO3+':return e%2==0
    if name=='SO3-':return (e+m)%2==0
    raise ValueError(name)

def s(e,m):return m,-e
def pairing(a,b):return a[0]*b[1]-a[1]*b[0]

class SphereSatakeSymmetryTests(unittest.TestCase):
    def test_two_sphere_normalized_singlet_moments(self):
        u=dot(0,1);u2=mul(u,u)
        self.assertEqual(average(u),0)
        self.assertEqual(average(u2),F(1,3))
        self.assertEqual(average(mul(u2,u2)),F(1,5))
        self.assertEqual(3*average(u2),1)
        self.assertEqual(3*average(mul(u2,u2)),F(3,5))

    def test_exact_three_direction_gram_identity_on_unit_spheres(self):
        x,y,z=dot(0,1),dot(1,2),dot(2,0);t=chirality()
        # We check the quotient identity in expectation of its square. Since
        # the real integrand is nonnegative, zero also verifies the identity
        # almost everywhere; the analytic determinant identity holds pointwise.
        gram=add({ZERO:F(1)},scale(mul(mul(x,y),z),2))
        for p in (x,y,z):gram=add(gram,scale(mul(p,p),-1))
        residual=add(mul(t,t),scale(gram,-1))
        self.assertEqual(average(mul(residual,residual)),0)
        self.assertEqual(average(t),0)
        self.assertEqual(average(mul(t,t)),F(2,9))
        self.assertEqual(average(mul(mul(t,t),mul(t,t))),F(8,75))

    def test_handed_states_have_exact_norm_and_odd_expectations(self):
        t=chirality();one={ZERO:F(1)}
        plus=add(one,scale(t,F(1,2)));minus=add(one,scale(t,F(-1,2)))
        self.assertEqual(average(mul(plus,plus)),F(19,18))
        self.assertEqual(average(mul(minus,minus)),F(19,18))
        self.assertEqual(average(mul(mul(plus,plus),t))/F(19,18),F(4,19))
        self.assertEqual(average(mul(mul(minus,minus),t))/F(19,18),F(-4,19))
        self.assertEqual(average(mul(plus,minus))/F(19,18),F(17,19))

    def test_same_gram_opposite_chirality_no_proper_rotation(self):
        a=(1,0,0);b=(0,1,0);c=(0,0,1);mirror=(0,0,-1)
        self.assertEqual([dotv(a,b),dotv(b,c),dotv(c,a)],
                         [dotv(a,b),dotv(b,mirror),dotv(mirror,a)])
        self.assertEqual((tvalue(a,b,c),tvalue(a,b,mirror)),(1,-1))
        # A proper orthogonal transformation preserves the determinant, so
        # these two triples cannot lie in the same SO(3) orbit.

    def test_pseudoscalar_is_trivial_rep_inside_three_vectors(self):
        # epsilon_ijk R_ia R_jb R_kc = det(R) epsilon_abc, tested on every
        # signed permutation matrix and all tensor indices.
        for perm in permutations(range(3)):
            parity=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
            for signs in product((-1,1),repeat=3):
                det=parity*math.prod(signs)
                basis=[tuple(signs[i] if j==perm[i] else 0 for j in range(3)) for i in range(3)]
                self.assertEqual(tvalue(*basis),det)
                self.assertEqual(tvalue(*basis)==1,det==1)
        # Uniqueness of the singlet follows analytically from 1⊗1=0⊕1⊕2.

    def test_center_obstruction_and_spinor_control(self):
        # z=-I acts trivially on scalar functions of directions, but as -I on
        # the fundamental. An intertwiner T would satisfy T=-T, hence T=0.
        for coefficient in (F(-3),F(0),F(5,7)):
            self.assertEqual(coefficient == -coefficient,coefficient==0)
        spinor=(1,0);minus_spinor=tuple(-x for x in spinor)
        self.assertNotEqual(spinor,minus_spinor)
        # The same ray is not the same linear vector, central to the obstruction.
        self.assertEqual(tuple(-x for x in minus_spinor),spinor)

    def test_charge_lattices_and_s_duality(self):
        for e,m in product(range(-8,9),repeat=2):
            self.assertEqual(lattice('SU2',e,m),lattice('SO3+',*s(e,m)))
            self.assertEqual(lattice('SO3+',e,m),lattice('SU2',*s(e,m)))
            self.assertEqual(lattice('SO3-',e,m),lattice('SO3-',*s(e,m)))
        self.assertTrue(lattice('SU2',1,0))
        self.assertFalse(lattice('SO3+',1,0))
        self.assertTrue(lattice('SO3+',0,1))
        self.assertFalse(lattice('SO3-',0,1))
        self.assertTrue(lattice('SO3-',1,1))

    def test_dirac_pairing_preserved_and_mutual_locality(self):
        charges=list(product(range(-3,4),repeat=2))
        for a,b in product(charges,repeat=2):
            self.assertEqual(pairing(a,b),pairing(s(*a),s(*b)))
            for name in ('SU2','SO3+','SO3-'):
                if lattice(name,*a) and lattice(name,*b):
                    self.assertEqual(pairing(a,b)%2,0)
        self.assertEqual(pairing((1,0),(0,1))%2,1)
        # Analytic proof: the parity classes are the three one-dimensional
        # isotropic subspaces of (Z/2)^2; S preserves the alternating form.

    def test_center_parity_fusion_ring_not_full_representation_fusion(self):
        for e1,m1,e2,m2 in product(range(-3,4),repeat=4):
            a=(e1,m1);b=(e2,m2);combined=(e1+e2,m1+m2)
            self.assertEqual(s(*combined),tuple(x+y for x,y in zip(s(*a),s(*b))))
            for name in ('SU2','SO3+','SO3-'):
                if lattice(name,*a) and lattice(name,*b):
                    self.assertTrue(lattice(name,*combined))
        # This checks the abelian charge grading, not the full OPE or dynamics.

if __name__=='__main__':unittest.main()
