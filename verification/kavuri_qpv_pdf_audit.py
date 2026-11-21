#!/usr/bin/env python3
"""Elementary checks only: supplied QPV PDF, not experiment or security proof."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def independence_counts(op):
    # Ideal independent, uniformly random verifier bits and local setting.
    joint = Counter((ua, op(ua, ub), ma) for ua, ub, ma in product((0, 1), repeat=3))
    ma_mp = Counter()
    mp = Counter()
    for (ua, m, ma), count in joint.items():
        ma_mp[(ma, m)] += count
        mp[m] += count
    # (M_P,M_A) independent of U_A; and M_A independent of (U_A,U_B)
    # conditional on M_P. Compute latter directly in full sample space.
    full = [(ua, ub, op(ua, ub), ma) for ua, ub, ma in product((0, 1), repeat=3)]
    first = all(joint[(ua, m, ma)] * 2 == ma_mp[(ma, m)] for ua, m, ma in product((0, 1), repeat=3))
    second = all(sum(1 for a,b,p,v in full if a==ua and b==ub and p==m and v==ma) * mp[m]
                 == sum(1 for a,b,p,v in full if a==ua and b==ub and p==m) * ma_mp[(ma,m)]
                 for ua,ub,m,ma in product((0,1), repeat=4) if mp[m])
    return {'setting_pair_independent_of_uA': first, 'verifier_setting_conditional_independence': second}


def main():
    xor = independence_counts(lambda a, b: a ^ b)
    and_setting = independence_counts(lambda a, b: a & b)
    assert xor == {'setting_pair_independent_of_uA': True, 'verifier_setting_conditional_independence': True}
    assert and_setting == {'setting_pair_independent_of_uA': False, 'verifier_setting_conditional_independence': True}
    assert Fraction(224, 232) * 100 > Fraction(964,10) and round(224/232*100, 1) == 96.6
    # The paper's 96.5% is compatible with truncation or alternate rounding,
    # but conventional rounding to one decimal gives 96.6%.
    assert 103 > 102
    assert round(102/103*100, 1) == 99.0
    assert Fraction(2, 1000) / Fraction(8, 1000000) == 250
    result = {'scope': 'Finite probability and arithmetic checks, not raw-data reproduction or full QPV proof.',
              'uniform_independent_bits_xor': xor, 'uniform_independent_bits_and_counterexample': and_setting,
              'basic_224_of_232_percent': 100*224/232,
              'extended_pdf_passed_exceeds_instances': True,
              'alternative_102_of_103_percent': 100*102/103,
              'designed_source_robustness_to_threshold_ratio': 250,
              'per_instance_delta_2_pow_minus_64': 2**-64}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
