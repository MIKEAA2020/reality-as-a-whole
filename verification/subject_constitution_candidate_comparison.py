#!/usr/bin/env python3
"""Three stipulated constitution rules on a shared finite Boolean causal sector.

This is not a model of a brain, an experiential assay, or evidence for subjects.
"""
import itertools
import json
import math

NODES = ('a', 'b', 'c', 'd')
CORES = (frozenset(('a', 'b')), frozenset(('c', 'd')))


def transition(state, intervention, coupled):
    """Simultaneous GF(2) update; interventions XOR into next-state nodes."""
    a, b, c, d = (state[x] for x in NODES)
    drive = (b ^ (d if coupled else 0), a, d ^ (b if coupled else 0), c)
    return {node: value ^ intervention[node] for node, value in zip(NODES, drive)}


def observed_edges(coupled):
    """Causal parent edges: interventionally toggle each source, all contexts."""
    edges = set()
    for s in itertools.product((0, 1), repeat=4):
        state = dict(zip(NODES, s))
        for u in itertools.product((0, 1), repeat=4):
            inputs = dict(zip(NODES, u))
            before = transition(state, inputs, coupled)
            for node in NODES:
                changed = dict(state); changed[node] ^= 1
                after = transition(changed, inputs, coupled)
                edges.update((node, dst) for dst in NODES if before[dst] != after[dst])
    return frozenset(edges)


def strongly_connected_components(nodes, edges):
    nodes = frozenset(nodes)
    reach = {node: {node} for node in nodes}
    for a, b in edges:
        if a not in nodes or b not in nodes:
            raise ValueError('edge outside node set')
        reach[a].add(b)
    for k in nodes:
        for i in nodes:
            if k in reach[i]:
                reach[i].update(reach[k])
    unseen = set(nodes); parts = []
    while unseen:
        x = next(iter(unseen))
        component = frozenset(y for y in nodes if y in reach[x] and x in reach[y])
        parts.append(component); unseen.difference_update(component)
    return frozenset(parts)


def subjects(nodes, edges, cores=CORES):
    nodes = frozenset(nodes)
    cores = frozenset(cores)
    if len(cores) != 2 or any(not c or not c <= nodes for c in cores):
        raise ValueError('this toy requires two distinct nonempty marked cores')
    core_list = list(cores)
    if core_list[0] & core_list[1] or frozenset.union(*cores) != nodes:
        raise ValueError('marked cores must partition the nodes')
    scc = strongly_connected_components(nodes, edges)
    # Global support only when both marked cores lie in the same SCC.
    global_supports = frozenset(c for c in scc if all(core <= c for core in cores))
    return {'maximal': scc, 'marked_local': cores, 'nested': cores | global_supports}


def binomial_upper(n, p, at_least):
    return sum(math.comb(n, k) * p**k * (1-p)**(n-k) for k in range(at_least, n+1))


def main():
    rows = []
    for coupled in (False, True):
        edges = observed_edges(coupled)
        assignments = subjects(NODES, edges)
        global_ = frozenset(NODES)
        rows.append({'coupled': coupled,
                     'edges': [list(pair) for pair in sorted(edges)],
                     'subjects': {k: [sorted(x) for x in sorted(v, key=lambda s: (len(s), sorted(s)))] for k, v in assignments.items()},
                     'global_subject_exists': {k: global_ in v for k, v in assignments.items()}})
    print(json.dumps({'scope': 'Invented finite model; subject labels are additional stipulations, not empirical discoveries.',
                      'update': "a'=b xor (g and d) xor u_a; b'=a xor u_b; c'=d xor (g and b) xor u_c; d'=c xor u_d",
                      'cases': rows,
                      'conditional_future_assay': {'n_independent_trials': 30, 'positive_threshold': 16,
                           'false_positive_per_trial_upper_bound': 0.1, 'false_negative_per_trial_upper_bound': 0.1,
                           'null_false_positive_upper_bound': binomial_upper(30, 0.1, 16),
                           'alternative_power_lower_bound': 1-binomial_upper(30, 0.1, 15)}}, indent=2))

if __name__ == '__main__':
    main()
