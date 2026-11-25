"""Derive a balanced parity exchange under explicit structural hypotheses.

Charges, conjugation, representations, bilinearity, nonzero coupling and the
zero-sector seed are inputs. This is not a cosmic energy or experience model.
"""
import math
import unittest
import numpy as np
from verification.zero_energy_sphere_work_incidence_test import X,Y,Z,I
from verification.zero_invariant_all_history_record_clock_test import kron
from verification.zero_covariant_pairing_reference_history_test import DS

I8=np.eye(8,dtype=complex)
I16=np.eye(16,dtype=complex)
I32=np.eye(32,dtype=complex)
# Physical order R, parity P, compensator Q, zero-spin multiplicity V.
XP=kron(I,X,I,I)
XQ=kron(I,I,X,I)
CHARGE=XP+XQ
P0=(I16-XP@XQ)/2
Qcharge=I16-P0
Kunit=kron(I,I,X,I) # antiunitary Θ=Kunit * complex conjugation
H=kron(I,(kron(Y,Y)+kron(Z,Z))/2,Y)
GROUP=[]
for d in DS:
    GROUP.append(kron(d.conj(),I if round(np.linalg.det(d).real)==1 else X,I,d))
PG=sum(GROUP)/24
Qsym=I16-PG
Qp=(I16-XP)/2
Qq=(I16+XQ)/2

# |Φ>_RV, |+>_P, |−>_Q in R,P,Q,V order.
psi=np.einsum('rv,p,q->rpqv',I/math.sqrt(2),
              np.array([1,1])/math.sqrt(2),np.array([1,-1])/math.sqrt(2)).reshape(-1)
Pcorr=np.zeros((16,16),complex)
for p in range(2):
    for q in range(2):
        v=np.zeros(16,complex)
        for r in range(2):v[((r*2+p)*2+q)*2+r]=1/math.sqrt(2)
        Pcorr+=np.outer(v,v.conj())
Qcorr=I16-Pcorr

# Partial history isometry on Q=0; non-neutral input is annihilated.
W=np.vstack(((P0+H)/2,(P0-H)/2))
Cclock=kron(I,H)-kron(Z,I16)
Qclock=kron(I,P0)@Cclock@Cclock/4
Qb=kron(I,Qcharge)
Qs=kron(I,Qsym)
Qready=W@Qp@W.conj().T
Hwhole=Qb+Qs+Qclock+Qready


def theta(x):return Kunit@x.conj()@Kunit.conj().T

def evolved(t):return math.cos(t)*psi-1j*math.sin(t)*(H@psi)

def table(v,a,b):
    return np.array([[np.vdot(v,(I16-a)@(I16-b)@v).real,np.vdot(v,(I16-a)@b@v).real],
                     [np.vdot(v,a@(I16-b)@v).real,np.vdot(v,a@b@v).real]])


def constraint_matrix(antiunitary):
    # All Hermitian P–Q bilinear terms with arbitrary V Pauli factor.
    basis=[kron(a,b,c) for a in (X,Y,Z) for b in (X,Y,Z) for c in (I,X,Y,Z)]
    q=kron(X,I,I)+kron(I,X,I)
    t=kron(I,X,I)
    cols=[]
    for h in basis:
        pieces=[]
        for d in DS:
            u=kron(I if round(np.linalg.det(d).real)==1 else X,I,d)
            pieces.append((h@u-u@h).ravel())
        pieces.append((h@q-q@h).ravel())
        if antiunitary:pieces.append((h-t@h.conj()@t).ravel())
        x=np.concatenate(pieces)
        cols.append(np.r_[x.real,x.imag])
    return np.array(cols).T


