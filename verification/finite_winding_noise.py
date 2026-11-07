#!/usr/bin/env python3
"""Exact rational finite-window counter, flag and noisy instrument checks.

This enumerates one specified finite constrained-history instrument. It does not
simulate cold atoms, derive autonomous hardware, or prove quantum gravity.
"""
from fractions import Fraction as F
from pathlib import Path
import json

U = ((F(3, 5), F(-4, 5)), (F(4, 5), F(3, 5)))
ID = ((F(1), F(0)), (F(0), F(1)))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def power(n):
    a = U if n >= 0 else tuple(tuple(U[j][i] for j in range(2)) for i in range(2))
    out = ID
    for _ in range(abs(n)):
        out = matmul(a, out)
    return out


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(2)) for i in range(2))


def advance(m, f, modulus):
    return ((m+1) % modulus, f ^ int(m == modulus-1))


def retreat(m, f, modulus):
    return ((m-1) % modulus, f ^ int(m == 0))


def move(m, f, steps, modulus):
    for _ in range(abs(steps)):
        m, f = advance(m, f, modulus) if steps >= 0 else retreat(m, f, modulus)
    return m, f


def distribution(K, offset_probability, slip, erasure):
    """Enumerate r, reported (raw counter,flag) or ?, and qubit x."""
    length, modulus = 2*K+1, 2*K+3
    vertices = 4*length
    result = {}
    for w in range(-K, K+1):
        for r in range(4):
            system = power(4*w+r)
            for d, prior in ((0, 1-offset_probability), (1, offset_probability)):
                raw0 = K+1+d
                raw, flag = move(raw0, 0, w, modulus)
                base = prior/F(vertices)
                readouts = [('?', erasure), ((raw, flag), (1-erasure)*(1-slip)),
                            (((raw+1)%modulus, flag), (1-erasure)*slip)]
                for report, chance in readouts:
                    for x in (0, 1):
                        key = (r, report, x)
                        result[key] = result.get(key, F(0)) + base*chance*system[x][0]**2
    return result


