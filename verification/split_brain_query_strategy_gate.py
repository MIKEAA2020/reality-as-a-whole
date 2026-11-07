#!/usr/bin/env python3
"""Exact, idealized task-control baselines; no paper data or human conclusions."""
from fractions import Fraction as F
from itertools import product
from math import comb, log2
from pathlib import Path
import json

BITS = (0, 1)
OUTPUTS = (0, 1, 2)  # 2 is STOP
CASES = tuple(product(BITS, repeat=2))  # shape, query/stop instruction


def target(x, instruction):
    return x if instruction == 0 else 2


def accuracy(f):
    return sum(F(f(x, y) == target(x, y), 4) for x,y in CASES)


def main():
    x_scores = [accuracy(lambda x,y, a=a: a[x]) for a in product(OUTPUTS, repeat=2)]
    y_scores = [accuracy(lambda x,y, a=a: a[y]) for a in product(OUTPUTS, repeat=2)]
    full_scores = [accuracy(lambda x,y, a=a: a[2*x+y]) for a in product(OUTPUTS, repeat=4)]
    assert max(x_scores) == F(1,2)
    assert max(y_scores) == F(3,4)
    assert max(full_scores) == 1
    # Perfect first-shape report regardless of instruction: succeeds on every
    # query trial but fails every stop trial.
    x_only = lambda x,y: x
    assert accuracy(x_only) == F(1,2)
    assert sum(F(x_only(x,0) == x,2) for x in BITS) == 1
    # Y-only: output stop when asked, otherwise always say shape zero.
    y_only = lambda x,y: 2 if y else 0
    assert accuracy(y_only) == F(3,4)
    q_baseline = F(3,4)
    # Demonstrate finite-sample uncertainty with fictional 65/80, not a paper dataset.
    n,k = 80,65
    tail = sum(F(comb(n,j), 1) * q_baseline**j * (1-q_baseline)**(n-j)
               for j in range(k,n+1))
    assert F(k,n) > q_baseline and tail > F(1,20)
    # Illustrative entropy plug-in at rounded 68.7%, not a confidence bound.
    err = .313
    fano = 1 + err*log2(err) + (1-err)*log2(1-err)
    assert .1033 < fano < .1035
    # A hypothetical non-transitive co-consciousness pattern cannot be the
    # equality relation of unique owners, but admits overlapping ownership.
    desired = {(0,1), (1,2)}
    unique_owner_solutions = []
    for owners in product(range(3), repeat=3):
        rel = {(i,j) for i,j in ((0,1),(1,2),(0,2)) if owners[i] == owners[j]}
        if rel == desired:
            unique_owner_solutions.append(owners)
    assert not unique_owner_solutions
    owners = ({'A'}, {'A','B'}, {'B'})
    overlap_rel = {(i,j) for i,j in ((0,1),(1,2),(0,2)) if owners[i] & owners[j]}
    assert overlap_rel == desired
    receipt = {
      'status':'passed',
      'inputs':'independent uniform bits, shape X and instruction Y',
      'output_labels':['shape_0','shape_1','stop'],
      'best_shape_only_overall_accuracy':str(max(x_scores)),
      'best_instruction_only_overall_accuracy':str(max(y_scores)),
      'best_both_inputs_overall_accuracy':str(max(full_scores)),
      'shape_only_query_subset_accuracy':'1',
      'shape_only_stop_subset_accuracy':'0',
      'fictional_example_successes':k,
      'fictional_example_trials':n,
      'fictional_exact_binomial_upper_tail_under_75_percent_null':float(tail),
      'illustrative_fano_at_assumed_true_68_7_percent_bits':fano,
      'nontransitive_relation_unique_owner_solutions':len(unique_owner_solutions),
      'nontransitive_relation_overlapping_owner_witness':[['A'],['A','B'],['B']],
      'scope':'Ideal balanced independent-input decision task; no trial-level data, empirical confidence bound, physical localization, phenomenal subject, or evidence of an actual shortcut.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__ == '__main__':
    main()
