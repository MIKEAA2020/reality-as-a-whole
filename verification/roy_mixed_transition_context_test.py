#!/usr/bin/env python3
import unittest
import numpy as np
from roy_mixed_transition_context import FS, grid, candidates, match, context, stability, flank_db, summarize


class ContextTest(unittest.TestCase):
    def test_grid_midpoint_missing_and_artifact(self):
        state=np.ones(42*FS,dtype=np.uint8);mask=np.zeros_like(state)
        state[251:270]=3  # too brief and between grid positions
        state[400:500]=3  # midpoint 450 is a grid center
        mixed,controls,c=candidates(state,mask)
        self.assertEqual(len(grid()),201)
        self.assertEqual(mixed,[450])
        self.assertEqual(c['mixed_segments_total'],2)
        self.assertEqual(c['mixed_segments_without_valid_grid_center'],1)
        self.assertTrue(all(state[x] in (1,2) for x in controls))
        mask[450]=1
        mixed,_,c=candidates(state,mask)
        self.assertEqual(mixed,[]);self.assertEqual(c['mixed_segments_artifact_excluded'],1)

    def test_matching_distance_tie_no_reuse_and_no_overlap(self):
        pairs=match([1000,1050],[500,1550,1600,2999])
        self.assertEqual(pairs,[(1000,500),(1050,1550)])
        self.assertEqual(len({c for _,c in pairs}),len(pairs))
        self.assertTrue(all(2*FS<=abs(m-c)<=6*FS for m,c in pairs))
        with self.assertRaises(ValueError):match([1000,1000],[500])

    def test_context_weights_and_timing(self):
        state=np.ones(42*FS,dtype=np.uint8);state[490:510]=3
        out=context(state,500)
        self.assertAlmostEqual(out['mixed_fraction'],20/500)
        self.assertGreater(out['mixed_hann_squared_weight_fraction'],out['mixed_fraction'])
        self.assertAlmostEqual(sum(out[k] for k in ('mixed_fraction','unknown_fraction','code1_fraction','code2_fraction')),1)
        self.assertEqual(stability(state,500),(0,0))
        state[:]=3
        self.assertEqual(stability(state,500),(1,1))
        self.assertAlmostEqual(context(state,500)['mixed_hann_squared_weight_fraction'],1)

    def test_spectral_and_undefined_empty_pairs(self):
        t=np.arange(500)/FS
        low=flank_db(np.sin(2*np.pi*6.6666666667*t));high=flank_db(np.sin(2*np.pi*8.5714285714*t))
        self.assertGreater(low[0],0);self.assertGreater(high[1],0)
        with self.assertRaises(ValueError):flank_db(np.zeros(500))
        n=42*FS
        out=summarize('synthetic',[(np.sin(2*np.pi*6.6666666667*np.arange(n)/FS),np.zeros(n,dtype=np.uint8),np.ones(n,dtype=np.uint8))])
        self.assertEqual(out['matching_coverage']['matched_pairs'],0)
        self.assertIsNone(out['matched_pair_summary']['fraction_positive'])


if __name__=='__main__':unittest.main()
