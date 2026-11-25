"""A relative chirality, invariant under a diagonal reference swap.

This is an exact refinement of the prior same-state report, not a proof that
any particular swap is gauge in nature or that pointer signs are felt.
"""
import math
import unittest
import numpy as np
from verification.zero_relational_chirality_report_test import (
    I,X,Y,Z,I16,I64,A,D,E,C,LL,CHI,PP,PM,GATE,SWAP,SING,
    XL,ZL,kron,eps,full_state,active_base,compressed_spin_base,
    output,relative_read,initial,apply64
)
from verification.zero_relational_orientation_reference_test import L,Psing
from verification.zero_constitution_hamiltonian_phase_gate_test import X16,Z16,J16,P16
from verification.zero_reciprocal_subject_exchange_test import n
from verification.zero_five_ray_record_current_unification_test import q,ns,axis

B=[kron(np.eye(8),p,I,I) for p in (-X,-Y,Z)]
CHIB=sum(s*B[i]@D[j]@E[k] for i,j,k,s in eps)/(2*math.sqrt(3))
V=(CHI-CHIB)/2
V2=V@V
SAB=(I64+sum(a@b for a,b in zip(A,B)))/2
G=SAB@SWAP
# Spectrum of V: 0, ±1/sqrt(3), ±1. Polynomials isolate ±1.
COMMON=(3/4)*V2@(V2-I64/3)
VP=COMMON@(I64+V)
VM=COMMON@(I64-V)
U=kron(I64-VM,I)+kron(VM,X)
H=(math.pi/2)*kron(VM,I-X)
GREPORT=kron(G,I)
T=kron(SWAP,X)
# Total SU(2) charges are Pauli-normalized: Casimir 0,8,24.
CAS=sum(c@c for c in C)
PZERO=(CAS-8*I64)@(CAS-24*I64)/192
OLD=(I16+L)@Psing/2
REF=np.outer(SING.reshape(4),SING.reshape(4).conj())
SOURCE=kron(OLD,REF)


