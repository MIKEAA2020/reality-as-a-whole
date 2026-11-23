"""Bell and no-signalling checks using the conserved five-ray trine.

The fixed records are a finite contextual construction, not a dynamical model,
a necessity proof, a local hidden-variable model, or an empirical dataset.
"""
from collections import Counter
from fractions import Fraction as F
from math import sqrt
import unittest

from verification.zero_sphere_conservation_born_bridge_test import bridge, ray


TRINE = ((1.0, 0.0, 0.0), (-0.5, sqrt(3)/2, 0.0),
         (-0.5, -sqrt(3)/2, 0.0))
A_AXES = ((1.0,0.0,0.0), (0.0,1.0,0.0))
B_AXES = ((0.6,0.8,0.0), (0.6,-0.8,0.0), (1.0,0.0,0.0))


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def fixed_record(a, b, seed):
    """A in {0,1,'T'}; B in {0,1,2}; seed in range(60)."""
    if a not in (0,1,'T') or b not in (0,1,2) or not 0 <= seed < 60:
        raise ValueError('invalid context or seed')
    if a == 'T':
        outcome = seed % 3
        rank = seed // 3
        limits = ((4,6,20), (4,20,6), (0,15,15))[b]
        return outcome, (1 if rank < limits[outcome] else -1)
    r = seed % 20
    a_result = 1 if r < 10 else -1
    rank = r % 10
    # Equal-size setting-independent seeds; correlations -a·b.
    limits = ((2,2,0),(1,9,5))
    product = 1 if rank < limits[a][b] else -1
    return a_result, a_result*product


def effects(axis, scale=1):
    """scale * projector along Bloch axis, in the standard z-spin basis."""
    x,y,z = axis
    return ((scale*(1+z)/2, scale*complex(x,-y)/2),
            (scale*complex(x,y)/2, scale*(1-z)/2))


