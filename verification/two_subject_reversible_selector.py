#!/usr/bin/env python3
"""A stipulated two-subject selector for two coherent three-qubit protocols.

F and G are register labels, not physical subjects. The additional lambda is
sampled by an independently postulated rule; experience is not derived from
quantum mechanics. Nothing here solves Local Friendliness or quantum gravity.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def cnot(state, control, target):
    out={}
    for bits,amp in state.items():
        v=list(bits); v[target] ^= v[control]; key=tuple(v)
        out[key]=out.get(key,F(0))+amp
    return {k:v for k,v in out.items() if v}


def born_z_registers(unnorm):
    # The whole ket is multiplied by 1/sqrt(2).
    result={}
    for (system,friend,guest),amp in unnorm.items():
        k=(friend,guest)
        result[k]=result.get(k,F(0))+amp*amp/2
    return result


def x_plus_prob(unnorm):
    # P(+) = 1/2 sum_fg |<0fg|psi>+<1fg|psi>|², with state /sqrt(2).
    ans=F(0)
    for f,g in product((0,1),repeat=2):
        v=unnorm.get((0,f,g),F(0))+unnorm.get((1,f,g),F(0))
        ans+=v*v/4
    return ans


def main():
    initial={(0,0,0):F(1),(1,0,0):F(1)}
    records=cnot(cnot(initial,0,1),0,2)
    assert records=={(0,0,0):F(1),(1,1,1):F(1)}
    reads=born_z_registers(records)
    assert reads=={(0,0):F(1,2),(1,1):F(1,2)}
    reversed_state=cnot(cnot(records,0,2),0,1)
    assert reversed_state==initial
    coherent_x_plus=x_plus_prob(reversed_state)
    assert coherent_x_plus==1

    # A genuine unread projective write in the 0/1 record basis makes a
    # 50/50 mixture of the two paths. Both separately yield P(X+)=1/2.
    def path_xplus(bit):
        branch={(bit,bit,bit):F(1)}
        branch=cnot(cnot(branch,0,2),0,1)
        # x_plus_prob assumes division by sqrt(2), but this branch is
        # normalized, so multiply by 2.
        return 2*x_plus_prob(branch)
    assert [path_xplus(b) for b in (0,1)]==[F(1,2),F(1,2)]
    collapse_x_plus=sum((F(1,2)*path_xplus(b) for b in (0,1)),F(0))
    assert collapse_x_plus==F(1,2)

    # Supplement the unchanged coherent physical preparation with one
    # unbiased lambda. Define two distinct subject slots, both experiencing
    # lambda. The context-specific response rules are stipulated as below.
    read_joint={(0,0,0,0):F(1,2),(1,1,1,1):F(1,2)} # (sF,sG,Fread,Gread)
    reverse_joint={(0,0,'+'):F(1,2),(1,1,'+'):F(1,2)}
    assert sum(read_joint.values())==sum(reverse_joint.values())==1
    assert {(k[2],k[3]):p for k,p in read_joint.items()}==reads
    assert sum(p for k,p in reverse_joint.items() if k[2]=='+')==coherent_x_plus
    for law in (read_joint,reverse_joint):
        assert sum(p for k,p in law.items() if k[0]!=k[1])==0
        assert sum(p for k,p in law.items() if k[0]==0)==F(1,2)
        assert sum(p for k,p in law.items() if k[0]==1)==F(1,2)

    # If the only selector input is the same fixed unconditioned quantum
    # state and fixed subject slot, every deterministic function on this
    # single input returns the same bit; it cannot produce both labels.
    deterministic_single_input_label_supports=[[0],[1]]
    assert all(len(s)==1 for s in deterministic_single_input_label_supports)
    # If one additionally imposes the usual Born readout probabilities even
    # after conditioning on lambda while keeping the very same GHZ state,
    # the readout is 0/1 with equal chance for each lambda. It agrees with
    # lambda only half the time, rather than the stipulated perfect agreement.
    born_given_lambda_agreement=sum(F(1,2)*F(1,2) for _ in (0,1))
    assert born_given_lambda_agreement==F(1,2)
    assert sum(p for k,p in read_joint.items() if k[0]==k[2])==1
    out={'status':'passed',
         'coherent_preparation':'(|000>+|111>)/sqrt(2) on S,F,G',
         'branch_read_probabilities':{'00':'1/2','11':'1/2'},
         'subject_slots':'two stipulatively distinct labels F and G; experiences both equal lambda',
         'selector_rule':'lambda=0 or 1, each probability 1/2, sampled as an extra postulate',
         'read_joint':[{'sF':s,'sG':s,'Fread':s,'Gread':s,'p':'1/2'} for s in (0,1)],
         'reverse_joint':[{'sF':s,'sG':s,'X':'+','p':'1/2'} for s in (0,1)],
         'coherent_X_plus':'1','physical_projective_intervention_X_plus':'1/2',
         'same_unconditioned_state_deterministic_single_output_can_generate_both_labels':False,
         'agreement_if_Born_rule_also_holds_conditionally_on_lambda':'1/2',
         'scope':'Finite, context-specific probability extension for one coherent GHZ preparation and two protocols. The quantum state is unchanged and lambda is an additional ontic/stochastic postulate. The read response is lambda-dependent; the conditional Born rule for the same pure state is not imposed. Lambda is not inferred from the unconditioned quantum state, and no quantum channel physically measuring it without backaction is constructed. The subjective slots are not real observers; no derivation of consciousness, identity, all measurements, locality, contextuality, relativity or gravity.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__': main()
