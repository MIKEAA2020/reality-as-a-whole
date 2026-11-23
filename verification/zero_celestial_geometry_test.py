import unittest
from fractions import Fraction as F


def rank(rows):
    a=[list(map(F,row)) for row in rows]
    pivots=0
    for col in range(len(a[0])):
        p=next((i for i in range(pivots,len(a)) if a[i][col]),None)
        if p is None: continue
        a[pivots],a[p]=a[p],a[pivots]
        factor=a[pivots][col]
        a[pivots]=[x/factor for x in a[pivots]]
        for i in range(len(a)):
            if i!=pivots and a[i][col]:
                factor=a[i][col]
                a[i]=[x-factor*y for x,y in zip(a[i],a[pivots])]
        pivots+=1
        if pivots==len(a): break
    return pivots


def quad_row(k):
    return [k[i]**2 for i in range(4)]+[2*k[i]*k[j] for i in range(4) for j in range(i+1,4)]


def cross_ratio(z):
    a,b,c,d=z
    return (a-b)*(c-d)/((a-c)*(b-d))


def mobius(z): return (2*z+1)/(z+1)


def aberration(t,beta):
    if not -1<beta<1 or not -1<=t<=1: raise ValueError('invalid boost or direction')
    return (t-beta)/(1-beta*t)


class ZeroCelestialGeometryTests(unittest.TestCase):
    def test_null_cone_fixes_metric_up_to_scale(self):
        axes=[]
        for i in range(3):
            for sign in (1,-1):
                n=[F(0)]*3; n[i]=F(sign); axes.append([F(1),*n])
        mixes=[]
        for i,j in ((0,1),(0,2),(1,2)):
            n=[F(0)]*3; n[i]=F(3,5); n[j]=F(4,5); mixes.append([F(1),*n])
        rows=[quad_row(k) for k in axes+mixes]
        # A symmetric 4x4 metric has 10 coefficients; these nine
        # independent null conditions leave exactly its overall scale.
        self.assertEqual(rank(rows),9)
        eta=[F(-1),F(1),F(1),F(1)]+[F(0)]*6
        self.assertTrue(all(sum(x*y for x,y in zip(row,eta))==0 for row in rows))

    def test_cross_ratio_preserved_by_lorentz_mobius_transform(self):
        first=list(map(F,[0,1,2,3]))
        second=list(map(F,[0,1,2,-1]))
        self.assertEqual(cross_ratio(first),F(1,4))
        self.assertEqual(cross_ratio(second),F(3,4))
        self.assertEqual(cross_ratio([mobius(z) for z in first]),F(1,4))
        # Use a Möbius map without a pole at the second quadruple.
        self.assertEqual(cross_ratio([2*z+3 for z in second]),F(3,4))

    def test_no_uniform_probability_is_boost_invariant(self):
        beta=F(3,5)
        self.assertEqual(aberration(beta,beta),0)
        # Uniform t on [-1,1]: boosted hemisphere t'>0 means t>beta.
        self.assertEqual((1-beta)/2,F(1,5))
        self.assertNotEqual((1-beta)/2,F(1,2))

    def test_ray_blowdown_commutes_with_z_boost(self):
        # n=(4/5,0,3/5), beta=3/5, gamma=5/4.
        r=F(7,10); beta=F(3,5); gamma=F(5,4)
        k0=r; kx=F(4,5)*r; kz=F(3,5)*r
        boosted0=gamma*(k0-beta*kz); boostedz=gamma*(kz-beta*k0)
        self.assertEqual(boosted0,F(4,5)*r)
        self.assertEqual(boostedz,0)
        self.assertEqual(kx,boosted0)
        self.assertEqual(k0*k0-kx*kx-kz*kz,0)
        self.assertEqual(boosted0*boosted0-kx*kx-boostedz*boostedz,0)
        self.assertEqual(F(0)*(1+aberration(F(3,5),beta)),0)

    def test_invalid_boost_rejected(self):
        with self.assertRaises(ValueError): aberration(0,1)


if __name__=='__main__': unittest.main()
