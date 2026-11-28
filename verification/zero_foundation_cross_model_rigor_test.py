"""Cross-check selected zero, clock, gauge, vacuum and modal claims.

Symbolic and finite controls check specified premises, not the actual universe.
"""
import itertools
import unittest
import sympy as sp


a,phi,pa,p,k,lam=sp.symbols('a phi pa p k lam',real=True,nonzero=True)
C=-k*pa**2/(12*a)+p**2/(2*a**3)

def pb(f,g):
    return sp.diff(f,a)*sp.diff(g,pa)-sp.diff(f,pa)*sp.diff(g,a)+sp.diff(f,phi)*sp.diff(g,p)-sp.diff(f,p)*sp.diff(g,phi)

class FoundationCrossModelReview(unittest.TestCase):
    def test_canonical_change_and_mixed_constraint(self):
        chi=phi+lam*sp.log(a); Pa=pa-lam*p/a; Pchi=p
        self.assertEqual(sp.simplify(pb(a,Pa)),1)
        self.assertEqual(sp.simplify(pb(chi,Pchi)),1)
        self.assertEqual(sp.simplify(pb(a,Pchi)),0)
        self.assertEqual(sp.simplify(pb(chi,Pa)),0)
        self.assertEqual(sp.simplify(pb(Pa,Pchi)),0)
        Q,P=sp.symbols('Q P',real=True)
        transformed=sp.expand(C.subs({pa:Q+lam*P/a,p:P}))
        expected=-k*Q**2/(12*a)-k*lam*Q*P/(6*a**2)+(sp.Rational(1,2)-k*lam**2/12)*P**2/a**3
        self.assertEqual(sp.simplify(transformed-expected),0)
        self.assertEqual(sp.simplify(transformed.coeff(P,2).subs(lam**2,6/k)),0)

    def test_critical_clock_is_bad_on_one_branch(self):
        # Use positive symbols for unambiguous square roots.
        A,K,L=sp.symbols('A K L',positive=True); momentum=sp.symbols('momentum',real=True,nonzero=True)
        clock_rate=p/a**3-lam*k*pa/(6*a**2)
        for sigma in [1,-1]:
            actual=clock_rate.subs({a:A,k:K,lam:sp.sqrt(6/K),pa:sigma*sp.sqrt(6/K)*momentum/A,p:momentum})
            self.assertEqual(sp.simplify(actual-(1-sigma)*momentum/A**3),0)
        # The physical scalar kinetic density retains its transformed momentum.
        P=sp.symbols('P',real=True,nonzero=True)
        rho=sp.simplify((p**2/(2*a**6)).subs(p,P))
        self.assertEqual(rho,P**2/(2*a**6))
        self.assertNotIn(lam,rho.free_symbols)

    def test_change_of_clock_agrees_on_valid_branch(self):
        A,K=sp.symbols('A K',positive=True); momentum=sp.symbols('momentum',real=True,nonzero=True)
        chi=phi+lam*sp.log(a)
        change={a:A,k:K,lam:sp.sqrt(6/K),pa:-sp.sqrt(6/K)*momentum/A,p:momentum}
        rate_a=sp.simplify(pb(a,C).subs(change))
        rate_phi=sp.simplify(pb(phi,C).subs(change))
        rate_chi=sp.simplify(pb(chi,C).subs(change))
        self.assertEqual(sp.simplify(rate_a/rate_phi-sp.sqrt(K/6)*A),0)
        self.assertEqual(sp.simplify(rate_chi/rate_phi),2)
        self.assertEqual(sp.simplify(rate_a/rate_chi-sp.sqrt(K/6)*A/2),0)

    def test_phase_space_rescaling_preserves_relational_derivative_on_shell(self):
        F=sp.Function('F')(a,phi,pa,p); T=sp.Function('T')(a,phi,pa,p)
        f=sp.Function('f')(a,phi,pa,p)
        N,D=pb(F,C),pb(T,C)
        defect=sp.simplify(pb(F,f*C)*D-N*pb(T,f*C)-C*(pb(F,f)*D-N*pb(T,f)))
        self.assertEqual(defect,0)
        # This comparison requires f != 0 and both clock rates nonzero.
        specific=sp.factor(pb(a,a**3*C)*pb(phi,C)-pb(a,C)*pb(phi,a**3*C))
        self.assertEqual(sp.simplify(specific-C*pb(a,a**3)*pb(phi,C)+C*pb(a,C)*pb(phi,a**3)),0)

    def test_stress_and_cosmological_shift(self):
        L,rho,delta,kappa=sp.symbols('Lambda rho delta kappa')
        self.assertEqual(sp.simplify((L-kappa*delta)+kappa*(rho+delta)-(L+kappa*rho)),0)
        metric=sp.diag(-1,1,1,1)
        beta=sp.symbols('beta',real=True); gamma=sp.symbols('gamma',positive=True)
        boost=sp.Matrix([[gamma,-gamma*beta,0,0],[-gamma*beta,gamma,0,0],[0,0,1,0],[0,0,0,1]])
        defect=sp.simplify((boost.T*metric*boost-metric).subs(gamma**2,1/(1-beta**2)))
        self.assertEqual(defect,sp.zeros(4))
        self.assertEqual((-rho*metric)[0,0],rho)

    def test_boost_does_not_preserve_spatial_torus_lattice(self):
        beta,L=sp.symbols('beta L',real=True,nonzero=True); gamma=sp.symbols('gamma',positive=True)
        identification=sp.Matrix([0,L,0,0])
        boost=sp.Matrix([[gamma,-gamma*beta,0,0],[-gamma*beta,gamma,0,0],[0,0,1,0],[0,0,0,1]])
        transformed=boost*identification
        self.assertEqual(transformed[0],-gamma*beta*L)
        self.assertNotEqual(transformed[0],0)

    def test_modal_collapse_need_not_identify_semantic_worlds(self):
        # Two distinct semantic worlds share all atoms, and every world sees both.
        # Inductively every formula built from atoms, Boolean operators, □ and ◇
        # has the same truth value at both worlds (successors are nonempty).
        worlds=(0,1); accessible={0:worlds,1:worlds}
        valuations=[{0:x,1:x} for x in (False,True)]
        for pval in valuations:
            for w in worlds:
                diamond=any(pval[v] for v in accessible[w]); box=all(pval[v] for v in accessible[w])
                self.assertEqual(diamond,pval[w]); self.assertEqual(box,pval[w])
        self.assertNotEqual(worlds[0],worlds[1])

    def test_group_inverse_can_be_self_opposite(self):
        # In the nontrivial group Z/2Z, x=1 is its own unique inverse.
        for x in range(2):
            inverses=[y for y in range(2) if (x+y)%2==0]
            self.assertEqual(len(inverses),1)
        self.assertEqual((-1)%2,1)
        # In Z/3Z a nonzero inverse is distinct, but a real-valued additive
        # map of either finite group sends every element to zero.
        self.assertEqual((-1)%3,2)
        for order in (2,3,5):
            for x in range(order):
                self.assertEqual((order*x)%order,0)

    def test_internal_plenitude_does_not_fix_measure(self):
        positions=('left','right'); signs={'left':-1,'right':1}
        # Same full family of internal qualitative queries and support in both measures.
        measures=({'left':sp.Rational(1,4),'right':sp.Rational(3,4)},
                  {'left':sp.Rational(3,5),'right':sp.Rational(2,5)})
        for mu in measures:
            self.assertEqual(sum(mu.values()),1)
            self.assertTrue(all(mu[x]>0 for x in positions))
        self.assertNotEqual(measures[0]['left'],measures[1]['left'])
        # Plenitude concerns every admitted subset of actual positions; empty
        # subsets are not declared possible by that coverage condition.
        for flags in itertools.product([False,True],repeat=2):
            realized={s for s,b in zip(positions,flags) if b}
            self.assertEqual(bool(realized),any(s in realized for s in positions))
        self.assertEqual(signs['left']+signs['right'],0)

if __name__=='__main__':unittest.main()
