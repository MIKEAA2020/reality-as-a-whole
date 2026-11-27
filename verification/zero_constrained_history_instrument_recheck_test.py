"""Full physical-subspace instrument controls for the finite eraser history."""
import unittest
import numpy as np
from verification.claude_time_formalization_rigor_test import I, X, Z, PX, H, V, PLUS, ZERO, density


class ConstrainedInstrumentRecheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        clock=np.eye(3,dtype=complex)
        he=np.kron(I,H)
        steps=(V,he,V@he)
        cls.vs=(np.eye(4,dtype=complex),steps[0],steps[1]@steps[0])
        cls.u=sum(np.kron(np.outer(clock[:,(k+1)%3],clock[:,k]),steps[k]) for k in range(3))
        cls.c=2*np.eye(12)-cls.u-cls.u.conj().T
        cls.p=(np.eye(12)+cls.u+cls.u@cls.u)/3
        cls.j=sum(np.kron(clock[:,k:k+1],cls.vs[k]) for k in range(3))/np.sqrt(3)
        cls.clock=clock

    def effect(self,k,m):
        pk=density(self.clock[:,k])
        return self.p@np.kron(pk,m)@self.p

    def test_isometry_spans_exactly_constraint_kernel(self):
        np.testing.assert_allclose(self.j.conj().T@self.j,np.eye(4),atol=1e-14)
        np.testing.assert_allclose(self.j@self.j.conj().T,self.p,atol=1e-14)
        np.testing.assert_allclose(self.c@self.j,np.zeros((12,4)),atol=1e-14)
        self.assertEqual(np.linalg.matrix_rank(self.p,tol=1e-12),4)

    def test_effects_instruments_and_mixed_state(self):
        measurements=(np.kron(PX,I),np.kron(I-PX,I))
        # A positive mixed logical input with off-diagonal terms.
        p0=np.kron(PLUS,ZERO)
        p1=np.kron(np.array([1.,-1.])/np.sqrt(2),ZERO)
        rho=.7*density(p0)+.3*density(p1)
        physical=self.j@rho@self.j.conj().T
        total=np.zeros((12,12),dtype=complex)
        output=np.zeros((12,12),dtype=complex)
        for k,v in enumerate(self.vs):
            for m in measurements:  # projectors, so sqrt(m)=m
                effect=self.effect(k,m)
                expected=self.j@v.conj().T@m@v@self.j.conj().T/3
                np.testing.assert_allclose(effect,expected,atol=1e-14)
                kraus=self.j@v.conj().T@m@v@self.j.conj().T/np.sqrt(3)
                np.testing.assert_allclose(kraus.conj().T@kraus,effect,atol=1e-14)
                operation=kraus@physical@kraus.conj().T
                self.assertGreaterEqual(np.linalg.eigvalsh(operation).min(),-1e-14)
                prob=np.trace(operation).real
                self.assertAlmostEqual(prob,(np.trace(rho@v.conj().T@m@v).real)/3)
                total+=effect; output+=operation
        np.testing.assert_allclose(total,self.p,atol=1e-14)
        self.assertAlmostEqual(np.trace(output).real,1.)
        np.testing.assert_allclose(self.p@output@self.p,output,atol=1e-14)

    def test_clock_reading_is_uniform_and_luders_leaves_state_unchanged(self):
        state=self.j@np.kron(PLUS,ZERO)
        physical=density(state)
        for k in range(3):
            e=self.effect(k,np.eye(4))
            np.testing.assert_allclose(e,self.p/3,atol=1e-14)
            kraus=self.p/np.sqrt(3)
            outcome=kraus@physical@kraus.conj().T
            self.assertAlmostEqual(np.trace(outcome).real,1/3)
            np.testing.assert_allclose(outcome/np.trace(outcome),physical,atol=1e-14)
            branch=np.kron(self.clock[:,k],self.vs[k]@np.kron(PLUS,ZERO))
            self.assertAlmostEqual(np.linalg.norm((np.eye(12)-self.p)@branch),np.sqrt(2/3))
            self.assertAlmostEqual(np.linalg.norm(self.c@branch),np.sqrt(6))

    def test_same_effects_allow_orthogonal_retained_outputs(self):
        psi=np.kron(PLUS,ZERO)
        rho=density(self.j@psi)
        clock_kraus=self.p/np.sqrt(3)
        physical_r=self.j@np.kron(Z,I)@self.j.conj().T
        base=clock_kraus@rho@clock_kraus.conj().T
        alternative=physical_r@base@physical_r.conj().T
        self.assertAlmostEqual(np.trace(base).real,1/3)
        self.assertAlmostEqual(np.trace(alternative).real,1/3)
        difference=base/np.trace(base)-alternative/np.trace(alternative)
        self.assertAlmostEqual(np.linalg.norm(difference,ord='nuc')/2,1.)
        np.testing.assert_allclose((physical_r@clock_kraus).conj().T@(physical_r@clock_kraus),
                                   clock_kraus.conj().T@clock_kraus,atol=1e-14)


if __name__=='__main__':
    unittest.main()
