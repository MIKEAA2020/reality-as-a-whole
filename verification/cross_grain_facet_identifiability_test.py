import unittest
from fractions import Fraction as F
from itertools import product
from cross_grain_facet_identifiability import distribution, binary, graded_code, oracle, factor

class CrossGrainFacetTests(unittest.TestCase):
    def setUp(self):self.d=distribution()
    def test_distribution(self):
        self.assertEqual(sum(self.d.values()),1)
        self.assertEqual(len(self.d),8)
        self.assertEqual(self.d[0,0,0],F(45,128))
    def test_scalar_loss(self):
        self.assertEqual(oracle(self.d,binary,0),F(1,4))
        self.assertEqual(oracle(self.d,graded_code,0),F(3,16))
        for code in (binary,graded_code):
            self.assertFalse(factor(self.d,code,lambda x:x[0]))
            self.assertFalse(factor(self.d,code,lambda x:x[2]))
    def test_structured_codes(self):
        for code,n in ((binary,5),(graded_code,8)):
            structured=lambda x:(code(x),x[0],x[2])
            self.assertEqual(len({structured(x) for x in self.d}),n)
            self.assertTrue(factor(self.d,structured,code))
            self.assertTrue(factor(self.d,structured,lambda x:x[0]))
            self.assertTrue(factor(self.d,structured,lambda x:x[2]))
    def test_symmetry(self):
        for l,m,r in product((0,1),repeat=3):
            self.assertEqual(self.d[l,m,r],self.d[r,m,l])
            self.assertEqual(graded_code((l,m,r)),graded_code((r,m,l)))
    def test_oracle_sharp_on_simple_case(self):
        d={(0,0,0):F(2,3),(1,0,0):F(1,3)}
        self.assertEqual(oracle(d,lambda x:0,0),F(1,3))
        self.assertEqual(oracle(d,lambda x:x[0],0),0)
if __name__=='__main__':unittest.main()
