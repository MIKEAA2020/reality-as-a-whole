#!/usr/bin/env python3
"""Q1 Gram-matrix agreement bound; analytic controls and finite checks only."""
from pathlib import Path
import json
import math
import numpy as np
from robust_quantum_agreement_bound import metrics, one_projector, random_state

ROOT = Path(__file__).resolve().parents[1]
TOL = 5e-10


def bound(p,s,e,t):
    return (0.5*math.sqrt(max(0,e))+math.sqrt(min(p,s)*max(0,t))+0.5*abs(p-s))/max(p,s)


def saturation():
    phi=np.array([1.,0,0,1])/math.sqrt(2)
    rho=np.outer(phi,phi)
    proj=lambda v: np.outer(v,v)
    zero=proj(np.array([1.,0]))
    rows=[]
    for theta in (0.0,0.01,0.1,math.pi/6,math.pi/4):
        va=np.array([math.cos(math.pi/4-theta/2),math.sin(math.pi/4-theta/2)])
        vb=np.array([math.cos(math.pi/4+theta/2),math.sin(math.pi/4+theta/2)])
        r=metrics(rho,proj(va),zero,proj(vb),zero)
        rhs=bound(r['p'],r['s'],r['e'],r['t'])
        assert abs(r['p']-.5)<TOL and abs(r['s']-.5)<TOL and abs(r['t'])<TOL
        assert abs(r['e']-math.sin(theta)**2)<TOL
        assert abs(r['q_A']-(1+math.sin(theta))/2)<TOL
        assert abs(r['q_B']-(1-math.sin(theta))/2)<TOL
        assert abs(r['absolute_gap']-rhs)<TOL
        selected_joint=(r['p']+r['s']-r['e'])/2
        assert abs(selected_joint-(1-r['e'])/2)<TOL and selected_joint>0
        if theta>0:
            # Both selected singleton sets survive the stipulated >= 1-e recursion.
            assert abs(selected_joint/r['p']-(1-r['e']))<TOL
            assert abs(selected_joint/r['s']-(1-r['e']))<TOL
            assert abs(r['q_A']-(1-r['q_B']))<TOL
            assert abs(r['q_A']-r['q_B'])>TOL
        rows.append({'theta':theta,'e':r['e'],'q_A':r['q_A'],'q_B':r['q_B'],
                     'gap':r['absolute_gap'],'selected_joint':selected_joint,
                     'centered_bound':rhs})
    return rows


def q1_postquantum_control():
    # Unit Gram vectors of identity and four +/-1 observables.
    # This Q1 completion is explicit; nonquantumness follows separately from
    # the standard CHSH rigidity theorem, not from this numerical PSD check.
    d=0.1
    h=np.array([d,0,math.sqrt(1-d*d)])
    a0=np.array([1.,0,0]); a1=np.array([0.,1,0])
    b0=(a0+a1)/math.sqrt(2); b1=(a0-a1)/math.sqrt(2)
    obs=[a0,a1,b0,b1]
    vectors=[h]+[(h+x)/2 for x in obs]
    gram=np.array([[np.dot(u,v) for v in vectors] for u in vectors])
    assert np.linalg.eigvalsh(gram).min()>-TOL
    for i in range(1,5): assert abs(gram[i,i]-gram[0,i])<TOL
    marg=[float(np.dot(h,x)) for x in obs]
    c=np.array([[np.dot(a0,b0),np.dot(a0,b1)],
                [np.dot(a1,b0),np.dot(a1,b1)]])
    probabilities=[]
    for x in range(2):
        for y in range(2):
            dist=[]
            for aa in (1,-1):
                for bb in (1,-1):
                    dist.append((1+aa*marg[x]+bb*marg[2+y]+aa*bb*c[x,y])/4)
            assert min(dist)>0 and abs(sum(dist)-1)<TOL
            probabilities.extend(dist)
    s=float(c[0,0]+c[0,1]+c[1,0]-c[1,1])
    assert abs(s-2*math.sqrt(2))<TOL and abs(marg[0]-.1)<TOL
    # Select A0=+, B0=+, target A1=+, B1=- (local relabeling).
    p=(1+marg[0])/2; selected_b=(1+marg[2])/2
    e=(1-c[0,0])/2; t=(1+c[1,1])/2
    qa=(1+marg[0]-marg[3]-c[0,1])/(4*p)
    qb=(1+marg[1]+marg[2]+c[1,0])/(4*selected_b)
    q1_bound=bound(p,selected_b,e,t)
    assert abs(qa-qb)<=q1_bound+TOL
    return {'observable_biases_A0_A1_B0_B1':marg,'correlators':c.tolist(),
            'chsh':s,'min_probability':min(probabilities),
            'minimum_gram_eigenvalue':float(np.linalg.eigvalsh(gram).min()),
            'selected_conditional_gap':abs(qa-qb),'selected_q1_bound':q1_bound,
            'qualification':'Q1 PSD completion explicit; nonquantum via cited exact maximal-CHSH self-testing, not numerically proved here'}


def pr_control():
    delta=.2; p=s=.5; e=t=delta/2; gap=1-delta
    rhs=bound(p,s,e,t)
    assert gap>rhs and 4*(1-delta)>2*math.sqrt(2)
    # Box probabilities are nonnegative and normalized; nonsignaling by construction.
    for x in (0,1):
        for y in (0,1):
            ps=[(1-delta)*(.5 if (a^b)==((x*y)^x) else 0)+delta/4
                for a in (0,1) for b in (0,1)]
            assert min(ps)>=0 and abs(sum(ps)-1)<TOL
    return {'noise':delta,'p':p,'s':s,'e':e,'t':t,'gap':gap,'centered_bound':rhs,
            'chsh':4*(1-delta),'violates_necessary_q1_bound':True}


def main():
    rng=np.random.default_rng(129748)
    count=0; max_residual=-10.0
    for na,nb in ((2,2),(2,3),(3,3)):
        for _ in range(1500):
            r=metrics(random_state(na*nb,rng),one_projector(na,rng),one_projector(na,rng),
                      one_projector(nb,rng),one_projector(nb,rng))
            rhs=bound(r['p'],r['s'],r['e'],r['t'])
            residual=r['absolute_gap']-rhs
            max_residual=max(max_residual,residual)
            assert residual<TOL
            count+=1
    out={'status':'passed','scope':'synthetic finite checks; Q1 theorem is analytic, not certified by randomized testing',
         'random_seed':129748,'random_quantum_cases':count,
         'max_random_gap_minus_bound':max_residual,'saturation_cases':saturation(),
         'explicit_q1_nonquantum_control':q1_postquantum_control(),
         'noisy_pr_outside_q1_control':pr_control()}
    (ROOT/'verification/q1_agreement_stability_gate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
