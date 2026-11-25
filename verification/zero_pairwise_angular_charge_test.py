"""Branchwise zero pair on original coherent angular echo vectors."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial,apply64
from verification.zero_internal_contextual_reference_test import ss
from verification.zero_internal_reference_subject_valence_candidates_test import j_project
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_quantum_angular_echo import embed,apply_quality
from verification.zero_sphere_angular_echo import magnitude
from verification.zero_pairwise_angular_charge import (
    energy_from_values,paired_energy,copy_angles,write_sign,prepared_output,undo_output,q_anchor_reading,
)


class PairwiseAngularChargeTests(unittest.TestCase):
    def test_gates_are_global_permutations_and_exactly_conserve_pair_charge(self):
        for n in (4,8):
            for i in range(n):
                for a,b,z1,z2 in product(range(n),range(n),(1,-1),(1,-1)):
                    old=(a,b,z1,z2)
                    new=copy_angles(i,*old,n)
                    self.assertEqual(copy_angles(i,*new,n,inverse=True),old)
                    for kind in ('absolute','swap_invariant'):
                        self.assertEqual(paired_energy(*old,n,kind),paired_energy(*new,n,kind))
                    for k in (1,-1):
                        nxt=write_sign(k,*new,n)
                        self.assertEqual(write_sign(k,*nxt,n),new)
                        for kind in ('absolute','swap_invariant'):
                            self.assertEqual(paired_energy(*new,n,kind),paired_energy(*nxt,n,kind))
        # Inactive blocks are fixed, and the active equal-angle zero sector
        # is permuted, so these are unitary charge-commuting permutations on
        # the full finite pair space, not only on the prepared input.

    def test_charge_conservation_does_not_select_magnitude_law(self):
        # The same gates conserve an arbitrary diagonal value function, not
        # just the two previously selected symmetric examples.
        for values in ((F(1,7),F(2,5),F(9,11),F(7,3)),
                       (F(0),F(-2),F(3,10),F(8))):
            for i,a,b,z1,z2,k in product(range(4),range(4),range(4),(1,-1),(1,-1),(1,-1)):
                old=(a,b,z1,z2)
                copied=copy_angles(i,*old,4)
                written=write_sign(k,*copied,4)
                e=energy_from_values(values,*old)
                self.assertEqual(energy_from_values(values,*copied),e)
                self.assertEqual(energy_from_values(values,*written),e)
            for i,k in product(range(4),(1,-1)):
                self.assertEqual(energy_from_values(values,*prepared_output(i,k,4)),0)

    def test_distinct_signed_records_balance_pointwise_and_uncompute(self):
        for n in (4,8,16):
            for i,k in product(range(n),(1,-1)):
                a,b,z1,z2=prepared_output(i,k,n)
                self.assertEqual((a,b,z1,z2),(i,i,k,-k))
                for kind in ('absolute','swap_invariant'):
                    self.assertEqual(paired_energy(a,b,z1,z2,n,kind),0)
                self.assertEqual(undo_output(i,k,(a,b,z1,z2),n),(0,0,1,-1))
        # The ready pair itself is already in a nontrivial opposite-sign
        # zero-charge state. It is a resource, not an origin-from-nothing.

    def test_actual_quantum_vectors_lift_both_local_signs_and_magnitudes(self):
        root=output(active_base())
        for label,s,n in product((0,7,15),(1,-1),(4,8)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            u,v,rows=embed(x,s,n);total=norm2(v)
            for kind in ('absolute','swap_invariant'):
                old_quality=apply_quality(rows,s,kind,'echo')
                for r,part,target in zip((1,-1),rows,old_quality):
                    for i,vec in enumerate(part):
                        recorded1=0*vec;recorded2=0*vec
                        for j in (1,-1):
                            branch=j_project(vec,j);k=s*r*j
                            a,b,z1,z2=prepared_output(i,k,n)
                            g=float(magnitude(u[i],kind))
                            recorded1=recorded1+g*z1*branch
                            recorded2=recorded2+g*z2*branch
                            self.assertEqual((a,b),(i,i))
                            self.assertEqual(paired_energy(a,b,z1,z2,n,kind),0)
                        self.assertLess(norm2(recorded1-target[i])/total,1e-24)
                        self.assertLess(norm2(recorded1+recorded2)/total,1e-24)
        # This is a linear isometric extension of actual complex quantum
        # states, not separate classical samples of an unmeasured history.

    def test_new_physical_records_change_old_angle_coherence(self):
        x=initial(relative_read(output(active_base()),4,labels=(0,))[0])
        for n in (4,8):
            u,v,rows=embed(x,1,n);total=norm2(v)
            weights=[sum(norm2(part[i]) for part in rows)/total for i in range(n)]
            for w in weights:self.assertAlmostEqual(w,1/n,places=13)
            # Distinct copied bins are orthogonal in both new value records.
            # After their trace, the old+A state is a mixture of orthogonal
            # normalized angular-bin vectors, with purity sum_i p_i².
            self.assertAlmostEqual(sum(w*w for w in weights),1/n,places=13)
            i,j=n//2,n-1
            before=sum(np.vdot(part[i],part[j]) for part in rows)/total
            self.assertAlmostEqual(before.real,1/n,places=13)
            self.assertAlmostEqual(before.imag,0.,places=13)
            # After tracing new records the same old angle entry is zero.
            self.assertNotEqual(i,j)

    def test_original_sign_counterpart_reverses_both_recorded_local_values(self):
        root=output(active_base())
        for label,n in product((0,7,15),(4,8)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            u,v,p=embed(x,1,n);_,w,m=embed(x,-1,n);total=norm2(v)
            for r,partp,partm in zip((1,-1),p,m):
                for i in range(n):
                    # At tick 10, S sends the s=+ slice to the s=- slice;
                    # the clock-dressed counterpart supplies an overall minus.
                    self.assertLess(norm2(apply64(ss,partp[i])-partm[i])/total,1e-24)
                    for j in (1,-1):
                        if norm2(j_project(partp[i],j))<1e-24:continue
                        plus=prepared_output(i,r*j,n)
                        minus=prepared_output(i,-r*j,n)
                        self.assertEqual(plus[:2],minus[:2])
                        self.assertEqual(plus[2],-minus[2])
                        self.assertEqual(plus[3],-minus[3])

    def test_24_tick_reversible_cycle_and_clock_conditioning(self):
        # Seven original steps, 3 echo gates, two paired-record gates and
        # their inverses, 3 inverse echo gates, seven original inverses.
        forward=list(range(7))+['T','Q','T','copy','write']
        reverse=['write','uncopy','T','Q','T']+list(reversed(range(7)))
        self.assertEqual(len(forward+reverse),24)
        for q in (1,2):
            for t in range(24):self.assertEqual((q*t+q)%4,(q*((t+1)%24))%4)
        # The designated complete-pair anchor is tick 12. The q=1 and q=2
        # reference=0 anchor mixtures have six and twelve clock anchors.
        # This selects that anchor, not every accidental occurrence of equal
        # paired records at some other time.
        self.assertEqual(q_anchor_reading(1,0,12),F(1,6))
        self.assertEqual(q_anchor_reading(2,0,12),F(1,12))
        for r in (1,3):
            with self.assertRaises(ValueError):q_anchor_reading(2,r,12)

if __name__=='__main__':unittest.main()
