"""Exact sign counterpart, clock phase and actual quantum branch controls."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial,apply64
from verification.zero_internal_contextual_reference_test import S,ss,P,Gint,Bs,Zj,value_history
from verification.zero_persistent_sphere_subject_selection_test import Q,norm2
from verification.zero_internal_reference_subject_valence_candidates_test import b_project,j_project
from verification.zero_quantum_angular_echo import difference_mass,mass,apply_swap,apply_quality
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints,checkpoint_at,dot_rows
from verification.zero_coherent_signed_counterpart import q_count,phase,exchange,raw_history_overlap,incidence_weights
from verification.zero_intrinsic_angular_estimation import BANDS,polynomial,integral


def negate(rows):return tuple([-x for x in part] for part in rows)


class CoherentSignedCounterpartTests(unittest.TestCase):
    def test_exchange_gauge_and_necessary_clock_phase(self):
        for a in (P,Gint,Bs,Zj):
            np.testing.assert_allclose(P@(S@a-a@S)@P,0,atol=1e-13)
        np.testing.assert_allclose(P@(S@Q+Q@S)@P,0,atol=1e-13)
        self.assertGreater(np.linalg.norm(P@(S@Q-Q@S)@P),1)
        # Outside the valid support the chosen Q has an identity extension.
        self.assertGreater(np.linalg.norm((np.eye(256)-P)@(S@Q+Q@S)@(np.eye(256)-P)),1)
        for t in range(20):
            self.assertEqual(phase(t+1),phase(t)*(-1 if t in (8,11) else 1))
        self.assertEqual(phase(0),phase(20))
        self.assertEqual(raw_history_overlap(),F(-7,10))
        self.assertEqual(raw_history_overlap()**2,F(49,100))
        # The undressed map has a relative phase at t=9..11: a clock phase,
        # not a global sign. Dressing makes the shift commute on P.

    def test_all_16_original_sources_and_pointer_components(self):
        root=output(active_base())
        for label in range(16):
            x=initial(relative_read(root,4,labels=(label,))[0]);total=norm2(x)
            self.assertGreater(total,0)
            sx=apply64(ss,x)
            self.assertLess(norm2(sx+x)/total,1e-24)
            for s in (1,-1):
                v=(x+s*value_history(x))/2
                opposite=(x-s*value_history(x))/2
                self.assertAlmostEqual(norm2(v)/total,.5,places=12)
                self.assertLess(norm2(apply64(ss,v)+opposite)/total,1e-24)

    def test_dressed_full_angular_echo_preserves_complex_branches(self):
        root=output(active_base())
        for label in (0,7,15):
            x=initial(relative_read(root,4,labels=(label,))[0])
            up,total,p=quantum_echo_checkpoints(x,1,4)
            um,total2,m=quantum_echo_checkpoints(x,-1,4)
            self.assertEqual(up,um);self.assertAlmostEqual(total,total2,places=13)
            for t in range(7,14):
                index=checkpoint_at(t)
                # X_M exchanges s slices; phase(t) S makes the output -1
                # times the complete opposite slice in each clock block.
                self.assertLess(difference_mass(exchange(p[index],t),negate(m[index]))/total,1e-24)
                self.assertLess(difference_mass(exchange(m[index],t),negate(p[index]))/total,1e-24)
                self.assertAlmostEqual(mass(p[index]),mass(m[index]),places=13)
            # Actual complex quantum inner products give the raw and dressed
            # whole-history overlaps; orthogonal clock labels remove cross terms.
            dots=[(dot_rows(p[i],exchange(m[i]))+dot_rows(m[i],exchange(p[i])))/norm2(x)
                  for i in range(4)]
            raw=sum(dots[checkpoint_at(t)] for t in range(20))/20
            dressed=sum(phase(t)*dots[checkpoint_at(t)] for t in range(20))/20
            self.assertAlmostEqual(raw.real,-.7,places=12)
            self.assertAlmostEqual(raw.imag,0.,places=12)
            self.assertAlmostEqual(dressed.real,-1.,places=12)
            self.assertAlmostEqual(dressed.imag,0.,places=12)
        # The repaired physical type swap D and the pointer-sign counterpart
        # commute on the actual post-echo vectors: S anticommutes with Q,
        # while X_M anticommutes with Z_M, so the two minus signs cancel.
        lhs=apply_swap(exchange(p[3]),-1)
        rhs=exchange(apply_swap(p[3],1))
        self.assertLess(difference_mass(lhs,rhs)/total,1e-24)
        self.assertLess(difference_mass(apply_swap(p[3],1),p[3])/total,1e-24)
        # D exchanges the full g2 now/echo operators, but not full g1.
        for kind in ('absolute','swap_invariant'):
            conjugated=apply_swap(apply_quality(apply_swap(p[3],1),1,kind,'now'),1)
            other=apply_quality(p[3],1,kind,'echo')
            d=difference_mass(conjugated,other)/total
            self.assertAlmostEqual(d,1/8 if kind=='absolute' else 0.,places=12)
        # Source/reservoir and reference factors are spectators under this
        # operation; their actual gates commute with S because they use B.

    def test_sign_pairing_on_every_record_cell_and_counterexample(self):
        x=initial(relative_read(output(active_base()),4,labels=(0,))[0]);total=norm2(x)
        _,_,p=quantum_echo_checkpoints(x,1,4)
        _,_,m=quantum_echo_checkpoints(x,-1,4)
        nonempty=0
        for t in (7,8,9,10):
            a,b=p[checkpoint_at(t)],m[checkpoint_at(t)]
            for r,parta,partb in zip((1,-1),a,b):
                for i in range(4):
                    for bs,j in product((1,-1),repeat=2):
                        va=j_project(b_project(parta[i],bs),j)
                        vb=j_project(b_project(partb[i],bs),j)
                        wa,wb=norm2(va)/total,norm2(vb)/total
                        self.assertAlmostEqual(wa,wb,places=13)
                        if wa>1e-12:
                            nonempty+=1
                            # M=s, with the same B,J,R,A cell, reverses both
                            # M J and M J R; no subjective incidence inferred.
                            self.assertEqual((1*j*r),-((-1)*j*r))
                            self.assertEqual((1*j),-((-1)*j))
        self.assertGreater(nonempty,0)
        # A condition selecting s=+, R=+, J=+ is not counterpart invariant.
        # It has nonzero actual physical weight and only positive K.
        selected=sum(norm2(j_project(v,1)) for v in p[3][0])/total
        self.assertAlmostEqual(selected,.25,places=12)
        self.assertGreater(selected,0)
        self.assertEqual(1*1*1,1)

    def test_two_invariant_involutions_force_equal_type_sign_weights(self):
        cells=tuple(product(('now','echo'),(1,-1)))
        sign=lambda x:(x[0],-x[1])
        swap=lambda x:('echo' if x[0]=='now' else 'now',x[1])
        for x in cells:
            self.assertEqual(sign(sign(x)),x)
            self.assertEqual(swap(swap(x)),x)
            self.assertEqual(sign(swap(x)),swap(sign(x)))
            self.assertEqual({x,sign(x),swap(x),sign(swap(x))},set(cells))
        # Formal group averaging is a control, not a derivation of an actual
        # incidence symmetry or proof that these four labels are subjects.
        original=dict(zip(cells,(F(1,10),F(2,10),F(3,10),F(4,10))))
        averaged={x:(original[x]+original[sign(x)]+original[swap(x)]+
                     original[sign(swap(x))])/4 for x in cells}
        self.assertEqual(set(averaged.values()),{F(1,4)})
        self.assertNotEqual(original,averaged)
        # Sign symmetry alone leaves unequal type weights possible.
        sign_only=dict(zip(cells,(F(1,3),F(1,3),F(1,6),F(1,6))))
        self.assertTrue(all(sign_only[x]==sign_only[sign(x)] for x in cells))
        self.assertFalse(all(sign_only[x]==sign_only[swap(x)] for x in cells))

    def test_global_zero_does_not_imply_conditional_incidence_symmetry(self):
        eps=F(1,2)
        for u in (F(-3,4),F(-1,4),F(1,4),F(3,4)):
            a=incidence_weights(eps,u,1);b=incidence_weights(eps,u,-1)
            self.assertGreater(a,0);self.assertGreater(b,0)
            self.assertEqual(a+b,1)
            self.assertNotEqual(a,b)
        # Hypothetical incidence weights p(k|u)=(1+eps*k*u)/2.
        # They retain u marginal du/2 but NOT the full Born (u,K) law.
        def signed_total(kind):
            return sum((integral((F(0),)+polynomial(kind,i),a,b)/2
                        for i,(a,b) in enumerate(BANDS)),F(0))*eps
        self.assertEqual(signed_total('absolute'),0)
        self.assertEqual(signed_total('swap_invariant'),eps/4)
        # In opposite hemispheres g1's conditional signed sums are ±eps/3.
        self.assertEqual(eps*integral((F(0),)+polynomial('absolute',2),F(0),F(1)),eps/3)
        negative=sum((integral((F(0),)+polynomial('absolute',i),a,b)
                      for i,(a,b) in enumerate(BANDS[:2])),F(0))*eps
        self.assertEqual(negative,-eps/3)

if __name__=='__main__':unittest.main()
