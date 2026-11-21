import unittest,math
from fractions import Fraction as F
from integrated_cross_scale_quality import EDGES,STATES,PAIRS,signature,quality,horizon_winners,run
from causal_influence_subject_gate import influence_graph
from competing_subject_constitution_rules import overlapping_local_maxima

class TestIntegratedCrossScale(unittest.TestCase):
 def test_pair_extension_equals_original(self):
  for s in STATES:
   for pair in PAIRS:
    sig=signature(s,pair,EDGES)
    self.assertEqual(quality(sig),quality(sig,'binary'))
    self.assertIn(quality(sig),[0,1])
 def test_tie_has_no_selected_quality(self):
  _,edges=influence_graph(F(1,2));w,ties=overlapping_local_maxima(frozenset(range(4)),edges)
  self.assertFalse(w);self.assertEqual(len(ties),6)
 def test_bad_domain(self):
  with self.assertRaises(ValueError):quality(())
  with self.assertRaises(ValueError):quality(((F(1,2),1),),'wrong')
 def test_distribution_and_disagreement(self):
  r=run();d=r['quality_distribution'];self.assertEqual(sum(F(x['probability']) for x in d),1)
  self.assertEqual(r['model_probability_of_law_disagreement'],'5/8')
  self.assertEqual(r['conditional_contrast']['probability'],'15/64')
  self.assertLess(r['conditional_contrast']['graded'],r['conditional_contrast']['binary'])
  self.assertEqual(r['relabeling_and_sign_transport_checks'],18432)
 def test_horizons(self):
  a,at=horizon_winners(1);b,bt=horizon_winners(9)
  self.assertEqual(a,PAIRS);self.assertEqual(b,{frozenset(range(4))});self.assertFalse(at or bt)
if __name__=='__main__':unittest.main()
