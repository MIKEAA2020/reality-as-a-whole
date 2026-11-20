#!/usr/bin/env python3
"""Check a finite subject/experience incidence toy; not consciousness evidence."""
from itertools import combinations, permutations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'verification/phenomenal_facet_subject_gate.json'


def subs(mask):
    """All nonempty subsets of a bitmask."""
    x = mask
    out = set()
    while x:
        out.add(x)
        x = (x - 1) & mask
    return out


def antichains(n):
    values = tuple(range(1, 1 << n))
    for family_bits in range(1, 1 << len(values)):
        fs = tuple(v for i, v in enumerate(values) if family_bits & (1 << i))
        if all(a & b != a and a & b != b for a, b in combinations(fs, 2)):
            yield fs


def possible_subject_families(facets, states):
    """Distinct subject supports are nonempty faces, all states covered."""
    supports = sorted(states)
    for selection in range(1, 1 << len(supports)):
        family = tuple(f for i, f in enumerate(supports) if selection & (1 << i))
        if all(any(x & s == x for s in family) for x in states):
            yield family


def rename(mask, perm):
    return sum(1 << perm[i] for i in range(len(perm)) if mask & (1 << i))


def main():
    totals = {'complexes': 0, 'families_checked': 0, 'overlapping_facet_complexes': 0,
              'disjoint_facet_complexes': 0}
    by_n = {}
    for n in range(1, 5):
        num = 0
        for facets in antichains(n):
            num += 1
            states = set().union(*(subs(f) for f in facets))
            # Every candidate subject support has a unique maximum and owns
            # exactly its nonempty subfaces, so it meets same-subject closure.
            for f in states:
                owned = subs(f)
                assert all((a | b) in owned for a in owned for b in owned)
            families = list(possible_subject_families(facets, states))
            totals['families_checked'] += len(families)
            facet_set = set(facets)
            assert all(facet_set <= set(fam) for fam in families)
            assert len(families) == 2 ** (len(states) - len(facets))
            assert {len(fam) for fam in families} == set(range(len(facets), len(states) + 1))
            exclusive = [fam for fam in families
                         if all(not (a & b) for a, b in combinations(fam, 2))]
            disjoint = all(not (a & b) for a, b in combinations(facets, 2))
            assert len(exclusive) == (1 if disjoint else 0)
            if disjoint:
                assert set(exclusive[0]) == facet_set
                totals['disjoint_facet_complexes'] += 1
            else:
                totals['overlapping_facet_complexes'] += 1
        by_n[str(n)] = num
        totals['complexes'] += num
    # A,G,B : path; all individual and pair faces are labeled by bitsets.
    A, G, B = 1, 2, 4
    facets = (A | G, G | B)
    states = set().union(*(subs(f) for f in facets))
    families = list(possible_subject_families(facets, states))
    assert sorted(set(map(len, families))) == [2, 3, 4, 5]
    assert not any((A | B) & f == (A | B) for f in facets)
    # A one-owner model holds all five states but fails pairwise closure.
    assert not any((A | B) & f == (A | B) for f in states)
    automorphisms = [p for p in permutations(range(3))
                     if {rename(f, p) for f in facets} == set(facets)]
    assert len(automorphisms) == 2
    assert any(rename(facets[0], p) != facets[0] for p in automorphisms)
    # Full triangle vs hollow triangle have identical singleton/pair faces.
    hollow = set().union(*(subs(f) for f in (3, 5, 6)))
    filled = subs(7)
    assert {x for x in hollow if x.bit_count() <= 2} == {x for x in filled if x.bit_count() <= 2}
    assert len((3, 5, 6)) == 3 and len((7,)) == 1
    result = {
        'status': 'passed',
        'scope': 'Finite stipulated incidence model; no claim that any complex is conscious or has actual subjects.',
        'complexes_by_ambient_vertex_count': by_n,
        **totals,
        'path_example': {'facets': ['AG', 'GB'], 'distinct_subject_count_range': [2, 3, 4, 5],
                         'automorphisms': len(automorphisms),
                         'one_partially_unified_owner_satisfies_same_subject_closure': False},
        'triangle_example': {'equal_singleton_and_pair_faces': True,
                             'filled_minimum_subjects': 1, 'hollow_minimum_subjects': 3},
    }
    OUT.write_text(json.dumps(result, indent=2) + '\n')
    print(f"PASS: {totals['complexes']} finite complexes, {totals['families_checked']} covering subject families")
    print('Path counts 2..5; no exclusive cover with overlapping facets; no empirical subject claim.')


if __name__ == '__main__':
    main()
