#!/usr/bin/env python3
"""Reproduce a published agreement example and check a partial-record extension.
The numerical checks are not a general proof, a consciousness assay, or an experiment.
"""
import json
import math
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent.parent
TOL=2e-11


def ket(n,i):
    x=np.zeros(n,dtype=complex);x[i]=1;return x


def outer(a,b):return np.outer(a,b.conj())
def kron(*args):
    result=np.array([1],dtype=complex)
    for x in args:result=np.kron(result,x)
    return result


def real(x):
    assert abs(np.imag(x))<TOL
    return float(np.real(x))


def probability(rho,obs,projector):
    w=real(np.trace(projector@rho))
    if w<TOL:return None
    return real(np.trace(obs@projector@rho@projector))/w


def certainty_operator(rho,measurements,event):
    z=np.zeros_like(rho)
    for P in measurements:
        p=probability(rho,event,P)
        if p is not None and abs(p-1)<TOL:z+=P
    return z


def estimate_operator(rho,measurements,event,q):
    z=np.zeros_like(rho)
    for P in measurements:
        p=probability(rho,event,P)
        if p is not None and abs(p-q)<TOL:z+=P
    return z


def check_case(t,g):
    # gamma is <r1|r0>, including its phase.
    r0=ket(2,0);r1=np.array([g.conjugate(),math.sqrt(max(0,1-abs(g)**2))],dtype=complex)
    assert abs(np.vdot(r1,r0)-g)<TOL
    u=kron(ket(3,0),ket(2,0),ket(2,0),r0)
    v=kron(ket(3,1),ket(2,0),ket(2,1),r1)
    rho=(outer(u,u)+outer(v,v)+t*outer(u,v)+t*outer(v,u))/2
    I3,I2=np.eye(3),np.eye(2)
    PAs=[kron(outer(ket(3,i),ket(3,i)),I2,I2,I2) for i in range(3)]
    PBs=[kron(I3,outer(ket(2,i),ket(2,i)),I2,I2) for i in range(2)]
    # |phi_AC> = (|00>+|11>+|20>)/sqrt(3), tensored with B,R identity.
    E=np.zeros((24,24),complex)
    for b in range(2):
        for r in range(2):
            phi=sum((kron(ket(3,a),ket(2,b),ket(2,c),ket(2,r))
                     for a,c in ((0,0),(1,1),(2,0))),np.zeros(24,complex))/math.sqrt(3)
            E+=outer(phi,phi)
    assert abs(real(np.trace(rho))-1)<TOL
    assert np.min(np.linalg.eigvalsh(rho))>-TOL
    assert np.linalg.norm(E@E-E)<TOL
    assert all(np.linalg.norm(a@b-b@a)<TOL for a in PAs for b in PBs)
    assert np.linalg.norm(PAs[0]@E-E@PAs[0])>0.1
    assert np.linalg.norm(PBs[0]@E-E@PBs[0])<TOL
    qa=probability(rho,E,PAs[0]);qa1=probability(rho,E,PAs[1]);qb=probability(rho,E,PBs[0])
    expected=(1+t*g.real)/3
    assert abs(qa-1/3)<TOL and abs(qa1-1/3)<TOL and abs(qb-expected)<TOL
    assert probability(rho,E,PAs[2]) is None and probability(rho,E,PBs[1]) is None
    aa=estimate_operator(rho,PAs,E,qa);bb=estimate_operator(rho,PBs,E,qb)
    steps=0
    for _ in range(8):
        an=aa@certainty_operator(rho,PAs,bb)
        bn=bb@certainty_operator(rho,PBs,aa)
        steps+=1
        if np.linalg.norm(an-aa)<TOL and np.linalg.norm(bn-bb)<TOL:break
        aa,bb=an,bn
    else:raise AssertionError('certainty recursion did not converge')
    weight=real(np.trace(aa@bb@rho));assert abs(weight-1)<TOL
    # Helstrom distinguishability of the two pure record states, equal priors.
    delta=outer(r0,r0)-outer(r1,r1)
    d=float(np.linalg.svd(delta,compute_uv=False).sum()/2)
    assert abs(d*d+abs(g)**2-1)<TOL
    assert abs(qb-qa)<=t*math.sqrt(max(0,1-d*d))/3+TOL
    # Alice's unread measurement dephases the original system regardless of tag.
    recorded=sum((a@rho@a for a in PAs),np.zeros_like(rho))
    assert abs(probability(recorded,E,PBs[0])-1/3)<TOL
    # Local B statistics do not reveal whether unread Alice measurement occurred.
    assert all(abs(real(np.trace(b@rho))-real(np.trace(b@recorded)))<TOL for b in PBs)
    return {'t':t,'record_overlap':[float(g.real),float(g.imag)],
            'record_distinguishability':round(d,12),
            'alice':round(qa,12),'bob':round(qb,12),
            'gap':round(abs(qb-qa),12),'common_certainty_weight':round(weight,12),
            'certainty_steps_to_fixed_point':steps,
            'bob_after_alice_dephasing':round(probability(recorded,E,PBs[0]),12)}


def main():
    tests=[(t,g) for t in (0.0,0.5,1.0) for g in (0j,0.5+0j,1+0j,0.6j,-0.5+0j)]
    values=[check_case(t,g) for t,g in tests]
    base=next(x for x in values if x['t']==1 and x['record_overlap']==[1.,0.])
    full=next(x for x in values if x['t']==1 and x['record_overlap']==[0.,0.])
    assert abs(base['bob']-2/3)<TOL and abs(base['alice']-1/3)<TOL
    assert abs(full['bob']-1/3)<TOL
    out={'status':'completed','scope':'finite matrix verification of one published model and a partial-record extension; not general proof or phenomenal evidence',
         'preprint':'https://arxiv.org/html/2511.21258v3',
         'system_dimensions':[3,2,2,2],
         'models_checked':len(values),'results':values,
         'assumptions':'equal branch weights, pure normalized record tags, no access to record in the given local update, fixed event and Lueders projectors',
         'verified_operators':['positivity and trace','projective event','measurement commutators','positive-outcome conditional estimates','stabilized common-certainty operators','record overlap/trace distance','dephasing and local Bob marginal']}
    (ROOT/'verification/quantum_agreement_record_gate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'models_checked':len(values),'published_example':base,'orthogonal_record':full},indent=2))

if __name__=='__main__':main()
