import unittest
import model as m

V=m.Content('visual',1);A=m.Content('auditory',0)
PROPOSALS=(m.Proposal(V,2),m.Proposal(A,1))

class WorkspaceTests(unittest.TestCase):
    def test_01_competitive_entry(self):self.assertEqual(m.step(m.State(),PROPOSALS).winner,V)
    def test_02_auditory_can_win(self):self.assertEqual(m.step(m.State(),(m.Proposal(V,1),m.Proposal(A,2))).winner,A)
    def test_03_one_slot_capacity(self):self.assertIsInstance(m.step(m.State(),PROPOSALS).state.workspace,m.Content)
    def test_04_deterministic_tie_rule_declared(self):self.assertEqual(m.select((m.Proposal(V),m.Proposal(A))),V)
    def test_05_same_content_multiple_uses(self):
        out=m.step(m.State(),PROPOSALS)
        self.assertEqual(out.state.memory,V);self.assertEqual(out.action,1);self.assertIs(out.comparison,True)
    def test_06_task_switch_without_content_change(self):
        a=m.step(m.State(),PROPOSALS,rule='copy');b=m.step(m.State(),PROPOSALS,rule='invert')
        self.assertEqual(a.state.workspace,b.state.workspace);self.assertEqual((a.action,b.action),(1,0))
    def test_07_comparison_context(self):
        self.assertTrue(m.step(m.State(),PROPOSALS,target=1).comparison);self.assertFalse(m.step(m.State(),PROPOSALS,target=0).comparison)
    def test_08_maintenance(self):
        first=m.step(m.State(),PROPOSALS);second=m.step(first.state)
        self.assertEqual(second.state.workspace,V);self.assertEqual(second.action,1)
    def test_09_maintenance_lesion(self):self.assertIsNone(m.step(m.State(workspace=V),config=m.Config(maintain=False)).state.workspace)
    def test_10_report_lesion_preserves_other_uses(self):
        normal=m.step(m.State(),PROPOSALS);lesion=m.step(m.State(),PROPOSALS,config=m.Config(report=False))
        self.assertIsNone(lesion.report);self.assertEqual((lesion.state,lesion.action,lesion.comparison),(normal.state,normal.action,normal.comparison))
    def test_11_readout_preserved_without_distribution(self):
        normal=m.step(m.State(),PROPOSALS);copy=m.step(m.State(),PROPOSALS,config=m.Config(distribute=False))
        self.assertEqual(normal.report,copy.report);self.assertEqual(normal.monitor,copy.monitor)
        self.assertIsNone(copy.action);self.assertIsNone(copy.comparison);self.assertIsNone(copy.state.memory)
    def test_12_local_discrimination_survives_entry_lesion(self):
        out=m.step(m.State(),PROPOSALS,config=m.Config(entry=False))
        self.assertEqual(dict(out.local),{'visual':1,'auditory':0});self.assertIsNone(out.state.workspace);self.assertIsNone(out.action)
    def test_13_workspace_intervention_propagates(self):
        out=m.step(m.State(),PROPOSALS,force_workspace=A)
        self.assertEqual(out.state.memory,A);self.assertEqual(out.action,0);self.assertEqual(out.report,0);self.assertFalse(out.comparison)
        self.assertEqual(dict(out.local)['visual'],1)
    def test_14_passive_monitor_intervention_does_not_propagate(self):
        normal=m.step(m.State(),PROPOSALS);forced=m.step(m.State(),PROPOSALS,force_monitor=A)
        self.assertEqual(m.signature(normal),m.signature(forced));self.assertEqual(normal.state,forced.state);self.assertNotEqual(normal.monitor,forced.monitor)
    def test_15_feedback_changes_later_selection(self):
        first=m.step(m.State(),(m.Proposal(A),));second=m.step(first.state,(m.Proposal(V),m.Proposal(A)))
        self.assertEqual(second.winner,A)
    def test_16_feedback_lesion_changes_later_selection(self):
        first=m.step(m.State(),(m.Proposal(A),));second=m.step(first.state,(m.Proposal(V),m.Proposal(A)),config=m.Config(feedback=False))
        self.assertEqual(second.winner,V)
    def test_17_feedback_is_not_unlimited(self):
        out=m.step(m.State(feedback='auditory'),(m.Proposal(A,1),m.Proposal(V,2)))
        self.assertEqual(out.winner,V)
    def test_18_action_lesion_spares_memory_and_comparison(self):
        out=m.step(m.State(),PROPOSALS,config=m.Config(action=False))
        self.assertEqual(out.state.memory,V);self.assertTrue(out.comparison);self.assertIsNone(out.action);self.assertIsNone(out.state.feedback)
    def test_19_distribution_changes_future_feedback(self):
        first=m.step(m.State(),(m.Proposal(A),),config=m.Config(distribute=False))
        second=m.step(first.state,(m.Proposal(V),m.Proposal(A)))
        self.assertEqual(second.winner,V)
    def test_20_both_sources_all_task_values(self):
        for source in m.SOURCES:
            for value in (0,1):
                for rule in m.RULES:
                    content=m.Content(source,value);out=m.step(m.State(),(m.Proposal(content),),rule=rule)
                    self.assertEqual(out.state.memory,content);self.assertEqual(out.action,value if rule=='copy' else 1-value)
    def test_21_readout_alone_cannot_identify_distribution(self):
        for value in (0,1):
            proposals=(m.Proposal(m.Content('visual',value)),)
            a=m.step(m.State(),proposals);b=m.step(m.State(),proposals,config=m.Config(distribute=False))
            self.assertEqual(a.report,b.report);self.assertNotEqual(m.signature(a),m.signature(b))
    def test_22_preserved_memory_not_current_availability(self):
        out=m.step(m.State(memory=V),config=m.Config(entry=False))
        self.assertEqual(out.state.memory,V);self.assertIsNone(out.action);self.assertIsNone(out.comparison)
    def test_23_no_input_and_no_maintained_content(self):
        out=m.step(m.State());self.assertIsNone(out.state.workspace);self.assertIsNone(out.report);self.assertIsNone(out.action)
    def test_24_validation(self):
        for call in (lambda:m.Content('other',0),lambda:m.Content('visual',2),lambda:m.Proposal(V,-1),lambda:m.select((m.Proposal(V),m.Proposal(V))),lambda:m.step(m.State(),rule='unknown'),lambda:m.step(m.State(),force_workspace=2),lambda:m.Config(report=1)):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
