"""Exact Poincare normalization and echo-reference scope checks."""
from itertools import product
import unittest
import sympy as sp
import numpy as np

from verification.zero_poincare_energy_why import (
    generators,bracket,derived_span_rank,boost_01,minkowski_metric,
    finite_rotation_boost_obstruction,
)
from verification.zero_perfect_symmetry_root import total_generators
from verification.zero_covariant_sphere_subject_bridge_test import (
    geom,boosts,Q,invroot,coeff,spin_base,
)
from verification.zero_all_sector_noncommuting_sphere_test import (
    active_base,output,relative_read,i_r_m_table,
)


class PoincareEnergyWhyTests(unittest.TestCase):
    def test_poincare_commutators_and_perfect_derived_algebra(self):
        j,k,p=generators();zero=sp.zeros(5)
        for i in range(3):
            ii=(i+1)%3;kk=(i+2)%3
            self.assertEqual(bracket(j[i],j[ii]),j[kk])
            self.assertEqual(bracket(j[i],k[ii]),k[kk])
            self.assertEqual(bracket(k[i],k[ii]),-j[kk])
            self.assertEqual(bracket(k[i],p[0]),p[i+1])
            for n in range(3):
                self.assertEqual(bracket(k[i],p[n+1]),p[0] if i==n else zero)
        allgen=j+k+p
        self.assertEqual(sp.Matrix.hstack(*(a.reshape(25,1) for a in allgen)).rank(),10)
        self.assertEqual(derived_span_rank(allgen),10)
        # This faithful affine representation is NOT a unitary quantum model.

    def test_energy_and_momentum_scalar_shift_breaks_strict_boost_algebra(self):
        _,k,p=generators();I=sp.eye(5)
        c=sp.symbols('c_0:4',real=True);new=tuple(p[i]+c[i]*I for i in range(4))
        for i in range(3):
            self.assertEqual(bracket(k[i],new[i+1])-new[0],-c[0]*I)
            self.assertEqual(bracket(k[i],new[0])-new[i+1],-c[i+1]*I)
        self.assertEqual(sp.solve(list(c),c),{x:0 for x in c})
        # Ray-level phases or a projective/cocycle lift require separate work.

    def test_finite_unitary_lorentz_extension_of_nonzero_rotation_is_impossible(self):
        j=total_generators(2);j3=j[2];zero=sp.zeros(4)
        self.assertEqual(sp.trace(j3*j3),2)
        self.assertEqual(finite_rotation_boost_obstruction(j3,zero),2)
        # For Hermitian K2, Tr(K2²) >= 0, so the full-Lorentz trace identity
        # Tr(J3²)+Tr(K2²)=0 cannot hold. Analytic proof is in the report.

    def test_lorentz_invariant_stress_allows_nonzero_energy_density(self):
        rho=sp.symbols('rho',real=True);eta=minkowski_metric()
        Lambda=boost_01(sp.Rational(5,3),sp.Rational(4,3))
        stress=-rho*eta
        self.assertEqual(Lambda.T*eta*Lambda,eta)
        self.assertEqual(Lambda.T*stress*Lambda,stress)
        self.assertEqual(stress[0,0],rho)
        # This constant invariant tensor is not a demonstrated gravity solution.

    def test_invariant_symmetric_rank2_tensors_have_one_free_scalar(self):
        j,k,_=generators()
        names=sp.symbols('t0:10');t=sp.zeros(4);z=0
        for a in range(4):
            for b in range(a,4):t[a,b]=t[b,a]=names[z];z+=1
        equations=[]
        for g in j+k:
            a=g[:4,:4];equations.extend(list(a.T*t+t*a))
        mat,_=sp.linear_eq_to_matrix(equations,names)
        self.assertEqual(mat.rank(),9)
        self.assertEqual(len(mat.nullspace()),1)
        self.assertEqual((mat*sp.Matrix([minkowski_metric()[a,b]
            for a in range(4) for b in range(a,4)])),sp.zeros(mat.rows,1))
        # Thus symmetry itself leaves the coefficient rho unconstrained.

    def test_same_echo_reference_transports_without_a_physical_boost_claim(self):
        base=output(active_base());old=relative_read(base,4,labels=(0,7,15))
        prior=i_r_m_table(old)
        for a in boosts():
            n,k,b,u=geom(a);w=invroot(n)
            np.testing.assert_allclose(sum(q*x for q,x in zip(Q,k)),n,atol=1e-12)
            np.testing.assert_allclose(u.conj().T@u,np.eye(2),atol=1e-12)
            np.testing.assert_allclose(sum(q*w@x@w for q,x in zip(Q,k)),np.eye(2),atol=1e-12)
            rays=[coeff(w@x@w-np.eye(2)) for x in k]
            reference_relative=coeff(w@b@w)
            transported,_=spin_base(2,rays,reference_relative)
            after=relative_read(output(transported),4,labels=(0,7,15))
            np.testing.assert_allclose(i_r_m_table(after),prior,atol=1e-12)
        # The old echo was NOT acted on by a physical noncompact boost; the
        # reference-relative representation is a covariance comparison only.

if __name__=='__main__':unittest.main()
