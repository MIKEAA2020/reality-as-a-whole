import itertools
import unittest

try:
    from . import self_cancelling_performance_control as m
except ImportError:
    import self_cancelling_performance_control as m


class PerformanceTests(unittest.TestCase):
    def test_worked_cycle(self):
        r=m.run()
        self.assertTrue(r['trajectory_is_nontrivial'])
        self.assertTrue(r['endpoint_returns_to_initial'])
        self.assertEqual(r['sum_at_each_stage'],[0,0,0,0])

    def test_shift_is_bijection_preserves_total_and_cycles(self):
        for q in itertools.product(range(-3,4),repeat=3):
            self.assertEqual(sum(m.shift(q)),sum(q))
            self.assertEqual(m.shift(m.shift(m.shift(q))),q)

    def test_not_every_state_has_nontrivial_trajectory(self):
        self.assertEqual(m.shift((0,0,0)),(0,0,0))
        self.assertEqual(m.shift((1,1,1)),(1,1,1))
        self.assertNotEqual(m.shift((1,-1,0)),(1,-1,0))

    def test_entire_record_not_equal_to_endpoint(self):
        a=(1,-1,0)
        seq=[a,m.shift(a),m.shift(m.shift(a)),a]
        self.assertNotEqual([a],seq)
        self.assertEqual(seq[0],seq[-1])

    def test_both_components_need_one_common_witness(self):
        A={1};B={2}
        self.assertTrue(A and B)
        self.assertFalse(A & B)
        self.assertTrue(A & {1,2})

    def test_bad_size(self):
        with self.assertRaises(ValueError):m.shift((1,2))

if __name__=='__main__':unittest.main()
