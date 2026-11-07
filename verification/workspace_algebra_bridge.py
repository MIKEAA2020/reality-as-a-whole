"""Exact finite workspace/algebra/channel bridge. No phenomenal assignments.

The quantum extension is measure-and-prepare, not a faithful representation of
arbitrary coherent quantum dynamics or a microscopic model of neural tissue.
"""
from dataclasses import replace
from fractions import Fraction as Q
from itertools import product
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = '_workspace_algebra_bridge_audit'
spec = importlib.util.spec_from_file_location(NAME, ROOT/'verification/workspace_intervention_audit.py')
a = importlib.util.module_from_spec(spec)
sys.modules[NAME] = a
spec.loader.exec_module(a)
w = a.w
CONTENTS = (None,) + a.CONTENTS
STATES = tuple(w.State(c,m,f) for c,m,f in product(CONTENTS,CONTENTS,(None,)+w.SOURCES))
INDEX = {s:i for i,s in enumerate(STATES)}
CORES = tuple(product(CONTENTS,(None,)+w.SOURCES))
CORE_INDEX = {c:i for i,c in enumerate(CORES)}
R = tuple(CORE_INDEX[a.core(s)] for s in STATES)


def push(prob, transition, size):
    result = [Q(0)]*size
    for x,y in enumerate(transition):
        result[y] += prob[x]
    return tuple(result)


def pull(observable, transition):
    return tuple(observable[y] for y in transition)


def expect(prob, observable):
    return sum((p*f for p,f in zip(prob,observable)),Q(0))


def quantum_extension(rho, transition):
    """Sparse matrix: sum_x |T(x)><x| rho |x><T(x)|."""
    diagonal = [rho.get((i,i),Q(0)) for i in range(len(transition))]
    out = push(diagonal,transition,len(transition))
    return {(j,j):p for j,p in enumerate(out) if p}


def main():
    assert len(STATES)==75 and len(CORES)==15
    assert set(R)==set(range(15))
    inputs=[()]
    inputs.extend((w.Proposal(c),) for c in a.CONTENTS)
    inputs.extend((w.Proposal(w.Content('visual',x)),w.Proposal(w.Content('auditory',y)))
                  for x,y in product((0,1),repeat=2))
    configs=[w.Config(entry=e,maintain=m,action=ac,feedback=f)
             for e,m,ac,f in product((False,True),repeat=4)]
    prob=tuple(Q(i+1,sum(range(1,76))) for i in range(75))
    core_obs=tuple(Q(i*i-3*i,7) for i in range(15))
    full_obs=pull(core_obs,R)
    controls=0
    full_core_intertwinings=0
    distinct_full_maps=0
    one_witness=None
    for inp,cfg,forced in product(inputs,configs,(a.UNSET,None)+a.CONTENTS):
        normal=tuple(INDEX[a.run(s,inp,cfg,forced).state] for s in STATES)
        repaired=tuple(INDEX[a.closed_loop_replacement(s,inp,cfg,forced).state] for s in STATES)
        # Construct the reduced map only if the fine map is constant on each fiber.
        fibers={}
        for x in range(75):
            reduced_target=R[normal[x]]
            if R[x] in fibers:
                assert fibers[R[x]]==reduced_target
            fibers[R[x]]=reduced_target
            assert R[repaired[x]]==reduced_target
            full_core_intertwinings+=1
        reduced=tuple(fibers[i] for i in range(15))
        assert pull(full_obs,normal)==pull(pull(core_obs,reduced),R)
        assert pull(full_obs,repaired)==pull(pull(core_obs,reduced),R)
        assert push(push(prob,normal,75),R,15)==push(push(prob,R,15),reduced,15)
        assert push(push(prob,repaired,75),R,15)==push(push(prob,R,15),reduced,15)
        assert expect(push(prob,normal,75),full_obs)==expect(prob,pull(full_obs,normal))
        if normal!=repaired:
            distinct_full_maps+=1
            if one_witness is None:
                x=next(i for i in range(75) if normal[i]!=repaired[i])
                one_witness={'source_index':x,'normal_target':normal[x],
                             'replacement_target':repaired[x],
                             'normal_core':R[normal[x]],'replacement_core':R[repaired[x]]}
        controls+=1

    # iota(f)=f o R is a unital, injective, product-preserving map on C(Y).
    for i in range(15):
        ei=tuple(Q(j==i) for j in range(15))
        assert sum(pull(ei,R))==5
        for j in range(15):
            ej=tuple(Q(k==j) for k in range(15))
            prod=tuple(x*y for x,y in zip(ei,ej))
            assert pull(prod,R)==tuple(x*y for x,y in zip(pull(ei,R),pull(ej,R)))
    assert pull((Q(1),)*15,R)==(Q(1),)*75

    # Explicit Kraus matrix units K_x=|T(x)><x| have sum K_x^* K_x=I.
    reference=tuple(INDEX[a.run(s,()).state] for s in STATES)
    gram = {}
    for x, target in enumerate(reference):
        assert 0 <= target < 75
        # K_x has its only unit entry at (target,x); K_x^* K_x=P_x.
        gram[(x,x)] = gram.get((x,x),0) + 1
    assert gram == {(i,i):1 for i in range(75)}
    mixed={(i,i):p for i,p in enumerate(prob)}
    qout=quantum_extension(mixed,reference)
    assert sum(qout.values())==1
    assert all(p>=0 for p in qout.values())
    assert tuple(qout.get((i,i),Q(0)) for i in range(75))==push(prob,reference,75)
    # Two orthogonal coherent input states have identical output: loss is explicit.
    plus={(0,0):Q(1,2),(1,1):Q(1,2),(0,1):Q(1,2),(1,0):Q(1,2)}
    minus={(0,0):Q(1,2),(1,1):Q(1,2),(0,1):Q(-1,2),(1,0):Q(-1,2)}
    assert plus!=minus
    assert quantum_extension(plus,reference)==quantum_extension(minus,reference)
    result={
        'status':'passed',
        'full_classical_states':75,'reduced_classical_states':15,
        'control_settings':controls,
        'statewise_controlled_intertwinings':full_core_intertwinings,
        'control_settings_with_distinct_full_maps':distinct_full_maps,
        'same_core_distinct_full_map_witness':one_witness,
        'observable_embedding':'unital injective *-homomorphism C(15) -> C(75)',
        'dynamics':'R T = t R for reference and replacement in declared family',
        'quantum_extension':'measure-and-prepare Kraus channel on M_75',
        'quantum_coherence_loss_witness':True,
        'neural_microphysical_reduction_established':False,
        'phenomenal_identity_or_subject_selector_established':False,
        'scope':'exact finite mathematics; CP/TP proof is analytic in report, not inferred from sampling',
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'PASS: {controls} controlled maps, {full_core_intertwinings} statewise intertwinings; no phenomenal claim.')


if __name__=='__main__':
    main()
