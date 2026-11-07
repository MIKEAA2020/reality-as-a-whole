#!/usr/bin/env python3
"""Check a known frustrated-oscillator motif, not a pain or string-theory model."""
import itertools
import json
import math
from pathlib import Path
import random

EDGES = ((0, 1), (1, 2), (2, 0))
TAU = 2 * math.pi


def energy(phi, pref):
    return sum(1 - math.cos(phi[i] - phi[j] - a)
               for (i, j), a in zip(EDGES, pref))


def gradient(phi, pref):
    out = [0.0] * 3
    for (i, j), a in zip(EDGES, pref):
        s = math.sin(phi[i] - phi[j] - a)
        out[i] += s
        out[j] -= s
    return out


def main():
    # Equal antiphase preference: the exact global lower bound is 3/2.
    phases = (0, TAU / 3, 2 * TAU / 3)
    anti = (math.pi,) * 3
    anti_minimum = energy(phases, anti)
    assert abs(anti_minimum - 1.5) < 1e-12
    grad = gradient(phases, anti)
    dissipation = sum(g * g for g in grad)
    assert dissipation < 1e-25
    # Same phase state, compatible preferred offsets on the directed cycle.
    compatible = (-TAU / 3,) * 3
    compatible_energy = energy(phases, compatible)
    assert abs(compatible_energy) < 1e-12
    r = abs(sum(complex(math.cos(p), math.sin(p)) for p in phases) / 3)
    assert r < 1e-12

    # Independent local choices of phase origin: transform offsets as well.
    rng = random.Random(6420)
    max_gauge_error = 0.0
    for _ in range(2000):
        phi = [rng.uniform(-TAU, TAU) for _ in range(3)]
        a = [rng.uniform(-TAU, TAU) for _ in EDGES]
        delta = [rng.uniform(-TAU, TAU) for _ in range(3)]
        shifted_phi = [x + d for x, d in zip(phi, delta)]
        shifted_a = [v + delta[i] - delta[j] for (i, j), v in zip(EDGES, a)]
        max_gauge_error = max(max_gauge_error,
                              abs(energy(phi, a) - energy(shifted_phi, shifted_a)))
    assert max_gauge_error < 1e-12

    # For 12 discrete phase values, enumerate all directed triangle offsets;
    # fix phi_0=0 because global phase cancels.
    q = 12
    compatible_count = 0
    for a in itertools.product(range(q), repeat=3):
        exists = any(all((p[i] - p[j] - ak) % q == 0
                         for (i, j), ak in zip(EDGES, a))
                     for p1, p2 in itertools.product(range(q), repeat=2)
                     for p in [(0, p1, p2)])
        cycle_zero = sum(a) % q == 0
        assert exists == cycle_zero
        compatible_count += exists
    assert compatible_count == q * q

    result = {
        'status': 'passed',
        'scope': 'Classical unit-weight phase model; not string theory, brain data, or a phenomenology metric.',
        'antiphase_triangle_exact_minimum': anti_minimum,
        'proof': 'E = (3 + |sum(exp(i*phi))|^2)/2 >= 3/2; 120-degree phases saturate.',
        'gradient_flow_energy_loss_at_minimum': dissipation,
        'same_phases_compatible_edge_energy': compatible_energy,
        'same_phases_order_parameter_R': r,
        'random_phase_origin_transforms': 2000,
        'max_gauge_energy_error': max_gauge_error,
        'discrete_cycle_assignments': q ** 3,
        'discrete_compatible_assignments': compatible_count,
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
