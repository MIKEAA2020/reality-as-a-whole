#!/usr/bin/env python3
"""Exact toy extension of a known one-friend CHSH/LF scenario.

Does not prove that the hidden variable C is a thought, that quantum cognition is
possible, or that the extension is a dynamical physical theory. All probabilities
are rational; matrices implement only the stated three-qubit circuit.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

SIGNS = (-1, 1)


def add(d, key, value):
    d[key] = d.get(key, F(0)) + value


def sharp(x, y):
    """P(a,b,c|x,y), with c=a for x=1 and optimal joint leakage for x=2."""
    out = {}
    for b in SIGNS:
        if x == 1:
            for g, p in ((1, F(4, 5)), (-1, F(1, 5))):
                c = g*b
                add(out, (c, b, c), p/2)
        else:
            # f=a*b, g=c*b. Both y settings have E[g]=3/5.
            fg = ({(1, 1): F(7, 10), (-1, 1): F(1, 10),
                   (1, -1): F(2, 10), (-1, -1): F(0)} if y == 1 else
                  {(1, 1): F(1, 10), (-1, 1): F(7, 10),
                   (1, -1): F(0), (-1, -1): F(2, 10)})
            for (f, g), p in fg.items():
                add(out, (f*b, b, g*b), p/2)
    return out


def local_threshold(x, y):
    """A convex mixture of four CHSH facets, with unbiased sign symmetrization."""
    weights = [F(2, 7), F(2, 7), F(3, 14), F(3, 14)]
    out = {}
    for i, weight in enumerate(weights):
        eps = [-1 if j == i else 1 for j in range(4)]
        for a1 in SIGNS:
            b1, b2 = eps[0]*a1, eps[1]*a1
            a2 = eps[2]*b1
            assert a2*b2 == -eps[3]
            a = a1 if x == 1 else a2
            b = b1 if y == 1 else b2
            add(out, (a, b, a1), weight/2)
    return out


def white(x, y):
    out = {}
    for a1, a2, b1, b2 in product(SIGNS, repeat=4):
        add(out, (a1 if x == 1 else a2, b1 if y == 1 else b2, a1), F(1, 16))
    return out


def mix(p, q, lam):
    return {k: (1-lam)*p.get(k, F(0)) + lam*q.get(k, F(0))
            for k in set(p) | set(q)}


def extension(x, y, visibility):
    if visibility <= F(5, 7):
        return mix(white(x, y), local_threshold(x, y), visibility*F(7, 5))
    return mix(local_threshold(x, y), sharp(x, y), (7*visibility-5)/2)


def marginal(dist, inds):
    out = {}
    for key, p in dist.items():
        add(out, tuple(key[i] for i in inds), p)
    return out


def expect(dist, inds):
    return sum((p * (1 if not inds else prod(key[i] for i in inds))
                for key, p in dist.items()), F(0))


def prod(vals):
    out = 1
    for v in vals:
        out *= v
    return out


def tv(p, q):
    return sum((abs(p.get(k, 0)-q.get(k, 0)) for k in set(p) | set(q)), F(0))/2


def quantum_correlators():
    """GHZ recording state; inverse CNOT on A,M for x=2. State unnormalized."""
    z = ((F(1), F(0)), (F(0), F(-1)))
    ident = ((F(1), F(0)), (F(0), F(1)))
    xx = ((F(0), F(1)), (F(1), F(0)))
    bob = [tuple(tuple(F(3, 5)*z[i][j] + s*F(4, 5)*xx[i][j]
                       for j in range(2)) for i in range(2)) for s in (1, -1)]
    ghz = {(0, 0, 0): F(1), (1, 1, 1): F(1)}
    undone = {(a, m ^ a, b): v for (a, m, b), v in ghz.items()}
    def value(state, ops):
        return sum((v*w*prod(ops[i][k[i]][l[i]] for i in range(3))
                    for k, v in state.items() for l, w in state.items()), F(0))/2
    return {(x, y): value(ghz if x == 1 else undone,
                           (ident, z, bob[y-1]) if x == 1 else (xx, ident, bob[y-1]))
            for x, y in product((1, 2), repeat=2)}


def main():
    correlators = {(1, 1): F(3, 5), (1, 2): F(3, 5),
                   (2, 1): F(4, 5), (2, 2): F(-4, 5)}
    assert quantum_correlators() == correlators
    sharp_tv = None
    for visibility in [F(i, 100) for i in range(101)] + [F(5, 7)]:
        tables = {(x, y): extension(x, y, visibility)
                  for x, y in product((1, 2), repeat=2)}
        for (x, y), p in tables.items():
            assert sum(p.values()) == 1 and all(v >= 0 for v in p.values())
            assert expect(p, (0, 1)) == visibility*correlators[x, y]
            assert expect(p, (0,)) == expect(p, (1,)) == expect(p, (2,)) == 0
            if x == 1:
                assert sum(v for (a, b, c), v in p.items() if a != c) == 0
        # (b,c) is outside x's future; c is independent of both settings.
        for y in (1, 2):
            assert marginal(tables[1, y], (1, 2)) == marginal(tables[2, y], (1, 2))
        for x in (1, 2):
            assert marginal(tables[x, 1], (2,)) == marginal(tables[x, 2], (2,))
            assert marginal(tables[x, 1], (0,)) == marginal(tables[x, 2], (0,))
        for y in (1, 2):
            assert marginal(tables[1, y], (1,)) == marginal(tables[2, y], (1,))
        hidden_tv = tv(marginal(tables[2, 1], (0, 2)), marginal(tables[2, 2], (0, 2)))
        lower_bound = max(F(0), F(7, 5)*visibility-1)
        assert hidden_tv == lower_bound
        if visibility == 1:
            sharp_tv = hidden_tv
            assert expect(tables[2, 1], (0, 2)) == F(2, 5)
            assert expect(tables[2, 2], (0, 2)) == F(-2, 5)
    S = correlators[1, 1] + correlators[1, 2] + correlators[2, 1] - correlators[2, 2]
    assert S == F(14, 5) and sharp_tv == F(2, 5)
    result = {
        'status': 'passed',
        'scope': 'One-friend, two-setting, exact rational toy circuit and constructed probability extensions; no consciousness, physical realization, dynamics, or complete interpretation established.',
        'three_qubit_circuit_correlators': {f'{x},{y}': str(v) for (x, y), v in correlators.items()},
        'CHSH_value': str(S),
        'sharp_witness_joint_ac_correlators': ['2/5', '-2/5'],
        'sharp_minimum_hidden_joint_total_variation': str(sharp_tv),
        'white_noise_visibility_threshold': '5/7',
        'tight_minimum_joint_tv_over_this_isotropic_family': 'max(0, 7*visibility/5 - 1)',
        'visibility_points_checked': 102,
        'limitations': 'Lower bound assumes read agreement c=a for x=1 and (b,c) independent of x. It concerns the unobserved joint (a,c), not operational signalling or a necessary change in every component of Local Agency.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
