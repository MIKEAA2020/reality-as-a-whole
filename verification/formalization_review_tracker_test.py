"""Test conservative, hash-sensitive formalization-review accounting."""
import tempfile
import unittest
from pathlib import Path
from verification.build_formalization_review_tracker import build, digest


class FormalizationReviewTrackerTests(unittest.TestCase):
    def test_overinclusive_candidates_and_stale_review(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            (root/'a.md').write_text('example')
            (root/'b.py').write_text('pass')
            (root/'data.json').write_text('{}')
            (root/'evidence.md').write_text('selected proof')
            receipts={'a.md': {'reviewed_sha256':digest(b'example'),
                                'scope':'one claim only','evidence':['evidence.md'],
                                'evidence_sha256':{'evidence.md':digest(b'selected proof')}}}
            result=build(root,['a.md','b.py','data.json','evidence.md','a.md'],receipts)
            self.assertEqual(result['counts'],{'not_rechecked_in_this_sweep':2,
                                                'selected_claims_reviewed':1})
            self.assertEqual(len(result['records']),3)
            (root/'evidence.md').write_text('changed evidence')
            result=build(root,['a.md','b.py','evidence.md'],receipts)
            self.assertEqual(result['counts']['review_stale_evidence_changed'],1)
            (root/'evidence.md').write_text('selected proof')
            (root/'a.md').write_text('changed')
            result=build(root,['a.md','b.py','evidence.md'],receipts)
            self.assertEqual(result['counts']['review_stale_file_changed'],1)

    def test_bad_receipt_is_not_silently_accepted(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); (root/'a.md').write_text('x')
            receipt={'a.md': {'reviewed_sha256':digest(b'x'),
                              'scope':'one claim','evidence':['missing.md'],
                              'evidence_sha256':{'missing.md':digest(b'missing')}}}
            with self.assertRaises(ValueError): build(root,['a.md'],receipt)


if __name__ == '__main__':
    unittest.main()
