"""Two continuous, timelessly conditioned completions of the sphere echo.

The 20-state space is the actual clock-labelled orbit, not the full physical
Hilbert space. The 40-state phase reference and generators are extra stipulated
resources. No cosmic energy, subject, or experienced quality is inferred.
"""
from fractions import Fraction as F
import unittest
import numpy as np

from verification.zero_echo_intrinsic_constitution_selection_test import (
    disagreement_by_tick, simple_paths, current_and_recovered,
)
from verification.zero_structural_time_data_echo_test import b_record_laws
from verification.zero_clock_finite_reservoir_reuse_test import Q as THERMAL

N,L=20,40
K=np.arange(N)
F20=np.exp(2j*np.pi*np.outer(np.arange(N),K)/N)/np.sqrt(N)
M=np.arange(L)


def lambdas(alias):
    return K+20*alias*(K==10)


def reference_phase(l):
    return np.exp(2j*np.pi*M*l/L)/np.sqrt(L)


def two_clock_history(alias):
    # On the sphere orbit, F20[:,k] are W eigenvectors. R's spectral m
    # labels have conjugate signed generator -m. Different lambdas choose
    # different joint stationary histories while retaining the same orbit.
    v=np.zeros((N,L),complex)
    for k,m in enumerate(lambdas(alias)):
        v[:,m]+=F20[:,k]/np.sqrt(N)
    return v


def conditional(alias,l):
    return np.sqrt(L)*(two_clock_history(alias)@reference_phase(l).conj())


def actual_echo_minus_probability(t,aux):
    return sum(p for (b,r),p in b_record_laws(aux)[t].items() if r==1)


class ActionFlowContinuousStationaryTests(unittest.TestCase):
    def test_both_histories_satisfy_exact_stationary_constraint(self):
        for alias in (0,1):
            v=two_clock_history(alias);lam=lambdas(alias)
            k_op=(F20*lam)@F20.conj().T
            constraint=k_op@v-v*M[None,:]
            np.testing.assert_allclose(constraint,0,atol=2e-13)
            self.assertAlmostEqual(np.linalg.norm(v),1,places=13)
            # The system/orbit density, after R is traced out, is identical
            # in the two joint preparations. It is a dephased mixed state,
            # NOT the pure unaugmented sphere history.
            np.testing.assert_allclose(v@v.conj().T,np.eye(N)/N,atol=2e-13)
            for l in range(L):
                p=np.linalg.norm(v@reference_phase(l).conj())**2
                self.assertAlmostEqual(p,1/L,places=13)

    def test_equal_on_all_original_integer_readings(self):
        shift=np.roll(np.eye(N,dtype=complex),1,axis=0)
        for step in range(N):
            expected=np.linalg.matrix_power(shift,step)[:,0]
            for alias in (0,1):
                np.testing.assert_allclose(conditional(alias,2*step),expected,atol=2e-13)
        # Identical on the sphere's entire 20-step sample but not asserted
        # to be identical between those steps or for the reference itself.
        h0=np.ones(N,complex)/np.sqrt(N)
        for alias in (0,1):
            k_op=(F20*lambdas(alias))@F20.conj().T
            np.testing.assert_allclose(k_op@h0,0,atol=2e-13)

    def test_half_step_distinguishes_the_two_physical_completions(self):
        a,b=conditional(0,1),conditional(1,1)
        self.assertAlmostEqual(abs(np.vdot(a,b))**2,F(81,100),places=13)
        # Global optimal binary discrimination given the reference event,
        # conditional on explicitly allowing the required joint observable.
        trace_distance=np.sqrt(1-abs(np.vdot(a,b))**2)
        self.assertAlmostEqual(trace_distance,np.sqrt(19)/10,places=13)
        c=1/np.tan(np.pi/40)
        self.assertAlmostEqual(abs(a[0])**2,(1+c*c)/400,places=13)
        self.assertAlmostEqual(abs(b[0])**2,(1+(c-2)**2)/400,places=13)
        self.assertAlmostEqual(abs(a[0])**2-abs(b[0])**2,(c-1)/100,places=13)
        self.assertAlmostEqual(abs(a[0])**2,0.4061190969939714,places=13)
        self.assertAlmostEqual(abs(b[0])**2,0.2890570496322241,places=13)

    def test_actual_echo_record_and_quality_candidates_at_half_step(self):
        # Measuring only the echo register traces the orthogonal sphere clock
        # labels. Therefore the actual reduced E probability is the mixture
        # of the true echo probabilities with the conditional orbit weights.
        expected=(0.003940893982717493,0.019366296894434303)
        for aux in (F(0),THERMAL):
            rminus=np.array([float(actual_echo_minus_probability(t,aux)) for t in range(N)])
            # For the previously defined physical signs s*j and s*j*r,
            # disagreement is exactly r=-; no phenomenal assumption.
            np.testing.assert_allclose(rminus,
                 np.array([float(x) for x in disagreement_by_tick()[:N]]),atol=1e-14)
            for alias in (0,1):
                weights=abs(conditional(alias,1))**2
                self.assertAlmostEqual(float(weights@rminus),expected[alias],places=13)
                self.assertAlmostEqual(sum(weights),1,places=13)
        # Explicitly check physical s-counterpart balance within each echo
        # outcome at the half-step, for both candidate sign observables.
        for alias in (0,1):
            weights=abs(conditional(alias,1))**2
            totals=np.zeros((2,2))
            for b,z,s,w,path in simple_paths():
                for t in range(N):
                    _,j,r=path[t]
                    a,c=current_and_recovered(s,j,r)
                    totals[r]+=weights[t]*float(w)*np.array([a,c])
            np.testing.assert_allclose(totals,0,atol=1e-13)
        # These physical means do not establish an experiential measure.

    def test_completions_are_not_just_reparameterizations_of_same_clock(self):
        a,b=conditional(0,1),conditional(1,1)
        # Identical joint conditional states at each *same* reference reading
        # would be required for a passive change of a common clock coordinate.
        self.assertLess(abs(np.vdot(a,b))**2,1)
        self.assertEqual(set(lambdas(0))-set(lambdas(1)),{10})
        self.assertEqual(set(lambdas(1))-set(lambdas(0)),{30})
        # They have distinct joint states, constraints and occupied reference
        # spectral supports in one fixed basis, and identical coarse ticks.

if __name__=='__main__':unittest.main()
