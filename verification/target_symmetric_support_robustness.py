#!/usr/bin/env python3
"""Finite symmetry and robustness checks; no experiential/ontological inference."""
from fractions import Fraction as F
from itertools import combinations
from math import sqrt, log
from pathlib import Path
import json
from subject_factorization_redescription_gate import (STATES, PERMS, factorizations,
    observable_partition, kernel, independent_local_factors, conjugate_kernel,
    permute_factors, defect)
from ground_support_factorization_gate import supports


def row_tv(a,b):
    return max(sum(abs(x-y) for x,y in zip(r,s))/2 for r,s in zip(a,b))


def compatible(Khat,eps):
    """Necessary candidate set when sup-row TV error <= eps and true defect = 0."""
    if eps < 0:raise ValueError('negative uncertainty')
    return frozenset(f for f in factorizations if defect(Khat,f)<=3*eps)


def main():
    actual=STATES.index((1,1)); target=frozenset(i for i,s in enumerate(STATES) if s[0]==1)
    xpart=observable_partition(tuple(s[0] for s in STATES))
    U=kernel(F(1,2),F(1,2));h=(1,0,2,3)
    stabilizer=[perm for perm in PERMS if perm[actual]==actual
                and frozenset(perm[i] for i in target)==target and conjugate_kernel(U,perm)==U]
    assert len(stabilizer)==2 and h in stabilizer
    aligned=frozenset(f for f in factorizations if xpart in f)
    assert len(aligned)==2
    assert not any(all(permute_factors(f,p)==f for p in stabilizer) for f in aligned)
    assert len([f for f in factorizations if all(permute_factors(f,p)==f for p in stabilizer)])==1
    assert permute_factors(next(iter(aligned)),h) in aligned
    assert all(independent_local_factors(U,f) for f in factorizations)
    # Both aligned candidates share the target block as their sole support.
    # This is a logical fact about the deliberately target-aligned toy, not
    # evidence that the target itself is an independent physical ground.
    aligned_supports={supports(target,actual,f) for f in aligned}
    assert aligned_supports==frozenset((frozenset((frozenset((target,)),)),))

    # Exact rational families K_delta and h K_delta h^-1. For a fixed labeled
    # candidate family, their winners differ while the inputs converge to U.
    cases=[]
    for n in (8,10,20,100,1000,10000):
        d=F(1,n);K=kernel(F(1,2)-d,F(1,2)-2*d);L=conjugate_kernel(K,h)
        wK=frozenset(f for f in factorizations if independent_local_factors(K,f))
        wL=frozenset(f for f in factorizations if independent_local_factors(L,f))
        assert len(wK)==len(wL)==1 and wK!=wL
        assert wL==frozenset(permute_factors(f,h) for f in wK)
        assert row_tv(K,U)==row_tv(L,U)==2*d
        assert row_tv(K,L)==2*d-4*d*d
        assert compatible(U,2*d)==factorizations
        assert wK.issubset(compatible(U,2*d)) and wL.issubset(compatible(U,2*d))
        cases.append({'delta':str(d),'tv_to_uniform':str(2*d),'pairwise_row_tv':str(2*d-4*d*d)})
    # A clear gap with an explicit error budget returns a single compatible factor.
    K=kernel(F(1,4),F(1,3));w=frozenset(f for f in factorizations if independent_local_factors(K,f))
    assert compatible(K,F(1,96))==w
    # Check the 3-epsilon Lipschitz certificate on the constructed pairs.
    for n in (8,20,100,1000):
        d=F(1,n);A=kernel(F(1,2)-d,F(1,2)-2*d);B=conjugate_kernel(A,h)
        eps=row_tv(A,B)
        for f in factorizations:assert abs(defect(A,f)-defect(B,f))<=3*eps
    # Ideal fixed-design independent sampling: verify the analytic KL upper
    # bound for one illustrative delta. The bound itself is proved in report.
    d=F(1,1000);n=100;A=kernel(F(1,2)-d,F(1,2)-2*d);B=conjugate_kernel(A,h)
    assert min(min(row) for row in B)>=F(1,16)
    a=2*d-4*d*d
    assert all(sorted([abs(x-y) for x,y in zip(r,s)])==[0,0,a,a] for r,s in zip(A,B))
    kl= n*sum(float(p)*log(float(p/q)) for ar,br in zip(A,B) for p,q in zip(ar,br))
    assert kl <= float(512*n*d*d)
    risk_lower=(1-16*sqrt(n)*float(d))/2
    assert abs(risk_lower-.42)<1e-12
    out={'scope':'finite model only; no empirical subjects or experiential grounds',
      'target_and_point_stabilizer_size':len(stabilizer),'target_aligned_candidate_pairs':len(aligned),
      'target_aligned_distinct_support_families':len(aligned_supports),
      'target_aligned_equivariant_unique_fixed_pairs':0,'nonaligned_fixed_pairs':1,
      'near_symmetry_rational_cases':cases,'uncertainty_rule':'retain F if defect(Khat,F) <= 3 epsilon',
      'gap_control_candidates':len(compatible(K,F(1,96))),
      'illustrative_four_rows_samples_each':n,'illustrative_delta':str(d),
      'illustrative_equal_prior_test_error_lower_bound':risk_lower,
      'scope_limit':'Statistical bound assumes the two stipulated kernels, known state preparation, independent trials and fixed parameter; not human or population inference.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS: target-preserving symmetry, near-tie uncertainty and finite-sample bound')

if __name__=='__main__':main()
