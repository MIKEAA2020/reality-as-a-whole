#!/usr/bin/env python3
"""Tests of a paper's packing idea under separate error budgets, not consciousness data."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import json
from phenomenal_unity_partition_gate import partitions, admissible, counts

ROOT = Path(__file__).resolve().parents[1]


def bad_triangles(n, pos, neg):
    P, N = set(pos), set(neg)
    triangles = []
    for t in combinations(range(n),3):
        es = list(combinations(t,2))
        if sum(e in P for e in es) == 2 and sum(e in N for e in es) == 1:
            triangles.append(es)
    return triangles


def mismatch(p, pos, neg):
    return (sum(p[i] != p[j] for i,j in pos),
            sum(p[i] == p[j] for i,j in neg))


def main():
    cases, comparisons = 0, 0
    # A particular valid weighted certificate for every n<=4 signed partial graph.
    for n in range(1,5):
        edges = list(combinations(range(n),2))
        for vals in product((-1,0,1), repeat=len(edges)):
            pos = [e for e,v in zip(edges,vals) if v == 1]
            neg = [e for e,v in zip(edges,vals) if v == -1]
            ts = bad_triangles(n,pos,neg)
            if ts:
                pos_degree = max(sum(e in t for t in ts) for e in pos)
                neg_degree = max(sum(e in t for t in ts) for e in neg)
                r = F(1,pos_degree)
                lam = F(neg_degree,pos_degree)
                weight = r*len(ts)
                for p in partitions(n):
                    fp, fn = mismatch(p,pos,neg)
                    assert weight <= fp + lam*fn
                    comparisons += 1
            cases += 1
    # Three conflicts share one negative edge, and have disjoint positive edges.
    pos = sorted([(0,i) for i in (2,3,4)] + [(1,i) for i in (2,3,4)])
    neg = [(0,1)]
    triangles = bad_triangles(5,pos,neg)
    assert len(triangles) == 3
    # Standard packing needs total weight <= 1 on the common negative edge.
    standard_weight = F(1)
    weighted = F(3)
    lam = F(3)
    rows = {}
    for a,b in [(2,0),(3,0),(0,1)]:
        ps = admissible(5,pos,neg,a,b)
        rows[f'a={a},b={b}'] = {'counts':counts(ps),'partitions':len(ps),
                                 'weighted_rejects':weighted > a + lam*b}
    assert not admissible(5,pos,neg,2,0)
    assert admissible(5,pos,neg,3,0)
    assert admissible(5,pos,neg,0,1)
    assert not (standard_weight > 2) and weighted > 2
    # Contradictory positive path with negative endpoints but no observed triangle.
    ppath = [(0,1),(1,2),(2,3)]
    npath = [(0,3)]
    assert len(bad_triangles(4,ppath,npath)) == 0
    assert not admissible(4,ppath,npath,0,0)
    # Fully observed ++- triangle has tied minimum disagreement but differing counts.
    ptri, ntri = [(0,1),(1,2)], [(0,2)]
    costs = [(sum(mismatch(p,ptri,ntri)),max(p)+1) for p in partitions(3)]
    optimal = min(x[0] for x in costs)
    optcounts = sorted({k for c,k in costs if c == optimal})
    assert (optimal,optcounts) == (1,[1,2])
    # Complete graph with a zero edge: keeping zero edges when deleting negatives
    # fails; treating zeros as absent and taking positive components succeeds.
    zpos, zneg = [(0,1)], [(1,2)]
    assert counts(admissible(3,zpos,zneg,0,0)) == [2]
    report = {'scope':'Finite checks of mathematical statements only; no experiential measurement or subject inference.',
              'signed_partial_graphs_checked':cases,
              'partition_inequalities_checked':comparisons,
              'shared_negative_star':{'triangles':3,'ordinary_packing_total':str(standard_weight),
                                      'asymmetric_weight':str(weighted),'lambda':str(lam),'budgets':rows},
              'positive_path_contradiction':{'length':3,'bad_triangles':0,'feasible_zero_error':False},
              'ambiguous_optimum':{'disagreements':optimal,'subject_counts':optcounts},
              'zero_edge_interpretation': 'Positive 01, negative 12, zero 02: ignoring zero yields components {01},{2}; keeping zero after deleting negative merges all.'}
    (ROOT/'verification/correlation_clustering_asymmetric_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
