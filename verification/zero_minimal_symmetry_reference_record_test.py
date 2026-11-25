"""Minimal invariant reference and constrained parity-pairing record dynamics.

The real structure, representations, parity-flipping coupling and factorization
are hypotheses, not consequences of zero. No claim of objective energy,
spacetime locality, subjective experience or actual incidence is made.
"""
import math
import unittest
import numpy as np
from verification.zero_energy_sphere_work_incidence_test import X,Y,Z,I
from verification.zero_invariant_all_history_record_clock_test import kron
from verification.zero_covariant_pairing_reference_history_test import GROUP,DS,V

I4=np.eye(4,dtype=complex)
I8=np.eye(8,dtype=complex)
I16=np.eye(16,dtype=complex)
P=X
R=[]
for d in DS:
    sign=round(np.linalg.det(d).real)
    R.append(kron(d.conj(),I if sign==1 else P,d))
PG=sum(R)/24
Qsym=I8-PG
Xp=kron(I,X,I)
Qp=(I8-Xp)/2
H=kron(I,Y,Y)

bell=np.zeros(8,complex)
# Canonical maximally entangled multiplicity reference–spin, parity in |+X>.
for r in range(2):
    for p in range(2):bell[(r*2+p)*2+r]=.5

# Singlet-multiplicity correlation projector on R⊗spin, parity untouched.
Pcorr=np.zeros((8,8),complex)
for p in range(2):
    v=np.zeros(8,complex)
    for r in range(2):v[(r*2+p)*2+r]=1/math.sqrt(2)
    Pcorr+=np.outer(v,v.conj())
Qcorr=I8-Pcorr

W=np.vstack(((I8+H)/2,(I8-H)/2))
Cclock=kron(I,H)-kron(Z,I8)
Qclock=Cclock@Cclock/4
Dressed=W@Qp@W.conj().T
Hwhole=Qclock+kron(I,Qsym)+Dressed


def evo(theta):return math.cos(theta)*bell-1j*math.sin(theta)*(H@bell)

def joint(v):
    return np.array([[np.vdot(v,(I8-Qp)@(I8-Qcorr)@v).real,
                      np.vdot(v,(I8-Qp)@Qcorr@v).real],
                     [np.vdot(v,Qp@(I8-Qcorr)@v).real,
                      np.vdot(v,Qp@Qcorr@v).real]])


def hermitian_constraint_matrix(reality):
    # General Hermitian 4x4 on parity⊗spin has real Pauli coefficients.
    # Constraints: invariance, anticommute with Xp, optionally KHK=H.
    basis=[kron(a,b) for a in (I,X,Y,Z) for b in (I,X,Y,Z)]
    cols=[]
    for h in basis:
        pieces=[]
        for d in DS:
            s=round(np.linalg.det(d).real)
            u=kron(I if s==1 else X,d)
            pieces.append((h@u-u@h).ravel())
        pieces.append((h@kron(X,I)+kron(X,I)@h).ravel())
        if reality:pieces.append((h-h.conj()).ravel())
        vec=np.concatenate(pieces)
        cols.append(np.concatenate((vec.real,vec.imag)))
    return np.array(cols).T


