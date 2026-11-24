"""Branchwise balance and a conditional stabilizer selection in the all-sector circuit.

All R,W,T matrices describe stipulated finite quantum registers. The extra
Hamiltonian is a constructed candidate, not the original circuit Hamiltonian
or a derivation of objective whole energy, actuality, or experience.
"""
import math
import unittest
import numpy as np
from verification.zero_energy_sphere_work_incidence_test import (
    X, Z, Jactive, full_state, relative_read, project_h,
    embed_records_and_work, target_memory
)
from verification.zero_all_sector_sphere_clock_work_test import complement_state
from verification.zero_dual_pair_sphere_energy_instrument_test import dual_output
from verification.zero_reciprocal_subject_exchange_test import J, proj, n
from verification.zero_all_sector_record_involution_test import transform

I2=np.eye(2,dtype=complex)
I8=np.eye(8,dtype=complex)
J16=np.asarray(J[0],complex)
P16=np.asarray(proj,complex)
V16=np.eye(16,dtype=complex)-P16
V16[6,9]=V16[9,6]=1
U8=-np.kron(np.kron(Z,X),X)
L8=np.kron(np.kron(Z,Jactive),Z)
Q8=np.kron(np.kron(I2,Jactive),I2)-np.kron(np.kron(Z,I2),Z)
U64=-np.kron(np.kron(Z,V16),X)
L64=np.kron(np.kron(Z,J16),Z)
Q64=np.kron(np.kron(I2,J16),I2)-np.kron(np.kron(Z,P16),Z)
PACT=np.kron(np.kron(I2,P16),I2)
H64=(np.eye(64)-L64)/2+(np.eye(64)-U64)/2


def apply(op,v):
    rwt=v.shape[-3:]
    assert rwt==(2,2,2)
    return np.einsum('xy,...y->...x',op,v.reshape(v.shape[:-3]+(8,)),optimize=True).reshape(v.shape)


def conditional_rho_work_target(vs,r):
    out=np.zeros((4,4),complex)
    for v in vs:
        a=v[...,r,:,:].reshape(-1,4).T
        out+=a@a.conj().T
    return out


def branch_prob(v,r,j):
    # j=±1 is a sharp J measurement, r indexes Z_R = ±1. T is read out
    # explicitly, so we can verify the opposite value of -Z_R Z_T.
    work_effect=(I2+j*Jactive)/2
    x=np.einsum('wu,...ut->...wt',work_effect,v[...,r,:,:],optimize=True)
    return np.sum(abs(x)**2,axis=tuple(range(x.ndim-1)))


class AllSectorBranchwiseBalanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.code=full_state(4)
        cls.comp=complement_state(4)
        cls.clock=[[x for x in relative_read(v,4,labels=tuple(range(16)))]
                   for v in (cls.code,cls.comp)]

    def test_full_physical_opposites_and_involution(self):
        a=np.kron(np.kron(I2,J16),I2)
        b=-np.kron(np.kron(Z,P16),Z)
        np.testing.assert_allclose(a@b,b@a,atol=1e-14)
        np.testing.assert_allclose(a@a,PACT,atol=1e-14)
        np.testing.assert_allclose(b@b,PACT,atol=1e-14)
        np.testing.assert_allclose(Q64,a+b,atol=1e-14)
        np.testing.assert_allclose(Q64@Q64,2*(PACT-L64),atol=1e-14)
        for op in (a,b,Q64):
            np.testing.assert_allclose(U64@op@U64,-op,atol=1e-14)
        np.testing.assert_allclose(U64@U64,np.eye(64),atol=1e-14)
        # Both terms have nonzero ±1 outcomes on active work. B requires
        # access to R and T; it is not asserted available to either alone.

    def test_exact_balance_and_symmetry_all_sectors_and_clock_labels(self):
        for v,vs in zip((self.code,self.comp),self.clock):
            for x in [v]+vs:
                np.testing.assert_allclose(apply(Q8,x),0,atol=2e-14)
                np.testing.assert_allclose(apply(L8,x),x,atol=2e-14)
                np.testing.assert_allclose(apply(U8,x),x,atol=2e-14)
                np.testing.assert_allclose(transform(x),x,atol=2e-14)
        # Orthogonal physical code/complement embeddings are fixed by these
        # same operators, so a coherent sum also satisfies both identities.

    def test_each_joint_branch_has_nonzero_opposites_and_equal_weights(self):
        for vs in self.clock:
            for v in vs:
                for r in (0,1):
                    sign=1-2*r
                    jp=branch_prob(v,r,1)
                    jm=branch_prob(v,r,-1)
                    # On support: J = r Z_T, hence B=-r Z_T=-J.
                    self.assertAlmostEqual(jp[(1+sign)//2],0,places=14)
                    self.assertAlmostEqual(jm[(1-sign)//2],0,places=14)
                    self.assertAlmostEqual(jp.sum(),jm.sum(),places=14)
            # Window event r=+, T=1 has J=-1 and B=+1.
            window=[vs[k] for k in (15,0,1)]
            p=sum(branch_prob(v,0,-1)[1] for v in window)
            self.assertAlmostEqual(p,3/64,places=13)
            self.assertAlmostEqual(sum(branch_prob(v,0,1)[1] for v in window),0,places=14)

    def test_complete_selection_on_physical_full_work_space(self):
        np.testing.assert_allclose(U64@L64,L64@U64,atol=1e-14)
        np.testing.assert_allclose(H64,H64.conj().T,atol=1e-14)
        vals=np.linalg.eigvalsh(H64)
        expected=np.array([0]*2+[.5]*28+[1]*4+[1.5]*28+[2]*2)
        np.testing.assert_allclose(vals,expected,atol=1e-13)
        # The physical work-number charges and declared lab charges are
        # preserved: H acts trivially on the labs, R and T are neutral.
        nums=np.asarray(n,complex)
        for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
            number=sum(nums[k] for k in inds)
            charge=np.kron(np.kron(I2,number),I2)
            np.testing.assert_allclose(H64@charge,charge@H64,atol=1e-14)
        # If imposed, the candidate selects a 2D ground space; it is not
        # identified with the originally specified whole-energy charge.

    def test_zero_kernel_plus_involution_uniquely_selects_wt_at_fixed_r(self):
        P=(I8+U8)@(I8+L8)/4
        np.testing.assert_allclose(P@P,P,atol=1e-14)
        self.assertAlmostEqual(np.trace(P).real,2,places=13)
        for r in (0,1):
            sub=P[r*4:(r+1)*4,r*4:(r+1)*4]
            self.assertAlmostEqual(np.trace(sub).real,1,places=13)
            vals,vec=np.linalg.eigh(sub)
            phi=vec[:,-1].reshape(2,2)
            np.testing.assert_allclose(np.linalg.svd(phi,compute_uv=False),
                                       [1/math.sqrt(2)]*2,atol=1e-14)
            # With R fixed, the surviving W-T vector is unique up to phase
            # and maximally entangled. The full R/environment state remains
            # free and need not be selected by these two conditions.
            for vs in self.clock:
                rho=conditional_rho_work_target(vs,r)
                p=np.trace(rho).real
                self.assertGreater(p,.1)
                np.testing.assert_allclose(rho/p,sub,atol=1e-13)

    def test_state_symmetry_as_density_does_not_select_plus_eigenspace(self):
        # U-invariant density allows both + and - U eigenvectors satisfying
        # L=+1. Their U measurement distinguishes them, although their
        # individual work and target reductions coincide at fixed r.
        plus=(I8+U8)@(I8+L8)/4
        minus=(I8-U8)@(I8+L8)/4
        for r in (0,1):
            states=[]
            for p,sign in ((plus,1),(minus,-1)):
                block=p[r*4:(r+1)*4,r*4:(r+1)*4]
                states.append(block)
                self.assertAlmostEqual(np.trace(block).real,1,places=13)
                embed=np.zeros((8,8),complex)
                embed[r*4:(r+1)*4,r*4:(r+1)*4]=block
                np.testing.assert_allclose(U8@embed@U8,embed,atol=1e-14)
                self.assertAlmostEqual(np.trace(U8@embed).real,sign,places=13)
            self.assertAlmostEqual(np.trace(states[0]@states[1]).real,0,places=13)
            for rho in states:
                self.assertAlmostEqual(np.trace(rho@np.kron(Jactive,I2)).real,0,places=13)
                self.assertAlmostEqual(np.trace(rho@np.kron(I2,Z)).real,0,places=13)

    def test_branchwise_balance_is_built_by_the_gate_not_initially_conserved(self):
        # Before target interaction, the alpha pulse acts while T=0, taking
        # the system away from Q=0. The target operation then restores it.
        for angle in (0,math.pi/8,math.pi/4):
            v=embed_records_and_work(dual_output(4,4),angle)
            post=target_memory(v,math.pi/2)
            self.assertAlmostEqual(np.linalg.norm(apply(Q8,v))**2,
                                   4*math.sin(angle)**2,places=12)
            self.assertAlmostEqual(np.vdot(v,apply(U8,v)).real,0,places=12)
            self.assertLess(np.linalg.norm(apply(Q8,post)),1e-12)
            self.assertAlmostEqual(np.vdot(post,apply(U8,post)).real,
                                   math.sin(2*angle),places=12)
        # At alpha=pi/4 the target gate changes <U> from 0 to 1, so it
        # cannot commute with U as a whole. A final zero of Q is not a
        # universal conservation law for the given dynamics. The added
        # selection Hamiltonian is not a ground-state-preparation mechanism.

if __name__=='__main__':
    unittest.main()
