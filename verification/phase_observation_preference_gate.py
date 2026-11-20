#!/usr/bin/env python3
"""Synthetic controls: observed phase lags need not be interaction preferences.

Not a neural-data analysis. Exact binary example plus a locked cosine triangle.
"""
from fractions import Fraction as Q
from itertools import product
import cmath
import json
import math
from pathlib import Path

OUT = Path(__file__).with_suffix('.json')
PAIRS = ((0, 1), (1, 2), (2, 0))


def cost(s):
    return sum((1+s[i]*s[j])//2 for i,j in PAIRS)


def main():
    states = list(product((-1,1), repeat=3))
    weights = {s: Q(1, 2**cost(s)) for s in states}
    z = sum(weights.values())
    prob = {s:w/z for s,w in weights.items()}
    assert z == Q(13,4)
    assert sum(prob.values()) == 1
    assert min(map(cost,states)) == 1
    assert sorted(set(prob.values())) == [Q(1,26), Q(2,13)]
    corr = [sum(prob[s]*s[i]*s[j] for s in states) for i,j in PAIRS]
    assert corr == [Q(-3,13)]*3
    # Same joint observational distribution, not just identical marginals:
    # A samples this Gibbs law; B receives a common variable with this law.
    model_a, model_b = prob.copy(), prob.copy()
    assert model_a == model_b
    # Clamp node 0 to +1: A keeps pair energy, B overrides its node output
    # without conditioning or altering the latent source distribution.
    a_raw = {(s[1],s[2]):weights[s] for s in states if s[0] == 1}
    az = sum(a_raw.values())
    a_clamp = {k:v/az for k,v in a_raw.items()}
    b_clamp = {(u,v):sum(p for s,p in prob.items() if s[1:]==(u,v))
               for u,v in product((-1,1), repeat=2)}
    tv = sum(abs(a_clamp[k]-b_clamp[k]) for k in a_clamp)/2
    assert tv == Q(3,26)
    assert a_clamp[(1,1)] == Q(1,13) and b_clamp[(1,1)] == Q(5,26)
    # 26 equally weighted observations exactly realize the same probabilities.
    samples = [s for s in states for _ in range(int(prob[s]*26))]
    assert len(samples) == 26
    assert all(math.prod(s[i]*s[j] for i,j in PAIRS)==1 for s in samples)
    assert [Q(sum(s[i]*s[j] for s in samples),26) for i,j in PAIRS] == corr
    # Mean phase resultant is negative and each independently fitted angle π;
    # for three equal weights the cosine triangle's F is 3/2 times its weight.
    fitted_unit_F = Q(3,2)
    fitted_plv_weight_F = fitted_unit_F * Q(3,13)
    assert fitted_plv_weight_F == Q(9,26)
    # Continuous locked configuration that minimizes antiphase cosine energy.
    theta = (0, 2*math.pi/3, 4*math.pi/3)
    actual_cost = sum(1-math.cos(theta[i]-theta[j]-math.pi) for i,j in PAIRS)
    learned_offsets = [cmath.phase(cmath.exp(1j*(theta[i]-theta[j]))) for i,j in PAIRS]
    fitted_cost = sum(1-math.cos(theta[i]-theta[j]-a)
                      for (i,j),a in zip(PAIRS,learned_offsets))
    assert math.isclose(actual_cost,1.5,abs_tol=1e-12)
    assert math.isclose(fitted_cost,0,abs_tol=1e-12)
    holonomy = cmath.exp(1j*sum(learned_offsets))
    assert abs(holonomy-1) < 1e-12
    result = {
        'scope':'synthetic phase-identifiability controls, no neural data',
        'binary_model':{
            'gibbs_energy':'sum (1+s_i*s_j)/2', 'inverse_temperature':'ln(2)',
            'normalizer':str(z), 'each_pair_mean':str(corr[0]),
            'pair_PLV':str(abs(corr[0])), 'fitted_phase_offset':'pi',
            'naive_fitted_cosine_F_unit_weights':str(fitted_unit_F),
            'naive_fitted_cosine_F_PLV_weights':str(fitted_plv_weight_F),
            'channel_frustration_A':1, 'channel_frustration_B':0,
            'entire_observational_distribution_equal':model_a==model_b,
            'synthetic_exact_frequency_sample_size':len(samples),
            'clamp_s0_positive_joint_plusplus_A':str(a_clamp[(1,1)]),
            'clamp_s0_positive_joint_plusplus_B':str(b_clamp[(1,1)]),
            'clamp_distribution_total_variation':str(tv),
            'minimax_expected_absolute_error_lower_bound':'1/2',
        },
        'locked_continuous_model':{
            'physical_antiphase_F':1.5,'actual_energy':actual_cost,
            'pair_PLV':1,'self_fitted_lag_cost':fitted_cost,
            'self_fitted_F':0,
        },
        'caveat':'observational equivalence is constructed; clamp predictions rely on specified intervention semantics',
    }
    OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
