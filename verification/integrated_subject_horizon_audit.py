#!/usr/bin/env python3
"""Exact horizon sensitivity in the integrated candidate's existing spin sector.

The counterfactual pulse, random initial background and subsequent dynamics are
explicit model choices. A change of horizon changes the causal query; it is not
in itself an invariance theorem, a phenomenal assay or a subject transition.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from pathlib import Path
import json

from coupled_subject_boundary_gate import STATES, flip_probability, stationary
from causal_influence_subject_gate import influence_graph, score
from competing_subject_constitution_rules import overlapping_local_maxima

V = tuple(range(4))
T = F(1, 4)
PAIRS = {frozenset((0, 1)), frozenset((2, 3))}
WHOLE = {frozenset(V)}


def kernel(t):
    out = {}
    for s in STATES:
        row = {}
        for i in V:
            u = tuple(-v if j == i else v for j, v in enumerate(s))
            row[u] = row.get(u, F(0)) + flip_probability(s, i, t) / 4
        row[s] = 1 - sum(row.values(), F(0))
        assert sum(row.values()) == 1 and all(p >= 0 for p in row.values())
        out[s] = row
    return out


def advance(dist, k):
    result = {s: F(0) for s in STATES}
    for s, mass in dist.items():
        for u, probability in k[s].items():
            result[u] += mass * probability
    return result


def encode_sets(sets):
    return [sorted(s) for s in sorted(sets, key=lambda x: (len(x), sorted(x)))]


def mismatch(s, edge=(0, 1)):
    i, j = edge
    return (1 - s[i] * s[j]) // 2


def main():
    k = kernel(T)
    # Initial pulse: set j to +/-1, randomize the other three spins uniformly;
    # after the pulse, all four sites evolve, including j. No sustained clamp.
    distributions = {(j, a): {s: F(1, 8) for s in STATES if s[j] == a}
                     for j in V for a in (-1, 1)}
    one_update = influence_graph(T)[1]
    rows = []
    for horizon in range(1, 10):
        distributions = {key: advance(d, k) for key, d in distributions.items()}
        def effect(j, i):
            return (sum(p for s, p in distributions[j, 1].items() if s[i] == 1)
                    - sum(p for s, p in distributions[j, -1].items() if s[i] == 1))
        directed = {(j, i): effect(j, i) for j in V for i in V if i != j}
        pair = {(i, j): min(directed[i, j], directed[j, i])
                for i, j in combinations(V, 2)}
        assert all(v >= 0 for v in pair.values())
        # At one random-site update this is exactly one quarter of the
        # old conditional local-update influence, including zero nonedges.
        if horizon == 1:
            assert all(pair[e] == one_update[e] / 4 for e in pair)
        winners, ties = overlapping_local_maxima(frozenset(V), pair)
        assert not ties
        assert winners == (PAIRS if horizon <= 8 else WHOLE)
        # Check graph relabeling equivariance of the same horizon-specific rule.
        for perm in permutations(V):
            pp = {tuple(sorted((perm[i], perm[j]))): w for (i, j), w in pair.items()}
            w2, t2 = overlapping_local_maxima(frozenset(V), pp)
            assert w2 == {frozenset(perm[i] for i in s) for s in winners}
            assert t2 == {frozenset(perm[i] for i in s) for s in ties}
        rows.append({
            'horizon_updates': horizon,
            'symmetric_influences': {f'{i}-{j}': str(w) for (i, j), w in pair.items()},
            'left_pair_score': str(score({0, 1}, pair)),
            'whole_score': str(score(V, pair)),
            'L_winners': encode_sets(winners),
            'L_unresolved_ties': encode_sets(ties),
        })
    # The same fixed physical kernel supports incompatible experiential labels.
    # Show both directions of change of the physical mismatch at equilibrium.
    equilibrium = stationary(T, (None,) * 4)
    assert advance(equilibrium, k) == equilibrium
    joint = {(a, b): F(0) for a in (0, 1) for b in (0, 1)}
    for s, p in equilibrium.items():
        for u, q in k[s].items():
            joint[mismatch(s), mismatch(u)] += p * q
    assert sum(joint.values()) == 1
    assert sum(joint[1, b] for b in (0, 1)) == F(1, 4)
    assert joint[0, 1] > 0 and joint[1, 0] > 0
    # A and B have the identical physics; A labels q=1 unpleasant and B
    # labels q=0 unpleasant. Both are stipulated to contain experiences.
    # Their physical laws agree because the same k is used, not as a general
    # theorem about every possible causal theory of experience.
    result = {
        'status': 'passed',
        'cross_tanh': str(T),
        'intervention': 'one initial +/- pulse with other sites uniform, then free random-site heat bath',
        'horizons': rows,
        'relabelings_checked_per_horizon': 24,
        'stationary_mismatch_transition_joint': {f'{a}->{b}': str(p) for (a,b),p in joint.items()},
        'experiential_rivals': {
            'A': 'q=1 unpleasant; q=0 neutral',
            'B': 'q=0 unpleasant; q=1 neutral',
            'status': 'both labels postulated, same physical kernel by construction; no subject or report bridge inferred',
        },
        'scope': 'Finite toy sector; horizon-dependent queries, not a proof of description invariance, real subject count, valence, or persistence.',
    }
    text = json.dumps(result, indent=2) + '\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
