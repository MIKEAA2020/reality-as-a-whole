#!/usr/bin/env python3
"""Exact finite causal countermodels; no observed or simulated animal data."""
from fractions import Fraction as F
from pathlib import Path
import json

# X and S are set experimentally. U is background; N is assay error.
# Q is a hypothetical binary microtubule quantum-state feature, C a classical
# pathway, M a noisy Q assay, Y a behavioral proxy. All are toy binary values.

def distribution(model, x, s, do_q=None):
    counts = {(m,y): F(0) for m in (0,1) for y in (0,1)}
    for u, pu in ((0,F(3,4)),(1,F(1,4))):
        for n, pn in ((0,F(9,10)),(1,F(1,10))):
            c = x ^ u ^ (s if model == 'shadow' else 0)
            q = x ^ u ^ s if do_q is None else do_q
            y = q if model == 'quantum' else c
            m = q ^ n
            counts[m,y] += pu*pn
    assert sum(counts.values()) == 1
    return counts


def mean_y(dist):
    return sum(p*y for (m,y),p in dist.items())


def serial(dist):
    return {f'M={m},Y={y}':str(dist[m,y]) for m in (0,1) for y in (0,1)}


def main():
    # Existing arm S=0 gives exactly the same joint observed records.
    for x in (0,1):
        assert distribution('quantum',x,0)==distribution('classical',x,0)
        assert distribution('quantum',x,0)==distribution('shadow',x,0)
    # Selective S breaks the first alternative, but not the shadow pathway.
    for x in (0,1):
        for s in (0,1):
            assert distribution('quantum',x,s)==distribution('shadow',x,s)
    assert mean_y(distribution('quantum',0,1))-mean_y(distribution('quantum',0,0))==F(1,2)
    assert mean_y(distribution('classical',0,1))-mean_y(distribution('classical',0,0))==0
    assert mean_y(distribution('quantum',1,1))-mean_y(distribution('quantum',1,0))==-F(1,2)
    # Intervening directly on Q changes only the quantum model's Y.
    interventions={}
    for model in ('quantum','classical','shadow'):
        means=[mean_y(distribution(model,0,0,do_q=q)) for q in (0,1)]
        effect=means[1]-means[0]
        assert effect == (1 if model=='quantum' else 0)
        interventions[model]={'E_Y_do_Q0':str(means[0]),'E_Y_do_Q1':str(means[1]),'contrast':str(effect)}
    # Conditional sensitivity example, not a fitted or observed effect.
    dy, eps, qlo, qhi = F(2,25), F(1,50), F(1,5), F(2,5)
    theta_lo, theta_hi = (dy-eps)/qhi, (dy+eps)/qlo
    assert (theta_lo, theta_hi) == (F(3,20), F(1,2))
    tables={model:{f'X={x},S={s}':serial(distribution(model,x,s))
                   for x in (0,1) for s in (0,1)}
            for model in ('quantum','classical','shadow')}
    out={'scope':'Exact finite mathematical countermodels, not experimental results or a physical brain model.',
         'background':{'P_U1':'1/4','P_assay_flip':'1/10'},
         'table_columns':'noisy hypothetical quantum assay M and behavioral outcome Y',
         'observed_joint_distributions':tables,
         'conditional_sensitivity_example':{'delta_Y':'2/25','unmeasured_bypass_bound':'1/50',
             'delta_Q_interval':['1/5','2/5'],'theta_interval':[str(theta_lo),str(theta_hi)],
             'scope':'Assumes common additive coefficient and valid bypass/assay bounds; illustrative values only.'},
         'selective_S_contrast_at_X0':{'quantum':'1/2','classical':'0','shadow':'1/2'},
         'ideal_do_Q_contrasts_at_X0_S0':interventions,
         'checks':{'existing_arm_joint_equality':True,'quantum_shadow_all_arms_equal':True,
                   'direct_Q_interventions_differ':True}}
    text=json.dumps(out,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text,encoding='utf-8')
    print(text)


if __name__=='__main__': main()
