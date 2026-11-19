#!/usr/bin/env python3
"""Check factor-graph augmentation and conditioning, not consciousness.

The standard auxiliary-variable factorization is described in Wainwright and
Jordan, appendix E.3, DOI 10.1561/2200000001. This finite example applies it
without claiming the conversion is a new method.
"""
from fractions import Fraction as F
from itertools import product
from math import log2
from pathlib import Path
import json

states = list(product((0, 1), repeat=3))
# Rational 3-way parity factor: 2 for even parity, 1 for odd.
def weight(a):
    return 2 if sum(a) % 2 == 0 else 1

Z = sum(weight(x) for x in states)
p = {x: F(weight(x), Z) for x in states}
# One auxiliary variable A has 8 possible values. Its unary potential is
# weight(A); three pair factors each enforce A_i = x_i.
q = {(x,a): F(weight(a), Z) * int(all(x[i] == a[i] for i in range(3)))
     for x in states for a in states}
assert sum(q.values()) == sum(p.values()) == 1
assert all(sum(q[x,a] for a in states) == p[x] for x in states)
assert all(sum(q[x,a] for x in states) == p[a] for a in states)

# All evidence patterns include wildcard None and assignments 0/1. Compare
# posterior probabilities for all original configurations, not interventions.
count = 0
for evidence in product((None, 0, 1), repeat=3):
    compatible = lambda x: all(v is None or x[i] == v for i,v in enumerate(evidence))
    base_event = sum(p[x] for x in states if compatible(x))
    aug_event = sum(q[x,a] for x in states for a in states if compatible(x))
    assert base_event == aug_event and base_event > 0
    for x in states:
        before = p[x] / base_event if compatible(x) else F(0)
        after = sum(q[x,a] for a in states) / aug_event if compatible(x) else F(0)
        assert before == after
    count += 1

# The augmented representation uses three binary variables plus one 8-state
# auxiliary, not four interchangeable physical binary units.
entropy = -sum(float(v)*log2(float(v)) for v in p.values())
joint_entropy = -sum(float(v)*log2(float(v)) for v in q.values() if v)
assert abs(entropy-joint_entropy) < 1e-12
result = {
 'status':'passed',
 'source_antecedent':'Wainwright and Jordan, Graphical Models, Exponential Families, and Variational Inference, Appendix E.3, DOI 10.1561/2200000001',
 'scope':'two exact finite probabilistic representations, not physical implementations or an experience assay',
 'original_variables':3,
 'auxiliary_representation_variables':4,
 'auxiliary_domain_size':8,
 'original_3_way_potential':'2 for even parity, 1 for odd parity',
 'partition_function': Z,
 'augmented_factors':'one unary auxiliary weight and three pairwise deterministic equality constraints',
 'identical_original_joint_probabilities':True,
 'matching_original_variable_evidence_conditions':count,
 'entropy_original_bits': entropy,
 'entropy_augmented_joint_bits': joint_entropy,
 'naive_one_subject_per_graph_variable_original':3,
 'naive_one_subject_per_graph_variable_augmented':4,
 'limitations':'conditioning is not intervention; auxiliary is an abstract encoding, not an added physical component; no model describes phenomenal facts.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
