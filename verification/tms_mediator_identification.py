#!/usr/bin/env python3
"""Exact synthetic randomized-treatment mediation nonidentification control."""
import json
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

OUT = Path(__file__).with_suffix('.json')


def mediator(t, u):
    if t not in (0, 1) or u not in range(4):
        raise ValueError('invalid binary treatment or latent state')
    return int(u == 0) if t == 0 else int(u != 3)


def outcome(model, t, m, u, e):
    if model not in ('A', 'B') or t not in (0, 1) or m not in (0, 1) or e not in (0, 1) or u not in range(4):
        raise ValueError('invalid structural input')
    return (m if model == 'A' else mediator(t, u)) ^ e


def weighted_latents():
    for u in range(4):
        for e, pe in ((0, F(3, 4)), (1, F(1, 4))):
            yield u, e, F(1, 4) * pe


def observed(model, t):
    out = defaultdict(F)
    for u, e, w in weighted_latents():
        m = mediator(t, u)
        out[(m, outcome(model, t, m, u, e))] += w
    return dict(out)


def mean(model, selector):
    return sum((w * selector(model, u, e) for u, e, w in weighted_latents()), F())


def quantities(model):
    p0 = mean(model, lambda a, u, e: outcome(a, 0, mediator(0, u), u, e))
    p1 = mean(model, lambda a, u, e: outcome(a, 1, mediator(1, u), u, e))
    cross = mean(model, lambda a, u, e: outcome(a, 1, mediator(0, u), u, e))
    return {'mean_y_t0': p0, 'mean_y_t1': p1, 'ate': p1-p0,
            'total_natural_indirect_effect': p1-cross,
            'pure_natural_direct_effect': cross-p0,
            'do_m0_given_t1': mean(model, lambda a, u, e: outcome(a, 1, 0, u, e)),
            'do_m1_given_t1': mean(model, lambda a, u, e: outcome(a, 1, 1, u, e))}


def render_fraction(value):
    return str(value)


def main():
    a = [observed('A', t) for t in (0, 1)]
    b = [observed('B', t) for t in (0, 1)]
    assert a == b and all(len(d) == 4 and all(v > 0 for v in d.values()) for d in a)
    numbers = {model: quantities(model) for model in ('A', 'B')}
    assert all(v['ate'] == v['total_natural_indirect_effect'] + v['pure_natural_direct_effect'] for v in numbers.values())
    result = {'scope': 'synthetic exact control, not a model or reanalysis of a human study',
              'conditional_observable_probabilities': {
                  'T='+str(t): {'M='+str(m)+',Y='+str(y): render_fraction(a[t][(m, y)])
                                for m in (0, 1) for y in (0, 1)} for t in (0, 1)},
              'effects': {model: {key: render_fraction(value) for key, value in row.items()}
                          for model, row in numbers.items()}}
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
