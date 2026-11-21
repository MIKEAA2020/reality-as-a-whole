#!/usr/bin/env python3
"""Discrete support/production diagnostic, not a model of human consciousness."""
import itertools
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent / 'klinge_event_sustainment.json'


def _bits(values):
    if any(type(v) is not int or v not in (0, 1) for v in values):
        raise ValueError('sequences must contain only integer bits')


def event_activity(production, duration):
    """Count active untruncated events per slot; no births before slot 0."""
    if type(duration) is not int or duration < 1:
        raise ValueError('duration must be a positive integer')
    _bits(production)
    return [sum(production[max(0, t-duration+1):t+1]) for t in range(len(production))]


def lifetime_covered(base, production, duration):
    """Check lifetime only inside the finite observed horizon."""
    if len(base) != len(production):
        raise ValueError('history length mismatch')
    _bits(base); _bits(production)
    if type(duration) is not int or duration < 1:
        raise ValueError('duration must be a positive integer')
    if any(p > b for b, p in zip(base, production)):
        raise ValueError('production requires an active base at its start')
    return all(base[t] for s, p in enumerate(production) if p
               for t in range(s, min(len(base), s+duration)))


def present_supported(base, production, duration):
    if len(base) != len(production):
        raise ValueError('history length mismatch')
    _bits(base); _bits(production)
    return all(n == 0 or base[t] == 1 for t, n in enumerate(event_activity(production, duration)))


def window_counts(duration):
    windows = list(itertools.product((0, 1), repeat=duration))
    buckets = {(b, e): 0 for b in (0, 1) for e in (0, 1)}
    for history in windows:
        buckets[(history[-1], int(any(history)))] += 1
    differing_pairs = sum(buckets[(b, 0)] * buckets[(b, 1)] for b in (0, 1))
    return {'duration': duration, 'windows': len(windows),
            'active_without_current_base': buckets[(0, 1)],
            'same_base_different_activity_unordered_pairs': differing_pairs}


def nonoverlapping(production, duration):
    if type(duration) is not int or duration < 1:
        raise ValueError('duration must be a positive integer')
    _bits(production)
    starts = [t for t, p in enumerate(production) if p]
    return all(b-a >= duration for a, b in zip(starts, starts[1:]))


def finite_horizon_counts(duration, length=6, require_nonoverlap=False):
    # Joint symbols (B,P), restricted to P<=B: 3 possibilities per slot.
    allowed_symbols = ((0, 0), (1, 0), (1, 1))
    count = supported = covered = boundary_underdetermined = 0
    for values in itertools.product(allowed_symbols, repeat=length):
        base, production = map(list, zip(*values))
        if require_nonoverlap and not nonoverlapping(production, duration):
            continue
        a = present_supported(base, production, duration)
        b = lifetime_covered(base, production, duration)
        if a != b:
            raise AssertionError('coverage equivalence failed')
        count += 1
        supported += a
        covered += b
        # An observed supported event may extend beyond our data boundary.
        boundary_underdetermined += a and any(p and s + duration > length for s, p in enumerate(production))
    return {'duration': duration, 'horizon': length, 'allowed_histories': count,
            'supported_at_all_observed_slots': supported,
            'all_event_lifetimes_covered_within_horizon': covered,
            'supported_but_some_events_extend_beyond_horizon': boundary_underdetermined}


def main():
    windows = [window_counts(d) for d in range(1, 9)]
    for row in windows:
        if row['active_without_current_base'] != 2**(row['duration']-1)-1:
            raise AssertionError('unrestricted window formula failed')
    horizon = [finite_horizon_counts(d) for d in range(1, 5)]
    for row in horizon:
        if row['allowed_histories'] != 3**6:
            raise AssertionError('invalid horizon enumeration')
    nonoverlap_counts = [finite_horizon_counts(d, require_nonoverlap=True) for d in range(1, 5)]
    single = [1, 1, 1, 0, 0, 0]
    overlap = [1, 0, 1, 0, 0, 0]
    sequential_base = [1, 1, 1, 1, 0, 0]
    sequential_starts = [1, 0, 0, 1, 0, 0]
    assert nonoverlapping(sequential_starts, 3)
    assert not present_supported(sequential_base, sequential_starts, 3)
    result = {'status': 'checked',
              'scope': 'Specified Boolean histories only; not an empirical or metaphysical possibility claim.',
              'window_model': 'P=B; active iff any start in last d slots',
              'window_counts': windows,
              'conditional_finite_horizon_model': 'P<=B; no births before slot zero; coverage tested only within six slots',
              'finite_horizon_counts': horizon,
              'post_result_nonoverlap_finite_horizon_counts': nonoverlap_counts,
              'examples': {'continuous_base_stops_duration_3': {'base': single, 'active_event_counts': event_activity(single, 3)},
                           'two_starts_duration_3': {'production': overlap, 'active_event_counts': event_activity(overlap, 3)},
                           'sequential_events_duration_3': {'base': sequential_base, 'production': sequential_starts,
                                                            'active_event_counts': event_activity(sequential_starts, 3)}},
              'limitations': 'A formal base bit is not a complete microstate; event occupancy is not an established phenomenal field, experience, personal identity or cause. Outside-horizon support is not tested.',
              'plan': 'KLINGE_EVENT_SUSTAINMENT_FIXED_PLAN.md'}
    OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
