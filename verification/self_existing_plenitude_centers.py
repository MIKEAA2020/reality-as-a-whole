#!/usr/bin/env python3
"""One stipulated actual whole, finite plural subject-locations and credence.

No simulator, creation event, unique physical measure, conscious machine or
proof of necessary actuality is assumed or established by this toy witness.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def main():
    # Fixed, coexisting subject-locations; q is any local experiential or
    # structural property, not a label for simulation versus base reality.
    centers = [('subject-A', 1), ('subject-B', 1),
               ('subject-C', 1), ('subject-D', 0)]
    assert len({s for s, q in centers}) == 4
    local_types_possible = {0, 1}  # stipulated toy admissibility catalogue
    local_types_actual = {q for _, q in centers}
    assert local_types_possible == local_types_actual
    equal_probability = F(sum(q for _, q in centers), len(centers))
    assert equal_probability == F(3, 4)
    # A distinct epistemic weighting, symmetric within the q and not-q groups.
    # It is a logical alternative, not a claim that two physical worlds exist.
    alternative = {s:(F(1,6) if q else F(1,2)) for s,q in centers}
    assert sum(alternative.values()) == 1
    assert sum(alternative[s] for s,q in centers if q) == F(1,2)
    # The whole remains fixed in both examples: local uncertainty is not
    # evidence that actuality needs an agent to choose or produce a world.
    result = {'status':'passed', 'number_of_subject_labels':len(centers),
              'stipulated_possible_local_types':sorted(local_types_possible),
              'actual_local_types':sorted(local_types_actual),
              'equal_center_q_credence':'3/4',
              'alternative_group_symmetric_q_credence':'1/2',
              'scope':'Finite labeled mathematical witness only. Real subjects, genuine possibility, concrete actuality, self-explanation, experiential qualities, justified weights, physical laws and necessary existence are not derived. The comparison concerns indexical measures, not literal simulations or cosmological probabilities.'}
    text=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__=='__main__':
    main()
