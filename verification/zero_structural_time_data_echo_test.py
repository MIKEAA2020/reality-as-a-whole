"""Test one realization of the DATA/structural-time scaffold on the sphere echo.

The material record and reference oscillator below are extra interventions;
none derives physical time or subjective experience from zero.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_clock_finite_reservoir_reuse_test import BITS3, Q as THERMAL
from verification.zero_sphere_local_constitution_echo_test import twenty_tick_path
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import distribution, words
from verification.zero_joint_constitution_incidence_echo_test import coarse_table


def b_record_laws(qaux):
    """Actual joint Born law for B and the echo register at each tick."""
    laws=[defaultdict(F) for _ in range(21)]
    for ((sign_b,sign_z,s),p),x,f,e in product(coarse_table().items(),BITS3,BITS3,words(1)):
        w=p*F(1,8)*distribution(THERMAL,f)*distribution(qaux,e)
        if not w:
            continue
        b=int(sign_b<0);z=int(sign_z<0)
        for t,(_,_,r) in enumerate(twenty_tick_path(b,x,f,e,((1,),(0,)),z)):
            laws[t][b,r]+=w
    return laws


def guess_b_from_r(law):
    return sum(max(law.get((0,r),F(0)),law.get((1,r),F(0))) for r in (0,1))


class StructuralTimeDataEchoTests(unittest.TestCase):
    def test_actual_complete_label_path_is_reflection_symmetric(self):
        # Includes arbitrary initial echo register, auxiliary/reservoir labels,
        # and old b,z labels; not just an averaged pair density matrix.
        for b,x,f,e,z,r in product((0,1),BITS3,BITS3,words(1),(0,1),(0,1)):
            path=twenty_tick_path(b,x,f,e,((1,),(0,)),z,r)
            for t in range(21):
                self.assertEqual(path[t],path[20-t])
        # The coherent quantum analogue follows gate by gate: the last ten
        # original gates are inverses of the first ten in reverse order.
        # See the existing old-sphere unitary and echo checks; the classical
        # label check above by itself would not prove phase equality.

    def test_accessible_echo_record_gets_then_loses_b_information(self):
        expected=[F(1,2)]*8+[F(3,4),F(3,4),F(1),F(3,4),F(3,4)]+[F(1,2)]*8
        for q in (F(0),THERMAL):
            laws=b_record_laws(q)
            self.assertEqual([guess_b_from_r(law) for law in laws],expected)
            self.assertEqual(laws[10],{(0,0):F(1,2),(1,1):F(1,2)})
            for t in range(21):
                self.assertEqual(laws[t],laws[20-t])

    def test_copy_then_rewind_leaves_partial_arrow_record(self):
        # An additional neutral memory L starts at zero. At midpoint one
        # extra CNOT r->L is performed, then the untouched inverse runs.
        # At pre-midpoint t=7, L=0; at t=13, the old variables have rewound
        # to their t=7 values but L=b. Reversible on full system+L.
        table=defaultdict(F)
        for (sb,sz,s),p in coarse_table().items():
            b=int(sb<0);z=int(sz<0)
            path=twenty_tick_path(b,(0,0,0),(0,0,0),(0,),((1,),(0,)),z)
            self.assertEqual(path[7],path[13])
            self.assertEqual(path[10][2],b)
            l_before=0; l_after=path[10][2]
            table[(0,l_before)]+=p/2
            table[(1,l_after)]+=p/2
        # Equal priors for the 7/13 comparison; L alone optimally guesses
        # side with probability 3/4, not certainty.
        success=sum(max(table.get((0,l),F(0)),table.get((1,l),F(0))) for l in (0,1))
        self.assertEqual(success,F(3,4))
        self.assertEqual(table[(0,0)],F(1,2))
        self.assertEqual(table[(1,0)],F(1,4))
        self.assertEqual(table[(1,1)],F(1,4))

    def test_identical_step_structure_can_have_distinct_reference_readings(self):
        # On the actual 20-dimensional history orbit of the sphere shift W,
        # clock labels make the orbit vectors orthonormal, and W|t>=|t+1>.
        # Different spectral generators realize this same discrete shift
        # after different periods, without changing W or any integer history.
        n=20
        j=np.arange(n)[:,None];k=np.arange(n)[None,:]
        fourier=np.exp(2j*np.pi*j*k/n)/np.sqrt(n)
        def evolve(step_fraction):
            return (fourier*np.exp(-2j*np.pi*np.arange(n)*step_fraction))@fourier.conj().T
        basis=np.eye(n,dtype=complex)
        shift=np.roll(basis,1,axis=0)
        np.testing.assert_allclose(evolve(1/n),shift,atol=2e-14)
        for m in range(n+1):
            np.testing.assert_allclose(evolve(m/n)@basis[:,0],basis[:,m%n],atol=2e-14)
        # In units omega=1, an independently prepared reference oscillator
        # (H=Z/2, initial |+>) gives P(+)=cos^2(T/2).
        # T=pi and T=2pi both implement the same 20 sampled shifts, but
        # yield P(+)=0 and 1 at the common endpoint, respectively.
        for T,p in ((np.pi,0.),(2*np.pi,1.)):
            self.assertAlmostEqual(np.cos(T/2)**2,p,places=13)
            np.testing.assert_allclose(evolve(T/T)@basis[:,0],basis[:,0],atol=2e-14)
        # This is an extra dynamical embedding and reference clock, not a
        # derivation of SI units, relativistic proper time, or cosmic time.

if __name__=='__main__':unittest.main()
