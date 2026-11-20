#!/usr/bin/env python3
"""Eraser/Bell checks plus explicit setting-independent lossy local model.

Finite model checks only; no claims about real subject selection or experiments.
Requires NumPy, already used elsewhere in the framework battery.
"""
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import numpy as np

I = np.eye(2, dtype=complex)
X = np.array([[0,1],[1,0]], complex)
Y = np.array([[0,-1j],[1j,0]], complex)
Z = np.diag([1,-1]).astype(complex)
kron = np.kron

def prob(rho, pa, pb):
    z = np.trace(rho @ kron(pa,pb))
    assert abs(z.imag) < 1e-12
    return float(z.real)

def projector(observable, value):
    return (I + value*observable)/2

def exp(rho, a, b):
    result = np.trace(rho @ kron(a,b))
    assert abs(result.imag) < 1e-12
    return float(result.real)

def state_overlap_example():
    # Balanced path A and normalized pure marker states B with overlap 3/5.
    vec = np.array([1,0,F(3,5),F(4,5)], dtype=float)/np.sqrt(2)
    rho = np.outer(vec,vec)
    vis=[]
    for phase in np.linspace(0,2*np.pi,25):
        obs = np.cos(phase)*X + np.sin(phase)*Y
        vis.append(sum(prob(rho,projector(obs,1),projector(Z,b)) for b in [-1,1]))
    assert np.isclose(max(vis),0.8) and np.isclose(min(vis),0.2)
    return {'overlap':'3/5','fringe_visibility':'3/5'}

def quantum_checks(v):
    # rho = (|00><00| + |11><11| + v|00><11| + v|11><00|)/2.
    rho=np.zeros((4,4),complex)
    rho[0,0]=rho[3,3]=0.5
    rho[0,3]=rho[3,0]=v/2
    assert np.linalg.eigvalsh(rho).min()>-1e-12
    assert np.isclose(np.trace(rho),1)
    for theta in np.linspace(0,2*np.pi,25):
        aobs = np.cos(theta)*X + np.sin(theta)*Y
        # Compare a coherent complementary read, a which-way read and ignored B.
        for a in [-1,1]:
            for bobs in [X,Z]:
                assert np.isclose(sum(prob(rho,projector(aobs,a),projector(bobs,b)) for b in [-1,1]),0.5)
            for b in [-1,1]:
                assert np.isclose(prob(rho,projector(aobs,a),projector(X,b)),(1+a*b*v*np.cos(theta))/4)
                assert np.isclose(prob(rho,projector(aobs,a),projector(Z,b)),0.25)
    # Same state, optimizing these particular Z/X-family settings.
    norm=np.sqrt(1+v*v)
    b0=(Z+v*X)/norm
    b1=(Z-v*X)/norm
    e=[exp(rho,Z,b0), exp(rho,Z,b1), exp(rho,X,b0), exp(rho,X,b1)]
    s=e[0]+e[1]+e[2]-e[3]
    assert np.isclose(s,2*norm)
    # Physically unread Z measurement on B dephases the AB state.
    rho_dephased=sum(kron(I,projector(Z,b))@rho@kron(I,projector(Z,b)) for b in [-1,1])
    assert np.isclose(exp(rho_dephased,X,X),0)
    assert np.isclose(exp(rho_dephased,Z,Z),1)
    assert np.isclose(exp(rho_dephased,Z,b0)+exp(rho_dephased,Z,b1)+exp(rho_dephased,X,b0)-exp(rho_dephased,X,b1),2/norm)
    return {'v':v,'conditional_visibility':v,'unconditional_visibility':0,'s_optimized':s,'s_after_dephasing_same_settings':2/norm}

