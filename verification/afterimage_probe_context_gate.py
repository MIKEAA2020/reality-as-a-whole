#!/usr/bin/env python3
"""An exact illustrative identification gate, not a visual-system model fit."""
from fractions import Fraction as F
from itertools import product
import json


def selective_margin(p, h, g):
    """Contour selectively multiplies the adaptation term; criterion zero."""
    return p - g * h


def criterion_margin(p, h, g):
    """Adaptation effect is fixed; the criterion depends on history and context."""
    signal = p - h
    criterion = (g - 1) * h
    return signal - criterion


def common_gain_margin(p, h, g):
    """A common gain changes both terms, with zero decision criterion."""
    return g * (p - h)


def probability(margin):
    """Invented binary choice link on a bounded margin interval."""
    p = F(1, 2) + margin / 16
    if not 0 <= p <= 1:
        raise ValueError('margin outside probability domain')
    return p


def decision_point(h, adapt_gain, probe_gain, criterion):
    """Solve probe_gain*p - adapt_gain*h - criterion = 0."""
    if probe_gain <= 0:
        raise ValueError('positive probe gain required')
    return (adapt_gain * h + criterion) / probe_gain


def run():
    levels = [F(-2), F(-1), F(0), F(1), F(2)]
    histories = [F(-1), F(0), F(1)]
    contexts = [F(1), F(2)]
    rows = []
    for p, h, g in product(levels, histories, contexts):
        selective = probability(selective_margin(p, h, g))
        criterion = probability(criterion_margin(p, h, g))
        rows.append((p, h, g, selective, criterion))
    return {
        'scope': 'Invented finite response model; not measurements or a participant-data reanalysis.',
        'grid': {'probe_levels': list(map(str, levels)),
                 'history_levels': list(map(str, histories)),
                 'context_gains': list(map(str, contexts)),
                 'number_of_conditions': len(rows)},
        'all_selective_and_criterion_choice_probabilities_equal': all(r[3] == r[4] for r in rows),
        'no_adaptation_probabilities_equal_across_contexts': all(
            probability(selective_margin(p, F(0), F(1))) ==
            probability(selective_margin(p, F(0), F(2))) for p in levels),
        'example_h_1': {
            'common_gain_nulls': [str(decision_point(F(1), g, g, F(0))) for g in contexts],
            'selective_gain_nulls': [str(decision_point(F(1), g, F(1), F(0))) for g in contexts],
            'criterion_shift_nulls': [str(decision_point(F(1), F(1), F(1), (g-F(1))*F(1))) for g in contexts]},
        'proof': 'For all p,h,g: (p-h)-(g-1)h = p-gh. Common gain has a different slope and predicts a fixed null when g>0.',
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
