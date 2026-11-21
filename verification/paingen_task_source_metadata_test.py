import hashlib
import unittest
from unittest.mock import patch
import paingen_task_source_metadata as audit


def sha(blob):
    return hashlib.sha1(b'blob ' + str(len(blob)).encode() + b'\0' + blob).hexdigest()


class SourceMetadataTests(unittest.TestCase):
    def setUp(self):
        self.blob = b'prespecified source content\n'
        self.blobs = {'example.m': (sha(self.blob), len(self.blob))}
        self.fragments = {'example.m': ('prespecified source',)}
        self.tree = {'sha': audit.COMMIT, 'truncated': False, 'tree': [
            {'path': audit.PREFIX+'example.m', 'type': 'blob', 'sha': sha(self.blob), 'size': len(self.blob)}]}

    def run_verify(self, tree=None, blob=None):
        with patch.object(audit, 'BLOBS', self.blobs), patch.object(audit, 'FRAGMENTS', self.fragments):
            return audit.verify(self.tree if tree is None else tree, {'example.m': self.blob if blob is None else blob})

    def test_good_blob(self):
        self.assertEqual(self.run_verify()['verified_source_files']['example.m']['git_blob_sha1'], sha(self.blob))

    def test_bad_blob_and_truncated_tree_fail(self):
        with self.assertRaises(ValueError):
            self.run_verify(blob=b'not the source')
        with self.assertRaises(ValueError):
            self.run_verify(tree={**self.tree, 'truncated': True})

    def test_duplicate_and_wrong_commit_fail(self):
        with self.assertRaises(ValueError):
            self.run_verify(tree={**self.tree, 'tree': self.tree['tree']*2})
        with self.assertRaises(ValueError):
            self.run_verify(tree={**self.tree, 'sha': 'wrong'})


if __name__ == '__main__':
    unittest.main()
