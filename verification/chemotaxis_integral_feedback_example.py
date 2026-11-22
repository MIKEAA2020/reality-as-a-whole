#!/usr/bin/env python3
"""Constructed scalar feedback example; not the authors' biochemical model or data."""
import json
import math
from pathlib import Path


def activity(z, ligand):
    return (1.0 + z) / (1.0 + z + ligand)


def drift(z, ligand, gain=1.0):
    return gain * (0.5 - activity(z, ligand))


def rk4(z, ligand, dt, gain=1.0):
    f = lambda x: drift(x, ligand, gain)
    a = f(z)
    b = f(z + dt*a/2)
    c = f(z + dt*b/2)
    d = f(z + dt*c)
    return z + dt*(a+2*b+2*c+d)/6


def simulate(ligand, *, cap=None, gain=1.0, time=20.0, dt=0.001):
    z = 0.0
    steps = round(time/dt)
    for _ in range(steps):
        z = rk4(z, ligand, dt, gain)
        if cap is not None:
            z = min(cap, max(0.0, z))
    return {'z': z, 'activity': activity(z, ligand), 'time': time}


def time_to_z(z, ligand, gain=1.0):
    # Exact separation for ligand > 1, z(0)=0, 0 <= z < ligand-1.
    target = ligand - 1
    assert ligand > 1 and 0 <= z < target and gain > 0
    return 2 * (-z - 2*ligand*math.log1p(-z/target)) / gain


def invert_time(time, ligand, gain=1.0):
    lo, hi = 0.0, ligand-1
    for _ in range(100):
        mid = (lo+hi)/2
        if time_to_z(mid, ligand, gain) < time:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def main():
    moderate = simulate(2)
    analytic_z = invert_time(20, 2)
    assert abs(moderate['z']-analytic_z) < 1e-9
    bounded = simulate(8, cap=2)
    hit_time = time_to_z(2, 8)
    assert hit_time < 20 and abs(bounded['z']-2) < 1e-12
    assert abs(bounded['activity']-3/11) < 1e-12
    assert drift(2, 8) > 0
    slow = simulate(2, gain=0.5)
    assert abs(slow['z']-invert_time(20, 2, 0.5)) < 1e-9
    assert slow['z'] < moderate['z'] < 1
    result = {
        'scope': 'Illustrative invented dimensionless ODE, not a fitted bacterial model, experiment, proof of biology or consciousness.',
        'activity': '(1+z)/(1+z+L)',
        'controller': 'dz/dt = k*(1/2 - activity); stop outward drift at 0 or cap in bounded case',
        'initial_ligand': 1, 'initial_z': 0, 'initial_activity': 0.5,
        'unbounded_ligand_2': {'immediate_activity': activity(0, 2), 'asymptotic_z': 1, 'asymptotic_activity': 0.5,
                               'rk4_at_t20': moderate, 'independent_analytic_z_at_t20': analytic_z},
        'frozen_ligand_2': {'activity': activity(0, 2)},
        'bounded_ligand_8': {'upper_z_bound': 2, 'unconstrained_equilibrium_z': 7,
                             'bounded_equilibrium_activity': 3/11,
                             'bounded_equilibrium_error': 5/22,
                             'analytical_first_hit_time': hit_time, 'projected_rk4_at_t20': bounded},
        'half_gain_ligand_2': {'asymptotic_z': 1, 'asymptotic_activity': 0.5,
                               'rk4_at_t20': slow},
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
