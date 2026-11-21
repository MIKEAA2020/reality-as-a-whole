import csv
import io
import unittest
from paingen_partial_run_salvage import recover

FIELDS = ['onset', 'duration', 'trial_type', 'int_rating', 'unp_rating', 'level', 'response_time']


def tsv(types, *, onset=None, bad_rating=False, bad_rt=False):
    out = io.StringIO(newline='')
    w = csv.DictWriter(out, fieldnames=FIELDS, delimiter='\t', lineterminator='\n')
    w.writeheader()
    for n, name in enumerate(types):
        row = dict(onset=str(onset[n] if onset else n), duration='1', trial_type=name,
                   int_rating='.2', unp_rating='.3', level='3', response_time='1')
        if name == 'int_rating' and bad_rating: row['int_rating'] = '.8'
        if name == 'int_rating' and bad_rt: row['response_time'] = 'n/a'
        w.writerow(row)
    return out.getvalue().encode()


class PartialRunTests(unittest.TestCase):
    def test_whole_group_and_orphan(self):
        valid, counts = recover(tsv(['orphan', 'warning_cue', 'press', 'unp_rating', 'int_rating']))
        self.assertEqual(len(valid), 1)
        self.assertEqual(counts['orphan_rows'], 1)

    def test_malformed_group_does_not_yield_internal_subsequence(self):
        valid, counts = recover(tsv(['warning_cue', 'press', 'int_rating', 'unp_rating', 'extra',
                                      'warning_cue', 'press', 'int_rating', 'unp_rating']))
        self.assertEqual(len(valid), 1)
        self.assertEqual(counts['group_grammar'], 1)

    def test_invalid_rating_and_missing_rt_skipped(self):
        for kwargs, reason in (({'bad_rating': True}, 'group_ratings'), ({'bad_rt': True}, 'group_rt')):
            valid, counts = recover(tsv(['warning_cue', 'press', 'int_rating', 'unp_rating'], **kwargs))
            self.assertEqual(valid, [])
            self.assertEqual(counts[reason], 1)

    def test_tied_onset_and_missing_schema_stop_file(self):
        valid, counts = recover(tsv(['warning_cue', 'press', 'int_rating', 'unp_rating'], onset=[0, 1, 2, 2]))
        self.assertEqual(valid, [])
        self.assertEqual(counts['file_tied_onsets'], 1)
        valid, counts = recover(b'onset\ttrial_type\n0\twarning_cue\n')
        self.assertEqual(valid, [])
        self.assertEqual(counts['file_schema'], 1)

    def test_onset_sort_recovers_event_order(self):
        valid, counts = recover(tsv(['warning_cue', 'press', 'unp_rating', 'int_rating'], onset=[0, 1, 3, 2]))
        self.assertEqual(len(valid), 1)
        self.assertEqual(valid[0][2]['trial_type'], 'int_rating')


if __name__ == '__main__':
    unittest.main()
