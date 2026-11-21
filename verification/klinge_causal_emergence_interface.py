#!/usr/bin/env python3
"""Finite illustration of immediate micro-cause vs micro-transition closure.

This is not Klinge's model, a human experiment, or a demonstration that the
model's stipulated interventions are physically or metaphysically possible.
"""
import itertools
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / 'klinge_causal_emergence_interface.json'


def check_bit(x):
    if type(x) is not int or x not in (0, 1):
        raise ValueError('binary integer required')


def emergent_step(base, macro):
    """Specified macro intervention changes a micro disposition, then its outcome."""
    check_bit(base); check_bit(macro)
    disposition = base ^ macro
    return disposition, disposition


def closed_control(base, macro):
    """Rival on same interface, with no macro effect on the disposition."""
    check_bit(base); check_bit(macro)
    return 0, 0


def receipt():
    rows = [(b, e, *emergent_step(b, e)) for b, e in itertools.product((0, 1), repeat=2)]
    baseline = [(b, b, *emergent_step(b, b)) for b in (0, 1)]
    control = [(b, b, *closed_control(b, b)) for b in (0, 1)]
    assert baseline == control
    assert all(d == y for _, _, d, y in rows)
    assert all(emergent_step(b, 0)[1] != emergent_step(b, 1)[1] for b in (0, 1))
    changed_vs_control = sum(emergent_step(b, 1-b) != closed_control(b, 1-b) for b in (0, 1))
    assert changed_vs_control == 2
    return {'status': 'checked',
            'scope': 'Illustrative binary structural equations only; no claim of physical or phenomenal instantiation.',
            'equations': {'emergent_model': 'D = B XOR E; Y = D',
                          'natural_regime': 'E = B', 'control': 'D = 0; Y = D'},
            'possible_input_pairs': len(rows), 'all_outcomes_equal_immediate_disposition': True,
            'base_values_for_which_outcome_changes_if_macro_is_set_to_0_vs_1': 2,
            'natural_base_values_with_identical_full_observed_records_between_models': len(baseline),
            'surgical_opposite_macro_settings_with_different_outputs': changed_vs_control,
            'counterfactual_qualification': 'Opposite-macro surgery violates the stipulated natural E=B relation; its physical or metaphysical feasibility is not established.',
            'interpretation': 'An immediate micro-description of an outcome and closure of the earlier micro-transition are distinct conditions; natural-data equality does not identify the macro intervention.'}


def main():
    result = receipt()
    OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
