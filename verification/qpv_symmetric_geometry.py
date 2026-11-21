#!/usr/bin/env python3
"""Symmetric stationary-prover geometry; not the authors' experiment or proof."""
import json
import math
from fractions import Fraction as F
from pathlib import Path


def validate(a, radius):
    if a <= 0 or radius <= a:
        raise ValueError('require a > 0 and R > a for nondegenerate spatial regions')


def geometry(a, radius):
    """Return exact lengths and volume/pi, float projected areas; a and R rational."""
    a, radius = F(a), F(radius)
    validate(a, radius)
    h = radius - a
    minor2 = radius**2 - a**2
    quantum_length = 2*h
    classical_length = 2*radius
    quantum_volume_over_pi = F(2, 3)*(2*radius+a)*h**2
    classical_volume_over_pi = F(4, 3)*radius*minor2
    af, rf = float(a), float(radius)
    minor = math.sqrt(float(minor2))
    # 2D projections of solids: intersection of discs and ellipse respectively.
    quantum_area = 2*rf**2*math.acos(af/rf) - 2*af*minor
    classical_area = math.pi*rf*minor
    return {'quantum_length': quantum_length, 'classical_length': classical_length,
            'length_ratio': classical_length/quantum_length,
            'quantum_volume_over_pi': quantum_volume_over_pi,
            'classical_volume_over_pi': classical_volume_over_pi,
            'volume_ratio': classical_volume_over_pi/quantum_volume_over_pi,
            'quantum_projected_area': quantum_area, 'classical_projected_area': classical_area,
            'area_ratio': classical_area/quantum_area}


def membership(a, radius, x, y, z):
    """Exact set definitions from symmetric specialization of article Methods."""
    a, radius, x, y, z = map(F, (a, radius, x, y, z))
    validate(a, radius)
    rho2 = y*y + z*z
    sphere_a = (x+a)**2 + rho2 <= radius**2
    sphere_b = (x-a)**2 + rho2 <= radius**2
    ellipsoid = x*x/radius**2 + rho2/(radius**2-a**2) <= 1
    # The two ellipsoids of the general formula coincide for this symmetry.
    quantum = sphere_a and sphere_b and ellipsoid
    classical = (sphere_a and ellipsoid) or (sphere_b and ellipsoid)
    return quantum, classical, ellipsoid


def simpson_quadratic(f, lo, hi):
    """Exact one-panel Simpson integration, independent of closed volume formula."""
    return (hi-lo)*(f(lo) + 4*f((lo+hi)/2) + f(hi))/6


def run():
    a, radius = F(100), F(110)
    g = geometry(a, radius)
    b2 = radius*radius-a*a
    # Radial-square profiles; multiply by pi and integrate symmetrically.
    ell_integral = 2*simpson_quadratic(lambda x: b2*(1-x*x/radius**2), F(0), radius)
    lens_integral = 2*simpson_quadratic(lambda x: radius**2-(x+a)**2, F(0), radius-a)
    assert ell_integral == g['classical_volume_over_pi']
    assert lens_integral == g['quantum_volume_over_pi']
    assert g['length_ratio'] == 11 and g['volume_ratio'] == F(231,16)
    # Exact containment proof by squared profiles: in 0 <= x <= R,
    # near-sphere radial bound minus ellipse bound = 2ax - a²x²/R² >= 0.
    # Sample on- and off-axis set membership for extra regression coverage.
    checked = 0
    for x in range(-120, 121, 5):
        for y in range(-50, 51, 5):
            for z in (-40, -20, 0, 20, 40):
                q, c, e = membership(a, radius, x, y, z)
                assert c == e
                if q:
                    assert c
                checked += 1
    assert membership(a, radius, 0, 0, 0) == (True, True, True)
    assert membership(a, radius, -100, 0, 0) == (False, True, True)
    assert membership(a, radius, 0, 46, 0) == (False, False, False)
    assert membership(a, radius, 0, 40, 0) == (True, True, True)
    for k in (F(1, 2), F(2), F(17, 3)):
        scaled = geometry(a*k, radius*k)
        assert scaled['length_ratio'] == g['length_ratio']
        assert scaled['volume_ratio'] == g['volume_ratio']
        assert scaled['classical_volume_over_pi'] == k**3*g['classical_volume_over_pi']
        assert math.isclose(scaled['area_ratio'], g['area_ratio'], rel_tol=1e-12)
    for a0, r0 in ((0, 2), (1, 1), (2, 1), (-1, 3)):
        try:
            geometry(a0, r0)
        except ValueError:
            pass
        else:
            raise AssertionError('accepted degenerate geometry')
    out = {'scope': 'Synthetic simultaneous equal-deadline stationary-prover spatial geometry; not experimental or security reproduction.',
           'a_m': str(a), 'R_m': str(radius),
           'quantum_length_m': str(g['quantum_length']), 'classical_length_m': str(g['classical_length']),
           'same_latency_length_ratio': str(g['length_ratio']),
           'quantum_volume_m3_over_pi': str(g['quantum_volume_over_pi']),
           'classical_volume_m3_over_pi': str(g['classical_volume_over_pi']),
           'same_latency_volume_ratio': str(g['volume_ratio']),
           'quantum_projected_area_m2': g['quantum_projected_area'],
           'classical_projected_area_m2': g['classical_projected_area'],
           'same_latency_projected_area_ratio': g['area_ratio'],
           'exact_grid_points_checked': checked,
           'integrals_agree_with_closed_forms': True}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    run()
