#!/usr/bin/env python3
"""Spatial set calculations for reported QPV timings; not the experiment or security proof."""
import itertools
import json
import math
from pathlib import Path

from scipy.integrate import quad

# Exact defined vacuum light speed expressed in metres/nanosecond.
C = 0.299792458
# Rounded central values from arXiv v2 supplement IV, tables 1 and 2.
CENTRAL = {'distance_m': 195.1, 'sA_ns': 1291.0, 'sB_ns': 1429.1,
           'rA_ns': 2340.3, 'rB_ns': 2207.7}


def poly_eval(p, x):
    return (p[0]*x+p[1])*x+p[2]


def roots(p):
    a, b, c = p
    if abs(a) < 1e-14:
        return [] if abs(b) < 1e-14 else [-c/b]
    discr = b*b-4*a*c
    if discr < 0:
        return []
    root = math.sqrt(discr)
    # Stable formula for potentially unequal roots.
    q = -0.5*(b + math.copysign(root, b))
    if q == 0:
        return [-b/(2*a)]
    return [q/a, c/q]


def from_timings(t):
    L = t['distance_m']
    if L <= 0 or t['rA_ns'] <= t['sA_ns'] or t['rB_ns'] <= t['sB_ns']:
        raise ValueError('invalid station separation or round-trip timing')
    # Article Δτ3 = rA - sB; Δτ4 = rB - sA. Their lengths
    # are ellipsoid major axes, not radii.
    ra = C*(t['rA_ns']-t['sA_ns'])/2
    rb = C*(t['rB_ns']-t['sB_ns'])/2
    ma = C*(t['rA_ns']-t['sB_ns'])
    mb = C*(t['rB_ns']-t['sA_ns'])
    return (L, ra, rb, ma, mb)


def interval_intersection(*intervals):
    lo = max(i[0] for i in intervals)
    hi = min(i[1] for i in intervals)
    return (lo, hi) if hi > lo else None


def interval_union(intervals):
    """Sorted union without double-counting; empty and degenerate inputs ignored."""
    valid = sorted(i for i in intervals if i is not None and i[1] > i[0])
    merged = []
    for lo, hi in valid:
        if merged and lo <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
        else:
            merged.append((lo, hi))
    return merged


def shape(L, ra, rb, ma, mb):
    if L <= 0 or ra <= 0 or rb <= 0 or ma <= L or mb <= L:
        raise ValueError('require positive sphere radii and nondegenerate ellipsoids')
    a = L/2
    # x=0 at midpoint; each polynomial is permitted radial distance squared.
    sa = (-1., -2*a, ra*ra-a*a)
    sb = (-1., 2*a, rb*rb-a*a)
    ea_b2 = (ma/2)**2-a*a
    eb_b2 = (mb/2)**2-a*a
    ea = (-ea_b2/(ma/2)**2, 0., ea_b2)
    eb = (-eb_b2/(mb/2)**2, 0., eb_b2)
    return sa, sb, ea, eb


def profiles(polys, x):
    sa, sb, ea, eb = (poly_eval(p, x) for p in polys)
    # All transverse sections are concentric disks. For a union their
    # maximum radius, not sum of disk areas, is the correct cross section.
    quantum = max(0., min(sa, sb, ea, eb))
    classical = max(0., min(sa, ea), min(sb, eb))
    return quantum, classical


