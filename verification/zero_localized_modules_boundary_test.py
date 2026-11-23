"""Physical-locality-preserving partitions and subject boundary energy checks.

The modules, energy allocations and phenomenological identities are hypotheses;
this is not a subject detector or a theory derived from zero.
"""
from fractions import Fraction as F
from math import sqrt
import unittest


def partitions(items):
    if not items:
        yield ()
        return
    first,*rest=items
    for p in partitions(rest):
        yield ((first,),)+p
        for i in range(len(p)):
            yield p[:i]+(tuple(sorted((first,)+p[i])),)+p[i+1:]


def edges(mid=F(1)):
    return {(0,1):F(3),(1,2):F(mid),(2,3):F(3)}


def modularity(p,w):
    m=sum(w.values())
    if m <= 0: raise ValueError('positive total coupling required')
    degree=[sum(v for (i,j),v in w.items() if i==k or j==k) for k in range(4)]
    return sum(sum(v for (i,j),v in w.items() if i in c and j in c)/m
               -(sum(degree[i] for i in c)/(2*m))**2 for c in p)


def maxima(w):
    all_partitions=list(partitions(list(range(4))))
    top=max(modularity(p,w) for p in all_partitions)
    return top,[p for p in all_partitions if modularity(p,w)==top]


def potential_matrix():
    return ((4,-3,0,0),(-3,5,-1,0),(0,-1,5,-3),(0,0,-3,4))


def normal_modes():
    s=sqrt(10)
    raw=((1,1,1,1),(1,-1,-1,1),
         (1,(-1+s)/3,-(-1+s)/3,-1),
         (1,(-1-s)/3,-(-1-s)/3,-1))
    out=[]
    for v in raw:
        n=sqrt(sum(x*x for x in v)); out.append(tuple(x/n for x in v))
    return out,(1,7,5-s,5+s)


class LocalizedModulesBoundaryTests(unittest.TestCase):
    def test_partition_is_unique_maximum_without_fixed_community_count(self):
        top,winners=maxima(edges())
        self.assertEqual(len(list(partitions(list(range(4))))),15)
        self.assertEqual(top,F(5,14))
        self.assertEqual(winners,[((0,1),(2,3))])
        self.assertEqual(modularity(((0,1,2,3),),edges()),0)

    def test_not_always_unique_and_partition_can_change(self):
        top,winners=maxima(edges(6))
        self.assertEqual(top,0)
        self.assertEqual(len(winners),2)
        self.assertIn(((0,1),(2,3)),winners)
        self.assertIn(((0,1,2,3),),winners)
        self.assertEqual(maxima(edges(12))[1],[((0,1,2,3),)])

    def test_normal_modes_are_orthonormal_and_diagonalize_physical_hamiltonian(self):
        modes,eigs=normal_modes(); K=potential_matrix()
        for i in range(4):
            for j in range(4):
                self.assertAlmostEqual(sum(modes[i][k]*modes[j][k] for k in range(4)),
                                       1 if i==j else 0)
            Kv=[sum(K[r][c]*modes[i][c] for c in range(4)) for r in range(4)]
            for x,y in zip(Kv,modes[i]): self.assertAlmostEqual(x,eigs[i]*y)

    def test_localized_interventions_recover_same_graph_in_mode_coordinates(self):
        modes,eigs=normal_modes()
        # In Q=O^T q coordinates, site displacement e_i maps to O^T e_i.
        # Their bilinear physical coupling is invariant, unlike raw mode Hessian.
        for i in range(4):
            for j in range(i+1,4):
                transported=sum(modes[k][i]*eigs[k]*modes[k][j] for k in range(4))
                self.assertAlmostEqual(transported,potential_matrix()[i][j])
        self.assertEqual(edges(),{(0,1):F(3),(1,2):F(1),(2,3):F(3)})

    def test_passive_canonical_shear_preserves_hessian_pairings(self):
        # Site displacement e0,e1 represented by S^-1 e0,e1 after q=S Q.
        S=((F(1),F(1)),(F(0),F(1)))
        Sinv=((F(1),F(-1)),(F(0),F(1)))
        K=((F(4),F(-3)),(F(-3),F(5)))
        Kp=[[sum(S[a][i]*K[a][b]*S[b][j] for a in range(2) for b in range(2))
             for j in range(2)] for i in range(2)]
        d0=(Sinv[0][0],Sinv[1][0]); d1=(Sinv[0][1],Sinv[1][1])
        self.assertEqual(sum(d0[i]*Kp[i][j]*d1[j] for i in range(2) for j in range(2)),K[0][1])
        self.assertNotEqual(Kp[0][1],K[0][1])
        # p=S^-T P supplies the corresponding canonical momentum transformation.

    def test_interface_stores_energy_while_both_local_energies_decrease(self):
        # q=(0,1,0,0), p=(0,1,-1,0); interface spring k=1.
        q1,q2,p1,p2=F(1),F(0),F(1),F(-1)
        d=q1-q2
        subject_a=-d*p1
        subject_b=d*p2
        interface_rate=d*(p1-p2)
        self.assertEqual((subject_a,subject_b,interface_rate),(-1,-1,2))
        self.assertEqual(subject_a+subject_b+interface_rate,0)
        self.assertEqual(subject_a+subject_b,-2)
        q=(F(0),F(1),F(0),F(0)); p=(F(0),F(1),F(-1),F(0))
        total=sum((x*x+y*y)/2 for x,y in zip(q,p))
        total+=sum(k*(q[i]-q[j])**2/2 for (i,j),k in edges().items())
        self.assertEqual(total,F(7,2))

    def test_allocating_interface_energy_forces_balance_but_not_sign(self):
        a,b,du=F(-1),F(-1),F(2)
        values=[]
        for theta in (F(0),F(1,2),F(1)):
            va=a+theta*du
            vb=b+(1-theta)*du
            self.assertEqual(va+vb,0)
            values.append((va,vb))
        self.assertEqual(values,[(-1,1),(0,0),(1,-1)])


if __name__ == '__main__': unittest.main()
