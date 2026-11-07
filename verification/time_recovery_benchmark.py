#!/usr/bin/env python3
"""Numerical checks for the finite-window qubit benchmark in TIME_RESEARCH_ROADMAP.md.

This checks two input states, not arbitrary states or recovery channels. The
universal lower bound uses the cited trace-distance data-processing theorem.
"""
import math


def sinc(x):
    return 1.0 if x == 0.0 else math.sin(x) / x


def integrate_coherence(delta, window, steps=20000):
    """Trapezoidal average of exp(-i delta t) on a symmetric window."""
    dt = window / steps
    value = 0j
    for j in range(steps + 1):
        t = -window / 2 + j * dt
        weight = 0.5 if j in (0, steps) else 1.0
        value += weight * complex(math.cos(delta * t), -math.sin(delta * t))
    return value * dt / window


def trace_distance_qubit(a, b):
    """Trace distance of Hermitian, trace-one 2x2 matrices."""
    diagonal = (a[0][0] - b[0][0]).real
    off_diagonal = a[0][1] - b[0][1]
    return math.sqrt(diagonal**2 + abs(off_diagonal)**2)


def density(sign, coherence):
    return ((0.5, sign * coherence / 2), (sign * coherence.conjugate() / 2, 0.5))


def main():
    delta = 1.0
    for fraction in (0.1, 0.5, 1.0):
        window = fraction * 2 * math.pi / delta
        coherence = integrate_coherence(delta, window)
        exact = sinc(delta * window / 2)
        assert abs(coherence - exact) < 1e-8
        plus, minus = density(1, coherence), density(-1, coherence)
        initial_plus, initial_minus = density(1, 1 + 0j), density(-1, 1 + 0j)
        distance = trace_distance_qubit(plus, minus)
        lower_bound = (1 - abs(exact)) / 2
        identity_error = max(trace_distance_qubit(plus, initial_plus),
                             trace_distance_qubit(minus, initial_minus))
        assert abs(distance - abs(exact)) < 1e-8
        assert abs(identity_error - lower_bound) < 1e-8
        print(f'T/period={fraction:g}  output distance={distance:.9f}  '
              f'lower bound={lower_bound:.9f}  identity error={identity_error:.9f}')
    print('PASS: finite-window quadrature and pairwise errors; '
          'the universal recovery bound is analytical, not numerically optimized.')


if __name__ == '__main__':
    main()