def evaluate(L, ra, rb, ma, mb):
    ps = shape(L, ra, rb, ma, mb)
    a = L/2
    ia, ib = (-a-ra, -a+ra), (a-rb, a+rb)
    iea, ieb = (-ma/2, ma/2), (-mb/2, mb/2)
    iq = interval_intersection(ia, ib, iea, ieb)
    parts = [interval_intersection(ia, iea), interval_intersection(ib, ieb)]
    ic = interval_union(parts)
    if iq is None:
        raise ValueError('empty quantum axial projection')
    qlen = iq[1]-iq[0]
    clen = sum(hi-lo for lo, hi in ic)
    # Include all roots and pairwise profile intersections to make each
    # integration interval a single active quadratic (or the zero function).
    limit = max(ma, mb)/2
    breaks = [-limit, limit]
    for p in ps:
        breaks.extend(x for x in roots(p) if -limit < x < limit)
    for p, q in itertools.combinations(ps, 2):
        breaks.extend(x for x in roots(tuple(p[i]-q[i] for i in range(3))) if -limit < x < limit)
    breaks = sorted(set(breaks))
    totals = [[0., 0.], [0., 0.]]  # quantum/classical x area/volume
    errors = [0., 0.]
    for lo, hi in zip(breaks, breaks[1:]):
        if hi-lo < 1e-10:
            continue
        mid = (lo+hi)/2
        for k in (0, 1):
            # Simpson integrates the chosen quadratic exactly on this interval.
            p0, pm, p1 = (profiles(ps, x)[k] for x in (lo, mid, hi))
            totals[k][1] += math.pi*(hi-lo)*(p0+4*pm+p1)/6
            if pm > 0:
                value, err = quad(lambda x: 2*math.sqrt(max(0., profiles(ps, x)[k])),
                                  lo, hi, epsabs=1e-8, epsrel=1e-11, limit=100)
                totals[k][0] += value
                errors[k] += err
    qa, qv = totals[0]
    ca, cv = totals[1]
    if min(qa, qv, ca, cv) <= 0:
        raise ValueError('empty or degenerate spatial region')
    naive_sum = sum(part[1]-part[0] for part in parts if part is not None)
    return {'quantum_axis_interval_m': list(iq), 'classical_axis_intervals_m': [list(i) for i in ic],
            'classical_component_axis_intervals_m': [list(i) if i is not None else None for i in parts],
            'classical_naive_sum_of_component_lengths_m': naive_sum,
            'quantum_length_m': qlen, 'classical_length_m': clen,
            'quantum_area_m2': qa, 'classical_area_m2': ca,
            'quantum_volume_m3': qv, 'classical_volume_m3': cv,
            'ratios': {'length_same_latency': clen/qlen, 'area_same_latency': ca/qa,
                       'volume_same_latency': cv/qv, 'length_ideal_classical': L/qlen,
                       'length_naive_component_sum_diagnostic': naive_sum/qlen,
                       'length_ellipsoid_upper_bound': max(ma, mb)/qlen},
            'area_quad_error_estimate_m2': errors}


def main():
    L, ra, rb, ma, mb = from_timings(CENTRAL)
    central = evaluate(L, ra, rb, ma, mb)
    # Each input was printed to 0.1 in its units. Corner perturbations are
    # an illustrative rounding stress test, not a measurement uncertainty.
    vals = {key: [] for key in central['ratios']}
    for signs in itertools.product((-1, 1), repeat=5):
        test = {name: value+sign*.05 for (name, value), sign in zip(CENTRAL.items(), signs)}
        result = evaluate(*from_timings(test))
        for key, value in result['ratios'].items():
            vals[key].append(value)
    # Conservative interval-arithmetic bound for all values within ±0.05 of
    # each rounded input. Treat derived quantities independently; this can
    # only widen the bound and does not model the measurement uncertainties.
    amin, amax = (L-.05)/2, (L+.05)/2
    ramin, ramax = ra-C*.1/2, ra+C*.1/2
    rbmin, rbmax = rb-C*.1/2, rb+C*.1/2
    mamin, mamax = ma-C*.1, ma+C*.1
    mbmin, mbmax = mb-C*.1, mb+C*.1
    conservative_q_low = max(-amin-ramin, amax-rbmin, -mamin/2, -mbmin/2)
    conservative_q_high = min(-amax+ramin, amin+rbmin, mamin/2, mbmin/2)
    q_min = conservative_q_high-conservative_q_low
    if q_min <= 0:
        raise ValueError('rounding perturbation bound is degenerate')
    all_rounding_upper = max(mamax, mbmax)/q_min
    result = {'scope': 'Spatial geometry from rounded reported timing inputs, not replay of experimental records, uncertainty model, or security proof.',
              'inputs': CENTRAL, 'c_m_per_ns': C,
              'derived_shapes_m': {'sphere_A_radius': ra, 'sphere_B_radius': rb,
                                   'ellipsoid_3_major_axis_rA_minus_sB': ma,
                                   'ellipsoid_4_major_axis_rB_minus_sA': mb},
              'central': central,
              'cross_check_from_separately_rounded_preprint_table3': {
                  'inputs_L_rA_rB_major3_major4_m': [195.1, 157.3, 116.7, 273.1, 274.8],
                  'ratios': evaluate(195.1, 157.3, 116.7, 273.1, 274.8)['ratios']},
              'rounding_corner_stress_test': {'description': '32 simultaneous ±0.05 corners for five one-decimal printed inputs; sampled extrema are not confidence intervals or proven global extrema.',
                  'sampled_min_max': {key: [min(v), max(v)] for key, v in vals.items()},
                  'conservative_all_inputs_1d_quantum_length_lower_m': q_min,
                  'conservative_all_inputs_1d_ratio_upper_bound': all_rounding_upper,
                  'bound_scope': 'All inputs within 0.05 printed units; interval arithmetic with independent bounds, not measurement uncertainty.'}}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
