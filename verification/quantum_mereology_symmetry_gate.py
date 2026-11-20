#!/usr/bin/env python3
"""Exact arithmetic for a state-preserving factorization ambiguity.

Only finite matrix identities are checked. No subject, observation or spacetime
emergence is inferred. See QUANTUM_MEREOLOGY_STATE_STABILIZER_GATE.md.
"""
from fractions import Fraction as F
import json
from pathlib import Path

z, o = F(0), F(1)
I = [[o,z],[z,o]]; X = [[z,o],[o,z]]; Z = [[o,z],[z,-o]]
def tensor(a,b):
    return [[a[i//len(b)][j//len(b[0])]*b[i%len(b)][j%len(b[0])]
            for j in range(len(a[0])*len(b[0]))] for i in range(len(a)*len(b))]
def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
            for j in range(len(b[0]))] for i in range(len(a))]
def add(*terms):
    return [[sum(term[i][j] for term in terms) for j in range(len(terms[0][0]))]
            for i in range(len(terms[0]))]
def scale(c,a): return [[c*x for x in row] for row in a]
def diag(vals): return [[F(vals[i]) if i == j else z for j in range(len(vals))] for i in range(len(vals))]
def trace(a): return sum(a[i][i] for i in range(len(a)))
def conj(u,a): return mul(mul(u,a),u) # real symmetric involution here

ii, xi, zi, ix, iz = (tensor(I,I), tensor(X,I), tensor(Z,I), tensor(I,X), tensor(I,Z))
xz, zx, zz = tensor(X,Z), tensor(Z,X), tensor(Z,Z)
H=diag([0,1,2,4]); U=diag([1,1,1,-1]); rho=diag([1,0,0,0])
assert len(set(H[i][i] for i in range(4))) == 4
assert mul(U,U) == ii and mul(U,H) == mul(H,U) and conj(U,rho) == rho
assert H == add(scale(F(7,4),ii),scale(F(-5,4),zi),scale(F(-3,4),iz),scale(F(1,4),zz))
assert conj(U,xi)==xz and conj(U,ix)==zx and conj(U,zi)==zi and conj(U,iz)==iz
# A tensor-identity operator necessarily commutes with I tensor X and I tensor Z;
# an identity-tensor-B operator necessarily commutes with X tensor I and Z tensor I.
assert mul(xz,ix) != mul(ix,xz)  # transformed A X not in original A
assert mul(xz,zi) != mul(zi,xz)  # nor in original B, even allowing swaps
assert mul(xi,ix) == mul(ix,xi) and mul(xi,iz) == mul(iz,xi)
assert mul(xz,zx) == mul(zx,xz)  # transformed A and B local X's commute
P0, P1 = [[o,z],[z,z]], [[z,z],[z,o]]
plus = [[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
# Candidate pointer states are Pj tensor |+><+| and their U-images.
for p in (P0,P1):
    state=tensor(p,plus); projector=tensor(p,I)
    assert trace(state)==1 and mul(state,state)==state
    assert mul(projector,state)==state and mul(projector,H)==mul(H,projector)
    assert mul(conj(U,projector),conj(U,state)) == conj(U,state)
    assert mul(conj(U,projector),H)==mul(H,conj(U,projector))
# With an independently marked X_A and a separately specified |++> preparation,
# X_A and its U-conjugate X_A Z_B lead to different expectation values.
rpp=tensor(plus,plus)
assert trace(mul(rpp,xi))==1 and trace(mul(rpp,xz))==0
assert conj(U,xi)!=xi
result={'H_spectrum':[0,1,2,4], 'H_non_degenerate':True,
        'U':'diag(1,1,1,-1)', 'actual_state':'|00><00|',
        'U_preserves_H_and_actual_state':True,
        'maps':{'X_A':'X tensor Z', 'X_B':'Z tensor X', 'Z_A':'Z tensor I', 'Z_B':'I tensor Z'},
        'transformed_A_not_original_A_or_B':True,
        'transformed_AB_algebras_commute':True,
        'fixed_pointer_projectors_and_commutation_with_H':True,
        'marked_preparation_plus_plus_expectations':{'X_A':'1','U X_A U_dagger':'0'},
        'scope':'Exact finite identities; no exhaustive optimization or reproduction of published algorithm; no phenomenal claims.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
