#!/usr/bin/env python3
"""Digital approximation of a continuous coupled feedback counterexample.

Dimensionless two-variable ODE, not a model of a brain or real EM field.
Exact rational Euler updates, compared to the known analytic solution.
"""
from fractions import Fraction
from pathlib import Path
import json
import math


def euler(n):
    x, y = Fraction(1), Fraction(0)
    h = Fraction(1, n)
    for _ in range(n):
        x, y = x + h*y, y - h*x
    return x, y


def main():
    rows = []
    previous = math.inf
    for n in (4, 16, 64, 256, 1024):
        x, y = euler(n)
        error = math.hypot(float(x)-math.cos(1), float(y)+math.sin(1))
        # Rotation has norm 1, Lipschitz constant 1, and local Euler error
        # <= h**2/2. Sum the explicit amplification factors (1+h)^k.
        geometric_bound = (float((1+Fraction(1,n))**n)-1)/(2*n)
        assert error <= geometric_bound + 1e-14
        assert error < previous
        previous = error
        rows.append({'steps': n, 'error_euclidean': error,
                     'proved_upper_bound': geometric_bound})
    output = {'status':'passed', 'ode':'x_prime=y, y_prime=-x; x(0)=1, y(0)=0; T=1',
              'algorithm':'explicit Euler with rational updates', 'cases': rows,
              'bound':'error <= ((1+1/n)^n - 1)/(2n) <= (e-1)/(2n)',
              'scope':'A computable two-variable counterexample to a general inference from continuity or feedback to digital non-approximability. Not a biological model, consciousness test, brain simulation, universal approximation theorem or computational cost estimate for a real brain.'}
    text=json.dumps(output,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
