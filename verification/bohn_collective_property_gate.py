#!/usr/bin/env python3
"""Finite illustrations of one-way plural-property transport.

Sets are a finite extensional bookkeeping semantics, not a reduction of
Bohn's plural ontology, real grounding, subjecthood, or actual experience.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json

from coupled_subject_boundary_gate import STATES, stationary
from integrated_subject_horizon_audit import mismatch

LEFT = frozenset((0, 1))
RIGHT = frozenset((2, 3))
ALL = frozenset(range(4))
SINGLETONS = {frozenset((i,)) for i in range(4)}


def toy_assignments(state):
    # Both local subjects are separately stipulated, and have the same
    # designated M type exactly when their respective physical bit is 1.
    forced = {pair for pair, q in ((LEFT, mismatch(state, (0, 1))),
                                   (RIGHT, mismatch(state, (2, 3)))) if q}
    return (frozenset(forced), frozenset(forced | {ALL}))


def transport(poly, permutation):
    return frozenset(frozenset(permutation[i] for i in p) for p in poly)


def run():
    pi = stationary(F(1, 4), (None,) * 4)
    both = F(0)
    models, relabel_checks = 0, 0
    for s, probability in pi.items():
        ql = mismatch(s, (0, 1))
        qr = mismatch(s, (2, 3))
        a, b = toy_assignments(s)
        assert (LEFT in a) == bool(ql) and (RIGHT in a) == bool(qr)
        assert (LEFT in b) == bool(ql) and (RIGHT in b) == bool(qr)
        assert ALL not in a and ALL in b
        assert all(singleton not in a and singleton not in b for singleton in SINGLETONS)
        # Explicit TDP implications for these two stipulated singular subjects.
        for property_extension in (a, b):
            assert not ql or LEFT in property_extension
            assert not qr or RIGHT in property_extension
            models += 1
            for perm in permutations(range(4)):
                p = transport(property_extension, perm)
                assert (frozenset(perm[i] for i in LEFT) in p) == bool(ql)
                assert (frozenset(perm[i] for i in RIGHT) in p) == bool(qr)
                assert (frozenset(perm[i] for i in ALL) in p) == (ALL in property_extension)
                assert not any(frozenset((i,)) in p for i in range(4))
                relabel_checks += 1
        if ql and qr:
            both += probability
    assert both == F(1, 16) and models == 32 and relabel_checks == 768
    # Exhaust the truth values of singular M, the singleton-whole grounding
    # claim, and the plural M. TDP is only an implication.
    satisfying = [(x, g, m) for x in (False, True) for g in (False, True)
                  for m in (False, True) if not (x and g) or m]
    assert len(satisfying) == 7
    assert all(m for x, g, m in satisfying if x and g)
    return {'status': 'passed',
            'scope': 'Finite extensional bookkeeping only; no literal sets in Bohn ontology, no independently justified grounding or lived subject.',
            'physical_q_both_one_probability': str(both),
            'physical_states': len(pi), 'two_property_extensions_per_state': 2,
            'property_assignments': models, 'simultaneous_relabel_checks': relabel_checks,
            'singleton_whole_control': 'literal TDP plus a singular whole as full ground implies the same M of its singleton plurality, not an independently established universal subject',
            'closure_note': 'No inference to union or one-subject-per-plurality was imposed; setting M(all) is an independent assignment.'}


def main():
    text = json.dumps(run(), indent=2) + '\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
