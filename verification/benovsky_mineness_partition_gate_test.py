import unittest
from benovsky_mineness_partition_gate import (partitions, valid_time_partition, edge_supported,
                                             relabel, partition_from_mask, run)


class MinenessPartitionGateTest(unittest.TestCase):
    def test_full_gate(self):
        r = run()
        self.assertEqual((r['all_four_event_partitions'], r['at_most_one_per_time'],
                          r['and_edge_supported'], r['and_exchange_invariant']), (15, 7, 4, 2))

    def test_same_physical_paths_different_link_rules(self):
        none = partition_from_mask(2, 0)
        both = partition_from_mask(2, 3)
        self.assertNotEqual(none, both)
        self.assertTrue(edge_supported(none) and edge_supported(both))
        self.assertEqual(relabel(none, (1, 0)), none)
        self.assertEqual(relabel(both, (1, 0)), both)

    def test_one_selected_path_breaks_exchange(self):
        one = partition_from_mask(2, 1)
        self.assertNotEqual(relabel(one, (1, 0)), one)

    def test_same_time_group_not_admissible(self):
        self.assertFalse(valid_time_partition(frozenset([frozenset(((0, 0), (1, 0)))])))

    def test_complete_partitions_no_duplicates(self):
        for n in range(5):
            p = list(partitions(tuple(range(n))))
            self.assertEqual(len(p), len(set(p)))
        self.assertEqual(len(list(partitions(tuple(range(4))))), 15)


if __name__ == '__main__':
    unittest.main()
