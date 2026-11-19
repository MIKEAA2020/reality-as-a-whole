#!/usr/bin/env python3
"""Bounded synthetic checks of a conditional quantum-agreement inequality.

No experiential claims, physical data, or independent proof of cited theorems.
"""
from pathlib import Path
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
TOL = 2e-11


def expval(rho, op):
    v = np.trace(rho @ op)
    assert abs(v.imag) < TOL
    return float(v.real)


def one_projector(n, rng):
    v = rng.normal(size=n) + 1j * rng.normal(size=n)
    v /= np.linalg.norm(v)
    return np.outer(v, v.conj())


def random_state(n, rng):
    mat = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    rho = mat @ mat.conj().T
    return rho / np.trace(rho)


def metrics(rho, a0, a1, b0, b1):
    na, nb = len(a0), len(b0)
    ai, bi = np.eye(na), np.eye(nb)
    a0, a1 = np.kron(a0, bi), np.kron(a1, bi)
    b0, b1 = np.kron(ai, b0), np.kron(ai, b1)
    p, s = expval(rho, a0), expval(rho, b0)
    assert p > 0 and s > 0
    e = max(0.0, expval(rho, (a0 - b0) @ (a0 - b0)))
    t = max(0.0, expval(rho, (a1 - b1) @ (a1 - b1)))
    aa, bb = expval(rho, a1), expval(rho, b1)
    qa, qb = expval(rho, a0 @ b1) / p, expval(rho, a1 @ b0) / s
    delta = abs(qa - qb)
    difference = p * qa - s * qb
    weighted = abs(difference)
    ident = np.eye(na * nb)
    alpha = expval(rho, a0 @ (ident - b0))
    beta = expval(rho, (ident - a1) @ b1)
    alpha_reverse = expval(rho, (ident - a0) @ b0)
    beta_reverse = expval(rho, a1 @ (ident - b1))
    aa0, aa1, bb0, bb1 = (2*a0-ident, 2*a1-ident, 2*b0-ident, 2*b1-ident)
    correlators = [expval(rho, aa0@bb0), expval(rho, aa0@bb1),
                   expval(rho, aa1@bb0), expval(rho, aa1@bb1)]
    c00,c01,c10,c11 = correlators
    s_forward = c00+c01-c10+c11
    s_reverse = c00-c01+c10+c11
    assert abs(s_forward - (2+4*(difference-alpha-beta))) < TOL
    assert abs(s_reverse - (2+4*(-difference-alpha_reverse-beta_reverse))) < TOL
    u1 = math.sqrt(e * max(0.0, bb)) + math.sqrt(s * t)
    u2 = math.sqrt(e * max(0.0, aa)) + math.sqrt(p * t)
    rhs = (min(u1, u2) + abs(p - s)) / max(p, s)
    assert weighted <= min(u1, u2) + TOL
    assert delta <= rhs + TOL
    return dict(p=p, s=s, e=e, t=t, q_A=qa, q_B=qb,
                absolute_gap=delta, weighted_gap=weighted,
                refined_bound=rhs, classical_bound=e+t,
                directional_classical_bound_forward=alpha+beta,
                directional_classical_bound_reverse=alpha_reverse+beta_reverse,
                chsh_forward=s_forward, chsh_reverse=s_reverse)


def exact_example():
    phi = np.array([1, 0, 0, 1], dtype=complex) / math.sqrt(2)
    rho = np.outer(phi, phi.conj())
    plus = np.array([1, 1], dtype=complex) / math.sqrt(2)
    minus = np.array([1, -1], dtype=complex) / math.sqrt(2)
    zero = np.array([1, 0], dtype=complex)
    projector = lambda v: np.outer(v, v.conj())
    theta = math.pi / 12
    result = metrics(rho, projector(plus), projector(zero),
                     projector(math.cos(theta)*plus + math.sin(theta)*minus),
                     projector(zero))
    assert abs(result['e']-(2-math.sqrt(3))/4) < TOL
    assert abs(result['q_A']-.5) < TOL and abs(result['q_B']-.75) < TOL
    assert abs(result['t']) < TOL and abs(result['weighted_gap']-.125) < TOL
    assert result['weighted_gap'] > result['classical_bound']
    assert abs(result['chsh_reverse']-(2+math.sqrt(3)/2-0.5)) < TOL
    assert result['chsh_reverse'] > 2
    for theta in (1e-1, 1e-2, 1e-3):
        r = metrics(rho, projector(plus), projector(zero),
                    projector(math.cos(theta)*plus + math.sin(theta)*minus),
                    projector(zero))
        assert abs(r['absolute_gap']-math.sqrt(r['e']*(1-r['e']))) < TOL
    return result


def classical_controls(rng):
    # A common deterministic assignment to all four measurement outcomes.
    records = np.array([[a0, a1, b0, b1]
                        for a0 in (0, 1) for a1 in (0, 1)
                        for b0 in (0, 1) for b1 in (0, 1)])
    greatest_violation = -1.0
    for _ in range(5000):
        w = rng.dirichlet(np.ones(16))
        a0, a1, b0, b1 = records.T
        lhs = abs(w @ (a0*b1) - w @ (a1*b0))
        e, t = w @ (a0 != b0), w @ (a1 != b1)
        greatest_violation = max(greatest_violation, float(lhs-e-t))
        diff = w @ (a0*b1) - w @ (a1*b0)
        forward = w @ (a0*(1-b0)) + w @ ((1-a1)*b1)
        reverse = w @ ((1-a0)*b0) + w @ (a1*(1-b1))
        assert lhs <= e+t+TOL
        assert diff <= forward+TOL and -diff <= reverse+TOL
    # Rare selected event. The fourth mass is positive for eta < 2/3.
    eta = 0.001
    rows = np.array([[1,1,1,1],[1,1,0,1],[0,0,1,0],[0,0,0,0]])
    weights = np.array([eta/2,eta/2,eta/2,1-3*eta/2])
    a0,a1,b0,b1 = rows.T
    p,s = weights@a0,weights@b0
    e,t = weights@(a0!=b0),weights@(a1!=b1)
    q_a,q_b = (weights@(a0*b1))/p,(weights@(a1*b0))/s
    overlap = weights@(a0*b0)
    assert abs(p-eta)<TOL and abs(s-eta)<TOL
    assert abs(e-eta)<TOL and abs(t)<TOL and abs(overlap-eta/2)<TOL
    assert abs(q_a-1)<TOL and abs(q_b-.5)<TOL
    return {'mixtures_checked':5000,'max_classical_inequality_residual':greatest_violation,
            'rare_control':{'eta':eta,'p':p,'s':s,'overlap':overlap,'e':e,'t':t,
                            'q_A':q_a,'q_B':q_b}}


def main():
    rng = np.random.default_rng(20261118)
    count = 0
    max_residual = -1.0
    for na, nb in ((2,2),(2,3),(3,3)):
        for _ in range(1500):
            rho = random_state(na*nb, rng)
            r = metrics(rho, one_projector(na,rng),one_projector(na,rng),
                        one_projector(nb,rng),one_projector(nb,rng))
            max_residual = max(max_residual, r['absolute_gap']-r['refined_bound'])
            count += 1
    report = {'status':'passed', 'scope':'finite synthetic checks; not a proof, physical experiment or consciousness assay',
              'seed':20261118,'random_quantum_models_checked':count,
              'random_quantum_max_gap_minus_bound':max_residual,
              'quantum_two_qubit_example':exact_example(),
              'classical_controls':classical_controls(rng)}
    (ROOT/'verification/robust_quantum_agreement_bound.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__ == '__main__':
    main()
