"""Subject-access comparison on the real sphere-coupled memory circuit.

No modeled factor is asserted to be conscious. Source references are included
only in explicitly stated access sets. Added reporter models are hypotheses.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import sqrt
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base, output, relative_read, I, X, Z, kron
from verification.zero_internal_contextual_reference_test import Gint, Bs, Zj, P
from verification.zero_spin_reversal_sign_selection_test import physical_old_to_canonical
from verification.zero_relational_chirality_report_test import C, LL
from verification.zero_relative_gauge_invariant_report_test import G
from verification.zero_invariant_all_history_record_clock_test import XL, ZL
from verification.zero_relational_chirality_report_test import initial
from verification.zero_internal_reference_subject_valence_candidates_test import (
    b_project, j_project, reduced, value_history, born_table,
)
from verification.zero_clock_finite_reservoir_reuse_test import BITS3, Q
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import (
    history, words, distribution,
)


def outputs(cols, q, b, tick=7, refs=()):
    """Exact output law conditioned on old B=b, with specified source refs."""
    out=defaultdict(F)
    for x,f,e in product(BITS3,BITS3,words(len(cols[0]))):
        w=F(1,8)*distribution(Q,f)*distribution(q,e)
        if not w: continue
        bb,y,m,n,c,d=history(b,x,f,e,cols)[tick]
        # Only R,C and requested reference bits are made accessible.
        out[(m[1:],c,tuple(x[i] for i in refs))]+=w
    return dict(out)


def guess_score(cols, q, refs=(), keep_j=True):
    """Optimal classical score; quantum reduction is checked separately."""
    law=defaultdict(lambda:defaultdict(F))
    for (i,b,z,s),w in born_table().items():
        for extra,p in outputs(cols,q,int(b==-1),refs=refs).items():
            obs=(s,z if keep_j else None,extra)
            law[obs][s*b]+=w*p
    return sum((max(v.values()) for v in law.values()),F(0))


def effective_noise_score(cols):
    # A faster equivalent calculation for all linear codes using R1 XOR x1.
    prior={(1,1):F(1,2),(-1,1):F(1,4),(-1,-1):F(1,4)}
    law=defaultdict(lambda:defaultdict(F))
    for (b,z), f,e in product(prior,words(2),words(len(cols[0]))):
        code=tuple((f[0]*a)^(f[1]*c) for a,c in zip(*cols))
        c=tuple(a^v for a,v in zip(e,code))
        parity=int(b==-1)^f[0]
        law[(z,parity,c)][b]+=prior[(b,z)]*distribution(Q,f)*distribution(Q,e)
    return sum((max(v.values()) for v in law.values()),F(0))


def reduced_coherent(t,cols,q,psi):
    """Independent finite coherent check of tracing source and all refs.

    psi[b,j] is an arbitrary coherent old state. Retain old two-qubit system
    and R,C; trace source, all refs, all purifiers, A and both batteries.
    All f/e purifiers exist, even when q=0. This uses the actual gate history.
    """
    k=len(cols[0]); dimrc=8*(2**k); groups={}
    for b,x,f,e in product((0,1),BITS3,BITS3,words(k)):
        w=F(1,8)*distribution(Q,f)*distribution(q,e)
        if not w:continue
        _,y,m,n,c,d=history(b,x,f,e,cols)[t]
        env=(x,y,f,e,m[0],n,d)
        v=groups.setdefault(env,np.zeros(4*dimrc,complex))
        rindex=BITS3.index(m[1:]); cindex=words(k).index(c)
        for j in (0,1):
            index=((2*b+j)*dimrc+rindex*(2**k)+cindex)
            v[index]+=psi[b,j]*sqrt(float(w))
    return sum((np.outer(v,v.conj()) for v in groups.values()),np.zeros((4*dimrc,4*dimrc),complex))


class SphereReuseExperientialAccessTests(unittest.TestCase):
    def test_original_quantum_history_reduced_b_s_z_all_16(self):
        # No replacement with a fabricated classical state: check the exact
        # actual old vectors against the table and diagonal j reductions.
        expected=born_table(); state=output(active_base())
        for label in range(16):
            v=initial(relative_read(state,4,labels=(label,))[0]); mass=np.vdot(v,v).real
            for s,b in product((1,-1),repeat=2):
                branch=(v+s*value_history(v))/2
                rho=reduced(b_project(branch,b),7)/mass
                self.assertAlmostEqual(abs(rho[0,1]),0,places=12)
                for z in (1,-1):
                    projected=j_project(b_project(branch,b),z)
                    sub=reduced(projected,7)/mass
                    target=sum(w for (i,bb,zz,ss),w in expected.items() if (bb,zz,ss)==(b,z,s))
                    self.assertAlmostEqual(np.trace(sub).real,float(target),places=12)
                    self.assertAlmostEqual(sub[0 if z==1 else 1,0 if z==1 else 1].real,float(target),places=12)

    def test_no_reference_apparatus_is_independent_of_b_all_ticks(self):
        for cols,q in [(((),()),Q),(((1,),(0,)),F(0)),(((1,1),(0,0)),Q)]:
            for t in range(15):
                self.assertEqual(outputs(cols,q,0,t),outputs(cols,q,1,t))
        # At intermediate ticks tracing source AND references also dephases B,
        # as checked coherently below; identical diagonals alone are not enough.

    def test_coherent_factorization_and_return_with_old_entanglement(self):
        psi=np.array([[1,1j],[-1j,2]],complex);psi/=np.linalg.norm(psi)
        old=np.outer(psi.ravel(),psi.ravel().conj())
        dephased=old.copy();dephased[:2,2:]=0;dephased[2:,:2]=0
        cols=((1,),(0,)); dim=16
        for t in range(15):
            rho=reduced_coherent(t,cols,Q,psi)
            blocks=rho.reshape(4,dim,4,dim)
            sigma=np.einsum('iaib->ab',blocks)
            old_expected=old if t in (0,14) else dephased
            np.testing.assert_allclose(rho,np.kron(old_expected,sigma),atol=2e-14)
            self.assertAlmostEqual(np.trace(rho).real,1,places=12)
        # Algebraic proof in report covers any old density operator and the
        # entire accessible apparatus, not just this finite subsystem test.

    def test_no_reference_best_physical_sphere_parity_is_three_quarters(self):
        for cols,q in [(((),()),Q),(((1,),(0,)),F(0)),(((1,1),(0,0)),Q)]:
            self.assertEqual(guess_score(cols,q),F(3,4))
            self.assertEqual(guess_score(cols,q,keep_j=False),F(1,2))
        # R,C do not replace access to a reference. Their independence is a
        # consequence of the chosen Bell-pair preparation and interface.

    def test_reference_and_memory_quantum_access_comparison(self):
        self.assertEqual(guess_score(((),()),Q,refs=(0,)),1)
        self.assertEqual(guess_score(((),()),Q,refs=(1,)),F(13,16))
        self.assertEqual(guess_score(((1,),(0,)),Q,refs=(1,)),F(55,64))
        self.assertEqual(guess_score(((1,),(0,)),F(0),refs=(1,)),1)
        self.assertEqual(guess_score(((1,1),(0,0)),Q,refs=(1,)),F(113,128))
        self.assertEqual(guess_score(((1,0),(0,1)),Q,refs=(1,)),F(55,64))
        # b = R1 XOR x1 XOR C when C copies f0 perfectly; direct access to
        # F1 is an extra interface, not available merely by being in a whole.

    def test_exhaustive_redundancy_for_the_accessible_target(self):
        for k,expected in ((0,F(13,16)),(1,F(55,64)),(2,F(113,128)),(3,F(931,1024))):
            scores=[effective_noise_score(cols) for cols in product(words(k),repeat=2)]
            self.assertEqual(max(scores),expected)
        self.assertEqual(effective_noise_score(((1,1),(0,0))),F(113,128))

    def test_two_physical_pointer_parities_are_compatible_readouts(self):
        # The original j control and old constraints commute; M and the
        # new degenerate pointer are neutral. R1 and C are diagonal energy
        # occupations used only as controls, and the source reference is
        # degenerate and gauge-neutral. Their CNOTs therefore preserve both
        # constructed charges. Existing helper checks actual pure-C history.
        for a in (Gint,Bs,P):
            np.testing.assert_allclose(Zj@a-a@Zj,0,atol=1e-13)
        for old in (LL,G,*C,kron(XL,I,I),kron(ZL,I,I)):
            embedded=kron(physical_old_to_canonical(old),I,I)
            np.testing.assert_allclose(Zj@embedded-embedded@Zj,0,atol=1e-13)
        np.testing.assert_allclose(X@X,I,atol=1e-13)
        for b,x,f,e in product((0,1),BITS3,BITS3,words(1)):
            if e!=(0,):continue  # clean memory required for exact B parity
            _,y,m,n,c,d=history(b,x,f,e,((1,),(0,)))[7]
            self.assertEqual(m[2]^x[1]^c[0],b)
            for s,z in product((1,-1),repeat=2):
                hs=s*(-1 if m[2]^x[1]^c[0] else 1)
                hj=s*z
                self.assertEqual(hs==hj,((-1 if b else 1)==z))
        # XOR-writing both parities into two initially blank neutral pointers
        # is unitary and leaves all controls unchanged. It copies observables,
        # not lived experience, and may dephase coherences if pointers traced.

    def test_distinguishing_conditional_report_models(self):
        tab=born_table(); mismatch=sum(w for (i,b,z,s),w in tab.items() if b!=z)
        self.assertEqual(mismatch,F(1,4))
        for eps in (F(0),F(1,10),F(1,2)):
            # Independently postulated error channel for the felt-sign report;
            # compare report to the sphere physical observable on mismatch.
            self.assertEqual((1-eps)-eps,1-2*eps)
            h_b=sum(w*((1-eps) if b!=z else (1-eps)) for (i,b,z,s),w in tab.items())
            h_j=sum(w*((1-eps) if b==z else eps) for (i,b,z,s),w in tab.items())
            self.assertEqual(h_b,1-eps)
            self.assertEqual(h_j,F(3,4)-eps/2)
        for b0 in (1,-1):
            for which in ('b','z'):
                signed=sum(w*s*(b if which=='b' else z) for (i,b,z,s),w in tab.items() if b==b0)
                self.assertEqual(signed,0)
        # These numbers are quantum Born weights, not proven incidence weights.

if __name__=='__main__':unittest.main()
