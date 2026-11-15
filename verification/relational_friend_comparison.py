#!/usr/bin/env python3
"""Scoped probability atlas for the existing one-friend circuit.

The intermediate friend/bob scope is a stipulated contextual assignment in
reversal runs, not evidence of subjects or an undisturbed physical measurement.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

from subject_friend_quantum_extensions import quantum_correlators, sharp, marginal, tv

SIGNS=(-1,1)


def ab_dist(correlation):
    return {(a,b): (1+a*b*correlation)/4 for a,b in product(SIGNS,repeat=2)}


def friend_bob():
    return {(c,b): (1+c*b*F(3,5))/4 for c,b in product(SIGNS,repeat=2)}


def read_joint(y, ab):
    return {(a,b,c): ab[a,b] if c==a else F(0)
            for a,b,c in product(SIGNS,repeat=3)}


def independent_reverse_joint(ab):
    # P(a,b) P(c|b). A contextual probability completion, NOT a physical law.
    return {(a,b,c): ab[a,b]*(1+c*b*F(3,5))/2
            for a,b,c in product(SIGNS,repeat=3)}


def assert_distribution(p):
    assert sum(p.values())==1 and all(v>=0 for v in p.values())


def main():
    corr=quantum_correlators()
    assert corr=={(1,1):F(3,5),(1,2):F(3,5),(2,1):F(4,5),(2,2):F(-4,5)}
    ab={xy:ab_dist(e) for xy,e in corr.items()}
    cb=friend_bob()
    assert_distribution(cb)
    for p in ab.values(): assert_distribution(p)
    assert marginal(cb,(1,))=={(-1,):F(1,2),(1,):F(1,2)}
    for xy,p in ab.items():
        assert marginal(p,(1,))==marginal(cb,(1,))
        assert marginal(p,(0,))=={(-1,):F(1,2),(1,):F(1,2)}
    for y in (1,2):
        read=read_joint(y,ab[1,y]); assert_distribution(read)
        assert marginal(read,(0,1))==ab[1,y]
        assert marginal(read,(2,1))==cb
        assert sum(p for (a,b,c),p in read.items() if a!=c)==0
    reverse={y:independent_reverse_joint(ab[2,y]) for y in (1,2)}
    for y,p in reverse.items():
        assert_distribution(p)
        assert marginal(p,(0,1))==ab[2,y]
        assert marginal(p,(2,1))==cb
    glued_tv=tv(marginal(reverse[1],(0,2)),marginal(reverse[2],(0,2)))
    assert glued_tv==F(12,25)
    # A separate known completion saturates the universal lower bound.
    sharp1,sharp2=sharp(2,1),sharp(2,2)
    for y,p in ((1,sharp1),(2,sharp2)):
        assert marginal(p,(0,1))==ab[2,y]
        assert marginal(p,(2,1))==cb
    min_tv=tv(marginal(sharp1,(0,2)),marginal(sharp2,(0,2)))
    assert min_tv==F(2,5)
    result={
      'status':'passed',
      'scope':'Exact overlapping probability scopes for an ideal friend circuit; relation to phenomenal observers and universal agency is stipulated and unresolved.',
      'quantum_correlators':{str(k):str(v) for k,v in corr.items()},
      'read_scope':'a=c with probability 1; overlapping (c,b) equals declared early friend-bob scope',
      'reverse_scope':'(a,b) and (c,b) have a common unbiased b marginal; no (a,c) joint is postulated by the atlas',
      'illustrative_conditional_gluing_ac_tv':'12/25',
      'known_sharp_gluing_ac_tv':'2/5',
      'limitations':'The friend-bob scope in a reversal run is an additional contextual postulate, not an independently measured joint record. Formal compatibility is not a subject or quantum interpretation.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
