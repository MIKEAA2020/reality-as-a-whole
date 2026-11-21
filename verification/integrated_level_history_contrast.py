#!/usr/bin/env python3
"""Post-inspection exact check of level vs onset in the existing four-spin sector.

No claim that q is free energy, human pain, experience, or a subject. This
compares two explicitly stipulated quality labels using the very same kernel.
"""
from fractions import Fraction as F
from pathlib import Path
import json

from coupled_subject_boundary_gate import STATES, stationary
from integrated_subject_horizon_audit import kernel, mismatch


def run():
    t = F(1, 4)
    pi = stationary(t, (None,) * 4)
    transition = kernel(t)
    joint = {(a, b): F(0) for a in (0, 1) for b in (0, 1)}
    # Group by complete current physical state and the rival's onset label.
    conditional = {s: {0: F(0), 1: F(0)} for s in STATES}
    flows = []
    for previous in STATES:
        for current, probability in transition[previous].items():
            mass = pi[previous] * probability
            before, now = mismatch(previous), mismatch(current)
            onset = int(before == 0 and now == 1)
            joint[before, now] += mass
            conditional[current][onset] += mass
            flows.append((previous, current, mass))
            assert mass == pi[current] * transition[current].get(previous, F(0))
    assert joint == {(0, 0): F(295, 448), (0, 1): F(41, 448),
                     (1, 0): F(41, 448), (1, 1): F(71, 448)}
    # Any deterministic (or independently randomized) current-state-only
    # classifier incurs this sharp Bayes error under the stipulated onset label.
    best_current_error = sum(min(classes.values()) for classes in conditional.values())
    assert best_current_error == F(41, 448)
    current = (1, -1, 1, 1)
    previous0 = (-1, -1, 1, 1)
    previous1 = current
    assert mismatch(previous0) == 0 and mismatch(previous1) == mismatch(current) == 1
    assert pi[previous0] * transition[previous0][current] > 0
    assert pi[previous1] * transition[previous1][current] > 0
    disagreements = sum(mass for prev, curr, mass in flows
                        if mismatch(curr) != int(mismatch(prev) == 0 and mismatch(curr) == 1))
    assert disagreements == F(71, 448)
    result = {
        'status': 'passed',
        'scope': 'Post-inspection mathematical comparison; q is not an empirical measure, free energy, feeling, or a derived subject. No causal report channel is supplied.',
        'probabilities': {f'{a}->{b}': str(p) for (a, b), p in joint.items()},
        'level_vs_onset_disagreement': str(disagreements),
        'best_full_current_state_only_error_for_onset': str(best_current_error),
        'matched_current_witness': {
            'current': current,
            'previous_aligned': previous0,
            'previous_mismatched': previous1,
            'aligned_to_current_joint_mass': str(pi[previous0] * transition[previous0][current]),
            'mismatched_to_current_joint_mass': str(pi[previous1] * transition[previous1][current]),
        },
        'checks': 'exact detailed balance for every represented transition, all 16 complete current states, exact joint event probabilities',
    }
    return result


def main():
    text = json.dumps(run(), indent=2) + '\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
