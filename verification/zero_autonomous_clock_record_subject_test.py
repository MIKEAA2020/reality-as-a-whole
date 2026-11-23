"""Autonomous cyclic clock, zero-sector record and incidence controls.

The clock and all logical blocks embed in the spin-zero sectors constructed in
previous tests. No classical selected history or phenomenology is derived.
"""
import math
import unittest
from fractions import Fraction as F
from verification.zero_spin_constitution_test import add, close, eye, mm, mv, scale
from verification.zero_invariant_sphere_instrument_test import adj
from verification.zero_sector_memory_incidence_test import Q
from verification.zero_sector_record_energy_exchange_test import (
    E, H0, comm, maxabs, records_state, state_exp, unitary,
)


def sub(a,b): return add(a,scale(-1,b))
def expect(v,a): return sum(x.conjugate()*y for x,y in zip(v,mv(a,v)))
def ket(i,n=4): return [complex(i==j) for j in range(n)]

I=eye(4)
A=[[complex((j-i)%4 in (1,3)) for j in range(4)] for i in range(4)]
P=[[complex(i==j and i in (1,2)) for j in range(4)] for i in range(4)]
D=scale(1j,comm(A,P))


def clock_state(t):
    return [math.cos(t)**2,-1j*math.sin(t)*math.cos(t),
            -math.sin(t)**2,-1j*math.sin(t)*math.cos(t)]


def alpha_derivative(t):
    return [-math.sin(2*t),-1j*math.cos(2*t),
            -math.sin(2*t),-1j*math.cos(2*t)]


def flag_probabilities(): return (Q[0]+Q[2],Q[1]+Q[2])

class AutonomousClockRecordSubjectTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.u=unitary(math.pi/2)
        cls.zero=records_state(0)
        cls.written=records_state(math.pi/2)

    def test_cyclic_history_gate_is_consistent_and_energy_conserving(self):
        u=self.u; ud=adj(u)
        # V0=U, V1=I, V2=U†, V3=I: closed ring has trivial holonomy.
        close(self,mm(ud,u),eye(48))
        close(self,mm(u,ud),eye(48))
        self.assertLess(maxabs(comm(u,H0)),1e-10)
        # Every history state remains in the prepared H0=2 sector.
        for state in (self.zero,self.written):
            for k,v in state.items(): self.assertEqual(sum(k[3:]),2)

    def test_full_clock_work_hamiltonian_propagates_correlated_history(self):
        # H_CW = K(A⊗I)K†, K=Σ|t><t|⊗V_t. Work uses the actual 48×48
        # encoded record unitary, not only a formal four-clock matrix.
        vs=(eye(48),self.u,self.u,eye(48))
        phi=[0j]*48
        phi[5]=1/math.sqrt(2); phi[37]=1j/math.sqrt(2)
        for s in range(4):
            source=mv(vs[s],phi)
            outputs=[]
            for t in range(4):
                if A[t][s]: outputs.append(mv(vs[t],mv(adj(vs[s]),source)))
                else: outputs.append([0j]*48)
            for t in range(4):
                expected=mv(vs[t],phi) if A[t][s] else [0j]*48
                for actual,want in zip(outputs[t],expected):
                    self.assertAlmostEqual(abs(actual-want),0)

    def test_clock_state_follows_autonomous_schrodinger_equation(self):
        for t in (0,.2,math.pi/4,math.pi/2,math.pi):
            v=clock_state(t)
            rhs=[-1j*x for x in mv(A,v)]
            for x,y in zip(rhs,alpha_derivative(t)): self.assertAlmostEqual(abs(x-y),0)
            self.assertAlmostEqual(sum(abs(x)**2 for x in v),1)
        close(self,[[x] for x in clock_state(math.pi/2)],[[0],[0],[-1],[0]])
        close(self,[[x] for x in clock_state(math.pi)],[[1],[0],[0],[0]])

    def test_clock_conditioned_history_contains_written_and_blank_states(self):
        # Gauge-rotated clock basis: work φ0, Uφ0, Uφ0, φ0.
        # Verify the conditional record states supplied by the actual U.
        for k,v in self.zero.items(): self.assertEqual(k[3:],(0,1,0,1))
        p=[0.,0.,0.]
        for (a,b,r,m1,w1,m2,w2),v in self.written.items():
            self.assertEqual(m1,int(r in (0,2)))
            self.assertEqual(m2,int(r in (1,2)))
            self.assertEqual(w1,1-m1); self.assertEqual(w2,1-m2)
            p[r]+=abs(v)**2
        for actual,expected in zip(p,Q): self.assertAlmostEqual(actual,float(expected))
        # Conditional states exist only when the relevant clock probability
        # is nonzero; this is not a definite sequence of observed ticks.

    def test_clock_conditioned_no_signalling_is_not_remote_control(self):
        from verification.zero_sector_record_energy_exchange_test import reduced_b
        close(self,reduced_b(self.zero),scale(.5,eye(2)))
        close(self,reduced_b(self.written),scale(.5,eye(2)))
        # Conditioning on internal clock states is not a freely chosen,
        # relativistically localized operation; only reduced-state equality.

    def test_unconditional_energy_and_currents_are_recurrent(self):
        for t in (0,.2,math.pi/4,math.pi/2,3*math.pi/4,math.pi):
            clock=clock_state(t)
            written_weight=abs(clock[1])**2+abs(clock[2])**2
            self.assertAlmostEqual(written_weight,math.sin(t)**2)
            for j,p in enumerate(flag_probabilities()):
                initial=state_exp(self.zero,3+2*j)
                final=state_exp(self.written,3+2*j)
                self.assertAlmostEqual(initial,0)
                self.assertAlmostEqual(final,float(p))
                self.assertAlmostEqual(written_weight*final,float(p)*math.sin(t)**2)
                self.assertAlmostEqual(expect(clock,scale(float(p),D)).real,float(p)*math.sin(2*t))
        # Closed cycle net gain of every individual memory and battery is zero.
        self.assertAlmostEqual(abs(clock_state(math.pi)[0]),1)

    def test_clock_current_has_bounded_nonnegative_incidence_operator(self):
        # In the cyclic history subspace, D=i[A,P] and D²=I.
        close(self,mm(D,D),I)
        lam=F(1,2)
        w=add(I,scale(float(lam),D))
        # W is positive: W=(1+λ)P_+ +(1-λ)P_- with P±=(I±D)/2.
        plus=scale(.5,add(I,D)); minus=scale(.5,sub(I,D))
        close(self,mm(plus,plus),plus)
        close(self,mm(minus,minus),minus)
        close(self,w,add(scale(1+float(lam),plus),scale(1-float(lam),minus)))
        self.assertLess(maxabs(comm(w,D)),1e-10)
        for t in (0,.4,math.pi/2,2.5):
            c=clock_state(t)
            self.assertAlmostEqual(expect(c,w).real,1+float(lam)*math.sin(2*t))
            self.assertAlmostEqual(expect(c,mm(w,D)).real,math.sin(2*t)+float(lam))
        # Over t∈[0,π], ∫⟨D⟩dt=0 but ∫⟨WD⟩dt=λπ.

    def test_history_energy_compression_yields_p_times_clock_current(self):
        # Work at clock 0,3 is blank; at 1,2 the same written state.
        # Hence P_hist N_M P_hist = p P and, since the history subspace is
        # invariant under H, P_hist i[H,N_M] P_hist = p i[A,P].
        for j,p in enumerate(flag_probabilities()):
            actual=state_exp(self.written,3+2*j)
            self.assertAlmostEqual(actual,float(p))
            compressed_energy=scale(actual,P)
            compressed_current=scale(1j,comm(A,compressed_energy))
            close(self,compressed_current,scale(float(p),D))
            # Battery has 1-pP, and its current is -pD.
            close(self,scale(1j,comm(A,sub(I,compressed_energy))),scale(-float(p),D))

    def test_nonuniform_quantum_incidence_leaves_exact_cycle_remainder(self):
        # W=I+λD for memory and I for battery, common history subspace.
        # Symmetrized contribution is p(D+λI)-pD=pλ I for each pair.
        lam=.5
        w=add(I,scale(lam,D))
        for p in flag_probabilities():
            jm=scale(float(p),D); jw=scale(-float(p),D)
            total=add(scale(.5,add(mm(w,jm),mm(jm,w))),jw)
            close(self,total,scale(float(p)*lam,I))
        # Common W for both ends instead preserves zero identically.
        close(self,add(mm(w,D),mm(w,scale(-1,D))),scale(0,I))

    def test_minimal_energy_closed_sets_are_the_two_memory_battery_pairs(self):
        # Candidate rule: a subset is closed if its bare energy commutes
        # with the writing unitary. This is not a general subject criterion.
        closed=[]
        for mask in range(16):
            n=scale(0,eye(48))
            for i in range(4):
                if mask & (1<<i): n=add(n,E[i])
            if maxabs(comm(self.u,n))<1e-9: closed.append(mask)
        self.assertEqual(closed,[0,3,12,15])
        self.assertEqual([mask for mask in closed if mask and not any(
            submask and submask != mask and submask & mask == submask for submask in closed)], [3,12])

    def test_subject_boundary_rules_give_different_record_incidence(self):
        p1,p2=flag_probabilities()
        self.assertEqual((p1,p2),(F(3,5),F(7,8)))
        bits=(p1,-p1,p2,-p2)
        # Four individual systems as subjects: opposite contributions zero.
        self.assertEqual(sum(bits),0)
        # Only memories as subjects: uncompensated transfer from batteries.
        self.assertEqual(bits[0]+bits[2],F(59,40))
        # Each entire energy pair as one subject, valued by its net change:
        # two subjects exist but each has zero signed contribution.
        self.assertEqual((bits[0]+bits[1],bits[2]+bits[3]),(0,0))

    def test_whole_cycle_weights_do_not_select_record_history(self):
        words=([0]*5+[1]*16+[2]*19,[2]*19+[1]*16+[0]*5)
        self.assertNotEqual(words[0],words[1])
        for word in words:
            self.assertEqual(tuple(F(word.count(i),40) for i in range(3)),Q)
        # Such words require a record-selection and relational-order account;
        # neither one is supplied by the pure quantum model.

if __name__=='__main__': unittest.main()
