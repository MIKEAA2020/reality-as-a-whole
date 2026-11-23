import unittest
from fractions import Fraction as F


def cross_ratio(z):
    a, b, c, d = z
    return (a-b)*(c-d)/((a-c)*(b-d))


def transform(z):
    return (2*z+1)/(z+1)


def incidence(vertex_count, edges):
    B = [[0]*len(edges) for _ in range(vertex_count)]
    for j, (tail, head) in enumerate(edges):
        if not (0 <= tail < vertex_count and 0 <= head < vertex_count) or tail == head:
            raise ValueError('invalid edge')
        B[tail][j] = -1
        B[head][j] = 1
    return B


def products(B, flows):
    return [[F(coefficient)*flow for coefficient,flow in zip(row,flows)] for row in B]


def rank(rows):
    a = [[F(x) for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r,len(a)) if a[i][c]),None)
        if pivot is None:
            continue
        a[r],a[pivot]=a[pivot],a[r]
        a[r]=[x/a[r][c] for x in a[r]]
        for i in range(len(a)):
            if i != r:
                factor = a[i][c]
                a[i]=[x-factor*y for x,y in zip(a[i],a[r])]
        r+=1
        if r == len(a):
            break
    return r


class RelationalSphereCycleTests(unittest.TestCase):
    def setUp(self):
        self.edges=[(0,1),(1,2),(2,3),(3,0)]
        self.B=incidence(4,self.edges)
        self.z=list(map(F,[0,1,2,3]))
        self.q=cross_ratio(self.z)

    def test_lorentz_invariant_nonzero_circulation(self):
        self.assertEqual(self.q,F(1,4))
        self.assertEqual(cross_ratio(list(map(transform,self.z))),self.q)
        cells=products(self.B,[self.q]*4)
        self.assertTrue(all(sum(row)==0 for row in cells))
        values=[x for row in cells for x in row if x]
        self.assertEqual(len(values),8)
        self.assertEqual(values.count(self.q),4)
        self.assertEqual(values.count(-self.q),4)
        self.assertEqual(sum(values),0)

    def test_zero_conservation_does_not_select_amplitude(self):
        for amplitude in [F(0),F(1,4),F(1,3),F(-1,4)]:
            self.assertTrue(all(sum(row)==0 for row in products(self.B,[amplitude]*4)))
        z2=list(map(F,[0,1,2,4]))
        self.assertEqual(cross_ratio(z2),F(1,3))
        self.assertNotEqual(self.q,cross_ratio(z2))

    def test_cycle_has_nonzero_kernel_tree_does_not(self):
        tree=incidence(4,self.edges[:3])
        self.assertEqual(4-rank(self.B),1)
        self.assertEqual(3-rank(tree),0)

    def test_unbalanced_local_exchange_but_global_zero(self):
        cells=products(self.B,[self.q*n for n in (1,2,3,4)])
        nets=[sum(row) for row in cells]
        self.assertEqual(nets,[F(3,4),F(-1,4),F(-1,4),F(-1,4)])
        self.assertEqual(sum(nets),0)
        self.assertEqual(2*nets[0]+sum(nets[1:]),F(3,4))

    def test_global_zero_not_zero_for_arbitrary_incidence_weights(self):
        cells=products(self.B,[self.q]*4)
        weighted=sum(2*x if x>0 else x for row in cells for x in row)
        self.assertEqual(weighted,4*self.q)
        self.assertNotEqual(weighted,0)

    def test_antipodal_partner_not_equivariant_with_translation(self):
        # A(z)=-1/conj(z), A(0)=infinity. For g(z)=z+1,
        # A(g(0))=-1 whereas g(A(0))=infinity.
        z=F(0)
        antipode_after_translate=-1/(z+1)
        translated_antipode='infinity'
        self.assertEqual(antipode_after_translate,-1)
        self.assertNotEqual(antipode_after_translate,translated_antipode)

    def test_reversing_edge_and_flow_is_same_incidences(self):
        forward=products(incidence(2,[(0,1)]),[self.q])
        reversed_representation=products(incidence(2,[(1,0)]),[-self.q])
        self.assertEqual(forward,reversed_representation)


if __name__=='__main__':
    unittest.main()
