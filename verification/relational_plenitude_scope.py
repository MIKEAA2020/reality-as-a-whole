#!/usr/bin/env python3
"""Exact finite checks of two scoped-plenitude probability examples.

Records and histories are formal mathematical controls, not evidence of
physical worlds, experiences, actual infinity or a sampling mechanism.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

from subject_friend_quantum_extensions import quantum_correlators

SIGNS=(-1,1)


def build_sector(visibility):
    """40 specified actual record-slots per quantum setting pair."""
    correlations=quantum_correlators()
    records=[]
    for x,y in product((1,2), repeat=2):
        e=visibility*correlations[x,y]
        for a,b in product(SIGNS, repeat=2):
            p=(1+a*b*e)/4
            count=40*p
            assert count.denominator==1 and count>0
            records.extend((x,y,a,b,i) for i in range(int(count)))
    return records


def analyze_sector(records):
    corr={}
    for x,y in product((1,2),repeat=2):
        group=[r for r in records if r[:2]==(x,y)]
        assert len(group)==40
        assert {(r[2],r[3]) for r in group}==set(product(SIGNS,repeat=2))
        assert sum(r[2] for r in group)==sum(r[3] for r in group)==0
        corr[x,y]=F(sum(r[2]*r[3] for r in group),len(group))
    s=corr[1,1]+corr[1,2]+corr[2,1]-corr[2,2]
    return corr,s


def prefix_weight(word,n_min,p):
    """L=n_min+K, P(K=k)=2^(-k-1), first bit Bernoulli p, rest fair;
    bits after L are zero. Computes a finite cylinder weight exactly.
    """
    n=len(word)
    assert n>=1 and n_min>=1 and 0<p<1
    first=p if word[0] else 1-p
    prob=F(0)
    for length in range(n_min,n):
        if all(bit==0 for bit in word[length:]):
            prob += F(1,2**(length-n_min+1))*first*F(1,2**(length-1))
    tail=F(1) if n<=n_min else F(1,2**(n-n_min))
    return prob+tail*first*F(1,2**(n-1))


def main():
    sectors={v:build_sector(v) for v in (F(1),F(1,2))}
    summaries={v:analyze_sector(r) for v,r in sectors.items()}
    assert len(sectors[F(1)])==len(sectors[F(1,2)])==160
    assert summaries[F(1)][1]==F(14,5)
    assert summaries[F(1,2)][1]==F(7,5)
    assert {(x,y,a,b) for x,y,a,b,i in sectors[F(1)]} == \
           {(x,y,a,b) for x,y,a,b,i in sectors[F(1,2)]}
    # Quantified finite-prefix check for the countably-supported full-domain law.
    for n in range(1,11):
        words=list(product((0,1),repeat=n))
        probs=[prefix_weight(w,6,F(1,2)) for w in words]
        assert sum(probs)==1 and all(p>0 for p in probs)
        if n<=6:
            assert all(p==F(1,2**n) for p in probs)
    assert prefix_weight((1,)*7,6,F(1,2))==F(1,256)
    assert prefix_weight((1,),1,F(1,4))==F(1,4)
    assert prefix_weight((1,),1,F(3,4))==F(3,4)
    result={
      'status':'passed',
      'finite_record_slots_per_sector':160,
      'finite_support_identical_across_sectors':True,
      'finite_sector_CHSH':{'visibility_1':'14/5','visibility_1_over_2':'7/5'},
      'actual_history_domain':'countable eventually-zero binary sequences, stipulated',
      'finite_prefix_full_support_checked_up_to_length':10,
      'fair_prefix_checks_up_to_length':6,
      'all_ones_length_7_after_fair_prefix_6':'1/256 (fair law: 1/128)',
      'same_history_domain_alternative_first_bit_probabilities':['1/4','3/4'],
      'limitations':'Finite checks do not prove infinitary measure results, real subjects, physical admissibility of infinite histories, necessity, intrinsic experience, or a justified subject measure.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
