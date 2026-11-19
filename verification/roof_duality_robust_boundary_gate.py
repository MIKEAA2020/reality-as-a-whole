#!/usr/bin/env python3
"""Exhaustive robustness check on Rother et al.'s three-bit energy example.

This enumerates a stated finite objective and an assumed uncertainty box; it
is not a QPBO implementation, a proof of their QPBO-stability claim, or a
physical/experiential model. All computations are exact rational arithmetic.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

states = list(product((0, 1), repeat=3))
nominal = (F(3), F(3), F(2), F(1))

def features(s):
    x, y, z = s
    return (abs(x-y), abs(y-z), x*y, (1-x)*(1-y))

def energy(s, params):
    return sum(a*b for a, b in zip(params, features(s)))

def minima(params):
    values = {s: energy(s, params) for s in states}
    best = min(values.values())
    return best, [s for s in states if values[s] == best]

origin, trap = (0, 0, 0), (1, 1, 1)
best, optima = minima(nominal)
assert (best, optima) == (F(1), [origin])
assert energy(trap, nominal) == 2
neighbors = [s for s in states if sum(a != b for a, b in zip(s, trap)) == 1]
assert all(energy(s, nominal) > energy(trap, nominal) for s in neighbors)

# Allow each of the four coefficients to vary independently by 1/4.
# Each rival's worst-case difference is exact because energy is linear in
# the uncertain coefficients and each coordinate ranges independently.
radius = (F(1,4),) * 4
f0 = features(origin)
rival_margins = {}
for s in states:
    if s == origin:
        continue
    d = tuple(a-b for a,b in zip(features(s), f0))
    nominal_gap = energy(s, nominal) - best
    worst = nominal_gap - sum(r*abs(v) for r,v in zip(radius,d))
    rival_margins[''.join(map(str,s))] = worst
assert min(rival_margins.values()) == F(1,2)
assert all(gap > 0 for gap in rival_margins.values())
# Independently enumerate all 16 box corners as a sanity check.
for signs in product((-1, 1), repeat=4):
    params = tuple(v + r*s for v,r,s in zip(nominal,radius,signs))
    assert minima(params)[1] == [origin]

# At radius 1/2 of the last two coefficients, the competitor 111 ties;
# at 3/4 it wins. The first two coefficients are held at nominal here.
tie = (F(3), F(3), F(3,2), F(3,2))
reverse = (F(3), F(3), F(5,4), F(7,4))
assert set(minima(tie)[1]) == {origin, trap}
assert minima(reverse)[1] == [trap]

out = {'status':'passed', 'scope':'finite 3-bit example; not QPBO replay or subject assay',
       'published_energy':'3|x-y| + 3|y-z| + 2xy + (1-x)(1-y)',
       'nominal_global_minimum': '000', 'nominal_minimum_energy': str(best),
       'nominal_single_flip_local_minimum': '111',
       'nominal_single_flip_neighbor_energies': {''.join(map(str,s)):str(energy(s,nominal)) for s in neighbors},
       'uncertainty_model':'independent absolute parameter variation at most 1/4 on each of the four coefficients',
       'worst_case_gap_to_each_rival': {k:str(v) for k,v in rival_margins.items()},
       'minimum_worst_case_gap': str(min(rival_margins.values())),
       'all_16_box_corners_checked': True,
       'radius_one_half_specific_perturbation_optima':['000','111'],
       'radius_three_quarters_specific_perturbation_optimum':'111',
       'limitations':'Parameter uncertainty stipulated, not estimated; strict robust optimum only for this finite objective and box. Local minimum check is not a test of QPBOI stability.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
