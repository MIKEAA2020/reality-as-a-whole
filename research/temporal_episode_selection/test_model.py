import unittest
import model as m
class TemporalSelectionTests(unittest.TestCase):
    def test_01_only_constant_masks_are_unit_shift_invariant(self):
        for n in range(2,10):self.assertEqual({p for p in m.masks(n) if m.is_unit_shift_invariant(p)},{(False,)*n,(True,)*n})
    def test_02_finite_blocks_break_unit_shift_symmetry(self):
        for length in range(2,12):self.assertFalse(m.is_unit_shift_invariant(m.equal_length_boundaries(length)))
    def test_03_length_alone_leaves_all_phases(self):
        for length in range(2,12):self.assertEqual(len({m.equal_length_boundaries(length,offset) for offset in range(length)}),length)
    def test_04_phase_shifts_transport_boundary_masks(self):
        for length in range(2,12):self.assertEqual(m.shift(m.equal_length_boundaries(length,0)),m.equal_length_boundaries(length,1))
    def test_05_partition_membership_depends_on_phase(self):
        self.assertTrue(m.same_episode(0,1,3,0));self.assertFalse(m.same_episode(0,1,3,1))
    def test_06_shift_covariance_given_an_anchor(self):
        for t in range(-5,6):
            for u in range(-5,6):self.assertEqual(m.same_episode(t,u,3,2),m.same_episode(t+4,u+4,3,6))
    def test_07_regeneration_period_preserves_subgroup_only(self):
        self.assertEqual(m.stabilizer(m.equal_length_boundaries(4)),(0,));self.assertEqual(len(m.orbit(m.equal_length_boundaries(4))),4)
    def test_08_sliding_windows_overlap_without_partition(self):
        windows=m.sliding_windows(3,0,2);self.assertTrue(windows[0]&windows[1]);self.assertNotEqual(windows[0],windows[1])
    def test_09_sliding_family_transports_without_privileged_phase(self):
        left=m.sliding_windows(3,-3,4);right=m.sliding_windows(3,2,9)
        self.assertEqual(tuple(frozenset(t+5 for t in w) for w in left),right)
    def test_10_observation_origin_selects_different_partition(self):
        self.assertNotEqual(m.anchored_boundaries(4,0),m.anchored_boundaries(4,1));self.assertEqual(m.anchored_boundaries(4,0),m.anchored_boundaries(4,4))
    def test_11_selecting_all_phase_partitions_is_not_one_partition(self):
        # The pair is grouped by some allowed phases but separated by others.
        verdicts={m.same_episode(0,1,3,phase) for phase in range(3)};self.assertEqual(verdicts,{False,True})
    def test_12_validation(self):
        for call in (lambda:m.masks(0),lambda:m.shift(()),lambda:m.equal_length_boundaries(0),lambda:m.same_episode(0,1,0),lambda:m.sliding_windows(2,3,1)):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
