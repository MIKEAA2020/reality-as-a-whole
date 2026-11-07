#!/usr/bin/env python3
"""Low-state checks of WdW oscillator-interface claims; standard library only.

These checks do not prove self-adjointness or a gravitational reduction.
"""
from pathlib import Path
import json
import math


def add(out, n, amplitude):
    out[n] = out.get(n, 0.0) + amplitude


def x_action(state, omega):
    out = {}
    for n, amplitude in state.items():
        if n > 0:
            add(out, n-1, amplitude * math.sqrt(n/(2*omega)))
        add(out, n+1, amplitude * math.sqrt((n+1)/(2*omega)))
    return out


def x_power(state, omega, power):
    for _ in range(power):
        state = x_action(state, omega)
    return state


def h_action(state, basis_omega, omega):
    # H(w) = p^2 + w^2*x^2; H(basis_omega) is diagonal.
    out = {n: basis_omega*(2*n+1)*amplitude for n, amplitude in state.items()}
    for n, amplitude in x_power(state, basis_omega, 2).items():
        add(out, n, (omega**2-basis_omega**2)*amplitude)
    return out


def norm(state):
    return math.sqrt(sum(abs(value)**2 for value in state.values()))


def main():
    omega = 2.0
    quartic_on_ground = x_power({0: 1.0}, omega, 4)
    observed_02 = quartic_on_ground[2]
    correct_02 = 3*math.sqrt(2)/(2*omega**2)
    historical_02 = 3*math.sqrt(2)/(4*omega**2)
    assert math.isclose(observed_02, correct_02, rel_tol=1e-12)
    ratios = []
    for n in (0, 5, 20, 60):
        output = x_power({n: 1.0}, omega, 4)
        expectation = 3*(2*n*n+2*n+1)/(4*omega**2)
        assert math.isclose(output[n], expectation, rel_tol=1e-12)
        ratios.append({'n': n, 'expectation': expectation,
                       'norm_over_H_plus_one': norm(output)/(omega*(n+0.5)+1)})
    assert all(ratios[i]['norm_over_H_plus_one'] < ratios[i+1]['norm_over_H_plus_one']
               for i in range(len(ratios)-1))
    w1, w2 = 1.0, 1.2
    ab = h_action(h_action({0:1.0}, omega, w2), omega, w1)
    ba = h_action(h_action({0:1.0}, omega, w1), omega, w2)
    witness = ab.get(2, 0) - ba.get(2, 0)
    expected = 2*math.sqrt(2)*(w2**2-w1**2)
    assert math.isclose(witness, expected, rel_tol=1e-12, abs_tol=1e-12)
    result = {'basis_frequency': omega,
              'quartic_02': {'ladder_calculation': observed_02, 'correct': correct_02,
                             'historical_claim': historical_02},
              'quartic_norm_ratios': ratios,
              'different_frequency_commutator_20': {'ladder_calculation': witness, 'expected': expected},
              'sqrt_vs_linear_energy_ratio': {'square_root': math.sqrt(3), 'number_operator': 3},
              'scope': 'finite low-state checks; no gravitational or self-adjointness proof'}
    path = Path(__file__).with_name('wdw_interface_audit.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    print('PASS: ladder witnesses; see WDW_INTERFACE_CORRECTIONS.md for analytic scope.')


if __name__ == '__main__':
    main()
