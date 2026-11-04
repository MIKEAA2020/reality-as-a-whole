"""Exact derivation of operational transport from specified quantum channels.

No supplied entity-continuation table, phenomenal labels, experimental data,
new physics, or personal-identity assignment. Standard channels are examples,
not claims about actual brains. Matrix arithmetic is rational complex.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from pathlib import Path
import json

from contextual_disclosure import (G, I, X, Y, Z, P0, P1, add, adjoint,
                                  conjugate, expect, eye, matrix, mul,
                                  scale, scalar, tensor, trace)


MIXED = scale(Q(1, 2), I)
BACKGROUND = tensor(MIXED, MIXED)
SWAP = matrix([[1, 0, 0, 0], [0, 0, 1, 0],
               [0, 1, 0, 0], [0, 0, 0, 1]])


def identity(rho):
    return rho


def exchange(rho):
    return conjugate(SWAP, rho)


def symmetric(rho):
    return scale(Q(1, 2), add(rho, exchange(rho)))


def reset(rho):
    return scale(trace(rho), BACKGROUND)


CHANNELS = {'identity': identity, 'swap': exchange,
            'symmetric_routing': symmetric, 'reset': reset}


def marginal(rho, output):
    rows = [[G() for _ in range(2)] for _ in range(2)]
    for a, b, other in product(range(2), repeat=3):
        i, j = ((2*a + other, 2*b + other) if output == 0
                else (2*other + a, 2*other + b))
        rows[a][b] += rho[i][j]
    return tuple(tuple(row) for row in rows)


def pauli_state(axis, sign):
    return scale(Q(1, 2), add(I, scale(sign, axis)))


STATES = [pauli_state(axis, sign) for axis in (X, Y, Z) for sign in (-1, 1)]


def cptp_kraus_checks():
    # K=rational matrices in E(rho)=sum weight*K*rho*K^dagger.
    # Positive rational weights stand for squared irrational Kraus factors.
    units = []
    for row, col in product(range(4), repeat=2):
        a = [[0] * 4 for _ in range(4)]
        a[row][col] = 1
        units.append(matrix(a))
    terms = {
        'identity': [(Q(1), eye(4))],
        'swap': [(Q(1), SWAP)],
        'symmetric_routing': [(Q(1, 2), eye(4)), (Q(1, 2), SWAP)],
        'reset': [(Q(1, 4), k) for k in units],
    }
    # Matrix units span all inputs, including off-diagonal coherences.
    for name, kraus in terms.items():
        normalization = scale(0, eye(4))
        for weight, k in kraus:
            assert weight > 0
            normalization = add(normalization, scale(weight, mul(adjoint(k), k)))
        assert normalization == eye(4)
        for rho in units:
            result = scale(0, eye(4))
            for weight, k in kraus:
                result = add(result, scale(weight, conjugate(k, rho)))
            assert result == CHANNELS[name](rho)
    return 4 * len(units)


def response_checks(name, channel):
    expected = {
        'identity': ((Q(1), Q(0)), (Q(0), Q(1))),
        'swap': ((Q(0), Q(1)), (Q(1), Q(0))),
        'symmetric_routing': ((Q(1, 2), Q(1, 2)), (Q(1, 2), Q(1, 2))),
        'reset': ((Q(0), Q(0)), (Q(0), Q(0))),
    }[name]
    checks = 0
    for source in range(2):
        # Vary the other independent input too, rather than assuming it is zero.
        for other in STATES + [MIXED]:
            for axis in (X, Y, Z):
                inputs = [tensor(pauli_state(axis, sign), other) if source == 0
                          else tensor(other, pauli_state(axis, sign)) for sign in (1, -1)]
                outputs = [channel(rho) for rho in inputs]
                for target in range(2):
                    delta = add(marginal(outputs[0], target), scale(-1, marginal(outputs[1], target)))
                    # Opposite Pauli preparations have difference axis. Reduced
                    # channel formulas in the report show expected is the exact
                    # optimal trace-distance response, not just a sampled bound.
                    assert delta == scale(expected[target][source], axis)
                    assert expect(delta, axis) == scalar(2 * expected[target][source])
                    checks += 1
    support = [(source, target) for source in range(2) for target in range(2)
               if expected[target][source] > 0]
    return {'trace_distance_response_output_by_input': [[str(x) for x in row] for row in expected],
            'causal_support_input_to_output': [list(x) for x in support],
            'exact_intervention_response_checks': checks}


def permute_relation(relation, inputs, outputs):
    return frozenset((inputs[source], outputs[target]) for source, target in relation)


def run():
    assert mul(SWAP, SWAP) == eye(4)
    kraus_checks = cptp_kraus_checks()
    results = {}
    for name, channel in CHANNELS.items():
        assert channel(BACKGROUND) == BACKGROUND
        results[name] = response_checks(name, channel)
    # The symmetric channel has independent input/output swap symmetries.
    for rho in [tensor(a, b) for a in STATES for b in STATES]:
        assert symmetric(exchange(rho)) == symmetric(rho)
        assert exchange(symmetric(rho)) == symmetric(rho)
    permutations_2 = list(permutations(range(2)))
    matchings = [frozenset(enumerate(p)) for p in permutations_2]
    invariant = [m for m in matchings if all(permute_relation(m, p, q) == m
                 for p in permutations_2 for q in permutations_2)]
    assert not invariant
    full_support = frozenset(product(range(2), repeat=2))
    assert all(permute_relation(full_support, p, q) == full_support
               for p in permutations_2 for q in permutations_2)
    # Covariance, not removal of real input/output tokens, is the requirement.
    support_i = frozenset(map(tuple, results['identity']['causal_support_input_to_output']))
    support_s = frozenset(map(tuple, results['swap']['causal_support_input_to_output']))
    assert permute_relation(support_i, (0, 1), (1, 0)) == support_s
    # Static correlation does not create cross-input causal transport in identity.
    correlated = scale(Q(1, 2), add(tensor(P0, P0), tensor(P1, P1)))
    assert expect(correlated, tensor(Z, Z)) == scalar(1)
    assert marginal(correlated, 0) == marginal(correlated, 1) == MIXED
    for sign in (-1, 1):
        # Physical local replacement breaks the correlation; the other input's
        # marginal stays fixed, rather than being conditioned on the outcome.
        replaced = tensor(pauli_state(Z, sign), marginal(correlated, 1))
        assert marginal(identity(replaced), 1) == MIXED
    return {
        'status': 'passed',
        'arithmetic': 'exact rational complex; no floating point',
        'channel_action_matrix_basis_checks': kraus_checks,
        'background_frames_identical_for_all_four_channels': True,
        'background': 'I_4/4',
        'channels': results,
        'symmetric_channel_independent_input_output_permutation_symmetry': True,
        'deterministic_bijective_continuations_invariant_under_these_symmetries': len(invariant),
        'many_to_many_causal_support_covariant': True,
        'static_correlation_distinguished_from_interventional_dependence': True,
        'scope': {
            'transport_relation_derived_from_channels_not_identity_markers': True,
            'tensor_factors_and_interventions_supplied': True,
            'channels_or_quantum_laws_derived_from_absolute': False,
            'physical_carrier_identity_derived': False,
            'subject_continuity_derived': False,
            'phenomenal_character_derived': False,
            'full_environment_or_unique_channel_dilation_identified': False,
            'standard_mathematics_not_metaphysical_breakthrough': True,
        },
    }


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print('PASS: identical background frames, four derived causal-transport relations, CPTP checks, and symmetry obstruction to a unique bijective continuation.')
