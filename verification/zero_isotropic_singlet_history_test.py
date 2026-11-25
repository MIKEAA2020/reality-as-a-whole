"""Rotationally invariant zero-balanced history, with explicit alternatives.

Diagonal SU(2), spin representations, pairing and exchange remain inputs;
spin balance is not cosmic energy or experiential valence. Clock-relative
Born correlations do not establish actual subjective outcomes.
"""
import math
import unittest
import numpy as np
from verification.zero_energy_sphere_work_incidence_test import X,Y,Z,I,full_state
from verification.zero_all_sector_sphere_clock_work_test import complement_state
from verification.zero_relational_orientation_reference_test import C1,C2,C3,L,S,with_reference
from verification.zero_invariant_all_history_record_clock_test import XL,ZL,kron
from verification.zero_stationary_whole_unique_history_test import seed,K,Hcas
from verification.zero_constitution_hamiltonian_phase_gate_test import J16,X16,Z16,P16
from verification.zero_reciprocal_subject_exchange_test import n

# Order B, R/W/T/F, M, N. Clock C is prepended to the whole.
I16=np.eye(16,dtype=complex)
I128=np.eye(128,dtype=complex)
I256=np.eye(256,dtype=complex)
YL=-1j*ZL@XL
bs=[kron(x,I16,I,I) for x in (X,Y,Z)]
ls=[kron(I,x,I,I) for x in (XL,YL,ZL)]
ms=[kron(I,I16,x,I) for x in (X,Y,Z)]
ns=[kron(I,I16,I,x) for x in (X,Y,Z)]
totalspin=[b+l+m+n for b,l,m,n in zip(bs,ls,ms,ns)]

def triplet(a,b):return (3*I128+sum(x@y for x,y in zip(a,b)))/4

def swap(a,b):return (I128+sum(x@y for x,y in zip(a,b)))/2

Qbl=triplet(bs,ls)
Qmn=triplet(ms,ns)
Qbm=triplet(bs,ms)
Qln=triplet(ls,ns)
H=swap(ls,ms)
Halt=swap(bs,ms)
Pp=(I128+H)/2
Pm=(I128-H)/2
W=np.vstack((Pp,Pm))
clock=kron(I,H)-kron(Z,I128)
Qc=clock@clock/4
Qbal=kron(I,I,Hcas,I,I)
Qbranch=kron(I,I,(I16-L)/2,I,I)
Rbl=W@Qbl@W.conj().T
Rmn=W@Qmn@W.conj().T
Hwhole=Qbal+Qbranch+Qc+Rbl+Rmn


def initial():
    e0,e1,_=seed()
    b0=np.array([1,0],complex);b1=np.array([0,1],complex)
    mn=(kron(b0,b1)-kron(b1,b0))/math.sqrt(2)
    bl=(kron(b0,e1)-kron(b1,e0))/math.sqrt(2)
    return kron(bl,mn)


def evolve(v,theta,h=H):
    return math.cos(theta)*v-1j*math.sin(theta)*(h@v)


def table_bm(v):
    a=v.reshape(2,2,2,2,2,2,2)
    return np.sum(abs(a)**2,axis=(1,2,3,4,6))


class IsotropicZeroHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.v=initial()
        cls.whole=W@cls.v

    def test_exact_spin_algebra_and_invariant_pair_projectors(self):
        for ops in (bs,ls,ms,ns):
            for i,j,k in ((0,1,2),(1,2,0),(2,0,1)):
                np.testing.assert_allclose(ops[i]@ops[j]-ops[j]@ops[i],2j*ops[k],atol=1e-14)
        for q in (Qbl,Qmn,Qbm,Qln):
            np.testing.assert_allclose(q@q,q,atol=1e-14)
            for t in totalspin:np.testing.assert_allclose(q@t,t@q,atol=1e-14)
        np.testing.assert_allclose(H@H,I128,atol=1e-14)
        for t in totalspin:
            np.testing.assert_allclose(H@t,t@H,atol=1e-14)
            np.testing.assert_allclose(Halt@t,t@Halt,atol=1e-14)
        for c in (C1,C2,C3,L,S):
            q=kron(I,c,I,I)
            np.testing.assert_allclose(H@q,q@H,atol=1e-14)
            np.testing.assert_allclose(Halt@q,q@Halt,atol=1e-14)

    def test_logical_exchange_factors_have_physical_work_extension(self):
        # R,W16,T,F; inactive work states are not asserted to carry a qubit.
        i16=np.eye(16,dtype=complex)
        xp=kron(X,J16,X,I)
        zp=kron(Z,i16,I,I)
        yp=-1j*zp@xp
        proj=kron(I,P16,I,I)
        c1=-kron(Z,X16,X,I)-kron(I,P16,I,X)
        c2=-kron(Z,Z16,X,I)-kron(I,P16,I,Y)
        c3=kron(I,J16,I,I)+kron(I,P16,I,Z)
        ell=kron(Z,J16,Z,I)
        qori=kron(I,J16,I,I)+kron(I,i16,I,Z)
        for x in (xp,yp,zp):
            for q in (proj,c1,c2,c3,ell,qori):
                np.testing.assert_allclose(x@q,q@x,atol=1e-14)
            for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
                number=kron(I,sum(np.asarray(n[k],complex) for k in inds),I,I)
                np.testing.assert_allclose(x@number,number@x,atol=1e-14)
        # Hence their coupling to neutral M preserves those charges. B's
        # old-environment encoding has not been shown local or charge-neutral.

    def test_unique_symmetric_stationary_zero_and_gap(self):
        np.testing.assert_allclose(W.conj().T@W,I128,atol=1e-14)
        np.testing.assert_allclose(clock@W,0,atol=1e-14)
        ps=[Qbal,Qbranch,Qc,Rbl,Rmn]
        for p in ps:
            np.testing.assert_allclose(p@p,p,atol=2e-14)
            np.testing.assert_allclose(p,p.conj().T,atol=1e-14)
        for i,p in enumerate(ps):
            for q in ps[i+1:]:np.testing.assert_allclose(p@q,q@p,atol=2e-14)
        vals=np.linalg.eigvalsh(Hwhole)
        self.assertEqual(np.count_nonzero(abs(vals)<1e-10),1)
        self.assertAlmostEqual(vals[1],1,places=12)
        np.testing.assert_allclose(Hwhole@self.whole,0,atol=2e-14)
        for t in totalspin:
            np.testing.assert_allclose(kron(I,t)@self.whole,0,atol=2e-14)
            np.testing.assert_allclose(kron(I,t)@Hwhole,Hwhole@kron(I,t),atol=2e-14)
        for c in (C1,C2,C3):
            np.testing.assert_allclose(kron(I,I,c,I,I)@self.whole,0,atol=2e-14)

    def test_full_global_zero_spin_does_not_force_pair_selection(self):
        # With only the old kernel and total spin zero, four spin halves have
        # two independent singlets. Qbl+Qmn selects one; Qbm+Qln another.
        t2=sum(t@t for t in totalspin)/4
        localbase=kron(I,Hcas,I,I)+kron(I,(I16-L)/2,I,I)
        vals=np.linalg.eigvalsh(localbase+t2)
        self.assertEqual(np.count_nonzero(abs(vals)<1e-10),2)
        a=self.v
        b=H@a # swap L and M, maps BL+MN pairing to BM+LN
        np.testing.assert_allclose(Qbm@b,0,atol=1e-14)
        np.testing.assert_allclose(Qln@b,0,atol=1e-14)
        for t in totalspin:np.testing.assert_allclose(t@b,0,atol=1e-14)
        self.assertAlmostEqual(abs(np.vdot(a,b))**2,.25,places=12)
        self.assertAlmostEqual(np.vdot(b,Qbl@b).real,.75,places=12)

    def test_isotropic_record_transfer_and_distinct_symmetric_dynamics(self):
        for theta in (0,math.pi/4,math.pi/2):
            v=evolve(self.v,theta)
            anti=(1+math.sin(theta)**2)/2
            np.testing.assert_allclose(table_bm(v),[[ (1-anti)/2,anti/2],
                                                   [anti/2,(1-anti)/2]],atol=1e-14)
            for b,m in zip(bs,ms):
                self.assertAlmostEqual(np.vdot(v,b@m@v).real,-math.sin(theta)**2,places=12)
            for c in (C1,C2,C3):
                np.testing.assert_allclose(kron(I,c,I,I)@v,0,atol=1e-14)
            for t in totalspin:np.testing.assert_allclose(t@v,0,atol=1e-14)
            other=evolve(self.v,theta,Halt)
            np.testing.assert_allclose(table_bm(other),np.ones((2,2))/4,atol=1e-14)
        # Both choices are SU(2)-symmetric and preserve all C_i, but give
        # different fixed-reference B–M statistics at θ=π/2.

    def test_alternative_exchange_also_has_a_unique_invariant_zero_whole(self):
        altw=np.vstack(((I128+Halt)/2,(I128-Halt)/2))
        altc=kron(I,Halt)-kron(Z,I128)
        altq=altc@altc/4
        altwhole=Qbal+Qbranch+altq+altw@Qbl@altw.conj().T+altw@Qmn@altw.conj().T
        self.assertEqual(np.count_nonzero(abs(np.linalg.eigvalsh(altwhole))<1e-10),1)
        np.testing.assert_allclose(altwhole@altw@self.v,0,atol=2e-14)
        for t in totalspin:
            np.testing.assert_allclose(kron(I,t)@altwhole,altwhole@kron(I,t),atol=2e-14)
        # Same zero balances, pair singlets, clock spectrum and diagonal SU(2),
        # but B–M's conditional probabilities differ from H=swap(L,M).

    def test_finite_clock_window_has_high_isotropic_transfer(self):
        delta=math.pi/8
        anti=(1+(.5+math.sin(2*delta)/(4*delta)))/2
        self.assertAlmostEqual(anti,.9750790790392765,places=12)
        info=1+anti*math.log2(anti)+(1-anti)*math.log2(1-anti)
        self.assertAlmostEqual(info,.8317572182877314,places=12)
        nodes,weights=np.polynomial.legendre.leggauss(24)
        avg=sum(w*table_bm(evolve(self.v,math.pi/2+delta*x))/2 for x,w in zip(nodes,weights))
        np.testing.assert_allclose(avg,[[(1-anti)/2,anti/2],[anti/2,(1-anti)/2]],atol=1e-14)
        self.assertAlmostEqual(2*delta/math.pi,.25,places=13)

    def test_dressed_selectors_reproduce_pair_seed_at_clock_zero(self):
        for theta in (0,.3,math.pi/2):
            bra=np.array([np.exp(-1j*theta),np.exp(1j*theta)])/math.sqrt(2)
            relative=kron(bra.reshape(1,2),I128)@self.whole
            np.testing.assert_allclose(relative,evolve(self.v,theta)/math.sqrt(2),atol=1e-14)
        np.testing.assert_allclose(Qbl@self.v,0,atol=1e-14)
        np.testing.assert_allclose(Qmn@self.v,0,atol=1e-14)
        # Neither M nor N alone has a preferred ready state.
        density=self.v.reshape(32,2,2)
        rho_m=np.einsum('amn,apn->mp',density,density.conj())
        np.testing.assert_allclose(rho_m,I/2,atol=1e-14)

    def test_old_coherent_environment_can_encode_isotropic_reference(self):
        e0,e1,_=seed()
        code=with_reference(full_state(4)).reshape(-1,16)
        comp=with_reference(complement_state(4)).reshape(-1,16)
        a=np.concatenate((math.sqrt(1/128)*code,math.sqrt(127/128)*comp),axis=0)
        f0=math.sqrt(2)*a@e0.conj()
        f1=math.sqrt(2)*a@e1.conj()
        self.assertLess(abs(np.vdot(f0,f1)),1e-12)
        self.assertAlmostEqual(np.linalg.norm(f0),1,places=12)
        self.assertAlmostEqual(np.linalg.norm(f1),1,places=12)
        # The singlet BL is mapped to the old state by V|0>=f1,V|1>=-f0.
        reconstructed=(np.outer(f1,e1)+np.outer(f0,e0))/math.sqrt(2)
        np.testing.assert_allclose(a,reconstructed,atol=2e-14)
        # V defines the representation of B on a selected environment
        # subspace; it does not derive the old state or a local interface.

class PermutationPlenitudeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        eye2=np.eye(2,dtype=complex)
        spins=[]
        for i in range(4):
            spins.append([kron(*[p if j==i else eye2 for j in range(4)])
                          for p in (X,Y,Z)])
        total=[sum(spins[i][a] for i in range(4)) for a in range(3)]
        j2=sum(t@t for t in total)/4
        values,vectors=np.linalg.eigh(j2)
        cls.v=vectors[:,abs(values)<1e-10]
        assert cls.v.shape==(16,2)
        cls.p=cls.v@cls.v.conj().T
        cls.swaps=[(np.eye(16)+sum(a@b for a,b in zip(spins[i],spins[i+1])))/2
                   for i in range(3)]
        cls.ds=[cls.v.conj().T@s@cls.v for s in cls.swaps]
        cls.spins=spins

    def test_all_pairings_symmetry_gives_unique_mixed_singlet(self):
        rho=self.p/2
        for s in self.swaps:np.testing.assert_allclose(s@rho@ s.conj().T,rho,atol=1e-14)
        self.assertAlmostEqual(np.trace(rho@rho).real,.5,places=12)
        # In the two-dimensional singlet multiplicity, the three adjacent
        # swaps have only scalar matrices in their common commutant.
        linear=np.vstack([np.kron(np.eye(2),d)-np.kron(d.T,np.eye(2)) for d in self.ds])
        self.assertEqual(np.linalg.matrix_rank(linear,tol=1e-10),3)
        for i in range(4):
            for j in range(i+1,4):
                for a in range(3):
                    self.assertAlmostEqual(np.trace(rho@self.spins[i][a]@self.spins[j][a]).real,-1/3,places=12)

    def test_no_pure_state_can_obey_both_full_symmetries_in_four_spins(self):
        # Any pure-state density invariant under S4 affords a 1D character;
        # all adjacent transpositions must have common sign + or common sign -.
        for sign in (1,-1):
            penalty=sum((np.eye(2)-sign*d)/2 for d in self.ds)
            self.assertGreater(np.linalg.eigvalsh(penalty)[0],.1)

    def test_canonical_purification_and_no_internal_symmetric_dynamics(self):
        # Add a 2D reference carrying the conjugate multiplicity representation.
        # The vectorized identity is invariant under D⊗D* independently of basis.
        bell=np.array([1,0,0,1],complex)/math.sqrt(2)
        penalty=np.zeros((4,4),complex)
        for d in self.ds:
            u=kron(d,d.conj())
            np.testing.assert_allclose(u@bell,bell,atol=1e-14)
            penalty+=(np.eye(4)-u).conj().T@(np.eye(4)-u)
        self.assertEqual(np.count_nonzero(abs(np.linalg.eigvalsh(penalty))<1e-10),1)
        # A Hamiltonian preserving the spin-zero sector and commuting with
        # all permutations is scalar on it (commutant dimension one above).
        # Hence all density-matrix readouts are frozen in this closed sector.

if __name__=='__main__':unittest.main()
