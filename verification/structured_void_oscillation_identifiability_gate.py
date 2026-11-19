#!/usr/bin/env python3
"""Three-state avoided-crossing witness; not a neutrino fit or lattice model."""
import cmath
import json
import math
from pathlib import Path

# Units are dimensionless, with hbar=1. In the |+>, |->, |s> basis,
# H=[[0,0,0],[0,0,1],[0,1,E]]. The initial |e>=(|+>+|->)/sqrt(2),
# the other visible state |mu>=(|+>-|->)/sqrt(2).
def exact(E, L):
    w = math.hypot(E, 2.0)
    phase = cmath.exp(-0.5j * E * L)
    u_minus = phase * (math.cos(w * L / 2) + 1j * E / w * math.sin(w * L / 2))
    e_amp = (1 + u_minus) / 2
    mu_amp = (1 - u_minus) / 2
    aux_prob = 2 * (math.sin(w * L / 2) / w) ** 2
    return abs(e_amp)**2, abs(mu_amp)**2, aux_prob

def rk4_check(E, L, steps=4000):
    # Independent direct integration of dψ/dL = -iHψ for one short path.
    def rhs(v):
        return (0j, -1j * v[2], -1j * (v[1] + E * v[2]))

    def add(v, k, factor):
        return tuple(a + factor * b for a, b in zip(v, k))

    psi = (2 ** -0.5, 2 ** -0.5, 0j)
    dt = L / steps
    for _ in range(steps):
        k1 = rhs(psi)
        k2 = rhs(add(psi, k1, dt / 2))
        k3 = rhs(add(psi, k2, dt / 2))
        k4 = rhs(add(psi, k3, dt))
        psi = tuple(v + dt * (a + 2*b + 2*c + d) / 6
                    for v, a, b, c, d in zip(psi, k1, k2, k3, k4))
    return (abs((psi[0] + psi[1]) / 2 ** 0.5) ** 2,
            abs((psi[0] - psi[1]) / 2 ** 0.5) ** 2, abs(psi[2]) ** 2)

assert max(abs(a-b) for a, b in zip(exact(10.0, 0.3), rk4_check(10.0, 0.3))) < 1e-10

rows = []
for E in (10.0, 20.0, 100.0):
    for x in (0.0, math.pi / 2, math.pi, 2 * math.pi):
        L = x * E
        p_e, p_mu, p_aux = exact(E, L)
        reference = math.sin(x / 2) ** 2
        assert abs(p_e + p_mu + p_aux - 1) < 1e-12
        assert p_aux <= 2 / (E * E + 4) + 1e-14
        assert abs(p_mu - reference) < 0.02
        rows.append({'E': E, 'L_over_E': x, 'P_visible_transition': p_mu,
                     'P_reference': reference, 'P_auxiliary': p_aux})
# At fixed L/E the reference has a maximum near pi; check convergence,
# not monotonicity (fast auxiliary oscillations are not monotonic in E).
pi_rows = [r for r in rows if r['L_over_E'] == math.pi]
assert pi_rows[-1]['P_visible_transition'] > 0.999
assert pi_rows[-1]['P_auxiliary'] < 0.0002
# Spectrum gap of the low eigenvalue and the uncoupled zero mode.
for E in (10.0, 20.0, 100.0):
    # stable form for (sqrt(E^2+4)-E)/2
    gap = 2 / (math.hypot(E, 2) + E)
    assert abs(gap * E - 1) < 0.01
print(json.dumps({'status': 'passed', 'scope': 'finite dimensionless witness, not an oscillation data fit',
                  'hamiltonian_plus_minus_aux': [[0,0,0],[0,0,1],[0,1,'E']],
                  'baseline_choice': 'L=(L/E)*E', 'rows': rows}, indent=2))
