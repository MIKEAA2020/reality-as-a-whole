#!/usr/bin/env python3
"""Exact finite entanglement-swapping and selection checks, not experimental data.

All density-matrix calculations use rational arithmetic; no third-party packages.
The entanglement and CHSH thresholds themselves are established results, not
claimed as new. See the accompanying report for assumptions and reading scope.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

Z = F(0)
O = F(1)
I = [[O, Z], [Z, O]]
X = [[Z, O], [O, Z]]
PAULI_Z = [[O, Z], [Z, -O]]
BELL = {
    'phi_plus': (1, 0, 0, 1),
    'phi_minus': (1, 0, 0, -1),
    'psi_plus': (0, 1, 1, 0),
    'psi_minus': (0, 1, -1, 0),
}


def bell_density(label):
    v = BELL[label]
    return [[F(v[i]*v[j], 2) for j in range(4)] for i in range(4)]


def werner(p, label='phi_plus'):
    b = bell_density(label)
    return [[p*b[i][j] + ((1-p)/4 if i == j else Z)
             for j in range(4)] for i in range(4)]


def kron(a, b):
    return [[a[i//len(b)][j//len(b[0])] * b[i%len(b)][j%len(b[0])]
             for j in range(len(a[0])*len(b[0]))]
            for i in range(len(a)*len(b))]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def expect(rho, op):
    return sum(rho[i][j]*op[j][i] for i in range(len(rho)) for j in range(len(rho)))


def project_middle(rho, label):
    # Four-qubit order A B C D; the Bell vector on B,C is v/sqrt(2).
    v = BELL[label]
    result = [[Z for _ in range(4)] for _ in range(4)]
    for a, d, ap, dp, b, c, bp, cp in product(range(2), repeat=8):
        left = 8*a + 4*b + 2*c + d
        right = 8*ap + 4*bp + 2*cp + dp
        result[2*a+d][2*ap+dp] += F(v[2*b+c]*v[2*bp+cp], 2)*rho[left][right]
    return result


def scale(m, x):
    return [[x*t for t in row] for row in m]


def add(a, b):
    return [[x+y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def norm_str(x):
    return str(x)


out = {}
# Test asymmetric rational input qualities, including zero and perfect links.
for p, q in [(F(0), F(0)), (F(0), F(1)), (F(1), F(0)), (F(1), F(1)),
             (F(4,5), F(4,5)), (F(2,3), F(3,4)), (F(9,10), F(9,10))]:
    source = kron(werner(p), werner(q))
    post = [project_middle(source, label) for label in BELL]
    for (label, sigma) in zip(BELL, post):
        assert trace(sigma) == F(1,4)
        assert scale(sigma, 4) == werner(p*q, label)
    unconditional = [[Z]*4 for _ in range(4)]
    for sigma in post:
        unconditional = add(unconditional, sigma)
    assert unconditional == werner(F(0))
    out[f'{p}*{q}'] = {'per_herald_probability': '1/4', 'swapped_visibility': str(p*q),
                         'unconditioned_outer_state': 'I/4'}

w = F(16,25)
quantum = werner(w)
# This explicit separable mixture matches all Z-versus-any-single-qubit-axis
# data, but not XX. It is not claimed to reproduce Pan et al.'s full data.
sep_diag = [[F(1,2) if i == j and i in (0,3) else Z for j in range(4)] for i in range(4)]
separable = add(scale(sep_diag, w), scale(werner(F(0)), 1-w))
assert trace(separable) == 1
zzq = expect(quantum, kron(PAULI_Z, PAULI_Z))
zzs = expect(separable, kron(PAULI_Z, PAULI_Z))
zxq = expect(quantum, kron(PAULI_Z, X))
zxs = expect(separable, kron(PAULI_Z, X))
xxq = expect(quantum, kron(X, X))
xxs = expect(separable, kron(X, X))
assert (zzq, zzs, zxq, zxs, xxq, xxs) == (w, w, Z, Z, w, Z)
# Both local marginals vanish, so matching all correlators for Alice Z and
# any Bob Bloch vector entails matching their entire joint distribution.
for op in [kron(PAULI_Z, I), kron(I, PAULI_Z), kron(I, X)]:
    assert expect(quantum, op) == expect(separable, op) == Z
# The missing Z⊗Y coefficient is zero for both: the real-symmetric matrices
# and antisymmetric Y give zero trace without complex arithmetic.
assert quantum == [list(row) for row in zip(*quantum)]
assert separable == [list(row) for row in zip(*separable)]
assert w > F(1,3) and 2*w*w < 1  # entangled yet CHSH-local in this family

# A late central selector reads x,y and the two otherwise independent local
# outcomes. It accepts precisely the PR parity relation. This is an explicitly
# nonlocal selection operation, NOT an ordinary independent event-ready herald.
counts = {}
for x,y,a_bit,b_bit in product(range(2), repeat=4):
    a, b = 1-2*a_bit, 1-2*b_bit
    h = int((a*b) == (-1)**(x*y))
    counts[(x,y,a,b,h)] = 1
for x,y in product(range(2), repeat=2):
    rows = [(a,b,h) for (xx,yy,a,b,h) in counts if (xx,yy)==(x,y)]
    assert len(rows)==4 and sum(h for a,b,h in rows)==2
    for h in (0,1):
        selected = [(a,b) for a,b,hh in rows if hh==h]
        assert len(selected)==2
        assert sum(a for a,b in selected)==0 and sum(b for a,b in selected)==0
        corr = F(sum(a*b for a,b in selected), len(selected))
        assert corr == (1 if h else -1)*(-1)**(x*y)
    assert sum(a*b for a,b,h in rows)==0
# The selected source-bit distribution changes with settings: P(a=b|h=1)
# goes from 1 for xy=0 to 0 for xy=1, even though P(h=1|x,y)=1/2 always.
summary = {
    'scope': 'Finite rational toy models only; not experimental data, a new Bell theorem, or evidence of experience.',
    'swapping_cases': out,
    'same_fixed_basis_example': {'w':str(w), 'ZZ_both':str(zzq), 'ZX_both':str(zxq),
        'XX_entangled':str(xxq), 'XX_separable':str(xxs),
        'werner_chsh_max': '32*sqrt(2)/25', 'classification': 'entangled but no CHSH violation in this model'},
    'late_central_selection': {'herald_rate_per_setting':'1/2', 'selected_chsh':4,
        'unconditional_chsh':0, 'selected_marginals':'uniform',
        'selected_equal_outcomes_probability_xy0':1, 'selected_equal_outcomes_probability_xy1':0},
}
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
