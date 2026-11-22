#!/usr/bin/env python3
import unittest
import numpy as np
from roy_s01_mixed_coverage_diagnostic import summarize


class MixedCoverageTest(unittest.TestCase):
    def test_window_thresholds_and_full_denominator(self):
        fs=2
        state=np.zeros(42*fs,dtype=np.uint8)
        state[0:3]=3            # first 2s window: 75% mixed
        state[4:6]=3            # second: 50%
        state[8]=3              # third: 25%
        m=np.zeros_like(state); m[0]=1
        out=summarize([state],[m],fs)
        self.assertEqual(out['windows'],21)
        self.assertEqual(out['windows_with_any_mixed'],3)
        self.assertEqual(out['windows_mixed_at_least_50pct'],2)
        self.assertEqual(out['windows_mixed_at_least_75pct'],1)
        self.assertEqual(out['max_mixed_fraction_of_any_window'],0.75)
        self.assertEqual(out['time_by_report_code_seconds']['3'],3.0)
        self.assertEqual(sum(out['time_by_report_code_seconds'].values()),42.0)


if __name__=='__main__':unittest.main()
