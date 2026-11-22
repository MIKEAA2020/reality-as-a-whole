import unittest
from fractions import Fraction as F
from afterimage_cone_contrast_geometry import calculate

class GeometryTests(unittest.TestCase):
    def test_example(self):
        a,b,e,p,q,det = calculate((F(1),)*3, (F(1,2),F(1,4),F(0)))
        self.assertEqual(p, (F(-1,2), F(-1,4)))
        self.assertEqual(q, (F(-1,3), F(-1,5)))
        self.assertEqual(det, F(1,60))
        self.assertEqual(e, (F(1,6), F(1,20), F(0)))

    def test_error_formula_and_scaling(self):
        d = (F(1,2), F(-1,3), F(0))
        for scale in (F(1), F(1,2), F(1,10)):
            ds = tuple(scale*x for x in d)
            _,_,err,_,_,_ = calculate((F(2), F(3), F(4)), ds)
            self.assertEqual(err, tuple(x*x/(1+x) for x in ds))

    def test_collinear_common_fractional_increment(self):
        *_, det = calculate((F(1),)*3, (F(1,3), F(1,3), F(0)))
        self.assertEqual(det, 0)

    def test_positivity(self):
        with self.assertRaises(ValueError):
            calculate((F(1),)*3, (F(-1), F(0), F(0)))
        with self.assertRaises(ValueError):
            calculate((F(0),F(1),F(1)), (F(0),)*3)

if __name__ == '__main__':
    unittest.main()
