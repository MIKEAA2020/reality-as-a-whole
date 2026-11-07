#!/usr/bin/env python3
"""Exact finite subject-factorization gate; no phenomenal or empirical inference."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json
import math

STATES = tuple(product((0, 1), repeat=2))
INDEX = {s: i for i, s in enumerate(STATES)}
PERMS = tuple(permutations(range(4)))
ACTIONS = tuple(product(range(4), repeat=4))


def observable_partition(values):
    """Binary observable modulo swapping its two output labels."""
    blocks = (frozenset(i for i, b in enumerate(values) if b == 0),
              frozenset(i for i, b in enumerate(values) if b == 1))
    return frozenset(blocks)


partitions = frozenset(observable_partition(v) for v in product((0, 1), repeat=4)
                       if sum(v) == 2)
assert len(partitions) == 3
factorizations = frozenset(frozenset(c) for c in combinations(partitions, 2))


def permute_partition(part, perm):
    return frozenset(frozenset(perm[s] for s in block) for block in part)


def permute_factors(factors, perm):
    return frozenset(permute_partition(part, perm) for part in factors)


def bits(part):
    # Arbitrary binary output labeling is harmless for factorization.
    zero = min(part, key=lambda b: tuple(sorted(b)))
    return tuple(int(i not in zero) for i in range(4))


def kernel(p, q):
    return tuple(tuple((p if x != a else 1-p) * (q if y != b else 1-q)
                       for a, b in STATES) for x, y in STATES)


def defect(K, factors):
    """Maximum of product-TV defect and local marginal-TV defect."""
    p1, p2 = sorted(factors, key=lambda f: sorted(sorted(b) for b in f))
    f, g = bits(p1), bits(p2)
    mf = [[sum(K[s][t] for t in range(4) if f[t] == out)
           for out in (0, 1)] for s in range(4)]
    mg = [[sum(K[s][t] for t in range(4) if g[t] == out)
           for out in (0, 1)] for s in range(4)]
    product_tv = max(sum(abs(K[s][t] - mf[s][f[t]] * mg[s][g[t]])
                         for t in range(4)) / 2 for s in range(4))
    local = max([F(0)] + [abs(mf[s][0] - mf[r][0]) for s in range(4) for r in range(4)
                           if f[s] == f[r]]
                + [abs(mg[s][0] - mg[r][0]) for s in range(4) for r in range(4)
                   if g[s] == g[r]])
    return max(product_tv, local)


def independent_local_factors(K, factors):
    p1, p2 = sorted(factors, key=lambda f: sorted(sorted(b) for b in f))
    f, g = bits(p1), bits(p2)
    # A complete factorization has each binary output pair exactly once.
    assert len({(f[i], g[i]) for i in range(4)}) == 4
    marg1 = [[sum(K[s][t] for t in range(4) if f[t] == out)
              for out in (0, 1)] for s in range(4)]
    marg2 = [[sum(K[s][t] for t in range(4) if g[t] == out)
              for out in (0, 1)] for s in range(4)]
    for s in range(4):
        for t in range(4):
            if K[s][t] != marg1[s][f[t]] * marg2[s][g[t]]:
                return False
        for r in range(4):
            if f[s] == f[r] and marg1[s] != marg1[r]:
                return False
            if g[s] == g[r] and marg2[s] != marg2[r]:
                return False
    return True


def xy_to_uv(s):
    x, y = s
    return (x, x ^ y)


def conjugate_kernel(K, perm):
    out = [[None]*4 for _ in range(4)]
    for s in range(4):
        for t in range(4):
            out[perm[s]][perm[t]] = K[s][t]
    return tuple(tuple(row) for row in out)


def clamp(s, c):
    return tuple(s[i] if c[i] is None else c[i] for i in range(2))


def main():
    uniform = kernel(F(1, 2), F(1, 2))
    generic = kernel(F(1, 4), F(1, 3))
    assert all(independent_local_factors(uniform, f) for f in factorizations)
    winners = frozenset(f for f in factorizations if independent_local_factors(generic, f))
    assert len(winners) == 1
    xpart = observable_partition(tuple(s[0] for s in STATES))
    ypart = observable_partition(tuple(s[1] for s in STATES))
    zpart = observable_partition(tuple(s[0] ^ s[1] for s in STATES))
    assert winners == frozenset((frozenset((xpart, ypart)),))
    scores = {'XY': defect(generic, frozenset((xpart, ypart))),
              'XZ': defect(generic, frozenset((xpart, zpart))),
              'YZ': defect(generic, frozenset((ypart, zpart)))}
    assert scores == {'XY': F(0), 'XZ': F(1, 8), 'YZ': F(2, 9)}

    # A fully symmetric uniform kernel plus all deterministic state operations,
    # with action identities conjugated under relabeling, has S4 automorphisms.
    assert all(conjugate_kernel(uniform, perm) == uniform for perm in PERMS)
    orbit = {permute_factors(next(iter(factorizations)), p) for p in PERMS}
    assert orbit == factorizations
    fixed_factorizations = [f for f in factorizations
                            if all(permute_factors(f, p) == f for p in PERMS)]
    assert not fixed_factorizations
    invariant_subsets = []
    for n in range(4):
        for selected in combinations(factorizations, n):
            selected = frozenset(selected)
            if all(frozenset(permute_factors(f, p) for f in selected) == selected
                   for p in PERMS):
                invariant_subsets.append(len(selected))
    assert sorted(invariant_subsets) == [0, 3]
    operations_checked = 0
    for perm in PERMS:
        inv = tuple(perm.index(i) for i in range(4))
        for action in ACTIONS:
            conjugated = tuple(perm[action[inv[i]]] for i in range(4))
            assert conjugated in ACTIONS
            for s in range(4):
                assert conjugated[perm[s]] == perm[action[s]]
                for t in range(4):
                    assert uniform[action[s]][t] == uniform[conjugated[perm[s]]][perm[t]]
            operations_checked += 1

    # Coordinate mixing is an exact bijection, with all actions transported.
    enc = tuple(INDEX[xy_to_uv(s)] for s in STATES)
    assert len(set(enc)) == 4
    for perm in PERMS:
        Kperm = conjugate_kernel(generic, perm)
        mapped_winners = frozenset(f for f in factorizations if independent_local_factors(Kperm, f))
        assert mapped_winners == frozenset(permute_factors(f, perm) for f in winners)
        for f in factorizations:
            assert defect(generic, f) == defect(Kperm, permute_factors(f, perm))
    encK = conjugate_kernel(generic, enc)
    encoded_winners = frozenset(f for f in factorizations if independent_local_factors(encK, f))
    assert encoded_winners == frozenset(permute_factors(f, enc) for f in winners)
    u = observable_partition(tuple(s[0] for s in STATES))
    v = observable_partition(tuple(s[1] for s in STATES))
    uxv = observable_partition(tuple(s[0] ^ s[1] for s in STATES))
    assert encoded_winners == frozenset((frozenset((u, uxv)),))
    assert frozenset((u, v)) not in encoded_winners
    # Same physical x/y hard clamps, expressed as transformed joint operations.
    clamp_cases = 0
    for c in product((None, 0, 1), repeat=2):
        for s in STATES:
            old = INDEX[clamp(s, c)]
            mapped = enc[old]
            # Explicit transformed operation: decode, clamp x/y, encode.
            uu, vv = xy_to_uv(s)
            a = uu if c[0] is None else c[0]
            b = (uu ^ vv) if c[1] is None else c[1]
            assert mapped == INDEX[(a, a ^ b)]
            for t in range(4):
                assert generic[old][t] == encK[mapped][enc[t]]
            clamp_cases += 1

    # At any starting state, joint increments in encoded coordinates are correlated.
    joint = F(1, 4) * (1-F(1, 3))
    uflip = F(1, 4)
    vflip = F(1, 4) + F(1, 3) - 2*F(1, 4)*F(1, 3)
    assert (joint, uflip*vflip) == (F(1, 6), F(5, 48))
    n = math.ceil(192**2 * math.log(32 / .05) / 2)
    assert n == 119098 and 32 * math.exp(-2 * n / 192**2) <= .05
    receipt = {
        'status': 'passed',
        'states': 4,
        'balanced_binary_observables_up_to_complement': len(partitions),
        'complete_two_factor_decompositions': len(factorizations),
        'state_permutations': len(PERMS),
        'all_deterministic_state_operations': len(ACTIONS),
        'permutation_operation_equivariance_cases': operations_checked,
        'uniform_kernel_factorizations_passing': 3,
        'uniform_kernel_invariant_factorization_selection_sizes': sorted(invariant_subsets),
        'generic_kernel_factorizations_passing': len(winners),
        'generic_factorization_defects': {name: str(value) for name, value in scores.items()},
        'sampling_bound_n_per_starting_state': n,
        'sampling_failure_union_bound': 32 * math.exp(-2 * n / 192**2),
        'generic_old_coordinates_factors': ['x', 'y'],
        'generic_encoded_factors': ['u', 'u XOR v'],
        'old_coordinate_clamp_state_cases': clamp_cases,
        'encoded_joint_flip_probability': str(joint),
        'encoded_product_of_flip_marginals': str(uflip*vflip),
        'scope': 'Finite classical exact model; candidate factorization gate only. No conscious subjects, physical substrate or phenomenology established. A coordinate change transports operations; independent native coordinate clamps are not automatically equivalent.'
    }
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
