"""Small finite semantic checks, not proofs of metaphysical possibility.

All worlds are mutually accessible. Existence bits are phenomenally concrete
subjects; they do not represent brain, spacetime or independently real worlds.
"""
from itertools import product
from pathlib import Path
import json


def main():
    # Columns: existence of subjects a and b at each world.
    vectors=list(product((0,1),repeat=2))
    admissible=[(w0,w1) for w0 in vectors for w1 in vectors
                if any(w0) and any(w1)]
    no_necessary_individual=[pair for pair in admissible
                             if not any(all(w[i] for w in pair) for i in range(2))]
    assert len(admissible)==9 and len(no_necessary_individual)==2
    assert ((1,0),(0,1)) in no_necessary_individual
    # Actual experiential truthmaker for a necessary truth, but none in w1.
    E=(1,0); tau=(1,1); T=E
    assert all(tau) and (not tau[0] or T[0]) and not (not tau[1] or T[1])
    # Excluded middle and the stronger all-world truthmaker assumption do
    # yield experience in every world (via ordinary Boolean reasoning).
    combos=list(product((0,1),repeat=4)) # E0,E1,T0,T1
    accepted=[x for x in combos if all(x[2+i] for i in range(2))
              and all((not x[2+i]) or x[i] for i in range(2))]
    assert accepted and all(x[0] and x[1] for x in accepted)
    # Schema 'possibly p implies p' for contingent p in this S5 frame.
    p=(1,0); possible_p=any(p); possible_not_p=any(not v for v in p)
    assert possible_p and possible_not_p and not p[1]
    # Distinct sector labels permit mutually exclusive local facts to be
    # realized jointly; no external measure follows from that bare set.
    sectors={'left': True,'right':False}
    assert any(sectors.values()) and any(not x for x in sectors.values())
    result={'status':'passed', 'domain':'two mutually accessible formal worlds; two potentially existing subjects',
            'nonempty_assignments':len(admissible),
            'nonempty_without_any_necessary_subject':len(no_necessary_individual),
            'witness':no_necessary_individual[0],
            'actual_truthmaker_does_not_give_all_world_truthmaker':True,
            'all_world_truthmaker_conditional_verified':True,
            'unindexed_possibility_implies_truth_fails_for_contingent_p':True,
            'opposite_facts_realizable_at_distinct_sector_labels':True,
            'scope_warning':'Formal consistency/validity in the declared tiny language is not metaphysical possibility or evidence for any premise.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
