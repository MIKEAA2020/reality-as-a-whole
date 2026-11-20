#!/usr/bin/env python3
"""Finite logic checks only: location inheritance and distinct priority labels."""
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
# b and s are atoms, w is their fusion. An atomic Boolean location models
# weak location in one region only; the example does not axiomatize spacetime.
objects = ('b', 's', 'w')
parts = {'b': {'b'}, 's': {'s'}, 'w': {'b', 's', 'w'}}

def inheritance(loc):
    return all(not loc[x] or loc[y] for y in objects for x in parts[y])

assignments = [dict(zip(objects, vals)) for vals in product((False, True), repeat=3)]
base_constraints = [a for a in assignments if not a['b'] and a['s'] and inheritance(a)]
assert base_constraints == [{'b': False, 's': True, 'w': True}]
# Conflating the located derivative and the fundamental base's parthood
# introduces s as part of b and makes those premises inconsistent.
assert all(not (a['s'] and not a['b'] and (not a['s'] or a['b'])) for a in assignments)
# Actual global E and C hold in both toy interpretations; a singleton modal
# frame with reflexive access makes every true global formula necessary.
models = []
for base_experiential in (False, True):
    E, C = True, True
    possible_not_E, possible_not_C = not E, not C
    row = {
        'base_experiential': base_experiential,
        'derivative_experience': E,
        'concrete_occurrence': C,
        'necessary_global_experience': not possible_not_E,
        'necessary_global_concrete_occurrence': not possible_not_C,
        'base_is_located': False,
        'totality_is_located': True,
    }
    models.append(row)
assert all(m['necessary_global_experience'] and m['necessary_global_concrete_occurrence'] for m in models)
assert models[0]['base_experiential'] != models[1]['base_experiential']
assert all(models[0][k] == models[1][k] for k in models[0] if k != 'base_experiential')
out = {
    'scope': 'Finite stipulated truth tables; not a spacetime derivation, actual grounding, or a test of consciousness.',
    'location_assignments_checked': len(assignments),
    'admissible_location_assignments': base_constraints,
    'conflated_parthood_consistent': False,
    'singleton_modal_interpretations': models,
    'warnings': ['Location is a one-region proxy.', 'The modal frame stipulates global modal collapse.', 'Experience and grounding direction are labels, not constructed or validated.'],
}
(ROOT / 'verification/timeless_whole_location_gate.json').write_text(json.dumps(out, indent=2) + '\n')
print('PASS: location inheritance, separated totality/base, and matched experiential labels')
print(out['scope'])