class RelativeGaugeInvariantReportTests(unittest.TestCase):
    def test_diagonal_swap_is_trivial_on_the_entire_total_zero_sector(self):
        np.testing.assert_allclose(SAB@SAB,I64,atol=1e-13)
        np.testing.assert_allclose(G@G,I64,atol=1e-13)
        np.testing.assert_allclose(PZERO@PZERO,PZERO,atol=1e-12)
        self.assertAlmostEqual(np.trace(PZERO).real,8,places=12)
        for c in C:np.testing.assert_allclose(c@PZERO,0,atol=1e-12)
        np.testing.assert_allclose(G@PZERO,PZERO,atol=1e-12)
        np.testing.assert_allclose(PZERO@SOURCE,SOURCE,atol=1e-13)
        # The identification is representation-specific; enlarging the
        # physical sector or declaring additional gauge maps changes it.

    def test_relative_sign_is_exactly_gauge_even_and_counterpart_odd(self):
        np.testing.assert_allclose(V,V.conj().T,atol=1e-13)
        np.testing.assert_allclose(G@V@G,V,atol=1e-13)
        np.testing.assert_allclose(SWAP@V@SWAP,-V,atol=1e-13)
        np.testing.assert_allclose(SAB@V@SAB,-V,atol=1e-13)
        np.testing.assert_allclose(V@PZERO,CHI@PZERO,atol=1e-12)
        np.testing.assert_allclose(V2@PZERO,PZERO,atol=1e-12)
        np.testing.assert_allclose(V2@SOURCE,SOURCE,atol=1e-13)
        for c in C:np.testing.assert_allclose(V@c-c@V,0,atol=1e-13)
        np.testing.assert_allclose(V@LL-LL@V,0,atol=1e-13)
        for oldclock in (XL,ZL):
            op=kron(oldclock,I,I)
            np.testing.assert_allclose(V@op-op@V,0,atol=1e-13)
            np.testing.assert_allclose(G@op-op@G,0,atol=1e-13)
        # Relative swap is a separate symmetry from G. Whether a broader
        # gauge group includes it is not fixed by these matrix identities.

    def test_exact_full_space_spectral_projectors_and_report_hamiltonian(self):
        for p in (VP,VM):
            np.testing.assert_allclose(p,p.conj().T,atol=1e-13)
            np.testing.assert_allclose(p@p,p,atol=1e-13)
        np.testing.assert_allclose(VP@VM,0,atol=1e-13)
        np.testing.assert_allclose(VP+VM,PZERO,atol=1e-12)
        for p in (VP,VM):
            self.assertAlmostEqual(np.trace(p).real,4,places=12)
            self.assertAlmostEqual(np.trace(p@(I64+LL)/2).real,2,places=12)
        np.testing.assert_allclose(V@VP,VP,atol=1e-13)
        np.testing.assert_allclose(V@VM,-VM,atol=1e-13)
        np.testing.assert_allclose(VP@SOURCE,PP@SOURCE,atol=1e-13)
        np.testing.assert_allclose(VM@SOURCE,PM@SOURCE,atol=1e-13)
        np.testing.assert_allclose(U.conj().T@U,np.eye(128),atol=1e-13)
        evals,basis=np.linalg.eigh(H)
        np.testing.assert_allclose((basis*np.exp(-1j*evals))@basis.conj().T,U,atol=1e-13)
        for x in (G,*C,LL):
            np.testing.assert_allclose(H@kron(x,I)-kron(x,I)@H,0,atol=1e-13)
            np.testing.assert_allclose(U@kron(x,I)-kron(x,I)@U,0,atol=1e-13)
        # The old gate and new globally G-even gate agree on the ready input
        # for the whole SOURCE, not only a selected pointer probability.
        ready=np.array([1.,0.])
        encoding=np.kron(SOURCE,ready[:,None])
        np.testing.assert_allclose(U@encoding,GATE@encoding,atol=1e-13)

    def test_recorded_opposites_remain_distinguishable_by_gauge_even_effect(self):
        ready=np.array([[1.,0.],[0.,0.]])
        rho=U@kron(SOURCE/2,ready)@U.conj().T
        z=kron(I64,Z);plus=(np.eye(128)+z)/2;minus=(np.eye(128)-z)/2
        rp=plus@rho@plus;rm=minus@rho@minus
        np.testing.assert_allclose(GREPORT@rho@GREPORT,rho,atol=1e-13)
        np.testing.assert_allclose(T@rho@T,rho,atol=1e-13)
        np.testing.assert_allclose(T@rp@T,rm,atol=1e-13)
        np.testing.assert_allclose(GREPORT@z@GREPORT,z,atol=1e-13)
        np.testing.assert_allclose(T@z@T,-z,atol=1e-13)
        np.testing.assert_allclose(T@GREPORT,GREPORT@T,atol=1e-13)
        self.assertAlmostEqual(np.trace(rp).real,.5,places=13)
        self.assertAlmostEqual(np.trace(rm).real,.5,places=13)
        self.assertAlmostEqual((np.trace(z@rp)/np.trace(rp)).real,1,places=13)
        self.assertAlmostEqual((np.trace(z@rm)/np.trace(rm)).real,-1,places=13)
        np.testing.assert_allclose(kron(V,Z)@rho,rho,atol=1e-13)
        # If T were added to the gauge group, Z would become inadmissible;
        # physical distinctness of subjects is not deduced here.

    def test_full_work_realization_including_inactive_states(self):
        # R2 W16 T2 F2 D2 E2. The encoded spin is zero on inactive W.
        aa=[-kron(Z,X16,X),-kron(Z,Z16,X),kron(I,J16,I)]
        support=kron(I,P16,I);full=np.eye(512)
        ap=[kron(a,I,I,I) for a in aa]
        bp=[kron(support,x,I,I) for x in (-X,-Y,Z)]
        dp=[kron(np.eye(64),I,x,I) for x in (X,Y,Z)]
        ep=[kron(np.eye(64),I,I,x) for x in (X,Y,Z)]
        cp=[a+b+d+e for a,b,d,e in zip(ap,bp,dp,ep)]
        chi_a=sum(s*ap[i]@dp[j]@ep[k] for i,j,k,s in eps)/(2*math.sqrt(3))
        chi_b=sum(s*bp[i]@dp[j]@ep[k] for i,j,k,s in eps)/(2*math.sqrt(3))
        value=(chi_a-chi_b)/2
        active=kron(support,I,I,I)
        sab=(full-active)+(active+sum(a@b for a,b in zip(ap,bp)))/2
        swap_de=kron(np.eye(128),(kron(I,I)+sum(kron(x,x) for x in (X,Y,Z)))/2)
        g=sab@swap_de
        np.testing.assert_allclose(sab@sab,full,atol=2e-13)
        np.testing.assert_allclose(g@value@g,value,atol=2e-13)
        np.testing.assert_allclose(value@(full-active),0,atol=1e-13)
        for c in cp:np.testing.assert_allclose(c@value-value@c,0,atol=2e-13)
        for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
            number=sum(np.asarray(n[k]) for k in inds)
            energy=kron(I,number,I,I,I,I)
            np.testing.assert_allclose(energy@value-value@energy,0,atol=1e-13)
        # Pointer/projector functions inherit these commutators. The new
        # reference/pointer/control energy is not included in this ledger.

    def test_actual_code_and_complement_clock_states_lie_in_source(self):
        states=[full_state(4),output(active_base()),output(compressed_spin_base(3)),
                output(compressed_spin_base(9))]
        for state in states:
            for old in relative_read(state,4,labels=(15,0,1)):
                v=initial(old);mass=np.linalg.norm(v)**2
                np.testing.assert_allclose(apply64(SOURCE,v),v,atol=1e-13)
                np.testing.assert_allclose(apply64(V,v),apply64(CHI,v),atol=1e-13)
                tables=[]
                for p in (VP,VM):
                    x=apply64(p,v)
                    self.assertAlmostEqual(np.linalg.norm(x)**2,mass/2,places=12)
                    for c in C:self.assertLess(np.linalg.norm(apply64(c,x)),1e-12)
                    np.testing.assert_allclose(apply64(G,x),x,atol=1e-13)
                    tables.append(np.sum(abs(x)**2,axis=(0,1,2,3,4,5,7,8,9,10,11,12,13)))
                table=np.stack(tables,axis=1)
                np.testing.assert_allclose(table,np.array(q)[:,None]*mass/2*np.ones((1,2)),atol=1e-13)
                d=np.array(ns)@np.array(axis)
                self.assertAlmostEqual(table[d<0].sum()/mass,3/5,places=12)
                self.assertAlmostEqual(np.einsum('is,s->',table,[1,-1]),0,places=13)
                self.assertAlmostEqual(np.einsum('is,i,s->',table,np.sign(d),[1,-1]),0,places=13)
        # Exact source-operator equivalence plus previous full-16-label test
        # carries these statements to every earlier retained clock label.

if __name__=='__main__':unittest.main()
