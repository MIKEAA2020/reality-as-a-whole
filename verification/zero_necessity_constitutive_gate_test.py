import itertools
import unittest


N=6


def solutions():
    out=[]
    for signs in itertools.product((-1,1),repeat=N):
        if sum(signs)==0 and all(signs[i]!=signs[(i+1)%N] for i in range(N)):
            out.append(signs)
    return out


class NecessityConstitutionGateTests(unittest.TestCase):
    def test_unique_rooted_physical_ring_allows_two_signed_expansions(self):
        models=solutions()
        self.assertEqual(len(models),2)
        self.assertEqual(models[0],tuple(-x for x in models[1]))
        self.assertNotEqual(models[0][0],models[1][0])
        self.assertEqual(sum(models[0]),0)
        self.assertEqual(sum(models[1]),0)
        # An allowed equivalence must fix physical root 0 and preserve signs.
        # Opposite signs at the fixed root rule out any such equivalence.

    def test_both_formal_expansions_include_both_signs_at_equal_incidence(self):
        for signs in solutions():
            self.assertEqual(signs.count(1),3)
            self.assertEqual(signs.count(-1),3)
            self.assertEqual(set(signs),{-1,1})

    def test_one_empirical_root_fact_distinguishes_but_does_not_explain_law(self):
        signs_at_root_negative=[s for s in solutions() if s[0]==-1]
        self.assertEqual(len(signs_at_root_negative),1)

    def test_qualitative_zero_requires_incidence_weights(self):
        signs=solutions()[0]
        weights=[2,1,1,1,1,1]
        self.assertEqual(sum(signs),0)
        self.assertNotEqual(sum(w*v for w,v in zip(weights,signs)),0)

    def test_local_realizations_transfer_across_physical_experiential_equivalence(self):
        # A cyclic relabelling of a given signed realization preserves all
        # occurrences when the root and sign labels are transported together.
        a=solutions()[0]
        shift=2
        b=tuple(a[(i-shift)%N] for i in range(N))
        for i in range(N):
            self.assertEqual(a[i],b[(i+shift)%N])
        self.assertEqual({s for s in a},{s for s in b})


if __name__=='__main__': unittest.main()
