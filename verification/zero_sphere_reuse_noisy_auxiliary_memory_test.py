"""Auxiliary recovery resources in the actual sphere-coupled reservoir clock.

The family, source state and finite stores are stipulated. This is not an
optimization over arbitrary interactions or an identification of signed charge
with cosmic energy or experience. Probabilities are exact rational numbers.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import log2, sqrt
import unittest

from verification.zero_clock_finite_reservoir_reuse_test import (
    BITS3, FORWARD, INITIAL_N, Q, energy, gate, original_source, weight,
)


def words(n):
    return list(product((0, 1), repeat=n))


def generalized_write(control, bit, level, maximum):
    # Involution preserving bit + level on the entire finite state space.
    if not control:
        return bit, level
    if bit == 0 and level > 0:
        return 1, level - 1
    if bit == 1 and level < maximum:
        return 0, level + 1
    return bit, level


def advance(state, op, cols, reverse=False):
    b, y, memory, n, c, d = state
    typ, index = op
    if typ != 'swap' or index >= 2:
        y, memory, n = gate(b, y, memory, n, op)
    else:
        # The copy uses the A holding f_i *after* swap i. On the inverse
        # the auxiliary operations must be reversed before the swap.
        def copy(memory, c, d, backwards):
            c = list(c)
            order = range(len(c)-1, -1, -1) if backwards else range(len(c))
            for j in order:
                if cols[index][j]:
                    c[j], d = generalized_write(memory[0], c[j], d, 2*len(c))
            return tuple(c), d
        if reverse:
            c, d = copy(memory, c, d, True)
            y, memory, n = gate(b, y, memory, n, op)
        else:
            y, memory, n = gate(b, y, memory, n, op)
            c, d = copy(memory, c, d, False)
    return b, y, memory, n, c, d


def history(b, x, f, e, cols):
    k = len(e)
    state = (b, x, (0,)+f, INITIAL_N, e, k)
    states = [state]
    for op in FORWARD:
        state = advance(state, op, cols)
        states.append(state)
    for op in reversed(FORWARD):
        state = advance(state, op, cols, reverse=True)
        states.append(state)
    return states


def distribution(q, bits):
    return (q ** sum(bits)) * ((1-q) ** (len(bits)-sum(bits)))


def code(f, cols):
    return tuple((f[0]*v0) ^ (f[1]*v1) for v0, v1 in zip(*cols))


def predicted_score(cols, q=Q):
    # R is independent of f; infer its two error bits from the auxiliary c.
    k = len(cols[0])
    return sum((max(distribution(Q, f)*distribution(q, tuple(a^b for a,b in zip(c,code(f,cols))))
                    for f in words(2)) for c in words(k)), F(0))


def best_code(k, q=Q):
    candidates = [(predicted_score(cols, q), cols) for cols in product(words(k), repeat=2)]
    return max(score for score, _ in candidates), [cols for score, cols in candidates if score == max(a for a,_ in candidates)]


def ensemble(cols, q=Q):
    k = len(cols[0])
    for b, x, f, e in product((0, 1), BITS3, BITS3, words(k)):
        w = weight(b,x,f)*distribution(q,e)
        if w:
            yield b,x,f,e,history(b,x,f,e,cols),w


def actual_score(cols, q=Q):
    # Access is R0,R1,R2 and C only; trace out B, references, original
    # sources, purifiers, A and both stores. Conditional states are diagonal.
    d = defaultdict(lambda: defaultdict(F))
    for b,x,f,e,states,w in ensemble(cols,q):
        _, y, mem, n, c, store = states[7]
        d[(mem[1:], c)][original_source(b,x)] += w
    return sum((max(v.values()) for v in d.values()), F(0))


def auxiliary_means(cols, q=Q):
    k=len(cols[0]); start=F(0); end=F(0); store=F(0)
    for b,x,f,e,states,w in ensemble(cols,q):
        _,y,m,n,c,d=states[7]
        start += w*sum(e); end += w*sum(c); store += w*d
    return start,end,store


class SphereReuseNoisyAuxiliaryMemoryTests(unittest.TestCase):
    def test_complete_finite_aux_write_gate(self):
        for k in (1,2,3):
            for control, bit, d in product((0,1),(0,1),range(2*k+1)):
                bit2,d2=generalized_write(control,bit,d,2*k)
                self.assertEqual(bit+d,bit2+d2)
                self.assertEqual(generalized_write(control,bit2,d2,2*k),(bit,d))

    def test_actual_sphere_all_histories_charge_midpoint_and_reversal(self):
        # All possible linear codes through k=2, all prepared branch values.
        # The controls are the same A that interacted with the B-coupled
        # original source; x and f retain their original sphere preparations.
        for k in (0,1,2):
            for cols in product(words(k),repeat=2):
                for b,x,f,e,states,w in ensemble(cols):
                    source=original_source(b,x)
                    for state in states:
                        bb,y,m,n,c,d=state
                        self.assertEqual(bb,b)
                        self.assertEqual(energy(m,n,f),0)
                        self.assertEqual(d-k+sum(c)-sum(e),0)
                    _,y,m,n,c,d=states[7]
                    self.assertEqual(y,source)
                    self.assertEqual(m[1:],(source[0],source[1]^f[0],source[2]^f[1]))
                    self.assertEqual(c,tuple(a^bb for a,bb in zip(e,code(f,cols))))
                    self.assertEqual(states[14],states[0])
                    # The signed charge is conserved even if the purification
                    # bit is not observed, and the full unitary is reversible.

    def test_clock_cycle_is_inverse_for_all_basis_states(self):
        # Representative k=2 code, including battery endpoints and blocked
        # writes on arbitrary states outside the prepared zero sector.
        cols=((1,0),(1,1)); k=2
        for b,yi,mi,n,c,d in product((0,1),BITS3,words(4),range(7),words(k),range(2*k+1)):
            state=(b,yi,mi,n,c,d)
            for op in FORWARD:
                out=advance(state,op,cols)
                self.assertEqual(advance(out,op,cols,reverse=True),state)
                self.assertEqual(n+sum(mi)+d+sum(c),out[3]+sum(out[2])+out[5]+sum(out[4]))

    def test_extended_stationary_clock_coherent_history(self):
        # b, x, f, e label mutually orthogonal sphere sectors, source
        # references and both sets of purifiers; amplitudes may therefore
        # be followed isometrically without constructing a huge dense vector.
        cols=((0,0),(1,1)); h={}; shifted={}
        for b,x,f,e,states,w in ensemble(cols):
            amp=sqrt(float(w)/14)
            for t in range(14):
                key=(t,b,x,f,e,states[t])
                nxt=advance(states[t],FORWARD[t] if t<7 else tuple(reversed(FORWARD))[t-7],cols,reverse=t>=7)
                self.assertEqual(nxt,states[t+1])
                target=((t+1)%14,b,x,f,e,nxt)
                self.assertNotIn(key,h)
                h[key]=amp
                self.assertNotIn(target,shifted)
                shifted[target]=amp
        self.assertEqual(h.keys(),shifted.keys())
        self.assertAlmostEqual(sum(a*a for a in h.values()),1,places=12)
        for key in h:self.assertAlmostEqual(h[key],shifted[key],places=14)
        # D|H>=|H> implies (2I-D-D†)|H>=0; the full map is unitary
        # because every basis step is a bijection and each reversal exact.

    def test_exact_maximum_likelihood_and_linear_code_search(self):
        self.assertEqual(actual_score(((),())), F(9,16))
        for k in (1,2):
            for cols in product(words(k),repeat=2):
                self.assertEqual(actual_score(cols),predicted_score(cols))
        self.assertEqual(best_code(1)[0],F(9,16))
        self.assertEqual(best_code(2)[0],F(81,128))
        self.assertEqual(best_code(3)[0],F(351,512))
        self.assertEqual(actual_score(((0,0),(1,1))),F(81,128))
        self.assertEqual(actual_score(((1,0),(0,1))),F(9,16))

    def test_pure_blanks_outperform_thermal_auxiliaries_in_same_family(self):
        self.assertEqual(best_code(0,F(0))[0],F(9,16))
        self.assertEqual(best_code(1,F(0))[0],F(3,4))
        self.assertEqual(best_code(2,F(0))[0],F(1))
        self.assertEqual(actual_score(((1,),(0,)),F(0)),F(3,4))
        self.assertEqual(actual_score(((1,0),(0,1)),F(0)),F(1))
        # One bit can distinguish at most two of the 4 independent noise
        # patterns; the best mass is P(00)+P(01)=9/16+3/16=3/4.
        self.assertEqual(F(9,16)+F(3,16),F(3,4))

    def test_energy_and_resource_quality(self):
        self.assertEqual(auxiliary_means(((1,),(0,)),F(0)),(F(0),F(1,4),F(3,4)))
        self.assertEqual(auxiliary_means(((1,0),(0,1)),F(0)),(F(0),F(1,2),F(3,2)))
        self.assertEqual(auxiliary_means(((0,0),(1,1)),Q),(F(1,2),F(3,4),F(7,4)))
        h=-.25*log2(.25)-.75*log2(.75)
        self.assertAlmostEqual(h,0.8112781244591328,places=14)
        self.assertLess(2*(1-h),1)

if __name__ == '__main__':
    unittest.main()
