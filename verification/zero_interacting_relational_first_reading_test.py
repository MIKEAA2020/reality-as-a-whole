"""Sequential geometry-window and pointer instrument in interacting FLRW.

An operational, discrete protocol on the chosen physical Hilbert sector,
not a local autonomous apparatus or exact alpha-time reduction. It compares
p and interacting spectral bases, retaining both pointer channels and all
finite-grid eigenmodes. No external packages required.
"""
import cmath
import math
import unittest
from itertools import product

from verification.zero_sphere_interacting_clock_spectral_test import build,transform,untransform
from verification.zero_sphere_finite_resolution_clock_instrument_test import apply,dot,no_filter

TIMES=(30,40,50)
CHANNELS=tuple(product((0,1),(1,-1)))


def norm2(v): return dot(v,v).real

def inner_state(x,y): return sum(dot(x[k],y[k]) for k in CHANNELS)

def pnorm(state): return inner_state(state,state).real

def initial_state(f):
    # Initial logical (|0>+i|1>)/sqrt(2), pointer |0_z>=(|+y>+|-y>)/sqrt(2).
    return {(h,d):[v*(1 if h==0 else 1j)/2 for v in f] for h,d in CHANNELS}


def p_to_s(state,systems):
    return {(h,d):transform(systems[d][2],state[h,d]) for h,d in CHANNELS}


def s_to_p(state,systems):
    return {(h,d):untransform(systems[d][2],state[h,d]) for h,d in CHANNELS}


