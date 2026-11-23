import unittest
from fractions import Fraction as F


def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def trace(a): return sum(a[i][i] for i in range(len(a)))


def matadd(a,b): return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scalar(s,a): return [[s*x for x in row] for row in a]


def det2(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def dot(a,b): return sum(x*y for x,y in zip(a,b))


def graph_value(B,q,weights):
    vertex=[sum(B[i][j]*q[j] for j in range(len(q))) for i in range(len(weights))]
    return dot(weights,vertex)


I=[[F(1),F(0)],[F(0),F(1)]]
X=[[F(0),F(1)],[F(1),F(0)]]
Z=[[F(1),F(0)],[F(0),F(-1)]]


class SphereQubitExperientialZeroTests(unittest.TestCase):
    def test_pure_state_is_one_point_on_sphere(self):
        # r=(3/5, 0, 4/5) is a unit Bloch vector.
        rho=scalar(F(1,2),matadd(I,matadd(scalar(F(3,5),X),scalar(F(4,5),Z))))
        self.assertEqual(trace(rho),1)
        self.assertEqual(det2(rho),0)
        self.assertEqual(mm(rho,rho),rho)
        self.assertEqual(trace(mm(rho,X)),F(3,5))
        self.assertEqual(trace(mm(rho,Z)),F(4,5))
        delta=matadd(rho,scalar(F(-1,2),I))
        self.assertEqual(trace(delta),0)
        self.assertNotEqual(delta,[[0,0],[0,0]])

    def test_trace_zero_does_not_imply_zero_state_weighted_mean(self):
        rho=[[F(1),F(0)],[F(0),F(0)]]
        self.assertEqual(trace(Z),0)
        self.assertEqual(trace(mm(rho,Z)),1)
        self.assertEqual(trace(mm(scalar(F(1,2),I),Z)),0)

    def test_mean_zero_does_not_imply_equal_outcome_frequencies_or_trace_zero(self):
        rho=[[F(1,4),F(0)],[F(0),F(3,4)]]
        operator=[[F(3),F(0)],[F(0),F(-1)]]
        self.assertEqual(trace(mm(rho,operator)),0)
        self.assertEqual(trace(operator),2)
        self.assertEqual(rho[1][1],F(3,4))

    def test_bare_boost_changes_selected_inner_product_orthogonality(self):
        u=[F(1),F(1)]; v=[F(1),F(-1)]
        self.assertEqual(dot(u,v),0)
        boost=[[F(2),F(0)],[F(0),F(1,2)]]
        self.assertEqual(det2(boost),1)
        bu=[F(2),F(1,2)]; bv=[F(2),F(-1,2)]
        self.assertEqual(dot(bu,bv)/dot(bu,bu),F(15,17))
        self.assertEqual(dot(bu,bv)**2/(dot(bu,bu)*dot(bv,bv)),F(225,289))
        hprime=[[F(1,4),F(0)],[F(0),F(4)]]
        h_bv=[dot(row,bv) for row in hprime]
        self.assertEqual(dot(bu,h_bv),0)

    def test_passive_spinor_basis_change_preserves_expectation(self):
        A=[[F(2),F(0)],[F(0),F(1,2)]]
        inv=[[F(1,2),F(0)],[F(0),F(2)]]
        rho=scalar(F(1,2),matadd(I,X))
        rho_prime=mm(mm(A,rho),inv)
        observable_prime=mm(mm(A,X),inv)
        self.assertEqual(trace(mm(rho,X)),1)
        self.assertEqual(trace(mm(rho_prime,observable_prime)),1)
        self.assertEqual(mm(rho_prime,rho_prime),rho_prime)

    def test_weighted_graph_balance_criterion_and_controls(self):
        B=[[-1,0,0,1],[1,-1,0,0],[0,1,-1,0],[0,0,1,-1]]
        q=list(map(F,[1,2,3,4]))
        self.assertEqual(graph_value(B,q,[1,1,1,1]),0)
        self.assertEqual(graph_value(B,q,[2,1,1,1]),3)
        # Nonconstant weights can nevertheless balance a particular fixed q.
        self.assertEqual(graph_value(B,q,[1,1,2,0]),0)
        # Such weights do not balance every possible q: isolate edge 2 -> 3.
        self.assertEqual(graph_value(B,[0,1,0,0],[1,1,2,0]),1)


if __name__=='__main__': unittest.main()
