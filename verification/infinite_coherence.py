"""Exact finite checks for the all-size construction in INFINITE_COHERENCE_CONSTRUCTION.md.

Standard AKLT / finitely correlated state mathematics; not an experience model.
Only standard-library integers and fractions. Run from any working directory.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

# Pauli labels I,X,Y,Z. Each entry is (power of i, product label).
MUL = (
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 1), (0, 0), (1, 3), (3, 2)),
    ((0, 2), (3, 3), (0, 0), (1, 1)),
    ((0, 3), (1, 2), (3, 1), (0, 0)),
)


def pauli_word(word):
    phase, label = 0, 0
    for s in word:
        k, label = MUL[s + 1][label]
        phase = (phase + k) % 4
    return phase, label


def words(n):
    return tuple(product(range(3), repeat=n))


def overlap(a, b):
    """One half Tr(P_b^* P_a), real on equal-length words."""
    ka, la = pauli_word(a)
    kb, lb = pauli_word(b)
    if la != lb:
        return 0
    delta = (ka - kb) % 4
    assert delta in (0, 2)
    return 1 if delta == 0 else -1


def density(n, identity_sector=False):
    w = words(n)
    return [[F(overlap(a, b), 3**n)
             if not identity_sector or pauli_word(a)[1] == 0 else F(0)
             for b in w] for a in w]


def mm(a, b):
    bt = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col)) for col in bt] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def partial_end(rho, n, first=False):
    w = words(n-1)
    def index(t):
        out = 0
        for x in t:
            out = 3*out + x
        return out
    return [[sum(rho[index((k,)+a if first else a+(k,))]
                       [index((k,)+b if first else b+(k,))]
                 for k in range(3)) for b in w] for a in w]


def parent_term():
    return [[F((a == c and b == d) + (a == d and b == c), 2)
             - F(a == b and c == d, 3)
             for c, d in words(2)] for a, b in words(2)]


def hamiltonian(n, periodic=False):
    w = words(n)
    lookup = {a: i for i, a in enumerate(w)}
    h = parent_term()
    out = [[F(0) for _ in w] for _ in w]
    edges = [(i, i+1) for i in range(n-1)]
    if periodic:
        edges.append((n-1, 0))
    for col, a in enumerate(w):
        for i, j in edges:
            for c, d in words(2):
                value = h[3*c+d][3*a[i]+a[j]]
                if value:
                    b = list(a)
                    b[i], b[j] = c, d
                    out[lookup[tuple(b)]][col] += value
    return out


def rank(matrix):
    a = [list(row) for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x/p for x in a[r]]
        for i in range(r+1, len(a)):
            if a[i][c]:
                k = a[i][c]
                a[i] = [x-k*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def support_vectors(n):
    w = words(n)
    out = []
    for label in range(4):
        reference = next((pauli_word(a)[0] for a in w
                          if pauli_word(a)[1] == label), None)
        if reference is None:
            continue
        v = []
        for a in w:
            k, l = pauli_word(a)
            if l != label:
                v.append(F(0))
            else:
                assert (k-reference) % 4 in (0, 2)
                v.append(F(1 if (k-reference) % 4 == 0 else -1))
        out.append(v)
    return out


def periodic_reduction(n, total):
    """Direct contraction of the finite-ring pure vector, not the limit formula."""
    w = words(n)
    raw = [[0 for _ in w] for _ in w]
    count = 0
    for rest in words(total-n):
        v = []
        for a in w:
            phase, label = pauli_word(a+rest)
            if label != 0:
                v.append(0)
            else:
                # Every identity-sector amplitude has a common real/imag phase.
                relative = (phase - (total % 2)) % 4
                assert relative in (0, 2)
                v.append(1 if relative == 0 else -1)
        count += sum(x*x for x in v)
        for i, x in enumerate(v):
            if x:
                for j, y in enumerate(v):
                    raw[i][j] += x*y
    assert count
    return [[F(x, count) for x in row] for row in raw], count


# Gaussian rationals, used only for the 2x2 transfer calculation in Pauli basis.
def gadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def gmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


ZERO = (F(0), F(0))
PHASE = ((F(1), F(0)), (F(0), F(1)),
         (F(-1), F(0)), (F(0), F(-1)))


def insert(observable, b):
    """E_O(B) = sum O_st sigma_s B sigma_t / 3, exact Pauli coefficients."""
    out = [ZERO for _ in range(4)]
    for s in range(3):
        for t in range(3):
            for label, value in enumerate(b):
                k1, l1 = MUL[s+1][label]
                k2, l2 = MUL[l1][t+1]
                z = gmul(gmul(observable[s][t], value), PHASE[(k1+k2) % 4])
                out[l2] = gadd(out[l2], (z[0]/3, z[1]/3))
    return out


def run():
    rho = {n: density(n) for n in range(1, 5)}
    for n, r in rho.items():
        assert trace(r) == 1
        assert r == [list(x) for x in zip(*r)]
        if n > 1:
            assert partial_end(r, n) == rho[n-1]
            assert partial_end(r, n, first=True) == rho[n-1]
        for v in support_vectors(n):
            label = next(pauli_word(a)[1] for a, x in zip(words(n), v) if x)
            eigen = (F(1+3*F(-1, 3)**n, 4) if label == 0
                     else F(1-F(-1, 3)**n, 4))
            assert [sum(x*y for x, y in zip(row, v)) for row in r] == [eigen*x for x in v]
    assert rho[1] == [[F(i == j, 3) for j in range(3)] for i in range(3)]
    e01, e10 = [[F(0)]*3 for _ in range(3)], [[F(0)]*3 for _ in range(3)]
    e01[0][1], e10[1][0] = F(1), F(1)
    assert mm(e01, e10) != mm(e10, e01)
    h = parent_term()
    assert mm(h, h) == h
    assert rank(h) == 5
    assert mm(h, rho[2]) == [[0]*9 for _ in range(9)]
    open_dimensions = {}
    for n in range(2, 5):
        H = hamiltonian(n)
        open_dimensions[n] = 3**n-rank(H)
        assert open_dimensions[n] == 4
        for v in support_vectors(n):
            assert all(sum(x*y for x, y in zip(row, v)) == 0 for row in H)
    ring = hamiltonian(4, periodic=True)
    assert 81-rank(ring) == 1
    ring_vector = support_vectors(4)[0]  # scalar Pauli sector, hence trace vector
    assert all(sum(x*y for x, y in zip(row, ring_vector)) == 0 for row in ring)
    pt = [[rho[2][3*(i//3)+j%3][3*(j//3)+i%3]
           for j in range(9)] for i in range(9)]
    diagonal_indices = (0, 4, 8)
    pt_witness = sum(pt[i][j] for i in diagonal_indices for j in diagonal_indices)/3
    assert pt_witness == F(-1, 9)
    finite_rings = []
    for total in range(4, 9):
        for n in (1, 2, 3):
            direct, count = periodic_reduction(n, total)
            q = F(-1, 3)
            r, r0 = density(n), density(n, identity_sector=True)
            norm = 1+3*q**total
            expected = [[(r[i][j]+q**(total-n)*(4*r0[i][j]-r[i][j]))/norm
                         for j in range(3**n)] for i in range(3**n)]
            assert direct == expected
            assert F(4*count, 3**total) == norm
            scalar_weight = (1+3*q**n)/4
            delta_scalar = (3*q**(total-n)-3*q**total)/norm
            delta_other = (-q**(total-n)-3*q**total)/norm
            trace_error = abs(delta_scalar)*scalar_weight + abs(delta_other)*(1-scalar_weight)
            assert trace_error <= 6*F(1, 3)**(total-n)
            finite_rings.append({'ring_sites': total, 'block_sites': n,
                                 'trace_norm_error': str(trace_error),
                                 'max_entry_error': str(max(abs(direct[i][j]-r[i][j])
                                                          for i in range(3**n) for j in range(3**n)))})
    one = [PHASE[0], ZERO, ZERO, ZERO]
    identity = [[PHASE[0] if i == j else ZERO for j in range(3)] for i in range(3)]
    spin = [[ZERO, PHASE[3], ZERO], [PHASE[1], ZERO, ZERO], [ZERO, ZERO, ZERO]]
    for label in range(4):
        basis = [ZERO]*4
        basis[label] = PHASE[0]
        expected = [ZERO]*4
        expected[label] = PHASE[0] if label == 0 else (F(-1, 3), F(0))
        assert insert(identity, basis) == expected
    spin_squared = [[PHASE[0] if i == j and i < 2 else ZERO
                     for j in range(3)] for i in range(3)]
    assert insert(spin_squared, one)[0] == (F(2, 3), F(0))
    for n in range(2, 5):
        direct = ZERO
        for i, a in enumerate(words(n)):
            for j, b in enumerate(words(n)):
                if a[1:-1] == b[1:-1]:
                    z = gmul(spin[b[0]][a[0]], spin[b[-1]][a[-1]])
                    direct = gadd(direct, (rho[n][i][j]*z[0], rho[n][i][j]*z[1]))
        assert direct == (F(4, 3)*F(-1, 3)**(n-1), F(0))
    correlations = []
    for distance in range(1, 13):
        b = insert(spin, one)
        for _ in range(distance-1):
            b = insert(identity, b)
        value = insert(spin, b)[0]
        predicted = F(4, 3)*F(-1, 3)**distance
        assert value == (predicted, F(0))
        correlations.append(str(predicted))
    structure_factors = {}
    cutoff = 12
    for name, cosines, c in [('0', (1,), F(1)), ('pi', (-1, 1), F(-1)),
                              ('pi/2', (0, -1, 0, 1), F(0))]:
        approx = F(2, 3)+2*sum(F(correlations[d-1])*cosines[(d-1) % len(cosines)]
                               for d in range(1, cutoff+1))
        closed = 2*(1-c)/(5+3*c)
        assert abs(approx-closed) <= 4*F(1, 3)**(cutoff+1)
        structure_factors[name] = str(closed)
    return {
        'status': 'passed',
        'model': 'standard spin-1 AKLT / Pauli finitely correlated state',
        'arithmetic': 'integers, fractions, Gaussian rationals; no floating-point checks',
        'local_state': 'I3/3', 'two_site_partial_transpose_witness': str(pt_witness),
        'open_ground_dimensions': open_dimensions, 'four_site_ring_ground_dimension': 1,
        'finite_ring_reductions': finite_rings, 'spin_correlations_distances_1_to_12': correlations,
        'structure_factor': structure_factors,
        'proofs_not_replaced_by_checks': ['all-size positivity and consistency',
             'open-chain kernel dimension for every N>=2', 'periodic uniqueness for every N>=4',
             'unique quasi-local state extension and periodic thermodynamic limit'],
        'not_derived': ['local dimension and lattice', 'why the parent law is actual or necessary',
             'physical spacetime, constants, or brain organization',
             'qualitative identities, subject incidence, value, or absolute actuality'],
    }


if __name__ == '__main__':
    result = run()
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: exact finite checks for infinite coherence construction')
    print(output)
