"""Controls for local subject candidates and incidence-weighted energy balance.

No graph criterion establishes consciousness, physically justified incidence,
metaphysical possibility, or a relativistic no-signalling mechanism.
"""
from fractions import Fraction as F
from itertools import combinations
import unittest


def partitions(items):
    if not items:
        yield ()
        return
    x,*tail=items
    for p in partitions(tail):
        yield ((x,),)+p
        for i in range(len(p)):
            yield p[:i]+(tuple(sorted((x,)+p[i])),)+p[i+1:]


def graph(extra=None):
    w={(0,1):F(3),(1,2):F(1),(2,3):F(3)}
    if extra is not None: w[(4,5)]=F(extra)
    return w


def modularity(p,w,n):
    m=sum(w.values())
    if m <= 0: raise ValueError('positive total edge weight required')
    degree=[sum(a for (i,j),a in w.items() if i==k or j==k) for k in range(n)]
    return sum(sum(a for (i,j),a in w.items() if i in c and j in c)/m
               -(sum(degree[i] for i in c)/(2*m))**2 for c in p)


def winners(w,n):
    ps=list(partitions(list(range(n))))
    top=max(modularity(p,w,n) for p in ps)
    return top,[p for p in ps if modularity(p,w,n)==top]


def internal_boundary(s,w):
    S=set(s)
    inside=sum(a for (i,j),a in w.items() if i in S and j in S)
    boundary=sum(a for (i,j),a in w.items() if (i in S)!=(j in S))
    return inside,boundary


def minimal_local_candidates(n,w):
    sets=[]
    for k in range(1,n+1):
        for t in combinations(range(n),k):
            inside,boundary=internal_boundary(t,w)
            if inside>boundary: sets.append(frozenset(t))
    return {s for s in sets if not any(t < s for t in sets)}


def rates(n,flows):
    # flow[(i,j)] is signed flow into i from j; keys have i<j.
    h=[F(0)]*n
    for (i,j),f in flows.items(): h[i]+=f; h[j]-=f
    return h


def multiplicities(n,subjects):
    return [sum(weight for support,weight in subjects if i in support) for i in range(n)]


class SubjectLocalityOverlapTests(unittest.TestCase):
    def test_global_modularity_depends_on_disconnected_remote_system(self):
        p17=winners(graph(17),6)
        p18=winners(graph(18),6)
        self.assertEqual(len(list(partitions(list(range(6))))),203)
        self.assertEqual(p17,(F(53,128),[((0,1),(2,3),(4,5))]))
        self.assertEqual(p18,(F(252,625),[((0,1,2,3),(4,5))]))
        self.assertEqual(graph(17)[(1,2)],graph(18)[(1,2)])

    def test_local_minimal_rule_unchanged_on_original_sites(self):
        expected={frozenset((0,1)),frozenset((2,3))}
        self.assertEqual(minimal_local_candidates(4,graph()),expected)
        for m in (17,18,100):
            candidates=minimal_local_candidates(6,graph(m))
            self.assertEqual({s for s in candidates if s <= {0,1,2,3}},expected)
            self.assertIn(frozenset((4,5)),candidates)

    def test_local_rule_allows_overlapping_supports(self):
        w={(0,1):F(1),(1,2):F(1),(2,3):F(1)}
        candidates=minimal_local_candidates(4,w)
        self.assertEqual(candidates,{frozenset((0,1,2)),frozenset((1,2,3))})
        self.assertEqual(candidates.pop().intersection(candidates.pop()),{1,2})

    def test_weighted_incidence_identity_for_overlapping_supports(self):
        subjects=[({0,1,2},F(1)),({1,2,3},F(1))]
        m=multiplicities(4,subjects)
        self.assertEqual(m,[1,2,2,1])
        flows={(0,1):F(-1,2),(1,2):F(0),(2,3):F(0)}
        h=rates(4,flows)
        self.assertEqual(h,[F(-1,2),F(1,2),0,0])
        self.assertEqual(sum(h),0)
        actual=sum(weight*sum(h[i] for i in support) for support,weight in subjects)
        edge=sum((m[i]-m[j])*f for (i,j),f in flows.items())
        self.assertEqual(actual,F(1,2))
        self.assertEqual(actual,edge)

    def test_uniform_multiplicity_suffices_for_all_edge_flows(self):
        flows={(0,1):F(7,3),(1,2):F(-11,7),(2,3):F(9,5)}
        h=rates(4,flows)
        for m in ([F(1)]*4,[F(2)]*4):
            self.assertEqual(sum(a*b for a,b in zip(m,h)),0)

    def test_unequal_multiplicity_can_be_witnessed_by_one_edge(self):
        m=[F(1),F(2),F(2),F(1)]
        for i,j in ((0,1),(2,3)):
            h=rates(4,{(i,j):F(1)})
            self.assertEqual(sum(a*b for a,b in zip(m,h)),m[i]-m[j])
            self.assertNotEqual(sum(a*b for a,b in zip(m,h)),0)

    def test_splitting_by_multiplicity_balances_but_is_new_rule(self):
        subjects=[({0,1,2},F(1)),({1,2,3},F(1))]
        m=multiplicities(4,subjects)
        h=rates(4,{(0,1):F(-1,2)})
        split=sum(weight*sum(h[i]/m[i] for i in support)
                  for support,weight in subjects)
        self.assertEqual(split,0)
        self.assertEqual(sum(h),0)
        # Mathematical sharing does not establish actual subjective incidence.


if __name__ == '__main__': unittest.main()
