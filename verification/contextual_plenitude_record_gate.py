#!/usr/bin/env python3
"""Peres–Mermin projectors and explicit contextual couplings; no subject inference."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import prod
import json

I = [[1, 0], [0, 1]]
X = [[0, 1], [1, 0]]
Y = [[0, -1j], [1j, 0]]
Z = [[1, 0], [0, -1]]

def kron(a, b):
    return [[a[i//2][j//2]*b[i%2][j%2] for j in range(4)] for i in range(4)]
def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def plus(a, b):
    return [[a[i][j]+b[i][j] for j in range(4)] for i in range(4)]
def scaled(a, c):
    return [[c*v for v in row] for row in a]

eye = kron(I, I)
ops = [kron(X,I), kron(I,X), kron(X,X),
       kron(I,Y), kron(Y,I), kron(Y,Y),
       kron(X,Y), kron(Y,X), kron(Z,Z)]
contexts = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8)]
target = [1,1,1,1,1,-1]

for ids, sign in zip(contexts, target):
    for i in ids:
        for j in ids:
            assert mm(ops[i], ops[j]) == mm(ops[j], ops[i])
    term = eye
    for i in ids:
        term = mm(term, ops[i])
    assert term == scaled(eye, sign)

# Projectors for rho=I/4; exact binary arithmetic suffices for these matrices.
quantum = []
for ids, sign in zip(contexts, target):
    dist = {}
    for outcomes in product((-1, 1), repeat=3):
        projector = eye
        for i, result in zip(ids, outcomes):
            projector = mm(projector, scaled(plus(eye, scaled(ops[i], result)), 0.5))
        trace = sum(projector[i][i] for i in range(4))
        assert abs(trace.imag) < 1e-12
        p = Fraction(round(trace.real), 4)
        assert p == (Fraction(1,4) if prod(outcomes)==sign else 0)
        dist[outcomes] = p
    quantum.append(dist)

# Independent unitary instrument: for each of three commuting observables,
# H--controlled-O--H copies its eigenvalue to one of three pointer qubits.
# Indices are system_basis * 8 + pointer_bits. This is a coherent record,
# not an irreversible detector or a model of experience.
def hadamard_pointer(v, bit):
    mask = 4 >> bit
    out = [0j] * 32
    for s in range(4):
        for b in range(8):
            amplitude = v[8*s+b] / (2 ** 0.5)
            out[8*s+(b & ~mask)] += amplitude
            out[8*s+(b | mask)] += -amplitude if b & mask else amplitude
    return out

def controlled_observable(v, bit, observable):
    mask = 4 >> bit
    out = [0j] * 32
    for s in range(4):
        for b in range(8):
            if b & mask:
                for t in range(4):
                    out[8*t+b] += observable[t][s] * v[8*s+b]
            else:
                out[8*s+b] += v[8*s+b]
    return out

def instrument(v, ids, reverse=False):
    order = range(2, -1, -1) if reverse else range(3)
    for bit in order:
        v = hadamard_pointer(v, bit)
        v = controlled_observable(v, bit, ops[ids[bit]])
        v = hadamard_pointer(v, bit)
    return v

for c, ids in enumerate(contexts):
    # Check reversal on a complete basis, including initially nonzero pointers.
    for basis in range(32):
        vector = [0j]*32
        vector[basis] = 1
        recovered = instrument(instrument(vector, ids), ids, reverse=True)
        assert max(abs(a-b) for a,b in zip(vector, recovered)) < 1e-12
    counts = {o:0.0 for o in quantum[c]}
    for system_basis in range(4):
        vector = [0j]*32
        vector[8*system_basis] = 1
        output = instrument(vector, ids)
        for outcome in counts:
            bits = sum(((1-val)//2) * (4>>i) for i,val in enumerate(outcome))
            counts[outcome] += sum(abs(output[8*s+bits])**2 for s in range(4))/4
    assert all(abs(counts[o]-float(quantum[c][o])) < 1e-12 for o in counts)

# Any context-independent deterministic value assignment fails an odd number
# of the six parity conditions; count all 512 assignments.
all_assignments = list(product((-1,1), repeat=9))
def failures(values):
    return tuple(c for c, ids in enumerate(contexts)
                 if prod(values[i] for i in ids) != target[c])
hist = Counter(len(failures(v)) for v in all_assignments)
assert hist == {1:96, 3:320, 5:96}

# For all 2^18 context-indexed tables, the sum of parity failures and
# row/column mismatches is odd and hence at least one. Taking expectations
# gives the union-bound tradeoff used in the report for arbitrary couplings.
min_defects = 99
for r in all_assignments:
    row_fails = sum(prod(r[i] for i in contexts[c]) != target[c] for c in range(3))
    for q in all_assignments:
        col_fails = sum(prod(q[i] for i in contexts[c]) != target[c] for c in range(3,6))
        defects = row_fails + col_fails + sum(a != b for a,b in zip(r,q))
        assert defects % 2 == 1
        min_defects = min(min_defects, defects)
assert min_defects == 1

# One mismatch per complete table: the row value and column value of one
# selected observable differ; other identifications are preserved.
coupling = []
for mismatched in range(9):
    records = []
    for values in all_assignments:
        rowvals = values
        colvals = tuple(-v if i==mismatched else v for i,v in enumerate(values))
        all_ok = all(prod((rowvals if c<3 else colvals)[i] for i in ids) == target[c]
                     for c,ids in enumerate(contexts))
        if all_ok:
            records.append((rowvals, colvals))
    assert len(records)==16
    coupling.extend(records)
assert len(coupling)==144
for c,ids in enumerate(contexts):
    observed = Counter(tuple((r if c<3 else q)[i] for i in ids) for r,q in coupling)
    assert {o:Fraction(observed[o],144) for o in quantum[c]} == quantum[c]
assert all(sum(r[i]!=q[i] for i in range(9))==1 for r,q in coupling)
mismatch = [Fraction(sum(r[i]!=q[i] for r,q in coupling),144) for i in range(9)]
assert mismatch == [Fraction(1,9)]*9

# A context-independent mixture of all 96 one-failure tables realizes the
# fully symmetric noisy family with parity error 1/6, uniformly within each
# parity class. This is a sharp feasibility example, not an experimental bound.
noncontextual = [v for v in all_assignments if len(failures(v))==1]
assert len(noncontextual)==96
for c,ids in enumerate(contexts):
    d=Counter(tuple(v[i] for i in ids) for v in noncontextual)
    for outcome in product((-1,1),repeat=3):
        expected = Fraction(5,24) if prod(outcome)==target[c] else Fraction(1,24)
        assert Fraction(d[outcome],96)==expected

result = {'status':'passed', 'scope':'ideal two-qubit model and abstract finite couplings, not experiments or subjects',
          'operator_context_signs': target,
          'quantum_nonzero_probabilities_per_context': [4]*6,
          'probability_each_allowed_outcome': '1/4',
          'reversible_pointer_instrument_contexts': 6,
          'pointer_reverse_basis_checks': 192,
          'pointer_instrument_matches_projectors': True,
          'global_value_assignment_failure_histogram': dict(sorted(hist.items())),
          'context_indexed_tables_checked_for_odd_defects': len(all_assignments)**2,
          'minimum_parity_plus_mismatch_defects': min_defects,
          'contextual_coupling_microstates': len(coupling),
          'mismatches_per_microstate': 1,
          'mismatch_probability_per_connection': '1/9',
          'sharp_noise_noncontextual_joint_tables': len(noncontextual),
          'symmetric_context_parity_error': '1/6'}
print(json.dumps(result,indent=2))
