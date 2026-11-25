"""Full relational sphere lift and symmetry controls on the old echo."""
from fractions import Fraction as F
from itertools import product
from math import cos,pi,sqrt
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_quantum_angular_echo import embed,apply_swap,difference_mass,mass
from verification.zero_coherent_signed_counterpart import exchange
from verification.zero_gauge_angular_pair import physical,encode,charges
from verification.zero_sphere_angular_echo import magnitude
from verification.zero_spherical_invariant_echo import (
    unit,angle,rodrigues,h,reflected_direction,bin_index,spherical_bin_amplitude,
    symmetric_density,density_reweight,
)


def pair(m,u,az=0.):
    m=unit(m);seed=np.array([1.,0.,0.])
    if abs(np.dot(m,seed))>.9:seed=np.array([0.,1.,0.])
    e=unit(seed-m*np.dot(seed,m));f=np.cross(m,e)
    return m,u*m+sqrt(1-u*u)*(cos(az)*e+np.sin(az)*f)


def frame(m,n):
    m=unit(m);n=unit(n);e=unit(n-angle(m,n)*m)
    return np.column_stack((e,np.cross(m,e),m))


def integral(a,b,func):
    x,w=np.polynomial.legendre.leggauss(64)
    v=(b-a)*x/2+(a+b)/2
    return float((b-a)/4*sum(weight*func(y) for y,weight in zip(v,w)))


