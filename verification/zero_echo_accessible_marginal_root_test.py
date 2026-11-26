"""Saved-echo-access subalgebra and pure/mixed marginal controls."""
import unittest
from fractions import Fraction as F
from itertools import product
import numpy as np
import sympy as sp

from verification.zero_echo_accessible_marginal_root import (
    saved_memory_density,local_blocks,product_local_blocks,recorded_pure,
    global_correlated_blocks,partial_trace_environment,cq_tagged,coherent_witness,
)


class EchoAccessibleMarginalRootTests(unittest.TestCase):
    def test_full_local_effect_algebra_allows_type_correlations(self):
        rho=saved_memory_density();n,e=local_blocks();n0,e0=product_local_blocks()
        self.assertEqual(n+e,rho)
        self.assertEqual(n0+e0,rho)
        self.assertEqual(sp.trace(n),sp.Rational(1,2))
        self.assertEqual(sp.trace(e),sp.Rational(1,2))
        self.assertEqual(n[0,0]/rho[0,0],sp.Rational(7,12))
        self.assertEqual(n[1,1]/rho[1,1],sp.Rational(1,4))
        x,y,u,v=sp.symbols('x y u v',real=True)
        effect=sp.Matrix([[x,u+sp.I*v],[u-sp.I*v,y]])
        self.assertEqual(sp.trace(effect*(n+e)),sp.trace(effect*(n0+e0)))
        for m in (n,e,n0,e0):
            self.assertTrue(all(val>=0 for val in m.eigenvals()))

    def test_general_positive_qubit_block_criterion_and_offdiagonal_control(self):
        rho=saved_memory_density();c=sp.Rational(1,8)
        n=rho/2+sp.Matrix([[0,c],[c,0]])
        e=rho-n
        self.assertEqual(n+e,rho)
        for m in (n,e):
            self.assertGreater(m.det(),0)
            self.assertGreater(m[0,0],0)
        x=sp.Matrix([[0,1],[1,0]])
        self.assertEqual(sp.trace(x*rho),0)
        self.assertEqual(sp.trace(x*n),sp.Rational(1,4))
        self.assertEqual(sp.trace(x*e),-sp.Rational(1,4))
        # A=[[a,c],[c*,b]] and rho-A>=0 iff diagonals nonnegative
        # and |c|²<=ab and |c|²<=(3/4-a)(1/4-b).

    def test_global_purity_coherence_and_distinguishability(self):
        pure=recorded_pure();n,e=global_correlated_blocks();deph=n+e
        self.assertEqual(partial_trace_environment(pure),saved_memory_density())
        self.assertEqual(partial_trace_environment(deph),saved_memory_density())
        self.assertNotEqual(pure,deph)
        c=coherent_witness()
        self.assertEqual(sp.trace(c*pure),sp.sqrt(3)/2)
        self.assertEqual(sp.trace(c*deph),0)
        self.assertEqual(sp.trace(pure*deph),sp.Rational(5,8))
        eig=(pure-deph).eigenvals()
        self.assertEqual(eig,{sp.sqrt(3)/4:1,-sp.sqrt(3)/4:1,sp.Integer(0):2})
        trace_distance=sum(abs(k)*v for k,v in eig.items())/2
        self.assertEqual(trace_distance,sp.sqrt(3)/4)
        self.assertEqual((1+trace_distance)/2,(4+sp.sqrt(3))/8)
        # Optimal distinguishing assumes arbitrary access to both factors.

    def test_extra_type_tag_creates_a_distinguishing_joint_report(self):
        correlated=cq_tagged(local_blocks());independent=cq_tagged(product_local_blocks())
        self.assertEqual(correlated[:2,:2]+correlated[2:,2:],saved_memory_density())
        self.assertEqual(independent[:2,:2]+independent[2:,2:],saved_memory_density())
        self.assertEqual(sp.trace(correlated),1)
        tv=sum(abs(correlated[i,i]-independent[i,i]) for i in range(4))/2
        self.assertEqual(tv,sp.Rational(1,8))
        self.assertEqual((1+tv)/2,sp.Rational(9,16))
        # Copying this hypothetical type into an actual report bit requires
        # a new physical interaction/bridge, not implied by its label.

    def test_record_only_access_does_not_read_the_candidate_quality_sign(self):
        from verification.zero_echo_subject_persistence import best_guess
        self.assertEqual(best_guess(('z',),'now'),F(1,2))
        self.assertEqual(best_guess(('z',),'echo'),F(1,2))
        self.assertEqual(best_guess(('s','z'),'echo'),1)
        self.assertEqual(best_guess(('s','j','r'),'now'),1)
        # These are the specified commuting physical sign queries, not a
        # universal quantum-access theorem or a first-person accuracy claim.

    def test_actual_complex_echo_record_supplies_the_schmidt_weights(self):
        from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
        from verification.zero_relational_chirality_report_test import initial
        from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints,dot_rows
        from verification.zero_echo_subject_persistence import copy_initial_j,evolve_record,record_fidelity
        from verification.zero_quantum_angular_echo import mass
        root=output(active_base())
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            record=evolve_record(copy_initial_j(states[0]),('T','Q','T'))
            self.assertAlmostEqual(mass(record[1])/total,.75,places=12)
            self.assertAlmostEqual(mass(record[-1])/total,.25,places=12)
            self.assertLess(abs(dot_rows(record[1],record[-1]))/total,1e-12)
            self.assertAlmostEqual(record_fidelity(record,states[3]),.625,places=12)
            # Each normalized orthogonal record vector is the old-side
            # Schmidt vector for the same separately added saved-J memory.

if __name__=='__main__':unittest.main()
