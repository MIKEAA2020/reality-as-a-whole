#!/usr/bin/env python3
"""Compare two stipulated subject rules on one four-spin physical model.

This is not an implementation of IIT, a model of patients, or a proof of
experience. Exact rational calculations and finite permutations only.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json

from causal_influence_subject_gate import influence_graph, score
from coupled_subject_boundary_gate import stationary

V = frozenset(range(4))


def connected_components(active, pair):
    remaining, result = set(active), []
    while remaining:
        stack = [min(remaining)]
        comp = set()
        while stack:
            i = stack.pop()
            if i in comp:
                continue
            comp.add(i)
            stack += [j for j in active if j not in comp and j != i
                      and pair[tuple(sorted((i, j)))] > 0]
        remaining -= comp
        if len(comp) >= 2:
            result.append(frozenset(comp))
    return frozenset(result)


def maximal_cohesion(active, pair):
    subsets = [frozenset(s) for n in range(2, len(active)+1)
               for s in combinations(sorted(active), n)]
    if not subsets:
        return frozenset(), False
    values = {s: score(s, pair) for s in subsets}
    maximum = max(values.values())
    if maximum <= 0:
        return frozenset(), False
    top = [s for s, value in values.items() if value == maximum]
    size = max(map(len, top))
    selected = frozenset(s for s in top if len(s) == size)
    overlap = any(a & b for a, b in combinations(selected, 2))
    # Do not silently choose among overlapping, equally sized maxima.
    return selected, overlap


def classify(active, pair):
    a = connected_components(active, pair)
    b, unresolved = maximal_cohesion(active, pair)
    return a, b, unresolved


def componentwise_cohesion(active, pair):
    selected, unresolved = set(), False
    for component in connected_components(active, pair):
        local, overlap = maximal_cohesion(component, pair)
        selected.update(local)
        unresolved |= overlap
    return frozenset(selected), unresolved


def overlapping_local_maxima(active, pair):
    subsets = [frozenset(s) for n in range(2, len(active)+1)
               for s in combinations(sorted(active), n)]
    vals = {s: score(s,pair) for s in subsets}
    positive = {s for s in subsets if vals[s] > 0}
    winners, unresolved = set(), set()
    for s in positive:
        rivals = [r for r in positive if r != s and r & s]
        if any(vals[r] > vals[s] for r in rivals):
            continue
        if any(vals[r] == vals[s] for r in rivals):
            unresolved.add(s)
        else:
            winners.add(s)
    assert not any(a & b for a,b in combinations(winners,2))
    return frozenset(winners), frozenset(unresolved)


def lists(sets):
    return sorted((sorted(s) for s in sets), key=lambda s: (len(s), s))


def relabel(sets, perm):
    return frozenset(frozenset(perm[i] for i in s) for s in sets)


def lineage(before, after):
    # Separate strict continuation (identical carrier set) from overlap lineage.
    return {
        'strict': sorted([[sorted(a), sorted(b)] for a in before for b in after if a == b]),
        'overlap': sorted([[sorted(a), sorted(b)] for a in before for b in after if a & b]),
    }


def main():
    couplings = [F(1,2), F(1,4), F(0), F(3,4)]
    rows = []
    checked = 0
    for t in couplings:
        _, pair = influence_graph(t)
        for bits in product((0, 1), repeat=4):
            active = frozenset(i for i, b in enumerate(bits) if b)
            a, b, unresolved = classify(active, pair)
            lw, lt = overlapping_local_maxima(active, pair)
            for perm in permutations(range(4)):
                perm_pair = {tuple(sorted((perm[i], perm[j]))): w
                             for (i,j),w in pair.items()}
                new_active = frozenset(perm[i] for i in active)
                aa, bb, uu = classify(new_active, perm_pair)
                ww, tt = overlapping_local_maxima(new_active, perm_pair)
                assert aa == relabel(a, perm) and bb == relabel(b, perm) and uu == unresolved
                assert ww == relabel(lw, perm) and tt == relabel(lt, perm)
                checked += 1
        a,b,unresolved = classify(V, pair)
        dist = stationary(t, (None,)*4)
        assert sum(dist.values()) == 1
        same = sum(p for s,p in dist.items() if s[0] == s[3])
        assert same == (1 + t/4)/2
        z_a = any({0,3} <= s for s in a)
        z_b = any({0,3} <= s for s in b) if not unresolved else None
        # The same toy reporter says 'yes' with probability 3/4 in both
        # completions. These are error rates relative to stipulated labels.
        q = F(3,4)
        error_a = 1-q if z_a else q
        error_b = (1-q if z_b else q) if z_b is not None else None
        rows.append({'coupling_tanh':str(t), 'rule_C':lists(a), 'rule_M':lists(b),
                     'M_unresolved_overlap':unresolved,
                     'endpoint_match_probability':str(same),
                     'endpoint_togetherness_C':z_a, 'endpoint_togetherness_M':z_b,
                     'report_yes_probability_both_rules':str(q),
                     'report_error_C':str(error_a),
                     'report_error_M':str(error_b) if error_b is not None else None})
    by_t={r['coupling_tanh']:r for r in rows}
    assert by_t['1/2']['rule_C'] == by_t['1/2']['rule_M'] == [[0,1,2,3]]
    assert by_t['1/4']['rule_C'] == [[0,1,2,3]]
    assert by_t['1/4']['rule_M'] == [[0,1],[2,3]]
    assert by_t['1/4']['endpoint_match_probability'] == '17/32'
    assert by_t['1/4']['report_error_C']=='1/4' and by_t['1/4']['report_error_M']=='3/4'
    # Even perfect source calibration cannot establish target calibration:
    # reporter always says yes, both rules say Z=1 at t=1/2, but at t=1/4
    # M says Z=0 while C says Z=1.
    q_perfect = F(1)
    assert 1-q_perfect == 0 and q_perfect == 1
    assert by_t['0']['rule_C'] == by_t['0']['rule_M'] == [[0,1],[2,3]]
    assert by_t['3/4']['rule_M'] == [[1,2]]
    _, zero_pair = influence_graph(F(0))
    # Disconnected pairs: strengthening only the left physical component
    # changes global-max M's decision about the unmodified right component.
    remote_pair = dict(zero_pair)
    remote_pair[(0,1)] = F(3,5)
    remote_c,remote_m,remote_unresolved=classify(V, remote_pair)
    assert not remote_unresolved
    assert lists(remote_c)==[[0,1],[2,3]] and lists(remote_m)==[[0,1]]
    local_zero, local_u = componentwise_cohesion(V,remote_pair)
    assert not local_u and lists(local_zero) == [[0,1],[2,3]]
    overlap_zero, overlap_ties = overlapping_local_maxima(V,remote_pair)
    assert lists(overlap_zero)==[[0,1],[2,3]] and not overlap_ties
    weak_link_cases=[]
    for epsilon in (F(1,100),F(1,10000)):
        wp = dict(remote_pair)
        wp[(1,2)] = epsilon
        local, local_u = componentwise_cohesion(V,wp)
        local_overlap, local_ties = overlapping_local_maxima(V,wp)
        assert not local_u and lists(local)==[[0,1]]
        assert lists(local_overlap)==[[0,1],[2,3]] and not local_ties
        weak_link_cases.append({'edge_12':str(epsilon),'componentwise_M':lists(local),
                                'overlap_local_winners':lists(local_overlap)})
    for perm in permutations(range(4)):
        remapped={tuple(sorted((perm[i],perm[j]))):w for (i,j),w in remote_pair.items()}
        rc,rm,ru=classify(V,remapped)
        loc,lu=componentwise_cohesion(V,remapped)
        ow,ot=overlapping_local_maxima(V,remapped)
        assert not ru and rc==relabel(remote_c,perm) and rm==relabel(remote_m,perm)
        assert not lu and loc==relabel(local_zero,perm)
        assert ow==relabel(overlap_zero,perm) and ot==relabel(overlap_ties,perm)
    one_a,one_b,u=classify(frozenset((2,3)),zero_pair)
    assert not u and lists(one_a)==lists(one_b)==[[2,3]]
    empty_a,empty_b,u=classify(frozenset(),zero_pair)
    assert not empty_a and not empty_b and not u
    _, half_pair = influence_graph(F(1,2))
    _, weak_pair = influence_graph(F(1,4))
    half_winners, half_ties = overlapping_local_maxima(V,half_pair)
    weak_winners, weak_ties = overlapping_local_maxima(V,weak_pair)
    assert not half_winners and len(half_ties)==6
    assert lists(weak_winners)==[[0,1],[2,3]] and not weak_ties
    for perm in permutations(range(4)):
        remapped={tuple(sorted((perm[i],perm[j]))):w for (i,j),w in half_pair.items()}
        w,ts=overlapping_local_maxima(V,remapped)
        assert w==relabel(half_winners,perm) and ts==relabel(half_ties,perm)
    pre_c,pre_m,_=classify(V,half_pair)
    post_c,post_m,_=classify(V,weak_pair)
    assert len(lineage(pre_c,post_c)['strict'])==1
    assert not lineage(pre_m,post_m)['strict'] and len(lineage(pre_m,post_m)['overlap'])==2
    for perm in permutations(range(4)):
        a, b = relabel(pre_m,perm), relabel(post_m,perm)
        assert len(lineage(a,b)['strict'])==0 and len(lineage(a,b)['overlap'])==2
    result={'status':'passed', 'scope':'Stipulated toy experiential rules and classical four-spin system, not patient data, physical validation, IIT, or proof of experience.',
            'full_active_cases':rows,'active_right_pair_only':lists(one_a),'no_active_units':lists(empty_a),
            'disconnected_stronger_left':{'edges_01_and_23':['3/5','1/2'],
                'C':lists(remote_c),'M':lists(remote_m),'componentwise_M':lists(local_zero),'relabelings_checked':24},
            'componentwise_M_weak_links':weak_link_cases,
            'overlap_local_half_coupling':{'strict_winners':lists(half_winners),'unresolved_ties':lists(half_ties),'relabelings_checked':24},
            'initial_to_weak_C_lineage':lineage(pre_c,post_c),
            'initial_to_weak_M_lineage':lineage(pre_m,post_m),
            'permutation_rule_checks':checked,'fission_relabelings_checked':24,
            'report_identity':'For complementary joint-label predictions Z_C=1 and Z_M=0, any binary report R has P(R!=Z_C)+P(R!=Z_M)=1.'}
    text=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__=='__main__':
    main()
