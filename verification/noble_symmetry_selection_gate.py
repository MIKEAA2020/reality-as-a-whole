#!/usr/bin/env python3
"""Finite information bookkeeping; not a theory of life or consciousness."""
from fractions import Fraction as F
from itertools import permutations, product
from math import log2, isclose
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]


def entropy(prob):
    return -sum(float(p) * log2(float(p)) for p in prob if p)


def main():
    # Distinct probability weights ensure each relabeling can be distinguished.
    p = (F(1, 10), F(2, 10), F(3, 10), F(4, 10))
    h = entropy(p)
    count = 0
    for perm in permutations(range(4)):
        q = tuple(p[i] for i in perm)
        assert isclose(entropy(q), h, abs_tol=1e-12)
        count += 1
    # Two fair, independent draws; select 1 if at least one is 1.
    pairs = list(product((0, 1), repeat=2))
    out = [int(any(x)) for x in pairs]
    q = F(sum(out), len(out))
    assert q == F(3, 4)
    h_out = entropy((q, 1-q))
    # The embedding X -> (X, OR(X)) retains every input; no information is erased.
    joint = {(x, int(any(x))) for x in pairs}
    assert len(joint) == len(pairs)
    h_input = entropy([F(1, 4)] * 4)
    h_joint = entropy([F(1, 4)] * len(joint))
    h_conditional = h_input - h_out
    assert isclose(h_joint, h_input, abs_tol=1e-12)
    assert isclose(h_conditional, 2 - h_out, abs_tol=1e-12)
    report = {
        'scope': 'Finite Shannon-information exercise only; no thermodynamic, biological, phenomenal or gravity result.',
        'permutations_checked': count,
        'input_distribution': [str(x) for x in p],
        'permutation_entropy_bits': h,
        'independent_fair_draws': 2,
        'selected_one_probability': str(q),
        'selected_output_entropy_bits': h_out,
        'full_input_and_reversible_embedded_joint_entropy_bits': h_joint,
        'conditional_input_entropy_given_output_bits': h_conditional,
        'selecting_success_probability_is_not_guaranteed': True
    }
    (ROOT / 'verification/noble_symmetry_selection_gate.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