class SphericalInvariantEchoTests(unittest.TestCase):
    def test_common_rotation_orbits_are_exactly_relative_angles(self):
        axes=((0,0,1),(1,2,3),(-2,1,1))
        for u in (-.9,-.4,.2,.8):
            for a,b in product(axes,repeat=2):
                m1,n1=pair(a,u,.3);m2,n2=pair(b,u,1.2)
                r=frame(m2,n2)@frame(m1,n1).T
                np.testing.assert_allclose(r.T@r,np.eye(3),atol=1e-13)
                self.assertAlmostEqual(np.linalg.det(r),1.,places=13)
                np.testing.assert_allclose(r@m1,m2,atol=1e-13)
                np.testing.assert_allclose(r@n1,n2,atol=1e-13)
        # Ordered sphere pairs at fixed u are one SO(3) orbit. The poles are
        # measure-zero; no prior external global axis is selected.

    def test_area_pushforward_and_normalized_spherical_latitudes(self):
        # For independent uniform sphere directions n,m, u=n·m has du/2.
        # Discrete normalized product-area quadrature verifies low moments.
        x,w=np.polynomial.legendre.leggauss(8);phis=np.arange(16)*2*pi/16
        vectors=[];weights=[]
        for u,weight in zip(x,w):
            for phi in phis:
                vectors.append([sqrt(1-u*u)*cos(phi),sqrt(1-u*u)*np.sin(phi),u])
                weights.append(weight/(2*len(phis)))
        vectors=np.array(vectors);weights=np.array(weights)
        dots=vectors@vectors.T;ww=np.outer(weights,weights)
        self.assertAlmostEqual(float(np.sum(ww)),1.,places=13)
        self.assertAlmostEqual(float(np.sum(ww*dots*dots)),1/3,places=13)
        self.assertAlmostEqual(float(np.sum(ww*dots**4)),1/5,places=13)
        for n in (4,8,16):
            for i in range(n):
                a=F(-1)+F(2*i,n);b=a+F(2,n)
                self.assertEqual((b-a)/2,F(1,n))
                # sqrt(n) 1_bin is normalized on the full m,n space.
                self.assertEqual(F(n)*(b-a)/2,1)

    def test_geometric_reflection_is_rotation_covariant_and_involutive(self):
        for u in (-.95,-.75,-.55,-.45,-.2,.2,.7):
            for axis in ((0,0,1),(1,2,3),(-2,1,1)):
                m,n=pair(axis,u,.37)
                nn=reflected_direction(m,n)
                self.assertAlmostEqual(np.linalg.norm(nn),1.,places=12)
                self.assertAlmostEqual(angle(m,nn),h(u),places=12)
                np.testing.assert_allclose(reflected_direction(m,nn),n,atol=1e-12)
                r=rodrigues((1,3,-2),.83)
                np.testing.assert_allclose(reflected_direction(r@m,r@n),r@nn,atol=1e-12)
        # u -> h(u) has slope ±1 on its pieces and preserves du/2; azimuth
        # is unchanged. This exact Jacobian proves product-area preservation.
        with self.assertRaises(ValueError):reflected_direction((0,0,1),(0,0,-1))

    def test_exact_common_continuous_spherical_embedding_of_quantum_echo(self):
        x=initial(relative_read(output(active_base()),4,labels=(0,))[0])
        _,v,coarse=embed(x,1,4);_,_,fine=embed(x,1,16);total=norm2(v)
        for u in (-.91,-.61,-.42,-.13,.19,.42,.78):
            m,n=pair((1,2,3),u,.61);r=rodrigues((2,-1,3),1.1)
            i,a=spherical_bin_amplitude(angle(m,n),4)
            j,b=spherical_bin_amplitude(angle(m,n),16)
            ii,_=spherical_bin_amplitude(angle(r@m,r@n),4)
            jj,_=spherical_bin_amplitude(angle(r@m,r@n),16)
            self.assertEqual((i,j),(ii,jj))
            for part,other in zip(coarse,fine):
                self.assertLess(norm2(a*part[i]-b*other[j])/total,1e-24)
        # Jφ(m,n)=sqrt(2) φ(n·m) is an isometry from L²(du) to the
        # simultaneous-rotation invariant subspace of L²(S²×S²,dΩ²/(4π)²).

    def test_symmetric_full_support_density_not_selected_by_subgroup(self):
        eps=.5
        for u in (-.93,-.79,-.57,-.34,-.11,.11,.34,.79,.93):
            self.assertGreater(symmetric_density(u,eps),0)
            self.assertAlmostEqual(symmetric_density(u,eps),symmetric_density(-u,eps),places=13)
            self.assertAlmostEqual(symmetric_density(u,eps),symmetric_density(h(u),eps),places=13)
        for a,b,expected in ((-1,-.5,.25),(-.5,0,.25),(0,1,.5)):
            self.assertAlmostEqual(integral(a,b,lambda u:symmetric_density(u,eps)),expected,places=13)
        # The same coarse physical sign weights, but different positive,
        # nonzero within-band densities and nonzero changes in magnitudes.
        g1low=integral(-1,-.5,lambda u:-u*symmetric_density(u,eps))/.25
        g1mid=integral(-.5,0,lambda u:-u*symmetric_density(u,eps))/.25
        g2low=integral(-1,-.5,lambda u:-u*(u+1)*symmetric_density(u,eps))/.25
        g2pos=integral(0,1,lambda u:u*(u+1)*symmetric_density(u,eps))/.5
        self.assertAlmostEqual(g1low,.75+eps/pi**2,places=13)
        self.assertAlmostEqual(g1mid,.25-eps/pi**2,places=13)
        self.assertAlmostEqual(g2low,1/6-eps/(2*pi**2),places=13)
        self.assertAlmostEqual(g2pos,5/6+eps/(2*pi**2),places=13)
        # Density symmetry is not a proof that every geometric flip is a
        # symmetry of the old quantum records, or that outcomes are subjects.

    def test_symmetric_reweighted_actual_quantum_state_keeps_old_reduction(self):
        root=output(active_base())
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            u,v,rows=embed(x,s,8);total=norm2(v);eps=.5
            new=density_reweight(rows,eps)
            self.assertAlmostEqual(mass(new)/total,1.,places=12)
            self.assertLess(difference_mass(apply_swap(new,s),new)/total,1e-24)
            for band in (range(0,2),range(2,4),range(4,8)):
                ids=list(band);weight=sum(symmetric_density(float(u[i]),eps) for i in ids)
                self.assertAlmostEqual(weight,len(ids),places=12)
                # Identical old/R vectors within each bin band + equal total
                # density weight gives equality of every old-only effect.
                for part in rows:
                    for i in ids:self.assertLess(norm2(part[i]-part[ids[0]])/total,1e-24)
            before=sum(norm2(part[0]) for part in rows)/total
            after=sum(norm2(part[0]) for part in new)/total
            self.assertAlmostEqual(before,1/8,places=12)
            self.assertNotAlmostEqual(after,before,places=5)
            if s==1:
                _,_,other=embed(x,-1,8)
                other=density_reweight(other,eps)
                negative=tuple([-x for x in part] for part in other)
                self.assertLess(difference_mass(exchange(new,10),negative)/total,1e-24)
            for k,i in product((1,-1),range(8)):
                item=encode(k,i,8)
                self.assertEqual(physical(*item),1)
                e1,e2,_=charges(*item,8,'swap_invariant')
                self.assertEqual(e1+e2,0)
        # Angular access distinguishes the physical preparations; this is not
        # a pure gauge relabeling. The full coherent states are different.

    def test_independent_sphere_rotations_select_uniform_marginal_not_full_echo_symmetry(self):
        m,n1=pair((0,0,1),-.75);_,n2=pair((0,0,1),.75)
        r=rodrigues((0,1,0),np.arccos(.75)-np.arccos(-.75))
        np.testing.assert_allclose(r@n1,n2,atol=1e-13)
        self.assertAlmostEqual(angle(m,n1),-.75,places=13)
        self.assertAlmostEqual(angle(m,n2),.75,places=13)
        # A nonconstant SO(3)-diagonal invariant density is not invariant
        # under arbitrary independent rotations; product Haar is the unique
        # normalized measure invariant under SO(3)×SO(3).
        self.assertNotAlmostEqual(symmetric_density(.1,.5),symmetric_density(.4,.5),places=5)
        x=initial(relative_read(output(active_base()),4,labels=(0,))[0])
        _,v,rows=embed(x,1,4);total=norm2(v)
        self.assertAlmostEqual(norm2(rows[0][0])/total,0.,places=13)
        self.assertAlmostEqual(norm2(rows[1][0])/total,.25,places=13)
        self.assertAlmostEqual(norm2(rows[0][3])/total,.25,places=13)
        self.assertAlmostEqual(norm2(rows[1][3])/total,0.,places=13)
        # Changing u while keeping the old echo memory R fixed cannot leave
        # the complete correlated state invariant, even when its angular
        # marginal is independent-rotation invariant.

if __name__=='__main__':unittest.main()
