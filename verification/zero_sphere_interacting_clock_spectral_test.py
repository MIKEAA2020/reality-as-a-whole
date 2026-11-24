"""Interacting detector: spectral clock data, bound modes and pointer transport.

Uses standard-library Jacobi diagonalization of Nyström matrices. Continuum
bound-state and scattering statements require the analytic arguments in the
companion report; a finite matrix does not numerically prove continuum spectra.
"""
import cmath
import math
import unittest

from verification.zero_sphere_finite_resolution_clock_instrument_test import (
    mesh,effects,apply,dot,window_kernel
)
from verification.zero_sphere_autonomous_detector_constraint_test import (
    translated,channel,p_pointer_one
)


def jacobi(matrix,tol=1e-13):
    """Real symmetric eigensystem; columns of vectors are eigenvectors."""
    n=len(matrix);a=[row[:] for row in matrix]
    vectors=[[float(i==j) for j in range(n)] for i in range(n)]
    for _ in range(30):
        if max(abs(a[i][j]) for i in range(n) for j in range(i+1,n))<tol:
            break
        for i in range(n-1):
            for j in range(i+1,n):
                aij=a[i][j]
                if abs(aij)<tol/n: continue
                tau=(a[j][j]-a[i][i])/(2*aij)
                t=(1 if tau>=0 else -1)/(abs(tau)+math.sqrt(1+tau*tau))
                c=1/math.sqrt(1+t*t);s=t*c
                aii,ajj=a[i][i],a[j][j]
                a[i][i]=aii-t*aij;a[j][j]=ajj+t*aij;a[i][j]=a[j][i]=0.0
                for k in range(n):
                    if k!=i and k!=j:
                        aki,akj=a[k][i],a[k][j]
                        a[k][i]=a[i][k]=c*aki-s*akj
                        a[k][j]=a[j][k]=s*aki+c*akj
                    vi,vj=vectors[k][i],vectors[k][j]
                    vectors[k][i]=c*vi-s*vj;vectors[k][j]=s*vi+c*vj
    else:
        raise ArithmeticError('Jacobi eigensystem failed to converge')
    order=sorted(range(n),key=lambda i:a[i][i])
    return [a[i][i] for i in order],[[vectors[k][i] for i in order] for k in range(n)]


def build(n):
    p,f,dp=mesh(n);E=effects(p,dp)[0][0]
    systems={}
    for d in (1,-1):
        matrix=[[(p[i]**2/6 if i==j else 0)-.8*d*E[i][j]
                for j in range(n)] for i in range(n)]
        values,vectors=jacobi(matrix)
        systems[d]=(matrix,values,vectors)
    return p,translated(f,p),E,systems


def transform(V,vec):
    return [sum(V[i][j]*vec[i] for i in range(len(vec))) for j in range(len(vec))]


def untransform(V,vec):
    return [sum(V[i][j]*vec[j] for j in range(len(vec))) for i in range(len(vec))]


def overlap_matrix(Vplus,Vminus):
    n=len(Vplus)
    return [[sum(Vplus[i][j]*Vminus[i][k] for i in range(n))
             for k in range(n)] for j in range(n)]


def pointer_spectral(f,systems,t,naive=False):
    _,ep,Vp=systems[1];_,em,Vm=systems[-1]
    ap,am=transform(Vp,f),transform(Vm,f)
    S=overlap_matrix(Vp,Vm) if not naive else None
    n=len(f);total=0j
    for h in (0,1):
        x=[ap[j]*cmath.exp(1j*math.sqrt(ep[j]-2*h)*t) for j in range(n)]
        y=[am[j]*cmath.exp(1j*math.sqrt(em[j]-2*h)*t) for j in range(n)]
        if naive:
            total+=dot(x,y)
        else:
            total+=sum(x[j].conjugate()*S[j][k]*y[k]
                       for j in range(n) for k in range(n))
    return .5-.25*total.real


def variational_upper(eps,delta,lam,lower):
    """Upper bound on unnormalised signed edge Rayleigh numerator."""
    if lower: b,c=2,2+eps/6
    else: b,c=(14-eps)/6,14/6
    k=window_kernel(eps)  # kernel decreases positively on 0..eps for eps<pi/2
    kinetic=math.log1p(b*eps/delta)/b
    overlap=math.log1p(c*eps/delta)/c
    return kinetic-2*lam*k*overlap**2


class InteractingSpectralClockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p,cls.f,cls.E,cls.systems=build(40)
        cls.p80,cls.f80,cls.E80,cls.systems80=build(80)

    def test_window_effect_is_trace_class_by_factorization(self):
        # E=A†A for A=M_{sqrt(g)} Fourier band-extension;
        # ||A||_HS² = band_length * integral(g)/(2π)=2/π.
        tr=sum(self.E[i][i] for i in range(len(self.E)))
        self.assertAlmostEqual(tr,2/math.pi,places=12)
        for p in (-7,-6.75,-6.5,-6.25,-6):
            for q in (-7,-6.75,-6.5,-6.25,-6):
                self.assertLessEqual(abs(window_kernel(p-q)),2/math.pi)

    def test_analytic_variational_witness_at_both_band_edges(self):
        for lower in (True,False):
            self.assertLess(variational_upper(.25,1e-4,.4,lower),0)
        # The companion proof shows the negative log-squared term eventually
        # dominates for every lambda>0, not only the tested parameter.

    def test_discrete_edge_states_refine(self):
        for data in (self.systems,self.systems80):
            ep=data[1][1];em=data[-1][1]
            self.assertLess(ep[0],6)
            self.assertGreater(em[-1],49/6)
            self.assertEqual(sum(x<6 for x in ep),1)
            self.assertEqual(sum(x>49/6 for x in em),1)
        self.assertAlmostEqual(self.systems80[1][1][0],5.977952126765304,places=10)
        self.assertAlmostEqual(self.systems80[-1][1][-1],8.179675297989524,places=10)
        # Count and numbers are finite discretization results only.

    def test_edge_levels_and_bound_weights_at_higher_resolution(self):
        p,f,E,data=build(160)
        low=data[1][1][0];high=data[-1][1][-1]
        self.assertAlmostEqual(low,5.977197914562014,places=10)
        self.assertAlmostEqual(high,8.181038154899736,places=10)
        weights=[]
        for d,index in ((1,0),(-1,-1)):
            V=data[d][2];v=[V[i][index] for i in range(len(p))]
            weights.append(abs(dot(v,f))**2)
        self.assertAlmostEqual(weights[0],.0010377661211289338,places=10)
        self.assertAlmostEqual(weights[1],.0006727996213783631,places=10)
        self.assertLess(sum(weights)/2,.00086)
        self.assertGreater(sum(weights)/2,.00085)

    def test_eigenvectors_orthonormal_and_have_small_residual(self):
        for matrix,values,V in self.systems.values():
            n=len(values)
            for j in (0,1,n//2,n-2,n-1):
                v=[V[i][j] for i in range(n)]
                self.assertAlmostEqual(dot(v,v).real,1,places=12)
                residual=[x-values[j]*y for x,y in zip(apply(matrix,v),v)]
                self.assertLess(dot(residual,residual).real,1e-22)
            for j,k in ((0,1),(0,n-1),(n//2,n-1)):
                self.assertAlmostEqual(sum(V[i][j]*V[i][k] for i in range(n)),0,places=12)

    def test_spectral_state_map_is_unitary_for_complex_states(self):
        for _,values,V in self.systems.values():
            v=transform(V,self.f);back=untransform(V,v)
            self.assertAlmostEqual(dot(v,v).real,dot(self.f,self.f).real,places=11)
            self.assertLess(sum(abs(x-y)**2 for x,y in zip(back,self.f)),1e-23)
            for h in (0,1):self.assertGreater(min(values)-2*h,0)

    def test_spectral_pointer_preserves_same_joint_prediction(self):
        for t in (0,40,80,100):
            direct=p_pointer_one(channel(self.p,self.E,self.f,t))
            full=pointer_spectral(self.f,self.systems,t)
            self.assertAlmostEqual(full,direct,places=11)
        # Failing to transport the pointer operator mispredicts even at zero.
        self.assertAlmostEqual(pointer_spectral(self.f,self.systems,0),0,places=11)
        self.assertGreater(pointer_spectral(self.f,self.systems,0,naive=True),.1)

    def test_pointer_overlap_matrix_and_phase_gauge(self):
        Vp=self.systems[1][2];Vm=self.systems[-1][2]
        S=overlap_matrix(Vp,Vm);n=len(S)
        for i,j in ((0,0),(0,n-1),(n//2,n//2)):
            v=sum(S[i][k]*S[j][k] for k in range(n))
            self.assertAlmostEqual(v,float(i==j),places=11)
        self.assertLess(abs(S[0][-1]),.06)
        self.assertGreater(1-abs(S[0][-1])**2,.99)
        # Eigenvector phase conventions are arbitrary; W A W† must respect
        # their simultaneous transformation, unlike an imposed identity map.
        orig=pointer_spectral(self.f,self.systems,100)
        changed={d:(mat,vals,[row[:] for row in V])
                 for d,(mat,vals,V) in self.systems.items()}
        mat,vals,V=changed[1]
        for row in V:row[0]=-row[0]
        self.assertAlmostEqual(pointer_spectral(self.f,changed,100),orig,places=11)
        self.assertGreater(abs(pointer_spectral(self.f,changed,100,True)-
                               pointer_spectral(self.f,self.systems,100,True)),1e-5)

    def test_bound_overlap_of_incident_preparation(self):
        result=[]
        for d,index in ((1,0),(-1,-1)):
            V=self.systems80[d][2]
            v=[V[i][index] for i in range(len(self.p80))]
            result.append(abs(dot(v,self.f80))**2)
        self.assertAlmostEqual(result[0],.0010737648778509422,places=10)
        self.assertAlmostEqual(result[1],.0007262370342719343,places=10)
        self.assertGreater(sum(result)/2,0)

    def test_bound_state_is_stationary_not_a_monotone_clock(self):
        _,values,V=self.systems[1]
        bound=[V[i][0] for i in range(len(self.p))]
        e=dot(bound,apply(self.E,bound)).real
        self.assertGreater(e,0)
        for t in (0,10,100):
            phase=cmath.exp(1j*math.sqrt(values[0])*t)
            evolved=[phase*x for x in bound]
            self.assertAlmostEqual(dot(evolved,apply(self.E,evolved)).real,e,places=12)
        # The general no-go for normalized covariant R-valued POVMs in a
        # stationary eigenstate is an analytic probability-measure argument.

if __name__=='__main__': unittest.main()
