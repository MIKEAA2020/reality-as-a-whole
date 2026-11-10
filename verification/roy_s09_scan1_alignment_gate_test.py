#!/usr/bin/env python3
"""Small combinatorial controls for the alignment witness; no human data."""
import numpy as np
from roy_s09_scan1_alignment_gate import candidate_starts, sample_indices


def main():
    assert candidate_starts(141,124) == list(range(1,19))
    assert candidate_starts(124,124) == [1]
    assert candidate_starts(5,1) == [1,2,3,4,5]
    assert candidate_starts(129,127) == [1,2,3]
    assert np.array_equal(sample_indices([1194.9999999999995, 1744.9999999999995, 2295.0]), [1195, 1745, 2295])
    for bad in ([1.25], [float('nan')], [float('inf')]):
        try:
            sample_indices(bad)
        except ValueError:
            pass
        else:
            raise AssertionError('Fractional or non-finite sample index should stop')
    for a,b in [(3,4),(0,1),(1,0)]:
        try:
            candidate_starts(a,b)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid mappings should stop')
    print('PASS: 18 candidate starts, boundary cases and invalid-length stop')


if __name__=='__main__':
    main()
