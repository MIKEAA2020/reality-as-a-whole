import unittest


def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def dagger(a): return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]


def det(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def hermitian(t,x,y,z): return [[t+z,x-1j*y],[x+1j*y,t-z]]


def spinor_ray(a,b): return [[a*a.conjugate(),a*b.conjugate()],[b*a.conjugate(),b*b.conjugate()]]


def scale(c,A): return [[c*value for value in row] for row in A]


def trans(M,A): return matmul(matmul(M,A),dagger(M))


class ProjectiveSphereLorentzTests(unittest.TestCase):
    def assertMatrixAlmostEqual(self,A,B):
        for r in range(2):
            for c in range(2): self.assertAlmostEqual(A[r][c],B[r][c],places=12)

    def test_hermitian_determinant_is_lorentz_quadratic_form(self):
        t,x,y,z=2,1,.5,.25
        self.assertAlmostEqual(det(hermitian(t,x,y,z)),t*t-x*x-y*y-z*z)

    def test_projective_direction_is_null_and_phase_independent(self):
        a,b=1+2j,3-1j
        A=spinor_ray(a,b)
        self.assertAlmostEqual(det(A),0)
        self.assertMatrixAlmostEqual(spinor_ray(1j*a,1j*b),A)
        self.assertMatrixAlmostEqual(spinor_ray(2*a,2*b),scale(4,A))

    def test_sl2c_transformation_preserves_lorentz_form_and_future_cone(self):
        M=[[2,0],[0,.5]]
        A=hermitian(2,1,.5,.25)
        B=trans(M,A)
        self.assertAlmostEqual(det(M),1)
        self.assertAlmostEqual(det(A),det(B))
        self.assertGreater(B[0][0].real,0)
        # cosh(ln 4)=17/8 and sinh(ln 4)=15/8
        self.assertAlmostEqual((B[0][0]+B[1][1]).real/2,(17*2+15*.25)/8)
        self.assertAlmostEqual((B[0][0]-B[1][1]).real/2,(15*2+17*.25)/8)

    def test_different_lifts_same_projective_map_give_conformal_scaling(self):
        M=[[1,1],[0,1]]
        A=hermitian(2,1,0,0)
        c=2+1j
        B=trans(M,A)
        B2=trans(scale(c,M),A)
        self.assertMatrixAlmostEqual(B2,scale(abs(c)**2,B))
        self.assertAlmostEqual(det(B2),abs(c)**4*det(B))

    def test_two_different_ray_pairs_make_same_timelike_state(self):
        v1=spinor_ray(1+0j,0j); v2=spinor_ray(0j,1+0j)
        w1=spinor_ray(2**-.5+0j,2**-.5+0j)
        w2=spinor_ray(2**-.5+0j,-2**-.5+0j)
        add=lambda A,B:[[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
        self.assertMatrixAlmostEqual(add(v1,v2),add(w1,w2))
        self.assertAlmostEqual(det(add(v1,v2)),1)
        self.assertNotEqual(v1,w1)

    def test_zero_matrix_has_no_projective_spinor_by_itself(self):
        self.assertMatrixAlmostEqual(spinor_ray(0j,0j),[[0,0],[0,0]])
        self.assertAlmostEqual(det(spinor_ray(0j,0j)),0)
        # CP1 is defined from nonzero spinors only: (0,0) has no ray.


if __name__=='__main__': unittest.main()
