#!/usr/bin/env python3
"""Finite checks of a Bell-preparation versus trace-correlator identity.

The all-size bound is proved in the accompanying report; finite numerical
checks do not establish experiment, physical ontology or experience.
"""
from fractions import Fraction
from functools import reduce
from pathlib import Path
import json
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)

def kron(*items):
    return reduce(np.kron, items)

def real(x):
    assert abs(complex(x).imag) < 1e-10
    return float(complex(x).real)

def close(a, b):
    return np.allclose(a, b, atol=1e-10, rtol=1e-10)

Pp, Pm = (I + X)/2, (I - X)/2
bell = np.array([1, 0, 0, 1], dtype=complex)/np.sqrt(2)
pair = np.outer(bell, bell.conj())
rows = []
for pairs in (1, 2, 3):
    d = 4**pairs
    rest = kron(*([pair] * pairs)) if pairs > 1 else pair
    rho = kron(Pp, rest)
    X0 = kron(X, np.eye(d))
    dim = 2*d
    # A-C = Tr[(rho-(I+X0)/dim) O] for traceless O.
    delta = rho - kron(Pp, np.eye(d))/d
    # A reflection on the rest with one positive eigenvector; another with
    # one negative eigenvector. Together O is traceless and squares to I.
    plus = 2*rest - np.eye(d)
    v = np.zeros(d, dtype=complex); v[-1] = 1
    minus = np.eye(d) - 2*np.outer(v, v.conj())
    O = kron(Pp, plus) + kron(Pm, minus)
    assert close(O.conj().T, O) and close(O@O, np.eye(dim))
    assert abs(np.trace(O)) < 1e-10
    eig = np.linalg.eigvalsh(delta)
    assert close(sum(abs(eig)), 2*(1-1/d))
    A = real(np.trace(rho@O)); C = real(np.trace(X0@O)/dim)
    assert close(A, 1) and close(C, -1+2/d)
    assert close(A-C, real(np.trace(delta@O)))
    assert close(A-C, 2*(1-1/d))
    if pairs == 1:
        # Every traceless Hermitian unitary O with equal +/− multiplicities
        # is U† X1 U. Construct U from sorted eigenbases, not just assert it.
        X1 = kron(I, X, I)
        vals_o, vec_o = np.linalg.eigh(O)
        vals_x, vec_x = np.linalg.eigh(X1)
        assert close(vals_o, vals_x)
        U = vec_x @ vec_o.conj().T
        assert close(U.conj().T@U, np.eye(dim)) and close(U.conj().T@X1@U, O)
    rows.append({'qubits': 2*pairs+1, 'ancilla_dimension': d,
                 'prepared_expectation': A, 'infinite_temperature_correlator': C,
                 'sharp_difference': str(2*(1-Fraction(1,d)))})

# Local, explicitly specified two-qubit operation, not the experiment's
# dual-unitary or perturbed kicked-Ising gate.
rho3 = kron(Pp, pair)
X0, X1 = kron(X,I,I), kron(I,X,I)
P = kron(I,Z,Y)
examples=[]
for theta in (0, np.pi/8, np.pi/4):
    U=np.cos(theta)*np.eye(8)-1j*np.sin(theta)*P
    O=U.conj().T@X1@U
    A=real(np.trace(rho3@O)); C=real(np.trace(X0@O)/8)
    assert close(A,np.sin(2*theta)) and close(C,0)
    examples.append({'theta_over_pi': round(theta/np.pi, 3),
                     'prepared_expectation': A, 'infinite_temperature_correlator': C})
assert close(np.linalg.eigvalsh(rho3).sum(), 1)
report = {
    'scope':'Ideal finite-dimensional algebra; no experimental data, subject identity, phenomenality, gravity or quantum advantage inference.',
    'sharp_bound':'2*(1-1/2^(N-1)) for odd N>=3 with the stated prepared Bell product and traceless Hermitian unitary observables',
    'saturating_checks':rows,
    'local_gate_examples':examples,
    'caution':'Local gate example is not the Fischer et al. Floquet circuit and does not identify a dual-unitary perturbation.',
}
(ROOT/'verification/bell_preparation_correlation_gate.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS: Bell-prepared expectation vs trace correlation; sharp examples N=3,5,7')
print(report['scope'])
