#!/usr/bin/env python3
"""Bounded partition arithmetic, conditional on supplied unity/error assumptions."""
from itertools import combinations, product, permutations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def partitions(n):
    if n < 1:
        return []
    out = []
    def grow(prefix):
        if len(prefix) == n:
            out.append(tuple(prefix))
            return
        for v in range(max(prefix) + 2):
            grow(prefix + [v])
    grow([0])
    return out


def admissible(n, positives, negatives, a=0, b=0):
    return [p for p in partitions(n)
            if sum(p[i] != p[j] for i,j in positives) <= a
            and sum(p[i] == p[j] for i,j in negatives) <= b]


def counts(ps):
    return sorted({max(p)+1 for p in ps})


def components(n, positives):
    parent = list(range(n))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i,j in positives:
        parent[root(i)] = root(j)
    return [root(i) for i in range(n)]


def main():
    cases = 0
    feasible = 0
    for n in range(1, 5):
        pairs = list(combinations(range(n),2))
        for values in product((-1,0,1), repeat=len(pairs)):
            pos = [p for p,v in zip(pairs,values) if v == 1]
            neg = [p for p,v in zip(pairs,values) if v == -1]
            ps = admissible(n,pos,neg)
            cs = counts(ps)
            comp = components(n,pos)
            bad = any(comp[i] == comp[j] for i,j in neg)
            assert bool(ps) == (not bad)
            if ps:
                feasible += 1
                assert max(cs) == len(set(comp))
                assert cs == list(range(min(cs), max(cs)+1))
            cases += 1
    pos = [(0,1),(2,3)]
    neg = [(0,2),(0,3),(1,2),(1,3)]
    scenarios = {}
    for a,b in [(0,0),(1,0),(2,0),(0,1),(0,4)]:
        ps = admissible(4,pos,neg,a,b)
        scenarios[f'a={a},b={b}'] = {'counts':counts(ps), 'partitions':len(ps)}
    assert scenarios['a=0,b=0']['counts'] == [2]
    assert scenarios['a=1,b=0']['counts'] == [2,3]
    assert scenarios['a=2,b=0']['counts'] == [2,3,4]
    assert scenarios['a=0,b=1']['counts'] == [2]
    assert scenarios['a=0,b=4']['counts'] == [1,2]
    triangle = {'exact':counts(admissible(3,[(0,1),(1,2)],[(0,2)])),
                'one_false_positive':counts(admissible(3,[(0,1),(1,2)],[(0,2)],1,0)),
                'one_false_negative':counts(admissible(3,[(0,1),(1,2)],[(0,2)],0,1))}
    assert triangle == {'exact': [], 'one_false_positive':[2], 'one_false_negative':[1]}
    under = counts(admissible(3,[],[(0,1),(1,2)]))
    assert under == [2,3]
    # A bijection transports the same finite tests, not all factorization changes.
    original = scenarios['a=1,b=0']['counts']
    for perm in permutations(range(4)):
        pp = [tuple(sorted((perm[i],perm[j]))) for i,j in pos]
        nn = [tuple(sorted((perm[i],perm[j]))) for i,j in neg]
        assert counts(admissible(4,pp,nn,1,0)) == original
    # Identical pair incidence but different higher-order face collections.
    pairs = set(combinations(range(3),2))
    def projection(faces):
        return {p for f in faces for p in combinations(sorted(f),2)}
    one = [frozenset(range(3))]
    three = [frozenset(p) for p in pairs]
    assert projection(one) == projection(three) == pairs
    report = {'scope':'Conditional finite combinatorics; no empirical unity assay, experiential bridge or actual subject count.',
              'signed_partial_graphs_checked_n_1_to_4':cases,
              'feasible_exact_graphs':feasible,
              'four_token_example':scenarios,
              'inconsistent_triangle':triangle,
              'partial_negative_chain_counts':under,
              'four_token_permutations_checked':24,
              'overlap_hypergraph_example':{'pair_projection_identical':True, 'maximal_faces':[1,3],
                                            'sharing_or_overlap_assumption':'formal only'}}
    (ROOT/'verification/phenomenal_unity_partition_gate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
