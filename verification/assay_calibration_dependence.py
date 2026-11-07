"""Exact finite controls for the maintained-disclosure assay contract.

Synthetic probability models only; not fitted to a consciousness experiment.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json


def majority_error(n,p):
    assert n%2==1
    return sum(F(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n//2+1,n+1))


def main():
    # Reference perfect, target prevalence 93%, and ocular channel always 1.
    # It agrees 93% overall while failing the negative class completely.
    prevalence=F(93,100)
    accuracy=prevalence
    fp,fn=F(1),F(0)
    assert accuracy==F(93,100) and fp+fn==1

    # Hypothetical balanced calibration: report/ocular disagreement <= .1,
    # report/true-target error <= .1. Union bound controls ocular error.
    delta,reference_error,pi=F(1,10),F(1,10),F(1,2)
    total_error_bound=min(F(1),delta+reference_error)
    alpha_plus_beta_bound=total_error_bound/pi # equal class sizes
    assert alpha_plus_beta_bound==F(2,5) and alpha_plus_beta_bound<1

    # Synthetic deterministic rival outcome, accurate assay in each arm.
    # q_H_D <= .2; q_H_M >= .8. iid draws and majority decision.
    p=F(1,5); eps=F(1,40)
    n=next(n for n in range(1,1000,2) if majority_error(n,p)<=eps)
    assert n==9 and majority_error(7,p)>eps
    iid_error=majority_error(n,p)
    assert iid_error==F(7649,390625)

    # Perfectly correlated repetitions: common Z is Bernoulli(.2) or (.8).
    # Marginal accuracy is unchanged, but all outcomes replicate one Z.
    shared_error=p
    assert shared_error>iid_error
    data={'status':'passed',
          'agreement_counterexample':{'overall_agreement':str(accuracy),'target_prevalence':str(prevalence),
              'false_positive':str(fp),'false_negative':str(fn)},
          'hypothetical_balanced_calibration':{'ocular_report_disagreement_max':str(delta),
              'reference_target_error_max':str(reference_error),'prevalence':str(pi),
              'ocular_total_error_max':str(total_error_bound),'false_positive_plus_false_negative_max':str(alpha_plus_beta_bound)},
          'iid_majority_example':{'class_error_bounds':'1/5 each','per_arm_error_target':'1/40',
              'smallest_odd_n':n,'each_worst_case_error_exact':str(iid_error),'each_worst_case_error_float':float(iid_error)},
          'shared_error_example':{'any_n_majority_error':str(shared_error)},
          'limitations':'All numeric calibration/independence assumptions are hypothetical; neither true target errors nor intervention validity have been measured.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__':main()
