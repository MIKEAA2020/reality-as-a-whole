"""Local commuting incidence / quantum current accounting controls.

Register bits and subject identities are stipulated; no claim of actual
consciousness, phenomenal intensity, global necessity or a cosmic energy zero.
"""
from itertools import product
from math import sqrt
import unittest


def eye(n): return [[complex(i==j) for j in range(n)] for i in range(n)]
def add(a,b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def scale(x,a): return [[x*v for v in row] for row in a]
def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]
def kron(a,b):
    return [[a[i//len(b)][j//len(b[0])]*b[i%len(b)][j%len(b[0])]
             for j in range(len(a[0])*len(b[0]))]
            for i in range(len(a)*len(b))]


def on_site(op,site):
    out=[[1]]
    for i in range(4): out=kron(out,op if i==site else eye(2))
    return out


def expectation(v,a):
    return sum(v[i].conjugate()*a[i][j]*v[j] for i in range(len(v))
               for j in range(len(v)))
def assert_close(test,a,b):
    for ar,br in zip(a,b):
        for x,y in zip(ar,br): test.assertAlmostEqual(abs(x-y),0)


def quantum_chain():
    # One-excitation sector of H=2 Σ n_i + Σ (σ+_i σ-_j+h.c.).
    H=scale(2,eye(4))
    for i in range(3): H[i][i+1]=H[i+1][i]=1
    currents=[]
    for i in range(4):
        Pi=[[complex(j==i and k==i) for k in range(4)] for j in range(4)]
        energy=scale(2,Pi)
        currents.append(scale(1j,add(mm(H,energy),scale(-1,mm(energy,H)))))
    return H,currents


def presence(subject,site,register):
    if subject==0: return int(site in (0,1,2))
    if subject==1:
        if site in (1,2): return int(register[site]==0)
        return int(site==3)
    raise ValueError('subject must be 0 or 1')


def local_contributions(currents,register):
    out=[[[0j]*4 for _ in range(4)] for _ in range(2)]
    for i,h in enumerate(currents):
        flags=[presence(s,i,register) for s in range(2)]
        m=sum(flags)
        if not m: raise ValueError('this example requires full coverage')
        for s in range(2):
            out[s]=add(out[s],scale(flags[s]/m,h))
    return out


class LocalIncidenceCurrentTests(unittest.TestCase):
    def setUp(self): self.H,self.h=quantum_chain()

    def test_physical_current_operators_sum_to_zero(self):
        total=[[0j]*4 for _ in range(4)]
        for h in self.h: total=add(total,h)
        assert_close(self,total,[[0j]*4 for _ in range(4)])
        self.assertTrue(any(abs(x)>0 for row in self.h[1] for x in row))

    def test_joint_local_incidence_identity_for_all_register_states(self):
        for r in product((0,1),repeat=4):
            a,b=local_contributions(self.h,r)
            assert_close(self,add(a,b),[[0j]*4 for _ in range(4)])
            for i in range(4):
                flags=[presence(s,i,r) for s in range(2)]
                m=sum(flags)
                self.assertGreater(m,0)
                self.assertEqual(sum(f/m for f in flags),1)

    def test_actual_nonzero_correlations_for_coherent_physical_state(self):
        r=(0,0,1,0)
        a,b=local_contributions(self.h,r)
        v=(0,1/sqrt(2),1j/sqrt(2),0)
        self.assertAlmostEqual(expectation(v,a).real,-1)
        self.assertAlmostEqual(expectation(v,b).real,1)
        self.assertAlmostEqual(expectation(v,add(a,b)).real,0)

    def test_each_local_allocation_ignores_a_remote_register_bit(self):
        # Site 1 allocation depends on r1, not remote r3.
        for r0,r1,r2 in product((0,1),repeat=3):
            r=(r0,r1,r2,0); rp=(r0,r1,r2,1)
            for s in range(2):
                a=presence(s,1,r)/sum(presence(k,1,r) for k in range(2))
                b=presence(s,1,rp)/sum(presence(k,1,rp) for k in range(2))
                self.assertEqual(a,b)

    def test_physical_current_is_local_in_full_four_qubit_algebra(self):
        sp=[[0,0],[1,0]]; sm=[[0,1],[0,0]]; n=[[0,0],[0,1]]
        x=[[0,1],[1,0]]
        H=[[0j]*16 for _ in range(16)]
        for i in range(4): H=add(H,scale(2,on_site(n,i)))
        for i in range(3):
            hop=add(mm(on_site(sp,i),on_site(sm,i+1)),
                    mm(on_site(sm,i),on_site(sp,i+1)))
            H=add(H,hop)
        h1=scale(1j,add(mm(H,scale(2,on_site(n,1))),
                         scale(-1,mm(scale(2,on_site(n,1)),H))))
        xremote=on_site(x,3)
        assert_close(self,mm(h1,xremote),mm(xremote,h1))
        self.assertTrue(any(abs(v)>0 for row in h1 for v in row))

    def test_uncovered_sector_leaves_exact_unassigned_current(self):
        # Drop all incidences on site 1: covered sum is total minus h1.
        covered=add(add(self.h[0],self.h[2]),self.h[3])
        assert_close(self,covered,scale(-1,self.h[1]))
        self.assertTrue(any(abs(x)>0 for row in covered for x in row))

    def test_excitation_presence_and_hopping_current_do_not_commute(self):
        # On |10>,|01> sector, H_A=2P0, J_A=2Y.
        P0=[[1,0],[0,0]]; P1=[[0,0],[0,1]]
        J=[[0,-2j],[2j,0]]
        comm=add(mm(P0,J),scale(-1,mm(J,P0)))
        self.assertTrue(any(abs(x)>0 for row in comm for x in row))
        # Every support-preserving split P0 V0 P0 + P1 V1 P1 is diagonal,
        # so cannot equal off-diagonal J.
        assert_close(self,add(mm(mm(P0,J),P0),mm(mm(P1,J),P1)),[[0,0],[0,0]])

    def test_formal_symmetrization_does_not_respect_absent_subject_support(self):
        P0=[[1,0],[0,0]]; P1=[[0,0],[0,1]]; J=[[0,-2j],[2j,0]]
        v0=scale(.5,add(mm(P0,J),mm(J,P0)))
        v1=scale(.5,add(mm(P1,J),mm(J,P1)))
        assert_close(self,add(v0,v1),J)
        assert_close(self,mm(mm(P1,v0),P1),[[0,0],[0,0]])
        # Despite zero mean for |1>, v0² has nonzero expectation: a sharp
        # v0 measurement can output ±1 even where P0 says 'absent'.
        absent=(0,1)
        self.assertAlmostEqual(expectation(absent,v0).real,0)
        self.assertAlmostEqual(expectation(absent,mm(v0,v0)).real,1)


if __name__ == '__main__': unittest.main()
