#!/usr/bin/env python3
"""Small combinatorial controls for the alignment witness; no human data."""
from roy_s09_scan1_alignment_gate import candidate_starts


def main():
    assert candidate_starts(141,124) == list(range(1,19))
    assert candidate_starts(124,124) == [1]
    assert candidate_starts(5,1) == [1,2,3,4,5]
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
