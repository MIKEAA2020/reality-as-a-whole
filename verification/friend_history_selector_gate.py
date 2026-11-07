#!/usr/bin/env python3
"""Exact decoherence-functional check for the candidate friend-memory selector.

A,M,B,E are qubits; amplitudes are unnormalized by sqrt(2). The code checks a
particular histories family, not whether actual conscious subjects exist.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

I = ((F(1), F(0)), (F(0), F(1)))
Z = ((F(1), F(0)), (F(0), F(-1)))
X = ((F(0), F(1)), (F(1), F(0)))


def mat_add(a, b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))


def scale(c, a):
    return tuple(tuple(c*a[i][j] for j in range(2)) for i in range(2))


def projector(op, sign):
    return scale(F(1, 2), mat_add(I, scale(sign, op)))


def apply(state, op, axis):
    out = {}
    for bits, amp in state.items():
        for newbit in (0, 1):
            target = list(bits)
            target[axis] = newbit
            target = tuple(target)
            out[target] = out.get(target, F(0)) + op[newbit][bits[axis]]*amp
    return {k: v for k, v in out.items() if v}


def undo(state):
    return {(a, m ^ a, b, e): amp for (a, m, b, e), amp in state.items()}


def inner(v, w):
    return sum((val*w.get(k, F(0)) for k, val in v.items()), F(0))/2


def class_state(state, x, y, c, a, b):
    selected = apply(state, projector(Z, c), 1)
    if x == 2:
        selected = undo(selected)
    selected = apply(selected, projector(Z if x == 1 else X, a), 1 if x == 1 else 0)
    bob = mat_add(scale(F(3, 5), Z), scale(F(4 if y == 1 else -4, 5), X))
    return apply(selected, projector(bob, b), 2)


def main():
    cases = 0
    for n in range(1, 13):
        for m in range(n+1):
            t = F(m, n)
            r = (1-t*t)/(1+t*t)
            d = 2*t/(1+t*t)
            state = {(0, 0, 0, 0): F(1), (1, 1, 1, 0): r,
                     (1, 1, 1, 1): d}
            correlations = {}
            for x, y in product((1, 2), repeat=2):
                histories = {(c, a, b): class_state(state, x, y, c, a, b)
                             for c, a, b in product((-1, 1), repeat=3)}
                for h, hp in product(histories, repeat=2):
                    g = inner(histories[h], histories[hp])
                    if h[1:] != hp[1:]:
                        assert g == 0
                    elif h[0] != hp[0]:
                        expected = (F(0) if x == 1 else
                                    F(h[1]*h[2]*(1 if y == 1 else -1), 10)*r)
                        assert g == expected
                actual, dephased = {}, {}
                for a, b in product((-1, 1), repeat=2):
                    v0, v1 = histories[-1, a, b], histories[1, a, b]
                    diagonal = inner(v0, v0)+inner(v1, v1)
                    actual[a, b] = diagonal + 2*inner(v0, v1)
                    dephased[a, b] = diagonal
                    if x == 2:
                        assert diagonal == F(1, 4)
                        assert actual[a, b] == F(1, 4)*(1+a*b*(1 if y == 1 else -1)*F(4, 5)*r)
                assert sum(actual.values()) == sum(dephased.values()) == 1
                actual_e = sum(F(a*b)*p for (a,b),p in actual.items())
                dephased_e = sum(F(a*b)*p for (a,b),p in dephased.items())
                correlations[x,y] = (actual_e,dephased_e)
                tv = sum(abs(actual[k]-dephased[k]) for k in actual)/2
                assert tv == (F(0) if x == 1 else F(2, 5)*r)
            assert correlations[1,1] == correlations[1,2] == (F(3,5), F(3,5))
            assert correlations[2,1] == (F(4,5)*r, F(0))
            assert correlations[2,2] == (-F(4,5)*r, F(0))
            cases += 1
    # For x=2,y=1,a=b=+1,r=1 the two diagonal history weights
    # are 1/5 and 1/20, with off-diagonal 1/10: 1/4+2/10=9/20.
    state = {(0,0,0,0): F(1), (1,1,1,0): F(1)}
    minus = class_state(state, 2, 1, -1, 1, 1)
    plus = class_state(state, 2, 1, 1, 1, 1)
    assert (inner(plus, plus), inner(minus, minus), inner(plus, minus)) == (F(1,5), F(1,20), F(1,10))
    result = {
        'status': 'passed',
        'scope': 'Four-qubit circuit and one fixed projector-based histories family. No proof about consciousness, all possible history families, hidden-variable models or universal time.',
        'rational_environment_cases': cases,
        'read_family_off_diagonals': '0',
        'reverse_family_matching_final_outcomes_off_diagonals': 'a*b*sign(y)*r/10',
        'reverse_unconditioned_distribution_TV_from_dephased': '2*r/5',
        'unit_overlap_plus_plus_example': {'history_c_plus': '1/5', 'history_c_minus': '1/20', 'off_diagonal': '1/10', 'coarse_grained_probability': '9/20'},
        'fixed_settings_CHSH_coherent': '(6+8*r)/5',
        'fixed_settings_CHSH_projective_history_mixture': '6/5',
        'notes': 'Sequential Born weights equal the statistics of an actual unread projective intervention. Non-additivity rejects that particular probability assignment for the coherent protocol, not every possible ontology of experiences.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
