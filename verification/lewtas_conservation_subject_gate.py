#!/usr/bin/env python3
"""Finite stipulated representations, NOT actual experiences or physical worlds.

Illustrate that an inventory measure alone does not fix subject ownership,
phenomenal quality, or observational identification. Definitions and outputs
are transparent assumptions, not a derivation of phenomenal consciousness.
"""
import json
from dataclasses import dataclass


@dataclass(frozen=True)
class Scenario:
    # Ingredients are formal tokens, not asserted to be micro-subjects.
    ingredients: frozenset
    # A support is one stipulated subject's set of represented ingredients.
    supports: tuple
    # An optional qualitative output label, stipulated rather than derived.
    quality: str
    # Observed physical/report record is stipulated to be the same for alternatives.
    record: tuple


def audit(s):
    if not s.ingredients or not s.supports or any(not x or not x<=s.ingredients for x in s.supports):
        raise ValueError('Invalid supports')
    if set().union(*s.supports)!=s.ingredients:
        raise ValueError('Uncovered ingredients')
    return {'distinct_ingredient_mass':len(s.ingredients),
            'sum_of_support_masses':sum(map(len,s.supports)),
            'represented_subjects':len(s.supports),
            'exclusive_ownership':sum(map(len,s.supports))==len(s.ingredients),
            'quality':s.quality,'record':list(s.record)}


def main():
    a,b=frozenset({'a'}),frozenset({'b'});ab=a|b
    rec=('integrated physical configuration','recorded response')
    # Fused, separate and nested cases each stipulate a different ownership rule.
    scenarios={'fused_orange':Scenario(ab,(ab,),'orange',rec),
               'fused_violet':Scenario(ab,(ab,),'violet',rec),
               'separate':Scenario(ab,(a,b),'unassigned',rec),
               'nested':Scenario(ab,(a,b,ab),'unassigned',rec)}
    values={k:audit(v) for k,v in scenarios.items()}
    assert all(x['distinct_ingredient_mass']==2 for x in values.values())
    assert values['nested']['sum_of_support_masses']==4
    assert len({tuple(x['record']) for x in values.values()})==1
    out={'scope':'Toy interpretation counterexamples only; neither consciousness nor physical or metaphysical possibility is established.',
         'cases':values,
         'lessons':['A distinct-token inventory is conserved in all four stipulations while subject assignments differ.',
                    'If quantity instead sums each subject support, nested case totals four rather than two; that stronger convention rules it out.',
                    'A quality label is not determined by a conserved amount unless additional qualitative or dynamical laws are specified.',
                    'Identical records were stipulated, not shown experimentally to arise from different real experiences.']}
    print(json.dumps(out,indent=2,allow_nan=False))


if __name__=='__main__':main()
