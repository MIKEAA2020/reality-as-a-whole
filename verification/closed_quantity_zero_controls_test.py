import itertools
import unittest

try:
    from . import closed_quantity_zero_controls as c
except ImportError:
    import closed_quantity_zero_controls as c


class ClosedQuantityTests(unittest.TestCase):
    def test_receipt_and_nonzero_signed_countermodel(self):
        r=c.run()
        self.assertEqual(r['conserved_total'],3)
        self.assertTrue(any(x<0 for x in r['nonzero_conserved_signed_charge_before']))
        self.assertTrue(any(x>0 for x in r['nonzero_conserved_signed_charge_before']))

    def test_gauss_zero_exact_for_all_sample_edge_fields(self):
        for field in itertools.product(range(-3,4),repeat=3):
            self.assertEqual(sum(c.divergence(field)),0)

    def test_internal_transfer_preserves_any_total(self):
        for q in itertools.product(range(-2,3),repeat=3):
            for f in ((1,2,3),(-5,0,7),(0,0,0)):
                self.assertEqual(sum(c.transfer(q,f)),sum(q))

    def test_symmetry_implies_zero_invariant_state(self):
        for q in itertools.product(range(-3,4),repeat=3):
            tq=c.inversion_swap(q)
            self.assertEqual(c.inversion_swap(tq),q)
            self.assertEqual(sum(tq),-sum(q))
            if tq==q: self.assertEqual(sum(q),0)

    def test_zero_score_is_not_empty_labelled_model(self):
        r=c.run()
        self.assertEqual(r['toy_net_score'],0)
        self.assertEqual(len(r['toy_signed_labelled_occurrences']),2)

    def test_invalid_dimension(self):
        with self.assertRaises(ValueError): c.divergence((1,2))
        with self.assertRaises(ValueError): c.transfer((1,2),(1,2,3))
        with self.assertRaises(ValueError): c.inversion_swap((1,2))

if __name__ == '__main__': unittest.main()
