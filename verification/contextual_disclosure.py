"""Exact standard quantum witnesses for contextual finite disclosure.

Reuses rational-complex scalars only; does not import a consciousness assignment.
The Peres--Mermin obstruction and ideal record copying are standard mathematics,
not new physics, empirical data, an actual outcome selector, or an omniscience proof.
Run from any directory: python /path/to/verification/contextual_disclosure.py
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

from operational_probability_reconstruction import G, scalar


def matrix(rows):
    return tuple(tuple(scalar(x) for x in row) for row in rows)


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def scale(t, a):
    return tuple(tuple(scalar(t) * x for x in row) for row in a)


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def mul(a, b):
    return tuple(tuple(sum((a[i][k] * b[k][j] for k in range(len(b))), G())
                       for j in range(len(b[0]))) for i in range(len(a)))


def adjoint(a):
    return tuple(tuple(a[j][i].conj() for j in range(len(a)))
                 for i in range(len(a[0])))


def trace(a):
    return sum((a[i][i] for i in range(len(a))), G())


def tensor(a, b):
    return tuple(tuple(a[i][j] * b[k][l]
                       for j in range(len(a[0])) for l in range(len(b[0])))
                 for i in range(len(a)) for k in range(len(b)))


def tensors(*items):
    out = matrix([[1]])
    for item in items:
        out = tensor(out, item)
    return out


def conjugate(u, a):
    return mul(mul(u, a), adjoint(u))


def expect(rho, a):
    return trace(mul(rho, a))


def real_string(x):
    assert x.im == 0
    return str(x.re)


I = eye(2)
X = matrix([[0, 1], [1, 0]])
Y = matrix([[0, G(0, -1)], [G(0, 1), 0]])
Z = matrix([[1, 0], [0, -1]])
P0 = matrix([[1, 0], [0, 0]])
P1 = matrix([[0, 0], [0, 1]])
PLUS = matrix([[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]])


def contextual_witness():
    # Each row and column is a jointly measurable context.
    square = [tensors(X, I), tensors(I, X), tensors(X, X),
              tensors(I, Y), tensors(Y, I), tensors(Y, Y),
              tensors(X, Y), tensors(Y, X), tensors(Z, Z)]
    contexts = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8)]
    targets = [1, 1, 1, 1, 1, -1]
    unit = eye(4)
    rho = scale(Q(1, 4), unit)
    distributions = []
    for observable in square:
        assert adjoint(observable) == observable
        assert mul(observable, observable) == unit
        assert expect(rho, observable) == scalar(0)
    for context, target in zip(contexts, targets):
        joint_product = unit
        for i in context:
            joint_product = mul(joint_product, square[i])
        assert joint_product == scale(target, unit)
        for i, j in [(0, 1), (0, 2), (1, 2)]:
            assert mul(square[context[i]], square[context[j]]) == mul(square[context[j]], square[context[i]])
        total = scale(0, unit)
        distribution = {}
        projectors = []
        for signs in product((-1, 1), repeat=3):
            projector = unit
            for i, sign in zip(context, signs):
                projector = mul(projector, scale(Q(1, 2), add(unit, scale(sign, square[i]))))
            assert adjoint(projector) == projector
            assert mul(projector, projector) == projector
            parity_ok = signs[0] * signs[1] * signs[2] == target
            probability = expect(rho, projector)
            assert probability == scalar(Q(1, 4) if parity_ok else 0)
            assert trace(projector) == scalar(1 if parity_ok else 0)
            total = add(total, projector)
            projectors.append(projector)
            distribution[signs] = probability
        assert total == unit
        for i in range(8):
            for j in range(i):
                assert mul(projectors[i], projectors[j]) == scale(0, unit)
        # The two contexts containing any one observable agree on its marginal.
        for local_index in range(3):
            for sign in (-1, 1):
                assert sum((p for signs, p in distribution.items()
                            if signs[local_index] == sign), G()) == scalar(Q(1, 2))
        distributions.append(distribution)
    counts = []
    for values in product((-1, 1), repeat=9):
        counts.append(sum(values[a] * values[b] * values[c] == target
                          for (a, b, c), target in zip(contexts, targets)))
    assert max(counts) == 5
    assert 6 not in counts
    return {
        'contexts': 6,
        'local_joint_outcome_probabilities_checked': 48,
        'nonzero_outcomes_per_context': 4,
        'each_nonzero_probability': '1/4',
        'shared_observable_marginals_agree': True,
        'one_common_quantum_state': 'I_4/4',
        'context_product_signs': targets,
        'noncontextual_value_assignments_exhausted': len(counts),
        'assignments_satisfying_all_six_constraints': counts.count(6),
        'maximum_constraints_satisfied': max(counts),
    }


def cnot(control, target):
    # Three-qubit basis |S,A,B>; qubit 0 is the most significant bit.
    rows = [[0] * 8 for _ in range(8)]
    for old in range(8):
        new = old ^ (1 << (2 - target)) if old & (1 << (2 - control)) else old
        rows[new][old] = 1
    return matrix(rows)


def record_witness():
    unit = eye(8)
    u = mul(cnot(1, 2), cnot(0, 1))
    assert mul(adjoint(u), u) == unit == mul(u, adjoint(u))
    initial = tensors(PLUS, P0, P0)
    rho = conjugate(u, initial)
    expected = [[0] * 8 for _ in range(8)]
    for i in (0, 7):
        for j in (0, 7):
            expected[i][j] = Q(1, 2)
    assert rho == matrix(expected)
    za, zb, zazb, xxx = (tensors(I, Z, I), tensors(I, I, Z),
                         tensors(I, Z, Z), tensors(X, X, X))
    assert expect(rho, za) == expect(rho, zb) == scalar(0)
    assert expect(rho, zazb) == expect(rho, xxx) == scalar(1)
    joint = {}
    for a, b in product((0, 1), repeat=2):
        projector = tensors(I, (P0, P1)[a], (P0, P1)[b])
        p = expect(rho, projector)
        assert p == scalar(Q(1, 2) if a == b else 0)
        joint[f'{a}{b}'] = real_string(p)
    pinching = scale(0, unit)
    for a in (0, 1):
        e = tensors(I, (P0, P1)[a], I)
        block = mul(mul(e, rho), e)
        p = trace(block)
        assert p == scalar(Q(1, 2))
        conditioned = scale(2, block)
        assert trace(conditioned) == scalar(1)
        assert expect(conditioned, tensors(I, I, (P0, P1)[a])) == scalar(1)
        assert expect(conditioned, zazb) == scalar(1)
        pinching = add(pinching, block)
    assert pinching != rho
    assert expect(pinching, xxx) == scalar(0)
    # Restriction to the diagonal record algebra loses none of its statistics;
    # applying pinching to the global state really does lose joint coherence.
    for a, b in product((0, 1), repeat=2):
        e = tensors(I, (P0, P1)[a], (P0, P1)[b])
        assert expect(rho, e) == expect(pinching, e)
    assert trace(mul(rho, rho)) == scalar(1)
    assert trace(mul(pinching, pinching)) == scalar(Q(1, 2))
    return {
        'specified_dynamics': 'CNOT(S,A) followed by CNOT(A,B)',
        'joint_record_probabilities': joint,
        'each_record_Z_expectation': '0',
        'record_agreement_ZA_ZB_expectation': '1',
        'conditional_matching_record_probability': '1',
        'global_XXX_coherence_before_pinching': '1',
        'global_XXX_coherence_after_pinching': '0',
        'record_statistics_preserved_by_pinching': True,
        'global_state_preserved_by_pinching': False,
        'actual_outcome_selected': False,
        'decoherence_or_long_term_record_robustness_modelled': False,
    }


def run():
    return {
        'status': 'passed',
        'arithmetic': 'exact rational complex; no floating point',
        'contextuality': contextual_witness(),
        'records': record_witness(),
        'scope': {
            'standard_quantum_results_not_novel_theorems': True,
            'physical_subject_boundary_derived': False,
            'phenomenal_character_derived': False,
            'absolute_awareness_proved': False,
            'physical_laws_or_initial_state_derived': False,
            'zero_residue_constitution_supplied': False,
        },
    }


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print('PASS: six compatible quantum contexts, no joint noncontextual valuation; unitary record copying, conditional agreement, and global-coherence distinction.')
