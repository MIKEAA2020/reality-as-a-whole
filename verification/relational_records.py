"""Exact intervention/record continuation of the relational constraint construction.

Only standard-library rational arithmetic. The report proves the arbitrary-length
and C*-algebra statements; these are finite algebraic checks, not experience data.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
if __package__:
    from .relational_constraint import eye, transpose, subtract, scale, zero, mv, dot, constraint, relative_observable, apply_site
    from .infinite_coherence import words, support_vectors
else:
    from relational_constraint import eye, transpose, subtract, scale, zero, mv, dot, constraint, relative_observable, apply_site
    from infinite_coherence import words, support_vectors


def mm(a, b):
    """Exact multiplication skipping zeros, for sparse clock/record matrices."""
    out = [[F(0) for _ in b[0]] for _ in a]
    rows = [[(j, x) for j, x in enumerate(row) if x] for row in b]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in rows[k]:
                    out[i][j] += x*y
    return out


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def norm(v):
    return dot(v, v)


def canonical_unitary(kraus):
    """U = [[0,V*],[V,I-VV*]], where V is the Kraus column."""
    d = len(kraus[0])
    V = [row[:] for K in kraus for row in K]
    Vt = transpose(V)
    assert mm(Vt, V) == eye(d)
    complement = subtract(eye(len(V)), mm(V, Vt))
    top = [[F(0)]*d + row for row in Vt]
    bottom = [a+b for a, b in zip(V, complement)]
    U = top+bottom
    assert U == transpose(U)
    assert mm(U, U) == eye(len(U))
    return U


def branch_probabilities(initial, rotation):
    P0, P1 = [[F(1), F(0)], [F(0), F(0)]], [[F(0), F(0)], [F(0), F(1)]]
    return [[norm(mv(Pb, mv(rotation, mv(Pa, initial)))) for Pb in (P0, P1)]
            for Pa in (P0, P1)]


def instrument_channel(kraus, rho):
    out = [[F(0)]*len(rho) for _ in rho]
    for K in kraus:
        out = add(out, mm(mm(K, rho), transpose(K)))
    return out


def run():
    R = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
    X = [[F(0), F(1)], [F(1), F(0)]]
    P0, P1 = [[F(1), F(0)], [F(0), F(0)]], [[F(0), F(0)], [F(0), F(1)]]
    # Canonical completion, including a non-projective rational instrument.
    damping = [[[F(1), F(0)], [F(0), F(3, 5)]],
               [[F(0), F(4, 5)], [F(0), F(0)]]]
    canonical_unitary([P0, P1])
    U = canonical_unitary(damping)
    for j in range(2):
        blank = [F(i == j) for i in range(6)]
        assert mv(U, blank) == [F(0), F(0)]+[row[j] for K in damping for row in K]
    damped = mv(U, [F(0), F(1), F(0), F(0), F(0), F(0)])
    reduced = [[sum(damped[2*p+i]*damped[2*p+j] for p in range(3))
                for j in range(2)] for i in range(2)]
    assert reduced == instrument_channel(damping, P1)
    assert [sum(x*x for x in damped[2*p:2*p+2]) for p in (1, 2)] == [F(9, 25), F(16, 25)]
    # For this Kraus-gauge test, group both operators into one recorded outcome.
    rotated_kraus = [add(scale(R[i][0], damping[0]), scale(R[i][1], damping[1])) for i in range(2)]
    for i, j in product(range(2), repeat=2):
        unit = [[F(a == i and b == j) for b in range(2)] for a in range(2)]
        assert instrument_channel(damping, unit) == instrument_channel(rotated_kraus, unit)
    # Both measurement memories have a distinct blank symbol 0; outcome a is a+1.
    basis = tuple(product(range(2), range(3), range(3)))
    lookup = {b: i for i, b in enumerate(basis)}
    d = len(basis)
    def write(register):
        gate = [[F(0)]*d for _ in range(d)]
        for col, b in enumerate(basis):
            target = list(b)
            a, value = b[0]+1, b[register]
            target[register] = a if value == 0 else 0 if value == a else value
            gate[lookup[tuple(target)]][col] = 1
        return gate
    def system_gate(gate, adaptive=False):
        out = [[F(0)]*d for _ in range(d)]
        for col, b in enumerate(basis):
            chosen = gate if not adaptive or b[1] == 1 else eye(2)
            for s in range(2):
                out[lookup[(s, b[1], b[2])]][col] = chosen[s][b[0]]
        return out
    write1, write2 = write(1), write(2)
    evolve = system_gate(R)
    for gate in (write1, write2, evolve):
        assert mm(transpose(gate), gate) == eye(d)
    initial = [F(0)]*d
    initial[lookup[(0, 0, 0)]], initial[lookup[(1, 0, 0)]] = F(3, 5), F(4, 5)
    paths = [eye(d)]
    for gate in (write1, evolve, write2):
        paths.append(mm(gate, paths[-1]))
    sections = [mv(p, initial) for p in paths]
    assert all(norm(s) == 1 for s in sections)
    edges = [(i, i+1, g) for i, g in enumerate((write1, evolve, write2))]
    C = constraint(4, d, edges)
    history = [x for s in sections for x in s]
    assert not any(mv(C, history))
    def Q(a, b):
        return [[F(i == j and row[1:] == (a+1, b+1)) for j in range(d)]
                for i, row in enumerate(basis)]
    predicted = branch_probabilities([F(3, 5), F(4, 5)], R)
    expected = [[F(81, 625), F(144, 625)], [F(256, 625), F(144, 625)]]
    assert predicted == expected
    joint = [[norm(mv(Q(a, b), sections[-1])) for b in range(2)] for a in range(2)]
    assert joint == predicted and sum(map(sum, joint)) == 1
    for a, b in product(range(2), repeat=2):
        selected = mv(Q(a, b), sections[-1])
        assert all(not x for x, label in zip(selected, basis) if label[0] != b)
    record_operators = []
    for a, b in product(range(2), repeat=2):
        O = relative_observable(paths, 3, Q(a, b))
        assert zero(subtract(mm(C, O), mm(O, C)))
        assert mm(O, O) == O
        assert dot(history, mv(O, history))/4 == joint[a][b]
        record_operators.append(O)
    for i, A in enumerate(record_operators):
        for B in record_operators[i+1:]:
            assert zero(mm(A, B))
    written_sum = [[F(0)]*(4*d) for _ in range(4*d)]
    for O in record_operators:
        written_sum = add(written_sum, O)
    invalid = subtract(eye(4*d), written_sum)
    assert mm(invalid, invalid) == invalid
    assert dot(history, mv(invalid, history)) == 0
    # First record persists after writing; not before writing.
    record0 = [[F(i == j and row[1] == 1) for j in range(d)] for i, row in enumerate(basis)]
    for v in (1, 2, 3):
        assert relative_observable(paths, v, record0) == relative_observable(paths, 3, record0)
    assert relative_observable(paths, 0, record0) != relative_observable(paths, 1, record0)
    assert zero(subtract(mm(evolve, record0), mm(record0, evolve)))
    assert zero(subtract(mm(write2, record0), mm(record0, write2)))
    # Omission is not forgetting. Coarse-graining retains the actual disturbance.
    second = [sum(joint[a][b] for a in range(2)) for b in range(2)]
    no_first = [x*x for x in mv(R, [F(3, 5), F(4, 5)])]
    assert second == [F(337, 625), F(288, 625)]
    assert no_first == [F(49, 625), F(576, 625)]
    # Prefix normalization, including feedback controlled by the first record.
    adaptive_gate = system_gate(R, adaptive=True)
    assert mm(transpose(adaptive_gate), adaptive_gate) == eye(d)
    assert zero(subtract(mm(adaptive_gate, record0), mm(record0, adaptive_gate)))
    adaptive_final = mv(write2, mv(adaptive_gate, sections[1]))
    adaptive = [[norm(mv(Q(a, b), adaptive_final)) for b in range(2)] for a in range(2)]
    assert adaptive == [[F(81, 625), F(144, 625)], [F(0), F(16, 25)]]
    assert [sum(row) for row in adaptive] == [sum(row) for row in joint] == [F(9, 25), F(16, 25)]
    # Nontrivial edge subdivision: R = (R X) X. Event effects are unchanged.
    first_half, second_half = system_gate(X), system_gate(mm(R, X))
    refined = [eye(d)]
    for gate in (write1, first_half, second_half, write2):
        refined.append(mm(gate, refined[-1]))
    assert refined[-1] == paths[-1]
    refined_sections = [mv(p, initial) for p in refined]
    assert sum(norm(v) for v in refined_sections) == 5
    assert norm(refined_sections[-1])/5 == F(1, 5)
    assert norm(sections[-1])/4 == F(1, 4)
    for a, b in product(range(2), repeat=2):
        q = Q(a, b)
        effect = mm(mm(transpose(paths[-1]), q), paths[-1])
        refined_effect = mm(mm(transpose(refined[-1]), q), refined[-1])
        assert effect == refined_effect
    # Eraser projectors mix outcome sectors; the instrument alone does not fix them.
    def eraser_plus(phase=1):
        out = [[F(0)]*d for _ in range(d)]
        for i, a in enumerate(basis):
            for j, b in enumerate(basis):
                if a[0] == b[0] and a[2] == b[2] and a[1] in (1, 2) and b[1] in (1, 2):
                    out[i][j] = F(1 if a[1] == b[1] else phase, 2)
        return out
    plus = eraser_plus()
    assert mm(plus, plus) == plus
    def eraser_joint(v):
        projected = mv(plus, v)
        return [sum(x*x for x, b in zip(projected, basis) if b[2] == outcome+1) for outcome in range(2)]
    eraser = eraser_joint(sections[-1])
    assert eraser == [F(49, 1250), F(288, 625)]
    assert sum(eraser) == F(1, 2)
    # Flip the coherent phase of outcome 1: same CP instrument and recorded data.
    phased = [(-x if b[1] == 2 else x) for x, b in zip(sections[-1], basis)]
    assert [[norm(mv(Q(a, b), phased)) for b in range(2)] for a in range(2)] == joint
    assert eraser_joint(phased) == [F(1, 2), F(0)]
    assert [eraser[b]+eraser_joint(phased)[b] for b in range(2)] == second
    for K in (P0, P1):
        for i, j in product(range(2), repeat=2):
            unit = [[F(a == i and b == j) for b in range(2)] for a in range(2)]
            assert instrument_channel([K], unit) == instrument_channel([scale(-1, K)], unit)
    # Uncompute all first-outcome markers before evolution, versus leaving a copy.
    restored = mv(write1, sections[1])
    assert restored == initial
    # Explicit reversible reset: swap first memory with a fresh ternary environment.
    big_basis = tuple(product(range(2), range(3), range(3), range(3)))
    big_lookup = {b: i for i, b in enumerate(big_basis)}
    reset = [F(0)]*len(big_basis)
    for x, (s, r1, r2) in zip(sections[-1], basis):
        reset[big_lookup[(s, 0, r2, r1)]] = x
    assert norm(reset) == 1
    assert all(not x for x, b in zip(reset, big_basis) if b[1] != 0)
    environment_joint = [[sum(x*x for x, b in zip(reset, big_basis)
                              if b[3] == a+1 and b[2] == c+1)
                           for c in range(2)] for a in range(2)]
    assert environment_joint == joint
    # Keeping the copied marker removes coherence even if the visible first register is undone.
    # Copy the first label, then undo the visible write; the environment remains orthogonal.
    copied = [F(0)]*len(big_basis)
    for amplitude, (s, r1, r2) in zip(sections[1], basis):
        if amplitude:
            copied[big_lookup[(s, 0, r2, r1)]] = amplitude
    assert norm(copied) == 1
    after_rotation = [F(0)]*len(big_basis)
    for amplitude, (s, r1, r2, e) in zip(copied, big_basis):
        if amplitude:
            for target in range(2):
                after_rotation[big_lookup[(target, r1, r2, e)]] += R[target][s]*amplitude
    marked_b0 = sum(x*x for x, b in zip(after_rotation, big_basis) if b[0] == 0)
    assert marked_b0 == second[0]
    # Direct continuation of the earlier four-site AKLT state.
    aklt = support_vectors(4)[0]
    aklt_basis = words(4)
    aklt_norm = norm(aklt)
    qutrit_rotation = [[F(3, 5), F(0), F(-4, 5)],
                       [F(0), F(1), F(0)],
                       [F(4, 5), F(0), F(3, 5)]]
    aklt_joint, neighbor = [], []
    for a in range(3):
        branch = [v if w[0] == a else F(0) for v, w in zip(aklt, aklt_basis)]
        neighbor.append([sum(v*v for v, w in zip(branch, aklt_basis) if w[1] == b)/norm(branch)
                         for b in range(3)])
        evolved = apply_site(branch, qutrit_rotation, 0)
        aklt_joint.append([sum(v*v for v, w in zip(evolved, aklt_basis) if w[0] == b)/aklt_norm
                           for b in range(3)])
    assert aklt_joint == [[F(3, 25), F(0), F(16, 75)], [F(0), F(1, 3), F(0)],
                          [F(16, 75), F(0), F(3, 25)]]
    assert neighbor == [[F(3 if a == b else 2, 7) for b in range(3)] for a in range(3)]
    return {
        'status': 'passed', 'arithmetic': 'exact rational; no random sampling',
        'canonical_unitary': 'projective and nonprojective inner instruments; U*=U and U^2=I',
        'joint_record_probabilities': [[str(x) for x in row] for row in joint],
        'second_outcome_after_coarse_graining': [str(x) for x in second],
        'second_outcome_if_first_intervention_omitted': [str(x) for x in no_first],
        'adaptive_joint': [[str(x) for x in row] for row in adaptive],
        'dirac_record_observables': 'commute with constraint and reproduce joint probabilities',
        'persistence': 'exact after writing, not asserted before writing',
        'clock_refinement': 'same endpoint effects; clock reading weights 1/4 versus 1/5',
        'eraser_plus_joint': [str(x) for x in eraser],
        'same_instrument_phase_variant_eraser_plus_joint': ['1/2', '0'],
        'reversible_reset': 'blank visible memory, unchanged joint distribution in environment',
        'aklt_sequential_joint': [[str(x) for x in row] for row in aklt_joint],
        'aklt_neighbor_conditioned_on_first_record': [[str(x) for x in row] for row in neighbor],
        'limitations': ['general C*-algebra theorem assumes finite inner Kraus families',
                        'fresh memories and nondemolition of prior outcomes are supplied',
                        'no selected unique outcome, phenomenal ownership, or fundamental arrow is derived'],
    }


if __name__ == '__main__':
    result = run()
    target = Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: sequential instruments, canonical dilations, Dirac records, feedback and erasure')
    print(target)
