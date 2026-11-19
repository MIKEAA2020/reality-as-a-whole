#!/usr/bin/env python3
"""Finite parity control: low-order record marginals do not fix a history law."""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def main():
    checks = []
    for n in range(3, 10):
        all_strings = list(product((0, 1), repeat=n))
        even = [x for x in all_strings if sum(x) % 2 == 0]
        for k in range(1, n):
            for indices in combinations(range(n), k):
                p = Counter(tuple(x[i] for i in indices) for x in all_strings)
                q = Counter(tuple(x[i] for i in indices) for x in even)
                assert len(p) == len(q) == 2**k
                assert all(p[z] * len(even) == q[z] * len(all_strings) for z in p)
        prefix = (1,) * (n - 1)
        compatible = [x for x in even if x[:-1] == prefix]
        assert len(compatible) == 1 and compatible[0][-1] == sum(prefix) % 2
        checks.append({'n': n, 'uniform_histories': len(all_strings),
                       'even_parity_histories': len(even),
                       'proper_nonempty_coordinate_subsets_checked': 2**n - 2,
                       'even_parity_probability_under_uniform': 0.5,
                       'even_parity_probability_under_even_law': 1.0,
                       'next_bit_probability_given_prefix_even_law': 1.0,
                       'next_bit_probability_given_prefix_uniform_law': 0.5})
    out = {'status': 'passed', 'cases': checks,
           'scope': 'finite exact counting, standard parity construction; not financial data, quantum simulations, experiential evidence or an infinite-history theorem'}
    (ROOT / 'verification/temporal_marginal_parity_gate.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
