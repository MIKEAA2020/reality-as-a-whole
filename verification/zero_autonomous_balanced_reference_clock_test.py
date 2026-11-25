"""One autonomous finite-clock realization of balanced reference preparation.

A perfect-transfer program clock drives the previous E,D,T gates. A separate
finite reference clock gives exact relational conditioning on a stationary
constraint state. Both clocks, couplings and input state are stipulated. The
constraint is not asserted to be objective cosmic energy or subjecthood.
"""
import math
import unittest
import numpy as np
from verification.zero_energy_sphere_work_incidence_test import I
from verification.zero_dual_pair_sphere_energy_instrument_test import dual_output
from verification.zero_balanced_reference_preparation_test import (
    E,D,T,balanced_seed,complement_base,prepare,clock_read,physical_operators
)
from verification.zero_relational_orientation_reference_test import (
    Qori,C1,S,apply16
)
from verification.zero_reciprocal_subject_exchange_test import n

I16=np.eye(16,dtype=complex)
I64=np.eye(64,dtype=complex)
COUPLINGS=np.array([math.sqrt(3)/2,1.,math.sqrt(3)/2])
JX=np.zeros((4,4),complex)
for i,c in enumerate(COUPLINGS):
    JX[i,i+1]=JX[i+1,i]=c
GATES=(E,D,T)
HISTORIES=(I16,E,D@E,T@D@E)
V=np.zeros((64,64),complex)
for i,g in enumerate(HISTORIES):V[16*i:16*(i+1),16*i:16*(i+1)]=g
H=V@np.kron(JX,I16)@V.conj().T
EVALS,EVECS=np.linalg.eigh(JX)
PROJECTIONS=[V@np.kron(np.outer(EVECS[:,k],EVECS[:,k].conj()),I16)@V.conj().T
             for k in range(4)]
# Reference index precedes (program clock, internal circuit) axes.
W=np.vstack(PROJECTIONS)
CONSTRAINT=np.kron(np.eye(4),H)-np.kron(np.diag(EVALS),I64)


def propagator(t):
    phases=(EVECS*np.exp(-1j*EVALS*t))@EVECS.conj().T
    return V@np.kron(phases,I16)@V.conj().T


def ref_contraction(t):
    # <t| = (1/2) Σ exp(-i E_k t) <k|.  With POVM density
    # 4|t><t|/(2π), normalized conditional evolution is exp(-itH).
    bra=np.exp(-1j*EVALS*t)/2
    return np.kron(bra.reshape(1,4),I64)@W


def amplitudes(t):
    return (EVECS*np.exp(-1j*EVALS*t))@EVECS.conj().T[:,0]


def state_history(seed):
    return [seed,apply16(E,seed),apply16(D@E,seed),prepare(seed)]


def projector_window_success(delta):
    return (10+15*math.sin(delta)/delta+3*math.sin(2*delta)/delta+
            math.sin(3*delta)/(3*delta))/32


def matrix_weighted_distance(hist,weights):
    # Trace distance between Σ p_i |ψ_i><ψ_i| and |ψ_3><ψ_3| via the
    # nonzero eigenvalues of the 5x5 Gram compression; vectors may be large.
    cols=np.stack([math.sqrt(weights[i])*hist[i].ravel() for i in range(4)]+
                  [hist[3].ravel()],axis=1)
    gram=cols.conj().T@cols
    vals,U=np.linalg.eigh(gram)
    root=(U*np.sqrt(np.maximum(vals,0)))@U.conj().T
    diff=root@np.diag([1,1,1,1,-1])@root
    return float(np.sum(abs(np.linalg.eigvalsh(diff)))/2)


class AutonomousBalancedReferenceClockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bases=(dual_output(4,4),complement_base())
        cls.seeds=[balanced_seed(base) for base in cls.bases]
        cls.hist=[state_history(x) for x in cls.seeds]

    def test_program_hamiltonian_is_autonomous_hermitian_and_universal(self):
        np.testing.assert_allclose(V.conj().T@V,I64,atol=1e-13)
        np.testing.assert_allclose(H.conj().T,H,atol=1e-13)
        for j,c in enumerate(COUPLINGS):
            np.testing.assert_allclose(H[16*(j+1):16*(j+2),16*j:16*(j+1)],
                                       c*GATES[j],atol=1e-13)
        np.testing.assert_allclose(np.linalg.eigvalsh(H),
                                   np.repeat([-1.5,-.5,.5,1.5],16),atol=1e-12)
        # Full unitary matrices E,D,T, rather than just one chosen input,
        # are implemented coherently in the prescribed order.

    def test_equal_spacing_derives_coupling_ratio_within_assumed_path_class(self):
        # For symmetric positive 4-site nearest-neighbor hopping (a,b,a),
        # eigenvalue magnitudes are (sqrt(b²+4a²) ± b)/2. Imposing equally
        # spaced ±s/2,±3s/2 forces b/a=2/sqrt(3); s is still chosen.
        for a in (.4,math.sqrt(3)/2,1.2):
            b=2*a/math.sqrt(3)
            h=np.diag([a,b,a],1)+np.diag([a,b,a],-1)
            ev=np.linalg.eigvalsh(h)
            s=b
            np.testing.assert_allclose(ev,[-1.5*s,-.5*s,.5*s,1.5*s],atol=1e-13)
        # An equally spaced spectrum, a line graph and reflection symmetry
        # are inputs; zero does not by itself entail them.

    def test_all_declared_charges_commute_with_full_work_program_generator(self):
        Ef,Df,Tf,Qf,_=physical_operators()
        gg=[np.eye(128),Ef,Df@Ef,Tf@Df@Ef]
        VP=np.zeros((512,512),complex)
        for i,g in enumerate(gg):VP[128*i:128*(i+1),128*i:128*(i+1)]=g
        HF=VP@np.kron(JX,np.eye(128))@VP.conj().T
        np.testing.assert_allclose(HF.conj().T,HF,atol=1e-13)
        q=np.kron(np.eye(4),Qf)
        np.testing.assert_allclose(HF@q,q@HF,atol=1e-13)
        nums=np.asarray(n,complex)
        for inds in ((0,1,2,3),(0,1),(2,3),(0,2),(1,3)):
            Q=np.kron(np.eye(4),np.kron(np.kron(np.kron(I,sum(nums[k] for k in inds)),I),I))
            np.testing.assert_allclose(HF@Q,Q@HF,atol=1e-13)
        # Existing lab/reference factors and the reference clock are not
        # acted on; program clock and added F are neutral in old energy.

    def test_stationary_constraint_is_exact_for_every_seed_and_reference_complete(self):
        np.testing.assert_allclose(W.conj().T@W,I64,atol=1e-13)
        np.testing.assert_allclose(CONSTRAINT@W,0,atol=1e-13)
        np.testing.assert_allclose(EVALS,[-1.5,-.5,.5,1.5],atol=1e-13)
        for t in (0,.4,math.pi,4.9):
            np.testing.assert_allclose(ref_contraction(t),propagator(t)/2,atol=1e-13)
        # Since these are operator identities they include arbitrary lab,
        # clock, sector and reference entanglement of the seed.

    def test_reference_phase_povm_and_ideal_transfer(self):
        for t in (0,.2,math.pi/2,math.pi,4.1):
            a=amplitudes(t)
            expected=np.array([math.comb(3,j)*math.cos(t/2)**(2*(3-j))*
                               math.sin(t/2)**(2*j) for j in range(4)])
            np.testing.assert_allclose(abs(a)**2,expected,atol=1e-13)
            self.assertAlmostEqual(sum(abs(a)**2),1,places=13)
        a=amplitudes(math.pi)
        np.testing.assert_allclose(a,[0,0,0,1j],atol=1e-13)
        # Phase states are nonorthogonal; the exact phase is a POVM density,
        # not a finite-probability sharp clock outcome.
        nodes,weights=np.polynomial.legendre.leggauss(60)
        integral=np.zeros((4,4),complex)
        for x,w in zip(nodes,weights):
            t=math.pi*(x+1)
            ket=np.exp(1j*EVALS*t)/2
            integral+=w*np.outer(ket,ket.conj())*2
        np.testing.assert_allclose(integral,np.eye(4),atol=1e-13)

    def test_real_all_sector_state_and_all_old_clock_labels_recovered(self):
        for seed,hist in zip(self.seeds,self.hist):
            a=amplitudes(math.pi)
            for j in range(3):self.assertLess(np.linalg.norm(a[j]*hist[j]),1e-12)
            np.testing.assert_allclose(a[3]*hist[3],1j*prepare(seed),atol=2e-14)
            for stage in hist:self.assertLess(np.linalg.norm(apply16(Qori,stage)),1e-13)
            got=clock_read(a[3]*hist[3]);expect=clock_read(prepare(seed))
            self.assertEqual(len(got),16)
            for g,e in zip(got,expect):np.testing.assert_allclose(g,1j*e,atol=2e-14)
        # Identical linear implementation on both orthogonal physical
        # sectors preserves their coherent superposition and flag phases.

    def test_the_unselected_coherent_all_sector_history_is_not_a_mixture(self):
        # Physical code and complement embeddings (and their flags) are
        # orthogonal. Direct-sum the normalized component vectors; this keeps
        # their coherent amplitude, rather than averaging density matrices.
        whole=[np.concatenate((self.hist[0][i].ravel()/math.sqrt(128),
                               math.sqrt(127/128)*self.hist[1][i].ravel()))
               for i in range(4)]
        weights=np.array([5,3,3,5],float)/16
        for v in whole:self.assertAlmostEqual(np.linalg.norm(v),1,places=12)
        f=sum(weights[i]*abs(np.vdot(whole[3],whole[i]))**2 for i in range(4))
        self.assertAlmostEqual(f,27/64,places=12)
        self.assertAlmostEqual(matrix_weighted_distance(whole,weights),
                               .616267337677457,places=11)
        # A 00/11 flag off-diagonal has trace norm sqrt(127)/128 for
        # normalized branches. The stationary history isometry preserves it.
        self.assertAlmostEqual(math.sqrt((1/128)*(127/128)),math.sqrt(127)/128,places=14)

    def test_finite_resolution_window_and_exact_heralded_channel(self):
        delta=math.pi/4
        p=projector_window_success(delta)
        self.assertAlmostEqual(p,.8632677754775349,places=13)
        self.assertAlmostEqual(delta/math.pi*p,.2158169438693837,places=13)
        x,w=np.polynomial.legendre.leggauss(64)
        avg=sum(wi*abs(amplitudes(math.pi+delta*xi)[3])**2/2 for xi,wi in zip(x,w))
        self.assertAlmostEqual(avg,p,places=13)
        # Program outcome 3 gives c3(t) T D E for every t; after an actual
        # clock-window and program readout, the conditional map is exactly
        # the desired unitary. Both readouts and their cost are explicit.
        for t in (math.pi-.5,math.pi,math.pi+.5):
            block=propagator(t)[48:64,:16]
            np.testing.assert_allclose(block,amplitudes(t)[3]*HISTORIES[3],atol=1e-13)

    def test_unselected_whole_does_not_satisfy_the_final_eigencondition(self):
        weights=np.array([5,3,3,5],float)/16
        # Uniform phase marginal = 1/(2π). Integrating the binomial program
        # probabilities yields weights 5/16,3/16,3/16,5/16.
        x,w=np.polynomial.legendre.leggauss(64)
        probs=sum(wi*abs(amplitudes(math.pi*(xi+1)))**2/2 for xi,wi in zip(x,w))
        np.testing.assert_allclose(probs,weights,atol=1e-13)
        for hist in self.hist:
            fidelity=sum(weights[i]*abs(np.vdot(hist[3],hist[i]))**2 for i in range(4))
            self.assertAlmostEqual(fidelity,27/64,places=12)
            self.assertAlmostEqual(matrix_weighted_distance(hist,weights),.616267337677457,places=11)
            ss=sum(weights[i]*np.vdot(hist[i],apply16(S,hist[i])).real for i in range(4))
            cc=sum(weights[i]*np.linalg.norm(apply16(C1,hist[i]))**2 for i in range(4))
            self.assertAlmostEqual(ss,5/16,places=12)
            self.assertAlmostEqual(cc,11/8,places=12)
        # No inference that the unselected complete history is the final
        # selected state: intermediate program sectors are retained.

if __name__=='__main__':
    unittest.main()
