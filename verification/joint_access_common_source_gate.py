#!/usr/bin/env python3
"""Finite common-source/joint-access diagnostics; no experiential inference."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math

BITS = (0, 1)


def h2(p):
    if p in (0, 1):
        return 0.0
    return -p * math.log2(p) - (1-p) * math.log2(1-p)


def open_distributions():
    joint, common = defaultdict(F), defaultdict(F)
    for x, y in product(BITS, repeat=2):
        parity = x ^ y
        # Internal joint access followed by a common error of probability 1/4.
        for error in BITS:
            w = parity ^ error
            joint[(x, y, w, w)] += F(1, 4) * (F(1, 4) if error else F(3, 4))
        # Common-source rival has a Y leakage on half of trials; otherwise guess.
        for leak, guess in product(BITS, repeat=2):
            w = parity if leak else guess
            common[(x, y, w, w)] += F(1, 4) * F(1, 2) * F(1, 2)
    return dict(joint), dict(common)


def acc(dist):
    return sum(prob for (x, y, w, _), prob in dist.items() if w == x ^ y)


def main():
    joint, common = open_distributions()
    assert sum(joint.values()) == sum(common.values()) == 1
    assert joint == common
    assert acc(joint) == F(3, 4)
    assert all(w == w2 for _, _, w, w2 in joint)
    for x, y in product(BITS, repeat=2):
        assert sum(v for (a,b,_,_),v in joint.items() if (a,b)==(x,y)) == F(1,4)

    # Parity-only leak S is independent of each input marginally, but
    # S together with X determines Y and parity exactly.
    for x in BITS:
        assert sum(F(1,4) for a,b in product(BITS, repeat=2)
                   if a == x and (a ^ b) == 1) == F(1,4)
    for y in BITS:
        assert sum(F(1,4) for a,b in product(BITS, repeat=2)
                   if b == y and (a ^ b) == 1) == F(1,4)
    assert all((x ^ (x ^ y)) == y for x, y in product(BITS, repeat=2))

    # Blocked-arm operational gate: validity >= 9/10, with no performance
    # restriction in the remaining fraction. These are endpoint witnesses.
    failure = F(1,10)
    common_upper = (1-failure) * F(1,2) + failure
    joint_lower = (1-failure) * F(3,4)
    assert (common_upper, joint_lower) == (F(11,20), F(27,40))
    midpoint = (common_upper + joint_lower) / 2
    radius = (joint_lower-common_upper)/2
    assert midpoint == F(49,80) and radius == F(1,16)
    n = math.ceil(math.log(40) / (2*float(radius)**2))
    assert n == 473 and math.exp(-2*n*float(radius)**2) < .025

    # Conditional report-to-experience bounds: hypothetical assumptions,
    # not empirical calibration. Endpoints are convex mixtures.
    a,b,eta,r = F(9,10),F(1,10),F(1,10),F(1,20)
    e_lower = (1-eta)*a-r
    e_upper = b+(1-b)*eta+r
    assert (e_lower,e_upper) == (F(19,25), F(6,25))
    # Monotonic orientation of binary entropy for success >= 1/2.
    information = 1 - h2(.25)
    assert .188 < information < .190
    receipt = {
        'status': 'passed',
        'open_complete_report_distributions_match': True,
        'open_parity_accuracy_both_models': str(acc(joint)),
        'report_agreement_both_models': '1',
        'marginal_leak_test_X_and_Y': 'independent in each marginal',
        'conditional_leak_information_bits': 1,
        'fano_information_lower_bound_at_75_percent_accuracy_bits': information,
        'blocked_common_source_accuracy_upper_bound': str(common_upper),
        'blocked_joint_access_accuracy_lower_bound': str(joint_lower),
        'blocked_decision_threshold': str(midpoint),
        'ideal_iid_blocked_trials_sufficient': n,
        'per_hypothesis_hoeffding_error_upper_bound': math.exp(-2*n*float(radius)**2),
        'hypothetical_experiential_report_bounds': [str(e_lower),str(e_upper)],
        'scope': 'Hypothetical finite causal models and stipulated validity/report bounds. No human data, validated experiential assay, subject count or claim of experimentally established pathway isolation.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
