"""Internal links: flag incidence, physical records, balance and coherence.

Inferences use the established sphere circuit and its Born table, not an
assertion of subjecthood or conscious access. Auxiliary thermal q is explicit.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import I,X,Z,kron
from verification.zero_clock_finite_reservoir_reuse_test import BITS3,Q as THERMAL
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import words,distribution
from verification.zero_sphere_local_constitution_echo_test import twenty_tick_path
from verification.zero_joint_constitution_incidence_echo_test import coarse_table


def ensemble(t,q=F(0)):
    for ((b,z,s),p),x,f,e in product(coarse_table().items(),BITS3,BITS3,words(1)):
        w=p*F(1,8)*distribution(THERMAL,f)*distribution(q,e)
        if not w:continue
        state,zz,r=twenty_tick_path(int(b==-1),x,f,e,((1,),(0,)),int(z==-1))[t]
        yield b,z,s,x,f,e,state,zz,r,w


def score(law):return sum((max(p) for p in law.values()),F(0))


class InternalConnectionTests(unittest.TestCase):
    def test_three_original_flags_and_two_access_interfaces(self):
        # Compare three actual reference qubits, not relabelled copies of x0.
        for q in (F(0),THERMAL):
            pairs=[defaultdict(lambda:[F(0),F(0)]) for _ in range(3)]
            full=[defaultdict(lambda:[F(0),F(0)]) for _ in range(3)]
            prior=defaultdict(F);same=F(0);different_values=F(0);mismatch=F(0)
            for b,z,s,x,f,e,st,zz,r,w in ensemble(10,q):
                m=st[2];c=st[4];j=(-1)**zz
                prior[x]+=w
                for i in range(3):
                    pairs[i][(m[1],r)][x[i]]+=w
                    full[i][(m[1],m[2],m[3],c,r)][x[i]]+=w
                self.assertEqual(m[1]^r,x[0])
                if not q:self.assertEqual(m[2]^c[0]^r,x[1])
                if x[0]==x[1]:same+=w
                if b!=j:mismatch+=w
                if s*(b if x[0]==0 else j)!=s*(b if x[1]==0 else j):
                    different_values+=w
            self.assertTrue(all(prior[x]==F(1,8) for x in BITS3))
            self.assertEqual([score(law) for law in pairs],[F(1),F(1,2),F(1,2)])
            self.assertEqual([score(law) for law in full],
                             [F(1),F(1) if q==0 else F(3,4),F(3,4)])
            self.assertEqual(same,F(1,2))
            self.assertEqual(mismatch,F(1,4))
            self.assertEqual(different_values,F(1,8))
        # Both candidate flag maps obey the same equal prior, sharp support,
        # source-reference identity constraints, conserved flag and global
        # sign balance. The specific restricted interface can distinguish
        # them operationally, but does not prove it is a subject's interface.

    def test_equal_balance_alternative_flags_give_distinct_report_predictions(self):
        # Conditional behavioral hypothesis, not an observed report: one
        # persistent subject's felt sign equals its selected candidate and
        # the same independently calibrated bit-flip error applies to both.
        for q in (F(0),THERMAL):
            total=F(0);match0=F(0);match1=F(0)
            for b,z,s,x,f,e,st,zz,r,w in ensemble(10,q):
                j=(-1)**zz
                if b==j:continue
                total+=w
                predicted=s*(b if st[2][1]^r==0 else j)
                value0=s*(b if x[0]==0 else j)
                value1=s*(b if x[1]==0 else j)
                if value0==predicted:match0+=w
                if value1==predicted:match1+=w
            self.assertEqual(total,F(1,4))
            self.assertEqual(match0/total,1)
            self.assertEqual(match1/total,F(1,2))
            for error in (F(0),F(1,10),F(1,2)):
                report0=error+(1-2*error)*(match0/total)
                report1=error+(1-2*error)*(match1/total)
                self.assertEqual(report0,1-error)
                self.assertEqual(report1,F(1,2))
        # Conditioning requires jointly accessing r, R0, s and current j.
        # The physical circuit alone neither supplies such a subject nor
        # validates the independent sign-report-error model.

    def test_signed_balance_after_recording_and_conditioning(self):
        for q in (F(0),THERMAL):
            for t in range(21):
                out=defaultdict(lambda:[F(0),F(0)])
                for b,z,s,x,f,e,st,zz,r,w in ensemble(t,q):
                    h=s*(b if x[0]==0 else (-1)**zz)
                    key=(st[2][1],r,x[0])
                    out[key][0]+=w;out[key][1]+=w*h
                # These records do not select the s-counterpart: each
                # nonempty flag-and-record cell has precisely zero numerator.
                for p,v in out.values():
                    if p:self.assertEqual(v,0)
            # Once s itself is recorded, local signed values need not vanish.
            out=defaultdict(lambda:[F(0),F(0)])
            for b,z,s,x,f,e,st,zz,r,w in ensemble(10,q):
                key=(st[2][1],r,s);h=s*(b if x[0]==0 else (-1)**zz)
                out[key][0]+=w;out[key][1]+=w*h
            for r0,r,s in product((0,1),(0,1),(1,-1)):
                p,v=out[r0,r,s];self.assertEqual(p,F(1,8))
                # flag x0=r0 XOR r. With r=0 current j=+; with r=1
                # the j-flag branch has equal +/- j, while B=-.
                expected=s if r==0 else (0 if r0==0 else -s)
                self.assertEqual(v/p,expected)
                self.assertEqual(out[r0,r,s][1],-out[r0,r,-s][1])

    def test_flag_pinching_gives_same_single_and_multistep_record_weights(self):
        # Flag and probe initially Bell-correlated, sign pointer |+>.
        phi=np.array([1,0,0,1],complex)/np.sqrt(2)
        plus=np.array([1,1],complex)/np.sqrt(2);psi=np.kron(phi,plus)
        rho=np.outer(psi,psi.conj());p0=kron((I+Z)/2,I,I);p1=kron((I-Z)/2,I,I)
        c=kron(I,I,X); h0=kron(I,Z,Z);h1=kron(I,I,Z)
        delta=p0@rho@p0+p1@rho@p1
        np.testing.assert_allclose(c@rho@c,rho,atol=1e-13)
        for h in (h0,h1):
            np.testing.assert_allclose(c@h@c,-h,atol=1e-13)
            for p in (p0,p1):np.testing.assert_allclose(p@h,h@p,atol=1e-13)
        # Two successive flag-compatible (but probe-noncommuting) projective
        # instruments. Their effective POVM commutes with the flag. No hidden
        # classical trajectory or outcome-independent collapse is required.
        zp=[(I+Z)/2,(I-Z)/2];xp=[(I+X)/2,(I-X)/2]
        for a,b in product(range(2),repeat=2):
            k1=kron(I,zp[a],I);k2=kron(I,xp[b],I);k=k2@k1
            np.testing.assert_allclose(k@p0,p0@k,atol=1e-13)
            self.assertAlmostEqual(np.trace(k@rho@k.conj().T).real,
                                   np.trace(k@delta@k.conj().T).real,places=13)
            for p,h in ((p0,h0),(p1,h1)):
                self.assertAlmostEqual(np.trace(p@h@k@rho@k.conj().T).real,0,places=13)
        # A non-counterpart-invariant sign record has nonzero local signed
        # contribution even though the full sum is zero.
        pos=kron(I,I,(I+Z)/2);neg=kron(I,I,(I-Z)/2)
        self.assertAlmostEqual(np.trace(p1@h1@pos@rho).real,.25,places=13)
        self.assertAlmostEqual(np.trace(p1@h1@neg@rho).real,-.25,places=13)
        witness=kron(X,X,I)
        self.assertAlmostEqual(np.trace(witness@rho).real,1,places=13)
        self.assertAlmostEqual(np.trace(witness@delta).real,0,places=13)

    def test_covariant_coarse_graining_and_cyclic_relational_observables(self):
        # Proof-by-construction on a nontrivial periodic flag-preserving
        # four-step clock; algebraic proof in the report extends to actual
        # 20-step U_t, whose gates preserve F and whose full cycle is I.
        flag=kron(Z,I);p=[(np.eye(4)+flag)/2,(np.eye(4)-flag)/2]
        def delta(a):return sum(v@a@v for v in p)
        control=kron((I+Z)/2,I)+kron((I-Z)/2,X)
        rot=kron(I,Z);gates=[control,rot,rot,control];us=[np.eye(4,dtype=complex)]
        rng=np.random.default_rng(191);v=rng.normal(size=4)+1j*rng.normal(size=4);v/=np.linalg.norm(v)
        rho=np.outer(v,v.conj())
        for gate in gates:
            np.testing.assert_allclose(gate@flag,flag@gate,atol=1e-13)
            before=us[-1]@rho@us[-1].conj().T
            np.testing.assert_allclose(delta(gate@before@gate.conj().T),
                                       gate@delta(before)@gate.conj().T,atol=1e-13)
            us.append(gate@us[-1])
        np.testing.assert_allclose(us[-1],np.eye(4),atol=1e-13)
        d=kron(X,I);dt=[u@d@u.conj().T for u in us[:-1]];steps=len(gates)
        shift=np.zeros((4*steps,4*steps),complex);rel=np.zeros_like(shift)
        for t,g in enumerate(gates):
            shift[4*((t+1)%steps):4*((t+1)%steps+1),4*t:4*(t+1)]=g
            rel[4*t:4*(t+1),4*t:4*(t+1)]=dt[t]
        np.testing.assert_allclose(shift@rel,rel@shift,atol=1e-13)
        history=np.concatenate([u@v for u in us[:-1]])/np.sqrt(steps)
        np.testing.assert_allclose(shift@history,history,atol=1e-13)
        self.assertAlmostEqual(np.vdot(history,rel@history).real,np.vdot(v,d@v).real,places=13)

if __name__=='__main__':unittest.main()
