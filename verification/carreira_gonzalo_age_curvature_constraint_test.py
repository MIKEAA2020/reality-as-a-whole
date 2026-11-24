"""Finite, open and contingent book: FLRW age/curvature and dust clock test.

Idealized classical FLRW, dust plus curvature and Lambda, no radiation.
Dimensionless parameters, a0=H0=8πG=1 and a fiducial comoving volume 1.
A Hamiltonian constraint is not asserted to be a physical whole energy.
"""
import math
import unittest
import numpy as np

NODES, WEIGHTS = np.polynomial.legendre.leggauss(128)
U=(NODES+1)/2
W=WEIGHTS/2


def e2(a, om, ok, ol):
    return om/a**3+ok/a**2+ol


def age(om,ok,ol):
    # a=u² removes the matter-era square-root endpoint singularity.
    return float(np.sum(W*2*U**2/np.sqrt(om+ok*U**2+ol*U**6)))


def open_matched_age(target):
    lo,hi=1e-5,.99999
    if not age(hi,1-hi,0)<target<age(lo,1-lo,0):
        raise ValueError('age outside model range')
    for _ in range(80):
        mid=(lo+hi)/2
        if age(mid,1-mid,0)>target:lo=mid
        else:hi=mid
    return (lo+hi)/2


def luminosity_distance(z,om,ok,ol):
    zz=z*U
    chi=float(np.sum(W*z/np.sqrt(om*(1+zz)**3+ok*(1+zz)**2+ol)))
    if ok>1e-12:
        dm=math.sinh(math.sqrt(ok)*chi)/math.sqrt(ok)
    elif ok< -1e-12:
        dm=math.sin(math.sqrt(-ok)*chi)/math.sqrt(-ok)
    else:
        dm=chi
    return (1+z)*dm  # in units c/H0


def deceleration(a,om,ok,ol):
    return (om/(2*a**3)-ol)/e2(a,om,ok,ol)


def constraint_parts(a,om,ok,ol):
    # C=-p_a²/(12a)-3ka+Λa³+P_T, with k=-ok, Λ=3ol.
    H=math.sqrt(e2(a,om,ok,ol))
    p=-6*a*a*H
    return np.array([-p*p/(12*a),3*ok*a,3*ol*a**3,3*om])


def hamiltonian_acceleration(a,om,ok,ol):
    k=-ok;lam=3*ol
    p=-6*a*a*math.sqrt(e2(a,om,ok,ol))
    da=-p/(6*a)
    dp=-p*p/(12*a*a)+3*k-3*lam*a*a
    return -dp/(6*a)+p*da/(6*a*a)


class CarreiraGonzaloAgeCurvatureConstraintTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.flat=(.3,0.,.7)
        cls.agematch=age(*cls.flat)
        cls.m=open_matched_age(cls.agematch)
        cls.open=(cls.m,1-cls.m,0.)

    def test_flat_dust_einstein_de_sitter_has_two_thirds_age(self):
        self.assertAlmostEqual(age(1.,0.,0.),2/3,places=13)
        self.assertAlmostEqual(deceleration(1.,1.,0.,0.),.5,places=13)

    def test_flat_lambda_counterexample_to_book_inference(self):
        # The book's 0.942 ± 0.065 range includes this exactly flat model.
        self.assertAlmostEqual(self.agematch,.964099381639469,places=12)
        self.assertGreater(self.agematch,2/3)
        self.assertLess(abs(self.agematch-.942),.065)
        self.assertAlmostEqual(deceleration(1,*self.flat),-.55,places=13)

    def test_open_dust_age_and_exactly_matched_open_flat_pair(self):
        self.assertAlmostEqual(age(.044,.956,0),.940406815069854,places=12)
        self.assertAlmostEqual(self.m,.021460704452916,places=12)
        self.assertAlmostEqual(age(*self.open),self.agematch,places=13)
        self.assertAlmostEqual(deceleration(1,*self.open),self.m/2,places=13)
        self.assertGreater(deceleration(1,*self.open),0)
        # The positive-lambda flat model accelerates; the age-matched
        # matter+curvature open model decelerates at the present epoch.

    def test_same_age_same_hubble_but_different_distance_redshift(self):
        expected=[(.5,.661476502430917,.622999671494847),
                  (1.,1.542854132855623,1.489397356071697),
                  (2.,3.628413612813331,3.937184341123428)]
        for z,flat,op in expected:
            self.assertAlmostEqual(luminosity_distance(z,*self.flat),flat,places=12)
            self.assertAlmostEqual(luminosity_distance(z,*self.open),op,places=12)
        # These are mathematical predictions of toy models, not a data fit.
        delta=5*math.log10(luminosity_distance(.5,*self.open)/
                           luminosity_distance(.5,*self.flat))
        self.assertAlmostEqual(delta,-.1301330186848146,places=12)

    def test_finite_constraints_in_both_curvatures_at_multiple_clock_readings(self):
        for model in (self.flat,self.open):
            for a in (.1,.3,1.,2.):
                grav,curv,vac,dust=constraint_parts(a,*model)
                self.assertAlmostEqual(grav+curv+vac+dust,0,places=11)
                self.assertLess(grav,0)
                self.assertGreater(dust,0)
                # Dust's P_T is constant and dT/dτ=∂C/∂P_T=1 at N=1;
                # hence the monotone T is a physical matter clock.
                self.assertAlmostEqual(dust,3*model[0],places=13)
                self.assertAlmostEqual(hamiltonian_acceleration(a,*model),
                    -deceleration(a,*model)*a*e2(a,*model),places=12)
        np.testing.assert_allclose(constraint_parts(1,*self.flat),[-3,0,2.1,.9],atol=1e-13)
        np.testing.assert_allclose(constraint_parts(1,*self.open),
            [-3,3*(1-self.m),0,3*self.m],atol=1e-13)

    def test_dust_local_density_is_nonzero_despite_zero_constraint(self):
        for model in (self.flat,self.open):
            for a in (.25,1.,2.):
                rho=3*model[0]/a**3
                self.assertGreater(rho,0)
                self.assertAlmostEqual(rho*a**3,3*model[0],places=12)
                self.assertAlmostEqual(sum(constraint_parts(a,*model)),0,places=11)
        # This is a comoving fiducial-cell constraint, not a proven global
        # energy or consciousness, and no initial data are derived from zero.

    def test_hubble_age_not_curvature_criterion_in_general(self):
        # q0 and Ht depend on matter/pressure/Lambda as well as k. Flat
        # radiation has Ht=1/2 and flat dust Ht=2/3; for this flat Lambda
        # example Ht>2/3. No claim all solutions obey the latter inequality.
        self.assertAlmostEqual(age(1,0,0),2/3,places=13)
        self.assertGreater(age(*self.flat),2/3)
        self.assertGreater(age(*self.open),2/3)
        self.assertNotEqual(self.flat[1],self.open[1])

if __name__=='__main__':
    unittest.main()
