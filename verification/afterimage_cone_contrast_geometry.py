#!/usr/bin/env python3
"""Exact illustrative geometry, not calibrated colour or a physiological model."""
import json
from fractions import Fraction as F


def project(lms):
    return (lms[0] - lms[2], lms[1] - lms[2])


def calculate(background, delta):
    if any(b <= 0 for b in background) or any(1 + d <= 0 for d in delta):
        raise ValueError('background and inducer LMS must be strictly positive')
    # Background-normalized subtractive increment vs componentwise Weber contrast.
    linear = tuple(-d for d in delta)
    nonlinear = tuple(-d / (1 + d) for d in delta)
    approximation_error = tuple(n - l for n, l in zip(nonlinear, linear))
    p, q = project(linear), project(nonlinear)
    determinant = p[0]*q[1] - p[1]*q[0]
    return linear, nonlinear, approximation_error, p, q, determinant


def encode(seq):
    return [str(v) for v in seq]


def main():
    b = (F(1), F(1), F(1)); d = (F(1, 2), F(1, 4), F(0))
    lin, non, err, p, q, det = calculate(b, d)
    print(json.dumps({'kind': 'Invented normalized LMS example; projection is arbitrary, not calibrated human hue.',
                      'background_LMS': encode(b), 'relative_inducer_increment': encode(d),
                      'inducer_LMS': encode(tuple(bi*(1+di) for bi,di in zip(b,d))),
                      'linear_normalized_reversal': encode(lin), 'weber_contrast': encode(non),
                      'weber_minus_linear': encode(err),
                      'projection': '(L-S, M-S)', 'projected_linear': encode(p),
                      'projected_weber': encode(q), 'projected_determinant': str(det)}, indent=2))

if __name__ == '__main__':
    main()
