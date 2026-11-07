#!/usr/bin/env python3
"""Exact finite path-constraint, counter, readout and backaction checks.

Uses only rational arithmetic. This is a prescribed history, not a laboratory
clock, autonomous machine, full gravitational model, or phenomenal theory.
"""
from fractions import Fraction as F
from pathlib import Path
import json

M, D = 13, 6  # history vertices; 3 counter values times 2 flag states


def idx(n, flag):
    return 2*n + flag


def gate(edge, s):
    n, flag = divmod(s, 2)
    if edge == 3 and n in (0, 1):
        n = 1-n
    elif edge == 7 and n in (1, 2):
        n = 3-n
    elif edge == 11 and n == 2:
        flag = 1-flag
    return idx(n, flag)


def permute(vec, permutation):
    out = [F(0) for _ in range(D)]
    for source, target in enumerate(permutation):
        out[target] += vec[source]
    return out


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(D))
             for j in range(D)] for i in range(D)]


def dagger(a):
    return [[a[j][i] for j in range(D)] for i in range(D)]


def trace(a):
    return sum(a[i][i] for i in range(D))


def scale(a, factor):
    return [[factor*a[i][j] for j in range(D)] for i in range(D)]


def plus(a, b):
    return [[a[i][j]+b[i][j] for j in range(D)] for i in range(D)]


