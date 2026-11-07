"""Check a synthetic coarse-vs-graded report contrast and paper logit transforms.

No subject data are read or reconstructed. Values in the first example are
invented; coefficients in the second are quoted published model summaries.
"""
from fractions import Fraction as F
from itertools import product
from math import exp
from pathlib import Path
import json


def logistic(x):
    return 1.0 / (1.0 + exp(-x))


def main():
    # B=0: stipulated no stimulus experience; B=1: stipulated blurry cue.
    # Both are classified unseen by the synthetic coarse criterion because
    # neither is judged as a clearly identified line. This is not participant data.
    mass = {}
    for x, b, decision in product((0, 1), repeat=3):
        correct_prob = F(1, 2) if b == 0 else F(4, 5)
        decision_prob = correct_prob if decision == x else 1 - correct_prob
        mass[(x, b, decision)] = F(1, 2) * F(1, 2) * decision_prob
    assert sum(mass.values()) == 1
    for b, expected in ((0, F(1, 2)), (1, F(4, 5))):
        denominator = sum(v for (_, bb, _), v in mass.items() if bb == b)
        numerator = sum(v for (x, bb, d), v in mass.items() if bb == b and d == x)
        assert numerator / denominator == expected
    coarse_accuracy = sum(v for (x, _, d), v in mass.items() if x == d)
    assert coarse_accuracy == F(13, 20)
    assert coarse_accuracy == F(1, 2) * F(1, 2) + F(1, 2) * F(4, 5)

    # Koivisto et al. 2021, comparison model: the PAS nothing category
    # at short SOA, active TMS. Published logit median .096, 90% CrI [-.18,.37].
    # Monotone transformations preserve posterior quantile order. These are fixed
    # effect model summaries, not raw trial proportions or a new reanalysis.
    logit_median, logit_lo, logit_hi = .096, -.18, .37
    p_mid, p_lo, p_hi = map(logistic, (logit_median, logit_lo, logit_hi))
    assert p_lo < .5 < p_hi
    assert p_hi > .55

    # Different comparison from the same source: dichotomous unseen group,
    # median .61 logit in the explicit between-scale comparison model.
    binary_median = logistic(.61)
    assert .64 < binary_median < .66
    result = {
        'status': 'passed',
        'synthetic_mixture_not_data': {
            'nothing_probability_in_coarse_unseen': '1/2',
            'something_probability_in_coarse_unseen': '1/2',
            'nothing_accuracy': '1/2', 'something_accuracy': '4/5',
            'coarse_unseen_accuracy': str(coarse_accuracy),
            'interpretation': 'A coarse report can mix experience categories and show above-chance accuracy even when the no-stimulus category is at chance.',
        },
        'published_model_summary_monotone_transform_only': {
            'source': 'https://doi.org/10.1016/j.neuroscience.2021.08.025',
            'published_nothing_logit_median': logit_median,
            'published_nothing_logit_90_percent_credible_interval': [logit_lo, logit_hi],
            'transformed_fixed_effect_median': p_mid,
            'transformed_90_percent_credible_interval': [p_lo, p_hi],
            'binary_unseen_comparison_model_logit_median': .61,
            'binary_unseen_comparison_model_transformed_median': binary_median,
        },
        'scope': ('Hypothetical model is not fitted to the article; logit transformation is a '
                  'calculation on rounded published coefficients, not trial-level data. '
                  'Between-subject scale groups cannot identify this mixture directly.')
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
