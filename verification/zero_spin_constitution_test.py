"""Zero total spin as a conditional quantum-constitution construction.

No claim that spin zero is global energy or experience, that qubits are
subjects, or that the chosen Hilbert space and constraints follow from zero.
"""
from fractions import Fraction as F
import unittest


def eye(n): return [[complex(i==j) for j in range(n)] for i in range(n)]
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(x,a): return [[x*y for y in row] for row in a]
def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]
def mv(a,v): return [sum(x*y for x,y in zip(row,v)) for row in a]
def kron(a,b):
    return [[a[i//len(b)][j//len(b[0])]*b[i%len(b)][j%len(b[0])]
             for j in range(len(a[0])*len(b[0]))]
            for i in range(len(a)*len(b))]
def inner(a,b): return sum(x.conjugate()*y for x,y in zip(a,b))
def close(test,a,b):
    for r,s in zip(a,b):
        for x,y in zip(r,s): test.assertAlmostEqual(abs(x-y),0)


def rank(matrix):
    a=[list(map(complex,row)) for row in matrix]
    n=len(a[0]); r=0
    for c in range(n):
        pivot=next((i for i in range(r,len(a)) if abs(a[i][c])>1e-10),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        d=a[r][c]; a[r]=[x/d for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                fac=a[i][c]; a[i]=[x-fac*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==len(a): break
    return r


I=eye(2)
X=[[0,1],[1,0]]
Y=[[0,-1j],[1j,0]]
Z=[[1,0],[0,-1]]
T=[add(kron(s,I),kron(I,s)) for s in (X,Y,Z)]
SINGLET=[0,1,-1,0] # unnormalized for exact nullspace checks


def tensor_op(op,site,n):
    a=[[1]]
    for i in range(n): a=kron(a,op if i==site else I)
    return a


def four_singlet_pairings():
    a=[0j]*16; b=[0j]*16
    for idx,val in ((5,F(1,2)),(6,F(-1,2)),(9,F(-1,2)),(10,F(1,2))): a[idx]=complex(val)
    for idx,val in ((3,F(1,2)),(6,F(-1,2)),(9,F(-1,2)),(12,F(1,2))): b[idx]=complex(val)
    return a,b


def pair_singlet_projector(i,j,n=4):
    out=eye(2**n)
    for op in (X,Y,Z):
        out=add(out,scale(-1,mm(tensor_op(op,i,n),tensor_op(op,j,n))))
    return scale(F(1,4),out)


def total_spin(op,n):
    out=[[0j]*(2**n) for _ in range(2**n)]
    for i in range(n): out=add(out,tensor_op(op,i,n))
    return out


class ZeroSpinConstitutionTests(unittest.TestCase):
    def test_one_axis_zero_does_not_select_unique_state(self):
        self.assertEqual(rank(T[2]),2)
        self.assertEqual(4-rank(T[2]),2)
        self.assertEqual(mv(T[2],SINGLET),[0]*4)

    def test_two_nonparallel_axes_fix_unique_two_spin_state(self):
        self.assertEqual(4-rank(T[0]+T[2]),1) # concatenate rows
        for t in T: self.assertEqual(mv(t,SINGLET),[0]*4)

    def test_zero_positive_operator_has_unique_singlet_kernel(self):
        h=[[0j]*4 for _ in range(4)]
        for t in T: h=add(h,scale(F(1,8),mm(t,t)))
        close(self,mm(h,h),h)
        self.assertAlmostEqual(sum(h[i][i].real for i in range(4)),3)
        self.assertEqual(4-rank(h),1)
        self.assertEqual(mv(h,SINGLET),[0]*4)
        # Projector positivity follows from h=h†=h².

    def test_matched_spin_measurements_have_opposite_outcomes(self):
        import math
        axes=((1,0,0),(0,1,0),(0,0,1),
              (1/math.sqrt(3),1/math.sqrt(3),1/math.sqrt(3)))
        psi=[x/(2**.5) for x in SINGLET]
        for nx,ny,nz in axes:
            total=add(add(scale(nx,T[0]),scale(ny,T[1])),scale(nz,T[2]))
            self.assertAlmostEqual(inner(mv(total,psi),mv(total,psi)).real,0)
            # This entails opposite matched sharp outcomes if that measurement
            # is performed, not that outcomes are experiences or selected here.

    def test_sharp_local_spin_does_not_preserve_strict_singlet_sector(self):
        # The rank-one singlet projector annihilates projected local spin.
        psi=[x/(2**.5) for x in SINGLET]
        P=[[x*y.conjugate() for y in psi] for x in psi]
        local=kron(Z,I)
        close(self,mm(mm(P,local),P),[[0j]*4 for _ in range(4)])
        # A matched z outcome |01> retains T_z=0 but not T_x=0.
        outcome=[0,1,0,0]
        self.assertEqual(mv(T[2],outcome),[0]*4)
        self.assertNotEqual(mv(T[0],outcome),[0]*4)

    def test_local_reduced_density_is_maximally_mixed(self):
        # ρ_A[a,c]=Σ_b ψ_ab ψ*_cb, using the normalized singlet.
        psi=[x/(2**.5) for x in SINGLET]
        rho=[[sum(psi[2*a+b]*psi[2*c+b].conjugate() for b in range(2))
              for c in range(2)] for a in range(2)]
        close(self,rho,scale(.5,I))

    def test_local_operator_zero_for_all_states_forces_constants(self):
        # Arbitrary traceless local Z cannot sum with a disjoint B operator
        # to zero as an operator: partial trace over B gives 2 Z plus a scalar I.
        a=kron(Z,I)
        for c in (-3,-1,0,1,3):
            b=kron(I,scale(c,I))
            self.assertTrue(any(abs(x)>0 for row in add(a,b) for x in row))
        # General proof by partial trace is in the report.

    def test_four_spin_zero_sector_is_not_unique(self):
        a,b=four_singlet_pairings()
        self.assertAlmostEqual(inner(a,a).real,1)
        self.assertAlmostEqual(inner(b,b).real,1)
        self.assertAlmostEqual(inner(a,b).real,.5)
        for op in (X,Y,Z):
            t=total_spin(op,4)
            self.assertTrue(all(abs(x)<1e-10 for x in mv(t,a)))
            self.assertTrue(all(abs(x)<1e-10 for x in mv(t,b)))
        # Complete zero sector has rank two (kernel of positive sum of squares).
        h=[[0j]*16 for _ in range(16)]
        for op in (X,Y,Z):
            t=total_spin(op,4); h=add(h,mm(t,t))
        self.assertEqual(16-rank(h),2)

    def test_four_spin_zero_sector_is_a_relational_qubit(self):
        import math
        a,b=four_singlet_pairings()
        c=[(2*y-x)/math.sqrt(3) for x,y in zip(a,b)]
        self.assertAlmostEqual(inner(a,c).real,0)
        self.assertAlmostEqual(inner(c,c).real,1)
        for op in (X,Y,Z):
            self.assertTrue(all(abs(x)<1e-10 for x in mv(total_spin(op,4),c)))
        p12=pair_singlet_projector(0,1)
        p13=pair_singlet_projector(0,2)
        for op in (X,Y,Z):
            total=total_spin(op,4)
            for p in (p12,p13): close(self,mm(total,p),mm(p,total))
        basis=(a,c)
        matrix12=[[inner(x,mv(p12,y)) for y in basis] for x in basis]
        matrix13=[[inner(x,mv(p13,y)) for y in basis] for x in basis]
        close(self,matrix12,[[1,0],[0,0]])
        close(self,matrix13,[[.25,math.sqrt(3)/4],[math.sqrt(3)/4,.75]])
        self.assertNotAlmostEqual(abs(matrix13[0][1]),0)
        # A relative complex phase is an observable relational distinction.
        state=[(x+1j*y)/math.sqrt(2) for x,y in zip(a,c)]
        comm=scale(1j,add(mm(p12,p13),scale(-1,mm(p13,p12))))
        self.assertAlmostEqual(inner(state,mv(comm,state)).real,-math.sqrt(3)/4)
        for op in (X,Y,Z):
            self.assertTrue(all(abs(x)<1e-10 for x in mv(total_spin(op,4),state)))

    def test_bell_pair_correlation_has_zero_total_but_nonzero_local_variance(self):
        psi=[x/(2**.5) for x in SINGLET]
        local=kron(Z,I); total=T[2]
        self.assertAlmostEqual(inner(psi,mv(total,psi)).real,0)
        self.assertAlmostEqual(inner(mv(total,psi),mv(total,psi)).real,0)
        self.assertAlmostEqual(inner(psi,mv(local,psi)).real,0)
        self.assertAlmostEqual(inner(mv(local,psi),mv(local,psi)).real,1)


if __name__ == '__main__': unittest.main()
