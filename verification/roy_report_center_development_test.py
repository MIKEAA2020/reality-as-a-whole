#!/usr/bin/env python3
import unittest
import numpy as np
from roy_s09_eeg_report_transfer import feature
from roy_report_center_development import trial_rows, fit, assess, predict


def row(y,z,slot=1,bad=False,segment=('x',1)):
    return {'label':y,'feature':z,'slot':slot,'bad':bad,'segment':segment}


class CenterTests(unittest.TestCase):
    def test_tone_feature_and_short_center_report(self):
        fs=250; t=np.arange(2*fs)/fs
        self.assertGreater(feature(np.sin(2*np.pi*6.6666666667*t),fs,6.6666666667,8.5714285714),1)
        self.assertLess(feature(np.sin(2*np.pi*8.5714285714*t),fs,6.6666666667,8.5714285714),-1)
        t=np.arange(42*fs)/fs
        signal=np.sin(2*np.pi*6.6666666667*t)
        states=np.ones(42*fs,dtype=np.uint8)
        states[250:300]=3  # exactly one report-center sample at 1 s; 0.2 s duration
        mask=np.zeros_like(states)
        rows=trial_rows(signal,mask,states,('scan',0))
        self.assertEqual(len(rows),201)
        self.assertEqual(sum(r['label']==3 for r in rows),1)
        self.assertEqual(rows[0]['label'],3)
        mask[0]=1
        rows=trial_rows(signal,mask,states,('scan',0))
        self.assertTrue(rows[0]['bad']);self.assertIsNone(rows[0]['feature'])

    def test_equal_participant_class_weight_and_slot_ties(self):
        a=[row(1,0),row(1,0),row(2,4),row(3,8)]
        b=[row(1,10),row(2,14),row(3,18)]
        model=fit({'A':a,'B':b})
        self.assertEqual(model['class_mean_features'],[5,9,13])
        self.assertEqual(model['majority'],1)
        self.assertEqual(model['slot_rules'][0],1)
        with self.assertRaises(ValueError):fit({'A':[row(1,0),row(2,1)]})

    def test_prediction_independent_of_label_and_equal_segment_recall(self):
        model={'class_mean_features':[0,1,2], 'majority':1,'slot_rules':[1]*42}
        r=row(3,2,segment=('a',1));p=predict(r,model);r['label']=1
        self.assertEqual(p,predict(r,model))
        rows=[row(3,2,segment=('a',1)),row(3,0,segment=('a',1)),row(3,0,segment=('a',2)),
              row(0,2),row(3,None,bad=True,segment=('a',3)),row(1,0),row(2,1)]
        result=assess(rows,model)
        self.assertEqual((result['total_centers'],result['labeled_clean_centers']), (7,5))
        eeg=result['models']['eeg']
        self.assertEqual(eeg['mixed_eligible_segments'],2)
        self.assertAlmostEqual(eeg['mixed_segment_equal_weight_recall'],0.25)
        self.assertEqual(eeg['mixed_segments_with_any_hit'],1)
        self.assertAlmostEqual(eeg['recalls'][2],1/3)
        self.assertAlmostEqual(eeg['mixed_precision'],1.0)


if __name__=='__main__':unittest.main()
