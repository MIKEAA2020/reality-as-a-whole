"""Explicit reversible registers on the existing four-spin history model.

The spin transition is the original classical stochastic heat-bath kernel.
Record and output gates are reversible Boolean permutations. Registers and
phenomenal identity are added proposals, not evidence of an actual subject.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import unittest

from verification.coupled_subject_boundary_gate import STATES, stationary
from verification.integrated_subject_horizon_audit import kernel, mismatch

ZERO=(0,0,0,0)  # memories m0,m1 and outputs level,onset
REGS=tuple(product((0,1),repeat=4))


def xor_bit(reg, index, value):
    result=list(reg)
    result[index]^=value
    return tuple(result)


def save_before(s, reg):
    return xor_bit(reg,0,mismatch(s))


def save_after(s, reg):
    return xor_bit(reg,1,mismatch(s))


def write_level(reg):
    return xor_bit(reg,2,reg[1])


def write_onset(reg):
    return xor_bit(reg,3,reg[1]*(1-reg[0]))


def outputs(reg):
    return write_onset(write_level(reg))


def undo_outputs(reg):
    return write_level(write_onset(reg))


def write_selected(reg6):
    """Reversible public-output XOR using mode z and candidate channels.

    Six registers are (m0,m1,level,onset,z,Y); z=0 selects level, z=1
    selects onset. The selector has no presumed experiential semantics.
    """
    a,b,l,o,z,y=reg6
    return (a,b,l,o,z,y ^ (o if z else l))


def law():
    """Full exact final law P(final spin, m0,m1,L,O), not postselected."""
    pi=stationary(F(1,4),(None,)*4)
    k=kernel(F(1,4))
    result=defaultdict(F)
    for before, p in pi.items():
        reg=save_before(before,ZERO)
        for now, prob in k[before].items():
            r=outputs(save_after(now,reg))
            result[(now,r)] += p*prob
    return result


def y_error(p, report_index, target):
    return sum(mass for (_,reg),mass in p.items() if reg[report_index] != target(reg))


class ConstitutiveSubjectAccessCircuitTests(unittest.TestCase):
    def test_gates_are_permutations_and_support_dirty_memory(self):
        # All memory states, not only the ready configuration, are included.
        for spin in STATES:
            for gate in (save_before,save_after):
                images={gate(spin,r) for r in REGS}
                self.assertEqual(images,set(REGS))
                for r in REGS:
                    self.assertEqual(gate(spin,gate(spin,r)),r)
        for gate in (write_level,write_onset):
            self.assertEqual({gate(r) for r in REGS},set(REGS))
            for r in REGS:
                self.assertEqual(gate(gate(r)),r)
        for r in REGS:
            self.assertEqual(undo_outputs(outputs(r)),r)

    def test_all_spin_histories_and_ready_output_functions(self):
        for before in STATES:
            for now in STATES:
                reg=outputs(save_after(now,save_before(before,ZERO)))
                a,b=mismatch(before),mismatch(now)
                self.assertEqual(reg,(a,b,b,int(a==0 and b==1)))

    def test_joint_distribution_and_original_spin_kernel_preserved(self):
        p=law(); self.assertEqual(sum(p.values()),1)
        hist=defaultdict(F); outputs_hist=defaultdict(F); final=defaultdict(F)
        for (spin,r),mass in p.items():
            a,b,l,o=r
            hist[a,b]+=mass; outputs_hist[l,o]+=mass; final[spin]+=mass
        self.assertEqual(dict(hist),{(0,0):F(295,448),(0,1):F(41,448),
                                    (1,0):F(41,448),(1,1):F(71,448)})
        self.assertEqual(dict(outputs_hist),{(0,0):F(336,448),
                                             (1,1):F(41,448),
                                             (1,0):F(71,448)})
        self.assertEqual(dict(final),stationary(F(1,4),(None,)*4))
        self.assertEqual(sum(hist.values()),1)

    def test_one_fixed_report_selects_a_candidate_only_given_bridge(self):
        p=law()
        level=lambda r:r[1]
        onset=lambda r:int(r[0]==0 and r[1]==1)
        self.assertEqual(y_error(p,2,level),0)
        self.assertEqual(y_error(p,2,onset),F(71,448))
        self.assertEqual(y_error(p,3,onset),0)
        self.assertEqual(y_error(p,3,level),F(71,448))
        # Both outputs coexist in the very same physical state; selection of
        # either as a quality witness is extra, not supplied by the circuit.
        self.assertEqual(sum(mass for (_,r),mass in p.items() if r[2]!=r[3]),F(71,448))

    def test_single_selected_public_output_is_a_reversible_gate(self):
        regs=tuple(product((0,1),repeat=6))
        self.assertEqual({write_selected(r) for r in regs},set(regs))
        for r in regs:
            self.assertEqual(write_selected(write_selected(r)),r)
        p=law()
        for z in (0,1):
            for (_,r),mass in p.items():
                a,b,l,o=r
                out=write_selected((a,b,l,o,z,0))
                self.assertEqual(out[-1],l if z==0 else o)
                self.assertEqual(out[-2],z)
        # z=0 is one fixed output channel, even when two candidate registers
        # exist. z=1 is a distinct physical selector preparation.
        err_level=sum(m for (_,r),m in p.items()
                      if write_selected((*r,0,0))[-1] != r[1])
        err_onset=sum(m for (_,r),m in p.items()
                      if write_selected((*r,0,0))[-1] != int(r[0]==0 and r[1]==1))
        self.assertEqual((err_level,err_onset),(0,F(71,448)))

    def test_at_matched_current_state_history_memory_enables_onset(self):
        p=law(); now=(1,-1,1,1)
        found={r for (s,r),mass in p.items() if s==now and mass>0}
        self.assertIn((0,1,1,1),found)
        self.assertIn((1,1,1,0),found)
        # Earlier full-current-state-only Bayes error is removed because the
        # physical state is now larger and carries the extra history bit.
        for (s,r),mass in p.items():
            if mass:
                self.assertEqual(r[3],int(r[0]==0 and r[1]==1))

    def test_no_closed_reset_of_distinct_records_with_same_final_spin(self):
        p=law(); now=(1,-1,1,1)
        r0=(0,1,1,1); r1=(1,1,1,0)
        self.assertGreater(p[now,r0],0); self.assertGreater(p[now,r1],0)
        self.assertNotEqual((now,r0),(now,r1))
        # A purported reset holding final spin fixed and clearing ALL four
        # registers sends two distinct supported inputs to the same output.
        proposed_reset=lambda pair:(pair[0],ZERO)
        self.assertEqual(proposed_reset((now,r0)),proposed_reset((now,r1)))
        # Therefore it cannot be a permutation on the modeled closed state.
        # Clearing a single register can be reversible if information remains
        # in the other registers; entropy/heat is not quantified here.

    def test_inverse_record_gates_at_same_spin(self):
        for spin in STATES:
            for r in REGS:
                out=outputs(save_after(spin,save_before(spin,r)))
                restored=save_before(spin,save_after(spin,undo_outputs(out)))
                self.assertEqual(restored,r)
        # This same-spin algebra does not invert the stochastic heat-bath
        # step: that would require an explicit reversible dilation and access
        # to its recorded randomness/environment.


if __name__=='__main__':
    unittest.main()
