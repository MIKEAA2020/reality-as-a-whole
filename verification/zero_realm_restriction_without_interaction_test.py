"""Restricted succession, retained labels, and conditional relational zero.

Finite ordered sets and exact rational bookkeeping. Neither the richer event
order nor the flow is asserted to be actual physics, consciousness or time.
"""
from fractions import Fraction as F
from itertools import permutations, product
import unittest


def closure(vertices, edges):
    """Strict transitive closure of a finite directed acyclic graph."""
    rel=set(edges)
    while True:
        new=rel | {(a,d) for a,b in rel for c,d in rel if b==c}
        if new==rel: break
        rel=new
    if any(a==b for a,b in rel): raise ValueError('cycle')
    if any(a not in vertices or b not in vertices for a,b in rel):
        raise ValueError('unknown node')
    return frozenset(rel)


def induced(order, subset):
    return frozenset((a,b) for a,b in order if a in subset and b in subset)


def extensions(vertices, order):
    for p in permutations(vertices):
        loc={v:i for i,v in enumerate(p)}
        if all(loc[a]<loc[b] for a,b in order): yield p


def retained(v, surface, order):
    """Most recent surface event in v's past (or v); reject ambiguity."""
    past={s for s in surface if s==v or (s,v) in order}
    maxima={a for a in past if not any((a,b) in order for b in past)}
    if len(maxima)!=1: raise ValueError('no unique prior surface event')
    return next(iter(maxima))


def compressed(seq):
    ans=[]
    for x in seq:
        if not ans or x!=ans[-1]: ans.append(x)
    return tuple(ans)


def divergence(vertices, flow):
    result={v:F(0) for v in vertices}
    for (a,b),f in flow.items():
        result[a]+=f; result[b]-=f
    return result


def chain(n):
    verts=('A',)+tuple('h'+str(i) for i in range(n))+('B',)
    return verts,closure(verts,zip(verts,verts[1:]))


def diamond():
    verts=('A','x','y','B')
    edges=(('A','x'),('A','y'),('x','B'),('y','B'))
    return verts,closure(verts,edges)


def symmetric_flow(n,total):
    return {(a,b):total/n for i in range(n) for a,b in
            (('A','h'+str(i)),('h'+str(i),'B'))}


class RealmRestrictionTests(unittest.TestCase):
    def test_same_two_confined_events_have_arbitrarily_many_internal_links(self):
        signature=frozenset({('A','B')})
        sizes=[]
        for n in range(9):
            v,o=chain(n); sizes.append(len(v))
            self.assertEqual(induced(o,{'A','B'}),signature)
            self.assertEqual([retained(x,{'A','B'},o) for x in v],['A']*(n+1)+['B'])
            self.assertEqual(compressed(retained(x,{'A','B'},o) for x in v),('A','B'))
        self.assertEqual(sizes,list(range(2,11)))

    def test_hidden_order_nonnecessity_even_at_equal_cardinality(self):
        c,co=chain(2); d,do=diamond()
        self.assertEqual(len(c),len(d))
        self.assertEqual(induced(co,{'A','B'}),induced(do,{'A','B'}))
        self.assertEqual(len(list(extensions(c,co))),1)
        self.assertEqual(len(list(extensions(d,do))),2)
        self.assertTrue(('h0','h1') in co)
        self.assertNotIn(('x','y'),do); self.assertNotIn(('y','x'),do)
        # Different cardinality of the strict relation rules out isomorphism.
        self.assertNotEqual(len(co),len(do))

    def test_no_fundamental_linear_order_is_assumed_for_diamond(self):
        v,o=diamond(); orders=list(extensions(v,o))
        self.assertEqual(set(orders),{('A','x','y','B'),('A','y','x','B')})
        for linear in orders:
            self.assertEqual(compressed(retained(x,{'A','B'},o) for x in linear),('A','B'))
        self.assertEqual(o,closure(v,(('A','x'),('A','y'),('x','B'),('y','B'))))

    def test_held_value_is_relative_to_order_not_a_dynamical_force(self):
        v,o=diamond()
        self.assertEqual({x:retained(x,{'A','B'},o) for x in v},
                         {'A':'A','x':'A','y':'A','B':'B'})
        # No clock, physical interaction or material register was provided.

    def test_relabel_all_events_preserves_relational_facts(self):
        v,o=diamond(); surface={'A','B'}
        for perm in permutations(v):
            p=dict(zip(v,perm))
            vo=tuple(p[x] for x in v); oo={(p[a],p[b]) for a,b in o}
            ss={p[x] for x in surface}
            for x in v: self.assertEqual(retained(p[x],ss,oo),p[retained(x,surface,o)])
            self.assertEqual(induced(oo,ss),{(p['A'],p['B'])})
            self.assertEqual(len(list(extensions(vo,oo))),2)

    def test_partial_order_needs_no_automatic_unique_latest_event(self):
        v=('A','C','x'); o=closure(v,(('A','x'),('C','x')))
        with self.assertRaises(ValueError): retained('x',{'A','C'},o)
        with self.assertRaises(ValueError): retained('A',{'C'},o)

    def test_exact_equal_split_from_permutation_symmetry_and_balance(self):
        for n in range(1,9):
            vertices=('A','B')+tuple('h'+str(i) for i in range(n))
            for total in (F(1),F(2,3),F(-4,5)):
                f=symmetric_flow(n,total); div=divergence(vertices,f)
                self.assertEqual(div['A'],total); self.assertEqual(div['B'],-total)
                self.assertEqual(sum(div.values(),F(0)),0)
                self.assertTrue(all(div['h'+str(i)]==0 for i in range(n)))
                self.assertEqual({f['A','h'+str(i)] for i in range(n)},{total/n})
                self.assertEqual({f['h'+str(i),'B'] for i in range(n)},{total/n})

    def test_same_balance_also_allows_unequal_flow(self):
        vertices=('A','x','y','B'); total=F(1)
        for amount in (F(0),F(1,4),F(1,2),F(1)):
            f={('A','x'):amount,('x','B'):amount,
               ('A','y'):total-amount,('y','B'):total-amount}
            self.assertEqual(divergence(vertices,f),{'A':F(1),'x':F(0),'y':F(0),'B':F(-1)})
            self.assertEqual(f['A','x']==f['A','y'],amount==F(1,2))

    def test_chain_and_diamond_share_same_boundary_balance(self):
        verts,o=chain(2)
        fc={(a,b):F(1) for a,b in zip(verts,verts[1:])}
        v,d=diamond(); fd={('A','x'):F(1,2),('x','B'):F(1,2),
                          ('A','y'):F(1,2),('y','B'):F(1,2)}
        for vertices,f in ((verts,fc),(v,fd)):
            div=divergence(vertices,f)
            self.assertEqual((div['A'],div['B']),(F(1),F(-1)))
            self.assertEqual(sum(div.values(),F(0)),0)
        self.assertEqual(induced(o,{'A','B'}),induced(d,{'A','B'}))

    def test_sign_balance_does_not_fix_subject_multiplicity(self):
        for n,m in product(range(1,5),repeat=2):
            signed=[F(1)]*n+[F(-1)]*m
            self.assertEqual(sum(signed),n-m)
            self.assertEqual(sum(signed)==0,n==m)
        # A single + and single - cancel, but altered incidence counts need not.

if __name__=='__main__': unittest.main()
