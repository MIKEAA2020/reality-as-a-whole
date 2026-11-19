#!/usr/bin/env python3
"""Exact checks of a published contextual example; not a general proof.

Source: García Díaz, Brandenburger and Scarpa, PNAS supplement, Tables E1/E2.
"""
from fractions import Fraction as F
from itertools import product

# Signed phase-space entries ordered a,b,e = 000,001,...,111.
w = dict(zip(product(range(2), repeat=3), map(lambda n: F(n, 16),
             [3, 5, 5, -1, -3, 3, 3, 1])))
# Pairwise probabilities, keyed by first and second measurement outcomes.
expected = {
    (0, 1): {(0, 0): F(1, 2), (1, 0): F(0), (0, 1): F(1, 4), (1, 1): F(1, 4)},
    (0, 2): {(0, 0): F(1, 2), (1, 0): F(0), (0, 1): F(1, 4), (1, 1): F(1, 4)},
    (1, 2): {(0, 0): F(0), (1, 0): F(1, 2), (0, 1): F(1, 2), (1, 1): F(0)},
}
assert sum(w.values()) == 1
assert sum(value < 0 for value in w.values()) == 2
for (i, j), table in expected.items():
    for (x, y), prob in table.items():
        assert sum(v for bits, v in w.items() if bits[i] == x and bits[j] == y) == prob
    assert sum(table.values()) == 1
    assert min(table.values()) >= 0
# Pairwise distributions share consistent one-site marginals.
for i in range(3):
    for x in range(2):
        values = []
        for (j, k), table in expected.items():
            if i == j:
                values.append(sum(p for (a, b), p in table.items() if a == x))
            elif i == k:
                values.append(sum(p for (a, b), p in table.items() if b == x))
        assert len(values) == 2 and values[0] == values[1]
# A nonnegative joint distribution cannot have these marginals:
# a=1,b=0; a=1,e=0; b=1,e=1 all have zero probability.
# Every assignment with a=1 lies in one of these zero events, so P(a=1)=0,
# contradicting P(a=1)=1/4. Test that cover exhaustively.
for a, b, e in product(range(2), repeat=3):
    if a == 1:
        assert (b == 0) or (e == 0) or (b == 1 and e == 1)
assert expected[(0, 1)][(1, 0)] == 0
assert expected[(0, 2)][(1, 0)] == 0
assert expected[(1, 2)][(1, 1)] == 0
assert sum(p for (a, b), p in expected[(0, 1)].items() if a == 1) == F(1, 4)
print('PASS: signed representation, three pair marginals and no-signaling')
print('PASS: nonnegative-joint contradiction: P(a=1)=0 versus 1/4')
print('Scope: authors’ single example only; no general quantum theorem proved.')
