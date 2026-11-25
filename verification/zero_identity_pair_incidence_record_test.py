"""Identity pairing, physical incidence flags, and the actual reservoir echo.

The old source/reference pairs and finite program are imported, not spectator
systems. Signed charge and subjective incidence are separate hypotheses.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import I,X,Y,Z,kron
from verification.zero_clock_finite_reservoir_reuse_test import BITS3, weight, energy, Q as THERMAL
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import history, words, distribution
from verification.zero_sphere_local_constitution_echo_test import twenty_tick_path
from verification.zero_internal_reference_subject_valence_candidates_test import born_table


def record_stats(t,auxq=F(0),twenty=False,zbit=0):
    """Exact X_S0 X_F0 coherence and y0 inference from R0 only.

    Off-diagonal overlap keeps B, the other source/ref labels, old state,
    reservoir purifiers, aux purifiers, the echo, and stores in the
    environment. All apparatus gates are basis permutations; source y stays
    unchanged until the final sphere-interface reversal.
    """
    cols=((1,),(0,)); gamma=F(0); law=defaultdict(lambda:[F(0),F(0)])
    for b,x,f,e in product((0,1),BITS3,BITS3,words(1)):
        w=weight(b,x,f)*distribution(auxq,e)
        if not w:continue
        xflip=(x[0]^1,x[1],x[2])
        if twenty:
            state,z,r=twenty_tick_path(b,x,f,e,cols,zbit)[t]
            other,zz,rr=twenty_tick_path(b,xflip,f,e,cols,zbit)[t]
            same=state[2:]==other[2:] and (z,r)==(zz,rr)
        else:
            state=history(b,x,f,e,cols)[t]
            other=history(b,xflip,f,e,cols)[t]
            same=state[2:]==other[2:]
        if same:gamma+=w
        law[state[2][1]][x[0]^b]+=w
    return gamma,sum((max(v) for v in law.values()),F(0))


def flag_incidence(alpha_for_positive=True):
    """Assign F0 flag 0->B and 1->j; flag uniform conditional on b,z,s."""
    out=defaultdict(F)
    for (i,b,z,s),p in born_table().items():
        for flag in (0,1):
            typ='B' if (flag==0)==alpha_for_positive else 'j'
            out[(typ,b,z,s)]+=p/2
    return dict(out)


class IdentityPairIncidenceRecordTests(unittest.TestCase):
    def test_two_relational_zero_operators_fix_each_actual_bell_pair(self):
        # B is represented in its eigenbasis here; this is unitarily
        # equivalent to the physical sphere B, with S,F actual source pair.
        bz=kron(Z,I,I);zs=kron(I,Z,I);zf=kron(I,I,Z)
        xs=kron(I,X,I);xf=kron(I,I,X)
        qz=zs-bz@zf;qx=xs-xf
        gz=bz@zs@zf;gx=xs@xf
        np.testing.assert_allclose(gz@gx,gx@gz,atol=1e-14)
        intersection=(np.eye(8)+gz)@(np.eye(8)+gx)/4
        np.testing.assert_allclose(intersection@intersection,intersection,atol=1e-14)
        self.assertAlmostEqual(np.trace(intersection).real,2,places=13)
        np.testing.assert_allclose(qz@intersection,0,atol=1e-14)
        np.testing.assert_allclose(qx@intersection,0,atol=1e-14)
        # Exactly one pair state for each B sector; arbitrary B-sector
        # amplitudes remain. The conditions are chosen, not derived from zero.
        for bit in (0,1):
            v=np.zeros(8,complex)
            for x in (0,1):v[4*bit+2*(x^bit)+x]=1/np.sqrt(2)
            np.testing.assert_allclose(intersection@v,v,atol=1e-14)
            np.testing.assert_allclose(qz@v,0,atol=1e-14)
            np.testing.assert_allclose(qx@v,0,atol=1e-14)

    def test_exact_coupled_source_relations_and_ledger_all_20_ticks(self):
        cols=((1,),(0,));k=1
        for b,x,f,e,z in product((0,1),BITS3,BITS3,words(k),(0,1)):
            states=twenty_tick_path(b,x,f,e,cols,z)
            for t,((bb,y,m,n,c,d),zz,r) in enumerate(states):
                self.assertEqual(energy(m,n,f),0)
                self.assertEqual(d-k+sum(c)-sum(e),0)
                if 1<=t<=19:self.assertEqual(y[0]^x[0],b)
                else:self.assertEqual(y[0],x[0])
            self.assertEqual(states[20],states[0])

    def test_bare_pair_coherence_and_local_record_through_both_clocks(self):
        for q in (F(0),THERMAL):
            for t in range(15):
                gamma,guess=record_stats(t,q)
                self.assertEqual(gamma,F(1) if t in (0,1,13,14) else F(0))
                self.assertEqual(guess,F(1) if 3<=t<=11 else F(1,2))
            for z in (0,1):
                for t in range(21):
                    gamma,guess=record_stats(t,q,twenty=True,zbit=z)
                    self.assertEqual(gamma,F(1) if t in (0,1,19,20) else F(0))
                    self.assertEqual(guess,F(1) if 3<=t<=17 else F(1,2))
        # At t=2 and 18 coherence is lost while R0 alone has no information:
        # the record is in A/store, so R0's information alone is not a bound
        # on the coherence lost to the entire environment.

    def test_reference_flag_has_equal_weight_but_does_not_fix_type_meaning(self):
        a=flag_incidence(True);b=flag_incidence(False)
        self.assertEqual(a,b) # after tracing the flag, each type remains 1/2
        first={0:'B',1:'j'}; swapped={0:'j',1:'B'}
        self.assertNotEqual(first,swapped) # meanings conditioned on flag differ
        for (typ,bb,z,s),p in a.items():
            original=sum(w for (i,b0,z0,s0),w in born_table().items()
                         if (b0,z0,s0)==(bb,z,s))
            self.assertEqual(p,original/2)
        for typ in ('B','j'):
            self.assertEqual(sum(p*s*(bb if t=='B' else z)
                                 for (t,bb,z,s),p in a.items() if t==typ),0)
        tab=born_table()
        mismatch=sum(w for (i,b,z,s),w in tab.items() if b!=z)
        self.assertEqual(mismatch,F(1,4))
        # X_S X_F toggles the physical flag while leaving b,z,s unchanged.
        # The incidence value changes between sb and sz: on agreement it
        # stays the same; on mismatch it reverses, so this is neither a
        # universally sign-odd mirror nor a valence-preserving gauge map.
        for (i,bb,z,s),p in tab.items():
            ratio=(s*bb)*(s*z)
            self.assertEqual(ratio,1 if bb==z else -1)

    def test_sharp_type_flags_dephase_the_same_pure_physical_state(self):
        # Illustrative single b sector of the actual Bell source pair.
        p0=kron(I,(I+Z)/2);p1=kron(I,(I-Z)/2)
        d=kron(X,X)
        for bit in (0,1):
            psi=np.zeros(4,complex)
            for x in (0,1):psi[2*(x^bit)+x]=1/np.sqrt(2)
            rho=np.outer(psi,psi.conj())
            parts=[p0@rho@p0,p1@rho@p1]
            self.assertAlmostEqual(np.trace(parts[0]).real,.5,places=14)
            self.assertAlmostEqual(np.trace(parts[1]).real,.5,places=14)
            self.assertAlmostEqual(np.trace(rho@d).real,1,places=14)
            self.assertAlmostEqual(np.trace((parts[0]+parts[1])@d).real,0,places=14)
            np.testing.assert_allclose(p0@(parts[0]+parts[1])@p0,p0@rho@p0,atol=1e-14)
            self.assertGreater(np.linalg.norm(rho-(parts[0]+parts[1])),.5)
            # If positive type blocks sum to this pure rho, each is a
            # scalar multiple of rho. They cannot also live in the two
            # orthogonal F0 flag sectors with both weights >0.
            for a in (.25,.5,.75):
                type0=a*rho; type1=(1-a)*rho
                self.assertGreater(np.trace(p1@type0).real,0)
                self.assertGreater(np.trace(p0@type1).real,0)
            # Physical sharp flag versus formally independent equal type:
            # same 1/2 marginals but different type-and-flag joint weights.
            self.assertAlmostEqual(np.trace(parts[0]@p0).real,.5,places=14)
            self.assertAlmostEqual(np.trace((rho/2)@p0).real,.25,places=14)

    def test_source_readout_vs_the_coherent_dressed_witness(self):
        # For any actual unitary U_t that leaves F0 fixed, D_t=U_t D U_t†
        # anticommutes with Z_F and is sharp +1 on U_t|Psi>. The dephased
        # type sum has zero expectation of D_t. Demonstrate the algebra on
        # a representative source-controlled record gate, including the
        # reference F and a neutral memory; the full sequence follows by
        # the same commutation and is additionally checked by record_stats.
        ds=kron(X,X,I);zf=kron(I,Z,I)
        cnot=np.zeros((8,8),complex)
        for s,f,r in product((0,1),repeat=3):
            idx=4*s+2*f+r;target=4*s+2*f+(r^s);cnot[target,idx]=1
        np.testing.assert_allclose(cnot@cnot,np.eye(8),atol=1e-14)
        np.testing.assert_allclose(cnot@zf,zf@cnot,atol=1e-14)
        dt=cnot@ds@cnot
        np.testing.assert_allclose(dt@zf+zf@dt,0,atol=1e-14)
        psi=np.zeros(8,complex);psi[0]=psi[6]=1/np.sqrt(2)
        out=cnot@psi;rho=np.outer(out,out.conj())
        self.assertAlmostEqual(np.vdot(out,dt@out).real,1,places=14)
        p0=(np.eye(8)+zf)/2;p1=(np.eye(8)-zf)/2
        self.assertAlmostEqual(np.trace((p0@rho@p0+p1@rho@p1)@dt).real,0,places=14)
        # Tracing the record makes bare D's expectation 0; it does NOT
        # erase the correlation globally or prove permanent irreversibility.

if __name__=='__main__':unittest.main()
