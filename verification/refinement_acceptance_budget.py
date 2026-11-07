"""Conservative cutoff selection for the declared 1D locality/record model.

The certificate combines explicit analytic tails for a triangular smear with
Gaussian sign readout. It is not a quantum-gravity or universal cutoff bound.
"""
from math import ceil, pi
from pathlib import Path
import json
from cross_framework_causal_cutoff import evaluate, WIDTH, G, Q


def certificate(N):
    comm=16/(3*pi*WIDTH**4*N**3)
    energy=8*G**2/(pi*WIDTH**4*N)
    # For the specified Gaussian initial state, V_N >= 1/(2pi).
    # erf(x) <= 2x/sqrt(pi) yields noisy-order TV <= (1-2Q)*|G|*|kappa_N|.
    order=(1-2*Q)*abs(G)*comm
    return order,energy


def main():
    order_tolerance=1e-4
    energy_tolerance=.1
    # ceil plus explicit verification avoids relying on rounding near integer boundaries.
    n_order=ceil(((1-2*Q)*abs(G)*16/(3*pi*WIDTH**4*order_tolerance))**(1/3))
    n_energy=ceil(8*G**2/(pi*WIDTH**4*energy_tolerance))
    n=max(n_order,n_energy)
    ob,eb=certificate(n)
    assert ob<=order_tolerance and eb<=energy_tolerance
    obs=evaluate(n)
    energy_error=abs(obs['signal_energy']-G**2/WIDTH**3)
    assert obs['two_record_ordering_tv']<=ob+1e-14
    assert energy_error<=eb+1e-14
    # No smaller N can satisfy both selected analytic certificates: the
    # energy certificate is strictly decreasing and already fails at n-1.
    assert n==n_energy and certificate(n-1)[1]>energy_tolerance
    result={'status':'passed','scope':'fixed triangular-smear, Gaussian state and two-memory instrument; 1D regulated free field',
            'requirements':{'two_record_ordering_tv_max':order_tolerance,'source_energy_error_max':energy_tolerance},
            'certified_minimum_N_for_these_sufficient_bounds':n,
            'separate_bound_minima':{'ordering':n_order,'energy':n_energy},
            'at_N':{'ordering_tv_bound':ob,'energy_error_bound':eb,
                    'actual_computed_ordering_tv':obs['two_record_ordering_tv'],
                    'actual_computed_energy_error':energy_error,
                    'signal_energy':obs['signal_energy']},
            'limitations':'Sufficient bounds only; does not prove smaller cutoff fails, detector correctness, quantum gravity or full stress-energy control.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
