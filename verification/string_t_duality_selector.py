#!/usr/bin/env python3
"""Exact compact-string label audit; assumes the standard T-duality dictionary."""
from fractions import Fraction as Q
import json
from pathlib import Path


def data(r, n, w, alpha):
    a, b = Q(n, 1) / r, Q(w, 1) * r / alpha
    return {'mass_squared_compact': a*a + b*b, 'left': a+b,
            'right': a-b, 'right_squared': (a-b)**2}


def main():
    alphas = [Q(1, 2), Q(1), Q(2)]
    radii = [Q(1, 2), Q(1), Q(2), Q(3), Q(4)]
    pairs = [(n, w) for n in range(-3, 4) for w in range(-3, 4) if n*w == 0]
    total = failures = 0
    for alpha in alphas:
        for r in radii:
            for n, w in pairs:
                original = data(r, n, w, alpha)
                dual = data(alpha/r, w, n, alpha)
                assert original['mass_squared_compact'] == dual['mass_squared_compact']
                assert original['left'] == dual['left']
                assert original['right'] == -dual['right']
                assert original['right_squared'] == dual['right_squared']
                # Naive same-form winding-dependent predicate on the dual.
                failures += (w != 0) != (n != 0)
                total += 1
    # Two momentum states, equal and opposite charge; oscillator levels N=Nbar=1
    # are compatible with n*w=0. At alpha=1, R=2, each compact mass^2=1/4.
    r, alpha = Q(2), Q(1)
    states = [(1, 0), (-1, 0)]
    dual_states = [(w, n) for n, w in states]
    assert sum(n for n, _ in states) == 0
    assert sum(w for _, w in states) == 0
    assert sum(n for n, _ in dual_states) == 0
    assert sum(w for _, w in dual_states) == 0
    assert sum(w != 0 for n, w in states) == 0
    assert sum(w != 0 for n, w in dual_states) == 2
    assert all(data(r, n, w, alpha)['mass_squared_compact'] == Q(1, 4) for n, w in states)
    assert all(data(alpha/r, n, w, alpha)['mass_squared_compact'] == Q(1, 4) for n, w in dual_states)
    inv = data(r, 1, 0, alpha)['right_squared']
    # Two distinct T-invariant threshold rules disagree, so covariance alone
    # does not fix an experiential or subject selector.
    assert inv == Q(1, 4) and (inv > Q(1, 8)) and not (inv > Q(1, 2))
    result = {
        'status': 'passed',
        'scope': 'Free closed-string circle spectrum and stated dictionary; no consciousness, full interactions, or real-world compactification established.',
        'alpha_radius_charge_cases_checked': total,
        'naive_winding_predicate_duality_failures': failures,
        'example': {'alpha_prime': str(alpha), 'radius': str(r),
                    'dual_radius': str(alpha/r), 'states': states, 'dual_states': dual_states,
                    'compact_mass_squared_each': '1/4', 'naive_winding_counts': [0, 2],
                    'dual_invariant_right_momentum_squared_each': str(inv)},
        'selector_note': 'Two invariant threshold rules on p_R^2 disagree; invariance is necessary only under the declared experiential-equivalence premise and is not sufficient.',
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
