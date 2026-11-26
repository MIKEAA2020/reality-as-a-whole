"""Exact mode identities and Lüders controls on the original echo."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np
import sympy as sp

from verification.zero_echo_constitutive_modes import (
    modes,mode_law,fixed_pointer_law,coarse_law,lueders_fidelity,reported_pair_balance)
from verification.zero_joint_quality_incidence_root import R,J,quality,swap,counterpart
from verification.zero_echo_quality_bridge_discrimination import structural_value
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_internal_reference_subject_valence_candidates_test import j_project
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints


class ConstitutiveEchoModeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_mode_operators_reconstruct_original_signs_exactly(self):
        # Complete abstract joint spectrum; these are operator identities on
        # any space with two commuting self-adjoint sign involutions.
        N=sp.diag(1,1,-1,-1);K=sp.diag(1,-1,1,-1);I=sp.eye(4)
        S=(N+K)/2;T=(N-K)/2;Rop=N*K
        self.assertEqual(N*K,K*N)
        self.assertEqual(S+T,N);self.assertEqual(S-T,K)
        self.assertEqual(S*S,(I+Rop)/2)
        self.assertEqual(T*T,(I-Rop)/2)
        self.assertEqual(S*T,sp.zeros(4))
        self.assertEqual(S*S+T*T,I)
        self.assertEqual(S*S*S,S);self.assertEqual(T*T*T,T)
        swapop=sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
        self.assertEqual(swapop*S*swapop.T,S)
        self.assertEqual(swapop*T*swapop.T,-T)
        self.assertEqual(S*T,T*S)  # distinct modes are not incompatible effects

    def test_uniqueness_of_swap_even_odd_scalar_without_linearity(self):
        pairs=tuple(product((1,-1),repeat=2))
        matches=0
        for values in product((-2,-1,0,1,2),repeat=4):
            v=dict(zip(pairs,values))
            if v[1,1]!=1:continue
            if all(v[k,n]==v[n,k] and v[-n,-k]==-v[n,k] for n,k in pairs):
                matches+=1
                self.assertEqual(v,{(n,k):F(n+k,2) for n,k in pairs})
        self.assertEqual(matches,1)
        # This is an exhaustive finite-grid check of the separate algebraic
        # proof; it is not a derivation that actual valence meets the premises.

    def test_joint_table_is_one_physical_population_not_independent_modes(self):
        self.assertEqual(mode_law(),{(1,0):F(1,4),(-1,0):F(1,4),
                                     (0,1):F(1,4),(0,-1):F(1,4)})
        for i,s in product(range(4),(1,-1)):
            S,T=modes(i,s);n,k=quality(i,s)
            self.assertEqual((S+T,S-T),(n,k))
            self.assertEqual(S*S,F(1+R[i],2))
            self.assertEqual(T*T,F(1-R[i],2))
            self.assertEqual(modes(*swap(i,s)),(S,-T))
            self.assertEqual(modes(*counterpart(i,s)),(-S,-T))
            if R[i]==-1:
                self.assertEqual(S,0);self.assertNotEqual(T,0)
                self.assertEqual(structural_value(i,s,'symmetric'),0)
                self.assertNotEqual(structural_value(i,s,'pointer'),0)
                self.assertEqual(reported_pair_balance(i,s,F(3,4)),(0,T/2))
                self.assertEqual(reported_pair_balance(i,s,F(1,2)),(0,0))
        law=mode_law()
        self.assertEqual(law.get((1,1),0),0)
        self.assertEqual(sum(v for (S,T),v in law.items() if S==1)*
                         sum(v for (S,T),v in law.items() if T==1),F(1,16))
        # Scalar S's zero on R=- hides nonzero structural T and cannot
        # establish either no experience or balance under uneven incidences.

    def test_lueders_refinement_fidelity_formulas(self):
        for sign in (-1,1):
            joint=fixed_pointer_law(sign);coarse=coarse_law(joint)
            self.assertEqual(joint,{(0,sign):F(1,4),(0,-sign):F(1,4),(sign,0):F(1,2)})
            self.assertEqual(lueders_fidelity(coarse.values()),F(1,2))
            self.assertEqual(lueders_fidelity(joint.values()),F(3,8))
        with self.assertRaises(ValueError):lueders_fidelity((F(1,3),F(1,3)))
        with self.assertRaises(ValueError):fixed_pointer_law(0)

    def test_actual_complex_echo_components_and_lueders_probabilities(self):
        for label,sign in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,sign,4)
            rows=states[-1]
            for i in range(4):
                ri=0 if R[i]==1 else 1
                self.assertAlmostEqual(sum(norm2(rows[r][i]) for r in range(2))/total,.25,places=12)
                self.assertLess(norm2(rows[1-ri][i])/total,1e-23)
                part=rows[ri][i]
                self.assertLess(norm2(j_project(part,J[i])-part)/total,1e-23)
                S,T=modes(i,sign)
                self.assertEqual((S+T,S-T),quality(i,sign))
            # Bin support and J/R checks identify the genuine PVM cells on
            # the selected source family, not a universal bin decoder.
            probabilities={}
            for i in range(4):
                key=modes(i,sign)
                probabilities[key]=probabilities.get(key,0.)+sum(norm2(rows[r][i]) for r in range(2))/total
            self.assertAlmostEqual(sum(p*p for p in probabilities.values()),3/8,places=12)
            coarse={}
            for (S,T),p in probabilities.items():coarse[S]=coarse.get(S,0.)+p
            self.assertAlmostEqual(sum(p*p for p in coarse.values()),1/2,places=12)
            # The two T=± branches are orthogonal angular-bin subspaces;
            # both carry exactly half of the selected S=0 norm.
            self.assertAlmostEqual((sum(norm2(rows[r][0]) for r in range(2))/total)/coarse[0],.5,places=12)
            self.assertAlmostEqual((sum(norm2(rows[r][1]) for r in range(2))/total)/coarse[0],.5,places=12)

    def test_same_mode_distribution_can_hide_coherence_and_extra_disturbance(self):
        # Isometric representation of the two actual orthogonal S=0 branches,
        # with their relative phase absorbed into the first preparation.
        plus=np.array([1.,1.])/np.sqrt(2)
        minus=np.array([1.,-1.])/np.sqrt(2)
        rp=np.outer(plus,plus);rm=np.outer(minus,minus)
        self.assertTrue(np.allclose(np.diag(rp),np.diag(rm)))
        self.assertAlmostEqual(float(plus@rm@plus),0.)
        self.assertAlmostEqual(float(plus@rp@plus),1.)
        # Ideal S=0 Lüders outcome is identity on this subspace; a refined
        # T measurement (even if T is discarded) removes its off-diagonal.
        coarse=rp.copy();refined=np.diag(np.diag(rp))
        self.assertAlmostEqual(float(plus@coarse@plus),1.)
        self.assertAlmostEqual(float(plus@refined@plus),.5)
        self.assertTrue(np.allclose(refined,np.diag(np.diag(rm))))
        # Phase flip and projective interference effect are stipulated extra
        # operations, not shown local or accessible to an actual experiencer.

if __name__=='__main__':unittest.main()
