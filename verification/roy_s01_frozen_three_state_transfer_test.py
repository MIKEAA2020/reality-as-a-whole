#!/usr/bin/env python3
"""Synthetic validation of participant-held-out plumbing and fixed model."""
import hashlib
from pathlib import Path
import tempfile
import unittest
from roy_s01_frozen_three_state_transfer import RIVALRY, dropbox_hash, load_frozen_model, evaluate


def row(label, feature, slot=0, bad=False):
    return {'label':label, 'feature':feature, 'slot':slot, 'bad':bad}


class FrozenTransferTest(unittest.TestCase):
    def test_frozen_model_and_tampered_file(self):
        path = Path(__file__).with_name('roy_s09_three_state_pilot.json')
        model = load_frozen_model(path)
        self.assertEqual(model['majority'], 2)
        self.assertEqual(set(model['means']), {1,2,3})
        with tempfile.TemporaryDirectory(dir='.arena') as td:
            tampered = Path(td)/'model.json'
            tampered.write_bytes(path.read_bytes()+b' ')
            with self.assertRaises(ValueError): load_frozen_model(tampered)

    def test_dropbox_hash_independent_two_block_calculation(self):
        with tempfile.TemporaryDirectory(dir='.arena') as td:
            path = Path(td)/'sample'
            first = b'a'*(4*1024*1024)
            second = b'b'*19
            path.write_bytes(first+second)
            expected = hashlib.sha256(hashlib.sha256(first).digest()+hashlib.sha256(second).digest()).hexdigest()
            self.assertEqual(dropbox_hash(path), expected)

    def test_six_scans_pool_counts_and_model_unchanged(self):
        model = load_frozen_model(Path(__file__).with_name('roy_s09_three_state_pilot.json'))
        before = repr(model)
        samples = {s: [row(1,model['means'][1]),row(2,model['means'][2]),
                       row(3,model['means'][3]),row(0,model['means'][3]),row(3,None,bad=True)] for s in RIVALRY}
        summary = evaluate(samples, model)
        pooled = summary['pooled']
        self.assertEqual((pooled['total_windows'],pooled['report_unresolved_windows'],
                          pooled['artifact_windows'], pooled['labeled_clean_windows']), (30,6,6,18))
        self.assertEqual(pooled['models']['eeg']['confusion_true_rows_pred_columns'],
                         [[6,0,0],[0,6,0],[0,0,6]])
        self.assertEqual(pooled['models']['eeg']['full_grid_correct_fraction'], 18/30)
        self.assertEqual(before,repr(model))
        with self.assertRaises(ValueError): evaluate({1:samples[1]},model)


if __name__ == '__main__': unittest.main()
