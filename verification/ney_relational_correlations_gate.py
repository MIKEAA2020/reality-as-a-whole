#!/usr/bin/env python3
"""Exact qubit bookkeeping for Ney's position-marginal example and controls.

Not a derivation of quantum mechanics, a measurement solution, or a subject test.
"""
from fractions import Fraction as F
import json
from pathlib import Path

Z0, O, H = F(0), F(1), F(1, 2)
I = [[O,Z0],[Z0,O]]
X = [[Z0,O],[O,Z0]]
Z = [[O,Z0],[Z0,-O]]

def tensor(a,b):
    return [[a[i//len(b)][j//len(b[0])] * b[i%len(b)][j%len(b[0])]
             for j in range(len(a[0])*len(b[0]))] for i in range(len(a)*len(b))]

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

def tr(a):
    return sum(a[i][i] for i in range(len(a)))

def expect(rho, op):
    return tr(mm(rho,op))

def partial_a(rho):
    return [[sum(rho[2*i+k][2*j+k] for k in range(2)) for j in range(2)] for i in range(2)]

def partial_b(rho):
    return [[sum(rho[2*k+i][2*k+j] for k in range(2)) for j in range(2)] for i in range(2)]

def show(x):
    if isinstance(x,list): return [show(v) for v in x]
    return str(x)

# rho_plus/minus for (|01> +/- |10>)/sqrt(2), rho_product for |++>.
def bell(sign):
    r = [[Z0 for _ in range(4)] for _ in range(4)]
    r[1][1]=r[2][2]=H
    r[1][2]=r[2][1]=sign*H
    return r

plus, minus = bell(1), bell(-1)
prod = [[F(1,4) for _ in range(4)] for _ in range(4)]
states = {'ney_written_plus':plus, 'phase_minus':minus, 'product':prod}
for rho in states.values():
    assert tr(rho) == 1 and mm(rho,rho) == rho
    assert partial_a(rho) == partial_b(rho)
assert partial_a(plus) == partial_a(minus) == [[H,Z0],[Z0,H]]
assert partial_a(prod) == [[H,H],[H,H]]
assert [plus[i][i] for i in range(4)] == [minus[i][i] for i in range(4)] == [Z0,H,H,Z0]
assert [prod[i][i] for i in range(4)] == [F(1,4)]*4
assert [partial_a(r)[i][i] for i in range(2) for r in (plus,minus,prod)] == [H]*6
assert [expect(r,tensor(Z,Z)) for r in (plus,minus,prod)] == [-O,-O,Z0]
assert [expect(r,tensor(X,X)) for r in (plus,minus,prod)] == [O,-O,O]
assert [expect(r,tensor(X,I)) for r in (plus,minus,prod)] == [Z0,Z0,O]
# Active phase operation Z on B changes + to -, with unchanged A local state.
u = tensor(I,Z)
assert mm(mm(u,plus),u) == minus
assert partial_a(mm(mm(u,plus),u)) == partial_a(plus)
# In a passive redescription, transform BOTH state and observable.
xx = tensor(X,X)
assert expect(mm(mm(u,plus),u), mm(mm(u,xx),u)) == expect(plus,xx)

out={'scope':'Exact arithmetic in two idealized two-level subsystems; no phenomenal or QFT inference.',
     'states':{name:{'position_joint_probabilities_00_01_10_11':show([r[i][i] for i in range(4)]),
                     'marginal_A':show(partial_a(r)), 'marginal_B':show(partial_b(r)),
                     'X_A':str(expect(r,tensor(X,I))), 'ZZ':str(expect(r,tensor(Z,Z))),
                     'XX':str(expect(r,tensor(X,X)))} for name,r in states.items()},
     'active_local_phase_changes_joint_state_but_not_A_marginal':True,
     'passive_transport_of_state_and_observable_preserves_prediction':True,
     'assertions':'passed'}
p = Path(__file__).with_suffix('.json'); p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
