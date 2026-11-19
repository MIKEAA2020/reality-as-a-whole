#!/usr/bin/env python3
"""Exact moment checks for free-particle uncertainties in the Vedral paper.

This tests two admissible Gaussian moment triples, not the paper's cloud
chamber or any interpretation of quantum mechanics. Set hbar = m = 1.
"""
from fractions import Fraction as F
from pathlib import Path
import json

hbar = mass = F(1)
def spread_squared(var_x, var_p, cov_xp, t):
    return var_x + 2*t*cov_xp/mass + t*t*var_p/(mass*mass)
def physical(var_x, var_p, cov_xp):
    # Robertson-Schrodinger condition; equality gives a pure Gaussian.
    return var_x > 0 and var_p > 0 and var_x*var_p-cov_xp**2 >= hbar**2/4

# Real minimum-uncertainty Gaussian, time 2.
a = (F(1), F(1,4), F(0)); t = F(2)
assert physical(*a)
var_t = spread_squared(*a,t)
claimed_bound_sq = (hbar*t/(mass))**2/a[0]
correct_bound_sq = claimed_bound_sq/4
assert var_t == 2 and claimed_bound_sq == 4 and correct_bound_sq == 1
assert var_t < claimed_bound_sq and var_t >= correct_bound_sq

# A squeezed Gaussian can initially contract; covariance is nonzero.
b = (F(1), F(1,2), F(-1,2)); t_contract = F(1)
assert physical(*b)
var_contract = spread_squared(*b,t_contract)
assert var_contract == F(1,2) and var_contract < b[0]
assert var_contract >= (hbar*t_contract/(2*mass))**2 / b[0]

result = {
 'status':'passed',
 'units':'hbar = m = 1',
 'interpretation':'standard deviations with [x,p]=i hbar, free Heisenberg x(t)=x(0)+p(0)t/m',
 'first_case': {'initial_var_x':'1','initial_var_p':'1/4','initial_symmetrized_xp_covariance':'0','t':'2','var_x_t':str(var_t),'paper_eq_3_claimed_lower_bound_squared':str(claimed_bound_sq),'standard_lower_bound_squared':str(correct_bound_sq),'paper_bound_violated':True},
 'second_case': {'initial_var_x':'1','initial_var_p':'1/2','initial_symmetrized_xp_covariance':'-1/2','t':'1','var_x_t':str(var_contract),'initial_contraction':True},
 'scope':'standard exact uncertainty/moment identities; admissible Gaussian examples; not a cloud-chamber calculation, full proof audit, or consciousness test'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