class NeutralExchangeFromBalanceTests(unittest.TestCase):
    def test_two_invariant_bilinears_and_one_nonscalar_neutral_dynamics(self):
        self.assertEqual(np.linalg.matrix_rank(constraint_matrix(False),tol=1e-10),33)
        self.assertEqual(np.linalg.matrix_rank(constraint_matrix(True),tol=1e-10),34)
        diag=XP@XQ
        for op in (H,diag):
            for u in GROUP:np.testing.assert_allclose(op@u,u@op,atol=1e-14)
            np.testing.assert_allclose(op@CHARGE,CHARGE@op,atol=1e-14)
            np.testing.assert_allclose(theta(op),op,atol=1e-14)
        np.testing.assert_allclose(P0@diag@P0,-P0,atol=1e-14)
        np.testing.assert_allclose(H@H,P0,atol=1e-14)
        # Complete 36-dimensional Hermitian bilinear solve leaves exactly
        # span{Xp Xq, (Yp Yq + Zp Zq) Yv}; first is scalar on Q=0.

    def test_balanced_exchange_is_derived_from_commutation_not_imposed(self):
        np.testing.assert_allclose(H@CHARGE,CHARGE@H,atol=1e-14)
        np.testing.assert_allclose(H@XP,-XP@H,atol=1e-14)
        np.testing.assert_allclose(H@XQ,-XQ@H,atol=1e-14)
        np.testing.assert_allclose(CHARGE@psi,0,atol=1e-14)
        np.testing.assert_allclose(PG@psi,psi,atol=1e-14)
        np.testing.assert_allclose(theta(H),H,atol=1e-14)
        # Θ reverses the unitary phase; it is specified, not a derived
        # physical time reversal on the original full lab.
        for t in (.2,math.pi/4,math.pi/2):
            np.testing.assert_allclose(CHARGE@evolved(t),0,atol=1e-14)
            np.testing.assert_allclose(Kunit@evolved(t).conj(),-evolved(-t),atol=1e-14)

    def test_same_symmetries_permit_no_transfer_and_reality_matters(self):
        frozen=XP@XQ
        np.testing.assert_allclose(frozen@psi,-psi,atol=1e-14)
        np.testing.assert_allclose(theta(frozen),frozen,atol=1e-14)
        # Another neutral exchange is allowed when the antiunitary condition
        # is dropped, so it is a genuine extra restriction.
        other=kron(I,(kron(Y,Z)-kron(Z,Y))/2,Y)
        np.testing.assert_allclose(other@CHARGE,CHARGE@other,atol=1e-14)
        for u in GROUP:np.testing.assert_allclose(other@u,u@other,atol=1e-14)
        np.testing.assert_allclose(theta(other),-other,atol=1e-14)
        self.assertGreater(np.linalg.norm(other),1)

    def test_exact_stationary_whole_and_charged_outside_states(self):
        np.testing.assert_allclose(W.conj().T@W,P0,atol=1e-14)
        np.testing.assert_allclose(Cclock@W,0,atol=1e-14)
        ps=(Qb,Qs,Qclock,Qready)
        for a in ps:
            np.testing.assert_allclose(a@a,a,atol=1e-14)
            np.testing.assert_allclose(a,a.conj().T,atol=1e-14)
        for i,a in enumerate(ps):
            for b in ps[i+1:]:np.testing.assert_allclose(a@b,b@a,atol=1e-14)
        vals=np.linalg.eigvalsh(Hwhole)
        self.assertEqual(np.count_nonzero(abs(vals)<1e-10),1)
        self.assertAlmostEqual(vals[1],1,places=12)
        whole=W@psi
        np.testing.assert_allclose(Hwhole@whole,0,atol=1e-14)
        np.testing.assert_allclose(kron(I,CHARGE)@whole,0,atol=1e-14)
        np.testing.assert_allclose(Cclock@whole,0,atol=1e-14)
        for u in GROUP:np.testing.assert_allclose(kron(I,u)@whole,whole,atol=1e-14)

    def test_both_charge_signs_and_joint_record_through_the_history(self):
        for t in (0,math.pi/8,math.pi/4,math.pi/2,math.pi):
            v=evolved(t)
            np.testing.assert_allclose(CHARGE@v,0,atol=1e-14)
            for u in GROUP:np.testing.assert_allclose(u@v,v,atol=1e-14)
            expected=np.diag([math.cos(t)**2,math.sin(t)**2])
            np.testing.assert_allclose(table(v,Qp,Qq),expected,atol=1e-14)
            np.testing.assert_allclose(table(v,Qp,Qcorr),expected,atol=1e-14)
        # Individual signed Xp and Xq are opposite in every branch, while
        # the correlation flag Qcorr is a nonlocal R–V comparison.

    def test_unselected_stationary_clock_retains_exact_one_bit_record(self):
        whole=W@psi
        a=whole.reshape(2,16)
        rho=a.T@a.conj()
        for x,y in ((Qp,Qq),(Qp,Qcorr)):
            t=np.array([[np.trace(rho@(I16-x)@(I16-y)).real,np.trace(rho@(I16-x)@y).real],
                        [np.trace(rho@x@(I16-y)).real,np.trace(rho@x@y).real]])
            np.testing.assert_allclose(t,np.diag([.5,.5]),atol=1e-14)
        for t in (0,math.pi/4,math.pi/2):
            bra=np.array([np.exp(-1j*t),np.exp(1j*t)])/math.sqrt(2)
            np.testing.assert_allclose(kron(bra.reshape(1,2),I16)@whole,evolved(t)/math.sqrt(2),atol=1e-14)

if __name__=='__main__':unittest.main()
