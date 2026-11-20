#!/usr/bin/env python3
"""Exact integer checks of quantum access structures, not subject counts.

Cleve-Gottesman-Lo (2,3) code, used on one and two logical qutrits.
All states use implicit amplitude 3^(-n/2). No floating point or NumPy.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json

F = range(3)
PAIRS = tuple(combinations(range(3), 2))


def physical(s, r):
    """Each party's local tuple is (r_l + party*s_l) mod 3."""
    return tuple(tuple((r[l] + a*s[l]) % 3 for l in range(len(s)))
                 for a in range(3))


def states(n):
    return tuple(product(F, repeat=n))


def word(s):
    return tuple(physical(s, r) for r in states(len(s)))


def trace_single(a, b, party):
    """Unnormalized matrix of Tr_other(|V a><V b|)."""
    counts = Counter()
    keep = [j for j in range(3) if j != party]
    for x in word(a):
        for y in word(b):
            if all(x[j] == y[j] for j in keep):
                counts[(x[party], y[party])] += 1
    return +counts


def decode_pair(x, pair):
    i, j = pair
    k = ({0, 1, 2} - set(pair)).pop()
    # inverse of j-i mod 3; output secret and would-be missing value
    inv = pow((j-i) % 3, -1, 3)
    secret = tuple(((x[j][l]-x[i][l])*inv) % 3 for l in range(len(x[i])))
    q = tuple((x[i][l] + (k-i)*secret[l]) % 3 for l in range(len(x[i])))
    return secret, q, x[k]


checks = {}
for n in (1, 2):
    logical = states(n)
    d = 3**n
    # All matrix units, including off-diagonal coherences: the complementary
    # singleton channel is rho -> Tr(rho)*I/d even with a reference system.
    singles = 0
    for party in range(3):
        for a in logical:
            for b in logical:
                actual = trace_single(a, b, party)
                expected = Counter({(x, x): 1 for x in logical}) if a == b else Counter()
                assert actual == expected, (n, party, a, b, actual, expected)
                singles += 1

    # Every pair decoder is a bijective permutation on physical pair basis.
    # For each input basis vector the leftover state is a fixed maximally
    # entangled pair, independent of input; linearity covers reference states.
    perms = decodes = 0
    for pair in PAIRS:
        mappings = []
        i,j = pair
        for xi in logical:
            for xj in logical:
                allx = [None]*3
                allx[i], allx[j] = xi, xj
                allx[({0,1,2}-set(pair)).pop()] = (0,)*n
                secret, q, _ = decode_pair(tuple(allx), pair)
                mappings.append((secret, q))
        assert len(set(mappings)) == d*d
        perms += len(mappings)
        for s in logical:
            qs=[]
            for x in word(s):
                got, q, missing = decode_pair(x, pair)
                assert got == s and q == missing
                qs.append(q)
                decodes += 1
            assert set(qs) == set(logical)
    checks[str(n)] = {'logical_dimension':d,'single_party_matrix_unit_checks':singles,
                      'decoder_basis_permutation_entries':perms,
                      'encoded_basis_term_decodes':decodes}

# Fix the second input in the same 9-dimensional local physical space to |0>.
# Relative to this restricted code family every singleton remains blind to s,
# and every pair decodes s. With both inputs free, the Boolean access family
# remains unchanged, while the allowed logical dimension grows 3 -> 9.
restricted = [(x, 0) for x in F]
for a in restricted:
    for b in restricted:
        for party in range(3):
            assert trace_single(a,b,party) == (Counter({(x,x):1 for x in states(2)}) if a==b else Counter())
        for pair in PAIRS:
            for x in word(a):
                secret,q,missing=decode_pair(x,pair)
                assert secret == a and q == missing

# Each authorized pair intersects every other; the single-share intersection
# is unauthorized. No two pair recoveries are on disjoint resources.
assert all(set(p)&set(q) and len(set(p)&set(q)) == 1 for p,q in combinations(PAIRS,2))
result = {'status':'passed','encoder':'Cleve-Gottesman-Lo ((2,3)) code, tensor powers',
          'minimal_authorized_sets':['AB','AC','BC'],
          'singleton_authorized':False,'any_pair_can_recover_full_secret':True,
          'pairwise_intersection_is_authorized':False,
          'common_physical_local_dimension':9,
          'restricted_logical_dimension':3,'unrestricted_logical_dimension':9,
          'checks':checks,
          'scope':'exact ideal finite quantum models; no empirical, consciousness, or subject-count inference'}
text=json.dumps(result,indent=2)+'\n'
Path(__file__).with_suffix('.json').write_text(text)
print(text)
