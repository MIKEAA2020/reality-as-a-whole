#!/usr/bin/env python3
"""Invented spatial aggregation and smoothing examples, not rivalry data."""
from fractions import Fraction as F
from pathlib import Path
import json


def spatial_traces():
    binary_local = [[F(int(i < k)) for i in range(4)] for k in range(5)]
    uniform_local = [[F(k, 4)] * 4 for k in range(5)]
    mean = lambda row: sum(row, F(0)) / len(row)
    return binary_local, uniform_local, [mean(row) for row in binary_local], [mean(row) for row in uniform_local]


def causal_three_point(signal):
    """Fixed baseline -1 in the two samples preceding the observed sequence."""
    values = [F(-1), F(-1)] + [F(x) for x in signal]
    return [sum(values[i:i+3], F(0)) / 3 for i in range(len(signal))]


def main():
    binary, uniform, avg_binary, avg_uniform = spatial_traces()
    short = [-1, -1, 1, -1, -1, -1]
    longer = [-1, -1, 1, 1, -1, -1, -1]
    short_smoothed = causal_three_point(short)
    longer_smoothed = causal_three_point(longer)
    assert avg_binary == avg_uniform == [F(0), F(1,4), F(1,2), F(3,4), F(1)]
    assert max(short_smoothed) < 0 and max(longer_smoothed) > 0
    receipt = {'scope': 'Synthetic local numerical scores and a boxcar filter; not data, subjects, or an ocular model.',
               'binary_local_scores': binary, 'uniform_local_scores': uniform,
               'shared_means': avg_binary, 'short_signal': short,
               'short_smoothed': short_smoothed, 'longer_signal': longer,
               'longer_smoothed': longer_smoothed}
    def encode(v):
        if isinstance(v, F): return str(v)
        if isinstance(v, list): return [encode(x) for x in v]
        if isinstance(v, dict): return {k: encode(x) for k, x in v.items()}
        return v
    result = json.dumps(encode(receipt), indent=2) + '\n'
    Path(__file__).with_suffix('.json').write_text(result)
    print(result, end='')


if __name__ == '__main__':
    main()
