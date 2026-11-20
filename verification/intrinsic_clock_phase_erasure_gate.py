#!/usr/bin/env python3
"""Finite periodic clock: conditional change, constraint observable, lost phase.

All entries are dyadic rationals and Gaussian dyadics exactly represented by
Python complex numbers; no square-root amplitudes or transcendental phases are
used. A finite periodic example, not a continuous-clock theorem.
"""
import json
from pathlib import Path

I2 = [[1,0],[0,1]]; X = [[0,1],[1,0]]
def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def kron(a,b):
    return [[a[i//len(b)][j//len(b[0])]*b[i%len(b)][j%len(b[0])] for j in range(len(a[0])*len(b[0]))] for i in range(len(a)*len(b))]
def add(a,b): return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def scale(a,s): return [[s*x for x in row] for row in a]
def tr(a): return sum(a[i][i] for i in range(len(a)))
def diag(a): return [[a[i] if i == j else 0 for j in range(len(a))] for i in range(len(a))]
def partial_c(a): return [[sum(a[2*k+i][2*k+j] for k in range(2)) for j in range(2)] for i in range(2)]
def rho(sign):
    m=[[0]*4 for _ in range(4)]
    m[0][0]=m[3][3]=.5; m[0][3]=m[3][0]=sign*.5
    return m

def povm(phase): # 1/2 |t><t|; |t>=(|0>+phase|1>)/sqrt(2)
    return [[.25,.25*phase.conjugate()],[.25*phase,.25]]
def project_rel(phase):
    m=[[0]*4 for _ in range(4)]
    m[0][3]=phase; m[3][0]=phase.conjugate()
    return m

C=diag([0,1,-1,0]); P=diag([1,0,0,1]); phases=[1+0j,1j,-1+0j,-1j]
effects=[povm(p) for p in phases]
sum_e=[[sum(e[i][j] for e in effects) for j in range(2)] for i in range(2)]
assert sum_e==I2
assert mm(C,P)==mm(P,C)
results={}
for sign in (1,-1):
    r=rho(sign)
    assert tr(r)==1 and mm(r,r)==r and mm(C,r)==mm(r,C)
    assert partial_c(r)==[[.5,0],[0,.5]]
    scores=[]; weights=[]; rel_scores=[]
    for phase,e in zip(phases,effects):
        pr=tr(mm(kron(e,I2),r))
        assert pr==.25
        # Partial trace permits calculating unnormalised conditional state
        # directly from (E tensor I) rho, since clock indices are traced.
        cond=scale(partial_c(mm(kron(e,I2),r)),1/pr)
        assert tr(cond)==1 and mm(cond,cond)==cond
        x=tr(mm(cond,X)).real
        rel=project_rel(phase)
        assert mm(C,rel)==mm(rel,C)
        val=tr(mm(r,rel)).real
        assert val==x
        assert x==sign*phase.real
        scores.append(x); weights.append(pr.real); rel_scores.append(val)
    results['plus' if sign==1 else 'minus']={'clock_outcome_probabilities':weights,'conditional_X':scores,'constraint_commuting_relative_X':rel_scores}
# Conditional normalized kets, scaled by sqrt(2): [1, sign*phase.conjugate()].
# Their arithmetic mean is exactly [1,0] for either sign.
for sign in (1,-1):
    avg=[sum(v)/4 for v in zip(*[[1,sign*p.conjugate()] for p in phases])]
    assert avg==[1,0]
# The two global states are orthogonal and distinguished by a physical
# constraint-commuting relational operator, despite identical system reductions.
assert mm(rho(1),rho(-1))==[[0]*4 for _ in range(4)]
assert tr(mm(rho(1),project_rel(1)))==1
assert tr(mm(rho(-1),project_rel(1)))==-1
assert partial_c(rho(1))==partial_c(rho(-1))
# Original clock effects themselves are not generally Dirac observables.
assert mm(C,kron(effects[0],I2))!=mm(kron(effects[0],I2),C)
result={'scope':'Four-outcome periodic qubit clock; no claim about continuum clock or subjective time.',
        'clock_phases':['0','pi/2','pi','3pi/2'], 'states':results,
        'system_reductions_both':'I/2','global_states_orthogonal':True,
        'coherent_average_of_conditional_kets':'|0>/sqrt(2) for each state',
        'relative_X_at_zero_distinguishes_states':[1,-1],
        'clock_effect_itself_does_not_commute_with_constraint':True,
        'arithmetic':'exact for displayed dyadic values'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
