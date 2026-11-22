#!/usr/bin/env python3
"""Exact finite toy of turnover and repair; not biology or conscious subjects."""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import json


def majority(state):
    return int(sum(state) >= 2)


def replace(state, site, incoming):
    s = list(state)
    s[site] = incoming
    return tuple(s)


def repair(state):
    return (majority(state),) * 3


def run(initial_bit, incoming, repair_after_each):
    state = (initial_bit,) * 3
    tokens = ['original-0', 'original-1', 'original-2']
    record = []
    for site, bit in enumerate(incoming):
        before = state
        old_token = tokens[site]
        tokens[site] = f'new-{site}'
        displaced = replace(state, site, bit)
        state = repair(displaced) if repair_after_each else displaced
        record.append({'site': site, 'incoming': bit, 'replaced_token': old_token,
                       'new_token': tokens[site], 'before': list(before),
                       'after_replacement': list(displaced), 'after_operation': list(state)})
    return state, tuple(tokens), record


def exact_probability(predicate, cases):
    values = tuple(cases)
    return Fraction(sum(bool(predicate(case)) for case in values), len(values))


def main():
    inputs = tuple(product((0, 1), repeat=3))
    cases = {}
    for bit in (0, 1):
        repaired = [run(bit, seq, True) for seq in inputs]
        unrepaired = [run(bit, seq, False) for seq in inputs]
        assert all(t == ('new-0', 'new-1', 'new-2') for _, t, _ in repaired + unrepaired)
        assert len({tuple(row['incoming'] for row in log) for _, _, log in repaired}) == 8
        cases[str(bit)] = {
            'repair_majority_preserved': str(exact_probability(lambda x: majority(x[0]) == bit, repaired)),
            'repair_unanimity_preserved': str(exact_probability(lambda x: x[0] == (bit,) * 3, repaired)),
            'no_repair_majority_preserved': str(exact_probability(lambda x: majority(x[0]) == bit, unrepaired)),
            'no_repair_unanimity_preserved': str(exact_probability(lambda x: x[0] == (bit,) * 3, unrepaired)),
            'repaired_final_state_counts': dict(sorted(Counter(''.join(map(str, x[0])) for x in repaired).items())),
            'unrepaired_final_state_counts': dict(sorted(Counter(''.join(map(str, x[0])) for x in unrepaired).items())),
        }
    burst = tuple(product((0, 1), repeat=2))
    def burst_run(seq):
        state = replace((0, 0, 0), 0, seq[0])
        state = replace(state, 1, seq[1])
        return repair(state)
    burst_fail = exact_probability(lambda seq: majority(burst_run(seq)) != 0, burst)
    hidden = {}
    for state in ((0, 0, 0), (0, 0, 1)):
        hidden[''.join(map(str, state))] = str(exact_probability(
            lambda bit: majority(replace(state, 0, bit)) == 1, (0, 1)))
    receipt = {
        'scope': 'Finite mathematical example with specified input distributions and a stipulated repair mechanism; no biological, physical energy or phenomenal inference.',
        'schedule': 'Sites 0, 1, 2 replaced once in order, independent equiprobable incoming bits; repair, when enabled, follows each replacement.',
        'paired_inputs_per_initial_bit': len(inputs),
        'results': cases,
        'two_replacements_before_repair_error_probability': str(burst_fail),
        'same_initial_majority_zero_different_next_majority_one_probability': hidden,
        'retained_repair_history_count': 8,
        'illustrative_repaired_history': run(0, (1, 0, 1), True)[2],
    }
    assert cases['0']['repair_majority_preserved'] == '1'
    assert cases['0']['no_repair_majority_preserved'] == '1/2'
    assert burst_fail == Fraction(1, 4)
    assert hidden == {'000': '0', '001': '1/2'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
