#!/usr/bin/env python3
"""Bounded organization/realization checks; no consciousness or physics inference."""
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
bits = (0, 1)
# Target organization: state x, externally supplied input i, output x;
# abstract state transition T(x,i)=x XOR i.
def target(x, i):
    return x ^ i

# Two distinct stipulated implementation types: physical code b = x XOR k.
# k=0 and k=1 are treated as distinct physical descriptions/types, not
# evidence that silicon or biology can implement the proposed organizations.
def decode(b, k):
    return b ^ k

def step(b, i, k):
    return b ^ i

def clamp_x(b, a, k):
    return a ^ k

def bad_step(b, i):
    return b  # matches the observed zero-input trajectory but ignores input

rows = []
for k, b, i in product(bits, repeat=3):
    x = decode(b, k)
    out = decode(step(b, i, k), k)
    assert out == target(x, i)
    for a in bits:
        assert decode(clamp_x(b, a, k), k) == a
    rows.append((k, b, i))

# A trace alone is insufficient: the two laws agree on a four-step observed
# trajectory at x=0 with inputs 0, yet disagree for both states on input 1.
x_good = x_bad = 0
for _ in range(4):
    x_good = target(x_good, 0)
    x_bad = bad_step(x_bad, 0)
    assert x_good == x_bad == 0
failures = [(x, i) for x, i in product(bits, repeat=2)
            if target(x, i) != bad_step(x, i)]
assert failures == [(0, 1), (1, 1)]

# For two indistinguishable disjoint copies, enumerate candidate subsets of
# {L,R}; a selector based solely on swap-symmetric input must be swap-invariant.
candidates = [frozenset(c) for n in range(4)
              for c in [[s for j, s in enumerate(('L', 'R')) if n & (1 << j)]]]
def swap(c):
    return frozenset({'L': 'R', 'R': 'L'}[s] for s in c)
invariant = [sorted(c) for c in candidates if swap(c) == c]
assert invariant == [[], ['L', 'R']]

# Physical/functional facts do not force one independently anchored
# qualitative assignment. Both maps are transported across the encodings.
for x in bits:
    for f in (lambda v: v, lambda v: 1-v):
        from_encoding_0 = f(decode(x ^ 0, 0))
        from_encoding_1 = f(decode(x ^ 1, 1))
        assert from_encoding_0 == from_encoding_1 == f(x)
assert [0, 1] != [1, 0]

result = {
    'scope': 'Finite stipulated local input-output/state toy. Labels and transition equations neither establish implementation in nature nor determine experiences, their subjects, actual possibility, existence, physics, or time.',
    'target': 'x_next=x XOR i; output=x',
    'encoded_transition_checks': len(rows),
    'encoded_clamp_checks': len(rows)*2,
    'training_trace_steps': 4,
    'bad_law_disagreements': failures,
    'swap_invariant_candidate_subsets': invariant,
    'qualitative_maps': {'q1':[0,1], 'q2':[1,0]},
    'note': 'Two qualitative assignments are alternative stipulated anchored interpretations, not empirical evidence of different experiences or genuinely possible worlds.'
}
(ROOT / 'verification/substrate_self_existent_interface.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
