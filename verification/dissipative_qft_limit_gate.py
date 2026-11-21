#!/usr/bin/env python3
"""Exact finite amplitude-damping and Abel-limit checks, not a QFT proof."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import math


def determinant(matrix):
    """Exact recursive determinant; matrices here are at most four by four."""
    if not matrix:
        return F(1)
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(((-1) ** j) * matrix[0][j] * determinant(
        [row[:j] + row[j + 1:] for row in matrix[1:]])
        for j in range(len(matrix)))


def choi(q):
    z = F(0)
    return [[F(1), z, z, q], [z, z, z, z],
            [z, z, 1 - q*q, z], [q, z, z, q*q]]


def channel(rho, q):
    a, b = rho[0]
    c, d = rho[1]
    return [[a + (1-q*q)*d, q*b], [q*c, q*q*d]]


def abel(s, gamma):
    return s / (s + 2*gamma)


def run():
    qs = [F(i, 8) for i in range(9)]
    matrices_checked = 0
    for q in qs:
        J = choi(q)
        for n in range(1, 5):
            for index in combinations(range(4), n):
                sub = [[J[i][j] for j in index] for i in index]
                assert determinant(sub) >= 0
                matrices_checked += 1
        # Choi basis ordered as |input,output>: partial trace over output is I.
        assert [[sum(J[2*i+k][2*j+k] for k in (0, 1)) for j in (0, 1)]
                for i in (0, 1)] == [[1, 0], [0, 1]]
        for r in qs:
            for rho in ([[F(1), F(0)], [F(0), F(0)]],
                        [[F(0), F(0)], [F(0), F(1)]],
                        [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]):
                assert channel(channel(rho, r), q) == channel(rho, q*r)
    # For gamma=1/n, s=1/n^2, 1/n, and 1/sqrt(n), respectively:
    # use square n=m^2 to keep the third path rational.
    paths = []
    for m in (2, 10, 100):
        n = m*m
        gamma = F(1, n)
        vals = [abel(F(1, n*n), gamma), abel(F(1, n), gamma),
                abel(F(1, m), gamma)]
        assert vals == [F(1, 2*n+1), F(1, 3), F(m, m+2)]
        paths.append({'n': n, 'slow_s': str(vals[0]),
                      'balanced_s': str(vals[1]), 'fast_s': str(vals[2])})
    # gamma=n^-4, k=n, t=1: a mode whose damping stays finite.
    probe = []
    for n in (2, 4, 8, 16):
        gamma = F(1, n**4)
        assert gamma * n**4 == 1
        probe.append({'k': n, 'gamma': str(gamma),
                      'excited_population': math.exp(-2)})
    # Bounded-energy one-particle number-loss estimate, finite examples only.
    energy_checks = 0
    k_values = (1, 2, 4, 8)
    for probabilities in ((F(1), F(0), F(0), F(0)),
                          (F(1, 4), F(1, 4), F(1, 4), F(1, 4)),
                          (F(0), F(1, 4), F(0), F(1, 2))):
        energy = float(sum(k*p for k, p in zip(k_values, probabilities)))
        for gamma in (1e-1, 1e-3, 1e-6):
            cutoff = (energy / (8*gamma))**(1/5)  # t=1
            bound = 2*gamma*cutoff**4 + energy/cutoff
            loss = sum(float(p) * (-math.expm1(-2*gamma*k**4))
                       for k, p in zip(k_values, probabilities))
            assert loss <= bound + 1e-12
            energy_checks += 1
    return {'status': 'passed', 'choi_principal_minors_checked': matrices_checked,
            'q_values': len(qs), 'semigroup_q_pairs': len(qs)**2,
            'sampled_energy_bound_checks': energy_checks,
            'sampled_abel_paths': paths, 'moving_momentum_probe': probe,
            'scope': ('Finite one-mode free zero-temperature amplitude damping '
                      'on the vacuum/one-particle sector only. Neither the interacting '
                      'nonlinear thermodynamic equation nor a QFT continuum, '
                      'Lorentz covariance, gauge symmetry, or measurement interpretation '
                      'is derived by these checks.')}


if __name__ == '__main__':
    text = json.dumps(run(), indent=2) + '\n'
    Path(__file__).with_suffix('.json').write_text(text, encoding='utf-8')
    print(text, end='')
