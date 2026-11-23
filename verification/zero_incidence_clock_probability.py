#!/usr/bin/env python3
"""Covariant clock-incidence probability, illustrated on a flat cylinder.

J and K are stipulated currents, not identified as real subjects or valence.
Midpoint quadrature is used for the analytic example in the report.
"""
import math


def sample(b=0.5, ell=0.5, cells=20000, split=1):
    """J^t=cos(2x), K^t=1+b cos(2x), T=t, L=(1+ell cos(2x))/(1+|ell|).

    Splitting a cell duplicates its same value with divided measure; it is a
    representation refinement, not an assertion about new physical subjects.
    """
    if abs(b) >= 1 or abs(ell) > 1 or cells <= 0 or split <= 0:
        raise ValueError('require |b|<1, |ell|<=1 and positive grid sizes')
    dx=2*math.pi/cells
    total=positive=negative=zero=val=sel_total=sel_val=sel_positive=naive_total=0.0
    for j in range(cells):
        x=(j+0.5)*dx
        c=math.cos(2*x)
        n=1+b*c
        v=c/n
        likelihood=(1+ell*c)/(1+abs(ell))
        for _ in range(split):
            w=n*dx/split
            total+=w
            val+=w*v
            naive_total+=w*c
            sel_total+=w*likelihood
            sel_val+=w*likelihood*v
            if v>0:
                positive+=w
                sel_positive+=w*likelihood
            elif v<0:
                negative+=w
            else:
                zero+=w
    return {'total':total, 'signed_total':val, 'naive_weighted_total':naive_total,
            'positive_fraction':positive/total, 'negative_fraction':negative/total,
            'zero_fraction':zero/total, 'mean':val/total,
            'selected_mean':sel_val/sel_total, 'selected_positive':sel_positive/sel_total}


def conditional_balance(p_zero, mean_plus, mean_minus):
    if not 0 <= p_zero < 1 or mean_plus <= 0 or mean_minus <= 0:
        raise ValueError('requires positive signs and nontrivial positive/negative populations')
    return (1-p_zero)*mean_plus/(mean_plus+mean_minus)


def admissible_ratio(incidence, signed_density):
    if incidence < 0:
        raise ValueError('negative incidence density')
    if incidence == 0:
        if signed_density != 0:
            raise ValueError('signed density exists outside incidence support')
        return None
    return signed_density/incidence
