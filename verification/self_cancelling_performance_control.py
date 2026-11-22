#!/usr/bin/env python3
"""Finite controls for internal cyclic performance, net score and explanation.

An explicit relation, admissible configurations, and input state are stipulated;
this is not a demonstration of self-subsistence or real experience.
"""
import json
from pathlib import Path


def shift(q):
    if len(q)!=3:
        raise ValueError('three entries required')
    return (q[2],q[0],q[1])


def run():
    initial=(1,-1,0)
    trajectory=[initial]
    for _ in range(3): trajectory.append(shift(trajectory[-1]))
    assert trajectory==[(1,-1,0),(0,1,-1),(-1,0,1),(1,-1,0)]
    assert len(set(trajectory[:3]))==3
    assert all(sum(x)==0 for x in trajectory)
    assert trajectory[-1]==trajectory[0]
    # At the endpoint the specified complete state cannot reveal whether
    # zero or three steps occurred; retaining the trajectory distinguishes them.
    assert [initial] != trajectory
    # Both components can individually have witnesses yet no common witness.
    universe={'a','b'}; structural={'a'}; experiential={'b'}
    assert structural and experiential and structural|experiential==universe
    assert not (structural & experiential)
    # Two full states with identical zero total need not be the same state.
    empty=(0,0,0)
    assert sum(initial)==sum(empty)==0 and initial!=empty
    return {'status':'passed', 'initial':list(initial),
        'cyclic_trajectory':[list(x) for x in trajectory],
        'sum_at_each_stage':[sum(x) for x in trajectory],
        'endpoint_returns_to_initial':True,'trajectory_is_nontrivial':True,
        'endpoint_alone_distinguishes_zero_from_three_steps':False,
        'full_trajectory_distinguishes_zero_from_three_steps':True,
        'zero_total_distinguishes_nonzero_from_zero_state':False,
        'separate_component_witnesses_need_not_be_joint':True,
        'scope':'Finite stipulated relation; no ontological or experiential result, physical apparatus, or zero-residue proof.'}


if __name__=='__main__':
    result=run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
