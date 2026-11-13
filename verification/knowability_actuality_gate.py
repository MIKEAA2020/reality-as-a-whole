#!/usr/bin/env python3
"""Finite checks for relational knowability scope; not a metaphysical decision."""
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def powerset_mask(n):
    return range(1 << n)


def image_exists(rows, p, n):
    return sum((1 << w) for w in range(n) if rows[w] & p)


def knows(rows, knowers, p, n):
    full = (1 << n) - 1
    return sum(1 << w for w in range(n)
               if knowers & (1 << w) and not (rows[w] & (full ^ p)))


def main():
    # Exhaust every 2-point modal/epistemic relation, including non-reflexive
    # relations, all assignments of the existence of a knower, and all events.
    n=2; full=(1 << n)-1
    cases=0; relevant=0; factive_cases=0; full_fitch_models=0
    for rm in product(powerset_mask(n), repeat=n):
        for rk in product(powerset_mask(n), repeat=n):
            for knowers in powerset_mask(n):
                k=[knows(rk,knowers,p,n) for p in powerset_mask(n)]
                for w in range(n):
                    bit=1 << w
                    for p in powerset_mask(n):
                        # The bridge uses the actuality schema only for Kp.
                        kp=k[p]; poss_kp=image_exists(rm,kp,n)
                        kp_axiom=not (p & bit) or bool(poss_kp & bit)
                        collapse_instance=not (poss_kp & bit) or bool(kp & bit)
                        if kp_axiom and collapse_instance:
                            relevant+=1
                            assert not (p & bit) or bool(kp & bit)
                        cases+=1
                    if all((rk[v] & (1 << v)) for v in range(n)):
                        # Fitch only at w; possible knowers must be factive
                        # throughout the modal accessible set, assured here.
                        factive_cases+=1
                        unrestricted=all(not (p & bit) or
                           bool(image_exists(rm,k[p],n) & bit) for p in powerset_mask(n))
                        if unrestricted:
                            full_fitch_models+=1
                            assert all(not (p & bit) or bool(k[p] & bit)
                                       for p in powerset_mask(n))
    # 3-point restricted-KP countermodel; 0 is actual, 1 knower, 2 p-false.
    n=3; rm=(7,7,7); rk=(5,2,4); exist=2; experience=2; p=3; top=7; bit=1
    kp=knows(rk,exist,p,n); ktop=knows(rk,exist,top,n)
    moore=p & (7 ^ kp)
    kmoore=knows(rk,exist,moore,n)
    posskp=image_exists(rm,kp,n); posstop=image_exists(rm,ktop,n)
    assert p & bit and not kp & bit and posskp & bit and posstop & bit
    assert not exist & bit and not experience & bit and not kmoore and moore & bit
    assert not (kp & (7 ^ experience)) and not (ktop & (7 ^ experience))
    assert not image_exists(rm,kmoore,n) & bit
    # Strong schema holds for no-experience one-point model, but knowability
    # of a tautology fails there. No knower-existence is smuggled into K.
    empty_k=knows((1,),0,1,1)
    assert empty_k==0 and image_exists((1,),empty_k,1)==0
    out={'scope':'Finite extensional Kripke-style controls, not justification of knowability, phenomenality, possibility or concrete reality.',
         'two_point_cases': cases,'direct_bridge_premise_cases':relevant,
         'factive_two_point_designated_models':factive_cases,
         'unrestricted_factive_fitch_models':full_fitch_models,
         'restricted_three_point':{'modal_rows_bitmask':list(rm),'epistemic_rows_bitmask':list(rk),
             'knower_existence_mask':exist,'experience_mask':experience,'p_mask':p,'actual_point':0,
             'Kp_mask':kp,'K_top_mask':ktop,'p_and_not_Kp_mask':moore,
             'K_p_and_not_Kp_mask':kmoore,'p_true_and_unknown':True,
             'p_and_tautology_knowable':True,'actual_knower_and_experience_absent':True},
         'empty_knower_one_point':{'strong_schema_holds':True,'tautology_knowable':False}}
    text=json.dumps(out,indent=2)+'\n'; (ROOT/'verification/knowability_actuality_gate.json').write_text(text); print(text)


if __name__=='__main__': main()