def rank_exact(a):
    matrix = [row[:] for row in a]
    row = 0
    for col in range(len(matrix[0])):
        pivot = next((r for r in range(row, len(matrix)) if matrix[r][col]), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        leading = matrix[row][col]
        matrix[row] = [v/leading for v in matrix[row]]
        for r in range(len(matrix)):
            if r != row and matrix[r][col]:
                coefficient = matrix[r][col]
                matrix[r] = [x-coefficient*y for x, y in zip(matrix[r], matrix[row])]
        row += 1
        if row == len(matrix):
            break
    return row


def projector(s):
    return [[F(int(i == s and j == s)) for j in range(D)] for i in range(D)]


def unitary(permutation):
    return [[F(int(permutation[j] == i)) for j in range(D)] for i in range(D)]


def constraint(blocks, gates):
    out = [[F(0) for _ in range(D)] for _ in range(M)]
    for t, p in enumerate(gates):
        # B_t^* psi = psi_t - W_t^* psi_(t+1)
        residual = [blocks[t][s]-blocks[t+1][p[s]] for s in range(D)]
        forwarded = permute(residual, p)
        for s in range(D):
            out[t][s] += residual[s]
            out[t+1][s] -= forwarded[s]
    return out


def cyclic_constraint(blocks):
    # Four phase vertices, identity on first three edges, cyclic shift on wrap.
    out = [[F(0) for _ in range(D)] for _ in range(4)]
    for t in range(4):
        target = (t+1) % 4
        p = [idx((s//2+1)%3, s%2) if t == 3 else s for s in range(D)]
        residual = [blocks[t][s]-blocks[target][p[s]] for s in range(D)]
        forwarded = permute(residual, p)
        for s in range(D):
            out[t][s] += residual[s]
            out[target][s] -= forwarded[s]
    return out


def physical_projection_event(blocks, frames, root_index):
    # J P_root J^* with J=(1/sqrt(M)) sum_t |t> V_t.
    amplitude = sum(blocks[t][frames[t][root_index]] for t in range(M))/M
    out = [[F(0) for _ in range(D)] for _ in range(M)]
    for t in range(M):
        out[t][frames[t][root_index]] = amplitude
    return out


def main():
    gates = [[gate(t, s) for s in range(D)] for t in range(M-1)]
    assert all(sorted(p) == list(range(D)) for p in gates)
    frames = [list(range(D))]
    for p in gates:
        frames.append([p[s] for s in frames[-1]])
    # The unnormalized columns of J must be annihilated by the constraint.
    for root in range(D):
        history = [[F(int(s == frames[t][root])) for s in range(D)] for t in range(M)]
        assert not any(x for row in constraint(history, gates) for x in row)
    # Check the exact Dirac-commutator claim on every one of 78 basis vectors.
    for clock in range(M):
        for memory in range(D):
            basis = [[F(int(t == clock and s == memory)) for s in range(D)] for t in range(M)]
            d_then_c = constraint(physical_projection_event(basis, frames, idx(1, 0)), gates)
            c_then_d = physical_projection_event(constraint(basis, gates), frames, idx(1, 0))
            assert d_then_c == c_then_d
    # Verify the chosen blank preparation's prescribed finite counter path.
    q_by_leg = [1, 0, -1, 0]
    decoded = []
    for t in range(M):
        n, flag = divmod(frames[t][idx(0, 0)], 2)
        if t < 12:
            assert (n, flag) == (t//4, 0)
            decoded.append(4*n + t%4)  # tau/a, with q and orientation supplied
            assert decoded[-1] == t
        else:
            assert (n, flag) == (2, 1)  # overflow; not a valid third cycle
    assert [q_by_leg[t % 4] for t in (0, 4, 8)] == [1, 1, 1]
    # Ideal same-event covariance for E=P_(root counter 1), measured at t=4.
    root = idx(1, 0)
    v0, v4 = unitary(frames[0]), unitary(frames[4])
    rho = projector(root)
    event_root = projector(root)
    event0 = matmul(matmul(v0, event_root), dagger(v0))
    event4 = matmul(matmul(v4, event_root), dagger(v4))
    rho0 = matmul(matmul(v0, rho), dagger(v0))
    rho4 = matmul(matmul(v4, rho), dagger(v4))
    p0 = trace(matmul(rho0, event0))
    p4 = trace(matmul(rho4, event4))
    naive = trace(matmul(rho0, projector(idx(0, 0))))
    assert (p0, p4, naive) == (1, 1, 0)
    # Counter/flag readout: projective measurement followed by erasure with e=1/5.
    # The initial density matrix is |(0,0)+(1,0)> / sqrt(2).
    rho_super = [[F(0) for _ in range(D)] for _ in range(D)]
    for i in (idx(0, 0), idx(1, 0)):
        for j in (idx(0, 0), idx(1, 0)):
            rho_super[i][j] = F(1, 2)
    state4 = matmul(matmul(v4, rho_super), dagger(v4))
    epsilon = F(1, 5)
    probabilities = [trace(matmul(projector(s), state4))*(1-epsilon) for s in range(D)]
    probabilities.append(epsilon*trace(state4))
    assert sum(probabilities) == 1
    assert probabilities[idx(0, 0)] == probabilities[idx(1, 0)] == F(2, 5)
    assert probabilities[-1] == F(1, 5)
    dephased = [[state4[i][j] if i == j else F(0) for j in range(D)] for i in range(D)]
    assert dephased[idx(0, 0)][idx(1, 0)] == 0
    assert state4[idx(0, 0)][idx(1, 0)] == F(1, 2)
    # Check the entire anchored instrument and a subsequent noncommuting
    # plus-effect in BOTH frames, not just a single marginal probability.
    post_root, post_frame4 = [], []
    erase = [[F(0) for _ in range(D)] for _ in range(D)]
    erase4 = [[F(0) for _ in range(D)] for _ in range(D)]
    for s in range(D):
        p = projector(s)
        effect4 = matmul(matmul(v4, p), dagger(v4))
        root_piece = matmul(matmul(p, rho_super), p)
        frame_piece = matmul(matmul(effect4, state4), effect4)
        post_root.append(scale(root_piece, 1-epsilon))
        post_frame4.append(scale(frame_piece, 1-epsilon))
        erase = plus(erase, scale(root_piece, epsilon))
        erase4 = plus(erase4, scale(frame_piece, epsilon))
    post_root.append(erase)
    post_frame4.append(erase4)
    assert sum(trace(post) for post in post_root) == 1
    plus_root = rho_super
    plus4 = matmul(matmul(v4, plus_root), dagger(v4))
    two_event_probabilities = []
    for post, computed_frame_post in zip(post_root, post_frame4):
        transformed_post = matmul(matmul(v4, post), dagger(v4))
        assert computed_frame_post == transformed_post
        prob_root = trace(matmul(plus_root, post))
        prob_frame4 = trace(matmul(plus4, computed_frame_post))
        assert prob_root == prob_frame4
        two_event_probabilities.append(prob_root)
    assert two_event_probabilities[idx(0, 0)] == F(1, 5)
    assert two_event_probabilities[idx(1, 0)] == F(1, 5)
    assert two_event_probabilities[-1] == F(1, 10)
    # A strictly periodic four-vertex clock with a one-step wrap shift has
    # nontrivial holonomy. A sharp blank counter violates its wrap constraint.
    periodic_blank = [[F(1, 2) if s == idx(0, 0) else F(0)
                       for s in range(D)] for _ in range(4)]
    residual_state = cyclic_constraint(periodic_blank)
    periodic_blank_energy = sum(periodic_blank[t][s]*residual_state[t][s]
                                for t in range(4) for s in range(D))
    assert periodic_blank_energy == F(1, 2)
    # Uniform counter superposition (unnormalized) satisfies the cyclic constraint.
    periodic_uniform = [[F(int(s in (idx(0, 0), idx(1, 0), idx(2, 0))))
                         for s in range(D)] for _ in range(4)]
    assert not any(x for row in cyclic_constraint(periodic_uniform) for x in row)
    cyclic_shift = [idx((s//2+1)%3, s%2) for s in range(D)]
    shift_matrix = unitary(cyclic_shift)
    shift_minus_identity = [[shift_matrix[i][j]-F(int(i == j)) for j in range(D)] for i in range(D)]
    fixed_dimension = D-rank_exact(shift_minus_identity)
    assert fixed_dimension == 2
    # On the prepared blank path the overflow flag is 1 at t=12.
    over = frames[12][idx(0, 0)]
    assert divmod(over, 2) == (2, 1)
    result = {'clock_vertices': M, 'memory_dimension': D, 'constraint_kernel_dimension': D,
              'valid_decoded_tau_over_a': decoded,
              'overflow_counter_flag': [2, 1],
              'overflow_detected_probability': str(1-epsilon),
              'overflow_erased_probability': str(epsilon),
              'same_event_probabilities_frame_0_and_4': [str(p0), str(p4)],
              'incorrect_same_matrix_probability_frame_0': str(naive),
              'readout_probabilities_for_counter_0_1_erasure': [str(F(2, 5)), str(F(2, 5)), str(epsilon)],
              'joint_probabilities_counter_0_1_erasure_then_plus':
                  [str(two_event_probabilities[idx(0, 0)]), str(two_event_probabilities[idx(1, 0)]), str(two_event_probabilities[-1])],
              'discarded_readout_trace_distance_for_chosen_superposition': '1/2',
              'basis_vectors_checked_for_dirac_commutator': M*D,
              'cyclic_clock_blank_history_constraint_expectation': str(periodic_blank_energy),
              'cyclic_clock_uniform_counter_is_zero_mode': True,
              'cyclic_counter_fixed_subspace_dimension_with_flag': fixed_dimension,
              'scope': 'finite engineered history; no physical laboratory, gravity or phenomenal claim'}
    path = Path(__file__).with_name('finite_turning_counter.json')
    assert result['same_event_probabilities_frame_0_and_4'] == ['1', '1']
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    print('PASS: exact finite constraint, counter, frame comparison and complete readout.')


if __name__ == '__main__':
    main()
