"""Finite sufficiency audit of non-additivity plus macro-causal relevance.
Target labels stand for independently fixed hypothetical contrasts; no actual
phenomenal measurements or conscious assignments are asserted.
"""
from itertools import permutations

STATES=tuple(range(4))
TARGETS=('a','b','c','d')


def mappings():return tuple(permutations(TARGETS))


def validate(mapping):
    if len(mapping)!=4 or set(mapping)!=set(TARGETS):raise ValueError('Bijective four-state target map required')


def inverse(mapping):
    validate(mapping)
    return {q:x for x,q in enumerate(mapping)}


def transition(x):
    if x not in STATES:raise ValueError('Physical state in {0,1,2,3} required')
    return (x+1)%4


def physical_history(initial,steps):
    if initial not in STATES or not isinstance(steps,int) or steps<0:raise ValueError('Valid initial state and nonnegative horizon required')
    result=[initial]
    for _ in range(steps):result.append(transition(result[-1]))
    return tuple(result)


def macro_transition(mapping,q):
    back=inverse(mapping)
    if q not in back:raise ValueError('Unknown target label')
    return mapping[transition(back[q])]


def implemented_intervention(mapping,q):
    """do(E=q) is shorthand for implementing do(X=f^{-1}(q)).
    It is not an additional independently manipulable phenomenal variable.
    """
    back=inverse(mapping)
    if q not in back:raise ValueError('Unknown target label')
    x=back[q]
    return {'physical_state':x,'physical_report':x,'target_annotation':q}


def calibrated(anchors):
    if any(x not in STATES or q not in TARGETS for x,q in anchors.items()):raise ValueError('Valid physical/target anchors required')
    return tuple(f for f in mappings() if all(f[x]==q for x,q in anchors.items()))


def predictions_under_physical_interventions(mapping):
    validate(mapping)
    return tuple((x,x,transition(x)) for x in STATES)


def physical_realization_of_report(mapping,x):
    validate(mapping)
    if x not in STATES:raise ValueError('Invalid physical state')
    # The target is a deterministic physical macro-coordinate, not an extra cause.
    q=mapping[x]
    return inverse(mapping)[q]
