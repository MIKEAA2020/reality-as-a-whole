#!/usr/bin/env python3
"""Exact checks for an infinite clock with a correlated winding counter.

Finite-support tests of the rigging identity and rational two-clock examples.
The model is idealized, not a physical clock or a quantum-gravity solution.
"""
from fractions import Fraction as F
from pathlib import Path
import json

U = ((F(3, 5), F(-4, 5)), (F(4, 5), F(3, 5)))
ID = ((F(1), F(0)), (F(0), F(1)))
ZERO = (F(0), F(0))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(2)) for i in range(2))


def power(n):
    a = U if n >= 0 else transpose(U)
    out = ID
    for _ in range(abs(n)):
        out = matmul(a, out)
    return out


def apply(a, v):
    return tuple(sum(a[i][j]*v[j] for j in range(2)) for i in range(2))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def inner(a, b):
    return sum(x*y for x, y in zip(a, b))


def shift(state, n):
    return {(k+n, d): apply(power(n), vector) for (k, d), vector in state.items()}


def state_inner(a, b):
    return sum(inner(v, b.get(key, ZERO)) for key, v in a.items())


def rig(state):
    out = {}
    for (k, d), v in state.items():
        out[d] = add(out.get(d, ZERO), apply(power(-k), v))
    return out


def rig_inner(a, b):
    return sum(inner(v, b.get(d, ZERO)) for d, v in a.items())


def w_frame(root, w, r):
    return {w+d: apply(power(4*w+r), v) for d, v in root.items()}


def m_frame(root, m, r):
    return {m-d: apply(power(4*(m-d)+r), v) for d, v in root.items()}


def frame_change(state, w, m):
    # Input key is m' = w+d; output key is w'=m-d.
    out = {}
    for m_prime, v in state.items():
        d = m_prime-w
        w_prime = m-d
        out[w_prime] = apply(power(4*(w_prime-w)), v)
    return out


def inverse_frame_change(state, w, m):
    out = {}
    for w_prime, v in state.items():
        d = m-w_prime
        m_prime = w+d
        out[m_prime] = apply(power(4*(w-w_prime)), v)
    return out


def norm2(state):
    return sum(inner(v, v) for v in state.values())


def main():
    f = {(0, 0): (F(1), F(0)), (2, 0): (F(0), F(1)),
         (-1, 1): (F(1, 2), F(-1, 3))}
    g = {(-2, 0): (F(2, 3), F(1, 5)), (1, 0): (F(1, 4), F(2, 5)),
         (3, 1): (F(-1, 3), F(3, 7))}
    differences = {kf-kg for (kf, df) in f for (kg, dg) in g if df == dg}
    average = sum(state_inner(f, shift(g, n)) for n in differences)
    assert average == rig_inner(rig(f), rig(g))
    assert rig(shift(f, 1)) == rig(f)
    assert rig_inner(rig(f), rig(f)) >= 0
    # Clock k=4w+r; d=m-w is unchanged both at ordinary edges and wraps.
    for w in range(-3, 4):
        for r in range(4):
            for m in range(-3, 4):
                w2, r2, m2 = (w, r+1, m) if r < 3 else (w+1, 0, m+1)
                assert m2-w2 == m-w
                assert 4*w2+r2 == 4*w+r+1
    # Unnormalized physical state: (|d=0>+|d=1>)|0>; norm^2=2.
    root = {0: (F(1), F(0)), 1: (F(1), F(0))}
    state_w = w_frame(root, 0, 0)
    state_m = m_frame(root, 0, 0)
    assert frame_change(state_w, 0, 0) == state_m
    assert inverse_frame_change(state_m, 0, 0) == state_w
    assert norm2(state_w) == norm2(state_m) == 2
    varied_root = {-2: (F(1, 3), F(2, 7)), 0: (F(1), F(-1, 2)),
                   3: (F(-2, 5), F(4, 9))}
    for w, m, r in ((-1, 2, 3), (2, -1, 1), (0, 0, 2)):
        left, right = w_frame(varied_root, w, r), m_frame(varied_root, m, r)
        assert frame_change(left, w, m) == right
        assert inverse_frame_change(right, w, m) == left
        assert norm2(left) == norm2(right)
    p_w_bare = sum(v[0]**2 for v in state_w.values())/norm2(state_w)
    p_m_bare = sum(v[0]**2 for v in state_m.values())/norm2(state_m)
    assert p_w_bare == 1
    assert p_m_bare == F(334177, 390625)
    # General offset probability λ: independently evaluate the two branch
    # predictions and compare to the closed calibration-sensitivity formula.
    p_offset1 = apply(power(-4), (F(1), F(0)))[0]**2
    calibration_curve = {}
    for lam in (F(0), F(1, 4), F(1, 2), F(1)):
        probability = (1-lam) + lam*p_offset1
        assert probability == 1 - F(112896, 390625)*lam
        calibration_curve[str(lam)] = str(probability)
    # Same root event P0, transported to the m-frame, is blockwise rotated.
    anchored_probability = F(0)
    for w_prime, v in state_m.items():
        pulled_back = apply(power(-4*w_prime), v)
        anchored_probability += pulled_back[0]**2
    anchored_probability /= norm2(state_m)
    assert anchored_probability == 1
    result = {'rigging_group_average_exact': True,
              'rigging_invariant_under_shift': True,
              'rigging_test_inner_product': str(average),
              'counter_offset_conserved_on_sampled_edges': True,
              'frame_change_and_inverse_exact': True,
              'bare_system_P0_at_w0_phase0': str(p_w_bare),
              'bare_system_P0_at_m0_phase0': str(p_m_bare),
              'offset_uncertainty_calibration_curve': calibration_curve,
              'same_anchored_event_in_m_frame': str(anchored_probability),
              'unwrapped_parent_clock_supplied': True,
              'scope': 'finite-support rational checks of a specified infinite idealization; not a lab or gravity result'}
    path = Path(__file__).with_name('infinite_winding_clock.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
    print('PASS: exact finite-support and two-frame checks; infinite claims are analytic.')


if __name__ == '__main__':
    main()
