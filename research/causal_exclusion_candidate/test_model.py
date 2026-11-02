import unittest
import model as m
class CausalExclusionTests(unittest.TestCase):
    def test_01_stochastic_kernels(self):
        for k in (m.source_monitor(),m.coupled_sources(0),m.coupled_sources(.1),m.coupled_sources(1),m.feedforward_copy()):self.assertIn(m.validate(k),(2,4))
    def test_02_source_score_derived(self):self.assertAlmostEqual(m.irreducibility(m.deterministic(2,m.source_update)),.75)
    def test_03_independent_whole_factorizes(self):self.assertAlmostEqual(m.irreducibility(m.coupled_sources(0)),0)
    def test_04_independent_cores_selected(self):self.assertEqual(set(m.maximal_regions(m.coupled_sources(0))),{(0,1),(2,3)})
    def test_05_source_excludes_its_monitor_in_fixture(self):self.assertEqual(set(m.maximal_regions(m.source_monitor())),{(0,1)})
    def test_06_monitor_only_score_zero(self):self.assertEqual(m.scores(m.source_monitor())[(2,3)],0)
    def test_07_weak_bridge_does_not_merge(self):
        for epsilon in (.001,.01,.1):self.assertEqual(set(m.maximal_regions(m.coupled_sources(epsilon))),{(0,1),(2,3)})
    def test_08_weak_bridge_whole_score_positive(self):self.assertGreater(m.irreducibility(m.coupled_sources(.001)),0)
    def test_09_strong_bridge_whole_selected(self):self.assertEqual(set(m.maximal_regions(m.coupled_sources(1))),{(0,1,2,3)})
    def test_10_boundary_switch_is_comparison_not_positive_support(self):
        self.assertEqual(set(m.maximal_regions(m.coupled_sources(.55))),{(0,1),(2,3)})
        self.assertEqual(set(m.maximal_regions(m.coupled_sources(.6))),{(0,1,2,3)})
    def test_11_score_bounds(self):
        for epsilon in (0,.1,.5,1):self.assertTrue(all(0<=v<=1 for v in m.scores(m.coupled_sources(epsilon)).values()))
    def test_12_physical_coordinate_permutation_covariance(self):
        k=m.source_monitor();perm=(2,3,0,1)
        def swap(x):return sum(((x>>i)&1)<<perm[i] for i in range(4))
        moved=tuple(tuple(k[swap(x)][swap(y)] for y in range(16)) for x in range(16))
        self.assertEqual(set(m.maximal_regions(moved)),{(2,3)})
    def test_13_temporal_grain_counterexample(self):
        k=m.deterministic(2,m.source_update)
        self.assertAlmostEqual(m.irreducibility(k),.75);self.assertEqual(m.irreducibility(m.power(k,3)),0)
    def test_14_feedforward_counterexample(self):
        # Positive score despite x'=0, y'=x having no recurrent dependency loop.
        k=m.feedforward_copy();self.assertAlmostEqual(m.irreducibility(k),.5);self.assertEqual(set(m.maximal_regions(k)),{(0,1)})
    def test_15_identity_kernel_not_integrated(self):self.assertEqual(m.irreducibility(m.deterministic(2,lambda x:x)),0)
    def test_16_validation(self):
        for call in (lambda:m.validate(((.2,.2),(.5,.5))),lambda:m.coupled_sources(-1),lambda:m.regional(m.source_monitor(),()),lambda:m.power(m.source_monitor(),0)):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
