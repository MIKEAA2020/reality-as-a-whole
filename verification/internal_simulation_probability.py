#!/usr/bin/env python3
"""Finite observer-count examples, conditional on explicit consciousness assumptions.

These are accounting controls, not measured population fractions or a derivation
of the physical, experiential, simulation, or self-location principles.
"""
from fractions import Fraction


def sampled_observer_probability(base, simulated, evidence_base=1, evidence_simulated=1):
    if min(base, simulated, evidence_base, evidence_simulated) < 0:
        raise ValueError('counts and likelihoods must be nonnegative')
    if evidence_base > 1 or evidence_simulated > 1:
        raise ValueError('likelihoods must be <= 1')
    b=Fraction(base)*Fraction(evidence_base)
    s=Fraction(simulated)*Fraction(evidence_simulated)
    if b+s == 0:
        raise ValueError('evidence has zero weight')
    return s/(b+s)


def worlds_probability(worlds, size_bias=False):
    """(world prior, eligible base weight, eligible simulated weight).

    Unbiased mode chooses a world by its prior, then an observer uniformly;
    size-bias mode weights worlds by their observer population before sampling.
    All observers are assumed to match the evidence in this comparison.
    """
    numerator=Fraction(0)
    denominator=Fraction(0)
    for prior,base,sim in worlds:
        p,b,s=map(Fraction,(prior,base,sim))
        if p < 0 or b < 0 or s < 0 or b+s == 0:
            raise ValueError('invalid world or empty observer population')
        if size_bias:
            numerator+=p*s
            denominator+=p*(b+s)
        else:
            numerator+=p*s/(b+s)
            denominator+=p
    if denominator == 0:
        raise ValueError('world prior must have positive total')
    return numerator/denominator


def nested_fraction(reproduction, depth):
    r=Fraction(reproduction)
    if r < 0 or depth < 0:
        raise ValueError('negative reproduction or depth')
    amounts=[r**d for d in range(depth+1)]
    return sum(amounts[1:])/sum(amounts)


def total_valence(values):
    return sum((Fraction(v) for v in values), Fraction(0))


def steering_marginals(plus, minus):
    """Hypothetical reweighting by Alice's ± outcome in Bell Z/X tests."""
    p,m=Fraction(plus),Fraction(minus)
    if p <= 0 or m <= 0:
        raise ValueError('weights must be positive')
    return p/(p+m), Fraction(1,2)
