"""Counterexample to unrestricted uniform order-instrument convergence.

Same finite cosine regulator/smears as cross_framework_causal_cutoff.py.
The input is a squeezed Gaussian with N-dependent energy. Standard QM,
not a new general diamond-norm theorem or a gravitational calculation.
"""
from math import erf, sqrt, cos, pi, ceil
from pathlib import Path
import json
from cross_framework_causal_cutoff import evaluate, coefficient, Y


def noisy_joint(p, q):
    return [p*(1-q)**(2-a-b)*q**(a+b)
            +(1-p)*q**(2-a-b)*(1-q)**(a+b)
            for a in (0,1) for b in (0,1)]


def tv(p, r):
    return sum(abs(x-y) for x,y in zip(p,r))/2


def main():
    rows=[]
    for N in (4,8,16,32,64,128):
        k=evaluate(N)['commutator_overlap']
        assert abs(k)>1e-15
        # Q_h = sum_j h_j q_j; B = sum_j h_j^2.
        B=(1+2*sum(coefficient(n)**2*cos(n*Y)**2 for n in range(1,N+1)))/(2*pi)
        sigma=abs(k)/8
        # Input Q_h mean is -k/2 for g=+1. Source shifts it by k.
        # TV between pre- and post-source sign distributions is this erf.
        ideal_tv=erf(abs(k)/(2*sqrt(2)*sigma))
        # Independently form both four-outcome distributions (also for k<0).
        p_before=(1+erf(-k/(2*sqrt(2)*sigma)))/2
        p_after=(1+erf(k/(2*sqrt(2)*sigma)))/2
        assert abs(tv(noisy_joint(p_before,0),noisy_joint(p_after,0))-ideal_tv)<1e-14
        assert abs(tv(noisy_joint(p_before,.1),noisy_joint(p_after,.1))-.8*ideal_tv)<1e-14
        assert tv(noisy_joint(p_before,.1),noisy_joint(p_before,.1))==0
        assert tv(noisy_joint(p_before,.5),noisy_joint(p_after,.5))==0
        # P_h=(sum h_j p_j)/B is canonical to Q_h; uncertainty plus
        # Cauchy-Schwarz gives E_kin >= B/(8 sigma²).
        energy_lower=B/(8*sigma*sigma)
        assert ideal_tv>.9999
        rows.append({'N':N,'kappa':k,'Q_h_sigma':sigma,'ideal_record_order_tv':ideal_tv,
                     'lower_bound_input_kinetic_energy':energy_lower})
    # Uniform over Gaussian field input states for this classical record
    # marginal only, with total retained-mode kinetic energy <= E.
    E, q, d, g, target = 100.0, .1, .4, 1.0, 1e-4
    # |kappa_N| <= 16/(3*pi*d^4*N^3), B_N >= 1/(2*pi).
    prefactor=(1-2*q)*2*sqrt(2*E)*abs(g)*16/(3*pi*d**4)
    N_sufficient=ceil((prefactor/target)**(1/3))
    while prefactor/N_sufficient**3>target:
        N_sufficient+=1
    assert prefactor/N_sufficient**3 <= target
    result={'status':'passed','scope':'one prescribed threshold-readout instrument, ideal records, N-dependent squeezed Gaussian states',
            'rows':rows,'conclusion':'For every nonzero kappa, supremum over unrestricted input states of ideal record-order TV is one; the corresponding channel diamond distance is two.',
            'gaussian_energy_bound':{'E_kin_max':E,'bit_flip_probability':q,'tv_target':target,
                'sufficient_N':N_sufficient,'conservative_tv_at_N':prefactor/N_sufficient**3},
            'limitations':'Counterexample energy diverges as kappa tends to zero; bounded-energy result covers only Gaussian inputs and classical record marginals, not general complete-instrument convergence.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
