#!/usr/bin/env python3
"""Bound conditional state-mismatch differences from sampled net responses.
No human data; no inference that a physical response is a pain/experience assay.
"""
import json
import math
import random
from pathlib import Path

PI=math.pi
ROOT=Path(__file__).resolve().parent.parent


def midpoints(n):
    return [(j+0.5)/n for j in range(n)]


def midpoint(f,n):
    return sum(f(x) for x in midpoints(n))/n


def fourier_integral(a,b):
    # q(s) = sum_h a_h sin(pi*h*s) + b_h cos(pi*h*s).
    return sum(ah*(1-(-1)**h)/(PI*h) for h,ah in enumerate(a,1))


def main():
    n=32; beta=.1; lipschitz=PI**2
    err=beta+lipschitz/(4*n)
    examples={}
    for k in (0.0,2.0):
        # gamma(s)=pi*s. q = dE/ds; D(A)-D(B)=-integral q.
        q=lambda s: PI*(k-1)*math.sin(PI*s)
        m=midpoint(q,n); estimate=-m
        actual=2*(1-k)
        assert abs(estimate-actual)<=err
        examples[str(k)]={'exact_D_A_minus_D_B':actual,'midpoint_estimate':estimate,
                          'interval':[estimate-err,estimate+err]}
    assert examples['0.0']['interval'][0]>0
    assert examples['2.0']['interval'][1]<0

    # Smooth globally periodic phase potential, yet zero response at every
    # sampled midpoint AND both endpoints; no finite-sample inference without
    # an independently bounded between-sample variation.
    amplitude=100.0
    alias=lambda s: amplitude*math.sin(PI*s)*math.cos(n*PI*s)**2
    alias_int=amplitude/PI*(1+1/(1-4*n*n))
    assert max(abs(alias(s)) for s in midpoints(n))<1e-20
    assert abs(alias(0))<1e-12 and abs(alias(1))<1e-12
    # Check exact integral against a much finer midpoint rule.
    assert abs(midpoint(alias,30000)-alias_int)<1e-5

    # Both alternatives have the same q samples and endpoint forces.
    # q(s) is periodic with period 2 and integral over a period is zero,
    # so it is derivative of a periodic scalar phase potential.
    assert abs(midpoint(alias,30000)+midpoint(lambda s:alias(s+1),30000))<1e-10

    # A local gradient on a circle can have nonzero global period.
    torque=0.7
    q_positive_path=PI*torque
    q_negative_path=-PI*torque
    circulation=q_positive_path-q_negative_path
    assert abs(circulation-2*PI*torque)<1e-12

    # Hidden states at fixed temperature: E(x,0)=0 and
    # E(x,1)=1-cos(x). Mean-force free energy shift differs from E(x,0).
    microscopic_h0_difference=0.0
    mean_force_difference=math.log(2/(1+math.exp(-2)))
    assert mean_force_difference>0

    rng=random.Random(251103)
    for case in range(15000):
        a=[rng.uniform(-2,2) for _ in range(5)]
        b=[rng.uniform(-2,2) for _ in range(5)]
        q=lambda s: sum(ah*math.sin(h*PI*s)+bh*math.cos(h*PI*s)
                        for h,(ah,bh) in enumerate(zip(a,b),1))
        l=PI*sum(h*(abs(ah)+abs(bh)) for h,(ah,bh) in enumerate(zip(a,b),1))
        count=rng.randint(2,100)
        true=fourier_integral(a,b)
        noise=[rng.uniform(-beta,beta) for _ in range(count)]
        sample=sum(q(s)+e for s,e in zip(midpoints(count),noise))/count
        bound=beta+l/(4*count)
        assert abs(sample-true)<=bound+1e-12, (case,sample,true,bound)
    receipt={'status':'completed',
      'scope':'ideal scalar potential and deterministic error bounds; no neural data or phenomenal-assay validation',
      'midpoint_example':{'n':n,'beta':beta,'lipschitz':lipschitz,'error_radius':err,'models':examples},
      'unsampled_periodic_alias':{'n':n,'amplitude':amplitude,'midpoint_average':midpoint(alias,n),
             'endpoints':[alias(0),alias(1)],'exact_integral':alias_int,
             'note':'This alias is not claimed to satisfy the illustrative pi-squared Lipschitz bound.'},
      'circle_nonconservative_torque':{'torque':torque,'positive_path_integral':q_positive_path,
             'negative_path_integral':q_negative_path,'closed_loop_integral':circulation},
      'hidden_equilibrium_modes':{'beta_inverse_temperature':1,'c':1,
             'microscopic_h0_energy_difference':microscopic_h0_difference,
             'free_energy_difference':mean_force_difference},
      'random_fourier_interval_checks':15000,'random_seed':251103,
      'note':'Finite tests exercise implementation, not physical or experiential assumptions.'}
    (ROOT/'verification/net_work_mismatch_gate.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':main()
