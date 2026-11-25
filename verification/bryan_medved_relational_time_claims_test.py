"""Exact finite countermodels to overly broad clock/arrow claims.

These are idealized conditional probabilities, not cosmology or experience.
A clock-system joint readout requires a physical interface not supplied here.
"""
import unittest
import numpy as np

N=4
PI=np.pi
omega=2*PI/N
I2=np.eye(2)


def ket(n,sign):
    return np.exp(sign*1j*omega*n*np.arange(N))/2


def reduced(v,axes):
    axes=tuple(axes);rest=tuple(i for i in range(v.ndim) if i not in axes)
    a=np.transpose(v,axes+rest)
    d=np.prod([v.shape[i] for i in axes]);a=a.reshape(d,-1)
    return a@a.conj().T


def entropy(rho):
    vals=np.linalg.eigvalsh(rho);vals=vals[vals>1e-12]
    return -np.sum(vals*np.log2(vals))


def condition(v,n):
    # Unnormalized conditional vector on the rest, clock axis first.
    return np.tensordot(ket(n,1).conj(),v,axes=(0,0))


def disjoint_clock_history():
    # C and S have opposite energy spectra; E is an idle 8-state spectator.
    # No interactions whatsoever, dim(C)=dim(S)=4, dim(R)=4*8=32.
    v=np.zeros((4,4,8),complex)
    for k in range(4):v[k,k,0]=.5
    return v


def ghz_history():
    # Clock basis has + phases, two remaining systems have - phases.
    # The rest has an S-E modular interaction; C remains fully isolated.
    return sum(np.einsum('i,j,k->ijk',ket(n,1),ket(n,-1),ket(n,-1))
               for n in range(4))/2


def cnot():
    u=np.zeros((4,4),complex)
    for x in range(2):
        for y in range(2):u[2*x+(y^x),2*x+y]=1
    return u


def oscillating_history():
    # H_R=pi/2 (I-CNOT), so exp(-i H_R)=CNOT; no external bath.
    u=cnot();init=np.array([1,0,1,0],complex)/np.sqrt(2)
    states=[np.linalg.matrix_power(u,n)@init for n in range(4)]
    history=sum(np.outer(ket(n,1),states[n]) for n in range(4))/2
    return history.reshape(4,2,2),states


