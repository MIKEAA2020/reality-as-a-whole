import unittest

from field_lineage_persistence_gate import mutual_unique, unique_maximum, run, stage_components


class PersistenceGateTests(unittest.TestCase):
    def test_exhaustive_gate(self):
        self.assertEqual(run()['three_stage_history_relabelings'], 2048)

    def test_chain_joins_without_identifying_field_tokens(self):
        classes = stage_components(({(0, 0)}, {(0, 0)}))
        self.assertIn(frozenset({(0, 0), (1, 0), (2, 0)}), classes)
        self.assertEqual(len(classes), 4)  # plus one isolated stage in each layer

    def test_unique_global_matching_differs_from_mutual_degree(self):
        edges = {(0, 0), (0, 1), (1, 1)}
        self.assertEqual(mutual_unique(edges), frozenset())
        self.assertEqual(unique_maximum(edges), frozenset({(0, 0), (1, 1)}))


if __name__ == '__main__':
    unittest.main()
