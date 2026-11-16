#!/usr/bin/env python3
"""Selective-channel certificate and a same-data higher-harmonic counterexample.

Bounded classical toy models; no real channel, neural activity, or pain data.
"""
import json
import math
import random
from pathlib import Path

PI = math.pi

def circle_dist(x, y):
    return abs((x-y+PI) % (2*PI)-PI)

def infer(y0, y1, eps, lambda_max=1.0):
    r = math.sqrt(2)*eps
    norm = math.hypot(y0, y1)
    if norm <= r:
        return None
    return ((norm-r)/lambda_max, math.atan2(-y0, y1), math.asin(r/norm))

# Closed-form uniform parameter illustration: observed differences (0,-1).
eps = 0.1
low, ahat, da = infer(0.0, -1.0, eps)
d_low = max(0.0, circle_dist(3*ahat, 0) - 3*da)
certificate = 2*low*d_low*d_low/(3*PI*PI)
assert abs(certificate-0.42777667831142024) < 1e-14

# Statistical bound: 12 cell means, n iid bounded observations per cell.
B, eta, alpha = 2.0, 0.05, 0.05
n = math.ceil(8*B*B/(eta*eta)*math.log(24/alpha))
coverage_failure_bound = 24*math.exp(-n*eta*eta/(8*B*B))
assert n == 79025 and coverage_failure_bound <= alpha
assert 24*math.exp(-(n-1)*eta*eta/(8*B*B)) > alpha

# Independent seeded checks of circle/strength bounds with varying gates.
rng = random.Random(722036)
resolved = 0
max_angular_violation = 0.0
max_strength_violation = 0.0
for _ in range(15000):
    a = rng.uniform(-PI, PI)
    k = rng.uniform(.05, 2.0)
    lam = rng.uniform(.1, 1.0)
    e0 = rng.uniform(-eps, eps)
    e1 = rng.uniform(-eps, eps)
    y0 = -lam*k*math.sin(a)+e0
    y1 = lam*k*math.cos(a)+e1
    result = infer(y0,y1,eps)
    if result is None:
        continue
    resolved += 1
    klow, est, radius = result
    err = circle_dist(est,a)
    max_angular_violation = max(max_angular_violation,err-radius)
    max_strength_violation = max(max_strength_violation, klow-k)
    assert err <= radius+1e-12 and klow <= k+1e-12
assert resolved > 0

# End-to-end check of the lower bound at random true triangles and states.
positive_triangles = 0
for _ in range(10000):
    entries = []
    for j in range(3):
        a = rng.uniform(-PI, PI)
        k = rng.uniform(.1, 2.0)
        lam = rng.uniform(.2, 1.0)
        y0 = -lam*k*math.sin(a) + rng.uniform(-eps, eps)
        y1 = lam*k*math.cos(a) + rng.uniform(-eps, eps)
        entries.append((a, k, infer(y0, y1, eps)))
    if any(item[2] is None for item in entries):
        continue
    kl = min(item[2][0] for item in entries)
    angle_hat = sum(item[2][1] for item in entries)
    dlow = max(0.0, circle_dist(angle_hat, 0) - sum(item[2][2] for item in entries))
    cert = 2*kl*dlow*dlow/(3*PI*PI)
    if cert > 0:
        positive_triangles += 1
    phi = [rng.uniform(-PI, PI) for _ in range(3)]
    cost = sum(entries[j][1]*(1-math.cos(phi[j]-phi[(j+1)%3]-entries[j][0]))
               for j in range(3))
    assert cost + 1e-12 >= cert
assert positive_triangles > 0

# An anti-phase first-harmonic channel and a zero-preference third-harmonic
# channel give exactly the same forces at 0 and pi/2, not at pi/4.
def anti_force(x): return -math.sin(x)
def third_force(x): return math.sin(3*x)
def anti_cost(x): return 1+math.cos(x)
def third_cost(x): return (1-math.cos(3*x))/3
for x in (0,PI/2):
    assert abs(anti_force(x)-third_force(x)) < 1e-14
assert abs(anti_force(PI/4)-third_force(PI/4)+math.sqrt(2)) < 1e-14
# Antiphase triangle minimum is 3/2 (known analytic result); 3rd-harmonic
# triangle reaches zero at all equal phases since every term is nonnegative.
assert abs(3*third_cost(0)) < 1e-14
assert abs(3*anti_cost(2*PI/3)-1.5) < 1e-14

report = {
  'status': 'passed',
  'scope': 'conditional phase-potential toy, not neural data or an experiential assay',
  'two_point_estimate_each_edge': [0, -1],
  'per_quadrature_total_error_bound': eps,
  'error_vector_radius': math.sqrt(2)*eps,
  'lower_channel_weight': low,
  'offset_error_bound_radians': da,
  'cycle_distance_lower_radians': d_low,
  'absolute_frustration_lower_bound': certificate,
  'qualification': 'First-harmonic law, reciprocal potential, selective same-fraction gate and bias bounds must independently hold.',
  'hoeffding_example': {'cells': 12, 'iid_trials_per_cell': n, 'total_trials': 12*n,
     'observation_range': [-B, B], 'sampling_difference_error': eta,
     'systematic_difference_error_assumed': .05, 'union_bound_failure_probability': coverage_failure_bound},
  'seeded_parameter_tests': 15000, 'resolved_parameter_tests': resolved,
  'seeded_triangle_trials': 10000, 'positive_certificates_among_evaluable_triangles': positive_triangles,
  'max_positive_angle_bound_violation': max_angular_violation,
  'max_positive_strength_bound_violation': max_strength_violation,
  'alias': {'two_point_forces_equal': True, 'first_harmonic_triangle_minimum': 1.5,
            'third_harmonic_triangle_minimum': 0,
            'force_difference_at_pi_over_4': anti_force(PI/4)-third_force(PI/4)}
}
path = Path(__file__).resolve().parent/'selective_phase_channel_certificate.json'
path.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
