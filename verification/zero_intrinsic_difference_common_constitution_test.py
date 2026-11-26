"""Reference-free balance and pointed content: finite structural controls.

A classical mathematical comparison, not a physical cosmic energy, proof
of experiential identity, or a derivation of real subjecthood.
"""
from fractions import Fraction as F
from itertools import permutations, product
import unittest


def centered(values):
    mean=sum(values,F(0))/len(values)
    return tuple(v-mean for v in values)


def weighted_centered(values,weights):
    assert len(values)==len(weights) and all(w>0 for w in weights)
    mean=sum((w*v for w,v in zip(weights,values)),F(0))/sum(weights,F(0))
    return tuple(v-mean for v in values)


def permute(values,order):
    return tuple(values[i] for i in order)


def pointed_value(a,p):
    assert p in (0,1)
    return a if p==0 else -a


def relabel(a,p):
    return -a,1-p


def matvec(m,v):
    return tuple(sum((m[i][j]*v[j] for j in range(len(v))),F(0))
                 for i in range(len(v)))


def is_equivariant(m):
    n=len(m)
    for order in permutations(range(n)):
        for i in range(n):
            for j in range(n):
                if m[i][j]!=m[order[i]][order[j]]:
                    return False
    return True


class IntrinsicDifferenceCommonConstitutionTests(unittest.TestCase):
    def test_shift_and_permutation_invariance_and_zero_sum(self):
        for raw in product(range(-2,3),repeat=3):
            v=tuple(map(F,raw)); e=centered(v)
            self.assertEqual(sum(e),0)
            for c in (F(-7,3),F(0),F(5,4)):
                self.assertEqual(centered(tuple(x+c for x in v)),e)
            for p in permutations(range(3)):
                self.assertEqual(centered(permute(v,p)),permute(e,p))
            # Reference-free nonzero overall spread is invariant too.
            spread=max(v)-min(v)
            self.assertEqual(max(e)-min(e),spread)

    def test_unequal_weights_are_input_not_automatically_fixed(self):
        values=(F(0),F(3),F(6))
        w1=(F(1),F(1),F(1)); w2=(F(1),F(1),F(2))
        e1=weighted_centered(values,w1); e2=weighted_centered(values,w2)
        self.assertEqual(e1,(F(-3),F(0),F(3)))
        self.assertEqual(e2,(F(-15,4),F(-3,4),F(9,4)))
        for w,e in ((w1,e1),(w2,e2)):
            self.assertEqual(sum(x*y for x,y in zip(w,e)),0)
        self.assertNotEqual(e1,e2)

    def test_linear_permutation_equivariant_shift_invariant_class(self):
        # Exhaust integer 3x3 matrices on [-2,2] restricted to equivariant
        # forms: diagonal d and off-diagonal o. Full permutation equivariance
        # itself forces this form; the proof is in the report.
        for n in range(2,6):
            for d,o in product(range(-4,5),repeat=2):
                m=tuple(tuple(F(d if i==j else o) for j in range(n)) for i in range(n))
                self.assertTrue(is_equivariant(m))
                if d+(n-1)*o==0:
                    alpha=F(d-o)
                    for v in (tuple(F(i) for i in range(n)),
                              tuple(F(i*i-2) for i in range(n))):
                        self.assertEqual(matvec(m,v),tuple(alpha*x for x in centered(v)))
                    self.assertEqual(matvec(m,tuple(F(1) for _ in range(n))),tuple(F(0) for _ in range(n)))

    def test_local_distinctions_survive_relabelling(self):
        for a in (F(-3),F(-1,2),F(0),F(1,2),F(3)):
            self.assertEqual(pointed_value(a,0)+pointed_value(a,1),0)
            for p in (0,1):
                aa,pp=relabel(a,p)
                self.assertEqual(pointed_value(a,p),pointed_value(aa,pp))
                self.assertEqual(relabel(aa,pp),(a,p))
            self.assertEqual(abs(pointed_value(a,0)-pointed_value(a,1)),2*abs(a))

    def test_structural_symmetry_alone_not_quality_or_total_energy(self):
        # These three assignments share the same balance and gauge behavior.
        # A sign-reversed assignment is only a physically different quality
        # claim if neutral/positive/negative experiential labels are held fixed.
        for a in (F(1,3),F(2)):
            for p in (0,1):
                a2,p2=relabel(a,p)
                v=pointed_value(a,p)
                values=(v,-v,F(0))
                relabelled=(pointed_value(a2,p2),-pointed_value(a2,p2),F(0))
                self.assertEqual(values,relabelled)
                self.assertEqual(len(set(values)),3)
            self.assertNotEqual(pointed_value(a,0),0)
            self.assertNotEqual(pointed_value(a,0),-pointed_value(a,0))
            # Their reference-free separation is nonzero even though the
            # additive centered sum is zero; it is not asserted to be energy.
            self.assertGreater(abs(pointed_value(a,0)-pointed_value(a,1)),0)


if __name__=='__main__':
    unittest.main()