def local_filter_model():
    # Four setting pairs and eight equally weighted lambda=(u,v,r). The
    # 32 rows are actual occurrences in this stipulated finite table.
    counts={}
    for x,y in product(range(2),repeat=2):
        records=[]
        for u,v,r in product(range(2),repeat=3):
            sign=(-1)**r
            # A can use only x,u,r; B only y,v,u,r (all are in lambda).
            a=sign if x==u else 0
            b=sign*((-1)**(u*v)) if y==v else 0
            records.append((u,v,r,a,b))
        counts[x,y]=records
    # Same hidden-variable distribution in all setting classes.
    baseline={(u,v,r) for u,v,r,_,_ in counts[0,0]}
    for records in counts.values():
        assert {(u,v,r) for u,v,r,_,_ in records}==baseline
        assert sum(a!=0 for _,_,_,a,b in records)==4
        assert sum(b!=0 for _,_,_,a,b in records)==4
        assert sum(a!=0 and b!=0 for _,_,_,a,b in records)==2
    corr=[]; filled=[]; marg=[]
    for x,y in product(range(2),repeat=2):
        records=counts[x,y]
        valid=[(a,b) for _,_,_,a,b in records if a and b]
        corr.append(F(sum(a*b for a,b in valid),len(valid)))
        # Include every row by assigning +1 to non-detections.
        filled.append(F(sum((a or 1)*(b or 1) for _,_,_,a,b in records),8))
        marg.append([sum(a==1 for a,b in valid),sum(a==-1 for a,b in valid),sum(b==1 for a,b in valid),sum(b==-1 for a,b in valid)])
        assert marg[-1]==[1,1,1,1]
    s=corr[0]+corr[1]+corr[2]-corr[3]
    all_s=filled[0]+filled[1]+filled[2]-filled[3]
    assert s==4 and abs(all_s)<=2
    # TV distance of each selected hidden-variable law to the uniform
    # preselection reference. Supports for different settings are disjoint.
    selected=[]
    for records in counts.values():
        support={(u,v,r) for u,v,r,a,b in records if a and b}
        selected.append(support)
    assert all(len(support)==2 for support in selected)
    assert all(not selected[i].intersection(selected[j]) for i in range(4) for j in range(i))
    distances=[sum(abs((F(1,2) if key in support else F(0))-F(1,8)) for key in baseline)/2 for support in selected]
    assert distances==[F(3,4)]*4
    assert abs(s)<=2+2*sum(distances)
    # Check local complete-output distributions, including no-click, are
    # independent of the distant setting, not just the selected marginals.
    for x in range(2):
        assert sorted(a for _,_,_,a,b in counts[x,0])==sorted(a for _,_,_,a,b in counts[x,1])
    for y in range(2):
        assert sorted(b for _,_,_,a,b in counts[0,y])==sorted(b for _,_,_,a,b in counts[1,y])
    return {'actual_table_rows':32,'hidden_variables_per_setting':8,
            'local_detection_efficiency_each':'1/2','coincidence_rate':'1/4',
            'postselected_correlations':[str(z) for z in corr],
            'postselected_CHSH':str(s),'postselected_marginals_balanced':True,
            'all_trial_plus_fill_correlations':[str(z) for z in filled],
            'all_trial_plus_fill_CHSH':str(all_s),
            'preselection_setting_independence':True,
            'setting_independence_after_coincidence':False,
            'TV_to_uniform_reference_each':[str(d) for d in distances],
            'selection_TV_bound_checked':True,
            'full_no_click_marginals_nonsignalling':True}

def quantum_bell_mimic():
    # Fixed v=3/5, Bob settings (3Z +/- 4X)/5. Locally selected
    # guess u,v sets the desired joint distribution; all 400 lambda values
    # occur identically in every setting class before selection.
    correlations=[]
    for x,y in product(range(2),repeat=2):
        valid=[]
        for u,v,r,k in product(range(2),range(2),range(2),range(50)):
            a=(-1)**r if x==u else 0
            threshold=40 if u==0 else 37
            b=((-1)**r)*(1 if k<threshold else -1)*((-1)**(u*v)) if y==v else 0
            if a and b:
                valid.append((a,b))
        assert len(valid)==100
        assert sum(a for a,b in valid)==sum(b for a,b in valid)==0
        correlation=F(sum(a*b for a,b in valid),len(valid))
        for a,b in product((-1,1),repeat=2):
            assert F(valid.count((a,b)),len(valid))==(1+a*b*correlation)/4
        correlations.append(correlation)
    assert correlations==[F(3,5),F(3,5),F(12,25),F(-12,25)]
    s=correlations[0]+correlations[1]+correlations[2]-correlations[3]
    assert s==F(54,25)
    # Independently compare the unconditioned quantum Born correlators.
    rho=np.zeros((4,4),complex)
    rho[0,0]=rho[3,3]=0.5; rho[0,3]=rho[3,0]=0.3
    q=[exp(rho,Z,(3*Z+4*X)/5),exp(rho,Z,(3*Z-4*X)/5),
       exp(rho,X,(3*Z+4*X)/5),exp(rho,X,(3*Z-4*X)/5)]
    assert all(np.isclose(a,float(b)) for a,b in zip(q,correlations))
    return {'rows':1600,'coincidence_rate_each_setting':'1/4',
            'selected_correlations':[str(c) for c in correlations],
            'selected_CHSH':str(s),'balanced_marginals':True,
            'matches_entire_quantum_joint_distribution_for_four_fixed_settings':True,
            'scope':'local low-efficiency selection model; does not match no-click statistics or demonstrate fair-sampling Bell violation'}

cases=[quantum_checks(v/20) for v in range(21)]
result={'status':'passed','pure_marker_example':state_overlap_example(),
        'quantum_family_cases':len(cases), 'example_v_3_over_5':cases[12],
        'lossy_local_model':local_filter_model(),
        'fixed_quantum_correlations_mimic':quantum_bell_mimic(),
        'scope':'finite model: no experiment, subject identification, metaphysical measure, general theorem or loophole-free data reanalysis'}
output=json.dumps(result,indent=2)+'\n'
Path(__file__).with_suffix('.json').write_text(output)
print(output)
