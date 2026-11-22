#!/usr/bin/env python3
import shutil
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch
import roy_s02_frozen_center_transfer as frozen


class FrozenTest(unittest.TestCase):
    def test_manifest_constraints(self):
        manifest={str(s):'a'*64 for s in frozen.SCANS}
        self.assertEqual(frozen.validate_manifest(manifest),manifest)
        for bad in ({}, {**manifest,'3':'a'*64}, {**manifest,'1':'A'*64}):
            with self.assertRaises(ValueError):frozen.validate_manifest(bad)

    def test_fixed_receipt_and_tamper(self):
        root=Path(__file__).resolve().parent
        model=frozen.load_frozen(root)
        self.assertEqual(model['training_participants'],['S01','S09'])
        with tempfile.TemporaryDirectory(dir='.arena') as d:
            target=Path(d)
            for name in frozen.FROZEN:shutil.copyfile(root/name,target/name)
            with (target/'roy_report_center_development.json').open('a') as f:f.write(' ')
            with self.assertRaises(ValueError):frozen.load_frozen(target)

    def test_exact_scan_order_and_pooling(self):
        manifest={str(s):'a'*64 for s in frozen.SCANS}
        calls=[]
        def mock_read(path,expected,scan):
            calls.append((path.name,expected,scan))
            return [{'label':3,'feature':2,'bad':False,'slot':1,'segment':(scan,0)}]
        model={'class_mean_features':[0,1,2], 'majority':1,'slot_rules':[1]*42}
        with patch.object(frozen,'sha',return_value='a'*64), patch.object(frozen,'read_scan',side_effect=mock_read):
            out=frozen.evaluate(Path('input'),manifest,model)
        with patch.object(frozen,'sha',return_value='b'*64), patch.object(frozen,'read_scan') as read:
            with self.assertRaises(ValueError): frozen.evaluate(Path('input'),manifest,model)
            read.assert_not_called()
        self.assertEqual([x[2] for x in calls],list(frozen.SCANS))
        self.assertEqual(out['pooled']['labeled_clean_centers'],6)
        self.assertEqual(out['pooled']['models']['eeg']['mixed_eligible_segments'],6)
        self.assertEqual(out['pooled']['models']['eeg']['recalls'][2],1)
        self.assertIsNone(out['pooled']['models']['eeg']['macro_recall'])


if __name__=='__main__':unittest.main()
