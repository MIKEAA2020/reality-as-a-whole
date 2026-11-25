"""Canonical flag-compatible incidence and an actual zero-charge echo record.

Type=flag and type-to-felt-sign are explicit hypotheses. Source reference,
thermal reservoirs, pure global state, and echo are the established model.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import I,X,Z,kron
from verification.zero_clock_finite_reservoir_reuse_test import BITS3,energy,Q as THERMAL
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import words,distribution
from verification.zero_sphere_local_constitution_echo_test import twenty_tick_path
from verification.zero_joint_constitution_incidence_echo_test import coarse_table


def physical_ledger(qaux=F(0)):
    """Exact measured-record statistics for the actual 20-step program."""
    cols=((1,),(0,));laws=[defaultdict(lambda:[F(0),F(0)]) for _ in range(21)]
    laws_j=[defaultdict(lambda:[F(0),F(0)]) for _ in range(21)]
    signs=[defaultdict(F) for _ in range(21)]
    change=[defaultdict(F) for _ in range(21)]
    for ((b,z,s),p),x,f,e in product(coarse_table().items(),BITS3,BITS3,words(1)):
        w=p*F(1,8)*distribution(THERMAL,f)*distribution(qaux,e)
        if not w:continue
        states=twenty_tick_path(int(b==-1),x,f,e,cols,int(z==-1))
        for t,((bb,y,m,n,c,d),zz,r) in enumerate(states):
            flag=x[0];j=1 if zz==0 else -1
            laws[t][(m[1],r)][flag]+=w
            laws_j[t][(m[1],r,zz)][flag]+=w
            val=s*(b if flag==0 else j)
            signs[t][(flag,val)]+=w
            before=s*(b if flag==0 else z)
            change[t][(flag,int(val!=before))]+=w
    def success(law):return sum((max(v) for v in law.values()),F(0))
    return ([success(v) for v in laws],[success(v) for v in laws_j],signs,change)


def copy_extension(b,x,f,e,zbit):
    """Insert four neutral R0/E-controlled XORs at tick 10.

    R0 XOR echo = F0 on the actual input support. Copy then uncopy, with
    all 20 original gates retained; the final state is the initial state.
    """
    states=twenty_tick_path(b,x,f,e,((1,),(0,)),zbit)
    out=[(st,zz,r,0) for st,zz,r in states[:11]]
    st,zz,r=states[10];r0=st[2][1]
    out.extend([(st,zz,r,r0),(st,zz,r,r0^r),(st,zz,r,r0),(st,zz,r,0)])
    out.extend((st,zz,r,0) for st,zz,r in states[11:])
    return out


class FlagRecordAlgebraEchoTests(unittest.TestCase):
    def test_canonical_weights_on_flag_commutant_and_noncommuting_failure(self):
        # Actual S,F pair conditional on b=+: Phi+. Use arbitrary positive
        # block effects commuting with F, not merely the basis projectors.
        psi=np.array([1,0,0,1],complex)/np.sqrt(2);rho=np.outer(psi,psi.conj())
        p0=kron(I,(I+Z)/2);p1=kron(I,(I-Z)/2);rng=np.random.default_rng(691)
        for _ in range(30):
            a=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4));a=a@a.conj().T
            effect=(p0@a@p0+p1@a@p1);effect/=max(np.linalg.eigvalsh(effect).max(),1)
            np.testing.assert_allclose(effect@p0,p0@effect,atol=1e-13)
            m0=np.trace(rho@p0@effect);m1=np.trace(rho@p1@effect)
            self.assertGreaterEqual(m0.real,-1e-13);self.assertGreaterEqual(m1.real,-1e-13)
            self.assertAlmostEqual((m0+m1).real,np.trace(rho@effect).real,places=13)
            self.assertAlmostEqual(m0.real,np.trace(p0@rho@p0@effect).real,places=13)
            self.assertAlmostEqual(m1.real,np.trace(p1@rho@p1@effect).real,places=13)
        self.assertAlmostEqual(np.trace(rho@p0).real,.5,places=13)
        # Naively extending Tr(rho P0 E) outside the commutant can be
        # negative even for a legitimate positive rank-one effect.
        phi=np.array([1,0,0,-2],complex)/np.sqrt(5);e=np.outer(phi,phi.conj())
        self.assertAlmostEqual(np.trace(rho@p0@e).real,-.1,places=13)

    def test_all_tick_flag_incidence_and_hypothetical_signs(self):
        for q in (F(0),THERMAL):
            scores,scores_j,signs,change=physical_ledger(q)
            for t in range(21):
                for flag,sign in product((0,1),(1,-1)):
                    self.assertEqual(signs[t][flag,sign],F(1,4))
                self.assertEqual(sum(signs[t].values()),1)
                self.assertEqual(change[t][0,1],0)
                self.assertEqual(change[t][1,1],F(1,4) if t in (9,10,11) else 0)
        # Even after the joint midpoint record selects the flag and B,
        # s-counterparts still cancel separately for every record outcome.
        signed=defaultdict(F);mass=defaultdict(F)
        for ((b,z,s),p),x,f,e in product(coarse_table().items(),BITS3,BITS3,words(1)):
            w=p*F(1,8)*distribution(THERMAL,f)*distribution(F(0),e)
            if not w:continue
            state,zz,r=twenty_tick_path(int(b==-1),x,f,e,((1,),(0,)),int(z==-1))[10]
            key=(state[2][1],r,x[0]);j=1 if zz==0 else -1
            signed[key]+=w*s*(b if x[0]==0 else j);mass[key]+=w
        self.assertEqual(len(mass),4)
        self.assertTrue(all(v==F(1,4) for v in mass.values()))
        self.assertTrue(all(v==0 for v in signed.values()))
        # A sign is assigned by the proposed flag->bridge rule; the circuit
        # does not establish actual subjects or felt valence.

    def test_finite_access_to_flag_requires_real_echo_interface(self):
        expected=[F(1,2)]*8+[F(3,4),F(3,4),F(1),F(3,4),F(3,4)]+[F(1,2)]*8
        expected_j=[F(1,2)]*3+[F(3,4)]*6+[F(1),F(1),F(1)]+[F(3,4)]*6+[F(1,2)]*3
        for q in (F(0),THERMAL):
            scores,scores_j,_,_=physical_ledger(q)
            self.assertEqual(scores,expected)
            self.assertEqual(scores_j,expected_j)
        # At midpoint R0 XOR echo bit is exactly x0; before that, the
        # observer does not magically access B or the source reference.
        # R0 alone is uninformative, and the actual parity conditional on
        # the two records is delta(flag, R0 XOR echo) at midpoint.
        for q in (F(0),THERMAL):
            for t in range(21):
                single=defaultdict(lambda:[F(0),F(0)])
                joint=defaultdict(lambda:[F(0),F(0)])
                for ((b,z,s),p),x,f,e in product(coarse_table().items(),BITS3,BITS3,words(1)):
                    w=p*F(1,8)*distribution(THERMAL,f)*distribution(q,e)
                    if not w:continue
                    state,zz,r=twenty_tick_path(int(b==-1),x,f,e,((1,),(0,)),int(z==-1))[t]
                    r0=state[2][1]
                    single[r0][x[0]]+=w;joint[(r0,r)][x[0]]+=w
                self.assertEqual(sum((max(v) for v in single.values()),F(0)),F(1,2))
                if t==10:
                    for (r0,r),weights in joint.items():
                        self.assertEqual(weights[1^(r0^r)],0)
                        self.assertEqual(weights[r0^r],F(1,4))

    def test_twenty_four_tick_neutral_copy_and_uncompute(self):
        cols=((1,),(0,));k=1
        for b,x,f,e,zbit in product((0,1),BITS3,BITS3,words(1),(0,1)):
            states=copy_extension(b,x,f,e,zbit)
            self.assertEqual(len(states),25)
            for (bb,y,m,n,c,d),z,r,l in states:
                self.assertEqual(energy(m,n,f),0)
                self.assertEqual(d-k+sum(c)-sum(e),0)
            (bb,y,m,n,c,d),z,r,l=states[12]
            self.assertEqual(m[1]^r,x[0])
            self.assertEqual(l,x[0])
            self.assertEqual(states[14][3],0)
            self.assertEqual(states[24],states[0])
        # Actual pulse old-sphere algebra and coherent echo were separately
        # checked on all 16 original histories by the inherited verifier.

    def test_copy_preserves_global_coherence_but_dephases_reduced_system(self):
        psi=np.array([1,0,0,1],complex)/np.sqrt(2);rho=np.outer(psi,psi.conj())
        p0=kron(I,(I+Z)/2);p1=kron(I,(I-Z)/2);d=kron(X,X)
        delta=p0@rho@p0+p1@rho@p1
        vals=np.linalg.eigvalsh(rho-delta)
        trace_distance=sum(abs(vals))/2
        self.assertAlmostEqual(trace_distance,.5,places=13)
        self.assertAlmostEqual((1+trace_distance)/2,.75,places=13)
        self.assertAlmostEqual(np.trace(rho@d).real,1,places=13)
        self.assertAlmostEqual(np.trace(delta@d).real,0,places=13)
        # Copy F into a neutral ready pointer L. The whole is pure; tracing L
        # gives delta, while the joint dressed witness D⊗X_L remains +1.
        init=np.kron(psi,[1,0]);u=kron(p0,I)+kron(p1,X)
        out=u@init
        np.testing.assert_allclose(u@u,np.eye(8),atol=1e-13)
        joint=np.outer(out,out.conj())
        reduced=np.trace(joint.reshape(4,2,4,2),axis1=1,axis2=3)
        np.testing.assert_allclose(reduced,delta,atol=1e-13)
        self.assertAlmostEqual(np.vdot(out,kron(d,X)@out).real,1,places=13)
        np.testing.assert_allclose(u@out,init,atol=1e-13)

    def test_gauge_invariant_cyclic_dressed_witness_construction(self):
        # Generic cyclic clock proof tested with a noncommuting four-gate
        # source/reference programme that preserves F. The same algebra
        # applies to the 20-step actual gate schedule and to the explicit
        # 24-step parity-copy extension: D_t=U_t D0 U_t†, U_T=I.
        # (No claim of an independently implemented laboratory gate.)
        zf=kron(I,Z);d0=kron(X,X);p0=(np.eye(4)+zf)/2;p1=(np.eye(4)-zf)/2
        v=kron(X,I);phase=np.diag([1,1,1,-1]).astype(complex)
        # Each commutes with F; phase makes the transported D nontrivial.
        gates=[v,phase,phase,v];us=[np.eye(4,dtype=complex)]
        for g in gates:us.append(g@us[-1])
        np.testing.assert_allclose(us[-1],np.eye(4),atol=1e-13)
        dim=4;steps=len(gates);shift=np.zeros((steps*dim,steps*dim),complex)
        witness=np.zeros_like(shift);flag=np.kron(np.eye(steps),zf)
        for t,g in enumerate(gates):
            shift[((t+1)%steps)*dim:((t+1)%steps+1)*dim,t*dim:(t+1)*dim]=g
            witness[t*dim:(t+1)*dim,t*dim:(t+1)*dim]=us[t]@d0@us[t].conj().T
        np.testing.assert_allclose(shift@witness,witness@shift,atol=1e-13)
        np.testing.assert_allclose(witness@flag+flag@witness,0,atol=1e-13)
        np.testing.assert_allclose(shift.conj().T@shift,np.eye(steps*dim),atol=1e-13)
        phi=np.array([1,0,0,1],complex)/np.sqrt(2)
        history=np.concatenate([u@phi for u in us[:-1]])/np.sqrt(steps)
        np.testing.assert_allclose(shift@history,history,atol=1e-13)
        np.testing.assert_allclose(witness@history,history,atol=1e-13)

if __name__=='__main__':unittest.main()
