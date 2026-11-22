#!/usr/bin/env python3
"""Finite matrix controls for trace/modular-flow and entropy distinctions.

These illustrate the exact operator-algebra statements in the companion audit;
they do not model a type-II gravitational algebra or solve the problem of time.
"""
import cmath
import json
import math
from pathlib import Path


def mul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def adj(a): return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]
def conj(u,a): return mul(mul(u,a),adj(u))
def diff(a,b): return max(abs(a[i][j]-b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def traceflow(t):
    # Faithful normalized matrix trace, represented by I/2.
    z=cmath.exp(1j*t*math.log(.5))
    return [[z,0],[0,z]]


def stateflow(t):
    return [[cmath.exp(1j*t*math.log(.75)),0],[0,cmath.exp(1j*t*math.log(.25))]]


def qubit_entropy(rho):
    # Entropy is used only for a checked positive, unit-trace 2x2 density.
    if abs(rho[0][1]-rho[1][0].conjugate())>1e-12 or abs(rho[0][0]+rho[1][1]-1)>1e-12:
        raise ValueError('expected a Hermitian density with trace one')
    determinant=(rho[0][0]*rho[1][1]-rho[0][1]*rho[1][0]).real
    root=math.sqrt(max(0,1-4*determinant))
    eig=[(1+root)/2,(1-root)/2]
    if min(eig)<-1e-12: raise ValueError('density not positive')
    return -sum(p*math.log(p) for p in eig if p>0)


def run():
    x=[[0,1],[1,0]]
    rho=[[.75,0],[0,.25]]
    eta=[[.6,.2],[.2,.4]]
    t=math.pi/(2*math.log(3))
    modular_x=conj(stateflow(t),x)
    stationary_x=conj(traceflow(t),x)
    assert diff(stationary_x,x)<1e-14
    assert abs(modular_x[0][1]-1j)<1e-14
    assert diff(conj(stateflow(t),rho),rho)<1e-14
    # H=diag(0,1), rho=exp(-beta H)/Z, beta=ln 3. Its nontracial
    # modular flow equals ordinary Heisenberg flow at -beta*s. The trace
    # alone remains static. The ideal constrained clock is not simulated.
    alpha=lambda time: [[1,0],[0,cmath.exp(1j*time)]]
    assert diff(modular_x,conj(alpha(-math.log(3)*t),x))<1e-14
    entropy0=qubit_entropy(eta)
    entropy_t=qubit_entropy(conj(stateflow(t),eta))
    assert abs(entropy0-entropy_t)<1e-14
    # Distinct faithful states on the commutative algebra C^2 have identical
    # trivial modular flows, and their weights are not a permutation pair.
    p=[.75,.25];q=[.5,.5]
    assert p!=q and p!=list(reversed(q))
    return {'status':'passed','scope':'Finite matrix controls only; not type-II gravity or a solution of time.',
            'state_density_relative_to_standard_trace':[.75,.25],
            'trace_density_relative_to_standard_trace':[.5,.5],
            'selected_modular_parameter':t,
            'trace_modular_flow_fixes_X':diff(stationary_x,x)<1e-14,
            'nontracial_modular_flow_X_off_diagonal':[modular_x[0][1].real,modular_x[0][1].imag],
            'nontracial_state_is_stationary':diff(conj(stateflow(t),rho),rho)<1e-14,
            'sample_state_entropy_before':entropy0,'sample_state_entropy_after':entropy_t,
            'distinct_commutative_states_same_trivial_flow':[p,q]}


def main():
    result=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
