import unittest
import model as m
class RelabelingTests(unittest.TestCase):
    def test_01_bijection_count(self):self.assertEqual(len(m.mappings()),24)
    def test_02_two_anchors_leave_two(self):self.assertEqual(len(m.calibrated({0:'a',1:'b'})),2)
    def test_03_survivors_disagree_on_unanchored_states(self):
        a,b=m.calibrated({0:'a',1:'b'});self.assertNotEqual(a[2],b[2]);self.assertNotEqual(a[3],b[3])
    def test_04_all_macro_maps_recover_report(self):
        for f in m.mappings():
            for x in m.STATES:self.assertEqual(m.physical_realization_of_report(f,x),x)
    def test_05_same_physical_intervention_predictions(self):self.assertEqual(len({m.predictions_under_physical_interventions(f) for f in m.mappings()}),1)
    def test_06_macro_conjugacy(self):
        for f in m.mappings():
            for x in m.STATES:self.assertEqual(m.macro_transition(f,f[x]),f[m.transition(x)])
    def test_07_all_target_contrasts_change_report_when_implemented(self):
        for f in m.mappings():self.assertEqual(len({m.implemented_intervention(f,q)['physical_report'] for q in m.TARGETS}),4)
    def test_08_same_target_name_can_require_different_physical_interventions(self):
        a,b=m.calibrated({0:'a',1:'b'});self.assertNotEqual(m.implemented_intervention(a,'c')['physical_state'],m.implemented_intervention(b,'c')['physical_state'])
    def test_09_actual_physical_history_does_not_change(self):
        history=m.physical_history(0,8)
        for f in m.mappings():self.assertEqual(tuple(m.inverse(f)[f[x]] for x in history),history)
    def test_10_third_anchor_selects_one_within_class(self):self.assertEqual(len(m.calibrated({0:'a',1:'b',2:'c'})),1)
    def test_11_inconsistent_anchors_reject_class(self):self.assertEqual(m.calibrated({0:'a',1:'a'}),())
    def test_12_validation(self):
        for call in (lambda:m.inverse(('a',)*4),lambda:m.transition(4),lambda:m.physical_history(0,-1),lambda:m.calibrated({5:'a'}),lambda:m.implemented_intervention(m.TARGETS,'z')):
            with self.assertRaises(ValueError):call()
if __name__=='__main__':unittest.main()
