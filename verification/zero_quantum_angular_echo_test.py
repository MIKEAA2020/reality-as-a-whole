"""Physical quantum/angular bridge: coherent states, symmetry, moments."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_internal_contextual_reference_test import B,value_history
from verification.zero_internal_reference_subject_valence_candidates_test import j_project
from verification.zero_conserving_sphere_handedness_report_test import bob_action,j_sign
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_dynamic_subject_memory_echo_test import jwrite
from verification.zero_sphere_angular_echo import magnitude
from verification.zero_quantum_angular_echo import (
    latitudes,reflect_index,embed,embed_before_echo,pulse,apply_swap,apply_quality,mass,difference_mass,
)


class QuantumAngularEchoTests(unittest.TestCase):
    def test_reflection_and_midpoint_sphere_measure(self):
        for n in (4,8,16,40):
            u=latitudes(n)
            for i in range(n):
                h=reflect_index(i,n)
                self.assertEqual(reflect_index(h,n),i)
                self.assertEqual(u[h],-1-u[i] if u[i]<0 else u[i])
            self.assertEqual(sum(abs(x) for x in u)/n,F(1,2))
            self.assertEqual(sum(magnitude(x,'swap_invariant') for x in u)/n,F(1,2))
            # Exact discrete L2 error for the full-quality swap of |u|.
            err=sum((magnitude(x,'absolute')-magnitude(u[reflect_index(i,n)],'absolute'))**2
                    for i,x in enumerate(u))/n
            self.assertEqual(err,F(1,6)-F(2,3*n*n))
        for n in (0,2,6):
            with self.assertRaises(ValueError):latitudes(n)

    def test_all_16_quantum_sources_match_record_distribution_and_swap(self):
        root=output(active_base())
        for label,s,n in product(range(16),(1,-1),(4,8)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            u,v,rows=embed(x,s,n);total=norm2(v)
            self.assertGreater(total,0)
            self.assertAlmostEqual(mass(rows),total,places=13)
            for i in range(n):
                weight=sum(norm2(part[i]) for part in rows)/total
                self.assertAlmostEqual(weight,1/n,places=13)
                r=1 if u[i]>0 else -1
                branch=rows[0 if r==1 else 1][i]
                np.testing.assert_allclose(bob_action(B,branch),r*branch,atol=1e-13)
                if r==-1:
                    j=1 if u[i]<F(-1,2) else -1
                    np.testing.assert_allclose(j_sign(branch),j*branch,atol=1e-13)
            swapped=apply_swap(rows,s)
            self.assertLess(difference_mass(rows,swapped)/total,1e-24)
            restored=apply_swap(swapped,s)
            self.assertLess(difference_mass(rows,restored)/total,1e-24)

    def test_refinements_share_one_piecewise_constant_l2_wavefunction(self):
        # Map each discrete bin |i> to sqrt(n/2)*1_[u_i-,u_i+) in L²(du).
        # At any nested midpoint, n=4 and n=16 give exactly the same old/R
        # vector-valued wavefunction, not merely equal event probabilities.
        root=output(active_base())
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            _,_,coarse=embed(x,s,4);_,_,fine=embed(x,s,16)
            for i in range(16):
                for r in (0,1):
                    np.testing.assert_allclose((4/2)**.5*coarse[r][i//4],
                                               (16/2)**.5*fine[r][i],atol=1e-13)
        # Boundaries have measure zero and do not affect the common vector.

    def test_coherent_angular_record_passes_through_full_echo_and_return(self):
        root=output(active_base())
        for label,s in product(range(16),(1,-1)):
            x=initial(relative_read(root,4,labels=(label,))[0]);n=4
            _,v,original=embed_before_echo(x,s,n)
            rows=original
            for op in ('T','Q','T'):rows=pulse(rows,op)
            _,_,after=embed(x,s,n)
            self.assertLess(difference_mass(rows,after)/norm2(v),1e-24)
            for op in ('T','Q','T'):rows=pulse(rows,op)
            self.assertLess(difference_mass(rows,original)/norm2(v),1e-24)
        # Actual coherent vectors, not assumed hidden unmeasured j paths.
        # The reservoir gates are not densely simulated in this test.

    def test_actual_full_quality_operator_failure_and_repair(self):
        # Directly act on original old quantum vectors, not merely compare
        # two scalar functions or infer results from coincident bin means.
        root=output(active_base())
        for label,s,n in product((0,5,15),(1,-1),(4,8,16)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            u,v,rows=embed(x,s,n);total=norm2(v)
            for kind in ('absolute','swap_invariant'):
                conjugated=apply_swap(apply_quality(apply_swap(rows,s),s,kind,'now'),s)
                other=apply_quality(rows,s,kind,'echo')
                discrepancy=difference_mass(conjugated,other)/total
                expected=float(F(1,6)-F(2,3*n*n)) if kind=='absolute' else 0.0
                self.assertAlmostEqual(discrepancy,expected,places=12)
        # This equality concerns physical operators on a prepared model, not
        # experiential reality, actual incidence or necessarily possible worlds.

    def test_old_pure_sector_loses_coherence_when_angular_record_traced(self):
        root=output(active_base())
        for label,s in product((0,4,15),(1,-1)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            v=(x+s*value_history(x))/2
            a,c=jwrite(v,0*v);a,c=value_history(a),value_history(c);a,c=jwrite(a,c)
            cp,cm=j_project(c,1),j_project(c,-1)
            self.assertAlmostEqual(norm2(cp),norm2(cm),places=13)
            self.assertGreater(norm2(cp),0)
            np.testing.assert_allclose(s*value_history(cp),cm,atol=1e-13)
            # Orthogonal latent bands yield the mixture of c+ and c-.
            p=(norm2(cp)**2+norm2(cm)**2)/(norm2(cp)+norm2(cm))**2
            self.assertAlmostEqual(p,.5,places=13)
            self.assertGreater(np.linalg.norm(cp)*np.linalg.norm(cm),0)

if __name__=='__main__':unittest.main()
