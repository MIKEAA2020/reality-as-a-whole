#!/usr/bin/env python3
"""Finite stage-lineage bookkeeping, not evidence for any subject theory."""
from itertools import combinations, product
import json
from pathlib import Path

VERTICES = (0, 1)
EDGES = tuple(product(VERTICES, repeat=2))


def subsets(items):
    items = tuple(items)
    return [frozenset(c) for n in range(len(items) + 1) for c in combinations(items, n)]


def mutual_unique(edges):
    """A deliberately strict candidate: both endpoints have degree one."""
    return frozenset((u, v) for u, v in edges
                     if sum(x == u for x, _ in edges) == 1
                     and sum(y == v for _, y in edges) == 1)


def matching(edges):
    return len({u for u, _ in edges}) == len(edges) == len({v for _, v in edges})


def unique_maximum(edges):
    candidates = [m for m in subsets(edges) if matching(m)]
    mx = max(map(len, candidates))
    best = [m for m in candidates if len(m) == mx]
    # In a tie, leave all links unresolved/unasserted; not a biological death rule.
    return best[0] if len(best) == 1 else frozenset()


def relabel(edges, left_swap, right_swap):
    return frozenset((u ^ left_swap, v ^ right_swap) for u, v in edges)


def stage_components(layers):
    """Equivalence classes of consecutive-layer mutual-unique links."""
    vertices = {(t, x) for t in range(len(layers) + 1) for x in VERTICES}
    adjacency = {v: set() for v in vertices}
    for t, layer in enumerate(layers):
        for u, v in mutual_unique(layer):
            x, y = (t, u), (t + 1, v)
            adjacency[x].add(y)
            adjacency[y].add(x)
    classes = []
    while vertices:
        stack = [next(iter(vertices))]
        component = set()
        while stack:
            n = stack.pop()
            if n in component:
                continue
            component.add(n)
            stack.extend(adjacency[n] - component)
        vertices -= component
        classes.append(frozenset(component))
    return classes


def run():
    graphs = subsets(EDGES)
    for graph in graphs:
        for rule in (mutual_unique, unique_maximum):
            selected = rule(graph)
            assert selected <= graph and matching(selected)
            for l, r in product(VERTICES, repeat=2):
                assert rule(relabel(graph, l, r)) == relabel(selected, l, r)

    single = frozenset({(0, 0)})
    fork = frozenset({(0, 0), (0, 1)})
    merge = frozenset({(0, 0), (1, 0)})
    asymmetric = frozenset({(0, 0), (0, 1), (1, 1)})
    assert mutual_unique(single) == unique_maximum(single) == single
    assert mutual_unique(fork) == unique_maximum(fork) == frozenset()
    assert mutual_unique(merge) == unique_maximum(merge) == frozenset()
    assert mutual_unique(asymmetric) == frozenset()
    assert unique_maximum(asymmetric) == frozenset({(0, 0), (1, 1)})

    # Exhaust every two-boundary, 3-stage, 2-slot history and stage relabeling.
    for first, second in product(graphs, repeat=2):
        original = stage_components((first, second))
        assert all(len({t for t, _ in c}) == len(c) for c in original)
        for a, b, c in product(VERTICES, repeat=3):
            transformed = stage_components((relabel(first, a, b), relabel(second, b, c)))
            expected = {frozenset((t, x ^ (a, b, c)[t]) for t, x in group) for group in original}
            assert set(transformed) == expected

    return {
        'status': 'passed',
        'two_by_two_graphs': len(graphs),
        'three_stage_histories': len(graphs) ** 2,
        'three_stage_history_relabelings': len(graphs) ** 2 * 8,
        'single_edge_selected': sorted(map(list, mutual_unique(single))),
        'symmetric_fork_mutual_unique': sorted(map(list, mutual_unique(fork))),
        'symmetric_fork_unique_maximum': sorted(map(list, unique_maximum(fork))),
        'asymmetric_graph_edges': sorted(map(list, asymmetric)),
        'asymmetric_mutual_unique': sorted(map(list, mutual_unique(asymmetric))),
        'asymmetric_unique_maximum': sorted(map(list, unique_maximum(asymmetric))),
        'scope': ('Formal stage-node and graph tests only. Edge inputs are stipulated '
                  'lineage, not derived physical or phenomenal facts. Matching '
                  'and tie conventions are candidate rules, not empirical identity. '
                  'Thin field occurrences are not numerically identified with '
                  'persisting persons. No subject, fission, or metaphysical possibility is established.')
    }


if __name__ == '__main__':
    result = run()
    text = json.dumps(result, indent=2) + '\n'
    Path(__file__).with_suffix('.json').write_text(text, encoding='utf-8')
    print(text, end='')
