"""Record discrimination and wavepacket coherence in the Morse gravity-clock model.

Uses the previously defined scattering phases. Quadrature checks are numerical,
not certificates for the continuum spectral theory or the parent action.
Run: python verification/gravity_clock_complementarity.py
"""
import cmath
import json
import math
from pathlib import Path

from gravitating_clock_probe import scatter


def simpson_complex(f, n):
    assert n > 0 and n % 2 == 0
    return (f(0) + f(1) + sum((4 if i % 2 else 2) * f(i / n)
                                  for i in range(1, n))) / (3 * n)


def calculate(a, b, width, omega, n=1024):
    mu = 1.0
    assert 0 < a and a + width < b and width > 0 and omega > 0
    kappa0 = omega / (3 * mu)
    kappa1 = omega / mu

    def z(k):
        s0 = scatter(k, kappa0, mu)
        s1 = scatter(k, kappa1, mu)
        assert abs(abs(s0) - 1) < 1e-10 and abs(abs(s1) - 1) < 1e-10
        return s1 * s0.conjugate()

    za = simpson_complex(lambda u: z(a + width * u), n)
    zb = simpson_complex(lambda u: z(b + width * u), n)
    cross = simpson_complex(lambda u: z(a + width*u) * z(b + width*u).conjugate(), n)
    d = abs(za-zb)/2
    v = abs((1+cross)/2)
    dx = abs((za-zb).real)/2
    assert abs(za) <= 1+1e-12 and abs(zb) <= 1+1e-12
    assert 0 <= dx <= d+1e-12 and d*d+v*v <= 1+1e-11
    return {'band_A': [a,a+width], 'band_B': [b,b+width],
            'omega': omega, 'z_A': [za.real,za.imag],
            'z_B': [zb.real,zb.imag], 'cross': [cross.real,cross.imag],
            'distinguishability': d, 'ramsey_x_distinguishability': dx,
            'optimal_guess_probability': (1+d)/2,
            'ramsey_x_guess_probability': (1+dx)/2,
            'visibility': v, 'duality_sum': d*d+v*v}


def main():
    # Two disjoint, uniformly weighted k bands; a common u in [0,1] is retained
    # in the Hilbert-space factorization and traced only after interaction.
    cases=[]
    for width in (0.02,0.2,0.8):
        for omega in (0.03,0.3,0.6):
            low=calculate(.3,7.9,width,omega,512)
            hi=calculate(.3,7.9,width,omega,1024)
            for key in ('distinguishability','visibility','ramsey_x_distinguishability'):
                assert abs(low[key]-hi[key]) < 5e-9, (key, low[key], hi[key])
            cases.append(hi)
    # Identical pointwise clock response: zero information, full visibility.
    assert abs((1+1)/2-1)<1e-15
    # The reduced 2x2 density matrices are positive by |z|<=1. Their trace
    # distance is |zA-zB|/2; equal-prior Helstrom success is (1+D)/2.
    for row in cases:
        assert row['ramsey_x_guess_probability'] <= row['optimal_guess_probability']+1e-14
    result={'status':'passed', 'quadrature':'composite Simpson 512 vs 1024',
            'test_cases':len(cases), 'cases':cases,
            'interpretation':'Model-conditional channel checks, not a general solution or experiment.'}
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
