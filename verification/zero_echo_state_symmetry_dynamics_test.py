"""State-level and dynamical type-swap diagnostics on the existing carrier."""
import unittest
import numpy as np
import sympy as sp
from scipy.linalg import expm
from verification.zero_echo_state_symmetry_dynamics import (
    free_q,swap,projector_plus,invariant_history_constraints,
    spectral_projector,odd_transition_amplitude,stationary_invariant_density,
)
from verification.zero_relational_laplacian import generator,type_symmetric_generator


class EchoStateSymmetryDynamicsTests(unittest.TestCase):
    def test_same_uniform_echo_is_stationary_for_both_generators(self):
        q=free_q();r=swap();ones=sp.ones(4,1)
        self.assertEqual(q*ones,sp.zeros(4,1))
        self.assertEqual(r*ones,ones)
        self.assertNotEqual(q*r,r*q)
        np.testing.assert_allclose(np.asarray(q,dtype=float),generator(4))
        np.testing.assert_allclose(type_symmetric_generator(4)@np.ones(4),0)

    def test_all_real_or_complex_swap_fixed_histories_reduce_to_uniform_vector(self):
        m=invariant_history_constraints()
        self.assertEqual(m.rank(),3)
        self.assertEqual(m.nullspace(),[sp.ones(4,1)])
        q=free_q();r=swap()
        # Necessity comes from k=0,1,2 derivatives of R exp(iQt)v.
        # Sufficiency follows because Q annihilates the uniform vector.
        for k in range(6):self.assertEqual((r-sp.eye(4))*q**k*sp.ones(4,1),sp.zeros(4,1))
        a,b,c=sp.symbols('a b c');v=sp.Matrix([a,a,b,c])
        first=(r-sp.eye(4))*q*v
        second=(r-sp.eye(4))*q*q*v
        self.assertEqual(sp.solve(list(first),[b]),{b:a})
        self.assertEqual(sp.solve(list(first)+list(second),[b,c]),{b:a,c:a})

    def test_exact_leakage_and_later_recurrence(self):
        t=sp.symbols('t',real=True);amp=odd_transition_amplitude(t)
        expected=(sp.exp(-2*sp.I*t)-sp.exp(-12*sp.I*t))/5
        self.assertEqual(sp.simplify(amp-expected),0)
        self.assertEqual(sp.simplify(sp.expand_complex(amp*sp.conjugate(amp))
                                     -sp.Rational(4,25)*sp.sin(5*t)**2),0)
        self.assertEqual(sp.simplify(abs(amp.subs(t,sp.pi/10))**2),sp.Rational(4,25))
        self.assertEqual(sp.simplify(amp.subs(t,sp.pi/5)),0)
        self.assertEqual(sp.limit(abs(amp)**2/t**2,t,0),4)
        q=np.asarray(free_q(),dtype=float);r=np.asarray(swap(),dtype=float)
        v=np.array([1,1,0,0],dtype=complex)/np.sqrt(2)
        odd=(np.eye(4)-r)/2
        for time in (0,.04,np.pi/10,np.pi/5):
            state=expm(1j*q*time)@v
            self.assertAlmostEqual(np.linalg.norm(odd@state)**2,
                                   4/25*np.sin(5*time)**2,places=12)
        qs=type_symmetric_generator(4)
        for time in (.04,np.pi/10,np.pi/5):
            self.assertLess(np.linalg.norm(odd@expm(1j*qs*time)@v),1e-13)

    def test_even_initial_data_can_hide_breaking_until_second_order(self):
        q=free_q();r=swap();v=sp.Matrix([1,1,1,0])/sp.sqrt(3)
        pminus=(sp.eye(4)-r)/2
        self.assertEqual(pminus*v,sp.zeros(4,1))
        self.assertEqual(pminus*q*v,sp.zeros(4,1))
        self.assertNotEqual(pminus*q*q*v,sp.zeros(4,1))
        # The odd probability starts at 6 t^4, not t^2.
        self.assertEqual(sp.simplify((pminus*q*q*v).dot(pminus*q*q*v)/4),6)

    def test_one_even_excitation_on_original_encoded_record_pair(self):
        # The prior echo test already establishes that the actual Q/pointer
        # swap agrees on these branches with the chosen dressed R extension.
        from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
        from verification.zero_relational_chirality_report_test import initial
        from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints
        from verification.zero_dressed_sphere_rotations import build_frames
        from verification.zero_dressed_history_pair import encode_pair
        from verification.zero_relational_laplacian import dressed_operator
        from verification.zero_relational_laplacian_test import scaled,encoded_diff
        from verification.zero_persistent_sphere_subject_selection_test import norm2
        shape,frames,_=build_frames()
        x=initial(relative_read(output(active_base()),4,labels=(0,))[0])
        _,total,states=quantum_echo_checkpoints(x,1,4);rows=states[3]
        raw=[encode_pair((rows[0][i],rows[1][i]),i,1) for i in range(4)]
        for sector in raw:
            self.assertAlmostEqual(sum(norm2(z) for pair in sector.values() for z in pair)/total,.25,places=12)
        coeff=np.array([np.sqrt(2),np.sqrt(2),0.,0.])
        bins=[scaled(raw[i],coeff[i]) for i in range(4)]
        out=dressed_operator(bins,10,1,frames,shape)
        hcoeff=-generator(4)@coeff
        self.assertLess(sum(encoded_diff(out[i],scaled(raw[i],hcoeff[i])) for i in range(4))/total,1e-21)
        odd=(hcoeff[0]-hcoeff[1])/2
        odd_sectors=[scaled(raw[0],odd),scaled(raw[1],-odd)]
        odd_norm=sum(norm2(z) for sector in odd_sectors for pair in sector.values() for z in pair)/total
        self.assertAlmostEqual(odd_norm,4.,places=11)
        self.assertTrue(all(k[2]+k[3]==0 for sector in out for k in sector))

    def test_stationary_physical_state_does_not_force_type_incidence_weights(self):
        rho=stationary_invariant_density(sp.Rational(1,2))
        a=sp.symbols('a',real=True);x=sp.Matrix([[0,1],[1,0]])
        sigma=sp.kronecker_product(sp.diag(a,1-a),rho)
        combined=sp.kronecker_product(x,swap())
        diff=sp.simplify(combined*sigma*combined.T-sigma)
        self.assertEqual(diff.subs(a,sp.Rational(1,2)),sp.zeros(8))
        self.assertNotEqual(diff.subs(a,sp.Rational(1,3)),sp.zeros(8))
        # Every identical block physical effect has the same marginal rho.
        self.assertEqual(sigma[:4,:4]+sigma[4:,4:],rho)

    def test_mixed_stationary_controls_are_not_necessarily_ground(self):
        q=free_q();r=swap();p=sp.symbols('p',real=True)
        rho=stationary_invariant_density(p)
        self.assertEqual(q*rho-rho*q,sp.zeros(4))
        self.assertEqual(r*rho-rho*r,sp.zeros(4))
        self.assertEqual(sp.trace(rho),1)
        self.assertEqual(rho.eigenvals(),{p:1,(1-p)/3:3})
        # Exhaustiveness: simple Q spectrum and R connects each of the
        # three excited eigenspaces, forcing their diagonal weights equal.
        eig=(0,-2,-6,-12)
        projectors={v:spectral_projector(q,v,eig) for v in eig}
        for i in range(1,4):
            for j in range(i+1,4):
                self.assertNotEqual(projectors[eig[i]]*r*projectors[eig[j]],sp.zeros(4))
        self.assertEqual(sp.trace(q*stationary_invariant_density(0)),-sp.Rational(20,3))

if __name__=='__main__':unittest.main()
