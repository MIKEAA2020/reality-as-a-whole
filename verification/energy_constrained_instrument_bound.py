"""Arithmetic/control checks for the analytic finite-N instrument-order bound.

These checks do not prove the Sobolev or channel inequalities; see
CUTOFF_INSTRUMENT_UNIFORMITY.md. Units and kinetic Hamiltonian are as there.
"""
from math import sqrt, erf, pi, ceil
from pathlib import Path
import json
from cross_framework_causal_cutoff import evaluate, coefficient, WIDTH, Y, G
from math import cos


def kappa_bound(N):
    return 16/(3*pi*WIDTH**4*N**3)


def norm_bound(N, E):
    # B_N >= 1/(2*pi); unhalved energy-constrained diamond norm.
    return min(2.,4*sqrt(abs(G)*kappa_bound(N)*sqrt(4*pi*E)))


def main():
    E=100.
    target=.01
    constant=16*abs(G)*(16/(3*pi*WIDTH**4))*sqrt(4*pi*E)
    N=ceil((constant/target**2)**(1/3))
    while norm_bound(N,E)>target:
        N+=1
    while N>1 and norm_bound(N-1,E)<=target:
        N-=1
    assert norm_bound(N,E)<=target and norm_bound(N-1,E)>target
    checks=[]
    for n in (4,8,16,32,64,128,256):
        k=abs(evaluate(n)['commutator_overlap'])
        B=(1+2*sum(coefficient(j)**2*cos(j*Y)**2 for j in range(1,n+1)))/(2*pi)
        sigma=sqrt(B/(8*E))
        # Worst Gaussian sign probability gap at this variance; record-only
        # trace distance is 2*TV. General instrument bound can be larger.
        record_trace_distance=2*erf(abs(G)*k/(2*sqrt(2)*sigma))
        finite_bound=min(2.,4*sqrt(abs(G)*k*sqrt(2*E/B)))
        assert record_trace_distance<=finite_bound+1e-14
        assert finite_bound<=norm_bound(n,E)+1e-12
        checks.append({'N':n,'gaussian_record_trace_distance':record_trace_distance,
                       'instrument_bound_using_actual_kappa_and_B':finite_bound,
                       'instrument_bound_using_tails':norm_bound(n,E)})
    result={'status':'passed','energy_constraint':E,'unhalved_diamond_tolerance':target,
            'sufficient_N_for_conservative_instrument_order_bound':N,
            'bound_at_N':norm_bound(N,E),'bound_at_N_minus_one':norm_bound(N-1,E),
            'controls':checks,'scope':'same finite-N threshold instruments, all field inputs and arbitrary ancillas with system kinetic-energy bound; not a continuum comparison or local probe'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
