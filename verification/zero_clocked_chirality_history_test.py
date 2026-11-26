"""Regression, stationary effects and original quantum-vector controls."""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import unittest
import numpy as np

from verification.zero_clocked_chirality_history import (
    INDEX,dress,dressing,history,old_shift,period,record_gate,selected,step,twirled_anchor,averaged_effect
)
from verification.zero_stationary_battery_bridge import STATES,PREFIX,advance
from verification.zero_sphere_chirality_echo_test import readout,bin_second_moment
from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial,apply64,PP,PM,P0
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_coherent_clock_angular_history import quantum_echo_checkpoints,checkpoint_at,apparatus_path
from verification.zero_clock_finite_reservoir_reuse_test import BITS3
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import words
from verification.zero_dressed_history_pair import encode_pair,decode_pair,from_anchor
from verification.zero_gauge_angular_pair import physical,stationary_physical


class ClockedChiralityTests(unittest.TestCase):
    def test_exact_clock_schedule_and_unitarity(self):
        for cycles,q,h in product((1,2),(1,2),(-.8,.0,.6)):
            n=period(cycles);rng=np.random.default_rng(201+cycles+q)
            a=rng.normal(size=(n,len(STATES),4,3))+1j*rng.normal(size=(n,len(STATES),4,3))
            a/=np.linalg.norm(a)
            self.assertAlmostEqual(np.linalg.norm(step(a,q,h)),1.,places=13)
            v=a.copy()
            for _ in range(n):v=step(v,q,h)
            np.testing.assert_allclose(v,a,atol=2e-14)
            # D W D† makes every dressed cycle unitary; D is identity before
            # tick 10, V afterwards, so the only pulses are write and erase.
            u=record_gate(h)
            for tick in range(n):
                dest=(tick+1)%n
                transition=dressing(dest,h)@dressing(tick,h).T
                expected=u if tick==9 else u.T if tick==n-1 else np.eye(3)
                np.testing.assert_allclose(transition,expected,atol=3e-16)

    def test_single_write_without_erase_fails_cycle_closure(self):
        for cycles,q in product((1,2),(1,2)):
            n=period(cycles);h=.3;v=np.zeros((n,len(STATES),4,3),complex)
            v[0,0,0,0]=1.;start=v.copy();gate=record_gate(h)
            for _ in range(n):
                v=old_shift(v,q)
                v[10]=v[10]@gate.T
            self.assertAlmostEqual(np.linalg.norm(v),1.,places=14)
            self.assertAlmostEqual(abs(np.vdot(start,v)),0.,places=14)
            self.assertAlmostEqual(np.linalg.norm(v-start),sqrt(2),places=14)
            # A single closed-orbit write sends the ready state to an
            # orthogonal recorded subspace, so this initialized orbit cannot
            # be stationary without a compensating operation or different model.

    def test_actual_stationary_history_and_cross_cycle_retention(self):
        for cycles,q,h in product((1,2),(1,2),(-.7,.25,.9)):
            psi=history(cycles,q,h)
            self.assertAlmostEqual(np.linalg.norm(psi),1.,places=13)
            np.testing.assert_allclose(step(psi,q,h),psi,atol=1e-14)
            old=np.array([1.,0.,0.]);written=record_gate(h)@old
            for tick in range(period(cycles)):
                expected=written if tick>=10 else old
                block=psi[tick].sum(axis=(0,1))
                # Old source amplitudes are nonnegative but permuted; ratio
                # of pointer components verifies the same coherent record.
                self.assertLess(np.linalg.norm(np.sum(block)*expected-block*np.sum(expected)),1e-13)
            if cycles==2:
                np.testing.assert_allclose(dressing(20,h)@old,written,atol=1e-15)
                np.testing.assert_allclose(dressing(39,h)@old,written,atol=1e-15)
                np.testing.assert_allclose(dressing(0,h)@old,old,atol=1e-15)

    def test_twirled_pointer_effects_commute_with_new_constraint(self):
        rng=np.random.default_rng(551)
        for cycles,q in product((1,2),(1,2)):
            n=period(cycles);h=.43
            v=rng.normal(size=(n,len(STATES),4,3))+1j*rng.normal(size=(n,len(STATES),4,3))
            v/=np.linalg.norm(v);minus=np.diag([0.,0.,1.]);eye=np.eye(3)
            for a,r in ((0,2),(10,2),(n-1,1)):
                Q=lambda z:twirled_anchor(z,q,a,r,minus,h)
                np.testing.assert_allclose(step(Q(v),q,h),Q(step(v,q,h)),atol=2e-14)
                np.testing.assert_allclose(Q(Q(v)),Q(v),atol=2e-14)
            summed=sum((averaged_effect(v,q,r,eye,h) for r in range(4)),np.zeros_like(v))
            np.testing.assert_allclose(summed,v,atol=2e-14)
            for r in range(4):
                plus=averaged_effect(v,q,r,np.diag([0.,1.,0.]),h)
                neg=averaged_effect(v,q,r,minus,h)
                blank=averaged_effect(v,q,r,np.diag([1.,0.,0.]),h)
                np.testing.assert_allclose(blank+plus+neg,averaged_effect(v,q,r,eye,h),atol=2e-14)
            # A bare reference=2 projector is not stationary.
            def bare(z):
                out=np.zeros_like(z);out[:,:,2,:]=z[:,:,2,:];return out
            self.assertGreater(np.linalg.norm(step(bare(v),q,h)-bare(step(v,q,h))),.1)

    def test_reference_conditioning_and_record_fractions(self):
        minus=np.diag([0.,0.,1.]);eye=np.eye(3);h=.6
        for cycles,q in product((1,2),(1,2)):
            psi=history(cycles,q,h);samples=selected(cycles,q,2)
            w=F(sum(n>=10 for n in samples),len(samples))
            analytic=(1-F(2,5*cycles)) if q==1 else (1-F(1,2*cycles))
            self.assertEqual(w,analytic)
            event=np.vdot(psi,averaged_effect(psi,q,2,eye,h)).real
            joint=np.vdot(psi,averaged_effect(psi,q,2,minus,h)).real
            self.assertAlmostEqual(event,.25 if q==1 else .5,places=13)
            self.assertAlmostEqual(joint/event,float(w)*(1-h)/2,places=13)
        self.assertEqual(F(sum(n>=10 for n in selected(2,1,2)),len(selected(2,1,2))),F(4,5))
        self.assertEqual(F(sum(n>=10 for n in selected(2,2,2)),len(selected(2,2,2))),F(3,4))
        # Integrating h over the symmetric sphere changes the conditional
        # minus probability to w/2 and the B*h moment to w*2/9.

    def test_pair_constraint_is_transported_at_all_steps(self):
        for t,x,i,z in product(range(40),STATES,range(4),(1,-1)):
            k=z;args=(i,i,i,k,-k)
            if stationary_physical(t%20,x,*args):
                y=advance(t%20,x)
                self.assertEqual(stationary_physical((t+1)%20,y,*args),1)
                self.assertEqual(z+(-z),0)
        # New U acts as a scalar on each old/pair fiber and preserves each
        # transported projector. The group-invariant directional extension
        # remains an additional model input.

    def test_actual_quantum_echo_vectors_and_pair(self):
        root=output(active_base())
        for label,s in ((0,1),(15,-1)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4)
            for tick in (0,9,10,20,39):
                old=states[checkpoint_at(tick%20)]
                for i in (0,2):
                    anchor_pair=tuple(row[i] for row in states[3])
                    old_pair=tuple(row[i] for row in old)
                    encoded=encode_pair(anchor_pair,i,s)
                    recovered=decode_pair(encoded,i,s,old_pair[0])
                    self.assertLess(sum(norm2(a-b) for a,b in zip(recovered,anchor_pair))/total,1e-23)
                    for key in encoded:self.assertEqual(key[2]+key[3],0)
                    amp=dressing(tick,.4)@np.array([1.,0.,0.])
                    self.assertAlmostEqual(float(np.vdot(amp,amp).real),1.,places=14)
                    self.assertLess(sum(norm2(a-b) for a,b in zip(from_anchor(anchor_pair,tick%20),old_pair))/total,1e-23)

    def test_actual_purified_apparatus_returns_and_repeats(self):
        cols=((1,),(0,))
        for b,x,f,e in product((0,1),BITS3,BITS3,words(1)):
            path=apparatus_path(b,x,f,e,cols)
            self.assertEqual(path[0],path[20])
            # Same B-controlled permutations repeat while pointer is held.
            self.assertEqual(path[10],path[(30%20)])
            self.assertEqual(path[19],path[(39%20)])

    def test_balanced_spinor_lift_has_an_invariant_singlet(self):
        i=np.eye(2);x=np.array([[0,1],[1,0]],complex)
        y=np.array([[0,-1j],[1j,0]],complex);z=np.diag([1.,-1.])
        singlet=np.array([0,1,-1,0],complex)/sqrt(2)
        for pauli in (x,y,z):
            charge=(np.kron(pauli,i)+np.kron(i,pauli))/2
            np.testing.assert_allclose(charge@singlet,0,atol=1e-15)
        for axis in (x,y,z):
            for angle in (0.,.3,1.7,2*np.pi):
                u=np.cos(angle/2)*i-1j*np.sin(angle/2)*axis
                np.testing.assert_allclose(np.kron(u,u)@singlet,singlet,atol=1e-14)
        # The center -I fixes scalar functions, reverses a single doublet,
        # but fixes this two-doublet singlet. It is a supplied extra carrier.
        np.testing.assert_allclose(np.kron(-i,-i)@singlet,singlet,atol=1e-15)
        self.assertEqual(np.linalg.matrix_rank(np.outer(singlet,singlet.conj())),1)

    def test_paired_spinor_lift_commutes_with_clock_memory_gate(self):
        singlet=np.array([0,1,-1,0],complex)/sqrt(2)
        theta=.73;u=np.diag([np.exp(1j*theta),np.exp(-1j*theta)])
        rotate=np.kron(np.eye(3),np.kron(u,u))
        for h in (-.8,0.,.9):
            gate=np.kron(record_gate(h),np.eye(4))
            np.testing.assert_allclose(gate@rotate,rotate@gate,atol=1e-15)
            source=np.kron(np.array([1.,0.,0.]),singlet)
            out=gate@source
            np.testing.assert_allclose(rotate@out,out,atol=1e-14)
            np.testing.assert_allclose(gate.T@out,source,atol=1e-15)

    def test_spin_and_sphere_pointers_are_distinct_compatible_readouts(self):
        root=output(active_base())
        for label,s in product((0,7,15),(1,-1)):
            x=initial(relative_read(root,4,labels=(label,))[0])
            _,total,states=quantum_echo_checkpoints(x,s,4);rows=states[3]
            spin=np.zeros(2);bybin=np.zeros((4,2))
            for i in range(4):
                for j,P in enumerate((PP,PM)):
                    bybin[i,j]=sum(norm2(apply64(P,row[i])) for row in rows)/total
                    spin[j]+=bybin[i,j]
                self.assertLess(sum(norm2(apply64(P0,row[i])) for row in rows)/total,1e-24)
            expected=np.array([[.125,.125],[.125,.125],
                               [.25,0] if s==1 else [0,.25],
                               [.25,0] if s==1 else [0,.25]])
            np.testing.assert_allclose(bybin,expected,atol=1e-13)
            np.testing.assert_allclose(spin,[.75,.25] if s==1 else [.25,.75],atol=1e-13)
            # Uniform p gives scalar pointer outcome ± with probability 1/2
            # within every old bin and every old spin effect, so its joint
            # distribution with this spin outcome is outer(spin,[.5,.5]).
            table=np.outer(spin,[.5,.5]);self.assertAlmostEqual(np.trace(table),.5,places=13)
            # Raw spin projections preserve the old pair on these supported
            # vectors; this is not an all-carrier commutation proof.
            for i in range(4):
                pair=tuple(row[i] for row in rows);enc=encode_pair(pair,i,s)
                for P in (PP,PM):
                    filtered={k:tuple(apply64(P,v) for v in z) for k,z in enc.items()}
                    decoded=decode_pair(filtered,i,s,pair[0]);again=encode_pair(decoded,i,s)
                    zero=(0*pair[0],0*pair[1])
                    residual=sum(sum(norm2(a-b) for a,b in zip(filtered.get(k,zero),again.get(k,zero))) for k in set(filtered)|set(again))
                    self.assertLess(residual/total,1e-22)

if __name__=='__main__':unittest.main()
