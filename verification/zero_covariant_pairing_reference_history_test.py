"""A permutation-invariant whole with changing relational pairing records.

A regular-representation reference and a covariant controlled exchange are
stipulated resources, not derived from zero. The four spins are logical
factors; no local, gravitational or experiential interpretation is asserted.
"""
import itertools
import math
import unittest
import numpy as np
from verification.zero_energy_sphere_work_incidence_test import X,Y,Z,I
from verification.zero_invariant_all_history_record_clock_test import kron
from verification.zero_stationary_whole_unique_history_test import seed
from verification.zero_relational_orientation_reference_test import C1,C2,C3,L,S

GROUP=list(itertools.permutations(range(4)))
INDEX={g:i for i,g in enumerate(GROUP)}
E=tuple(range(4))

def compose(p,q):return tuple(p[q[i]] for i in range(4))

def perm(p):
    a=np.zeros((16,16),complex)
    for x in range(16):
        bits=[(x>>(3-i))&1 for i in range(4)]
        out=[0]*4
        for i in range(4):out[p[i]]=bits[i]
        y=sum(out[i]<<(3-i) for i in range(4))
        a[y,x]=1
    return a

def transposition(i,j):
    p=list(E);p[i],p[j]=p[j],p[i]
    return perm(tuple(p))

spins=[[kron(*[p if j==i else I for j in range(4)]) for p in (X,Y,Z)] for i in range(4)]
total=[sum(spins[i][a] for i in range(4)) for a in range(3)]
j2=sum(t@t for t in total)/4
values,vectors=np.linalg.eigh(j2)
V=vectors[:,abs(values)<1e-10]
DS=[V.conj().T@perm(g)@V for g in GROUP]
I2=np.eye(2,dtype=complex)
I48=np.eye(48,dtype=complex)
I96=np.eye(96,dtype=complex)

def left(k):
    a=np.zeros((24,24),complex)
    for i,g in enumerate(GROUP):a[INDEX[compose(k,g)],i]=1
    return a

US=[kron(left(g),DS[i]) for i,g in enumerate(GROUP)]
PG=sum(US)/24
Qsym=I48-PG


def block_orbit(a):
    out=np.zeros((48,48),complex)
    for i,d in enumerate(DS):out[2*i:2*i+2,2*i:2*i+2]=d@a@d.conj().T
    return out

singlet=np.array([0,1,-1,0],complex)/math.sqrt(2)
v0=V.conj().T@kron(singlet,singlet)
h0=V.conj().T@transposition(1,2)@V
halt0=V.conj().T@transposition(0,1)@V
q12=(np.eye(16)+transposition(0,1))/2
q13=(np.eye(16)+transposition(0,2))/2
q12small=V.conj().T@q12@V
q13small=V.conj().T@q13@V
Qpair=block_orbit(q12small)
Qtarget=block_orbit(q13small)
H=block_orbit(h0)
Halt=block_orbit(halt0)
psi=np.concatenate([d@v0 for d in DS])/math.sqrt(24)


def stationary(h):
    w=np.vstack(((I48+h)/2,(I48-h)/2))
    c=kron(I,h)-kron(Z,I48)
    qc=c@c/4
    whole=qc+kron(I,Qsym)+w@Qpair@w.conj().T
    return w,c,whole


def evolve(theta,h=H):return math.cos(theta)*psi-1j*math.sin(theta)*(h@psi)

def reduced_spin(v):
    a=v.reshape(24,2)
    return a.T@a.conj()


class CovariantPairingReferenceHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w,cls.c,cls.whole=stationary(H)
        cls.state=cls.w@psi

    def test_permutation_representation_and_singlet_sector(self):
        self.assertEqual(V.shape,(16,2))
        np.testing.assert_allclose(V.conj().T@V,I2,atol=1e-14)
        for p,q in itertools.product(GROUP,repeat=2):
            np.testing.assert_allclose(DS[INDEX[p]]@DS[INDEX[q]],DS[INDEX[compose(p,q)]],atol=1e-14)
        np.testing.assert_allclose(PG@PG,PG,atol=1e-14)
        self.assertAlmostEqual(np.trace(PG).real,2,places=12)
        np.testing.assert_allclose(PG@psi,psi,atol=1e-14)
        # Physical four-spin V is entirely rotation-invariant.
        for t in total:np.testing.assert_allclose(t@V,0,atol=1e-14)
        p0=V@V.conj().T
        for a in (q12,q13,transposition(1,2),transposition(0,1),*[perm(g) for g in GROUP]):
            np.testing.assert_allclose(a@p0,p0@a,atol=1e-14)

    def test_full_spin_space_invariant_pair_and_zero_spin_intersection(self):
        # T maps the complete 16D spin space isometrically onto the full
        # simultaneous-permutation invariant subspace of reference⊗spins.
        t=np.vstack([perm(g) for g in GROUP])/math.sqrt(24)
        np.testing.assert_allclose(t.conj().T@t,np.eye(16),atol=1e-14)
        p0=V@V.conj().T
        np.testing.assert_allclose(p0@q12,q12@p0,atol=1e-14)
        # On an invariant vector, the covariant pair projector pulls back
        # to q12 and total spin zero to p0, even before singlet restriction.
        qapplied=np.vstack([perm(g)@q12@perm(g).conj().T@perm(g) for g in GROUP])/math.sqrt(24)
        np.testing.assert_allclose(qapplied,t@q12,atol=1e-14)
        z=p0@(np.eye(16)-q12)@p0
        self.assertEqual(np.count_nonzero(np.linalg.eigvalsh(z)>1e-10),1)
        for k in GROUP:
            np.testing.assert_allclose(kron(left(k),perm(k))@t,t,atol=1e-14)

    def test_singlet_embedding_retains_the_previous_complementary_zeros(self):
        e0,e1,_=seed()
        encoding=np.column_stack((e0,e1))
        physical=kron(I,encoding,I,I)
        np.testing.assert_allclose(physical.conj().T@physical,np.eye(16),atol=1e-14)
        for c in (C1,C2,C3):
            np.testing.assert_allclose(kron(I,c,I,I)@physical,0,atol=1e-14)
        for s in (L,S):
            np.testing.assert_allclose(kron(I,s,I,I)@physical,physical,atol=1e-14)
        # Every state of all four logical factors embeds in the same old
        # balance kernel; every frame and time branch stays in it.

    def test_covariant_controls_and_pair_condition_are_global_invariants(self):
        for a in (Qpair,Qtarget,H,Halt):
            for u in US:np.testing.assert_allclose(a@u,u@a,atol=1e-14)
        for a in (Qpair,Qtarget,Qsym):np.testing.assert_allclose(a@a,a,atol=1e-14)
        for h in (H,Halt):np.testing.assert_allclose(h@h,I48,atol=1e-14)
        np.testing.assert_allclose(Qpair@psi,0,atol=1e-14)
        self.assertEqual(np.count_nonzero(abs(np.linalg.eigvalsh(Qsym+Qpair))<1e-10),1)
        self.assertGreater(np.linalg.norm(H@Qpair-Qpair@H),.1)
        # At every frame label g, Qpair asks about the g-transformed
        # pairing, not a fixed pair in an external labeling.

    def test_stationary_whole_is_unique_invariant_and_balanced(self):
        np.testing.assert_allclose(self.w.conj().T@self.w,I48,atol=1e-14)
        np.testing.assert_allclose(self.c@self.w,0,atol=1e-14)
        ev=np.linalg.eigvalsh(self.whole)
        self.assertEqual(np.count_nonzero(abs(ev)<1e-10),1)
        self.assertAlmostEqual(ev[1],1,places=12)
        np.testing.assert_allclose(self.whole@self.state,0,atol=1e-14)
        for u in US:
            np.testing.assert_allclose(kron(I,u)@self.state,self.state,atol=1e-14)
            np.testing.assert_allclose(kron(I,u)@self.whole,self.whole@kron(I,u),atol=1e-14)

    def test_reference_relative_pairing_changes_while_unconditional_spin_does_not(self):
        for theta in (0,math.pi/4,math.pi/2):
            v=evolve(theta)
            np.testing.assert_allclose(reduced_spin(v),I2/2,atol=1e-14)
            self.assertAlmostEqual(np.vdot(v,Qpair@v).real,.75*math.sin(theta)**2,places=12)
            self.assertAlmostEqual(np.vdot(v,Qtarget@v).real,.75*math.cos(theta)**2,places=12)
            for u in US:np.testing.assert_allclose(u@v,v,atol=1e-14)
            # The frame diagonal stays uniform even while the relational
            # frame-spin joint state and invariant pair observables change.
            self.assertTrue(np.allclose(np.sum(abs(v.reshape(24,2))**2,axis=1),1/24))
        # The global state is pure and the frame-spin Schmidt rank is two;
        # discarding the frame is not a dephasing of the whole.
        self.assertAlmostEqual(np.linalg.norm(psi),1,places=12)
        self.assertAlmostEqual(np.trace(reduced_spin(psi)@reduced_spin(psi)).real,.5,places=12)
        self.assertEqual(np.count_nonzero(np.linalg.svd(psi.reshape(24,2),compute_uv=False)>1e-10),2)
        # In the identity frame, the actual four-spin readout transfers
        # anti-correlations from pair 01 to pair 02.
        physical0=V@v0
        physical1=transposition(1,2)@physical0
        self.assertAlmostEqual(np.vdot(physical0,q12@physical0).real,0,places=12)
        self.assertAlmostEqual(np.vdot(physical1,q13@physical1).real,0,places=12)

    def test_clock_relative_history_and_finite_window(self):
        for theta in (0,math.pi/4,math.pi/2):
            bra=np.array([np.exp(-1j*theta),np.exp(1j*theta)])/math.sqrt(2)
            raw=kron(bra.reshape(1,2),I48)@self.state
            np.testing.assert_allclose(raw,evolve(theta)/math.sqrt(2),atol=1e-14)
        delta=math.pi/8
        nodes,weights=np.polynomial.legendre.leggauss(24)
        averaged=sum(w*np.vdot(evolve(math.pi/2+delta*x),Qtarget@evolve(math.pi/2+delta*x)).real/2
                     for x,w in zip(nodes,weights))
        expected=.75*(.5-math.sin(2*delta)/(4*delta))
        self.assertAlmostEqual(averaged,expected,places=12)
        self.assertAlmostEqual(2*delta/math.pi,.25,places=13)

    def test_same_symmetries_admit_a_frozen_alternative(self):
        # Exchange within the initial singlet is invariant when covariantly
        # controlled, has the same ±1 spectrum, and fixes psi up to phase.
        np.testing.assert_allclose(Halt@psi,-psi,atol=1e-14)
        altw,altc,altwhole=stationary(Halt)
        ev=np.linalg.eigvalsh(altwhole)
        self.assertEqual(np.count_nonzero(abs(ev)<1e-10),1)
        np.testing.assert_allclose(altwhole@altw@psi,0,atol=1e-14)
        for theta in (0,math.pi/4,math.pi/2):
            v=evolve(theta,Halt)
            self.assertAlmostEqual(np.vdot(v,Qtarget@v).real,.75,places=12)
        for u in US:np.testing.assert_allclose(kron(I,u)@altwhole,altwhole@kron(I,u),atol=1e-14)

    def test_reference_label_redundancy_is_not_an_incidence_measure(self):
        # Orbits of the physical matching 01|23 comprise exactly 3 matchings,
        # each with 8 labels; group-frame labels are not distinct subjects.
        pairs=[]
        for p in GROUP:
            pairs.append(frozenset((frozenset((p[0],p[1])),frozenset((p[2],p[3])))))
        self.assertEqual(len(set(pairs)),3)
        self.assertEqual(sorted(pairs.count(x) for x in set(pairs)),[8,8,8])
        # Equal frame amplitudes were stipulated via regular-representation
        # invariance; no probability of actual subject incidence follows.

if __name__=='__main__':unittest.main()
