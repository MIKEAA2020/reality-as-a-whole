"""Exact reconstruction limits on the original coherent quantum carrier."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_internal_reference_subject_valence_candidates_test import j_project
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_quantum_angular_echo import embed,apply_quality,difference_mass
from verification.zero_intrinsic_angular_estimation import continuum_stats,discrete_stats


def estimate(rows,s,means):
    """Old-carrier operator M J R times band-estimated magnitude.

    At tick 10 the actual valid support has R=B. R+ is the positive band;
    R- with J+ is the lower negative band, and R- with J- the upper.
    No angular register control is used by this operator.
    """
    out=[]
    for r,part in zip((1,-1),rows):
        mp,mm=(means[2],means[2]) if r==1 else (means[0],means[1])
        out.append([s*r*(float(mp)*j_project(x,1)-float(mm)*j_project(x,-1)) for x in part])
    return tuple(out)


def sign_only(rows,s,avg):
    return estimate(rows,s,(avg,avg,avg))


class IntrinsicAngularEstimationTests(unittest.TestCase):
    def test_exact_continuous_conditional_means_and_irreducible_errors(self):
        self.assertEqual(continuum_stats('absolute'),
            ((F(3,4),F(1,4),F(1,2)),F(5,96),F(1,2),F(1,12)))
        self.assertEqual(continuum_stats('swap_invariant'),
            ((F(1,6),F(1,6),F(5,6)),F(31,180),F(1,2),F(17,60)))
        for kind in ('absolute','swap_invariant'):
            expected=continuum_stats(kind)
            # Exact rational finite refinements converge to the same values.
            fine=discrete_stats(kind,400)
            for a,b in zip(fine[0],expected[0]):self.assertLess(abs(a-b),F(1,10000))
            for a,b in zip(fine[1:],expected[1:]):self.assertLess(abs(a-b),F(1,10000))

    def test_direct_full_quantum_quality_operator_and_old_only_estimator(self):
        root=output(active_base())
        for label,s,n in product((0,7,15),(1,-1),(4,8)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            u,v,rows=embed(x,s,n);total=norm2(v)
            for kind in ('absolute','swap_invariant'):
                means,risk,avg,base=discrete_stats(kind,n)
                target=apply_quality(rows,s,kind,'echo')
                prediction=estimate(rows,s,means)
                baseline=sign_only(rows,s,avg)
                self.assertAlmostEqual(difference_mass(target,prediction)/total,float(risk),places=12)
                self.assertAlmostEqual(difference_mass(target,baseline)/total,float(base),places=12)
                self.assertLessEqual(risk,base)
                # Real record output, not an angular-index-controlled fit.
                # An arbitrary constant perturbation of all means worsens
                # squared error by exactly its square, including complex state.
                shifted=estimate(rows,s,tuple(m+F(1,7) for m in means))
                self.assertAlmostEqual(difference_mass(target,shifted)/total,
                                       float(risk+F(1,49)),places=12)

    def test_band_is_exactly_readable_but_within_band_u_is_not(self):
        x=initial(relative_read(output(active_base()),4,labels=(0,))[0])
        u,v,rows=embed(x,1,8);total=norm2(v)
        # Each column is the complete original old quantum system plus R,
        # conditional on a later angular-register bin readout.
        def inner(i,j):return sum(np.vdot(part[i],part[j]) for part in rows)
        for i,j in ((0,1),(2,3),(4,7)):
            self.assertAlmostEqual((inner(i,i)/total).real,1/8,places=12)
            self.assertLess(abs(inner(i,j)-inner(i,i))/total,1e-13)
        for i,j in ((0,2),(0,4),(2,4)):
            self.assertLess(abs(inner(i,j))/total,1e-13)
        # Hence the three sector states are orthogonal, while every member of
        # one sector has the same density operator after withholding A.

if __name__=='__main__':unittest.main()
