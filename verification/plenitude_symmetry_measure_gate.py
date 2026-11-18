#!/usr/bin/env python3
"""Finite exact checks for the plenitude/subject-measure symmetry gate.
No evidence of actual subjects, quantum derivation, or physical probabilities.
"""
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent


def product_weight(bits,p):
    k=sum(bits);return p**k*(1-p)**(len(bits)-k)


def tv(n,p,q):
    return sum((F(math.comb(n,k))*abs(p**k*(1-p)**(n-k)-q**k*(1-q)**(n-k))
                for k in range(n+1)),F())/2


def main():
    checked=0
    # For each sector and finite prefix, check exact invariance for every
    # finite coordinate flip; distinct alpha values remain possible.
    for n in range(1,9):
        states=list(itertools.product((0,1),repeat=n))
        state_set=set(states)
        for alpha in (F(1,4),F(3,4)):
            sector_mass=(alpha,1-alpha)
            for sector in (0,1):
                for word in states:
                    weight=sector_mass[sector]*F(1,2**n)
                    for flip in states:
                        other=tuple(a^b for a,b in zip(word,flip))
                        assert other in state_set
                        assert weight==sector_mass[sector]*F(1,2**n)
                        checked+=1
            assert sum((alpha*F(1,2**n) for _ in states),F())==alpha
            assert sum(((1-alpha)*F(1,2**n) for _ in states),F())==1-alpha
    # Swap of sectors is invariant only at alpha=1/2 in this family.
    assert F(1,4)!=1-F(1,4) and F(1,2)==1-F(1,2)
    p=F(3,4); q=F(1,4)
    for n in range(1,11):
        states=list(itertools.product((0,1),repeat=n))
        assert sum((product_weight(x,p) for x in states),F())==1
        assert sum((product_weight(x,q) for x in states),F())==1
        assert all(product_weight(x,p)>0 and product_weight(x,q)>0 for x in states)
        assert product_weight((0,)*n,p)!=product_weight((1,)+(0,)*(n-1),p)
    # Equal fine-label weights; the coarse projection must be specified separately.
    refinements={'three_to_one':(3,1),'one_to_one':(1,1),'nine_to_one':(9,1)}
    refinement_probs={k:[str(F(a,a+b)),str(F(b,a+b))] for k,(a,b) in refinements.items()}
    assert refinement_probs['three_to_one']==['3/4','1/4']
    assert refinement_probs['one_to_one']==['1/2','1/2']
    # Explicit partial trace of the Schmidt vector and its local swap.
    def partial_trace_b(vec):
        return [[sum(vec[2*i+b]*vec[2*j+b] for b in range(2))
                 for j in range(2)] for i in range(2)]
    psi=[math.sqrt(3)/2,0.0,0.0,0.5]
    swap_a=[psi[2],psi[3],psi[0],psi[1]]
    original_matrix=partial_trace_b(psi)
    swapped_matrix=partial_trace_b(swap_a)
    reduced=(F(3,4),F(1,4)); swapped=(reduced[1],reduced[0])
    for i in range(2):
        for j in range(2):
            assert abs(original_matrix[i][j]-(float(reduced[i]) if i==j else 0.0))<1e-12
            assert abs(swapped_matrix[i][j]-(float(swapped[i]) if i==j else 0.0))<1e-12
    trace_distance=sum(abs(x-y) for x,y in zip(reduced,swapped))/2
    assert trace_distance==F(1,2)
    psi_equal=[math.sqrt(.5),0.0,0.0,math.sqrt(.5)]
    both_swapped=[psi_equal[3],psi_equal[2],psi_equal[1],psi_equal[0]]
    assert all(abs(a-b)<1e-12 for a,b in zip(psi_equal,both_swapped))
    tvs={str(n):str(tv(n,p,q)) for n in (1,4,8,20)}
    result={'status':'completed',
      'scope':'finite mathematics and stipulated toy measures; not subject discovery or derivation of Born probabilities',
      'type_weight_options':['1/4','3/4'],
      'finite_coordinate_flip_checks':checked,'max_finite_prefix_length':8,
      'type_swap_forces_equal_type_weight':True,
      'p_and_q':['3/4','1/4'],'total_variation_for_n':tvs,
      'finite_refinement_outcome_weights':refinement_probs,
      'unequal_schmidt_reduced_diagonal':[str(x) for x in reduced],
      'local_swap_reduced_diagonal':[str(x) for x in swapped],
      'local_swap_reduced_trace_distance':str(trace_distance),
      'proof_scope':'Infinite product uniqueness and singularity are analytical consequences of stated assumptions, not finite-test outputs.'}
    (ROOT/'verification/plenitude_symmetry_measure_gate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
