"""Exact finite-history, erasure, no-signalling and modular-flow controls.

The finite models are not physical-energy or experiential derivations.
"""
import math
import unittest
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1., -1.]).astype(complex)
P0, P1 = (I+Z)/2, (I-Z)/2
PX = (I+X)/2
H = np.array([[1, 1], [1, -1]], dtype=complex)/np.sqrt(2)
V = np.array([[1, 0, 0, 0], [0, 1, 0, 0],
              [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)
PLUS = np.array([1., 1.], dtype=complex)/np.sqrt(2)
ZERO = np.array([1., 0.], dtype=complex)


def density(v):
    return np.outer(v, v.conj())


def trace_e(rho):
    return np.einsum('aibi->ab', rho.reshape(2, 2, 2, 2))


def trace_ef(rho):
    return np.einsum('abcdbc->ad', rho.reshape(2, 2, 2, 2, 2, 2))


def channel_e(rho, kraus):
    return sum(np.kron(I, k) @ rho @ np.kron(I, k.conj().T) for k in kraus)


def dephase(a):
    return (a + Z@a@Z)/2


def modular(rho, a, s):
    values, vectors = np.linalg.eigh(rho)
    u = (vectors * np.exp(1j*s*np.log(values))) @ vectors.conj().T
    return u @ a @ u.conj().T


class FormalizationRigor(unittest.TestCase):
    def test_no_signalling_even_when_joint_output_changes(self):
        bell = V @ np.kron(PLUS, ZERO)
        rho = density(bell)
        gamma = .7
        amplitude = (np.diag([1., np.sqrt(1-gamma)]),
                     np.array([[0, np.sqrt(gamma)], [0, 0]], dtype=complex))
        for ks in ((I,), (P0, P1), amplitude):
            np.testing.assert_allclose(sum(k.conj().T @ k for k in ks), I, atol=1e-14)
            result = channel_e(rho, ks)
            np.testing.assert_allclose(trace_e(result), I/2, atol=1e-14)
            self.assertAlmostEqual(np.trace(result).real, 1.)
        self.assertGreater(np.linalg.norm(channel_e(rho, amplitude)-rho), .1)
        # Selected outcome on E changes S, unlike the nonselective sum.
        selected = np.kron(I, P0) @ rho @ np.kron(I, P0)
        np.testing.assert_allclose(trace_e(selected)/np.trace(selected), P0, atol=1e-14)

    def test_uncontrolled_copy_survives_marker_reset(self):
        ghz = np.zeros(8, dtype=complex)
        ghz[0] = ghz[7] = 1/np.sqrt(2)
        after = np.kron(V, I) @ ghz
        expected = np.zeros(8, dtype=complex)
        expected[0] = expected[5] = 1/np.sqrt(2)  # |000>+|101>
        np.testing.assert_allclose(after, expected, atol=1e-14)
        reduced = trace_ef(density(after))
        np.testing.assert_allclose(reduced, I/2, atol=1e-14)
        self.assertAlmostEqual(2*abs(reduced[0, 1]), 0.)

    def test_partial_marking_visibility_distinguishability_and_eraser(self):
        for theta in (0., .29, .91, math.pi/2):
            c, sn = math.cos(theta/2), math.sin(theta/2)
            e0=np.array([c,sn], dtype=complex)
            e1=np.array([c,-sn], dtype=complex)
            state=(np.kron(ZERO,e0)+np.kron(np.array([0.,1.]),e1))/np.sqrt(2)
            rho=density(state)
            marginal=trace_e(rho)
            visibility=2*abs(marginal[0, 1])
            distinguishability=np.linalg.norm(density(e0)-density(e1), ord='nuc')/2
            self.assertAlmostEqual(visibility, math.cos(theta))
            self.assertAlmostEqual(distinguishability, math.sin(theta))
            self.assertAlmostEqual(visibility**2+distinguishability**2, 1.)
            for sign in (1, -1):
                marker=(I+sign*Y)/2
                selected=np.kron(I,marker) @ rho @ np.kron(I,marker)
                probability=np.trace(selected).real
                self.assertAlmostEqual(probability, .5)
                s=trace_e(selected)/probability
                self.assertAlmostEqual(np.trace(s@Z).real, 0.)
                self.assertAlmostEqual(2*abs(s[0,1]), 1.)
                for phi in (0., .3, 1.7):
                    phase=np.diag([1., np.exp(1j*phi)])
                    actual=np.trace(PX@phase@s@phase.conj().T).real
                    self.assertAlmostEqual(actual, (1+math.cos(phi+sign*theta))/2)

    def test_modular_intertwining_exact_qubit_criterion(self):
        for r in ((0., 0., 0.), (0., 0., .4), (.6, 0., 0.),
                  (.2, -.3, .4), (-.4, .2, -.1)):
            r=np.array(r)
            R=np.linalg.norm(r)
            rho=(I+r[0]*X+r[1]*Y+r[2]*Z)/2
            output_state=dephase(rho)
            for s in (0., .4, 1.1, 2.3):
                actual=dephase(modular(rho,Z,s))
                if R == 0:
                    factor=1.
                else:
                    nz=r[2]/R
                    factor=nz**2+(1-nz**2)*math.cos(2*math.atanh(R)*s)
                np.testing.assert_allclose(actual,factor*Z,atol=1e-14)
                np.testing.assert_allclose(modular(output_state,Z,s),Z,atol=1e-14)
            if abs(r[0])+abs(r[1]) < 1e-15:
                for a in (I, X, Y, Z, X+2j*Z):
                    for s in (.4, 1.1):
                        np.testing.assert_allclose(dephase(modular(rho,a,s)),
                                                   modular(output_state,dephase(a),s),atol=1e-14)
            else:
                # Choose s so cos(2*a*s) = -1, avoiding accidental return.
                s=math.pi/(2*math.atanh(R))
                self.assertGreater(np.linalg.norm(dephase(modular(rho,Z,s))-Z), .1)

    def test_one_stationary_constrained_record_history(self):
        clock=np.eye(3, dtype=complex)
        he=np.kron(I,H)
        transitions=(V,he,V@he)
        np.testing.assert_allclose(transitions[2]@transitions[1]@transitions[0],np.eye(4),atol=1e-14)
        u=sum(np.kron(np.outer(clock[:,(k+1)%3],clock[:,k]),transitions[k])
              for k in range(3))
        np.testing.assert_allclose(u.conj().T@u,np.eye(12),atol=1e-14)
        np.testing.assert_allclose(np.linalg.matrix_power(u,3),np.eye(12),atol=1e-14)
        constraint=2*np.eye(12)-u-u.conj().T
        np.testing.assert_allclose(np.linalg.eigvalsh(constraint),[0.]*4+[3.]*8,atol=1e-14)
        psi0=np.kron(PLUS,ZERO)
        psi1=transitions[0]@psi0
        psi2=transitions[1]@psi1
        history=sum(np.kron(clock[:,k],p) for k,p in enumerate((psi0,psi1,psi2)))/np.sqrt(3)
        np.testing.assert_allclose(constraint@history,np.zeros(12),atol=1e-14)
        self.assertAlmostEqual(np.linalg.norm(history),1.)
        for k,expected in enumerate((psi0,psi1,psi2)):
            part=np.kron(clock[:,k].conj(),np.eye(4))@history
            self.assertAlmostEqual(np.vdot(part,part).real,1/3)
            np.testing.assert_allclose(part*np.sqrt(3),expected,atol=1e-14)
        # Compress a joint clock/system POVM to ker C rather than using a
        # clock projection as if it preserved the constraint on its own.
        phys=(np.eye(12)+u+u@u)/3
        np.testing.assert_allclose(phys,phys.conj().T,atol=1e-14)
        np.testing.assert_allclose(phys@phys,phys,atol=1e-14)
        np.testing.assert_allclose(constraint@phys,np.zeros((12,12)),atol=1e-14)
        effects=[]
        for k,psi in enumerate((psi0,psi1,psi2)):
            pk=density(clock[:,k])
            for outcome in (PX,I-PX):
                e=phys@np.kron(pk,np.kron(outcome,I))@phys
                effects.append(e)
                self.assertGreaterEqual(np.linalg.eigvalsh(e).min(),-1e-14)
                actual=np.vdot(history,e@history).real
                expected=np.vdot(psi,np.kron(outcome,I)@psi).real/3
                self.assertAlmostEqual(actual,expected)
        np.testing.assert_allclose(sum(effects),phys,atol=1e-14)
        self.assertAlmostEqual(np.trace(density(psi1)@np.kron(Z,Z)).real,1.)
        for psi,vis in ((psi0,1.),(psi1,0.),(psi2,0.)):
            self.assertAlmostEqual(2*abs(trace_e(density(psi))[0,1]),vis)
        for sign,p in ((1,P0),(-1,P1)):
            selected=np.kron(I,p)@density(psi2)@np.kron(I,p)
            np.testing.assert_allclose(trace_e(selected)/np.trace(selected),(I+sign*X)/2,atol=1e-14)


if __name__ == '__main__':
    unittest.main()
