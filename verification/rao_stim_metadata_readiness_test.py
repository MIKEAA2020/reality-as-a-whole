import io
import json
import tarfile
import unittest
from unittest.mock import patch
import rao_stim_metadata_readiness as audit
from rao_stim_metadata_readiness import blob_sha, numeric_class, timing_class, inspect


def fixture(label='recording_stim', corrupt_blob=False):
    files = {'dataset_description.json': b'{}'}
    for task in ('stim', 'sps'):
        files['task-' + task + '_events.json'] = json.dumps({'trial_type': {'Levels': {
            'recording_' + task: 'whole recording; timing not annotated'}}}).encode()
        key = 'sub-test/ieeg/sub-test_task-' + task + '_run-01'
        event_label = label if task == 'stim' else 'recording_sps'
        files[key + '_events.tsv'] = ('onset\tduration\ttrial_type\n0\t3\t' + event_label + '\n').encode()
        files[key + '_ieeg.json'] = json.dumps({'TaskName': task}).encode()
    tree = {'sha': audit.COMMIT, 'truncated': False, 'tree': [
        {'path': p, 'type': 'blob', 'size': len(v), 'sha': blob_sha(v)} for p, v in files.items()]}
    if corrupt_blob:
        tree['tree'][0]['sha'] = '0' * 40
    tree_bytes = json.dumps(tree).encode()
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode='w:gz') as t:
        for path, content in files.items():
            info = tarfile.TarInfo('root/' + path)
            info.size = len(content)
            t.addfile(info, io.BytesIO(content))
    archive = buf.getvalue()
    with patch.object(audit, 'ARCHIVE_SHA', audit.sha256(archive)), \
         patch.object(audit, 'TREE_SHA', audit.sha256(tree_bytes)), \
         patch.object(audit, 'TARGET_COUNT', len(files)):
        return inspect(archive, tree_bytes)


class MetadataReadinessTests(unittest.TestCase):
    def test_git_blob(self):
        self.assertEqual(blob_sha(b'hello\n'), 'ce013625030ba8dba906f756967f9e9ca394464a')

    def test_numeric_class(self):
        self.assertEqual([numeric_class(x) for x in ('0', '1.2', '', 'n/a', '-1', 'nan', 'bad')],
                         ['valid', 'valid', 'missing', 'missing', 'invalid', 'invalid', 'invalid'])

    def test_known_recording_span_is_not_stimulus_onset(self):
        levels = {'recording_stim': 'one row spanning the whole recording (stimulation onset/offset not annotated in the release)'}
        self.assertEqual(timing_class('stim', levels, ['recording_stim'], {'TaskName': 'stim'}),
                         'not_annotated_recording_span_only')
        self.assertEqual(timing_class('stim', levels, ['recording_stim'], {'TaskName': 'sps'}), 'ambiguous')
        self.assertEqual(timing_class('stim', levels, ['stimulation'], {'TaskName': 'stim'}), 'ambiguous')

    def test_aggregate_join_is_not_event_join(self):
        result = fixture()
        self.assertEqual(result['people_with_both_tasks'], 1)
        self.assertEqual(result['tasks']['stim']['rows'], 1)
        self.assertEqual(result['tasks']['stim']['runs_with_documented_stimulus_or_report_event'], 0)
        self.assertEqual(result['tasks']['sps']['timing_documentation']['not_annotated_recording_span_only'], 1)

    def test_unknown_label_stops(self):
        with self.assertRaisesRegex(ValueError, 'undocumented event label'):
            fixture(label='unknown')

    def test_blob_mismatch_stops_even_with_matching_outer_digests(self):
        with self.assertRaisesRegex(ValueError, 'blob verification'):
            fixture(corrupt_blob=True)

    def test_wrong_source_fails_closed(self):
        with self.assertRaises(ValueError):
            inspect(b'not archive', b'not tree')


if __name__ == '__main__':
    unittest.main()
