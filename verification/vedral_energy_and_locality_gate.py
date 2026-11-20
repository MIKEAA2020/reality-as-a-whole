#!/usr/bin/env python3
"""Two-qubit conservation, conditioning and local-marginal diagnostic."""
from fractions import Fraction as F
import json

# Basis |system, pointer>: |00>, |01>, |10>, |11>.
def matrix(rows): return [[F(x) for x in row] for row in rows]
def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]
def transpose(a): return [list(row) for row in zip(*a)]
def tr(a): return sum(a[i][i] for i in range(len(a)))
def conjugate(u,rho): return mm(mm(u,rho),transpose(u))
def expect(rho,observable): return tr(mm(rho,observable))
def partial_pointer(rho):
    return [[sum(rho[2*s+b][2*t+b] for b in range(2)) for t in range(2)] for s in range(2)]
def partial_system(rho):
    return [[sum(rho[2*s+b][2*s+c] for s in range(2)) for c in range(2)] for b in range(2)]

zero=F(0); half=F(1,2)
U=matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
H=matrix([[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,1]])
P1=H
rho0=[[zero]*4 for _ in range(4)]
for i in (0,2):
    for j in (0,2): rho0[i][j]=half
rho=conjugate(U,rho0)
assert mm(H,U)==mm(U,H)
assert tr(rho0)==tr(rho)==1
assert expect(rho0,H)==expect(rho,H)==half
assert expect(rho0,P1)==expect(rho,P1)==half
assert tr(rho0)-expect(rho0,P1)==tr(rho)-expect(rho,P1)==half

# Conditioning on pointer labels yields different energies, without a
# separately modelled energy-violating collapse. They were already correlated
# to the corresponding system energy in the unitary output.
Ps=[matrix([[1,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]),
    matrix([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,1]])]
conditions=[]
for p in Ps:
    unnormalized=mm(mm(p,rho),p)
    prob=tr(unnormalized)
    energy=expect(unnormalized,H)/prob
    conditions.append((prob,energy))
assert conditions == [(half,F(0)),(half,F(1))]
assert sum(p*e for p,e in conditions)==half

Z_system=matrix([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]])
XX=matrix([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
rho_phase=conjugate(Z_system,rho)
assert partial_system(rho)==partial_system(rho_phase)
assert partial_pointer(rho)==partial_pointer(rho_phase)
assert expect(rho,XX)==1 and expect(rho_phase,XX)==-1
assert expect(rho_phase,H)==half
result={'status':'passed','scope':'two-qubit idealized closed-system unitary, not relativistic QFT, collapse dynamics, or experience',
        'energy_generator_commutes_with_measurement_unitary': True,
        'pre_and_post_energy_distribution':{'0':'1/2','1':'1/2'},
        'pre_and_post_mean_energy':'1/2',
        'conditional_pointer_outcomes':[{'probability':str(p),'conditional_energy':str(e)} for p,e in conditions],
        'local_phase_flip_preserves_both_reduced_states':True,
        'XX_correlation_before':'1','XX_correlation_after':'-1'}
print(json.dumps(result,indent=2))
