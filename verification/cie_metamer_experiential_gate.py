#!/usr/bin/env python3
"""CIE-standard proxy factorization check; not an assay of real experiences.

Four 1931 2-degree XYZ table rows from pdbuchan/colorimetry at pinned commit
b542bec75fdc7946a380071dc1c450bf4e7d5687, file git blob
9b4e3f73b4bb412a762a6d03cb8060bfea652a6e. Fractions make all equations exact
for the rounded decimal inputs. No full external dataset is redistributed.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'verification' / 'cie_metamer_experiential_gate.json'
WAVELENGTHS = (450, 500, 550, 600)
ROWS = (
    ('0.336200000000', '0.0380000000000', '1.772110000000'),
    ('0.004900000000', '0.3230000000000', '0.272000000000'),
    ('0.433449900000', '0.9949501000000', '0.008749999000'),
    ('1.062200000000', '0.6310000000000', '0.000800000000'),
)
C = [[Q(ROWS[j][i]) for j in range(4)] for i in range(3)]

def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), Q(0))

def project(s):
    return [dot(row,s) for row in C]

# The signed maximal minors form a null vector, computed from decimal table.
v = [(-1)**j * det3([[row[k] for k in range(4) if k != j] for row in C])
     for j in range(4)]
assert any(v), 'table must have rank 3'
v = [x/max(abs(x) for x in v) for x in v]
assert project(v)==[Q(0)]*3
p = [1 + Q(4,5)*x for x in v]
m = [1 - Q(4,5)*x for x in v]
assert min(p+m)>=Q(1,5) and project(p)==project(m) and p!=m
j=max(range(4),key=lambda i:abs(v[i]))
# An ideal filter passes the wavelength j and blocks the other three.
filtered_p=[x if i==j else Q(0) for i,x in enumerate(p)]
filtered_m=[x if i==j else Q(0) for i,x in enumerate(m)]
assert project(filtered_p)!=project(filtered_m)
assert abs(p[j]-m[j])==Q(8,5)

def floats(v): return [float(x) for x in v]
result={
    'source_git_commit':'b542bec75fdc7946a380071dc1c450bf4e7d5687',
    'source_blob':'9b4e3f73b4bb412a762a6d03cb8060bfea652a6e',
    'source_sha256':'fa663e3535a7e0763a745993a1f0a192eb0275ac46ad2d1befd7626841e713c1',
    'wavelengths_nm':list(WAVELENGTHS),
    'cmf_rows_decimal_strings':[list(row) for row in ROWS],
    'normalized_null_direction':floats(v),
    'relative_band_powers_plus':floats(p),
    'relative_band_powers_minus':floats(m),
    'tristimulus_both_exact_rounded_table':floats(project(p)),
    'selected_filter_nm':WAVELENGTHS[j],
    'passed_band_power_difference_exact':'8/5',
    'filtered_tristimulus_plus':floats(project(filtered_p)),
    'filtered_tristimulus_minus':floats(project(filtered_m)),
    'scope':'Exact rational arithmetic on four rounded CIE table rows and idealized monochromatic sources and filter. Not an experiment; standard-observer predictions are not phenomenal equivalence for an actual person.'
}
OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,indent=2))
