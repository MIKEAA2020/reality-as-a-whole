import math
import unittest

try:
    from . import gravity_volume_jet_reconstruction as j
except ImportError:
    import gravity_volume_jet_reconstruction as j


class GravityVolumeJetTests(unittest.TestCase):
    def test_end_to_end_checks(self):
        r=j.run()
        self.assertGreater(r['uniform_chart_bounds_b_0_to_1']['certified_joint_success_probability'],.00098)
        self.assertLess(r['distinguishability_after_tracing_jet_and_k'],.86)
        self.assertLess(r['max_two_event_probability_error'],1e-12)

    def test_certified_filter_recovery_and_failure(self):
        bounds=j.rigorous_bounds(1)
        lo,hi=bounds['lower_squared_norm'],bounds['upper_squared_norm']
        for b in (0.,.8,1.):
            for k in (2.,2.496546215136184,4.,8.):
                for kap in j.KAPPAS:
                    jet=j.jet(k,kap,b)
                    r2=j.jet_norm2(jet)
                    filt=r2/hi
                    recov=lo/r2
                    # First and second measurement outcomes are complete.
                    self.assertTrue(0<=filt<=1 and 0<=recov<=1)
                    self.assertAlmostEqual(filt+(1-filt),1)
                    self.assertAlmostEqual(recov+(1-recov),1)
                    self.assertAlmostEqual(filt*recov,lo/hi)
                    # Recover the complex root amplitude, not just its norm.
                    root=.3+.4j
                    out=tuple(z*root/math.sqrt(hi) for z in jet)
                    v=tuple(z/math.sqrt(r2) for z in jet)
                    recovered=math.sqrt(lo/r2)*j.inner(v,out)
                    self.assertAlmostEqual(abs(recovered-math.sqrt(lo/hi)*root),0,places=13)

    def test_jet_survives_old_value_node(self):
        k=2.496546215136184
        value,gradient=j.jet(k,.6,0)
        self.assertLess(abs(value),1e-12)
        self.assertGreater(abs(gradient),.36)
        self.assertGreater(j.jet_norm2((value,gradient)),j.rigorous_bounds(0)['lower_squared_norm'])

    def test_direction_labels_are_equal_not_independent_branches(self):
        for k,b in ((2.,.8),(4.,1.),(8.,0.)):
            for kap in j.KAPPAS:
                q=j.directional(j.frame(k,kap,b))
                self.assertAlmostEqual(abs(q[0])**2,.5,places=12)
                self.assertAlmostEqual(abs(q[1])**2,.5,places=12)
        # Forgetting a slot is not the inverse of the coherent embedding.
        self.assertLess(abs(j.phase_calibrated_overlap(2.5,0)),.86)

    def test_limits_and_trivial_free_bound(self):
        self.assertAlmostEqual(j.potential_integral(1,0),.5)
        with self.assertRaises(ValueError): j.jet(1.9,.2,0)
        with self.assertRaises(ValueError): j.jet(2,.2,-.1)
        with self.assertRaises(ValueError): j.rigorous_bounds(3.1)
        self.assertGreater(j.rigorous_bounds(2.16)['certified_joint_success_probability'],0)
        with self.assertRaises(ValueError): j.potential_integral(0,.2)

if __name__=='__main__': unittest.main()
