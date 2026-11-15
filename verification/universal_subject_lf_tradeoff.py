#!/usr/bin/env python3
"""Exact bounded Local-Friendliness read-error/hidden-joint tradeoff.

Uses the existing one-friend extension. A finite probabilistic control only:
no physical selector, phenomenal subject, dynamics, or completed interpretation.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

from subject_friend_quantum_extensions import sharp, marginal, tv, expect

# Entries of P(a,b,c | x,y), exact feasible endpoint at e=1/5.
RAW = {
 (1, 1): [(-1,-1,-1,8), (-1,1,-1,2), (1,-1,1,2), (1,1,-1,4), (1,1,1,4)],
 (1, 2): [(-1,-1,-1,8), (-1,1,-1,2), (1,-1,1,2), (1,1,-1,4), (1,1,1,4)],
 (2, 1): [(-1,-1,-1,7), (-1,-1,1,2), (-1,1,1,1), (1,-1,-1,1), (1,1,-1,6), (1,1,1,3)],
 (2, 2): [(-1,-1,-1,1), (-1,1,-1,6), (-1,1,1,3), (1,-1,-1,7), (1,-1,1,2), (1,1,1,1)],
}
SIGNS = (-1, 1)
TARGET = {(1,1): F(3,5), (1,2): F(3,5), (2,1): F(4,5), (2,2): F(-4,5)}


def endpoint(x, y):
    table = {k: F(0) for k in product(SIGNS, repeat=3)}
    for a,b,c,n in RAW[x,y]:
        table[a,b,c] = F(n,20)
    return table


def mixture(x, y, t):
    p, q = sharp(x,y), endpoint(x,y)
    return {k: (1-t)*p.get(k,F(0)) + t*q[k] for k in q}


def mismatch(table):
    return sum(p for (a,b,c),p in table.items() if a != c)


def check(t):
    tables = {(x,y): mixture(x,y,t) for x,y in product((1,2), repeat=2)}
    for (x,y), p in tables.items():
        assert sum(p.values()) == 1 and all(v >= 0 for v in p.values())
        for a,b in product(SIGNS, repeat=2):
            pab = sum(p[a,b,c] for c in SIGNS)
            assert pab == (1+a*b*TARGET[x,y])/4
        assert expect(p,(0,1)) == TARGET[x,y]
    # Exact (b,c) independence of Alice setting; (a,c) independence of Bob
    # setting holds for x=1, but x=2 incurs the declared hidden-joint cost.
    for y in (1,2):
        assert marginal(tables[1,y],(1,2)) == marginal(tables[2,y],(1,2))
    assert marginal(tables[1,1],(0,2)) == marginal(tables[1,2],(0,2))
    for x,y in product((1,2),repeat=2):
        assert marginal(tables[x,y],(2,)) == marginal(tables[1,1],(2,))
    e = mismatch(tables[1,1])
    assert e == mismatch(tables[1,2]) == t/5
    leak = tv(marginal(tables[2,1],(0,2)), marginal(tables[2,2],(0,2)))
    assert leak == (1-t)*F(2,5) == F(2,5)-2*e
    return e, leak


def main():
    for i in range(101):
        check(F(i,100))
    samples = {str(t): {'read_mismatch': str(check(t)[0]),
                         'hidden_joint_tv': str(check(t)[1])}
               for t in (F(0), F(1,2), F(1))}
    result = {
      'status': 'passed',
      'scope': 'Exact probability tables for one finite ideal circuit, not a theory of experience or a dynamical model.',
      'observable_correlators': {str(k): str(v) for k,v in TARGET.items()},
      'S': '14/5',
      'tradeoff': 'TV[P(a,c|x=2,y=1),P(a,c|x=2,y=2)] >= 2/5 - 2e, for both read mismatches <= e and (b,c) independent of x',
      'tight_witness': 'Equality for every 0 <= e <= 1/5 via convex mixtures of exact endpoint tables.',
      'sample_points': samples,
      'rational_mixture_checks': 101,
      'limitations': 'All constraints on c are stipulated; no proof of a real friend or conscious universal subject, no derivation of quantum dynamics, and hidden-joint dependence is not automatically operational signalling.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
