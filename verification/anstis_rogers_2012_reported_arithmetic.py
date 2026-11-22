#!/usr/bin/env python3
"""Arithmetic checks on *reported* aggregate numbers, not original data.

CIE checks assume the article's numbers denote standard nonnegative XYZ-derived
chromaticities. Distances are Euclidean in printed CIE x,y coordinates, not
necessarily the paper's unreported individual-observer averaging procedure.
"""
import json
from fractions import Fraction
from math import sqrt


def q(s):return Fraction(str(s))


def valid_xy(x,y):
    x,y=q(x),q(y)
    return x>=0 and y>=0 and x+y<=1


def squared_distance(a,b):
    return sum((q(x)-q(y))**2 for x,y in zip(a,b))


def ratio(monocular,binocular):
    m=squared_distance(*monocular);b=squared_distance(*binocular)
    if m<=0:raise ValueError('Zero monocular distance')
    return sqrt(float(b/m))


def results():
    exp2_m=(('0.454','0.448'),('0.440','0.452'))
    exp2_b=(('0.485','0.425'),('0.412','0.474'))
    exp4_m=(('0.448','0.452'),('0.433','0.462'))
    exp4_b=(('0.477','0.434'),('0.415','0.472'))
    exp3={'lime':('0.627','0.667'),'orange':('0.894','0.608')}
    return {'scope':'Arithmetic on article HTML; not original observations, statistics, or evidence of consciousness.',
            'exp3_reported_xy':{name:{'x':xy[0],'y':xy[1],'x_plus_y':str(q(xy[0])+q(xy[1])),
                                      'valid_nonnegative_XYZ_chromaticity':valid_xy(*xy)} for name,xy in exp3.items()},
            'exp2_ratio_from_printed_coordinates':ratio(exp2_m,exp2_b),
            'exp4_ratio_from_printed_coordinates':ratio(exp4_m,exp4_b),
            'article_ratios':{'exp2':6.5,'exp4':4.67},
            'hypothetical_independent_400_fair_binary_success_probability':2**-400,
            'source_cautions':['Article HTML has not been checked against original typeset figure images or raw data.',
                               'Ratio of distances between rounded aggregate coordinates is not necessarily the average individual ratio.',
                               'The probability 2^-400 assumes independent fair binary trials; actual experiment need not satisfy it.']}


if __name__=='__main__':print(json.dumps(results(),indent=2,allow_nan=False))
