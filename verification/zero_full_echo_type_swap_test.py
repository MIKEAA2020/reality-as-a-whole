"""Lift the reduced physical type swap to the original coherent echo.

On the actual r=b support, a gauge-compatible controlled Q*Z_M gate swaps
J with J*R and stabilizes the prepared state. This is a physical-model
operator result, not an actual experiential-symmetry or subjecthood proof.
"""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_internal_contextual_reference_test import (
    B,eye,P,Gint,Bs,Zj,value_history,gauge_history,
)
from verification.zero_persistent_sphere_subject_selection_test import Q,norm2
from verification.zero_dynamic_subject_memory_echo_test import jwrite
from verification.zero_internal_reference_subject_valence_candidates_test import j_project
from verification.zero_conserving_sphere_handedness_report_test import bob_action
from verification.zero_sphere_angular_echo import magnitude_moments


class FullEchoTypeSwapTests(unittest.TestCase):
    def test_quantum_operator_lift_on_actual_support(self):
        # On valid P, Q J Q = B J and Q commutes with B, gauge and P.
        np.testing.assert_allclose(Q@Q,eye,atol=1e-13)
        for a in (P,Gint,Bs):np.testing.assert_allclose(Q@a,a@Q,atol=1e-13)
        np.testing.assert_allclose(P@(Q@Zj@Q-Bs@Zj)@P,0,atol=1e-13)
        # r=+ block: D=I. r=- block: D=Q Z_M, unitary/involutive.
        # B R=+ on the actual post-echo state, so b=r in either block.
        for r,b in product((1,-1),repeat=2):
            sector=P@(eye+b*Bs)/2
            jtransport=Zj if r==1 else Q@Zj@Q
            if b==r:
                np.testing.assert_allclose(sector@(jtransport-r*Zj)@sector,0,atol=1e-13)
            elif r==-1:
                self.assertGreater(np.linalg.norm(sector@(jtransport-r*Zj)@sector),1)
        # Z_M commutes with J and simply multiplies Q on its block, so the
        # same result holds for signed observables M J and M J R.

    def test_all_16_full_quantum_histories_preserved(self):
        root=output(active_base())
        for label in range(16):
            x=initial(relative_read(root,4,labels=(label,))[0]);mass=norm2(x)
            for s in (1,-1):
                # Coherent controlled sign write, then T-Q-T echo. M's
                # orthogonal s branch is represented as a state slice.
                v=(x+s*value_history(x))/2
                a,c=jwrite(v,0*v);a,c=value_history(a),value_history(c);a,c=jwrite(a,c)
                for r,w in ((1,a),(-1,c)):
                    if norm2(w)<1e-20:continue
                    np.testing.assert_allclose(bob_action(B,w),r*w,atol=1e-13)
                    # Q has eigenvalue s on each final B/R block. D multiplies
                    # by pointer Z_M=s, restoring the same complex vector.
                    np.testing.assert_allclose(value_history(w),s*w,atol=1e-13)
                    transformed=w if r==1 else s*value_history(w)
                    np.testing.assert_allclose(transformed,w,atol=1e-13)
                    np.testing.assert_allclose(gauge_history(transformed),transformed,atol=1e-13)
                    for z in (1,-1):
                        component=j_project(w,z)
                        if r==-1:
                            changed=s*value_history(component)
                            np.testing.assert_allclose(j_project(changed,-z),changed,atol=1e-13)
            self.assertGreater(mass,0)

    def test_recorded_angular_bands_change_symmetry_and_old_coherence(self):
        # Coherently attach one new qubit A recording J at tick 10. In the
        # b=r=- sector its two values are the old z bands in reverse order.
        # This retains all old diagonal statistics but dephases J if A is
        # traced out. The full state includes A; nothing is erased.
        root=output(active_base())
        for label in range(16):
            x=initial(relative_read(root,4,labels=(label,))[0])
            for s in (1,-1):
                v=(x+s*value_history(x))/2
                a,c=jwrite(v,0*v);a,c=value_history(a),value_history(c);a,c=jwrite(a,c)
                cp,cm=j_project(c,1),j_project(c,-1)
                self.assertAlmostEqual(norm2(cp),norm2(cm),places=13)
                self.assertGreater(norm2(cp),1e-12)
                np.testing.assert_allclose(s*value_history(cp),cm,atol=1e-13)
                np.testing.assert_allclose(s*value_history(cm),cp,atol=1e-13)
                total=norm2(a)+norm2(cp)+norm2(cm)
                # Old D leaves A fixed and flips J in R=-, making those two
                # A-tagged components orthogonal to themselves.
                overlap=(norm2(a)+np.vdot(cp,s*value_history(cp))+
                         np.vdot(cm,s*value_history(cm)))/total
                self.assertAlmostEqual(overlap.real,.5,places=13)
                self.assertAlmostEqual(overlap.imag,0,places=13)
                # Flip A in the R=- branch as well: the full state is fixed.
                np.testing.assert_allclose(s*value_history(cm),cp,atol=1e-13)
                np.testing.assert_allclose(s*value_history(cp),cm,atol=1e-13)
                # Trace A in the conditional R=- sector: two equal orthogonal
                # components produce purity 1/2, instead of the original 1.
                purity=(norm2(cp)**2+norm2(cm)**2)/(norm2(cp)+norm2(cm))**2
                self.assertAlmostEqual(purity,.5,places=13)
                # g1's old angular bin means are distinct 3/4 and 1/4;
                # the A-flip exchanges them. g2's means are both 1/6.
                means={kind:{key:moment/mass for key,(mass,moment) in magnitude_moments(kind).items()}
                       for kind in ('absolute','swap_invariant')}
                self.assertEqual((means['absolute'][-1,-1],means['absolute'][-1,1]),(F(3,4),F(1,4)))
                self.assertEqual((means['swap_invariant'][-1,-1],means['swap_invariant'][-1,1]),(F(1,6),F(1,6)))

    def test_pointer_correction_matters(self):
        root=output(active_base())
        x=initial(relative_read(root,4,labels=(0,))[0])
        v=(x-value_history(x))/2 # s=-1
        a,c=jwrite(v,0*v);a,c=value_history(a),value_history(c);a,c=jwrite(a,c)
        self.assertGreater(norm2(c),1e-10)
        np.testing.assert_allclose(value_history(c),-c,atol=1e-13)
        self.assertGreater(np.linalg.norm(value_history(c)-c),1e-5)
        np.testing.assert_allclose(-value_history(c),c,atol=1e-13)
        self.assertAlmostEqual(norm2(a),norm2(c),places=13)
        overlap=(norm2(a)+np.vdot(c,value_history(c)))/(norm2(a)+norm2(c))
        self.assertAlmostEqual(abs(overlap),0,places=13)
        # Without Z_M the conditional-R operation changes the relative
        # r-branch phase; it is not merely a global phase in this sector.

if __name__=='__main__':unittest.main()
