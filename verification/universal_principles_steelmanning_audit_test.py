"""Focused countermodels for a user-supplied polarity/record proposal.

These are exact finite algebra and standard illustrative models, not a
physical derivation of the proposed ontology or phenomenal experience.
"""
from fractions import Fraction as F
from itertools import product
from math import exp
import unittest
import numpy as np


def closure(n,edges):
    reach=[[False]*n for _ in range(n)]
    for i,j in edges:reach[i][j]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):reach[i][j] |= reach[i][k] and reach[k][j]
    return reach


def committor(x,beta=4):
    # q(x)=int_-1^x exp(beta*V(u))du / int_-1^1 exp(beta*V(u))du,
    # V=(u²−1)²/4, for the 1D overdamped Langevin model.
    nodes,w=np.polynomial.legendre.leggauss(100)
    def integral(a,b):
        u=(a+b)/2+(b-a)*nodes/2
        return (b-a)/2*np.sum(w*np.exp(beta*(u*u-1)**2/4))
    return integral(-1,x)/integral(-1,1)


class UniversalPrinciplesSteelmanningAuditTests(unittest.TestCase):
    def test_asymmetric_counts_do_not_mean_asymmetric_signed_totals(self):
        # One positive composite and N smaller negative entries. The number
        # differs but the absolute total signed amounts exactly match.
        for n in range(1,100):
            neg=[-F(1)]*n;pos=[F(n)]
            self.assertEqual(sum(neg)+sum(pos),0)
            self.assertEqual(abs(sum(neg)),sum(pos))
            if n>1:self.assertGreater(pos[0],abs(neg[0]))
        # Equal-magnitude opposite-sign units need equal total counts.
        for a,b in product(range(12),repeat=2):self.assertEqual(a-b==0,a==b)
        # A mirror possibility may have a different incidence weight.
        self.assertEqual(2*F(1)+1*(-F(1)),1)

    def test_neutral_seed_activates_many_balanced_pairs(self):
        def gate(seed,pairs):
            return tuple((1-n,1-m) if seed and n==m else (n,m) for n,m in pairs)
        def charge(pairs):return sum(n-m for n,m in pairs)
        # Exhaustively check conservation and reversibility on all states.
        for seed in (0,1):
            for flat in product((0,1),repeat=6):
                pairs=tuple(zip(flat[::2],flat[1::2]))
                after=gate(seed,pairs)
                self.assertEqual(charge(after),charge(pairs))
                self.assertEqual(gate(seed,after),pairs)
        before=((0,0),)*3
        self.assertEqual(gate(0,before),before)
        self.assertEqual(gate(1,before),((1,1),)*3)

    def test_positive_surface_negative_bulk_balance_is_not_critical_radius(self):
        gamma=F(3);dg=F(2)
        # ΔG/(4π) = γ r² − Δg r³/3.
        energy=lambda r:gamma*r*r-dg*r**3/3
        derivative=lambda r:2*gamma*r-dg*r*r
        critical=2*gamma/dg;zero=3*gamma/dg
        self.assertEqual(critical,F(3));self.assertEqual(zero,F(9,2))
        self.assertEqual(derivative(critical),0)
        self.assertEqual(energy(critical),9)
        self.assertEqual(energy(zero),0)
        self.assertEqual(zero/critical,F(3,2))
        # This is a local free-energy model, not a total cosmic energy.

    def test_committor_is_not_arrhenius_factor(self):
        # Symmetry of V and boundaries forces the saddle committor to 1/2;
        # the barrier factor at β=4 is exp(-1), not this probability.
        self.assertAlmostEqual(committor(0),.5,places=12)
        self.assertGreater(abs(committor(0)-exp(-1)),.1)
        self.assertAlmostEqual(committor(-1),0,places=12)
        self.assertAlmostEqual(committor(1),1,places=12)
        for x in (.2,.4,.7):self.assertAlmostEqual(committor(x)+committor(-x),1,places=12)

    def test_dead_time_fano_is_not_g2_zero(self):
        # Stationary renewal with Exp(λ)+τ interarrival: λ=2, τ=1/2.
        lam=F(2);tau=F(1,2);rate=lam/(1+lam*tau)
        long_fano=1/(1+lam*tau)**2
        self.assertEqual(rate,1);self.assertEqual(long_fano,F(1,4))
        # For window T<τ at most one event: N~Bernoulli(rate*T).
        T=F(1,4);mean=rate*T;short_fano=1-mean
        self.assertEqual(short_fano,F(3,4))
        g2_zero=F(0)
        self.assertNotEqual(g2_zero,long_fano)
        self.assertNotEqual(g2_zero,short_fano)
        # Strongly time-window-dependent F despite g²(0+)=0.

    def test_three_layer_poset_has_positive_finite_growth_probability(self):
        # An explicit 2,4,2 three-layer order on eight naturally labeled
        # elements. Add all 16 adjacent-layer arrows and no others.
        layers=[range(0,2),range(2,6),range(6,8)]
        edges=[(i,j) for a,b in zip(layers,layers[1:]) for i in a for j in b]
        self.assertEqual(len(edges),16)
        reach=closure(8,edges)
        for a in range(3):
            for b in range(3):
                for i in layers[a]:
                    for j in layers[b]:self.assertEqual(reach[i][j],a<b)
        # Transitive percolation, independent p=1/2 candidate edges.
        self.assertEqual(F(1,2)**16 * F(1,2)**(28-16),F(1,2**28))
        # This is one raw growth history's positive probability, not the
        # total probability or an asymptotic theorem about KR orders.

    def test_a_record_is_reversibly_written_and_unwritten(self):
        cnot=np.zeros((4,4),complex)
        for s,m in product(range(2),repeat=2):cnot[2*s+(s^m),2*s+m]=1
        np.testing.assert_allclose(cnot@cnot,np.eye(4),atol=1e-14)
        for s in (0,1):
            state=np.eye(4)[:,2*s]
            first=cnot@state;second=cnot@first
            self.assertAlmostEqual(abs(first[2*s+s])**2,1)
            np.testing.assert_allclose(second,state,atol=1e-14)
        # S=0 and S=1 remain orthogonal globally after unwriting, although
        # the memory M is blank for both. No bath or heat is modeled.

if __name__=='__main__':unittest.main()
