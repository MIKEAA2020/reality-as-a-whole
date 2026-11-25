"""Two explicitly synchronized cyclic clocks on the real sphere history orbit.

A reference clock and its phase-locking are added resources, not derived from
zero. The finite cyclic correlations do not establish physical proper time.
"""
from collections import defaultdict
from fractions import Fraction as F
import unittest
import numpy as np
from verification.zero_structural_time_data_echo_test import b_record_laws,guess_b_from_r
from verification.zero_clock_finite_reservoir_reuse_test import Q as THERMAL

N,M=20,4


def shift(n,q=1):
    return np.roll(np.eye(n,dtype=complex),q,axis=0)


def history(q):
    v=np.zeros((N,M),complex)
    for t in range(N):v[t,(q*t)%M]=1/np.sqrt(N)
    return v.reshape(N*M)


def relational_effect(t,r,q):
    # Twirl the kinematic event |t><t| tensor |r><r| by the common
    # 20-step shift. Time labels are orthogonal, so this is a projector.
    d=np.zeros((N,M),float)
    for s in range(N):d[(t+s)%N,(r+q*s)%M]=1
    return np.diag(d.reshape(N*M))


def echo_law_given_reference(q,r,aux=F(0)):
    laws=b_record_laws(aux);selected=[t for t in range(N) if q*t%M==r]
    if not selected:return None
    out=defaultdict(F)
    for t in selected:
        for key,p in laws[t].items():out[key]+=p/F(len(selected))
    return out


class StationaryTwoClockTests(unittest.TestCase):
    def test_stationary_relational_readouts(self):
        for q in (1,2):
            w=np.kron(shift(N),shift(M,q));v=history(q)
            np.testing.assert_allclose(w@v,v,atol=1e-13)
            np.testing.assert_allclose(np.linalg.matrix_power(w,N),np.eye(N*M),atol=1e-13)
            for t in range(N):
                effects=[relational_effect(t,r,q) for r in range(M)]
                np.testing.assert_allclose(sum(effects),np.eye(N*M),atol=1e-13)
                for r,p in enumerate(effects):
                    np.testing.assert_allclose(p@p,p,atol=1e-13)
                    np.testing.assert_allclose(w@p,p@w,atol=1e-13)
                    self.assertAlmostEqual(np.vdot(v,p@v).real,
                        1 if r==q*t%M else 0,places=13)
            self.assertEqual(q*10%M,2 if q==1 else 0)
        # These are complete relational projectors on the history orbit;
        # outside that orbit the full sphere uses the controlled W shift.

    def test_full_controlled_shift_effect_for_noncommuting_system(self):
        # Independent small-system check of the algebra used for the full
        # sphere's controlled shift; this is not the actual sphere circuit.
        x=np.array([[0,1],[1,0]],complex)
        z=np.diag([1,-1]).astype(complex)
        h=np.array([[1,1],[1,-1]],complex)/np.sqrt(2)
        gates=([x,h,z,h,x]*2)
        gates+=list(reversed(gates))  # all chosen gates are involutions
        prefixes=[np.eye(2,dtype=complex)]
        for g in gates:prefixes.append(g@prefixes[-1])
        np.testing.assert_allclose(prefixes[-1],np.eye(2),atol=1e-13)
        w=np.zeros((N*2,N*2),complex)
        for t,g in enumerate(gates):
            dest=(t+1)%N
            w[2*dest:2*dest+2,2*t:2*t+2]=g
        psi=np.array([1,1j],complex)/np.sqrt(2)
        for q in (1,2):
            d=np.kron(w,shift(M,q))
            v=np.zeros(N*2*M,complex)
            for t in range(N):
                v+=np.kron(np.kron(np.eye(N)[:,t],prefixes[t]@psi),np.eye(M)[:,q*t%M])/np.sqrt(N)
            np.testing.assert_allclose(d@v,v,atol=1e-13)
            for t,r in ((7,q*7%M),(10,q*10%M),(10,(q*10+1)%M)):
                pclock=np.diag(np.eye(N)[t]);pr=np.diag(np.eye(M)[r])
                a=(np.eye(2)+z)/2
                term=np.kron(np.kron(pclock,a),pr);observable=np.zeros_like(term)
                for _ in range(N):
                    observable+=term;term=d@term@d.conj().T
                np.testing.assert_allclose(d@observable,observable@d,atol=1e-13)
                expected=(np.vdot(prefixes[t]@psi,a@prefixes[t]@psi).real
                          if r==q*t%M else 0)
                self.assertAlmostEqual(np.vdot(v,observable@v).real,expected,places=13)

    def test_aliasing_and_unequal_reference_support(self):
        self.assertEqual([t for t in range(N) if t%4==2],[2,6,10,14,18])
        self.assertEqual([t for t in range(N) if 2*t%4==2],list(range(1,20,2)))
        self.assertIsNone(echo_law_given_reference(2,1))
        self.assertIsNone(echo_law_given_reference(2,3))
        for aux in (F(0),THERMAL):
            # Born law for B, echo register and a reference-clock readout:
            # q=1 at reference 2 averages five actual ticks, q=2 averages ten.
            self.assertEqual(guess_b_from_r(echo_law_given_reference(1,2,aux)),F(3,5))
            self.assertEqual(guess_b_from_r(echo_law_given_reference(2,2,aux)),F(11,20))
            # Direct conditioning on original clock t=10 still gives B=r_echo.
            self.assertEqual(guess_b_from_r(b_record_laws(aux)[10]),F(1))

    def test_reference_changes_unconditioned_clock_coherence(self):
        # The old clock marginal after tracing reference: off-diagonal
        # components survive exactly when q*t == q*u modulo 4.
        # Compare against the unaugmented pure uniform orbit history.
        pure=np.ones((N,N),complex)/N
        for q in (1,2):
            amp=history(q).reshape(N,M)
            reduced=amp@amp.conj().T
            for t in range(N):
                for u in range(N):
                    self.assertAlmostEqual(reduced[t,u].real,
                        1/N if q*(t-u)%M==0 else 0,places=13)
            self.assertAlmostEqual(np.trace(reduced).real,1,places=13)
            self.assertFalse(np.allclose(reduced,pure))

if __name__=='__main__':unittest.main()
