#!/usr/bin/env python3
"""Finite path check of the turning-clock / entropy-path / record bridge.

This checks a discrete cosine path, not the Barontini entropy measurements or a
quantum measurement instrument. See TURNING_ENTROPY_RECORD_BRIDGE.md.
"""
import json
import math
from pathlib import Path


def analytic_tau(theta, a):
    twopi = 2*math.pi
    winding = math.floor(theta/twopi)
    phase = theta - winding*twopi
    q = math.cos(phase)
    if phase <= math.pi:
        return 4*a*winding + a*(1-q)
    return 4*a*winding + a*(3+q)


def main():
    # Step length divides every turning point, so discrete total variation is exact.
    steps = 12000
    a = 2.0
    q = [math.cos(4*math.pi*i/steps) for i in range(steps+1)]
    tau = [0.0]
    for i in range(1, steps+1):
        tau.append(tau[-1]+a*abs(q[i]-q[i-1]))
    maximum_error = max(abs(value-analytic_tau(4*math.pi*i/steps, a))
                        for i, value in enumerate(tau))
    assert maximum_error < 1e-10
    i, j = steps//12, steps//12 + steps//2
    assert abs(q[i]-q[j]) < 1e-12
    assert abs((tau[j]-tau[i])-4*a) < 1e-10
    q_gravity = 2/math.cosh(1)-1
    gravity_expanding = a*(1+q_gravity)
    gravity_contracting = a*(3-q_gravity)
    assert math.isclose(gravity_contracting-gravity_expanding,
                        2*a*(1-q_gravity), rel_tol=1e-12)
    result = {'a': a, 'cycles': 2, 'steps': steps,
              'maximum_path_vs_formula_error': maximum_error,
              'same_local_reading': [q[i], q[j]],
              'same_branch_elapsed_values': [tau[i], tau[j]],
              'one_cycle_increment': tau[j]-tau[i],
              'recollapse_interface': {'equal_q_at_T_plus_minus_1': q_gravity,
                                       'expanding_tau': gravity_expanding,
                                       'contracting_tau': gravity_contracting},
              'scope': 'prescribed paths, not an experiment, quantum gravity result, or autonomous memory device'}
    path = Path(__file__).with_name('turning_entropy_bridge.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    print('PASS: finite-path checks; analytic claims are in TURNING_ENTROPY_RECORD_BRIDGE.md')


if __name__ == '__main__':
    main()
