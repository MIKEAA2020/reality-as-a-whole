"""Mathematical controls motivated by Saketh et al. (2026).

These are invented processes and data, NOT the study's EEG or a replication.
They test what an ACW-50 summary, pooled correlation, and signed difference
can logically establish. Nothing here diagnoses or measures experience.
"""
import math
import unittest
import numpy as np


def first_half_window(acf):
    return next(i for i,a in enumerate(acf) if a<=.5)


def tied_ranks(x):
    x=np.asarray(x)
    return np.array([1+np.sum(x<value)+(np.sum(x==value)-1)/2 for value in x])


class NondualityTimescaleIdentifiabilityTests(unittest.TestCase):
    def test_equal_half_windows_can_hide_different_autocorrelations(self):
        # Both functions are valid unit-variance stationary Gaussian ACFs:
        # the second is a weighted sum of two independent AR(1) processes.
        k=np.arange(40)
        one=.8**k
        mixture=.7*.9**k+.3*.4**k
        self.assertEqual(first_half_window(one),4)
        self.assertEqual(first_half_window(mixture),4)
        self.assertAlmostEqual(one[3],.512,places=12)
        self.assertAlmostEqual(mixture[3],.5295,places=12)
        self.assertAlmostEqual(one[4],.4096,places=12)
        self.assertAlmostEqual(mixture[4],.46695,places=12)
        self.assertGreater(np.max(abs(one-mixture)),.1)
        toeplitz=lambda a: np.fromfunction(lambda i,j:a[abs(i-j).astype(int)],(12,12))
        for a in (one,mixture):self.assertGreater(np.linalg.eigvalsh(toeplitz(a)).min(),0)

    def test_same_entire_marginal_acfs_allow_different_joint_relations(self):
        # Stationary bivariate AR(1), M=.8I. Innovation covariance is
        # (1-.8²)Σ. All choices yield exactly the same marginal ACF .8**k.
        a=.8
        for rho in (0,.8,-.8):
            sigma=np.array([[1.,rho],[rho,1.]])
            noise=(1-a*a)*sigma
            self.assertGreater(np.linalg.eigvalsh(sigma).min(),0)
            self.assertGreater(np.linalg.eigvalsh(noise).min(),0)
            np.testing.assert_allclose(a*a*sigma+noise,sigma,atol=1e-14)
            for k in range(8):
                gamma=a**k*sigma
                np.testing.assert_allclose(np.diag(gamma),[a**k,a**k],atol=1e-14)
                self.assertAlmostEqual(gamma[0,1],rho*a**k,places=13)
        self.assertAlmostEqual(-.5*math.log(1-.8**2),.5108256237659908,places=13)
        # Same marginal ACF and ACW, but correlation can be zero or ±.8.
        # This joint-process example is not the paper's sequential tasks.

    def test_pooled_correlation_does_not_establish_a_within_group_relation(self):
        x=np.array([g+dx for g in range(3) for dx in (-.1,-.1,.1,.1)])
        y=np.array([2-g+dy for g in range(3) for dy in (-.1,.1,-.1,.1)])
        for g in range(3):
            xx=x[4*g:4*g+4];yy=y[4*g:4*g+4]
            self.assertAlmostEqual(np.corrcoef(xx,yy)[0,1],0,places=12)
            self.assertAlmostEqual(np.corrcoef(tied_ranks(xx),tied_ranks(yy))[0,1],0,places=12)
        self.assertLess(np.corrcoef(x,y)[0,1],-.98)
        self.assertLess(np.corrcoef(tied_ranks(x),tied_ranks(y))[0,1],-.9)
        # A logical possibility, not an analysis of the real participants.

    def test_zero_difference_is_not_zero_components_or_signed_experience(self):
        a,b=4.,4.
        self.assertEqual(a-b,0)
        self.assertNotEqual(a,0)
        # The two quantities are positive descriptive times; opposite signs
        # in their difference are a comparison convention, not two valences.
        self.assertGreater(a,0);self.assertGreater(b,0)

if __name__=='__main__':unittest.main()
