#!/usr/bin/env python3
"""Explicitly stipulated feedback/replay and phenomenal-label comparison, not real subjects."""
from itertools import product
from pathlib import Path
import json

NOMINAL = (0, 1, 1, 1)


def trace(inputs, mode, error_clamps=None):
    if len(inputs) != len(NOMINAL) or any(x not in (0, 1) for x in inputs):
        raise ValueError('Expected four binary inputs')
    if mode not in ('feedback', 'replay', 'direct_copy'):
        raise ValueError('Unknown mode')
    error_clamps = {} if error_clamps is None else error_clamps
    if any(t not in range(4) or v not in (0, 1) for t, v in error_clamps.items()):
        raise ValueError('Clamps must map valid times to binary values')
    memory = 0
    rows = []
    for t, u in enumerate(inputs):
        computed_error = u ^ memory
        output = error_clamps.get(t, computed_error)
        rows.append({'time': t, 'input': u, 'memory': memory, 'output': output})
        # Normally memory XOR error equals input, but an error-node clamp
        # distinguishes that causal update from a direct input-copy update.
        if mode == 'feedback':
            memory = memory ^ output
        elif mode == 'direct_copy':
            memory = u
        else:
            memory = NOMINAL[t]
    return rows


def outputs(rows):
    return tuple(r['output'] for r in rows)


def incidence(functional_feedback, biological_flag, rule):
    """Stipulated illustration only; neither rule is a validated experience test."""
    if rule == 'functional':
        return functional_feedback
    if rule == 'biology_required':
        return functional_feedback and biological_flag
    raise ValueError('Unknown illustrative rule')


def main():
    alt = (0, 1, 0, 0)
    nominal_f = trace(NOMINAL, 'feedback')
    nominal_r = trace(NOMINAL, 'replay')
    alt_f = trace(alt, 'feedback')
    alt_r = trace(alt, 'replay')
    assert nominal_f == nominal_r
    assert outputs(alt_f) == (0, 1, 1, 0)
    assert outputs(alt_r) == (0, 1, 1, 1)
    histories = tuple(product((0, 1), repeat=4))
    same = [h for h in histories if outputs(trace(h, 'feedback')) == outputs(trace(h, 'replay'))]
    assert same == [(0, 1, 1, 0), (0, 1, 1, 1)]
    assert all((h in same) == (h[:3] == NOMINAL[:3]) for h in histories)
    assignments = []
    for tag, feedback, bio in [('stipulated_anchored_human', True, True),
                               ('hypothetical_nonbiological_feedback', True, False),
                               ('hypothetical_nonbiological_replay', False, False)]:
        assignments.append({'case': tag, 'feedback': feedback, 'biological_flag': bio,
                            'functional_rule_E': incidence(feedback, bio, 'functional'),
                            'biology_required_rule_E': incidence(feedback, bio, 'biology_required')})
    receipt = {
        'scope': 'Stipulated four-step discrete process and artificial labels, not an empirical model, biological mechanism, phenomenal rule, or subject test.',
        'nominal_input': list(NOMINAL), 'nominal_identical_trace': nominal_f,
        'alternative_input': list(alt), 'alternative_feedback_trace': alt_f,
        'alternative_replay_trace': alt_r, 'enumerated_histories': len(histories),
        'matching_output_histories': [list(h) for h in same],
        'different_output_histories': len(histories)-len(same),
        'error_node_clamp_time_1_to_zero_feedback': trace(NOMINAL, 'feedback', {1: 0}),
        'error_node_clamp_time_1_to_zero_direct_copy': trace(NOMINAL, 'direct_copy', {1: 0}),
        'phenomenal_assignment_illustrations': assignments,
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
