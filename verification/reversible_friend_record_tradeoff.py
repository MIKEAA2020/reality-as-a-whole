#!/usr/bin/env python3
"""Exact rational checks of a model-specific friend-record/coherence tradeoff.

Four qubits A,M,B,E. This is standard complementarity in a chosen circuit, not
an experience test, a general collapse theorem, or evidence about human observers.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

Z = ((F(1), F(0)), (F(0), F(-1)))
X = ((F(0), F(1)), (F(1), F(0)))
I = ((F(1), F(0)), (F(0), F(1)))


def matrix_add(a, b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))


def scale(x, a):
    return tuple(tuple(x*a[i][j] for j in range(2)) for i in range(2))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def prod(vals):
    z = F(1)
    for a in vals:
        z *= a
    return z


def expectation(state, ops):
    # State amplitudes are unnormalized by sqrt(2).
    return sum((v*w*prod(ops[i][k[i]][l[i]] for i in range(4))
                for k, v in state.items() for l, w in state.items()), F(0))/2


def undo_memory(state):
    return {(a, m ^ a, b, e): amp for (a, m, b, e), amp in state.items()}


def recover_environment(state, r, d):
    # Controlled inverse of rotation R=[[r,-d],[d,r]], with control A.
    out = {}
    inverse = ((r, d), (-d, r))
    for (a, m, b, e), amp in state.items():
        matrix = inverse if a else I
        for ep in (0, 1):
            key = (a, m, b, ep)
            out[key] = out.get(key, F(0)) + matrix[ep][e]*amp
    return {k: v for k, v in out.items() if v}


def main():
    cases = 0
    witness = None
    # Rational parametrization of r²+d²=1, 0≤r,d≤1.
    for n in range(1, 13):
        for m in range(n+1):
            t = F(m, n)
            r = (1-t*t)/(1+t*t)
            d = 2*t/(1+t*t)
            assert r*r+d*d == 1
            # |0000>+r|1110>+d|1111>, all divided by sqrt(2).
            state = {(0, 0, 0, 0): F(1), (1, 1, 1, 0): r,
                     (1, 1, 1, 1): d}
            reversed_state = undo_memory(state)
            bz_plus = matrix_add(scale(F(3, 5), Z), scale(F(4, 5), X))
            bz_minus = matrix_add(scale(F(3, 5), Z), scale(F(-4, 5), X))
            corr = [expectation(state, (I, Z, bz_plus, I)),
                    expectation(state, (I, Z, bz_minus, I)),
                    expectation(reversed_state, (X, I, bz_plus, I)),
                    expectation(reversed_state, (X, I, bz_minus, I))]
            assert corr == [F(3, 5), F(3, 5), F(4, 5)*r, -F(4, 5)*r]
            score = corr[0]+corr[1]+corr[2]-corr[3]
            assert score == F(6, 5) + F(8, 5)*r
            # Δ = |0><0| - |e1><e1|; trace distance of this pair is d.
            delta = ((d*d, -r*d), (-r*d, -d*d))
            assert matmul(delta, delta) == scale(d*d, I)
            p_guess = (1+d)/2
            assert (1-2*(1-p_guess))**2 + r*r == 1
            # Include E in the coherent inverse, then undo M.
            recovered = undo_memory(recover_environment(state, r, d))
            assert recovered == {(0, 0, 0, 0): F(1), (1, 0, 1, 0): F(1)}
            rcorr = [expectation(recovered, (X, I, bz_plus, I)),
                     expectation(recovered, (X, I, bz_minus, I))]
            assert rcorr == [F(4, 5), F(-4, 5)]
            # The optimum over Bob's real symmetric angles is bounded by
            # 2*sqrt(1+r²). Check the Cauchy bound on rational unit vectors.
            for nn in range(1, 9):
                for mm in range(nn+1):
                    u = F(mm, nn)
                    c, s = (1-u*u)/(1+u*u), 2*u/(1+u*u)
                    assert c*c+s*s == 1
                    assert (c+r*s)**2 <= 1+r*r
            if r == F(3, 5) and d == F(4, 5):
                witness = {'overlap': str(r), 'trace_distance': str(d),
                           'optimal_environment_guess_probability': str(p_guess),
                           'fixed_angles_correlations': [str(c) for c in corr],
                           'fixed_angles_CHSH': str(score),
                           'score_after_coherent_environment_recovery': '14/5'}
            cases += 1
    assert witness is not None
    result = {
        'status': 'passed',
        'scope': 'Pure four-qubit controlled-record circuit; unconditional measurements, E outside reversal unless explicitly recovered; not a subject, consciousness, general measurement or gravity model.',
        'rational_environment_cases': cases,
        'fixed_angle_score': '6/5 + 8*r/5',
        'fixed_angle_violation_condition': 'r > 1/2',
        'optimized_symmetric_angle_score': '2*sqrt(1+r^2)',
        'witness': witness,
        'limitations': 'Record-guess probabilities refer to explicitly prepared branch states; all-label-recovery, arbitrary channels, nonideal noise, and temporal experience supervenience are not established.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
