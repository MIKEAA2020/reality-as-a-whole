"""Scope and conservative evidence checks for the repass index."""
import unittest
from verification.build_source_repass_tracker import ROOT,PARTIAL,build,collect

class SourceRepassTrackerTests(unittest.TestCase):
    def test_enumerates_repository_markdown_and_preserved_sources(self):
        records=build()['records'];names={r['path'] for r in records}
        self.assertEqual(names,set(collect()))
        self.assertTrue(any(x.startswith('sources/uploads/') for x in names))
        self.assertTrue(any(x.startswith('sources/external/') for x in names))
        self.assertTrue(any(x.startswith('psr-5 battery/') for x in names))
        self.assertIn('WHOLE_CHAT_MULTI_PASS_INTEGRATION_WORKBOARD.md',names)
        self.assertIn('ZERO_SOURCE_INTEGRATION_STATIONARY_SUBJECT_INCIDENCE.md',names)

    def test_partial_marks_have_evidence_and_are_conservative(self):
        records=build()['records']
        for r in records:
            for kind,stage in r['stages'].items():
                self.assertIn(stage['status'],('partial','unassessed_in_this_repass'))
                self.assertEqual(stage['status']=='partial',bool(stage['evidence']))
                for ref in stage['evidence']:self.assertTrue((ROOT/ref).is_file(),ref)
            if r['path'] not in PARTIAL:
                self.assertTrue(all(s['status']=='unassessed_in_this_repass'
                                    for s in r['stages'].values()))

if __name__=='__main__':unittest.main()
