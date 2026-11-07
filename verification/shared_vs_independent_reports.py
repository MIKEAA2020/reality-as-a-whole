#!/usr/bin/env python3
"""Two physical report registers: common-source versus independent probes.

Exact rational amplitudes, with a common factor 1/sqrt(2). This is a circuit
check, not a subject, consciousness, locality, or general physics model.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def add(out, bits, amp):
    out[bits] = out.get(bits, F(0)) + amp


def cnot(state, control, target):
    out = {}
    for bits, amp in state.items():
        b = list(bits)
        b[target] ^= b[control]
        add(out, tuple(b), amp)
    return {bits: amp for bits, amp in out.items() if amp}


def conditional_rotation(state, control, target, a, b, inverse=False):
    # For control=0 use rotation (cos,sin)=(a,b); for 1 use (b,a).
    # Both are real orthogonal unitaries on the target.
    out = {}
    for bits, amp in state.items():
        cos, sin = (a, b) if bits[control] == 0 else (b, a)
        if inverse:
            sin = -sin
        x = bits[target]
        for y, coefficient in ((0, cos if x == 0 else -sin),
                               (1, sin if x == 0 else cos)):
            new_bits = list(bits)
            new_bits[target] = y
            add(out, tuple(new_bits), amp * coefficient)
    return {bits: amp for bits, amp in out.items() if amp}


def initial():
    # S,F,G,P,Q; all amplitudes divided by sqrt(2).
    return {(0, 0, 0, 0, 0): F(1), (1, 0, 0, 0, 0): F(1)}


def write_friend_records(state):
    return cnot(cnot(state, 0, 1), 0, 2)


def undo_friend_records(state):
    return cnot(cnot(state, 0, 2), 0, 1)


def reports_joint(state):
    # Joint Z measurements of F,P,Q; orthogonal unobserved components add
    # in probability, and the global 1/sqrt(2) contributes 1/2.
    result = {}
    for (s, f, g, p, q), amp in state.items():
        key = (f, p, q)
        result[key] = result.get(key, F(0)) + amp * amp / 2
    return result


def x_plus_probability(state):
    result = F(0)
    for f, g, p, q in product((0, 1), repeat=4):
        combined = state.get((0, f, g, p, q), F(0))
        combined += state.get((1, f, g, p, q), F(0))
        result += combined * combined / 4
    return result


def json_joint(joint):
    return [{'F': f, 'P': p, 'Q': q, 'probability': str(prob)}
            for (f, p, q), prob in sorted(joint.items())]


def main():
    cases = [(F(1), F(0)), (F(4, 5), F(3, 5)),
             (F(12, 13), F(5, 13)), (F(15, 17), F(8, 17))]
    results = []
    for a, b in cases:
        assert a*a + b*b == 1 and a >= b >= 0
        start = initial()
        ghz = write_friend_records(start)
        base = conditional_rotation(ghz, 1, 3, a, b)
        shared = cnot(base, 3, 4)
        independent = conditional_rotation(base, 1, 4, a, b)
        row = {'a': str(a), 'b': str(b), 'single_report_accuracy': str(a*a)}
        for mode, state in [('shared', shared), ('independent', independent)]:
            joint = reports_joint(state)
            assert sum(joint.values()) == 1
            consensus = sum(prob for (f, p, q), prob in joint.items() if p == q)
            accuracy_p = sum(prob for (f, p, q), prob in joint.items() if p == f)
            accuracy_q = sum(prob for (f, p, q), prob in joint.items() if q == f)
            assert accuracy_p == accuracy_q == a*a
            # A single report's calibrated bias cannot exceed the optimal
            # distinguishability of the entire retained report system.
            # Here the phase-aligned X contrast is its fringe visibility.
            both_wrong = sum(prob for (f, p, q), prob in joint.items()
                             if p != f and q != f)
            xplus = x_plus_probability(undo_friend_records(state))
            r = 2*a*b
            report_bias = 2*accuracy_p - 1
            fringe = 2*xplus - 1
            assert report_bias**2 + fringe**2 <= 1
            if mode == 'shared':
                assert report_bias**2 + fringe**2 == 1
                assert consensus == 1 and both_wrong == b*b
                assert xplus == (1+r)/2
                recovered = cnot(state, 3, 4)
                recovered = conditional_rotation(recovered, 1, 3, a, b, True)
            else:
                assert consensus == a**4+b**4 and both_wrong == b**4
                assert xplus == (1+r*r)/2
                recovered = conditional_rotation(state, 1, 4, a, b, True)
                recovered = conditional_rotation(recovered, 1, 3, a, b, True)
            assert undo_friend_records(recovered) == start
            row[mode] = {'joint_Z_F_P_Q': json_joint(joint),
                         'P_reports_agree': str(consensus),
                         'P_both_wrong': str(both_wrong),
                         'P_X_plus_with_reports_not_reversed': str(xplus),
                         'P_X_plus_after_unmeasured_full_reversal': '1'}
        results.append(row)
    witness = results[1]
    assert witness['shared']['P_reports_agree'] == '1'
    assert witness['shared']['P_both_wrong'] == '9/25'
    assert witness['shared']['P_X_plus_with_reports_not_reversed'] == '49/50'
    assert witness['independent']['P_reports_agree'] == '337/625'
    assert witness['independent']['P_X_plus_with_reports_not_reversed'] == '1201/1250'
    out = {'status': 'passed', 'qubit_order': 'S,F,G,P,Q',
           'initial_normalization': 'All stored amplitudes carry 1/sqrt(2).',
           'cases': results,
           'scope': 'Finite standard-quantum circuits only. P,Q are physical registers, not conscious subjects. The recovery uses coherent reversal before reports or uncontrolled copies are read; it does not recover a retained classical outcome. Equal circuit statistics do not establish any experience theory.'}
    text = json.dumps(out, indent=2) + '\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