def kron(x,y):
    return tuple(tuple(x[i//2][j//2]*y[i%2][j%2] for j in range(4))
                 for i in range(4))


def singlet_born(ea, eb):
    m = kron(ea,eb)
    v = (0,1/sqrt(2),-1/sqrt(2),0)
    return sum(v[i].conjugate()*m[i][j]*v[j] for i in range(4)
               for j in range(4)).real


class SphereSingletFixedRecordsTests(unittest.TestCase):
    def test_trine_really_comes_from_five_ray_configuration(self):
        rays = [ray(0), ray(2), ray(1), ray(0,1), ray(0,-1)]
        result, q, dots = bridge(rays)
        self.assertEqual(result['triple'], [2,3,4])
        self.assertEqual([q[i] for i in result['triple']], [F(1,3)]*3)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(dot(TRINE[i],TRINE[j]),
                                       float(dots[result['triple'][i]][result['triple'][j]]))

    def test_singlet_maximally_mixed_reduction_and_projector_probabilities(self):
        identity = ((1,0),(0,1))
        for n in TRINE:
            self.assertAlmostEqual(singlet_born(effects(n), identity), .5)
            self.assertAlmostEqual(singlet_born(effects(n, F(2,3)), identity), 1/3)
        for a in A_AXES:
            for b in B_AXES:
                for x in (-1,1):
                    for y in (-1,1):
                        p = singlet_born(effects(tuple(x*v for v in a)),
                                          effects(tuple(y*v for v in b)))
                        self.assertAlmostEqual(p, (1-x*y*dot(a,b))/4)

    def test_singlet_trine_joint_probabilities_and_no_signalling(self):
        for b in B_AXES:
            for n in TRINE:
                probs = [singlet_born(effects(n,F(2,3)),
                                      effects(tuple(y*v for v in b))) for y in (-1,1)]
                self.assertAlmostEqual(sum(probs), 1/3)
                for p,y in zip(probs,(-1,1)):
                    self.assertAlmostEqual(p, (1-y*dot(n,b))/6)
            for y in (-1,1):
                self.assertAlmostEqual(sum(singlet_born(effects(n,F(2,3)),
                                     effects(tuple(y*v for v in b))) for n in TRINE), 1/2)

    def test_asymmetric_conserved_weights_give_remote_steering(self):
        rays = [ray(0), ray(1), ray(3), ray(0,1), ray(0,2)]
        result, weights, dots = bridge(rays)
        i0,i1,i2 = result['triple']
        qs = [weights[i] for i in (i0,i1,i2)]
        self.assertEqual(qs, [F(1,8),F(2,5),F(19,40)])
        c = float(dots[i0][i1])
        n0 = (1.0,0.0,0.0)
        n1 = (c,sqrt(1-c*c),0.0)
        n2 = tuple(-float(qs[0]/qs[2])*x-float(qs[1]/qs[2])*y
                   for x,y in zip(n0,n1))
        ns = (n0,n1,n2)
        self.assertAlmostEqual(dot(n2,n2),1)
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(dot(ns[i],ns[j]),
                                       float(dots[result['triple'][i]][result['triple'][j]]))
        for axis in ((1.,0.,0.),(0.,1.,0.),(0.,0.,1.)):
            for y in (-1,1):
                probs = [singlet_born(effects(n,2*float(q)),
                            effects(tuple(y*v for v in axis))) for n,q in zip(ns,qs)]
                for p,n,q in zip(probs,ns,qs):
                    self.assertAlmostEqual(p,float(q)*(1-y*dot(n,axis))/2)
                self.assertAlmostEqual(sum(probs),.5)

    def test_exact_chsh_violation_in_fixed_records(self):
        values = []
        for a,b in ((0,0),(0,1),(1,0),(1,1)):
            c = Counter(fixed_record(a,b,s) for s in range(60))
            values.append(sum(F(x*y*count,60) for (x,y),count in c.items()))
        self.assertEqual(values, [F(-3,5),F(-3,5),F(-4,5),F(4,5)])
        self.assertEqual(abs(values[0]+values[1]+values[2]-values[3]), F(14,5))

    def test_fixed_records_are_no_signalling_and_measurement_independent(self):
        # Every one of nine settings pairs occurs with every seed once.
        records = [(a,b,s,*fixed_record(a,b,s))
                   for a in (0,1,'T') for b in (0,1,2) for s in range(60)]
        self.assertEqual(len(records), 540)
        self.assertEqual(len({(a,b,s) for a,b,s,_,_ in records}), 540)
        for a in (0,1,'T'):
            alice = [Counter(x for aa,bb,_,x,_ in records if aa==a and bb==b)
                     for b in (0,1,2)]
            self.assertTrue(all(m == alice[0] for m in alice))
            self.assertEqual(alice[0], Counter({0:20,1:20,2:20}) if a=='T'
                             else Counter({-1:30,1:30}))
        for b in (0,1,2):
            for a in (0,1,'T'):
                marginal = Counter(y for aa,bb,_,_,y in records if aa==a and bb==b)
                self.assertEqual(marginal, Counter({-1:30,1:30}))

    def test_contextuality_is_explicit_not_local_determinism(self):
        # Same seed and Bob setting, different Alice setting, flips Bob's result.
        self.assertEqual(fixed_record(0,0,1), (1,1))
        self.assertEqual(fixed_record(1,0,1), (1,-1))

    def test_trine_records_close_to_quantum_joint_distribution(self):
        max_error = 0.0
        for b,axis in enumerate(B_AXES):
            c = Counter(fixed_record('T',b,s) for s in range(60))
            for i,n in enumerate(TRINE):
                for y in (-1,1):
                    target = singlet_born(effects(n,F(2,3)),
                                          effects(tuple(y*v for v in axis)))
                    max_error = max(max_error,abs(c[(i,y)]/60-target))
        self.assertGreater(max_error,0)
        self.assertLess(max_error,0.0013)

    def test_binary_contexts_match_full_singlet_joint_distribution(self):
        for a in (0,1):
            for b in (0,1,2):
                c = Counter(fixed_record(a,b,s) for s in range(60))
                for x in (-1,1):
                    for y in (-1,1):
                        target = singlet_born(effects(tuple(x*v for v in A_AXES[a])),
                                              effects(tuple(y*v for v in B_AXES[b])))
                        self.assertAlmostEqual(c[(x,y)]/60,target)


if __name__ == '__main__':
    unittest.main()
