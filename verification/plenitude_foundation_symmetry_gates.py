#!/usr/bin/env python3
"""Finite logical and permutation checks, not proofs about metaphysical reality."""
from fractions import Fraction
from itertools import permutations, product
import json
from pathlib import Path


def main():
    # Reflexive singleton semantics: two distinct stipulated models, each
    # validating possibility -> truth for every Boolean proposition on its world.
    singleton = []
    for experiential_atom in (False, True):
        valuations = ((False,), (True,))  # all Boolean truth assignments
        assert all((not any(v)) or v[0] for v in valuations)
        assert all((not v[0]) or all(v) for v in valuations)
        singleton.append({'experience_atom': experiential_atom,
                          'experience_atom_necessary': experiential_atom,
                          'strong_schema_holds': True})
    assert singleton[0]['experience_atom_necessary'] is False
    assert singleton[1]['experience_atom_necessary'] is True

    # On two mutually accessible points, schema for q and not q holds iff q
    # has the same truth value at both points (same is true globally).
    two_worlds = []
    for q in product((False, True), repeat=2):
        schema_q = all((not any(q)) or q[w] for w in range(2))
        schema_not_q = all((not any(not x for x in q)) or (not q[w])
                           for w in range(2))
        both = schema_q and schema_not_q
        assert both == (q[0] == q[1])
        two_worlds.append({'q': list(q), 'schema_q_and_not_q': both})

    # Unpointed graph = triangle plus isolated vertex 3. Its automorphisms
    # permute the triangle and fix the isolated vertex.
    vertices = range(4)
    edges = {frozenset((i,j)) for i in range(3) for j in range(i+1,3)}
    autos = [p for p in permutations(vertices)
             if {frozenset((p[i],p[j])) for i,j in (tuple(e) for e in edges)} == edges]
    assert len(autos) == 6
    selectors = []
    for bits in product((0,1), repeat=4):
        if all(all(bits[i] == bits[p[i]] for i in vertices) for p in autos):
            selectors.append(''.join(map(str,bits)))
    assert set(selectors) == {'0000','0001','1110','1111'}

    # Rival stipulated subject partitions of the very same labeled dynamics:
    # individual vertices versus connected components. Both partitions are
    # invariant as SETS of blocks under graph automorphisms.
    per_vertex = frozenset(frozenset((i,)) for i in vertices)
    per_component = frozenset((frozenset((0,1,2)), frozenset((3,))))
    for partition in (per_vertex, per_component):
        for a in autos:
            mapped = frozenset(frozenset(a[i] for i in block) for block in partition)
            assert mapped == partition
    assert len(per_vertex) == 4 and len(per_component) == 2
    # Stipulated local reports q XOR intervention. Neither partition enters
    # this report rule, so exhaustively check its 16 binary interventions.
    q = (1,1,1,0)
    report_rows = []
    for u in product((0,1), repeat=4):
        def reports(partition):
            assert partition in (per_vertex, per_component)
            return tuple(q[i] ^ u[i] for i in vertices)
        r1, r2 = reports(per_vertex), reports(per_component)
        assert r1 == r2
        report_rows.append({'intervention':list(u), 'reports':list(r1)})

    # Interpret bits independently as candidate binary experiential valence;
    # invariance by itself permits precisely the same four assignments.
    valence_assignments = selectors.copy()
    mixed_valence = [bits for bits in valence_assignments
                     if '0' in bits and '1' in bits]
    assert set(mixed_valence) == {'0001', '1110'}

    def invariant_measure(p):
        weights = [p/3, p/3, p/3, 1-p]
        assert sum(weights) == 1
        assert all(w > 0 for w in weights)
        assert all(all(weights[i] == weights[a[i]] for i in vertices) for a in autos)
        return weights
    weights_a = invariant_measure(Fraction(3,4))
    weights_b = invariant_measure(Fraction(1,2))
    assert sum(weights_a[:3]) == Fraction(3,4)
    assert sum(weights_b[:3]) == Fraction(1,2)

    receipt = {
        'status':'passed',
        'one_world_models': singleton,
        'two_world_proposition_valuations': two_worlds,
        'graph':'unpointed triangle plus isolated vertex',
        'automorphism_count':len(autos),
        'invariant_subject_selectors_bits':selectors,
        'rival_subject_partition_counts': [len(per_vertex),len(per_component)],
        'identical_report_interventions_checked':len(report_rows),
        'rival_partition_report_table':report_rows,
        'invariant_binary_valence_assignments':valence_assignments,
        'mixed_valence_assignments':mixed_valence,
        'two_strictly_positive_invariant_measures':[[str(x) for x in weights_a],
                                                     [str(x) for x in weights_b]],
        'scope':'Toy modal semantics and finite graph only. Experiential atoms, subject boundaries, empirical valences, metaphysical necessity, actual possibility and probability measures are stipulated, not established. Invariance under these graph automorphisms is a limited assumed constraint, not a theorem that no further laws or data can determine these quantities.'}
    text=json.dumps(receipt,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text)


if __name__ == '__main__':
    main()