class MinimalSymmetryReferenceRecordTests(unittest.TestCase):
    def test_real_irrep_and_exact_two_copy_invariant_sector(self):
        self.assertEqual(V.shape,(16,2))
        for d in DS:
            np.testing.assert_allclose(d.imag,0,atol=1e-14)
            np.testing.assert_allclose(d.T@d,I,atol=1e-14)
        np.testing.assert_allclose(PG@PG,PG,atol=1e-14)
        self.assertAlmostEqual(np.trace(PG).real,2,places=12)
        np.testing.assert_allclose(PG@bell,bell,atol=1e-14)
        self.assertEqual(np.count_nonzero(abs(np.linalg.eigvalsh(Qsym+Qp))<1e-10),1)
        # The real S4 singlet multiplicity is irreducible: its commutant is
        # scalar. Thus each equivalent reference copy adds one invariant ray.
        a=np.vstack([np.kron(I,d)-np.kron(d.T,I) for d in DS])
        self.assertEqual(np.linalg.matrix_rank(a,tol=1e-10),3)

    def test_unique_interaction_from_explicit_symmetry_hypotheses(self):
        # Real coefficients parameterize all Hermitian 4x4 matrices.
        self.assertEqual(np.linalg.matrix_rank(hermitian_constraint_matrix(False),tol=1e-10),14)
        self.assertEqual(np.linalg.matrix_rank(hermitian_constraint_matrix(True),tol=1e-10),15)
        np.testing.assert_allclose(H,H.conj(),atol=1e-14)
        np.testing.assert_allclose(H@H,I8,atol=1e-14)
        np.testing.assert_allclose(H@Xp,-Xp@H,atol=1e-14)
        for u in R:np.testing.assert_allclose(H@u,u@H,atol=1e-14)
        # The sole real, invariant, parity-flipping Hermitian interaction on
        # parity⊗spin is proportional to Yp⊗Ys. No uniqueness is claimed if
        # factorization, the K-real structure, or the flip condition is dropped.

    def test_stationary_zero_and_prior_spin_embedding(self):
        np.testing.assert_allclose(W.conj().T@W,I8,atol=1e-14)
        np.testing.assert_allclose(Cclock@W,0,atol=1e-14)
        for u in R:np.testing.assert_allclose(H@u,u@H,atol=1e-14)
        for a in (Qclock,kron(I,Qsym),Dressed):
            np.testing.assert_allclose(a@a,a,atol=1e-14)
        for a,b in ((Qclock,kron(I,Qsym)),(Qclock,Dressed),(kron(I,Qsym),Dressed)):
            np.testing.assert_allclose(a@b,b@a,atol=1e-14)
        vals=np.linalg.eigvalsh(Hwhole)
        self.assertEqual(np.count_nonzero(abs(vals)<1e-10),1)
        self.assertAlmostEqual(vals[1],1,places=12)
        np.testing.assert_allclose(Hwhole@W@bell,0,atol=1e-14)
        for u in R:np.testing.assert_allclose(kron(I,u)@W@bell,W@bell,atol=1e-14)
        # V was explicitly embedded into the previous C_i=0 logical kernel
        # in zero_covariant_pairing_reference_history_test.

    def test_invariant_record_is_exact_and_nontrivial(self):
        np.testing.assert_allclose(Qp@Qcorr,Qcorr@Qp,atol=1e-14)
        for u in R:
            for q in (Qp,Qcorr):np.testing.assert_allclose(q@u,u@q,atol=1e-14)
        for theta in (0,math.pi/8,math.pi/4,math.pi/2):
            v=evo(theta)
            for u in R:np.testing.assert_allclose(u@v,v,atol=1e-14)
            np.testing.assert_allclose(joint(v),np.diag([math.cos(theta)**2,math.sin(theta)**2]),atol=1e-14)
            # spin reduction is always maximally mixed; correlation is relational
            a=v.reshape(4,2)
            np.testing.assert_allclose(a.T@a.conj(),I/2,atol=1e-14)
        # At pi/4 this binary pair has one bit of mutual information.

    def test_stationary_unselected_whole_retains_record_correlation(self):
        state=W@bell
        a=state.reshape(2,8)
        rho=a.T@a.conj()
        table=np.array([[np.trace(rho@(I8-Qp)@(I8-Qcorr)).real,
                         np.trace(rho@(I8-Qp)@Qcorr).real],
                        [np.trace(rho@Qp@(I8-Qcorr)).real,
                         np.trace(rho@Qp@Qcorr).real]])
        np.testing.assert_allclose(table,np.diag([.5,.5]),atol=1e-14)
        for theta in (0,math.pi/4,math.pi/2):
            bra=np.array([np.exp(-1j*theta),np.exp(1j*theta)])/math.sqrt(2)
            np.testing.assert_allclose(kron(bra.reshape(1,2),I8)@state,evo(theta)/math.sqrt(2),atol=1e-14)
        # One bit in the unselected joint readout, not a permanent record.

    def test_drop_reality_and_frozen_control(self):
        # The other symmetry-allowed flip is imaginary, Zp⊗Ys; it becomes
        # available when the chosen K-real structure is not imposed.
        alternate=kron(I,Z,Y)
        self.assertGreater(np.linalg.norm(alternate-alternate.conj()),1)
        for u in R:np.testing.assert_allclose(alternate@u,u@alternate,atol=1e-14)
        np.testing.assert_allclose(alternate@Xp,-Xp@alternate,atol=1e-14)
        # An invariant K-real non-flipping Hamiltonian exists; symmetry plus
        # reality alone does not entail the parity-flipping condition.
        frozen=Xp
        for u in R:np.testing.assert_allclose(frozen@u,u@frozen,atol=1e-14)
        np.testing.assert_allclose(frozen@bell,bell,atol=1e-14)
        self.assertGreater(np.linalg.norm(frozen@Xp+Xp@frozen),1)

if __name__=='__main__':unittest.main()
