#!/usr/bin/env python3
"""Finite logical witness for plenitude and Bostrom-like observer counting.

Every physical, experiential and modal interpretation is stipulated. This is
not a proof of concrete actuality, necessary existence or conscious software.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json


def powerset(seq):
    for size in range(len(seq)+1):
        for xs in combinations(seq, size):
            yield set(xs)


def validate_modal_schema(worlds, relation):
    # For all propositions over this finite set, test ◇p -> p at every world.
    for extension in powerset(worlds):
        for w in worlds:
            possible = any(v in extension for v in relation[w])
            if possible and w not in extension:
                return False
    return True


def base_history(bit):
    """Two local transitions in the declared ancestor toy model."""
    states = [bit]
    for _ in range(2):
        states.append(1 - states[-1])
    return tuple(states)


def host_program(bit):
    """Distinct representation using parity; matches the base model."""
    return tuple(bit ^ (step % 2) for step in range(3))


def main():
    c, p, i, n, h = 10, 4, 3, 10, 2
    assert 0 < i <= p <= c
    episodes = []
    for civilization in range(c):
        for bit in range(h):
            episodes.append({'observer': f'base-{civilization}-{bit}',
                             'context': f'base-{civilization}',
                             'origin':'base','bit':bit})
    simulation_edges = []
    for owner in range(i):
        for run in range(n):
            sim = f'sim-{owner}-{run}'
            simulation_edges.append((f'base-{owner}',sim))
            for bit in range(h):
                episodes.append({'observer': f'{sim}-{bit}',
                                 'context': sim, 'origin':'simulated', 'bit':bit})
    assert len(set(e['observer'] for e in episodes)) == len(episodes)
    base = [e for e in episodes if e['origin']=='base']
    sim = [e for e in episodes if e['origin']=='simulated']
    assert len(base) == c*h == 20 and len(sim) == i*n*h == 60
    assert len(simulation_edges) == i*n == 30
    for e in episodes:
        trace = (host_program(e['bit']) if e['origin'] == 'simulated'
                 else base_history(e['bit']))
        assert trace == base_history(e['bit'])
    # Symbolic local experience types; admissibility=realization is a
    # stipulation for this four-element toy catalogue, not a metaphysical proof.
    possible_types = set(product_pair for product_pair in
                         [('base',0),('base',1),('simulated',0),('simulated',1)])
    actual_types = {(e['origin'],e['bit']) for e in episodes}
    assert possible_types == actual_types
    assert len({e['bit'] for e in episodes}) == 2
    # All comparison observers are stipulated evidence-compatible.
    by_count = F(len(sim),len(episodes))
    f_p, f_i = F(p,c), F(i,p)
    bostrom_ratio = f_p*f_i*n / (1+f_p*f_i*n)
    assert by_count == bostrom_ratio == F(3,4)
    # Patch sensitivity: keep the civilization fractions and simulation
    # counts fixed, but make non-simulating ancestral populations larger.
    history_sizes = [2 if j < i else 1000 for j in range(c)]
    heterogeneous_base = sum(history_sizes)
    heterogeneous_sim = n * sum(history_sizes[:i])
    heterogeneous_fraction = F(heterogeneous_sim, heterogeneous_base+heterogeneous_sim)
    assert heterogeneous_base == 7006 and heterogeneous_sim == 60
    assert heterogeneous_fraction == F(30,3533) and heterogeneous_fraction != bostrom_ratio
    # A different normalized weighting, still symmetric within each category.
    # This is an epistemic/modeling comparison, not proof both choices are real.
    weight_b, weight_s = F(1,2*len(base)), F(1,2*len(sim))
    weighted_base = len(base)*weight_b
    weighted_sim = len(sim)*weight_s
    assert weighted_base+weighted_sim == 1 and weighted_sim == F(1,2)
    # Standard untyped possibility->actuality schema: singleton vs two
    # mutually accessible formal worlds. Different formal countermodels are
    # not claims about what is metaphysically possible in the proposed whole.
    singleton = ['w0']
    two = ['w0','w1']
    assert validate_modal_schema(singleton, {'w0':['w0']})
    assert not validate_modal_schema(two, {'w0':two,'w1':two})
    # Countably many simulations and bases, both exhaustively enumerated in
    # two orderings; limiting densities differ even though populations coincide.
    cutoff_results = []
    for k in (1,10,100,1000):
        a = [('S',3*j+t) for j in range(k) for t in range(3)]
        a += [('B',j) for j in range(k)]
        b = [('S',j) for j in range(k)]
        b += [('B',3*j+t) for j in range(k) for t in range(3)]
        assert len(set(a))==len(a) and len(set(b))==len(b)
        fa=F(sum(1 for kind,_ in a if kind=='S'),len(a))
        fb=F(sum(1 for kind,_ in b if kind=='S'),len(b))
        assert fa==F(3,4) and fb==F(1,4)
        cutoff_results.append({'blocks':k,'simulation_heavy_fraction':str(fa),
                               'base_heavy_fraction':str(fb)})
    out={
       'status':'passed',
       'finite_example':{'base_civilizations':c, 'posthuman_civilizations':p,
           'interested_posthuman_civilizations':i, 'simulations_per_interested_civilization':n,
           'reference_observers_per_history':h, 'base_observers':len(base),
           'simulated_observers':len(sim), 'simulations':len(simulation_edges),
           'stipulated_realized_local_types':sorted([list(x) for x in actual_types]),
           'base_history_initial_0':list(base_history(0)),
           'base_history_initial_1':list(base_history(1)),
           'all_simulated_traces_equal_their_base_toy_histories':True,
           'counting_fraction_and_bostrom_formula':str(by_count),
           'alternative_group_symmetric_weighted_fraction':str(weighted_sim),
           'heterogeneous_counterexample_base_count':heterogeneous_base,
           'heterogeneous_counterexample_sim_count':heterogeneous_sim,
           'heterogeneous_correct_fraction':str(heterogeneous_fraction),
           'unchanged_simplified_formula_in_heterogeneous_case':str(bostrom_ratio)},
       'global_modal_schema_holds_singleton':True,
       'global_modal_schema_holds_two_mutually_accessible_worlds':False,
       'countably_infinite_cutoff_examples':cutoff_results,
       'scope':'Finite labeled relational witness and conditional probability algebra only. The admissibility catalogue, concrete status, subject incidence, implementer relation, mental content and weights are postulated. No physical simulation, empirical subjects, necessary existence, universal plenitude, uniquely justified measure, quantum dynamics or cosmological prediction is established.'}
    text=json.dumps(out,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__=='__main__':
    main()
