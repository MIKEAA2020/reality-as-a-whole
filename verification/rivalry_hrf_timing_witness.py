#!/usr/bin/env python3
"""Synthetic BOLD design witness, not a replay or an analysis of Roy data.

The toy uses a standard double-gamma-shaped HRF and samples two matched event
trains 1.142 seconds apart at TR 2.2 seconds.  The reported 1.142 seconds in
Roy is crossing-to-green-dominance-button latency, NOT the relative timing of
Roy's GLM regressors; that value is only a scale for the illustration.
"""
import json
import math
from pathlib import Path
from statistics import mean

TR = 2.2
ONSETS = [20.0 + 25.0 * i for i in range(10)]
SHIFT = 1.142
N = 124


def hrf(t):
    if t < 0:
        return 0.0
    return math.exp(-t) * (t**5 / math.factorial(5) - t**15 / (6 * math.factorial(15)))


def regressor(shift):
    return [sum(hrf(i * TR - onset - shift) for onset in ONSETS) for i in range(N)]


def centered(x):
    m = mean(x)
    return [v - m for v in x]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def correlation(a, b):
    a, b = centered(a), centered(b)
    return dot(a, b) / math.sqrt(dot(a, a) * dot(b, b))


def main():
    a, b = regressor(0.0), regressor(SHIFT)
    rho = correlation(a, b)
    # OLS variance inflation relative to an intercept + this regressor alone,
    # for the SAME regressor and spherical homoskedastic errors. Intercept is
    # removed by centering. Actual fMRI may have other nuisance regressors and
    # autocorrelated errors, so this does not estimate Roy's variance.
    vif = 1.0 / (1.0 - rho * rho)
    assert abs(correlation(a, a) - 1.0) < 1e-12
    assert abs(correlation(a, b) - correlation(b, a)) < 1e-12
    assert 0.90 < rho < 0.92
    assert 5.0 < vif < 6.0
    out = {
        "kind": "synthetic design witness; no participant data",
        "tr_s": TR, "n_samples": N, "event_onsets_s": ONSETS,
        "shift_s": SHIFT,
        "hrf": "exp(-t)*(t**5/5! - t**15/(6*15!)) for t>=0; zero otherwise",
        "centered_regressor_correlation": rho,
        "ols_variance_inflation_for_one_coefficient": vif,
        "assumptions": "intercept, two regressors, iid equal-variance errors; no filtering or nuisance regressors",
        "warning": "The 1.142 s published cross-to-button mean is not the GLM cross-to-mixing-midpoint delay. This is not the actual design.",
    }
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))
    print('Wrote', path)


if __name__ == '__main__':
    main()
