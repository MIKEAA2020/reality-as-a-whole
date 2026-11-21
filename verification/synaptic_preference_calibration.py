#!/usr/bin/env python3
"""Invented-probability calibration and channel-selectivity control; no patient data."""
import json
import math
from pathlib import Path

P = {'on_minus': 1/5, 'on_plus': 3/5, 'off_minus': 3/10, 'off_plus': 1/2}


def logit(p):
    if not 0 < p < 1:
        raise ValueError('logit requires a probability strictly between 0 and 1')
    return math.log(p / (1-p))


def interaction(p_minus, p_plus):
    return logit(p_plus) - logit(p_minus)


def delta(p):
    return interaction(p['on_minus'], p['on_plus']) - interaction(p['off_minus'], p['off_plus'])


def simultaneous_delta_interval(p, n, alpha):
    if n <= 0 or not 0 < alpha < 1 or set(p) != set(P):
        raise ValueError('invalid design or missing arms')
    epsilon = math.sqrt(math.log(8/alpha)/(2*n))
    intervals = {k: (max(0.0, v-epsilon), min(1.0, v+epsilon)) for k, v in p.items()}
    if any(lo <= 0 or hi >= 1 for lo, hi in intervals.values()):
        # On this simple conservative procedure the log-odds range is unbounded.
        raise ValueError('cell probability interval touches 0 or 1; no finite certificate')
    lo = (logit(intervals['on_plus'][0]) - logit(intervals['on_minus'][1])
          - logit(intervals['off_plus'][1]) + logit(intervals['off_minus'][0]))
    hi = (logit(intervals['on_plus'][1]) - logit(intervals['on_minus'][0])
          - logit(intervals['off_plus'][0]) + logit(intervals['off_minus'][1]))
    return epsilon, (lo, hi)


def target_interval(bounds, drift, attenuation):
    lo, hi = bounds
    lamlo, lamhi = attenuation
    if lo > hi or drift < 0 or not 0 < lamlo <= lamhi <= 1:
        raise ValueError('invalid intervals')
    extremes = [(d-r)/lam for d in (lo, hi) for r in (-drift, drift) for lam in (lamlo, lamhi)]
    return min(extremes), max(extremes)


def relabel(p, flip_a=False, flip_b=False):
    result = {}
    for gate in ('on', 'off'):
        for label in ('minus', 'plus'):
            other = ('plus' if label == 'minus' else 'minus') if flip_a else label
            val = p[gate+'_'+other]
            result[gate+'_'+label] = 1-val if flip_b else val
    return result


def main():
    don = interaction(P['on_minus'], P['on_plus'])
    doff = interaction(P['off_minus'], P['off_plus'])
    observed_delta = delta(P)
    epsilon, interval = simultaneous_delta_interval(P, 10000, .05)
    cases = {}
    for b in (.3, 1.2):
        bounds = target_interval(interval, b, (.5, 1))
        cases[str(b)] = {'target_interval': bounds,
                         'sign': '+' if bounds[0] > 0 else '-' if bounds[1] < 0 else 'unresolved'}
    rivals = []
    for k in (1, -.25):
        r0, r1 = don-k, doff
        rivals.append({'K': k, 'lambda': 1, 'R_on': r0, 'R_off': r1,
                       'delta_residual': r0-r1})
    assert math.isclose(observed_delta, math.log(18/7))
    assert all(abs(x['delta_residual']) <= 1.2 for x in rivals)
    result = {'scope': 'invented probabilities and calibration assumptions; not neural data',
              'probabilities': P, 'D_on': don, 'D_off': doff, 'delta': observed_delta,
              'epsilon_simultaneous_95pct': epsilon, 'delta_interval': interval,
              'cases': cases, 'observationally_identical_rivals': rivals}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
