#!/usr/bin/env python3
"""Clock-smearing control for one finite constrained Gibbs history.

Kinematical measurement disturbance is not gravitational backreaction. Analytic
identities and the scope of the sequential measurement are in the companion note.
Requires NumPy. No external-time detector or infinite algebra is simulated.
"""
import json
from pathlib import Path
import numpy as np

N = 3
H = np.diag([0., 1., 2.]).astype(complex)
P = np.exp(-np.arange(N, dtype=float)); P /= P.sum()
PSI = np.sqrt(P).astype(complex)
TAU = np.diag(P).astype(complex)
I = np.eye(N, dtype=complex)
RHO0 = np.outer(PSI, PSI.conj())
B = RHO0.copy()


def U(j):
    return np.diag(np.exp(-2j * np.pi * j * np.arange(N) / N))


def dagger(a):
    return a.conj().T


def history_isometry():
    return np.vstack([U(j) for j in range(N)]) / np.sqrt(N)


def constraint():
    c = np.zeros((N*N, N*N), dtype=complex)
    for j in range(N-1):
        d = np.zeros((N, N*N), dtype=complex)
        d[:, j*N:(j+1)*N] = -U(1)
        d[:, (j+1)*N:(j+2)*N] = I
        c += dagger(d) @ d
    return c


def projectors():
    return [np.diag([float(k == j) for k in range(N)]).astype(complex) for j in range(N)]


def effects(e):
    if not 0 <= e <= 1:
        raise ValueError('noise must lie in [0,1]')
    p = projectors()
    return [(1-e)*p[j] + e*p[(j-1) % N] for j in range(N)]


def lueders(e):
    p = projectors()
    return [np.sqrt(1-e)*p[j] + np.sqrt(e)*p[(j-1) % N] for j in range(N)]


def root_effects(e):
    jmat = history_isometry()
    return [[dagger(jmat) @ np.kron(q, b) @ jmat for b in (B, I-B)] for q in effects(e)]


def joint(e, rho=RHO0):
    return np.array([[np.trace(rho @ f).real for f in row] for row in root_effects(e)])


def conditional_systems(e):
    states = [U(j) @ RHO0 @ dagger(U(j)) for j in range(N)]
    return [(1-e)*states[j] + e*states[(j-1) % N] for j in range(N)]


def entropy(rho):
    vals = np.linalg.eigvalsh((rho + dagger(rho))/2)
    if min(vals) < -1e-11 or abs(sum(vals)-1) > 1e-11:
        raise ValueError('not a density matrix')
    vals = np.clip(vals, 0, 1)
    return float(-sum(x*np.log(x) for x in vals if x > 1e-14))


def postmeasurement(e):
    jmat = history_isometry()
    v = jmat @ PSI
    rho = np.outer(v, v.conj())
    out = np.zeros_like(rho)
    for k in lueders(e):
        big = np.kron(k, I)
        out += big @ rho @ dagger(big)
    return out


def partial_system(rho):
    return sum(rho[j*N:(j+1)*N, j*N:(j+1)*N] for j in range(N))


def calculate(e=.25):
    jmat = history_isometry(); c = constraint()
    f = float(abs(np.vdot(PSI, U(1) @ PSI))**2)
    disc = np.sqrt(1 - 4*e*(1-e)*(1-f))
    formula_entropy = entropy(np.diag([(1+disc)/2, (1-disc)/2, 0]).astype(complex))
    sharp = joint(0); noisy = joint(e)
    sharp_after = postmeasurement(0); noisy_after = postmeasurement(e)
    assert np.allclose(dagger(jmat) @ jmat, I)
    assert np.allclose(c @ jmat, 0, atol=1e-12)
    assert np.allclose(sum(effects(e)), I)
    assert np.allclose(sum(dagger(k) @ k for k in lueders(e)), I)
    assert np.allclose(sum(sum(row) for row in root_effects(e)), I)
    assert np.allclose(partial_system(sharp_after), TAU)
    assert np.allclose(partial_system(noisy_after), TAU)
    assert np.allclose([entropy(x) for x in conditional_systems(e)], formula_entropy)
    assert np.isclose(np.trace(c @ sharp_after).real, 4/3)
    assert np.isclose(np.trace(c @ noisy_after).real, 4/3*(1-np.sqrt(e*(1-e))))
    assert np.allclose(noisy, (1-e)*sharp + e*np.roll(sharp, 1, axis=0))
    return {
        'status':'passed', 'noise':e, 'probabilities_gibbs':P.tolist(),
        'adjacent_state_fidelity':f,
        'sharp_joint_clock_then_B':sharp.tolist(), 'noisy_joint_clock_then_B':noisy.tolist(),
        'sharp_B_yes_given_reading_zero':float(sharp[0,0]/sum(sharp[0])),
        'noisy_B_yes_given_reading_zero':float(noisy[0,0]/sum(noisy[0])),
        'conditional_system_entropy_nats_sharp':0.0,
        'conditional_system_entropy_nats_noisy':formula_entropy,
        'system_marginal_entropy_nats_both':entropy(TAU),
        'clock_system_holevo_nats_sharp':entropy(TAU),
        'clock_system_holevo_nats_noisy':entropy(TAU)-formula_entropy,
        'kinematical_constraint_expectation_before':0.0,
        'kinematical_constraint_expectation_sharp_lueders':float(np.trace(c @ sharp_after).real),
        'kinematical_constraint_expectation_noisy_lueders':float(np.trace(c @ noisy_after).real),
        'scope':'One finite, cyclic, kinematical measurement; not gravitational backreaction, an autonomous clock, or an entropy of a gravity algebra.'}


if __name__ == '__main__':
    result = calculate()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
