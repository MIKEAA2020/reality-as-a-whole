import unittest
import model as m
class CompositionTests(unittest.TestCase):
    def test_01_source_type_feedback(self):self.assertEqual(m.strong_components(*m.type_graph()),frozenset({frozenset({'x','y'})}))
    def test_02_source_type_self_loop(self):self.assertIn(('y','y'),m.type_graph()[1])
    def test_03_event_edges_forward(self):self.assertTrue(m.all_forward(m.event_graph(5)[1]))
    def test_04_event_components_singletons(self):self.assertTrue(all(len(c)==1 for c in m.strong_components(*m.event_graph(5))))
    def test_05_no_return_to_same_occurrence(self):
        nodes,edges=m.event_graph(5)
        for a,b in edges:self.assertNotIn(a,m.reachable(nodes,edges,b))
    def test_06_later_return_is_not_same_event(self):
        nodes,edges=m.event_graph(3)
        self.assertIn((2,'x'),m.reachable(nodes,edges,(0,'x')));self.assertNotIn((0,'x'),m.reachable(nodes,edges,(2,'x')))
    def test_07_occurrence_count(self):self.assertEqual(len(m.event_graph(5)[0]),12)
    def test_08_type_quotient_creates_cycle(self):
        nodes,edges=m.event_graph(5);q=m.quotient(nodes,edges,lambda v:v[1])
        self.assertEqual(q,m.type_graph());self.assertEqual(len(m.strong_components(*q)),1)
    def test_09_quotient_not_injective(self):
        nodes,_=m.event_graph(5);self.assertGreater(len(nodes),len({v[1] for v in nodes}))
    def test_10_monitor_type_no_feedback(self):
        nodes,edges=m.type_graph(True);self.assertNotIn('x',m.reachable(nodes,edges,'u'));self.assertNotIn('y',m.reachable(nodes,edges,'v'))
    def test_11_source_monitor_type_components(self):self.assertEqual(m.strong_components(*m.type_graph(True)),frozenset({frozenset({'x','y'}),frozenset({'u'}),frozenset({'v'})}))
    def test_12_monitor_event_singletons(self):self.assertTrue(all(len(c)==1 for c in m.strong_components(*m.event_graph(4,True))))
    def test_13_weak_rule_includes_copy(self):
        nodes,edges=m.event_graph(4,True);parts=m.weak_components(nodes,edges)
        self.assertTrue(any((1,'u') in c and (0,'y') in c and (1,'x') in c for c in parts))
    def test_14_directed_rule_distinguishes_roles(self):
        nodes,edges=m.type_graph(True);self.assertIn('u',m.reachable(nodes,edges,'y'));self.assertNotIn('y',m.reachable(nodes,edges,'u'))
    def test_15_weak_rule_spans_window(self):
        nodes,edges=m.event_graph(5)
        self.assertEqual(m.weak_components(nodes,edges),frozenset({frozenset(nodes)}))
    def test_16_window_extends_complex(self):
        self.assertGreater(max(map(len,m.weak_components(*m.event_graph(5)))),max(map(len,m.weak_components(*m.event_graph(2)))))
    def test_17_inactive_history_still_singletons(self):self.assertTrue(all(len(c)==1 for c in m.strong_components(*m.event_graph(5,active=set()))))
    def test_18_inactive_weak_two_chains(self):self.assertEqual(len(m.weak_components(*m.event_graph(5,active=set()))),2)
    def test_19_one_active_update_merges_weak_chains(self):self.assertEqual(len(m.weak_components(*m.event_graph(5,active={2}))),1)
    def test_20_positive_support_merges_types(self):self.assertEqual(len(m.strong_components(*m.support_graph(.000001))),1)
    def test_21_zero_support_separates_types(self):self.assertEqual(len(m.strong_components(*m.support_graph(0))),2)
    def test_22_positive_support_allows_no_actual_update(self):self.assertGreater(m.no_update_probability(.001,10),.99)
    def test_23_relabel_preserves_component_sizes(self):
        nodes,edges=m.event_graph(5);q=m.quotient(nodes,edges,lambda v:(v[0],{'x':'a','y':'b'}[v[1]]))
        self.assertEqual(sorted(map(len,m.strong_components(*q))),sorted(map(len,m.strong_components(nodes,edges))))
    def test_24_validation(self):
        for call in (lambda:m.event_graph(0),lambda:m.event_graph(2,active={2}),lambda:m.support_graph(2),lambda:m.no_update_probability(-1,2),lambda:m.reachable({1},set(),2)):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
