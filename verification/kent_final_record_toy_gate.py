#!/usr/bin/env python3
"""Finite consistency checks inspired by Kent's 2015 toy models, not a QFT replay.

Use two deterministic hypotheses and hypothetical final photon-location records.
All coordinates and posterior probabilities are exact Fractions. No assertion
is made that this idealized discrete construction defines a continuum beable.
"""
from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
P = (F(1, 3), F(2, 3))  # branch 0 (x1=0) and branch 1 (x2=1)


def outside(y, z):
    """Spacelike separation in 1+1 dimensions, c=1; boundary excluded."""
    t, x = y
    T, X = z
    assert T > t
    return abs(X - x) > T - t


def boost(z):
    """Passive boost with v=3/5, gamma=5/4."""
    t, x = z
    return ((5*t - 3*x)/4, (5*x - 3*t)/4)


def records(T, photons):
    # Each row is a possible detector location and its deterministic occupancy
    # in branch 0 and branch 1 respectively. x1=0,x2=1,t1=1,t2=2.
    rows = [((T, 1-T), (1, 0)), ((T, 3-T), (0, 1))]
    if photons == 2:
        rows.extend([((T, T-2), (1, 0)), ((T, T), (0, 1))])
    return rows


def local_posterior(y, rows, actual):
    compatible = []
    for h in range(2):
        compatible.append(all(occupancy[h] == occupancy[actual]
                              for z, occupancy in rows if outside(y, z)))
    weights = [P[h] if compatible[h] else F(0) for h in range(2)]
    total = sum(weights)
    assert total > 0  # actual branch always compatible with its own data
    return tuple(w / total for w in weights)


def beables(t, rows, actual):
    # The mass in location i equals the posterior probability of hypothesis i.
    return tuple(local_posterior((t, F(i)), rows, actual)[i] for i in range(2))


def pair(xs):
    return [str(x) for x in xs]


def main():
    checks = 0
    times = [F(-2), F(-1, 2), F(0), F(1, 2), F(1), F(3, 2), F(2), F(3)]
    samples = {}
    for T in (F(8), F(16), F(64)):
        for n in (1, 2):
            rows = records(T, n)
            for t in times:
                for i in (0, 1):
                    y = (t, F(i))
                    for z, _ in rows:
                        assert outside(y, z) == outside(boost(y), boost(z))
                        checks += 1
            # Strict light-cone condition at the switch itself is material.
            assert beables(F(-1, 2), rows, 0) == P
            checks += 1
            if n == 1:
                assert beables(F(0), rows, 0) == P
                assert beables(F(1, 2), rows, 0) == (P[0], F(0))
                assert beables(F(1), rows, 0) == (P[0], F(0))
                assert beables(F(3, 2), rows, 0) == (F(1), F(0))
                checks += 4
            else:
                for actual in (0, 1):
                    assert beables(F(0), rows, actual) == P
                    assert beables(F(1, 2), rows, actual) == tuple(F(i == actual) for i in (0, 1))
                    checks += 2
            samples[f'T={T},photons={n}'] = {
                str(t): pair(beables(t, rows, 0)) for t in (F(-1, 2), F(0), F(1, 2), F(1), F(3, 2))
            }
    out = {'status': 'passed', 'exact_assertions': checks, 'branch_prior': pair(P),
           'samples_actual_first_branch': samples,
           'scope': '1+1 discrete deterministic records, prescribed branch prior; checks only selected matter-beable points. No claim of QFT, generic asymptotic convergence, full stress-energy conservation, physical observation or phenomenal subject derivation.'}
    (ROOT / 'verification/kent_final_record_toy_gate.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
