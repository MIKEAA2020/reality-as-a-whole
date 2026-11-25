"""Exact and geometric checks for the common sphere/echo extension."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np
from verification.zero_sphere_angular_echo import (
    BANDS,initial,state,angular_swap,magnitude,quality,coarse_tick,
    magnitude_moments,band_mass,reference_disagreement,
)
from verification.zero_stationary_battery_bridge import TICKS,stationary_weights
from verification.zero_stationary_subject_incidence import anchor_flip
from verification.zero_stationary_clock_claim_quality import joint_at_tick


class SphereAngularEchoTests(unittest.TestCase):
    def test_cap_threshold_recovers_old_sector_and_is_unique_in_chosen_family(self):
        # For b=-, z=- represented by u<tau, P=(tau+1)/2=1/4
        # makes tau=-1/2. This is only unique within this one cap family.
        tau=2*F(1,4)-1
        self.assertEqual(tau,F(-1,2))
        self.assertEqual({(b,z):band_mass(a,c) for a,c,b,z in BANDS},
                         {(1,1):F(1,2),(-1,1):F(1,4),(-1,-1):F(1,4)})

    def test_every_old_tick_and_joint_claim_table_recovered(self):
        old=stationary_weights()
        for t in range(TICKS):
            self.assertEqual(coarse_tick(t),{k:TICKS*v for k,v in old[t].items() if v})
            tab=joint_at_tick(t)
            for c,d in product((False,True),repeat=2):
                new=sum((p for (b,j,r,s),p in coarse_tick(t).items()
                         if (r==b)==c and (r==-1)==d),F(0))
                self.assertEqual(new,tab.get((c,d),0))
        self.assertEqual(coarse_tick(20),coarse_tick(0))

    def test_exact_first_absolute_moments_in_each_sector(self):
        self.assertEqual(magnitude_moments('absolute'),{
            (1,1):(F(1,2),F(1,4)),
            (-1,1):(F(1,4),F(1,16)),
            (-1,-1):(F(1,4),F(3,16))})
        self.assertEqual(magnitude_moments('swap_invariant'),{
            (1,1):(F(1,2),F(5,12)),
            (-1,1):(F(1,4),F(1,24)),
            (-1,-1):(F(1,4),F(1,24))})
        for kind in ('absolute','swap_invariant'):
            self.assertEqual(sum(moment for mass,moment in magnitude_moments(kind).values()),F(1,2))

    def test_same_reference_clock_disagreement_has_magnitude_predictions(self):
        self.assertEqual(reference_disagreement(1,2,'absolute'),(F(1,10),F(1,20)))
        self.assertEqual(reference_disagreement(2,2,'absolute'),(F(1,20),F(3,80)))
        self.assertEqual(reference_disagreement(1,2,'swap_invariant'),(F(1,10),F(1,60)))
        self.assertEqual(reference_disagreement(2,2,'swap_invariant'),(F(1,20),F(1,120)))
        # The q=1 contrast samples all of b=-; q=2 samples z=- only.
        # The differing angle distribution, not speed alone, determines g.
        with self.assertRaises(ValueError):reference_disagreement(2,1,'absolute')

    def test_sign_reversal_preserves_records_and_cancels_locally(self):
        for u,s,t,kind,port in product((F(-7,8),F(-1,4),F(1,4)),(1,-1),
                                       range(21),('absolute','swap_invariant'),('now','echo')):
            x,y=state(t,u,s),state(t,u,-s)
            self.assertEqual(x[:3],y[:3])
            self.assertEqual(quality(t,u,s,kind,port),-quality(t,u,-s,kind,port))
            self.assertNotEqual(quality(t,u,s,kind,port),0)
        # This is signed model arithmetic, not a proof of actual experiences.

    def test_angular_swap_implements_old_physical_port_swap(self):
        for u,s in product((F(-7,8),F(-3,4),F(-1,4),F(1,4)),(1,-1)):
            other=angular_swap(u)
            self.assertEqual(angular_swap(other),u)
            self.assertEqual(state(10,other,s),anchor_flip(state(10,u,s)))
        # At every clock tick, the transformed input remains in the same
        # 20-step history construction and returns after the cycle.
        for u,s in product((F(-7,8),F(-1,4),F(1,4)),(1,-1)):
            self.assertEqual(state(20,angular_swap(u),s),initial(angular_swap(u),s))

    def test_equal_signs_do_not_guarantee_magnitude_swap_symmetry(self):
        u=F(-1,4);s=1;v=angular_swap(u)
        self.assertEqual(quality(10,u,s,'absolute','now'),F(-1,4))
        self.assertEqual(quality(10,v,s,'absolute','echo'),F(-3,4))
        self.assertNotEqual(quality(10,u,s,'absolute','now'),quality(10,v,s,'absolute','echo'))
        for u,s in product((F(-7,8),F(-3,4),F(-1,4),F(1,4)),(1,-1)):
            v=angular_swap(u)
            self.assertEqual(magnitude(u,'swap_invariant'),magnitude(v,'swap_invariant'))
            self.assertEqual(quality(10,u,s,'swap_invariant','now'),
                             quality(10,v,s,'swap_invariant','echo'))

    def test_angular_magnitude_requires_more_than_old_record_boundary(self):
        u,v=F(-1,4),F(-1,8)
        for t in range(21):
            self.assertEqual(state(t,u,1),state(t,v,1))
            for kind in ('absolute','swap_invariant'):
                self.assertNotEqual(magnitude(u,kind),magnitude(v,kind))
                self.assertNotEqual(quality(t,u,1,kind,'echo'),quality(t,v,1,kind,'echo'))
        # The angular carrier/access assumption is genuinely additional:
        # the old M,j,R sign algebra alone cannot specify this magnitude.

    def test_rotation_covariance_and_area_density(self):
        # Numerical geometry sanity check; exact area/moments use integration.
        rng=np.random.default_rng(7123)
        def unit(v):return v/np.linalg.norm(v)
        n,m,k=(unit(rng.normal(size=3)) for _ in range(3))
        axis=unit(rng.normal(size=3));a=.73
        cross=np.array([[0,-axis[2],axis[1]],[axis[2],0,-axis[0]],[-axis[1],axis[0],0]])
        rot=np.eye(3)+np.sin(a)*cross+(1-np.cos(a))*(cross@cross)
        self.assertAlmostEqual(n@m,(rot@n)@(rot@m),places=13)
        self.assertAlmostEqual(k@m,(rot@k)@(rot@m),places=13)
        # Analytically dOmega=dphi du and uniform k gives each s sign half.

if __name__=='__main__':unittest.main()
