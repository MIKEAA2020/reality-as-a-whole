"""Target-relative coarse graining of the existing level/onset spin circuit.

Exact risk calculations assume the existing toy distribution; the physical
bits and their outputs are not evidence of any experience or actual subject.
"""
from collections import defaultdict
from fractions import Fraction as F
import unittest

from verification.constitutive_subject_access_circuit_test import law


def optimal_error(distribution, encoding, target):
    """Best deterministic binary prediction of target from encoding alone."""
    cells=defaultdict(lambda:[F(0),F(0)])
    for (spin,reg),weight in distribution.items():
        cells[encoding(spin,reg)][target(spin,reg)] += weight
    return sum((min(v) for v in cells.values()),F(0))


class CoarseGrainingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.p=law()

    def test_history_distribution_and_level_encoder(self):
        hist=defaultdict(F)
        for (_,r),w in self.p.items(): hist[r[0],r[1]]+=w
        self.assertEqual(dict(hist),{(0,0):F(295,448),(0,1):F(41,448),
                                     (1,0):F(41,448),(1,1):F(71,448)})
        level=lambda s,r:r[1]
        coarse=lambda s,r:r[2]
        self.assertEqual(optimal_error(self.p,coarse,level),0)
        self.assertEqual(sum(w for (_,r),w in self.p.items() if r[2]==1),F(1,4))

    def test_level_encoder_loses_onset(self):
        onset=lambda s,r:r[3]
        level=lambda s,r:r[2]
        self.assertEqual(optimal_error(self.p,level,onset),F(41,448))
        # Within level=1, both onset=1 and onset=0 are supported.
        cells=defaultdict(F)
        for (_,r),w in self.p.items():
            if r[2]==1: cells[r[3]]+=w
        self.assertEqual(dict(cells),{0:F(71,448),1:F(41,448)})
        self.assertEqual(cells[1]/sum(cells.values()),F(41,112))

    def test_entire_current_spin_is_still_insufficient_for_onset(self):
        onset=lambda s,r:r[3]
        self.assertEqual(optimal_error(self.p,lambda s,r:s,onset),F(41,448))
        # Same *full spin* at the final time, different supported memories.
        matches=defaultdict(lambda:[F(0),F(0)])
        for (s,r),w in self.p.items(): matches[s][r[3]]+=w
        self.assertTrue(any(a>0 and b>0 for a,b in matches.values()))

    def test_record_or_target_specific_compression_restores_onset(self):
        onset=lambda s,r:r[3]
        for enc in (lambda s,r:(r[0],r[1]),lambda s,r:r[3]):
            self.assertEqual(optimal_error(self.p,enc,onset),0)
        # Onset alone does not recover persistent mismatch/level.
        self.assertEqual(optimal_error(self.p,lambda s,r:r[3],lambda s,r:r[2]),F(71,448))

    def test_uniform_record_coarse_grain_zeros_can_retain_no_level_details(self):
        # Both distributions have exactly P(level=1)=1/4. They are abstract
        # history distributions, not additional realizations of the spin kernel.
        a={(0,0):F(3,4),(0,1):F(1,4)}
        b={(0,0):F(3,4),(1,1):F(1,4)}
        self.assertEqual(sum(w for (old,new),w in a.items() if new),F(1,4))
        self.assertEqual(sum(w for (old,new),w in b.items() if new),F(1,4))
        self.assertEqual(sum(w for (old,new),w in a.items() if new and not old),F(1,4))
        self.assertEqual(sum(w for (old,new),w in b.items() if new and not old),F(0))


if __name__=='__main__': unittest.main()
