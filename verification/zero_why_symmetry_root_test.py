"""Exact symmetry classification and the actual complex echo carrier."""
from fractions import Fraction as F
from itertools import product
import unittest

from verification.zero_why_symmetry_root import (
    CELLS,BASIC,INDEPENDENT,counterpart,type_swap,flip_now,flip_echo,
    vector,table,equivariant,orbit,second_moment,
)
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_joint_quality_incidence_root import quality,R
from verification.zero_quantum_angular_echo import embed
from verification.zero_persistent_sphere_subject_selection_test import norm2


class ZeroWhySymmetryRootTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.root=output(active_base())

    def test_orbits_reveal_the_cause_of_two_magnitude_degrees_of_freedom(self):
        ops=(counterpart,type_swap)
        self.assertEqual(orbit((1,1),ops),{(1,1),(-1,-1)})
        self.assertEqual(orbit((1,-1),ops),{(1,-1),(-1,1)})
        self.assertEqual(orbit((1,1),(flip_now,flip_echo)),set(CELLS))

    def test_complete_covariant_classification_on_rational_grid(self):
        grid=tuple(map(F,range(-2,3)));values=tuple(product(grid,repeat=2))
        basic=[];independent=[]
        for outputs in product(values,repeat=4):
            candidate=dict(zip(CELLS,outputs))
            if equivariant(candidate,BASIC):basic.append(candidate)
            if equivariant(candidate,INDEPENDENT):independent.append(candidate)
        self.assertEqual(len(basic),25)
        self.assertTrue(all(candidate==table(candidate[1,1][0],candidate[1,-1][0])
                            for candidate in basic))
        self.assertEqual(len(independent),5)
        self.assertTrue(all(candidate==table(candidate[1,1][0],candidate[1,1][0])
                            for candidate in independent))
        # Exhaustive finite check is a control; the report proves the result
        # for all real-valued maps, not only this grid.

    def test_different_ratios_survive_sign_and_type_symmetry(self):
        uniform=table(1,1);unequal=table(1,2)
        self.assertTrue(equivariant(uniform,BASIC));self.assertTrue(equivariant(unequal,BASIC))
        self.assertTrue(equivariant(uniform,INDEPENDENT))
        self.assertFalse(equivariant(unequal,INDEPENDENT))
        self.assertEqual(second_moment(1,1),1)
        self.assertEqual(second_moment(1,2),F(5,2))
        for cell in CELLS:
            p=unequal[cell];opposite=tuple(-x for x in p)
            self.assertEqual(tuple(a+b for a,b in zip(p,opposite)),(0,0))
        # Differing sector ratio is dimensionless and cannot be removed
        # by a common change of units; neither model asserts felt magnitude.

    def test_uniform_cell_distribution_from_actual_complex_vectors(self):
        for label in (0,7,15):
            x=initial(relative_read(self.root,4,labels=(label,))[0]);total=norm2(x)
            cells={c:0. for c in CELLS}
            for s in (1,-1):
                _,_,rows=embed(x,s,4)
                for i in range(4):
                    m=sum(norm2(part[i]) for part in rows)/total
                    cells[quality(i,s)]+=m
                    self.assertEqual(quality(i,s)[0]*quality(i,s)[1],R[i])
            for c in CELLS:self.assertAlmostEqual(cells[c],0.25,places=12)
            for a,b in ((1,1),(1,2)):
                empirical=sum(cells[c]*float(vector(*c,a,b)[0]**2) for c in CELLS)
                self.assertAlmostEqual(empirical,float(second_moment(a,b)),places=12)
        # Same state, same projections, same two tested symmetries. The
        # assignments differ as operators; no measured value is asserted.

    def test_bad_inputs(self):
        with self.assertRaises(ValueError):vector(0,1,1,1)
        with self.assertRaises(ValueError):orbit((0,1),(counterpart,))
        with self.assertRaises(ValueError):equivariant({},BASIC)

if __name__=='__main__':unittest.main()
