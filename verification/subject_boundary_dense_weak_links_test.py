import itertools
import unittest
from fractions import Fraction as F

from causal_influence_subject_gate import score
from competing_subject_constitution_rules import overlapping_local_maxima
from subject_boundary_dense_weak_links import type_score, classify_scores, analyze


class DenseBoundaryTests(unittest.TestCase):
    def test_score_matches_existing_calculation(self):
        m=3
        for eps in (F(0), F(1,6), F(1,3), F(1)):
            edges={(i,j): F(1) if (i<m)==(j<m) else eps
                   for i,j in itertools.combinations(range(2*m),2)}
            for size in range(2,2*m+1):
                for subset in itertools.combinations(range(2*m),size):
                    a=sum(i<m for i in subset)
                    self.assertEqual(type_score(a,size-a,m,eps),score(subset,edges))

    def test_existing_selector_same(self):
        m=3; n=2*m
        for eps in (F(1,6),F(1,3),F(1)):
            edges={(i,j): F(1) if (i<m)==(j<m) else eps
                   for i,j in itertools.combinations(range(n),2)}
            actual=overlapping_local_maxima(frozenset(range(n)),edges)
            winner_masks,tie_masks=analyze(m,eps)
            conv=lambda masks:frozenset(frozenset(i for i in range(n) if mask & (1<<i)) for mask in masks)
            self.assertEqual((conv(winner_masks),conv(tie_masks)),actual)

    def test_whole_score_and_all_proper_subset_gap(self):
        for m in range(3,13):
            e=F(1,m)
            self.assertEqual(type_score(m,m,m,e),m)
            for a in range(m+1):
                for b in range(m+1):
                    if a+b<2 or (a==m and b==m):continue
                    self.assertLessEqual(type_score(a,b,m,e), F(m)-F(1,m))

    def test_normalization_repairs_finite_cases(self):
        for m in (3,4,5):
            cores=frozenset(((1<<m)-1,((1<<m)-1)<<m))
            whole=frozenset(((1<<(2*m))-1,))
            self.assertEqual(analyze(m,F(1,2*m)),(cores,frozenset()))
            self.assertEqual(analyze(m,F(1,m)),(whole,frozenset()))
            self.assertEqual(analyze(m,F(1,m),True),(cores,frozenset()))
            self.assertEqual(analyze(m,F(1),True),(whole,frozenset()))

    def test_normalization_symmetric_overlap_tie(self):
        edges={(0,1):F(1),(1,2):F(1),(0,2):F(0)}
        scores={sum(1<<i for i in s):score(s,edges)/len(s)
                for k in (2,3) for s in itertools.combinations(range(3),k)}
        winners,ties=classify_scores(scores)
        self.assertFalse(winners)
        self.assertEqual(ties,frozenset((0b011,0b110)))

    def test_bad_input(self):
        with self.assertRaises(ValueError): type_score(4,0,3,F(1))
        with self.assertRaises(ValueError): analyze(1,F(0))

if __name__=='__main__': unittest.main()
