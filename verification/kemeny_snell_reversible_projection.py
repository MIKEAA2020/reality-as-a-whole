#!/usr/bin/env python3
"""Apply Kemeny-Snell 6.4.8 to the established finite heat-bath model."""
from fractions import Fraction as F
from pathlib import Path
import json
from coupled_subject_boundary_gate import STATES,stationary
from integrated_subject_horizon_audit import kernel
from integrated_subject_context_dynamics import project,maximal_discrepancy
from chalmers_structural_alternatives import any_q,max_discrepancy


def mm(a,b):
    assert len(a[0])==len(b)
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]

def powm(a,n):
    r=[[F(int(i==j)) for j in range(len(a))] for i in range(len(a))]
    for _ in range(n):r=mm(r,a)
    return r

def stationary_projected(p,pi,labels):
    classes=sorted(set(labels)); n=len(p)
    masses=[sum((pi[i] for i in range(n) if labels[i]==a),F(0)) for a in classes]
    assert all(x>0 for x in masses)
    def project(matrix):
        return [[sum((pi[i]*matrix[i][j] for i in range(n) for j in range(n) if labels[i]==a and labels[j]==b),F(0))/masses[h]
                 for b in classes] for h,a in enumerate(classes)]
    q=project(p);r=project(mm(p,p));q2=mm(q,q)
    gaps=[(abs(r[i][j]-q2[i][j]),i,j) for i in range(len(classes)) for j in range(len(classes))]
    d,i,j=max(gaps)
    return {'blocks':len(classes),'max_block_gap':str(d),'gap_source':classes[i],'gap_destination':classes[j],
            'actual_two_step':str(r[i][j]),'square_one_step':str(q2[i][j])}

def is_balanced(p,pi):
    return all(pi[i]*p[i][j]==pi[j]*p[j][i] for i in range(len(p)) for j in range(len(p)))

def regular_power(p,maxpower=12):
    for n in range(1,maxpower+1):
        if all(x>0 for row in powm(p,n) for x in row):return n
    return None

def book_example():
    p=[[F(1,4),F(1,4),F(1,2)], [F(0),F(1,6),F(5,6)], [F(7,8),F(1,8),F(0)]]
    pi=[F(7,16),F(3,16),F(3,8)]; labels=[0,1,1]
    assert all(sum(row)==1 and min(row)>=0 for row in p)
    assert all(sum(pi[i]*p[i][j] for i in range(3))==pi[j] for j in range(3))
    assert not is_balanced(p,pi)
    assert p[1][0]!=p[2][0]
    # Every observed singleton or {1,2} block leaves a unique conditional fine
    # distribution; multiplying by P and conditioning preserves this property.
    conditionals=[[F(1),F(0),F(0)],[F(0),F(1,3),F(2,3)]]
    for a in conditionals:
        new=mm([a],p)[0]
        for b,c in enumerate(conditionals):
            indices=[i for i,x in enumerate(labels) if x==b]; mass=sum(new[i] for i in indices)
            assert mass>0
            assert [new[i]/mass if i in indices else F(0) for i in range(3)]==c
    assert regular_power(p) is not None
    return {'matrix':[[str(x) for x in row] for row in p],'stationary':[str(x) for x in pi],
            'regular_power':regular_power(p),'reversible':False,
            'unequal_destination_singleton_probabilities':[str(p[1][0]),str(p[2][0])],
            'stationary_block_conditionals_preserved':True,
            'stationary_two_step':stationary_projected(p,pi,labels)}

def run():
    k=kernel(F(1,4));pi_map=stationary(F(1,4),(None,)*4);pi=[pi_map[s] for s in STATES]
    p=[[k[s].get(u,F(0)) for u in STATES] for s in STATES]
    assert all(sum(row)==1 and all(x>=0 for x in row) for row in p)
    assert all(x>0 for x in pi) and sum(pi)==1
    assert all(sum((pi[i]*p[i][j] for i in range(len(p))),F(0))==pi[j] for j in range(len(p)))
    assert is_balanced(p,pi)
    assert all(x>0 for row in powm(p,4) for x in row)
    expected={'pair_state':F(1,21),'left_q':F(1,21),'left_middle_q':F(5,42),
              'left_right_q':F(2,21),'edge_qs':F(0),'any_mismatch':F(5,24)}
    output={}
    for name in expected:
        f=any_q if name=='any_mismatch' else lambda s,n=name:project(s,n)
        d=max_discrepancy(k,f)
        if name!='any_mismatch':assert d==maximal_discrepancy(k,name)[0]
        assert d==expected[name]
        stat=stationary_projected(p,pi,[f(s) for s in STATES])
        assert (F(stat['max_block_gap'])==0)==(d==0)
        output[name]={'maximum_strong_block_tv':str(d),
                      'homogeneous_markov_for_some_initial_distribution':'yes' if d==0 else 'no',
                      'verdict_basis':'Kemeny-Snell 6.3.2 and 6.4.8 after regularity/reversibility checks',
                      'stationary_Q2_vs_actual_two_step':stat}
    return {'model':'four-spin random-site heat-bath at t=1/4',
            'assumptions':{'positive_stationary_distribution':True,'row_stochastic':True,'stationary':True,
                           'detailed_balance_all_state_pairs':True,'p4_all_entries_positive':True},
            'projections':output,'book_nonreversible_example_6_4_2':book_example(),
            'scope':'exact finite physical model; homogeneous first-order Markovity, not approximate/inhomogeneous models, subjects, felt qualities or quantum gravity'}

def main():
    text=json.dumps(run(),indent=2)+'\n';Path(__file__).with_suffix('.json').write_text(text);print(text)
if __name__=='__main__':main()