def main():
    K, lam, slip, erasure = 2, F(1, 2), F(1, 10), F(1, 5)
    length, modulus, vertices = 2*K+1, 2*K+3, 4*(2*K+1)
    for m in range(modulus):
        for f in (0, 1):
            assert retreat(*advance(m, f, modulus), modulus) == (m, f)
            assert advance(*retreat(m, f, modulus), modulus) == (m, f)
    assert advance(modulus-1, 0, modulus) == (0, 1)
    assert move(modulus-1, 0, 2*modulus, modulus) == (modulus-1, 0)
    assert matmul(transpose(U), U) == ID
    # Exact path transport V_j: test every edge, counter state and flag.
    for w in range(-K, K+1):
        for r in range(4):
            if w == K and r == 3:
                continue
            w2, r2 = (w, r+1) if r < 3 else (w+1, 0)
            assert matmul(U, power(4*w+r)) == power(4*w2+r2)
            for c in range(modulus):
                for flag in (0, 1):
                    before = move(c, flag, w, modulus)
                    after = before if r < 3 else advance(*before, modulus)
                    assert after == move(c, flag, w2, modulus)
    for w in range(-K, K+1):
        for d in (0, 1):
            raw, flag = move(K+1+d, 0, w, modulus)
            assert raw == K+1+d+w and flag == 0
    # The measured full register includes j/m/flag in a hidden Kraus record.
    # Distinct offsets therefore leave orthogonal records and their coherences
    # disappear when that record is traced, for this particular instrument.
    for w in range(-K, K+1):
        assert move(K+1, 0, w, modulus) != move(K+2, 0, w, modulus)
    data = distribution(K, lam, slip, erasure)
    assert sum(data.values()) == 1
    total_erasure = sum(p for (r, y, x), p in data.items() if y == '?')
    assert total_erasure == erasure
    label = (K+1, 0)  # reported signed counter m=0, flag=0
    event = sum(p for (r, y, x), p in data.items() if r == 0 and y == label)
    p0 = data.get((0, label, 0), F(0))
    assert event == F(1, 25)
    conditional = p0/event
    ideal = F(334177, 390625)
    p1 = F(277729, 390625)
    p2 = F(164833, 390625)**2
    closed = (1-slip)*((1-lam)+lam*p1)+slip*((1-lam)*p1+lam*p2)
    assert conditional == closed == F(621334959941, 762939453125)
    bound = slip*(p1-p2)
    assert abs(conditional-ideal) <= bound
    # Adversarial parameter sweep, including extreme calibration/slip rates.
    cases = 0
    for test_K in (2, 3, 5):
        for test_lam in (F(0), F(1, 4), F(1, 2), F(1)):
            for test_slip in (F(0), F(1, 10), F(1)):
                for test_erasure in (F(0), F(1, 5)):
                    obs = distribution(test_K, test_lam, test_slip, test_erasure)
                    obs_label = (test_K+1, 0)
                    denom = sum(p for (r, y, x), p in obs.items() if r == 0 and y == obs_label)
                    assert denom == (1-test_erasure)/F(4*(2*test_K+1))
                    observed = obs.get((0, obs_label, 0), F(0))/denom
                    reference = (1-test_lam)+test_lam*p1
                    expected = (1-test_slip)*reference+test_slip*((1-test_lam)*p1+test_lam*p2)
                    assert observed == expected
                    assert abs(observed-reference) <= test_slip*(p1-p2)
                    cases += 1
    # Independent nonselective offset backaction check. For each hidden
    # (j,c) branch, V† (P_c ⊗ P_x) V leaves the chosen offset label fixed.
    # Sum the output qubit norms with initial weight 1/2 and clock weight 1/T.
    offset_populations = [F(0), F(0)]
    for w in range(-K, K+1):
        for r in range(4):
            uk = power(4*w+r)
            inverse = transpose(uk)
            for x in (0, 1):
                # U^-k P_x U^k |0> in the root qubit basis.
                branch = tuple(inverse[i][x]*uk[x][0] for i in range(2))
                branch_norm = sum(a*a for a in branch)
                for d in (0, 1):
                    offset_populations[d] += branch_norm/F(2*vertices)
    assert offset_populations == [F(1, 2), F(1, 2)]
    # Distinct c labels at each j make all off-diagonal d terms vanish; the
    # trace distance of |+><+| and diag(1/2,1/2) is exactly 1/2.
    # Uniform finite clock is a chosen finite history model, not an infinite
    # invariant probability. Its graph constraint is checked in a separate
    # general finite-history construction.
    result = {'clock_vertices': vertices, 'counter_states': modulus, 'flag_bits': 1,
              'counter_initial_offset_probabilities': [str(1-lam), str(lam)],
              'slip_probability': str(slip), 'erasure_probability': str(erasure),
              'instrument_outcome_probability_sum': str(sum(data.values())),
              'total_erasure_probability': str(total_erasure),
              'phase0_reported_zero_probability': str(event),
              'ideal_comparison_probability': str(ideal),
              'noisy_conditional_probability': str(conditional),
              'noisy_conditional_decimal': float(conditional),
              'bias': str(conditional-ideal), 'bias_decimal': float(conditional-ideal),
              'uniform_offset_prior_bias_bound': str(bound),
              'parameter_sweep_cases': cases,
              'nonselective_offset_populations': [str(x) for x in offset_populations],
              'nonselective_offset_trace_distance_from_coherent_input': '1/2',
              'single_wrap_flagged': list(advance(modulus-1, 0, modulus)),
              'two_wrap_flag_not_latched': list(move(modulus-1, 0, 2*modulus, modulus)),
              'scope': 'specific finite history and declared instrument; no independent hardware or gravitational claim'}
    path = Path(__file__).with_name('finite_winding_noise.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    print('PASS: finite counter permutations, complete probabilities and noise formula.')


if __name__ == '__main__':
    main()