def spectral_E(E,systems):
    n=len(E); result={}
    for d in (1,-1):
        V=systems[d][2]
        EV=[[sum(E[i][k]*V[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        result[d]=[[sum(V[k][i]*EV[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    return result


def evolve(state,systems,dt,basis='p'):
    out={}
    for h,d in CHANNELS:
        values,V=systems[d][1:]
        a=transform(V,state[h,d]) if basis=='p' else state[h,d]
        b=[a[j]*cmath.exp(1j*math.sqrt(values[j]-2*h)*dt) for j in range(len(a))]
        out[h,d]=untransform(V,b) if basis=='p' else b
    return out


def measure(state,matrices,outcome,basis):
    out={}
    for h,d in CHANNELS:
        E=matrices[d] if basis=='spectral' else matrices
        out[h,d]=apply(E,state[h,d]) if outcome else no_filter(E,state[h,d])
    return out


def pointer_probs(state,systems,basis):
    # |1_z> ∝ |+y>−|-y>. Cross-Gram is supplied by going to p.
    st=s_to_p(state,systems) if basis=='spectral' else state
    values=[]
    for sign in (1,-1):
        values.append(sum(norm2([(a+sign*b)/math.sqrt(2)
                      for a,b in zip(st[h,1],st[h,-1])]) for h in (0,1)))
    return values  # pointer z=0, z=1


def first_protocol(f,E,systems,times=TIMES,basis='p'):
    matrices=spectral_E(E,systems) if basis=='spectral' else E
    st=initial_state(f)
    if basis=='spectral':st=p_to_s(st,systems)
    first=[];last=0
    for t in times:
        st=evolve(st,systems,t-last,basis)
        yes=measure(st,matrices,True,basis)
        first.append((pnorm(yes),pointer_probs(yes,systems,basis)))
        st=measure(st,matrices,False,basis)
        last=t
    return first,pnorm(st),st


def history_protocol(f,E,systems,times=TIMES,basis='p'):
    matrices=spectral_E(E,systems) if basis=='spectral' else E
    init=initial_state(f)
    if basis=='spectral':init=p_to_s(init,systems)
    branches={():init};last=0
    for t in times:
        new={}
        for hist,st in branches.items():
            evolved=evolve(st,systems,t-last,basis)
            for hit in (False,True):
                new[hist+(int(hit),)]=measure(evolved,matrices,hit,basis)
        branches=new;last=t
    return {hist:(pnorm(st),pointer_probs(st,systems,basis)) for hist,st in branches.items()}


def independent_occupancy(f,E,systems,t):
    st=evolve(initial_state(f),systems,t,'p')
    return pnorm(measure(st,E,True,'p'))


class InteractingRelationalFirstReadingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data={n:build(n) for n in (40,80)}
        p,f,E,systems=cls.data[80]
        cls.first=first_protocol(f,E,systems)
        cls.hist=history_protocol(f,E,systems)
        cls.first_s=first_protocol(f,E,systems,basis='spectral')
        cls.hist_s=history_protocol(f,E,systems,basis='spectral')

    def test_initial_state_normalized_and_pointer_zero(self):
        p,f,E,systems=self.data[80];st=initial_state(f)
        self.assertAlmostEqual(pnorm(st),1,places=12)
        a,b=pointer_probs(st,systems,'p')
        self.assertAlmostEqual(a,1,places=12);self.assertAlmostEqual(b,0,places=12)

    def test_first_detection_and_no_hit_are_normalized(self):
        first,no,_=self.first
        self.assertAlmostEqual(sum(item[0] for item in first)+no,1,places=11)
        for mass,pointer in first:
            self.assertGreater(mass,0)
            self.assertAlmostEqual(sum(pointer),mass,places=11)

    def test_all_histories_and_no_hit_coarse_graining(self):
        self.assertEqual(len(self.hist),8)
        self.assertAlmostEqual(sum(v[0] for v in self.hist.values()),1,places=11)
        self.assertAlmostEqual(self.hist[0,0,0][0],self.first[1],places=11)
        for k,(mass,_) in enumerate(self.first[0]):
            coarse=sum(v[0] for hist,v in self.hist.items() if hist[k]==1 and all(x==0 for x in hist[:k]))
            self.assertAlmostEqual(coarse,mass,places=11)
        for mass,pointer in self.hist.values():self.assertAlmostEqual(sum(pointer),mass,places=11)
        self.assertGreater(sum(v[0] for hist,v in self.hist.items() if sum(hist)>=2),0)

    def test_fully_transported_interacting_basis_agrees(self):
        for (p,ptr),(q,qtr) in zip(self.first[0],self.first_s[0]):
            self.assertAlmostEqual(p,q,places=10)
            for a,b in zip(ptr,qtr):self.assertAlmostEqual(a,b,places=10)
        self.assertAlmostEqual(self.first[1],self.first_s[1],places=10)
        for hist in self.hist:
            a,x=self.hist[hist];b,y=self.hist_s[hist]
            self.assertAlmostEqual(a,b,places=10)
            for aa,bb in zip(x,y):self.assertAlmostEqual(aa,bb,places=10)

    def test_no_hit_updates_different_question_from_occupancy(self):
        p,f,E,systems=self.data[80]
        occupied=independent_occupancy(f,E,systems,40)
        first40=self.first[0][1][0]
        self.assertGreater(abs(occupied-first40),.01)
        self.assertLess(first40,occupied)

    def test_conditional_pointer_depends_on_detection_time(self):
        first,_,_=self.first
        rates=[pointer[1]/mass for mass,pointer in first]
        self.assertGreater(max(rates)-min(rates),.01)
        for r in rates:self.assertTrue(0<=r<=1)

    def test_incident_and_bound_initial_state_are_both_covered(self):
        p,f,E,systems=self.data[80];Vp=systems[1][2]
        b=[row[0] for row in Vp]
        for state in (f,b):
            first,no,_=first_protocol(state,E,systems)
            self.assertAlmostEqual(sum(x[0] for x in first)+no,1,places=11)
        self.assertGreater(abs(dot(b,f))**2,0)
        # The full state has both d channels; calling b an eigenstate applies
        # only to its d=+ component, not to the whole initial pointer state.

    def test_bound_complement_interference_is_not_classical_mixture(self):
        p,f,E,systems=self.data[80];values,V=systems[1][1:]
        b=[row[0] for row in V]; amp=dot(b,f)
        bound=[amp*x for x in b]; rest=[x-y for x,y in zip(f,bound)]
        def hit(v,t):
            a=transform(V,v)
            u=untransform(V,[a[i]*cmath.exp(1j*math.sqrt(values[i])*t) for i in range(len(a))])
            return norm2(apply(E,u))
        coherent=hit(f,40); mixture=hit(bound,40)+hit(rest,40)
        self.assertAlmostEqual(coherent,.16299007579275132,places=10)
        self.assertAlmostEqual(mixture,.16468131514473944,places=10)
        self.assertGreater(abs(coherent-mixture),.001)

    def test_coherent_memory_unitary_dilation(self):
        p,f,E,systems=self.data[80]
        x=[a*(1+1j*i/80) for i,a in enumerate(f)]
        y=[a*(.3-1j*i/100) for i,a in enumerate(f)]
        Nx=no_filter(E,x); Ny=no_filter(E,y)
        Ex=apply(E,x); Ey=apply(E,y)
        # W = [[N,-E],[E,N]], N=sqrt(I-E²), acting on two memory amplitudes.
        out0=[a-b for a,b in zip(Nx,Ey)];out1=[a+b for a,b in zip(Ex,Ny)]
        self.assertAlmostEqual(norm2(out0)+norm2(out1),norm2(x)+norm2(y),places=10)
        # Inverse uses W†; the same positive operators commute by functional calculus.
        rx=[a+b for a,b in zip(no_filter(E,out0),apply(E,out1))]
        ry=[a-b for a,b in zip(no_filter(E,out1),apply(E,out0))]
        self.assertLess(norm2([a-b for a,b in zip(rx,x)])+norm2([a-b for a,b in zip(ry,y)]),1e-24)

    def test_grid_refinement(self):
        p,f,E,systems=self.data[40];f40,no40,_=first_protocol(f,E,systems)
        for (x,_),(y,_) in zip(f40,self.first[0]):self.assertLess(abs(x-y),.0003)
        self.assertLess(abs(no40-self.first[1]),.0003)

    def test_eigenvector_sign_gauge_does_not_change_predictions(self):
        p,f,E,systems=self.data[40]
        changed={d:(mat,vals,[row[:] for row in V]) for d,(mat,vals,V) in systems.items()}
        for row in changed[1][2]:row[0]=-row[0]
        for row in changed[-1][2]:row[5]=-row[5]
        original=first_protocol(f,E,systems,basis='spectral')
        flipped=first_protocol(f,E,changed,basis='spectral')
        for (mass,ptr),(mass2,ptr2) in zip(original[0],flipped[0]):
            self.assertAlmostEqual(mass,mass2,places=11)
            for a,b in zip(ptr,ptr2):self.assertAlmostEqual(a,b,places=11)
        self.assertAlmostEqual(original[1],flipped[1],places=11)

    def test_naive_ignoring_eigenbasis_mismatch_changes_pointer(self):
        p,f,E,systems=self.data[80]
        first,no,st=first_protocol(f,E,systems,basis='spectral')
        # Incorrectly subtracting equal coefficients in inequivalent d bases.
        naive=sum(norm2([(a-b)/math.sqrt(2) for a,b in zip(st[h,1],st[h,-1])]) for h in (0,1))
        correct=pointer_probs(st,systems,'spectral')[1]
        self.assertGreater(abs(naive-correct),1e-3)

if __name__=='__main__':unittest.main()
