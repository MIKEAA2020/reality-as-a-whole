#!/usr/bin/env python3
"""Combine two existing finite gates. No experiential or metaphysical inference."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
from subject_factorization_redescription_gate import (STATES, PERMS, factorizations,
    observable_partition, kernel, independent_local_factors, conjugate_kernel,
    permute_factors)
from experience_ground_support_toy import supports as coordinate_supports

UNIVERSE=frozenset(range(len(STATES)))


def supports(target, actual, factors):
    """Minimal subsets of actual factor blocks implying target on finite state space."""
    target=frozenset(target)
    if actual not in target or not target.issubset(UNIVERSE):
        raise ValueError('Actual point must satisfy a valid target')
    blocks=[]
    for part in factors:
        matching=[block for block in part if actual in block]
        if len(matching)!=1:raise ValueError('Factor must partition actual point uniquely')
        blocks.append(matching[0])
    result=set()
    for n in range(len(blocks)+1):
        for choice in combinations(blocks,n):
            chosen=frozenset(choice)
            if any(s.issubset(chosen) for s in result):continue
            intersection=UNIVERSE
            for block in chosen:intersection=intersection.intersection(block)
            if intersection.issubset(target):result.add(chosen)
    return frozenset(result)


def transport_family(family,perm):
    return frozenset(frozenset(frozenset(perm[i] for i in block) for block in s)
                     for s in family)


def encode_family(family):
    return sorted([sorted([sorted(block) for block in s]) for s in family])


def main():
    xpart=observable_partition(tuple(s[0] for s in STATES))
    target=frozenset(i for i,s in enumerate(STATES) if s[0]==1)
    actual=STATES.index((1,1))
    K=kernel(F(1,4),F(1,3)); uniform=kernel(F(1,2),F(1,2))
    winners=[f for f in factorizations if independent_local_factors(K,f)]
    assert len(winners)==1 and xpart in winners[0]
    base=supports(target,actual,winners[0])
    assert base==frozenset((frozenset((target,)),))
    # Naively replacing factors by new coordinate axes changes the answer:
    # u=x XOR y, v=y, so x=u XOR v and (x,y)=(1,1) -> (u,v)=(0,1).
    old=coordinate_supports(lambda s:bool(s[0]),(1,1))
    naive_new=coordinate_supports(lambda s:bool(s[0]^s[1]),(0,1))
    assert old==[(0,)] and naive_new==[(0,1)]
    assert supports(UNIVERSE,actual,winners[0])==frozenset((frozenset(),))
    try:supports(UNIVERSE-target,actual,winners[0])
    except ValueError:pass
    else:raise AssertionError('False target accepted')
    # The entire problem, including physical factor partitions, is transported.
    covariance_cases=0
    for perm in PERMS:
        moved=conjugate_kernel(K,perm)
        ws=[f for f in factorizations if independent_local_factors(moved,f)]
        assert len(ws)==1 and ws[0]==permute_factors(winners[0],perm)
        newtarget=frozenset(perm[i] for i in target)
        assert supports(newtarget,perm[actual],ws[0])==transport_family(base,perm)
        # Exhaust all three factor pairs, all target events and actual points.
        for factor in factorizations:
            moved_factor=permute_factors(factor,perm)
            for n in range(1,len(UNIVERSE)+1):
                for items in combinations(UNIVERSE,n):
                    event=frozenset(items)
                    mapped_event=frozenset(perm[i] for i in event)
                    for state in event:
                        before=supports(event,state,factor)
                        after=supports(mapped_event,perm[state],moved_factor)
                        assert after==transport_family(before,perm)
                        covariance_cases+=1
    assert covariance_cases==2304
    # Symmetric K has three permissible pairs. They yield two distinct support
    # families for the same target and point. We do not pick one after seeing p.
    ties=[f for f in factorizations if independent_local_factors(uniform,f)]
    families={supports(target,actual,f) for f in ties}
    assert len(ties)==3 and len(families)==2 and base in families
    assert sorted(sorted(len(s) for s in family) for family in families)==[[1],[2]]
    receipt={'scope':'finite support and factorization gates only; no phenomenal ground established',
      'states':4,'asymmetric_kernel_factorizations':len(winners),
      'asymmetric_support_block_indices':encode_family(base),
      'naive_coordinate_support_size_before_after_mixing':[len(old[0]),len(naive_new[0])],
      'all_bijective_renamings_checked':len(PERMS),
      'covariance_event_state_factor_cases':covariance_cases,
      'uniform_kernel_factorizations':len(ties),
      'uniform_kernel_distinct_support_families':len(families),
      'uniform_kernel_support_family_cardinalities':sorted(sorted(len(s) for s in family) for family in families),
      'tautology_supports_empty_set':True,
      'scope_limit':'Kernel, interventions, factor eligibility, and target content are specified; truthmaker or subject identity is not derived.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print('PASS: factor-selected support transports under all renamings; symmetry tie remains')

if __name__=='__main__':main()
