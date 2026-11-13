#!/usr/bin/env python3
"""Unplanned follow-up: correlation versus independent majority-vote errors."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from subject_constitution_interface import minority_error


def main():
    n=21; e=F(1,10); independent=minority_error(n,e)
    # Exactly the same marginal bit-flip error on each trial; a single common
    # noise bit is sampled per 21-trial block and reused on every trial.
    fully_shared=e
    # A mixture of independent and shared-noise blocks also preserves every
    # per-trial marginal but can drastically change majority error.
    delta=F(1,100)
    mixture=(1-delta)*independent+delta*fully_shared
    assert fully_shared==e and mixture > independent
    # Small-n explicit enumeration validates correlated mixture probabilities.
    for N in (1,3,5):
        indep=minority_error(N,e)
        table={seq:(1-delta)*e**sum(seq)*(1-e)**(N-sum(seq))
                  + (delta*(e if all(seq) else 1-e) if len(set(seq))==1 else 0)
               for seq in product((0,1),repeat=N)}
        assert sum(table.values())==1
        assert all(sum(p for seq,p in table.items() if seq[i])==e for i in range(N))
        assert sum(p for seq,p in table.items() if sum(seq)>N//2)==(1-delta)*indep+delta*e
    out={'scope':'Post-protocol toy sensitivity check; no measured error rates or human data.',
         'per_trial_error':'1/10','trials':n,
         'independent_majority_error':str(independent),
         'independent_majority_error_decimal':float(independent),
         'fully_shared_majority_error':str(fully_shared),
         'independent_vs_shared_ratio':float(fully_shared/independent),
         'one_percent_shared_block_mixture_majority_error':str(mixture),
         'one_percent_shared_block_mixture_error_decimal':float(mixture),
         'mixture_vs_independent_ratio':float(mixture/independent)}
    text=json.dumps(out,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text); print(text)


if __name__=='__main__': main()
