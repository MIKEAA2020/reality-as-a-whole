#!/usr/bin/env python3
"""Exact identifiability and a common-cause countermodel for three probes.

Z and H are abstract binary random variables, not established experiences.
No empirical data, conscious participants, quantum dynamics, or real error
rates are represented by these hypothetical models.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import json

BITS = (-1, 1)


def marginal_two(beta1, beta2):
    out = {}
    for h, x, y in product(BITS, repeat=3):
        p = F(1, 2) * (1 + beta1*h*x)/2 * (1 + beta2*h*y)/2
        out[(x, y)] = out.get((x, y), F(0)) + p
    return out


def law(betas, k, mean_h, model):
    """Same physical H,N,X law; A sets Z=H, B sets Z=H*N."""
    out = {}
    for h, n, x1, x2, x3 in product(BITS, repeat=5):
        p = (1 + mean_h*h)/2 * (1 + k*n)/2
        for beta, x in zip(betas, (x1, x2, x3)):
            p *= (1 + beta*h*x)/2
        z = h if model == 'A' else h*n
        out[(h, n, z, x1, x2, x3)] = p
    assert sum(out.values()) == 1
    return out


def obs(joint):
    out = {}
    for (h, n, z, *xs), p in joint.items():
        key = (h, n, *xs)
        out[key] = out.get(key, F(0)) + p
    return out


def moment(joint, *indices):
    total = F(0)
    for key, p in joint.items():
        v = F(1)
        for idx in indices:
            v *= key[idx]
        total += p*v
    return total


def conditional(joint, given_index, given_value, fn):
    weight = sum(p for key, p in joint.items() if key[given_index] == given_value)
    return sum(p*fn(key) for key, p in joint.items()
               if key[given_index] == given_value) / weight


def sqrt_fraction(q):
    n, d = isqrt(q.numerator), isqrt(q.denominator)
    assert n*n == q.numerator and d*d == q.denominator
    return F(n, d)


def table(joint):
    out = {}
    for key, p in joint.items():
        xs = key[3:]
        out[xs] = out.get(xs, F(0)) + p
    return [{'x': list(xs), 'p': str(p)} for xs, p in sorted(out.items())]


def main():
    # Two fully conditionally independent models: identical observable law,
    # different accuracies, even when all accuracies are at least 1/2.
    tw1 = marginal_two(F(1, 2), F(1, 2))
    tw2 = marginal_two(F(1), F(1, 4))
    assert tw1 == tw2
    assert tw1[(1, 1)] == tw1[(-1, -1)] == F(5, 16)
    assert tw1[(1, -1)] == tw1[(-1, 1)] == F(3, 16)

    betas = (F(1, 2), F(3, 5), F(4, 5))
    # A: candidate experience Z=H. B: Z is a noisy variant of H, but
    # report channels still follow H; conditional independence given Z fails.
    a = law(betas, F(3, 5), F(0), 'A')
    b = law(betas, F(3, 5), F(0), 'B')
    assert obs(a) == obs(b)
    cs = [moment(a, 3, 4), moment(a, 3, 5), moment(a, 4, 5)]
    assert cs == [F(3, 10), F(2, 5), F(12, 25)]
    c12, c13, c23 = cs
    inferred = (sqrt_fraction(c12*c13/c23),
                sqrt_fraction(c12*c23/c13),
                sqrt_fraction(c13*c23/c12))
    assert inferred == betas
    def accuracy(j, probe):
        return sum(p for key, p in j.items() if key[2] == key[probe])
    acc_a = [accuracy(a, i) for i in (3, 4, 5)]
    acc_b = [accuracy(b, i) for i in (3, 4, 5)]
    assert acc_a == [F(3, 4), F(4, 5), F(9, 10)]
    assert acc_b == [F(13, 20), F(17, 25), F(37, 50)]
    # Same positive observed pattern, different likelihood for the declared Z.
    def posterior(j):
        denom = sum(p for key, p in j.items() if key[3:] == (1, 1, 1))
        num = sum(p for key, p in j.items() if key[2] == 1 and key[3:] == (1, 1, 1))
        return num / denom
    assert posterior(a) == F(108, 109)
    assert posterior(b) == F(433, 545)
    # Quantify a violation of independence given Z in model B.
    e12 = conditional(b, 2, 1, lambda key: key[3]*key[4])
    e1 = conditional(b, 2, 1, lambda key: key[3])
    e2 = conditional(b, 2, 1, lambda key: key[4])
    covariance = e12 - e1*e2
    assert covariance == F(24, 125)
    # Two further specified settings that shift H but leave all channels fixed.
    # The two models remain identical on the specified observable variables.
    settings = []
    for mean_h in (F(-1, 2), F(0), F(1, 2)):
        aa, bb = law(betas, F(3, 5), mean_h, 'A'), law(betas, F(3, 5), mean_h, 'B')
        assert obs(aa) == obs(bb)
        settings.append({'mean_H': str(mean_h), 'observable_joint_equal': True,
                         'P_Z_plus_model_A': str(sum(p for key, p in aa.items() if key[2] == 1)),
                         'P_Z_plus_model_B': str(sum(p for key, p in bb.items() if key[2] == 1))})
    output = {
        'status': 'passed',
        'two_probes': {'observable_law_equal': True, 'model_A_accuracies': ['3/4','3/4'],
                       'model_B_accuracies': ['1','5/8'],
                       'law': [{'x': list(k), 'p': str(v)} for k,v in sorted(tw1.items())]},
        'three_probes_balanced': {'observable_distribution': table(a),
             'correlations_12_13_23': [str(c) for c in cs],
             'reconstructed_biases_under_conditional_independence': [str(x) for x in inferred],
             'model_A_accuracies': [str(x) for x in acc_a],
             'model_B_accuracies': [str(x) for x in acc_b],
             'P_Z_plus_given_all_probes_plus_model_A': str(posterior(a)),
             'P_Z_plus_given_all_probes_plus_model_B': str(posterior(b)),
             'model_B_conditional_covariance_X1_X2_given_Z_plus': str(covariance)},
        'specified_settings': settings,
        'scope': 'Abstract latent variables and hypothetical probes, not a verified model of subjective experience. Observable equivalence covers only the declared H, N and probe variables and the listed settings. Candidate Z is directly experienced only if an independent subject/experience interpretation is added. No quantum, empirical, or general impossibility claim.'}
    text = json.dumps(output, indent=2) + '\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
