"""A conservation-preserving three-outcome instrument in spin-zero sectors.

Finite checks only. Spin-zero representations, logical singlet, ray-to-logical
identification, instrument, and Born rule are assumptions, not experience.
"""
import math
import unittest
from verification.zero_spin_constitution_test import (
    X, Y, Z, add, close, eye, four_singlet_pairings, inner, mm, mv,
    pair_singlet_projector, scale, total_spin,
)


def adj(a): return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]
def norm(v): return math.sqrt(max(0, inner(v,v).real))
def unit(v):
    n=norm(v)
    return [x/n for x in v]
def dot_sub(v,b):
    coeff=inner(b,v)
    return [x-coeff*y for x,y in zip(v,b)]
def extend(vectors, dimension):
    out=[]
    for v in vectors + [[complex(i==j) for i in range(dimension)] for j in range(dimension)]:
        w=v[:]
        for b in out: w=dot_sub(w,b)
        if norm(w)>1e-9: out.append(unit(w))
        if len(out)==dimension: break
    return out

def columns_to_matrix(columns): return [[v[i] for v in columns] for i in range(len(columns[0]))]
def product(v,w): return [x*y for x in v for y in w]
def pairing_vectors(indices):
    if not indices:
        yield []
        return
    i=indices[0]
    for j in indices[1:]:
        remaining=[k for k in indices[1:] if k!=j]
        for rest in pairing_vectors(remaining): yield [(i,j)]+rest

def singlet_pairs(pairs,n=6):
    out=[0j]*(2**n)
    for choices in range(2**len(pairs)):
        bits=[0]*n; amp=1.0
        for p,(i,j) in enumerate(pairs):
            bit=(choices>>p)&1
            bits[i]=bit; bits[j]=1-bit
            if bit: amp=-amp
        index=sum(bit << (n-1-i) for i,bit in enumerate(bits))
        out[index]=amp/(2**(len(pairs)/2))
    return out

def frame(vectors):
    out=[]
    for v in vectors:
        w=v[:]
        for b in out: w=dot_sub(w,b)
        if norm(w)>1e-9: out.append(unit(w))
    return out

def logical_basis():
    a,b=four_singlet_pairings()
    return a,[(2*y-x)/math.sqrt(3) for x,y in zip(a,b)]

def effects():
    ns=((0,0,1),(math.sqrt(3)/2,0,-.5),(-math.sqrt(3)/2,0,-.5))
    return [scale(1/3,add(eye(2),add(add(scale(x,X),scale(y,Y)),scale(z,Z)))) for x,y,z in ns]

def mat_expect(v,a): return inner(v,mv(a,v))

# Positive square roots of F_i = (2/3) Π_i.
def kraus(): return [scale(math.sqrt(3/2),f) for f in effects()]

def instrument_unitary(ks=None):
    # Computational order: system logical bit, then pointer |0> ... |4>.
    if ks is None: ks=kraus()
    initial=[[complex(j==5*s) for j in range(10)] for s in range(2)]
    targets=[]
    for s in range(2):
        targets.append([sum(k[t][s] if p==i else 0 for i,k in enumerate(ks))
                        for t in range(2) for p in range(5)])
    source_basis=extend(initial,10)
    target_basis=extend(targets,10)
    return mm(columns_to_matrix(target_basis),adj(columns_to_matrix(source_basis)))

class InvariantInstrumentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pbasis=frame([singlet_pairs(p) for p in pairing_vectors(list(range(6)))])
        cls.sbasis=logical_basis()
        cls.u=instrument_unitary()

    def test_six_spin_pointer_zero_sector_dimension_five(self):
        # The angular-momentum addition rule gives singlet multiplicity
        # C(6,3)-C(6,2)=5; five independent constructed singlets saturate it.
        self.assertEqual(len(self.pbasis),5)
        self.assertEqual(math.comb(6,3)-math.comb(6,2),5)
        for b in self.pbasis:
            self.assertAlmostEqual(inner(b,b).real,1)
            for s in (X,Y,Z): self.assertLess(norm(mv(total_spin(s,6),b)),1e-9)
        for i in range(5):
            for j in range(5): self.assertAlmostEqual(abs(inner(self.pbasis[i],self.pbasis[j])-(i==j)),0)

    def test_logical_spin_comes_from_rotational_scalars(self):
        a,c=self.sbasis
        p12=pair_singlet_projector(0,1); p13=pair_singlet_projector(0,2)
        logical_x=scale(1/math.sqrt(3),add(add(scale(4,p13),scale(2,p12)),scale(-3,eye(16))))
        for op in (X,Y,Z):
            t=total_spin(op,4)
            close(self,mm(t,logical_x),mm(logical_x,t))
        for expected,state in ((c,a),(a,c)):
            self.assertLess(norm([x-y for x,y in zip(mv(logical_x,state),expected)]),1e-9)

    def test_effects_and_kraus_normalize(self):
        sums=[[0j]*2 for _ in range(2)]
        for k in kraus(): sums=add(sums,mm(adj(k),k))
        close(self,sums,eye(2))
        for f in effects():
            close(self,mm(f,f),scale(2/3,f))
            self.assertAlmostEqual(sum(f[i][i].real for i in range(2)),2/3)

    def test_explicit_unitary_implements_all_three_effects(self):
        u=self.u
        close(self,mm(adj(u),u),eye(10))
        close(self,mm(u,adj(u)),eye(10))
        for s in range(2):
            for t in range(2):
                for i in range(5):
                    want=kraus()[i][t][s] if i<3 else 0
                    self.assertAlmostEqual(abs(u[5*t+i][5*s]-want),0)

    def test_constraint_preserved_for_each_record_branch(self):
        # Each tensor factor in the expansion is individually a physical
        # spin-zero vector; any superposition or selected pointer branch
        # is annihilated by all components of total physical spin.
        for b in list(self.sbasis)+self.pbasis:
            for op in (X,Y,Z):
                t=total_spin(op,4 if len(b)==16 else 6)
                self.assertLess(norm(mv(t,b)),1e-9)
        for i in range(3):
            self.assertGreater(sum(abs(self.u[5*t+i][5*s])**2
                                   for s in range(2) for t in range(2)),0)

    def test_remote_steering_and_no_signalling(self):
        # ρ_SB is a logical singlet; σ_B|i=Tr_S[(F_i⊗I)ρ_SB].
        psi=[0,1/math.sqrt(2),-1/math.sqrt(2),0]
        sigma=[]
        for f in effects():
            b=[[sum(f[t][s]*psi[2*s+j]*psi[2*t+k].conjugate()
                    for s in range(2) for t in range(2)) for k in range(2)] for j in range(2)]
            sigma.append(b)
        for f,b in zip(effects(),sigma):
            close(self,b,scale(.5,add(scale(2/3,eye(2)),scale(-1,f))))
            self.assertAlmostEqual(sum(b[i][i].real for i in range(2)),1/3)
        total=[[0j]*2 for _ in range(2)]
        for b in sigma: total=add(total,b)
        close(self,total,scale(.5,eye(2)))

    def test_asymmetric_ray_weights_have_a_complete_invariant_dilation(self):
        from verification.zero_sphere_conservation_born_bridge_test import bridge, ray
        rays=[ray(0),ray(1),ray(3),ray(0,1),ray(0,2)]
        result,weights,dots=bridge(rays)
        ids=result['triple']
        q=[float(weights[i]) for i in ids]
        ns=((1,0,0),(.5,math.sqrt(3)/2,0),(-13/19,-8*math.sqrt(3)/19,0))
        for i in range(3):
            for j in range(3):
                self.assertAlmostEqual(sum(a*b for a,b in zip(ns[i],ns[j])),float(dots[ids[i]][ids[j]]))
        fs=[scale(qi,add(eye(2),add(add(scale(x,X),scale(y,Y)),scale(z,Z))))
            for qi,(x,y,z) in zip(q,ns)]
        ks=[scale(1/math.sqrt(2*qi),f) for qi,f in zip(q,fs)]
        sums=[[0j]*2 for _ in range(2)]
        for k in ks: sums=add(sums,mm(adj(k),k))
        close(self,sums,eye(2))
        u=instrument_unitary(ks)
        close(self,mm(adj(u),u),eye(10))
        for s in range(2):
            for t in range(2):
                for i in range(3): self.assertAlmostEqual(abs(u[5*t+i][5*s]-ks[i][t][s]),0)
        for f,qi in zip(fs,q):
            self.assertAlmostEqual(sum(f[j][j].real for j in range(2))/2,qi)
        for j in range(3): self.assertAlmostEqual(sum(q[i]*ns[i][j] for i in range(3)),0)

    def test_probability_depends_on_state_and_record_can_be_erased(self):
        f=effects()
        self.assertAlmostEqual(mat_expect([1,0],f[0]).real,2/3)
        self.assertNotAlmostEqual(mat_expect([1,0],f[0]).real,1/3)
        # U† reverses the measurement interaction; correlation is not itself
        # irreversible memory or a definite experienced outcome.
        initial=unit([complex(i==0)+1j*complex(i==5) for i in range(10)])
        restored=mv(adj(self.u),mv(self.u,initial))
        self.assertLess(norm([x-y for x,y in zip(restored,initial)]),1e-9)

if __name__=='__main__': unittest.main()
