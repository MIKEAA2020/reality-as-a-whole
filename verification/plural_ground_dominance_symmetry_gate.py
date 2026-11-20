#!/usr/bin/env python3
"""Symmetry constraint on a stipulated dominant-node selector; no phenomenology."""
from itertools import combinations, permutations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
V = tuple(range(6))
A, B = frozenset(range(3)), frozenset(range(3, 6))
COLORS = (0, 0, 0, 1, 1, 1)


def edge(i, j):
    return tuple(sorted((i, j)))


def automorphisms(edges):
    result = []
    for p in permutations(V):
        if any(COLORS[i] != COLORS[p[i]] for i in V):
            continue
        if {edge(p[i],p[j]) for i,j in edges} == edges:
            result.append(p)
    return result


def fixed_choices(autos, k):
    found = []
    for choice in combinations(V,k):
        s = frozenset(choice)
        if len(s & A) != 1 or len(s & B) != 1:
            continue
        if all(frozenset(p[i] for i in s) == s for p in autos):
            found.append(choice)
    return found


def main():
    triangles = set(combinations(range(3),2)) | set(combinations(range(3,6),2))
    autos = automorphisms(triangles)
    assert len(autos) == 36
    assert fixed_choices(autos,2) == []
    all_choices = [frozenset(c) for c in combinations(V,2) if len(set(c)&A)==1 and len(set(c)&B)==1]
    assert len(all_choices) == 9
    assert all({frozenset(p[i] for i in s) for s in all_choices} == set(all_choices) for p in autos)
    # A point-invariant uniform distribution on the nine choices does not select one.
    for s in all_choices:
        assert any(frozenset(p[i] for i in s) != s for p in autos)
    # Distinguishable hubs, supported by the graph, do yield an equivariant physical selection.
    stars = {edge(0,1),edge(0,2),edge(3,4),edge(3,5)}
    star_autos = automorphisms(stars)
    assert len(star_autos)==4
    assert fixed_choices(star_autos,2)==[(0,3)]
    report={'scope':'Finite physical-graph symmetry only; no experiential incidence or fundamental ontology.',
            'symmetric_graph_automorphisms_preserving_two_marked_components':len(autos),
            'admissible_one_per_component_choices':len(all_choices),
            'automorphism_invariant_choices':0,
            'uniform_distribution_over_choices':'1/9 each; invariant distribution, not a selected outcome',
            'asymmetric_control_automorphisms':len(star_autos),
            'asymmetric_control_unique_invariant_selection':[0,3],
            'warning':'Selection by degree is not evidence a physical node is a subject.'}
    (ROOT/'verification/plural_ground_dominance_symmetry_gate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
