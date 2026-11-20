import unittest
from faced_report_baseline import validate, scores, predict, splits

def row(i,on=0,d=1):
 return {'video_index':str(i),'onset':str(on),'duration':str(d),'Valence':'3','emotion_label':'Joy','binary_label':'positive','sample':'0'}
class Tests(unittest.TestCase):
 def test_duplicate_and_overlap(self):
  with self.assertRaisesRegex(ValueError,'duplicate'): validate([row(1),row(1,2)],10)
  with self.assertRaisesRegex(ValueError,'overlapping'): validate([row(1),row(2,.5)],10)
 def test_scores(self):
  s=scores([0,3],[1,1]); self.assertEqual(s['mae'],1.5);self.assertAlmostEqual(s['rmse'],(2.5)**.5)
 def test_fallback(self):
  train=[{'y':4,'cat':'a'}]; test=[{'y':2,'cat':'b'}]
  self.assertEqual(predict(train,test,'category'),([4.],1))
 def test_splits(self):
  rs=[{'subject':p,'video':v,'cat':'a' if v<=3 else 'b','y':2} for p in range(10) for v in range(1,7)]
  seen=[]
  for train,test in splits(rs,True):
   self.assertTrue(set(r['subject'] for r in train).isdisjoint(r['subject'] for r in test))
   self.assertTrue(set(r['video'] for r in train).isdisjoint(r['video'] for r in test))
   seen.extend((r['subject'],r['video']) for r in test)
  self.assertEqual(len(seen),len(rs)); self.assertEqual(len(set(seen)),len(rs))
 def test_invalid_range(self):
  x=row(2);x['Valence']='7.1'
  with self.assertRaises(ValueError): validate([x],10)
if __name__=='__main__':unittest.main()
