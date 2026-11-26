"""Decision gate for an explicitly hypothetical four-spin constitution test.

Exact transition and physical-noise calculations are reused from the existing
sector. Report-error bounds and independent per-episode calibrations are
hypothetical; no empirical subject, mismatch sensor or report calibration.
"""
from fractions import Fraction as F
import math
import unittest

from verification.coupled_subject_boundary_gate import STATES, stationary
from verification.integrated_subject_horizon_audit import kernel, mismatch
from verification.four_spin_mismatch_measurement_gate import majority_failure, posterior


def physical_history():
    p = stationary(F(1, 4), (None,) * 4)
    k = kernel(F(1, 4))
    j = {(a,b): F(0) for a in (0,1) for b in (0,1)}
    for s, mass in p.items():
        for z, probability in k[s].items():
            j[mismatch(s), mismatch(z)] += mass * probability
    return j


def observed_mixture(joint, e, d):
    masses = {}
    for (a,b), mass in joint.items():
        normal = (1-e if a else e)*(1-e if b else e)
        flipped = (e if a else 1-e)*(e if b else 1-e)
        masses[a,b] = mass*((1-d)*normal+d*flipped)
    w = sum(masses.values())
    return w, {c: m/w for c,m in masses.items()}


def model_rates(mixture, false_positive, sensitivity):
    # Extra assumption: a common report channel with the same sensitivity and
    # false positive probability in all true histories and both packages.
    baseline = false_positive
    contrast = sensitivity-false_positive
    level = baseline+contrast*(mixture[0,1]+mixture[1,1])
    onset = baseline+contrast*mixture[0,1]
    return level, onset


def radius(n, delta):
    if n <= 0 or not 0 < delta < 1:
        raise ValueError('invalid n or delta')
    return math.sqrt(math.log(2/delta)/(2*n))


def binomial_tail(n, k, p):
    return sum(math.comb(n,i)*p**i*(1-p)**(n-i) for i in range(k,n+1))


class ConstitutionChallengeTests(unittest.TestCase):
    def test_exact_common_physics_and_which_cell_disagrees(self):
        j=physical_history()
        self.assertEqual(j, {(0,0):F(295,448),(0,1):F(41,448),
                             (1,0):F(41,448),(1,1):F(71,448)})
        level = {(a,b): b for a,b in j}
        onset = {(a,b): int(a==0 and b==1) for a,b in j}
        self.assertEqual([c for c in j if level[c]!=onset[c]], [(1,1)])
        self.assertEqual(sum(j[c] for c in j if level[c]!=onset[c]), F(71,448))

    def test_gauge_independence_of_current_and_history_labels(self):
        for a in (-1,1):
            for b in (-1,1):
                for c in (-1,1):
                    for d in (-1,1):
                        for g0 in (-1,1):
                            for g1 in (-1,1):
                                for tau in (-1,1):
                                    q0=(1-tau*a*b)//2
                                    q1=(1-tau*c*d)//2
                                    tau2=g0*g1*tau
                                    h0=(1-tau2*(g0*a)*(g1*b))//2
                                    h1=(1-tau2*(g0*c)*(g1*d))//2
                                    self.assertEqual((q0,q1),(h0,h1))
                                    self.assertEqual(int(q0==0 and q1==1),int(h0==0 and h1==1))
        # A phase-dependent, independently stipulated time-varying frame must
        # transport its own tau at each time; a passive re-encoding is not a
        # physical change to the preferred relation.

    def test_independent_physical_calibration_mixture_and_error(self):
        j=physical_history(); e=F(19,200); d=majority_failure(19)
        w,mix=observed_mixture(j,e,d)
        self.assertEqual((w,1-mix[1,1]),posterior(j,e,d))
        self.assertEqual(sum(mix.values()),1)
        self.assertEqual(w,F(373009915633097,2405181685760000))
        self.assertEqual(1-mix[1,1],F(2034055896400553,11936317300259104))
        self.assertGreater(mix[1,1],F(4,5))
        self.assertGreater(mix[1,1], 2*F(1,10))

    def test_common_channel_gives_precise_distinct_predictions(self):
        _,mix=observed_mixture(physical_history(),F(19,200),majority_failure(19))
        level,onset=model_rates(mix,F(1,10),F(9,10))
        self.assertEqual(level-onset,F(4,5)*mix[1,1])
        self.assertAlmostEqual(float(level),.8042606012,places=9)
        self.assertAlmostEqual(float(onset),.1405878013,places=9)
        self.assertGreater(level,F(1,2)); self.assertLess(onset,F(1,2))
        # Complete insensitivity invalidates discrimination despite same physics.
        equal=model_rates(mix,F(1,2),F(1,2))
        self.assertEqual(equal,(F(1,2),F(1,2)))

    def test_robust_intervals_and_hypothetical_sample_planning(self):
        w,rho=posterior(physical_history(),F(19,200),majority_failure(19))
        eta=F(1,10); b=eta+rho
        self.assertLess(b,F(1,2))
        # Two-sided fixed-N Hoeffding: CI disjoint from both robust model
        # sets at a midpoint if radius < 1/2-b; no guaranteed power claim.
        n=next(n for n in range(1,10000) if radius(n,.05)<float(F(1,2)-b))
        self.assertEqual(n,35)
        self.assertGreaterEqual(radius(n-1,.05),float(F(1,2)-b))
        # For n=35 the midpoint is not an attainable binary sample mean;
        # n=36 allows the exact k=18 midpoint and hence both rejections.
        n=36
        self.assertLess(radius(n,.05),float(F(1,2)-b))
        all_n=next(total for total in range(n,1000)
                   if binomial_tail(total,n,float(w))>=.95)
        self.assertGreaterEqual(binomial_tail(all_n,n,float(w)),.95)
        self.assertLess(binomial_tail(all_n-1,n,float(w)),.95)
        self.assertEqual(all_n,294)

    def test_decision_rules_do_not_mistake_no_rejection_for_acceptance(self):
        rho=posterior(physical_history(),F(19,200),majority_failure(19))[1]
        b=float(F(1,10)+rho); rad=radius(36,.05)
        def decisions(k):
            lo=max(0,k/36-rad); hi=min(1,k/36+rad)
            return (hi < 1-b, lo > b) # reject level, reject onset
        self.assertEqual(decisions(0),(True,False))
        self.assertEqual(decisions(36),(False,True))
        self.assertEqual(decisions(18),(True,True))
        # Rejection concerns the composite candidate plus assumed calibrations.


if __name__ == '__main__':
    unittest.main()
