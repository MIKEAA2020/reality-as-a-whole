"""Read out a third-sphere pseudoscalar on the actual angular echo.

The third direction, neutral pointer, gate and checkpoint are stipulated.
Continuous identities use conditional spherical integration; the actual old
vectors are the repository's N=4 post-echo states. This does not demonstrate
spacetime locality, an autonomous detector, experience or energy accounting.
"""
from fractions import Fraction as F
from itertools import product
from math import log, pi, sqrt
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base, output, relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_quantum_angular_echo import embed
from verification.zero_dressed_history_pair import encode_pair, decode_pair
from verification.zero_gauge_angular_pair import physical, charges
from verification.zero_spherical_invariant_echo import rodrigues


def determinant(m,n,p):
    return float(np.dot(m,np.cross(n,p)))


def readout(t,strength=1.):
    """Unitary pointer rotation with unsharpness 0≤strength≤1."""
    if t < -1-1e-12 or t > 1+1e-12:raise ValueError('t outside [-1,1]')
    if not 0<=strength<=1:raise ValueError('invalid strength')
    t=float(np.clip(t,-1,1))*strength
    a=sqrt((1+t)/2);b=sqrt((1-t)/2)
    return np.array([[a,-b],[b,a]])


def bin_second_moment(i,n=4):
    """E[t² | u in equal-width bin i] with p a uniform third sphere."""
    if n<1 or i not in range(n):raise ValueError('invalid bin')
    a=F(-1)+F(2*i,n);b=a+F(2,n)
    e_u2=(a*a+a*b+b*b)/3
    return (1-e_u2)/3


class ChiralityEchoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root=output(active_base())
        cls.old=[initial(v) for v in relative_read(root,4,labels=tuple(range(16)))]

    def test_unitarity_and_kraus_effects(self):
        for t in (-1.,-.82,-.2,0.,.31,.9,1.):
            u=readout(t)
            np.testing.assert_allclose(u.T@u,np.eye(2),atol=3e-16)
            np.testing.assert_allclose(u[:,0]**2,[(1+t)/2,(1-t)/2],atol=3e-16)
        with self.assertRaises(ValueError):readout(1.1)

    def test_tunable_information_and_backaction(self):
        for strength in (0.,.25,.5,1.):
            for t in (-1.,-.2,0.,.4,1.):
                u=readout(t,strength)
                np.testing.assert_allclose(u.T@u,np.eye(2),atol=3e-16)
                self.assertAlmostEqual(u[0,0]**2-u[1,0]**2,strength*t,places=15)
        # Zero coupling obtains no t-information and leaves old rotations in
        # the singlet, though it still rotates the ready pointer by π/4.
        np.testing.assert_allclose(readout(-1,0),readout(1,0),atol=0)
        with self.assertRaises(ValueError):readout(0,1.1)
        x,w=np.polynomial.legendre.leggauss(90)
        u=(x+1)/2
        def leakage(strength):
            total=0.
            for value,weight in zip(u,w):
                a=sqrt(1-value*value)
                c=sum(wj*sqrt((1+strength*a*v)/2) for v,wj in zip(x,w))/2
                total+=weight*2*c*c/2
            return 1-total
        for strength in (.1,.05,.025):
            self.assertAlmostEqual(leakage(strength)/strength**2,1/18,delta=.0001)

    def test_rotations_preserve_and_reflections_reverse_the_coupling(self):
        m=np.array([0.,0.,1.]);n=np.array([.8,0.,.6]);p=np.array([0.,1.,0.])
        r=rodrigues((1,3,-2),.731);reflection=np.diag([1.,-1.,1.])
        t=determinant(m,n,p)
        self.assertAlmostEqual(determinant(r@m,r@n,r@p),t,places=14)
        self.assertAlmostEqual(determinant(reflection@m,reflection@n,reflection@p),-t,places=14)
        x=np.array([[0.,1.],[1.,0.]])
        np.testing.assert_allclose(x@readout(t)[:,0],readout(-t)[:,0],atol=1e-15)
        # The state is covariant under reflection plus pointer exchange. This
        # is not the assertion that the full readout unitary is conjugation invariant.

    def test_exact_conditional_sphere_moments(self):
        values=[bin_second_moment(i) for i in range(4)]
        self.assertEqual(values,[F(5,36),F(11,36),F(11,36),F(5,36)])
        self.assertEqual(sum(values,F(0))/4,F(2,9))
        # Every bin is equally likely in the actual normalized N=4 echo;
        # pointer outcomes have conditional mean t=±E[t² | bin].

    def test_sphere_quadrature_born_probabilities_and_sign_witness(self):
        # Fixed u: t=sqrt(1-u²)v, v uniform on [-1,1]. Quadrature
        # for u and v avoids pretending midpoint t is the continuous model.
        x,w=np.polynomial.legendre.leggauss(300)
        joint=np.outer(w,w)/4
        t=np.sqrt(1-x[:,None]**2)*x[None,:]
        plus=(1+t)/2
        self.assertAlmostEqual(float(np.sum(joint*plus)),.5,places=14)
        self.assertAlmostEqual(float(np.sum(joint*plus*t)),1/9,places=13)
        self.assertAlmostEqual(float(np.sum(joint*np.abs(t))),pi/8,places=5)
        # P(pointer agrees with sign(t)) = (1+E|t|)/2.
        self.assertAlmostEqual(float(np.sum(joint*(1+np.abs(t))/2)),.5+pi/16,places=5)

    def test_all_actual_old_histories_and_both_signs(self):
        expected=[F(5,36),F(11,36),F(11,36),F(5,36)]
        for label,sign in product(range(16),(1,-1)):
            _,v,rows=embed(self.old[label],sign,4);total=norm2(v)
            self.assertGreater(total,0.)
            probs=[sum(norm2(row[i]) for row in rows)/total for i in range(4)]
            np.testing.assert_allclose(probs,[.25]*4,atol=1e-13)
            for i in range(4):
                # For any old-only effect, conditional p integration gives
                # 1/2 times the original bin density operator, not merely
                # equality of its trace. Multipliers are scalar on the vector.
                self.assertAlmostEqual(probs[i]/2,.125,places=13)
                self.assertAlmostEqual(float(expected[i]),float(bin_second_moment(i)),places=14)
            corr=sum(probs[i]*float(expected[i]) for i in range(4))
            self.assertAlmostEqual(corr,2/9,places=13)
            # Joint E[B*T] is corr; E[T|B=±1]=±corr.

    def test_constrained_pair_is_preserved_for_actual_echo_vectors(self):
        for label,sign,i in product((0,7,15),(1,-1),range(4)):
            _,v,rows=embed(self.old[label],sign,4)
            pair=tuple(part[i] for part in rows)
            enc=encode_pair(pair,i,sign)
            for (a,b,z1,z2),vectors in enc.items():
                k=z1
                self.assertEqual(physical(k,i,a,b,z1,z2),1)
                h1,h2,_=charges(k,i,a,b,z1,z2,4,'swap_invariant')
                self.assertEqual(h1+h2,0)
                for t in (-.7,0.,.8):
                    for amp in readout(t)[:,0]:
                        self.assertEqual(physical(k,i,a,b,z1,z2),1)
                        self.assertGreaterEqual(norm2(amp*vectors[0])+norm2(amp*vectors[1]),0.)
            decoded=decode_pair(enc,i,sign,pair[0])
            self.assertLess(sum(norm2(x-y) for x,y in zip(decoded,pair)),1e-24*norm2(v))
        # The continuous gate is a scalar in every old/pair fiber, hence
        # commutes with their pointwise constraint operators analytically.

    def test_coherence_loss_is_not_old_state_invariance(self):
        # m⊥n and (m,n')=(m,-n): t'=-t. The pointer overlap is
        # sqrt(1-t²). Averaging p gives π/4, not 1.
        x,w=np.polynomial.legendre.leggauss(300)
        overlap=sum(weight*float(np.dot(readout(t)[:,0],readout(-t)[:,0])) for t,weight in zip(x,w))/2
        self.assertAlmostEqual(overlap,pi/4,places=6)
        self.assertLess(overlap,.79)
        # This is a kernel value, not the total trace-distance disturbance.

    def test_original_pair_singlet_leakage_when_reference_carries_rotation(self):
        # For fixed |u|, old-only group averaging takes each pointer amplitude
        # to c=E_v sqrt((1+a*v)/2), a=sqrt(1-u²), v uniform. For each
        # recorded branch its normalized old-singlet probability is 2c².
        x,w=np.polynomial.legendre.leggauss(100)
        for u in (0.,.1,.5,.9,1.):
            a=sqrt(1-u*u)
            c=sum(weight*sqrt((1+a*v)/2) for v,weight in zip(x,w))/2
            closed=2*(u+2)**2/(9*(1+u))
            self.assertAlmostEqual(2*c*c,closed,places=5 if u==0 else 12)
        x,w=np.polynomial.legendre.leggauss(48)
        u=(x+1)/2
        p0=sum(weight*(2*(v+2)**2/(9*(1+v))) for v,weight in zip(u,w))/2
        self.assertAlmostEqual(p0,7/9+2*log(2)/9,places=14)
        self.assertAlmostEqual(1-p0,2*(1-log(2))/9,places=14)
        self.assertGreater(1-p0,.068)
        self.assertLess(1-p0,.069)
        # The nonzero amount is not leakage from the *enlarged* diagonal
        # rotation singlet: the third sphere carries the compensating charge.

    def test_inverse_uncomputes_new_record(self):
        for t in np.linspace(-1,1,21):
            u=readout(t);ready=np.array([1.,0.])
            np.testing.assert_allclose(u.T@u@ready,ready,atol=1e-15)
        # The inverse erases the new pointer correlation; it is not a retained record.

if __name__=='__main__':unittest.main()
