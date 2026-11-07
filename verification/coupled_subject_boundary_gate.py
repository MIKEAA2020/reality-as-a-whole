#!/usr/bin/env python3
"""Exact finite Glauber/Ising gate; subject rules are imposed, not derived."""
from fractions import Fraction as F
from itertools import product
from math import log, sqrt
from pathlib import Path
import json

STATES = list(product((-1, 1), repeat=4))
EDGES = ((0, 1), (1, 2), (2, 3))
J = F(1, 2)  # tanh(beta J_internal)
THRESHOLD = F(3, 8)


def weights(t):
    return (J, t, J)


def raw(s, t):
    w = F(1)
    for (i, j), coupling in zip(EDGES, weights(t)):
        w *= 1 + coupling * s[i] * s[j]
    return w


def stationary(t, clamp):
    states = [s for s in STATES if all(c is None or s[i] == c
                                      for i, c in enumerate(clamp))]
    z = sum(raw(s, t) for s in states)
    return {s: raw(s, t) / z for s in states}


def flip_probability(s, i, t):
    # The standard heat-bath resampling probability for the opposite spin.
    plus, minus = F(1), F(1)
    for (a, b), k in zip(EDGES, weights(t)):
        if i in (a,b):
            j = b if i == a else a
            plus *= 1 + k * s[i] * s[j]
            minus *= 1 - k * s[i] * s[j]
    return minus / (plus + minus)


def components(t, threshold):
    adjacency = {i:set() for i in range(4)}
    for (i,j), k in zip(EDGES, weights(t)):
        if k > threshold:
            adjacency[i].add(j)
            adjacency[j].add(i)
    seen, output = set(), []
    for i in range(4):
        if i in seen:
            continue
        component, stack = set(), [i]
        while stack:
            v = stack.pop()
            if v not in component:
                component.add(v)
                stack.extend(adjacency[v] - component)
        seen |= component
        output.append(sorted(component))
    return output


def main():
    # Uniform random site heat bath, restricted to unclamped sites, is
    # reversible with the given Gibbs law. With all sites clamped it is static.
    checks = 0
    rows = []
    for t in (F(0), F(1,4), F(3,4)):
        for clamp in product((None,-1,1), repeat=4):
            d = stationary(t, clamp)
            assert sum(d.values()) == 1
            for s, p in d.items():
                for i, c in enumerate(clamp):
                    if c is not None:
                        continue
                    flipped = tuple(-x if j == i else x for j,x in enumerate(s))
                    assert p * flip_probability(s,i,t) == d[flipped] * flip_probability(flipped,i,t)
                    checks += 1
            # Both subject proposals use this same physical distribution for
            # every report function; this assertion verifies representative
            # local and global readout probabilities sum correctly.
            report_distribution = {(a,b,int(a != b)):F(0)
                                   for a in (-1,1) for b in (-1,1)}
            for s,p in d.items():
                report_distribution[(s[0],s[3],int(s[0] != s[3]))] += p
            assert sum(report_distribution.values()) == 1
        free = stationary(t, (None,)*4)
        corr = sum(p*s[0]*s[3] for s,p in free.items())
        assert corr == J * t * J
        equal = sum(p for s,p in free.items() if s[0] == s[3])
        assert equal == (1+corr)/2
        # Each endpoint pin gives the same probability for matching endpoints.
        for x in (-1,1):
            d = stationary(t, (x,None,None,None))
            assert sum(p for s,p in d.items() if s[3] == x) == equal
        rows.append({'cross_tanh':str(t),
                     'connected_edge_rule_subject_blocks':components(t,F(0)),
                     'threshold_edge_rule_subject_blocks':components(t,THRESHOLD),
                     'endpoint_correlation':str(corr),
                     'matching_endpoint_report_probability':str(equal),
                     'hard_clamp_settings_checked':81})
    weak = stationary(F(1,4), (None,)*4)
    zero = stationary(F(0), (None,)*4)
    tv = sum(abs(weak[s]-zero[s]) for s in STATES)/2
    assert tv == F(1,8)
    # Exact TV formula for several positive couplings: TV(P_t,P_0)=t/2.
    for t in (F(1,4), F(1,2**16), F(3,4)):
        d = stationary(t, (None,)*4)
        assert sum(abs(d[s]-zero[s]) for s in STATES)/2 == t/2
    t = 1/(2**16)
    n = 10000
    # log1p avoids cancellation for small t. Bound is only for iid equilibrated
    # full-state snapshots with known hypotheses and equal prior odds.
    from math import log1p
    kl = ((1+t)*log1p(t)+(1-t)*log1p(-t))/2
    bound = max(0.0, (1-sqrt(n*kl/2))/2)
    assert .499 < bound < .5
    result = {'status':'passed', 'coupling_cases':rows,
              'exact_detailed_balance_checks':checks,
              'weak_cross_vs_zero_total_variation':str(tv),
              'tiny_cross_versus_zero_iid_snapshot_test':{
                  'cross_tanh': '1/65536', 'snapshots':n,
                  'kl_one_snapshot_nats':kl,
                  'equal_prior_error_lower_bound_pinsker':bound},
              'scope':'Four-spin ideal classical Gibbs model and explicitly stipulated subject partitions, not brains, conscious systems, a quantum-gravity model, a probability of actualization, or evidence for either subject rule. Interventions are hard spin clamps followed by equilibrium; subject rules under a clamp are not specified. The indistinguishability of subject labels is by construction, not a universal theorem.'}
    text=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
