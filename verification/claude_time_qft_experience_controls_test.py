"""Small-system controls; not a claim of physical collapse or experience."""
import math
import unittest
import numpy as np

I=np.eye(2, dtype=complex)
X=np.array([[0,1],[1,0]], dtype=complex)
Y=np.array([[0,-1j],[1j,0]], dtype=complex)
Z=np.diag([1.,-1.]).astype(complex)
P0=(I+Z)/2
P1=(I-Z)/2
H=np.array([[1,1],[1,-1]],dtype=complex)/np.sqrt(2)
CNOT=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],dtype=complex)


def partial_e(r):
    return np.einsum('aibi->ab',r.reshape(2,2,2,2))


def modular(r, a, s):
    vals, vec = np.linalg.eigh(r)
    u=(vec*np.exp(1j*s*np.log(vals)))@vec.conj().T
    return u@a@u.conj().T


def dephase(a):
    return (a+Z@a@Z)/2


class QFTExperienceControls(unittest.TestCase):
    def test_records_postselection_and_eraser(self):
        plus=np.array([1.,1.])/np.sqrt(2)
        zero=np.array([1.,0.])
        psi=CNOT@np.kron(plus,zero)
        joint=np.outer(psi,psi.conj())
        np.testing.assert_allclose(partial_e(joint),I/2)
        self.assertAlmostEqual(np.trace(joint@np.kron(Z,Z)).real, 1.)
        init=np.outer(plus,plus.conj())
        selected=P0@init@P0
        self.assertAlmostEqual(np.trace(selected).real,.5)
        np.testing.assert_allclose(selected/.5,P0)
        erased=np.kron(I,H)@joint@np.kron(I,H)
        for outcome,p in enumerate((P0,P1)):
            unnorm=partial_e(np.kron(I,p)@erased@np.kron(I,p))
            prob=np.trace(unnorm).real
            self.assertAlmostEqual(prob,.5)
            conditional=unnorm/prob
            np.testing.assert_allclose(conditional,(I+(-1)**outcome*X)/2,atol=1e-14)
            self.assertAlmostEqual(np.trace(conditional@Z).real,0.)
            for phi in (0.,.5,math.pi):
                phase=np.diag([1.,np.exp(1j*phi)])
                result=np.trace((I+X)/2@phase@conditional@phase.conj().T).real
                self.assertAlmostEqual(result,(1+(-1)**outcome*math.cos(phi))/2)
        restored=CNOT@psi
        np.testing.assert_allclose(restored,np.kron(plus,zero))
        np.testing.assert_allclose(partial_e(erased),I/2,atol=1e-14)

    def test_coarse_graining_fails_modular_intertwining(self):
        r=.6; s=.7; a=math.atanh(r)
        rho=(I+r*X)/2
        actual=dephase(modular(rho,Z,s))
        output=modular(dephase(rho),dephase(Z),s)
        np.testing.assert_allclose(actual,math.cos(2*a*s)*Z,atol=1e-14)
        np.testing.assert_allclose(output,Z,atol=1e-14)
        self.assertAlmostEqual(np.linalg.norm(actual-output,2),abs(1-math.cos(2*a*s)))
        diagonal=(I+r*Z)/2
        for operator in (I,X,Y,Z):
            np.testing.assert_allclose(dephase(modular(diagonal,operator,s)),
                                       modular(dephase(diagonal),dephase(operator),s),atol=1e-14)

    def test_affine_equations(self):
        # Equal right sides require b=0 over any field; sample both signs.
        for a in (-3.,.5,2.):
            for x in (-2.,0.,4.):
                for b in (-1.,.3):
                    self.assertNotAlmostEqual(a*x+b,a*x)
        # Without the independent second equation, affine maps exist.
        self.assertEqual(2*3+1,7)

    def test_subject_quality_underdetermination(self):
        data={'o1':'d','o2':'d'}
        assignments=[{'o1':'red','o2':'blue'}, {'o1':'blue','o2':'red'}]
        for assignment in assignments:
            self.assertEqual(set(assignment), set(data))
            self.assertEqual(set(assignment.values()), {'red','blue'})
        self.assertNotEqual(assignments[0]['o1'], assignments[1]['o1'])

    def test_simultaneous_fixed_points(self):
        # Algebraic reduction of first pair is (p-1)^2=0.
        for p in (0.,.5,.9,1.):
            self.assertAlmostEqual((1+p*p)/2-p,(p-1)**2/2)
        for p in (.5,.7,1.):
            q=2*p-1
            self.assertAlmostEqual(p,(1+q)/2)


if __name__ == '__main__':
    unittest.main()
