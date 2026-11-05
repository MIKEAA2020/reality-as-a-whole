"""Finite-time activity-clock checks and a bounded processed-source comparison.

Standard library only. Never imports or executes the external analysis code.
Exact rational generator identities are distinct from experimental fit validity.
See CLASSICAL_TICK_READOUT.md for proofs, limitations and source accounting.
"""
import ast
import base64
from fractions import Fraction as F
import hashlib
import itertools
import json
import math
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parent


def solve(a, b):
    n = len(b)
    m = [[F(x) for x in row] + [F(y)] for row, y in zip(a, b)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if m[i][k])
        m[k], m[pivot] = m[pivot], m[k]
        scale = m[k][k]
        m[k] = [x / scale for x in m[k]]
        for i in range(n):
            if i != k:
                scale = m[i][k]
                m[i] = [x - scale * y for x, y in zip(m[i], m[k])]
    return [row[-1] for row in m]


def mv(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def stationary(q):
    n = len(q)
    p = solve(q[:-1] + [[1] * n], [0] * (n - 1) + [1])
    assert all(x > 0 for x in p) and sum(p) == 1
    assert mv(q, p) == [0] * n
    return p


def statistics(q):
    """Column generator; signed current counts 2 -> 0 minus 0 -> 2."""
    n = len(q)
    assert all(sum(q[j][i] for j in range(n)) == 0 for i in range(n))
    p = stationary(q)
    gamma = [-q[i][i] for i in range(n)]
    assert all(g > 0 for g in gamma)
    # Departure-weight clock has drift exactly 1, bracket rate 1 / Gamma_i.
    for i in range(n):
        assert sum(q[j][i] / gamma[i] for j in range(n) if j != i) == 1
        assert sum(q[j][i] / gamma[i] ** 2 for j in range(n) if j != i) == 1 / gamma[i]
    variance_rate = sum(p[i] / gamma[i] for i in range(n))
    b1 = [[F(0) for _ in range(n)] for _ in range(n)]
    b2 = [[F(0) for _ in range(n)] for _ in range(n)]
    b1[0][2], b1[2][0] = q[0][2], -q[2][0]
    b2[0][2], b2[2][0] = q[0][2], q[2][0]
    b1p = mv(b1, p)
    drift = sum(b1p)
    rhs = [drift * p[i] - b1p[i] for i in range(n)]
    h = solve(q[:-1] + [[1] * n], rhs[:-1] + [0])
    assert mv(q, h) == rhs and sum(h) == 0
    diffusion = sum(mv(b2, p)) + 2 * sum(mv(b1, h))
    assert diffusion > 0
    # Markov path-time-reversal entropy of the fitted generator, not calorimetry.
    sigma = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            f, r = p[i] * q[j][i], p[j] * q[i][j]
            assert f > 0 and r > 0
            sigma += float(f - r) * math.log(float(f / r))
    s_net = float(drift ** 2 / diffusion)
    assert s_net <= sigma / 2 + 1e-12
    return p, gamma, variance_rate, {
        'stationary_probability': [float(x) for x in p],
        'exit_rates_per_second': [float(x) for x in gamma],
        'activity_variance_rate_seconds': float(variance_rate),
        'activity_precision_per_second': float(1 / variance_rate),
        'signed_current_per_second': float(drift),
        'signed_current_variance_rate_per_second': float(diffusion),
        'signed_current_precision_per_second': s_net,
        'fitted_path_entropy_rate_in_kB_per_second': sigma,
    }


def npy_matrix(raw):
    """Strict non-pickle decoder for the archived 3x3 little-endian f64 arrays."""
    assert raw[:8] == b'\x93NUMPY\x01\x00'
    length = struct.unpack('<H', raw[8:10])[0]
    header = ast.literal_eval(raw[10:10 + length].decode('ascii'))
    assert header == {'descr': '<f8', 'fortran_order': False, 'shape': (3, 3)}
    values = struct.unpack('<9d', raw[10 + length:])
    assert all(math.isfinite(x) for x in values)
    return [[F(str(values[3 * i + j])) for j in range(3)] for i in range(3)]


def main():
    # Exact equilibrium witness; NOT fitted to the experimental device.
    gamma = list(map(F, [2, 3, 6]))
    q = [[-gamma[i] if j == i else gamma[i] / 2 for i in range(3)] for j in range(3)]
    p, g, variance, result = statistics(q)
    assert p == [F(1, 2), F(1, 3), F(1, 6)]
    assert variance == F(7, 18)
    assert result['signed_current_per_second'] == 0
    assert result['fitted_path_entropy_rate_in_kB_per_second'] == 0
    assert all(p[i] * q[j][i] == p[j] * q[i][j] for i in range(3) for j in range(3) if i != j)
    # Integer accumulator delta=1/6 sec. Verify every path up to eight jumps.
    paths_checked = 0
    for n in range(9):
        for path in itertools.product(range(3), repeat=n + 1):
            if any(a == b for a, b in zip(path, path[1:])):
                continue
            departed = sum((1 / g[i] for i in path[:-1]), F(0))
            visited = sum((1 / g[i] for i in path), F(0))
            assert visited - departed == 1 / g[path[-1]]
            counter = sum([3, 2, 1][i] for i in path[:-1])
            assert departed == F(counter, 6)
            assert 0 <= counter <= 3 * n
            # Conditional controlled translations on a finite cyclic register
            # are permutations; wrap is excluded for paths of <= n jumps.
            capacity = 3 * n + 1
            for w in (1, 2, 3):
                assert sorted((a + w) % capacity for a in range(capacity)) == list(range(capacity))
            paths_checked += 1
    # Correctly labelled independent thinning is an ideal observation channel,
    # not a model of the experiment's correlated finite-bandwidth missed jumps.
    thinning = []
    for eta in map(F, ['1', '0.5', '0.1']):
        for i in range(3):
            assert eta * g[i] * (1 / (eta * g[i])) == 1
            assert eta * g[i] * (1 / (eta * g[i])) ** 2 == 1 / (eta * g[i])
        thinning.append({'efficiency': float(eta), 'precision_per_second': float(eta / variance)})
    archive = json.loads((ROOT / 'sources/wadhia_2025/processed_sample.json').read_text())
    decoded = {}
    for item in archive['files']:
        raw = base64.b64decode(item['base64'], validate=True)
        assert len(raw) == item['bytes']
        assert hashlib.sha256(raw).hexdigest() == item['sha256']
        assert hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() == item['git_blob_sha1']
        decoded[item['path']] = raw
    assert (ROOT / 'sources/wadhia_2025/LICENSE.txt').read_bytes() == decoded['LICENSE']
    samples = []
    for channel in ('B-V-K3', 'PCA--K3'):
        path = f'data/+0.005 bias/5187/{channel}/M.npy'
        original = npy_matrix(decoded[path])
        errors = npy_matrix(decoded[path.replace('/M.npy', '/M_err.npy')])
        assert all(x >= 0 for row in errors for x in row)
        # Rebuild each diagonal from the archived off-diagonals: enforce exact
        # rational zero column sums rather than treating rounding as leakage.
        q = [row[:] for row in original]
        for i in range(3):
            assert all(q[j][i] > 0 for j in range(3) if i != j)
            q[i][i] = -sum(q[j][i] for j in range(3) if i != j)
        adjustment = max(abs(q[i][i] - original[i][i]) for i in range(3))
        assert adjustment < F('1e-12')
        *_, stats = statistics(q)
        samples.append({'source_path': path,
                        'max_diagonal_normalization_per_second': float(adjustment),
                        'scope': 'Central processed fit only; errors archived, not propagated; no exact-equilibrium claim.',
                        **stats})
    # Uniformization/Chernoff finite-duration register provision. The proof
    # supplies the probability bound; this is a floating-point evaluation.
    duration, event_limit = 10, 99
    mu = float(max(gamma) * duration)
    threshold = event_limit + 1
    assert threshold > mu
    capacity = 3 * event_limit + 1
    overflow = math.exp(-mu + threshold * (1 + math.log(mu / threshold)))
    assert capacity == 298 and (capacity - 1).bit_length() == 9
    assert 0 < overflow < 0.000016
    output = {
        'status': 'PASS',
        'finite_horizon_register': {
            'duration_seconds': duration, 'provisioned_departures': event_limit,
            'capacity': capacity, 'bits': (capacity - 1).bit_length(),
            'uniformization_poisson_mean': mu,
            'overflow_chernoff_upper_bound': overflow,
        },
        'scope': 'Exact specified-model identities plus processed-generator arithmetic; not raw-data or RF/DC energy replication.',
        'equilibrium_witness': {**result, 'paths_checked': paths_checked,
                                'integer_tick_seconds': '1/6',
                                'exact_variance_rate_seconds': '7/18',
                                'exact_precision_per_second': '18/7'},
        'ideal_marked_thinning': thinning,
        'processed_source_commit': archive['commit'],
        'processed_samples': samples,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
