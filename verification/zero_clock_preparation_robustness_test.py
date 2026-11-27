"""Finite controls for clock preparation/correlation robustness."""
import math
import unittest
import numpy as np

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],dtype=complex)
Z=np.diag([1.,-1.]).astype(complex)
PLUS=(I+X)/2
MINUS=(I-X)/2
ZERO=np.diag([1.,0.]).astype(complex)


def dtrace(a,b):
    diff=(a-b+(a-b).conj().T)/2
    return float(np.abs(np.linalg.eigvalsh(diff)).sum()/2)


def marginal_a(rho,da=2,dr=2):
    return np.einsum('irjr->ij',rho.reshape(da,dr,da,dr))


def marginal_r(rho,da=2,dr=2):
    return np.einsum('iris->rs',rho.reshape(da,dr,da,dr))


def bound(eps):
    eps=max(0.,min(1.,eps))
    fidelity=math.sqrt(max(0.,2*eps-eps*eps))
    return min(fidelity,eps+math.sqrt(eps*(1-eps))) if eps<=.5 else fidelity


def cyclic_fiber_instrument(rho):
    """Two-step finite control, not the physical semibounded clock."""
    output=[]
    U=np.kron(Z,Z)
    for proj in (PLUS,MINUS):
        effect=np.kron(proj,PLUS)
        y=np.zeros((2,2),complex)
        for u in (np.eye(4),U):
            branch=effect@u@rho@u.conj().T@effect
            y+=marginal_a(branch)
        output.append(y)
    return output


class ClockPreparationRobustnessTests(unittest.TestCase):
    def test_fixed_marginals_do_not_fix_relational_event(self):
        # Shared +/- preparation and product both have maximally mixed margins.
        correlated=(np.kron(PLUS,PLUS)+np.kron(MINUS,MINUS))/2
        product=np.kron(I/2,I/2)
        np.testing.assert_allclose(marginal_a(correlated),I/2)
        np.testing.assert_allclose(marginal_r(correlated),I/2)
        p_corr=np.trace(cyclic_fiber_instrument(correlated)[0]).real
        p_prod=np.trace(cyclic_fiber_instrument(product)[0]).real
        self.assertAlmostEqual(p_corr,1.)
        self.assertAlmostEqual(p_prod,.5)

    def test_near_pure_marginal_can_have_sqrt_scale_effect(self):
        e=.04
        psi=np.array([math.sqrt(1-e),0,0,math.sqrt(e)],complex)
        rho=np.outer(psi,psi.conj())
        product=np.kron(marginal_a(rho),ZERO)
        self.assertAlmostEqual(dtrace(marginal_r(rho),ZERO),e)
        actual=np.trace(cyclic_fiber_instrument(rho)[0]).real
        baseline=np.trace(cyclic_fiber_instrument(product)[0]).real
        self.assertAlmostEqual(actual-baseline,math.sqrt(e*(1-e)))
        self.assertGreater(actual-baseline,4*e)
        self.assertLessEqual(dtrace(rho,product),bound(e)+1e-12)

    def test_random_mixed_correlated_states_obey_bound(self):
        rng=np.random.default_rng(384)
        for da in (2,4): # da=4 can include an untouched reference
            for strength in (.001,.02,.2,.8,1.):
                for _ in range(8):
                    v=rng.normal(size=(da,da))+1j*rng.normal(size=(da,da))
                    a=v@v.conj().T;a/=np.trace(a)
                    z=rng.normal(size=(2*da,2*da))+1j*rng.normal(size=(2*da,2*da))
                    mixed=z@z.conj().T;mixed/=np.trace(mixed)
                    rho=(1-strength)*np.kron(a,ZERO)+strength*mixed
                    ma=marginal_a(rho,da);mr=marginal_r(rho,da)
                    eps=dtrace(mr,ZERO)
                    joint=dtrace(rho,np.kron(ma,ZERO))
                    self.assertLessEqual(joint,bound(eps)+1e-12)

    def test_product_clock_perturbation_contracts(self):
        # An orthogonal mixing perturbation of a pure |+> clock reaches the
        # TV bound for the orbit-clock POVM; any later channel cannot amplify it.
        e=.03
        gamma=(1-e)*PLUS+e*MINUS
        self.assertAlmostEqual(dtrace(gamma,PLUS),e)
        q=[np.trace(gamma@PLUS).real,np.trace(gamma@MINUS).real]
        tv=(abs(q[0]-1)+abs(q[1]))/2
        self.assertAlmostEqual(tv,e)
        rho=np.array([[.7,.2j],[-.2j,.3]],complex)
        a=cyclic_fiber_instrument(np.kron(rho,PLUS))
        b=cyclic_fiber_instrument(np.kron(rho,gamma))
        joint_distance=sum(dtrace(x,y) for x,y in zip(a,b))
        self.assertLessEqual(joint_distance,e+1e-12)

    def test_exact_pure_marginal_forces_product(self):
        rho_a=np.array([[.6,.1],[.1,.4]],complex)
        rho=np.kron(rho_a,ZERO)
        self.assertEqual(bound(0.),0.)
        self.assertAlmostEqual(dtrace(rho,np.kron(marginal_a(rho),ZERO)),0.)

if __name__=='__main__':unittest.main()