class BryanMedvedRelationalTimeClaimsTests(unittest.TestCase):
    def test_no_finite_exact_canonical_clock_commutator(self):
        h=-omega*np.diag(np.arange(4))
        u=np.array([ket(n,1) for n in range(4)]).T
        t=u@np.diag(np.arange(4))@u.conj().T
        comm=h@t-t@h
        self.assertAlmostEqual(np.trace(comm).real,0,places=12)
        self.assertAlmostEqual(np.trace(comm).imag,0,places=12)
        self.assertGreater(np.linalg.norm(comm-1j*np.eye(4)),1)
        np.testing.assert_allclose(u.conj().T@u,np.eye(4),atol=1e-13)

    def test_isolated_clock_and_small_part_have_sharp_conditionals(self):
        v=disjoint_clock_history()
        constraint=(-np.arange(4)[:,None,None]+np.arange(4)[None,:,None])*omega
        np.testing.assert_allclose(constraint*v,0,atol=1e-13)
        self.assertAlmostEqual(norm(v),1,places=12)
        rho_c=reduced(v,(0,));self.assertAlmostEqual(entropy(rho_c),2,places=12)
        self.assertEqual(v.shape[0],4);self.assertEqual(v.shape[1]*v.shape[2],32)
        self.assertEqual(v.shape[1],4)
        np.testing.assert_allclose(reduced(v,(1,)),np.eye(4)/4,atol=1e-13)
        for n in range(4):
            ce=condition(v,n)
            self.assertAlmostEqual(norm(ce),.25,places=12)
            target=np.outer(ket(n,-1),np.eye(8)[0])/2
            np.testing.assert_allclose(ce,target,atol=1e-13)
            # S time-basis outcome n conditional on C=n has probability one.
            amp=ket(n,-1).conj()@ce
            self.assertAlmostEqual(norm(amp)/norm(ce),1,places=12)

    def test_classically_correlated_local_record_with_max_entangled_whole(self):
        v=ghz_history()
        self.assertAlmostEqual(norm(v),1,places=12)
        a=np.arange(4)
        constraint=(-a[:,None,None]+(a[None,:,None]+a[None,None,:])%4)*omega
        np.testing.assert_allclose(constraint*v,0,atol=1e-13)
        self.assertAlmostEqual(entropy(reduced(v,(0,))),2,places=12)
        # Separable decomposition of C-S; no C-S entanglement.
        rho_cs=reduced(v,(0,1))
        mixture=np.zeros((16,16),complex)
        for n in range(4):
            a=np.kron(ket(n,1),ket(n,-1))
            mixture+=np.outer(a,a.conj())/4
            ce=condition(v,n)
            target=np.outer(ket(n,-1),ket(n,-1))/2
            np.testing.assert_allclose(ce,target,atol=1e-13)
            self.assertAlmostEqual(norm(ket(n,-1).conj()@ce)/norm(ce),1,places=12)
        np.testing.assert_allclose(rho_cs,mixture,atol=1e-13)
        rho_s=reduced(v,(1,));np.testing.assert_allclose(rho_s,np.eye(4)/4,atol=1e-13)
        self.assertAlmostEqual(entropy(rho_s),2,places=12)
        self.assertAlmostEqual(entropy(rho_cs),2,places=12)
        # C-S mutual information=2 bits, purely classical in this basis.
        self.assertAlmostEqual(entropy(reduced(v,(0,)))+entropy(rho_s)-entropy(rho_cs),2,places=12)

    def test_closed_interaction_has_reversible_record_and_nonmonotone_entropy(self):
        v,states=oscillating_history();u=cnot()
        h=(PI/2)*(np.eye(4)-u)
        total=np.kron(-omega*np.diag(np.arange(4)),np.eye(4))+np.kron(np.eye(4),h)
        np.testing.assert_allclose(total@v.reshape(-1),0,atol=1e-12)
        np.testing.assert_allclose(u@u,np.eye(4),atol=1e-13)
        ent=[]
        for n in range(4):
            target=states[n].reshape(2,2)
            actual=condition(v,n)
            np.testing.assert_allclose(actual,target/2,atol=1e-13)
            ent.append(entropy(reduced(target,(0,))))
        np.testing.assert_allclose(ent,[0,1,0,1],atol=1e-12)
        self.assertAlmostEqual(entropy(reduced(v,(0,1,2))),0,places=12)
        # Closed pure whole and cyclic conditional entropy are not heat data.

    def test_reset_exports_entropy_to_a_blank_ancilla(self):
        # Reset an unknown unbiased bit by swapping it with a pure blank.
        swap=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]],complex)
        blank=np.diag([1,0]);mixed=np.eye(2)/2
        before=np.kron(mixed,blank);after=swap@before@swap.conj().T
        np.testing.assert_allclose(after,np.kron(blank,mixed),atol=1e-13)
        self.assertAlmostEqual(entropy(before),entropy(after),places=12)
        self.assertAlmostEqual(entropy(mixed)-entropy(blank),1,places=12)
        # Total entropy is conserved, with one bit moved into the ancilla.
        # No bath temperature or heat is specified in this circuit.

    def test_simple_history_has_no_clock_rest_hamiltonian_interaction(self):
        # H = H_C⊗I + I⊗H_S⊗I_E. A stationary global state, not a
        # derivation that every isolated closed state is stationary.
        v=disjoint_clock_history()
        self.assertAlmostEqual(norm(v),1,places=12)
        for n in range(4):
            e=np.exp(-1j*omega*n*np.arange(4))
            np.testing.assert_allclose(ket(n,-1),e/2,atol=1e-13)
            np.testing.assert_allclose(np.einsum('s,se->se',e,condition(v,0)),
                                       condition(v,n),atol=1e-13)


def norm(v):return np.vdot(v,v).real

if __name__=='__main__':unittest.main()
