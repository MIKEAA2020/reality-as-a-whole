#!/usr/bin/env python3
import unittest
import numpy as np
from meeg_bounded_signal_audit import (
    PREFIX, SOURCE, first_channel_from_prefix, tar_member_prefix,
    trial_split_witness, upstream_methods,
)


class BoundedSignalTests(unittest.TestCase):
    def test_missing_tar_member_fails(self):
        with self.assertRaises(ValueError): tar_member_prefix(b'\0'*512,'missing')

    def test_untrusted_prefix_rejected(self):
        with self.assertRaises(ValueError): first_channel_from_prefix(b'not a pinned gzip')

    def test_untrusted_source_rejected(self):
        with self.assertRaises(ValueError): upstream_methods(b'not a pinned source')

    def test_witness(self):
        r=trial_split_witness()
        self.assertEqual(r['outer_trial_overlap'],0)
        self.assertEqual(r['inner_trial_overlap'],3)

    @unittest.skipUnless(PREFIX.exists() and SOURCE.exists(),'fetch pinned prefix/source')
    def test_pinned_data_and_caller(self):
        x, digest=first_channel_from_prefix(PREFIX.read_bytes())
        self.assertEqual(len(x),59900)
        self.assertEqual(digest,'9b9ffdae1cff24a9466e45755c6cd2fe5ab387cc7d664c9b89adde3b5da8fe83')
        upstream=upstream_methods(SOURCE.read_bytes())
        before=x[np.newaxis,np.newaxis,:].copy()
        result=upstream.notch_filter(before,fs=1000,Q=50)
        self.assertTrue(np.array_equal(x,result[0,0]))
        self.assertFalse(np.array_equal(x,upstream.notch_filter_per_channel(x,fs=1000,Q=50)))

if __name__=='__main__':
    unittest.main()
