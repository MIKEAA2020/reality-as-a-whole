#!/usr/bin/env python3
"""Exact conditional misclassification controls for stipulated toy labels.

No empirical data, validated experiential anchor or physical q sensor.
"""
from fractions import Fraction as F
from pathlib import Path
import json

CELLS = ((0, 0), (0, 1), (1, 0), (1, 1))
OBSERVED = (1, 1)


def quality(rule, c):
    before, now = c
    return now if rule == 'level' else int(before == 0 and now == 1)


def compositions(total, n):
    if n == 1:
        yield (total,)
    else:
        for i in range(total + 1):
            for rest in compositions(total - i, n - 1):
                yield (i,) + rest


def metrics(rule, table, denominator):
    # table is the full joint over true cell C and report Y, conditional on
    # observed cell H=11; each count has mass 1/denominator.
    rho = sum(F(table[2*i+y], denominator) for i, c in enumerate(CELLS)
              for y in (0, 1) if c != OBSERVED)
    eta = sum(F(table[2*i+y], denominator) for i, c in enumerate(CELLS)
              for y in (0, 1) if y != quality(rule, c))
    r = sum(F(table[2*i+1], denominator) for i in range(len(CELLS)))
    return rho, eta, r


def check():
    denominator = 4
    tables = list(compositions(denominator, 8))
    assert len(tables) == 330
    cases = 0
    for rule in ('level', 'onset'):
        for rho in (F(i, 4) for i in range(5)):
            for eta in (F(i, 4) for i in range(5)):
                candidates = [metrics(rule, t, denominator)[2] for t in tables
                              if metrics(rule, t, denominator)[0] <= rho
                              and metrics(rule, t, denominator)[1] <= eta]
                if rule == 'level':
                    assert min(candidates) == max(F(0), 1-rho-eta)
                    assert max(candidates) == 1
                else:
                    assert min(candidates) == 0
                    assert max(candidates) == min(F(1), rho+eta)
                cases += 1
    # Fixed *known* posterior physical mixture: level vs onset differ only
    # on true 11. At most eta report flips can move each predicted rate.
    mixture = {c: F(n, 20) for c, n in zip(CELLS, (1, 2, 3, 14))}
    v_level = sum(p * quality('level', c) for c, p in mixture.items())
    v_onset = sum(p * quality('onset', c) for c, p in mixture.items())
    assert v_level == F(4, 5) and v_onset == F(1, 10)
    assert v_level - v_onset == mixture[OBSERVED] == F(7, 10)
    # Distinct hypothetical conditional report rates in H=11, both admissible
    # when rho+eta=1/2. These models have different unobserved posteriors.
    eta, rho = F(1, 4), F(1, 4)
    level_witness = (0, 0, 0, 0, 1, 0, 1, 2)  # C10/Y0, C11/Y0, C11/Y1
    onset_witness = (0, 0, 0, 1, 0, 0, 2, 1)  # C01/Y1, C11/Y0, C11/Y1
    assert metrics('level', level_witness, 4) == (rho, eta, F(1, 2))
    assert metrics('onset', onset_witness, 4) == (rho, eta, F(1, 2))
    p = F(71, 448)
    eps, phi = F(1, 20), F(1, 50)
    combined = (eps + phi) / p
    assert combined == F(784, 1775) and 2 * combined < 1
    return {
        'status': 'passed',
        'scope': 'conditional finite arithmetic only; no empirical q sensor, experiential anchor, or real-world outcome',
        'conditional_cell': 'observed 11',
        'grid_joint_tables': len(tables),
        'grid_rule_and_error_budget_cases': cases,
        'inequalities': {'level_report_rate': '[max(0,1-rho-eta), 1]',
                         'onset_report_rate': '[0, min(1,rho+eta)]'},
        'overlap_example': {'rho': str(rho), 'eta': str(eta), 'observed_positive_rate': '1/2',
                            'note': 'witnesses use different latent physical mixtures'},
        'known_conditional_physical_mixture': {'P_C11': str(mixture[OBSERVED]),
                    'level_true_positive_rate': str(v_level), 'onset_true_positive_rate': str(v_onset)},
        'global_budget_example': {'observed_cell_mass': str(p), 'global_assay_budget': str(eps),
                    'global_physical_cell_budget': str(phi), 'conditional_sum_upper_bound': str(combined)},
    }


def main():
    report = check()
    text = json.dumps(report, indent=2) + '\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
