#!/usr/bin/env python3
"""Exact finite checks for the context-gated intervention example; not data."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
Z = F(0)
O = F(1)
Q = F(1, 4)
GRID = [Q * n for n in range(5)]


def expected(w, mu, rates):
    return sum(w[e] * (mu[e][0] * (1 - rates[e]) + mu[e][1] * rates[e]) for e in range(2))


def calculate(w, mu, rates):
    budget = sum(w[e] * rates[e] for e in range(2))
    fixed = expected(w, mu, [budget] * 2)
    gated = expected(w, mu, rates)
    delta = [mu[e][1] - mu[e][0] for e in range(2)]
    interaction = w[0] * w[1] * (rates[0] - rates[1]) * (delta[0] - delta[1])
    assert gated - fixed == interaction
    return budget, fixed, gated, interaction


def main():
    count = 0
    for w0 in GRID:
        for p0, p1, m00, m01, m10, m11 in product(GRID, repeat=6):
            w = [w0, 1-w0]
            mu = [[m00, m01], [m10, m11]]
            calculate(w, mu, [p0, p1])
            count += 1
    w = [F(1, 2)] * 2
    mu = [[F(1, 2), O], [F(1, 2), Z]]
    examples = []
    for eps in [Z, F(1, 4), F(1, 2), F(3, 4), O]:
        budget, fixed, gated, gain = calculate(w, mu, [1-eps, eps])
        assert budget == F(1, 2)
        assert fixed == F(1, 2)
        assert gain == F(1, 4) - eps / 2
        examples.append({'marker_error': str(eps), 'budget': str(budget), 'fixed': str(fixed),
                         'gated': str(gated), 'gain': str(gain)})
    # When the environment frequencies shift, a previously half-dose fixed baseline
    # no longer matches dose. Recompute it at the deployment population's rate.
    shifted = calculate([F(3, 4), F(1, 4)], mu, [F(3, 4), F(1, 4)])
    assert shifted == (F(5, 8), F(21, 32), F(3, 4), F(3, 32))
    # Conditioning on a binary marker causes a false interaction even if the
    # response depends only on A and M, not the declared environment E.
    # M=0 => mu(A=0)=1/2, mu(A=1)=1; M=1 => mu(A=0)=1/2, mu(A=1)=0.
    # M is correlated with E and remains causally relevant after conditioning on E.
    # s=3/4, f=1/4 give apparent E effects +1/4 and -1/4.
    observed_delta0 = F(3, 4)*F(1, 2) + F(1, 4)*(-F(1, 2))
    observed_delta1 = F(1, 4)*F(1, 2) + F(3, 4)*(-F(1, 2))
    assert (observed_delta0, observed_delta1) == (F(1, 4), -F(1, 4))
    # Both models share P(M|E) and P(Y|do(A),E), but not their
    # joint P(M,Y|do(A),E). Model I depends only on E; model II on M.
    proxy_mu = [[F(1, 2), F(3, 4)], [F(1, 2), F(1, 4)]]
    proxy = calculate(w, proxy_mu, [F(3, 4), F(1, 4)])
    assert proxy == (F(1, 2), F(1, 2), F(9, 16), F(1, 16))
    p_marker0 = [F(3, 4), F(1, 4)]
    def marker_prob(e, m):
        return p_marker0[e] if m == 0 else 1 - p_marker0[e]
    def response(model, e, m, a):
        if a == 0:
            return F(1, 2)
        return proxy_mu[e][1] if model == 'e_only' else (O if m == 0 else Z)
    # Entire Y distribution given E and each randomized A coincides;
    # the joint M,Y distribution differs for some E,A.
    unequal_joint = False
    for e, a, y in product(range(2), repeat=3):
        marginal = []
        for model in ['e_only', 'marker']:
            marginal.append(sum(marker_prob(e, m) * (response(model,e,m,a) if y else 1-response(model,e,m,a)) for m in range(2)))
        assert marginal[0] == marginal[1]
        for m in range(2):
            j0 = marker_prob(e,m)*(response('e_only',e,m,a) if y else 1-response('e_only',e,m,a))
            j1 = marker_prob(e,m)*(response('marker',e,m,a) if y else 1-response('marker',e,m,a))
            unequal_joint |= j0 != j1
    assert unequal_joint
    def gated_outcome(model):
        return sum(w[e]*marker_prob(e,m)*response(model,e,m,1 if m == 0 else 0)
                   for e,m in product(range(2), repeat=2))
    assert gated_outcome('e_only') == proxy[2]
    marker_gated = gated_outcome('marker')
    assert marker_gated == F(3, 4)
    assert marker_gated - proxy[2] == F(3, 16)
    # For E=0,A=1,M=0,Y=1 the corresponding joint probabilities differ.
    assert marker_prob(0,0)*response('e_only',0,0,1) == F(9,16)
    assert marker_prob(0,0)*response('marker',0,0,1) == F(3,4)
    report = {
        'scope': 'Exact finite allocation arithmetic only; not empirical biology or consciousness.',
        'grid_checks': count,
        'formula': 'gain = w0*w1*(p0-p1)*(delta0-delta1)',
        'symmetric_marker_example': examples,
        'shifted_population': {'w0': '3/4', 'w1': '1/4', 'budget': str(shifted[0]),
                               'fixed': str(shifted[1]), 'gated': str(shifted[2]), 'gain': str(shifted[3])},
        'marker_direct_effect_counterexample': {'apparent_effect_in_e0': str(observed_delta0),
                                                 'apparent_effect_in_e1': str(observed_delta1),
                                                 'true_effect_modification_by_E_at_fixed_M': '0',
                                                 'e_only_model_gated': str(proxy[2]),
                                                 'marker_model_gated': str(marker_gated),
                                                 'fixed_in_both': str(proxy[1]),
                                                 'e0_a1_joint_m0_y1': ['9/16', '3/4']}
    }
    (ROOT/'verification/context_gated_variability_gate.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
