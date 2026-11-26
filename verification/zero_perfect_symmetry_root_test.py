"""Exact perfect-algebra normalization, ray constraints and old echo."""
from itertools import product
import unittest
import numpy as np
import sympy as sp

from verification.zero_perfect_symmetry_root import (
    SIGMA,total_generators,commutator,shifted_defects,local_generators_of_dot,state_projector,
)
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_quantum_angular_echo import embed
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_spherical_invariant_echo import angle,rodrigues,spherical_bin_amplitude
from verification.zero_spherical_invariant_echo_test import pair


class PerfectSymmetryRootTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_exact_su2_algebra_eliminates_constant_shifts(self):
        a,b,c=sp.symbols('a b c',real=True)
        for n in (1,2,4):
            j=total_generators(n);I=sp.eye(2**n)
            for i in range(3):
                self.assertEqual(commutator(j[i],j[(i+1)%3]),sp.I*j[(i+2)%3])
            defects=shifted_defects(j,(a,b,c))
            self.assertEqual(defects,(-sp.I*c*I,-sp.I*a*I,-sp.I*b*I))
            self.assertEqual(sp.solve([x for matrix in defects for x in matrix],(a,b,c)),
                             {a:0,b:0,c:0})
        # This fixes the generators only after an honest Lie-algebra lift is
        # specified; projectively equivalent lifts need not have this form.

    def test_invariant_ray_under_full_group_versus_one_axis(self):
        j=total_generators(2);v=sp.Matrix([0,1,-1,0]);p=state_projector(v)
        for op in j:
            self.assertEqual(op*v,sp.zeros(4,1))
            self.assertEqual(commutator(op,p),sp.zeros(4))
        # A single U(1) action admits nonzero phase character on a ray.
        z=SIGMA[2]/2;up=sp.Matrix([1,0]);q=state_projector(up)
        self.assertEqual(z*up,up/2)
        self.assertEqual(commutator(z,q),sp.zeros(2))
        self.assertNotEqual(commutator(SIGMA[0]/2,q),sp.zeros(2))

    def test_invariant_mixed_state_is_not_a_singlet_state(self):
        rho=sp.eye(2)/2
        j=total_generators(1)
        for op in j:self.assertEqual(commutator(op,rho),sp.zeros(2))
        casimir=sum((op*op for op in j),sp.zeros(2))
        self.assertEqual(casimir,sp.Rational(3,4)*sp.eye(2))
        self.assertEqual(sp.trace(rho*casimir),sp.Rational(3,4))
        # Invariant density plus zero first moments does not imply J_i ρ=0.

    def test_full_zero_sector_not_unique_on_four_factors(self):
        j=total_generators(4);P=sum((op*op for op in j),sp.zeros(16))
        self.assertEqual(16-P.rank(),2)
        v12=sp.Matrix([0]*16);v13=sp.Matrix([0]*16)
        for i,a in ((5,1),(6,-1),(9,-1),(10,1)):v12[i]=a
        for i,a in ((3,1),(6,-1),(9,-1),(12,1)):v13[i]=a
        for op in j:
            self.assertEqual(op*v12,sp.zeros(16,1));self.assertEqual(op*v13,sp.zeros(16,1))
        self.assertEqual(sp.Matrix.hstack(v12,v13).rank(),2)

    def test_scalar_hamiltonian_shift_leaves_time_ray_dynamics(self):
        z=SIGMA[2]/2;up=sp.Matrix([1,0]);down=sp.Matrix([0,1])
        v=up+down;rho=state_projector(v);t,c=sp.symbols('t c',real=True)
        U=sp.diag(sp.exp(-sp.I*t/2),sp.exp(sp.I*t/2))
        shifted=sp.exp(-sp.I*c*t)*U
        self.assertEqual(sp.simplify(U*rho*U.conjugate().T-shifted*rho*shifted.conjugate().T),sp.zeros(2))
        self.assertEqual(commutator(z,sp.eye(2)),sp.zeros(2))
        # Same projective time evolution does not determine an energy zero.

    def test_local_angular_differences_cancel_for_smooth_relational_state(self):
        m,n,u,lm,ln=local_generators_of_dot()
        self.assertEqual(sp.simplify(lm+ln),sp.zeros(3,1))
        self.assertNotEqual(lm,sp.zeros(3,1))
        self.assertEqual(lm,-sp.I*m.cross(n))
        x=sp.symbols('x',real=True)
        # For ψ proportional to u under product normalized sphere area,
        # ||ψ||²=1/3 and ||L_m ψ||²=∫(1-u²)du/2=2/3.
        norm=sp.integrate(x*x/2,(x,-1,1))
        local=sp.integrate((1-x*x)/2,(x,-1,1))
        self.assertEqual(norm,sp.Rational(1,3))
        self.assertEqual(local/norm,2)
        # Smooth function is an invariant-sector illustration, not the
        # discontinuous old register state or evidence of phenomenality.

    def test_actual_echo_full_record_is_common_rotation_invariant_at_anchor(self):
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(self.root,4,labels=(label,))[0])
            _,old,rows=embed(x,s,4);total=norm2(old)
            for u in (-.83,-.32,.18,.72):
                m,n=pair((1,2,3),u,.41)
                rot=rodrigues((2,-1,3),1.1)
                i,a=spherical_bin_amplitude(angle(m,n),4)
                j,b=spherical_bin_amplitude(angle(rot@m,rot@n),4)
                self.assertEqual((i,a),(j,b))
                for part in rows:
                    self.assertLess(norm2(a*part[i]-b*part[j])/total,1e-24)
        # No claim that this finite geometric symmetry is cosmic energy,
        # a subject, or an actually accessible physical intervention.

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):total_generators(0)
        with self.assertRaises(ValueError):shifted_defects(total_generators(1),(1,2))

if __name__=='__main__':unittest.main()
