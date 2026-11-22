#!/usr/bin/env python3
"""Exact synthetic witnesses for randomized binary-report contrasts, not real data."""
from fractions import Fraction as F
from pathlib import Path
import json


def observed_joint(coupling, sensitivity, false_positive, arm):
    """Aggregate (E0,E1) population and conditional Bernoulli report in one arm."""
    joint = {(e, y): F(0) for e in (0, 1) for y in (0, 1)}
    for (e0, e1), weight in coupling.items():
        e = (e0, e1)[arm]
        positive = sensitivity if e else false_positive
        joint[e, 1] += weight * positive
        joint[e, 0] += weight * (1 - positive)
    return joint


def stats(coupling, rates):
    assert sum(coupling.values()) == 1 and min(coupling.values()) >= 0
    joints = [observed_joint(coupling, *rates[a], a) for a in (0, 1)]
    p = [sum(v for (e, y), v in j.items() if e == 1) for j in joints]
    q = [sum(v for (e, y), v in j.items() if y == 1) for j in joints]
    return {'p': p, 'q': q, 'benefit': coupling.get((0, 1), F(0)),
            'harm': coupling.get((1, 0), F(0))}


def serialize(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, list):
        return [serialize(x) for x in value]
    if isinstance(value, dict):
        return {str(k): serialize(v) for k, v in value.items()}
    return value


def main():
    stable = [(F(9, 10), F(1, 20))] * 2
    monotone = {(0, 0): F(4, 17), (0, 1): F(4, 17),
                (1, 0): F(0), (1, 1): F(9, 17)}
    mixed = {(0, 0): F(0), (0, 1): F(8, 17),
             (1, 0): F(4, 17), (1, 1): F(5, 17)}
    unchanged = {(0, 0): F(1, 2), (1, 1): F(1, 2)}
    drift = [(F(9, 10), F(1, 10)), (F(9, 10), F(1, 2))]
    witnesses = {'stable_monotone': stats(monotone, stable),
                 'stable_mixed': stats(mixed, stable),
                 'channel_drift_no_experiential_effect': stats(unchanged, drift)}
    assert all(w['q'] == [F(1, 2), F(7, 10)] for w in witnesses.values())
    assert witnesses['stable_monotone']['p'] == witnesses['stable_mixed']['p'] == [F(9, 17), F(13, 17)]
    assert witnesses['channel_drift_no_experiential_effect']['p'] == [F(1, 2)] * 2
    q0, q1 = F(1, 2), F(7, 10)
    bounds = {'lower': (q1-q0)/(F(9,10)-F(1,20)),
              'upper': (q1-q0)/(F(3,4)-F(1,5))}
    assert bounds == {'lower': F(4,17), 'upper': F(4,11)}
    # Endpoint prevalence values are valid; hence the extremal bounds are attained.
    endpoint_p = [[(q-f)/(s-f) for q in (q0,q1)] for s,f in
                  [(F(9,10),F(1,20)), (F(3,4),F(1,5))]]
    assert endpoint_p == [[F(9,17),F(13,17)], [F(6,11),F(10,11)]]
    receipt = {'scope': 'Synthetic exact population probabilities, not an empirical experience assay.',
               'report_arm_probabilities': [q0,q1], 'shared_rate_contrast_bounds': bounds,
               'endpoint_prevalences': endpoint_p, 'witnesses': witnesses}
    Path(__file__).with_suffix('.json').write_text(json.dumps(serialize(receipt), indent=2)+'\n')
    print(json.dumps(serialize(receipt), indent=2))


if __name__ == '__main__':
    main()
