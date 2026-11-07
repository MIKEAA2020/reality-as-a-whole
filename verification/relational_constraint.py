"""Exact relational-constraint checks; see RELATIONAL_TIME_CONSTRUCTION.md.

General proofs are in the report. Fractions only; finite examples are not
quantum-gravity data or consciousness assignments. Uses the previous AKLT code.
"""
from fractions import Fraction as F
import json
from pathlib import Path
if __package__:
    from .infinite_coherence import (words, support_vectors, hamiltonian,
                                    mm, rank, trace)
else:
    from infinite_coherence import (words, support_vectors, hamiltonian,
                                   mm, rank, trace)


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(x) for x in zip(*a)]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def subtract(a, b):
    return [[x-y for x, y in zip(r, s)] for r, s in zip(a, b)]


def zero(a):
    return all(not x for row in a for x in row)


def mv(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def block_diagonal(blocks):
    m, d = len(blocks), len(blocks[0])
    out = [[F(0)]*(m*d) for _ in range(m*d)]
    for v, b in enumerate(blocks):
        for i in range(d):
            for j in range(d):
                out[v*d+i][v*d+j] = b[i][j]
    return out


def constraint(vertices, d, edges):
    out = [[F(0)]*(vertices*d) for _ in range(vertices*d)]
    for u, v, U in edges:
        assert mm(transpose(U), U) == eye(d)
        for i in range(d):
            out[u*d+i][u*d+i] += 1
            out[v*d+i][v*d+i] += 1
            for j in range(d):
                out[v*d+i][u*d+j] -= U[i][j]
                out[u*d+j][v*d+i] -= U[i][j]
    return out


def root_pin(C, h, root=0):
    out = [row[:] for row in C]
    d = len(h)
    for i in range(d):
        for j in range(d):
            out[root*d+i][root*d+j] += h[i][j]
    return out


def relative_observable(P, clock, A, projection=None):
    B = mm(mm(transpose(P[clock]), A), P[clock])
    if projection is not None:
        B = mm(mm(projection, B), projection)
    return block_diagonal([mm(mm(p, B), transpose(p)) for p in P])


def apply_site(v, gate, site, sites=4):
    w = words(sites)
    lookup = {a: i for i, a in enumerate(w)}
    out = [F(0)]*len(w)
    for j, a in enumerate(w):
        for b in range(3):
            target = list(a)
            target[site] = b
            out[lookup[tuple(target)]] += gate[b][a[site]]*v[j]
    return out


def zz_expectation(v):
    # L_z = i J, so L_z tensor L_z = -J tensor J is real.
    J = [[0, -1, 0], [1, 0, 0], [0, 0, 0]]
    w = words(4)
    total = F(0)
    for i, a in enumerate(w):
        for j, b in enumerate(w):
            if a[2:] == b[2:]:
                total -= v[i]*v[j]*J[a[0]][b[0]]*J[a[1]][b[1]]
    return total/dot(v, v)


def run():
    I = eye(2)
    R = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
    Z = [[F(1), F(0)], [F(0), F(-1)]]
    X = [[F(0), F(1)], [F(1), F(0)]]
    P = [I, R, Z, mm(Z, R)]
    tree = [(0, 1, R), (1, 3, Z), (0, 2, Z)]
    results = {}
    for name, holonomy, expected in [('flat', I, 2), ('fixed_sector', Z, 1),
                                       ('phase_obstruction', scale(-1, I), 0)]:
        edge = mm(mm(P[3], holonomy), transpose(P[2]))
        edges = tree+[(2, 3, edge)]
        C = constraint(4, 2, edges)
        nullity = 8-rank(C)
        fixed = 2-rank(subtract(holonomy, I))
        assert nullity == fixed == expected
        assert C == transpose(C)
        results[name] = {'zero_constraint_dimension': nullity,
                         'holonomy_fixed_dimension': fixed}
        projection = I if name == 'flat' else [[F(1), F(0)], [F(0), F(0)]]
        if expected:
            for v in range(4):
                for A in (I, X, Z):
                    O = relative_observable(P, v, A, projection)
                    assert zero(subtract(mm(C, O), mm(O, C)))
        if name == 'fixed_sector':
            good_pin = [[F(0), F(0)], [F(0), F(1)]]
            bad_pin = [[F(1), F(0)], [F(0), F(0)]]
            assert 8-rank(root_pin(C, good_pin)) == 1
            assert 8-rank(root_pin(C, bad_pin)) == 0
        if name == 'phase_obstruction':
            # Density transport alone cannot see a scalar phase obstruction.
            rho = [[F(1), F(0)], [F(0), F(0)]]
            assert mm(mm(holonomy, rho), transpose(holonomy)) == rho
    flat_edges = tree+[(2, 3, mm(P[3], transpose(P[2])))]
    C = constraint(4, 2, flat_edges)
    # Exact finite witness of C = W (graph Laplacian tensor I) W^*.
    L = constraint(4, 2, [(u, v, I) for u, v, _ in flat_edges])
    W = block_diagonal(P)
    assert C == mm(mm(W, L), transpose(W))
    for v in range(4):
        OX = relative_observable(P, v, X)
        OZ = relative_observable(P, v, Z)
        assert relative_observable(P, v, mm(X, Z)) == mm(OX, OZ)
        assert relative_observable(P, v, transpose(X)) == transpose(OX)
        assert relative_observable(P, v, I) == eye(8)
        assert zero(subtract(mm(C, OZ), mm(OZ, C)))
        for w in range(4):
            U = mm(P[w], transpose(P[v]))
            transported = mm(mm(transpose(U), Z), U)
            assert relative_observable(P, w, Z) == relative_observable(P, v, transported)
    # Conditioning agrees with a constraint-commuting observable, for each root basis vector.
    for phi in ([F(1), F(0)], [F(0), F(1)]):
        sections = [mv(p, phi) for p in P]
        history = [x for section in sections for x in section]
        assert not any(mv(C, history))
        for v in range(4):
            conditioned = dot(sections[v], mv(Z, sections[v]))
            O = relative_observable(P, v, Z)
            assert dot(history, mv(O, history))/4 == conditioned
    # Gauge covariance under independent changes of the system basis at vertices.
    G = [Z, R, X, I]
    changed = [(u, v, mm(mm(G[v], U), transpose(G[u]))) for u, v, U in flat_edges]
    C_changed = constraint(4, 2, changed)
    G_total = block_diagonal(G)
    assert C_changed == mm(mm(G_total, C), transpose(G_total))
    pin = [[F(0), F(0)], [F(0), F(1)]]
    H_prep = root_pin(C, pin)
    assert 8-rank(H_prep) == 1
    # Preparation need not commute with relational observables: it is not the gauge constraint.
    O = relative_observable(P, 1, Z)
    assert not zero(subtract(mm(H_prep, O), mm(O, H_prep)))

    # Previous AKLT construction as an actual input, not a newly assigned state table.
    initial = support_vectors(4)[0]
    norm = dot(initial, initial)
    assert norm == 21
    H_AKLT = hamiltonian(4, periodic=True)
    assert not any(mv(H_AKLT, initial))
    rotate = [[F(3, 5), F(0), F(-4, 5)],
              [F(0), F(1), F(0)],
              [F(4, 5), F(0), F(3, 5)]]
    assert mm(transpose(rotate), rotate) == eye(3)
    sections = [initial]
    for _ in range(2):
        sections.append(apply_site(sections[-1], rotate, 0))
    assert all(dot(v, v) == norm for v in sections)
    for t in range(2):
        assert sections[t+1] == apply_site(sections[t], rotate, 0)
    correlations = [zz_expectation(v) for v in sections]
    assert correlations == [F(-10, 21), F(-2, 7), F(2, 15)]
    # One-site marginals stay maximally mixed; two-site relations really change.
    for v in sections:
        w = words(4)
        reduced = [[sum(v[i]*v[j] for i, a in enumerate(w) for j, b in enumerate(w)
                        if a[0] == s and b[0] == t and a[1:] == b[1:])/norm
                    for t in range(3)] for s in range(3)]
        assert reduced == scale(F(1, 3), eye(3))
    gram = [[dot(a, b)/norm for b in sections] for a in sections]
    assert gram == [[F(1), F(11, 15), F(11, 75)],
                    [F(11, 15), F(1), F(11, 15)],
                    [F(11, 75), F(11, 15), F(1)]]
    clock_rho = scale(F(1, 3), gram)
    clock_purity = trace(mm(clock_rho, clock_rho))
    assert clock_purity < 1
    clock_interference = 2*clock_rho[0][1]
    assert clock_interference == F(22, 45)
    degrees = (1, 2, 1)
    dephased_energy = sum(degrees[t]*dot(v, v)/(3*norm)
                          for t, v in enumerate(sections))
    assert dephased_energy == F(4, 3)
    return {
        'status': 'passed', 'arithmetic': 'exact rational; no numerical eigensolvers',
        'diamond_graph': results,
        'flat_dirac_observables': 'commutators, products, adjoints, unit and conditioning verified',
        'gauge_covariance': True, 'preparation_is_not_the_gauge_constraint': True,
        'aklt_input_sites': 4, 'clock_vertices': 3,
        'aklt_conditional_spin_correlations': [str(x) for x in correlations],
        'clock_probability_each_vertex': '1/3',
        'clock_reduced_purity': str(clock_purity),
        'coherent_clock_interference': str(clock_interference),
        'clock_dephased_interference': '0',
        'clock_dephased_constraint_expectation': str(dephased_energy),
        'proof_scope': ['finite-graph kernel and holonomy theorem',
                        'general unital C*-algebra state and Dirac embedding in flat case',
                        'unique preparation and finite spectral-gap lower bound'],
        'not_claimed': ['full general-relativistic problem of time',
                        'derived clock, causal order, arrow, or spacetime metric',
                        'necessary actuality, phenomenal identity, or subject selection'],
    }


if __name__ == '__main__':
    result = run()
    target = Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: exact relational constraint, holonomy, Dirac and AKLT-history checks')
    print(target)
