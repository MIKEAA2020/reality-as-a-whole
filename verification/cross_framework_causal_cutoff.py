"""Spacelike-locality/record test for the previous cosine-mode regulator.

Uses a 1D normalized transverse collective sector, not a 3+1 local net.
All calculations are finite sums; the continuum limits are analytic.
"""
import json
from math import sin, cos, pi, sqrt, erf
from pathlib import Path

WIDTH=.4
Y=pi/2
G=1.
Q=.1


def coefficient(n):
    x=n*WIDTH/2
    return (sin(x)/x)**2


def evaluate(N,include_sine=False):
    w=[0.]+[coefficient(n) for n in range(1,N+1)]
    # f centered at 0 and h at pi/2 are normalized triangular smearings.
    overlap=(1+2*sum(w[n]**2*cos(n*Y) for n in range(1,N+1)))/(2*pi)
    if include_sine:
        variance=(1+sum(w[n]**2/n for n in range(1,N+1)))/(2*pi)
    else:
        variance=(1+sum(w[n]**2*cos(n*Y)**2/n for n in range(1,N+1)))/(2*pi)
    # Preparation U_s=exp(-i s G Pi_f): expectation displacement ±G overlap.
    contrast=erf(abs(G*overlap)/sqrt(2*variance))
    signal_tv=(1-2*Q)*contrast
    success=(1+signal_tv)/2
    ordering_tv=(1-2*Q)*contrast/2
    energy=G**2*sum(n*n*w[n]**2 for n in range(1,N+1))/(2*pi)
    # Analytic asymptotic bounds, f/h and f are disjoint and f has H1 regularity.
    overlap_tail_bound=16/(3*pi*WIDTH**4*N**3)
    energy_tail_bound=8*G**2/(pi*WIDTH**4*N)
    assert abs(overlap)<=overlap_tail_bound+1e-12
    assert abs(energy-G**2/WIDTH**3)<=energy_tail_bound+1e-12
    return {'nmax':N,'commutator_overlap':overlap,'readout_variance':variance,
            'ideal_sign_contrast':contrast,'two_noisy_record_tv_between_signals':signal_tv,
            'equal_prior_success':success,'two_record_ordering_tv':ordering_tv,
            'signal_energy':energy,'analytic_overlap_tail_bound':overlap_tail_bound,
            'analytic_energy_tail_bound':energy_tail_bound}


def joint_probability(contrast,sign,after):
    # Encode first -> p0=(1+sign*contrast)/2; read first -> p0=1/2.
    p0=(1+sign*contrast)/2 if after else .5
    return {f'{a}{b}':p0*(1-Q)**(2-a-b)*Q**(a+b)+(1-p0)*Q**(2-a-b)*(1-Q)**(a+b) for a in (0,1) for b in (0,1)}


def main():
    sizes=[4,8,16,32,64,128,256]
    even=[evaluate(n) for n in sizes]
    full=[evaluate(n,True) for n in sizes]
    data=even[0]; contrast=data['ideal_sign_contrast']
    later=joint_probability(contrast,1,True); earlier=joint_probability(contrast,1,False)
    tv=sum(abs(later[k]-earlier[k]) for k in later)/2
    assert abs(tv-data['two_record_ordering_tv'])<1e-14
    assert abs(sum(later.values())-1)<1e-14 and abs(sum(earlier.values())-1)<1e-14
    assert abs(even[-1]['commutator_overlap'])<1e-6
    assert all(abs(x['commutator_overlap']-y['commutator_overlap'])<1e-14 for x,y in zip(even,full))
    result={'status':'passed','model':'one-dimensional cosine-mode sector at a=1; separate sine-inclusive control',
            'triangular_smearing_halfwidth':WIDTH,'centre_separation':Y,'source_displacement':G,
            'memory_bit_flip_probability':Q,'continuum_energy':G**2/WIDTH**3,
            'cosine_modes':even,'sine_inclusive_control':full,
            'two_bit_order_comparison_n4':{'source_before_readout':later,'readout_before_source':earlier,'tv':tv},
            'scope':'Regulator artifact; not superluminal signalling in a local continuum theory or a nonlinear GR refoliation test.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
