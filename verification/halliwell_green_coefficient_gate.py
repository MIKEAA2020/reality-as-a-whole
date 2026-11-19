#!/usr/bin/env python3
"""Check a small-absorber expansion in Halliwell arXiv:0909.2597v1.

Compare the x<y coefficient of PDF eq. (5.11), equivalently HTML eq. (122),
with the following equation's printed leading term. This is not a scattering
calculation or independent validation of the paper's semiclassical analysis.
"""
import cmath, json
from pathlib import Path

rows=[]
for epsilon in (1e-2,1e-4,1e-6):
    q=cmath.sqrt(1+1j*epsilon)  # Q/p
    exact=(q-1)/(2*q)            # magnitude factor before overall minus sign
    correct=1j*epsilon/4
    printed=4j*epsilon
    rows.append({'V0_over_E':epsilon,'exact_over_correct_real':(exact/correct).real,
                 'exact_over_correct_imag':(exact/correct).imag,
                 'exact_over_printed_real':(exact/printed).real})
assert abs(rows[-1]['exact_over_correct_real']-1)<1e-8
assert abs(rows[-1]['exact_over_correct_imag'])<1e-5
assert abs(rows[-1]['exact_over_printed_real']-1/16)<1e-8
result={'status':'passed','source':'Halliwell, arXiv:0909.2597v1, PDF equations (5.11) and (5.12), HTML (122) and (123)',
        'expansion_from_preceding_equation':'(Q-p)/(2Q) = i(V0/E)/4 + O((V0/E)^2)',
        'next_equation_printed_coefficient':'4i(V0/E)',
        'scope':'checks asymptotic coefficients from source text; PDF equation image not visually checked; published article comparison and full proof audit not performed',
        'ratios':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
