#!/usr/bin/env python3
import math
import unittest
from types import SimpleNamespace
import pandas as pd
from daly_comparator_metadata_audit import UPSTREAM, audit_rows, make_parser, same


class EventAuditTests(unittest.TestCase):
    def test_boundaries_and_coincident_codes(self):
        events=[(0,788,20),(0,901,20), (12,800,20), (12,904,20), (12,836,20),
                (19.9,801,20),(19.9,909,20),(19.9,833,20),
                (20,802,20), (30,788,20), (35,800,20)]
        c,o=audit_rows(events)
        self.assertEqual(c['music_starts'],2)
        self.assertEqual(c['question_within_12s_including_start'],1)
        self.assertEqual(c['question_within_20s_including_start'],2)
        self.assertEqual(c['answer_or_response_within_12s_including_start'],1)
        self.assertEqual(c['answer_or_response_within_12s_strictly_after_start'],0)
        self.assertEqual(c['one_q_one_answer_one_response_timestamps'],2)
        self.assertEqual(c['triples_equal'],1)
        self.assertEqual(c['triples_unequal'],1)
        self.assertEqual(c['intervals_with_unequal_triple'],1)
        self.assertEqual(o['first_question_after_start'],[12,5])

    def test_duplicate_codes_are_collapsed(self):
        ev=[(0,788,20),(13,800,20),(13,800,20),(13,901,20),(13,833,20)]
        c,_=audit_rows(ev)
        self.assertEqual(c['triples_equal'],1)
        self.assertEqual(c['one_q_one_answer_one_response_timestamps'],1)

    @unittest.skipUnless(UPSTREAM.exists(), 'pinned upstream source not fetched')
    def test_upstream_equal_timestamp_reordering_can_change_answer(self):
        env = make_parser()
        parsed = []
        for order in ((800,904,836),(836,904,800)):
            rows = [(0,788),(0,301)] + [(16.5,c) for c in order] + [(18,801),(18,901),(25,802),(25,903)]
            frame = pd.DataFrame(rows, columns=['onset','trial_type'])
            frame['duration'] = 20
            env['pd'] = SimpleNamespace(read_csv=lambda *a, **kw: frame.copy(),
                                        to_numeric=pd.to_numeric,concat=pd.concat)
            parsed.append(env['parse_events']('synthetic','1','2')[0].pleasantness)
        self.assertEqual(parsed[0],4.0)
        self.assertTrue(math.isnan(parsed[1]))

    def test_nan_comparison(self):
        self.assertTrue(same(math.nan,math.nan))
        self.assertFalse(same(math.nan,1.0))
        self.assertFalse(same(1.0,2.0))

if __name__=='__main__':
    unittest.main()
