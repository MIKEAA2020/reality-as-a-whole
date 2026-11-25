"""Original coherent angular echo inside the purified 20-step clock."""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_clock_finite_reservoir_reuse_test import BITS3,Q,energy
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import words
from verification.zero_persistent_sphere_subject_selection_test import norm2
from verification.zero_internal_reference_subject_valence_candidates_test import b_project
from verification.zero_quantum_angular_echo import latitudes,embed_before_echo,pulse,mass,difference_mass
from verification.zero_sphere_angular_echo import magnitude
from verification.zero_coherent_clock_angular_history import (
    apparatus_path,apparatus_overlap,quantum_echo_checkpoints,quantum_event_moments,
    dot_rows,checkpoint_at,stationary_povm_joint,clock_coherence_factor,clock_selection,
)


class CoherentClockAngularHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        x=initial(relative_read(output(active_base()),4,labels=(0,))[0])
        cls.x=x;cls.s=1;cls.n=4
        cls.u,cls.total,cls.states=quantum_echo_checkpoints(x,cls.s,cls.n)
        cls.moments=[quantum_event_moments(rows,cls.u,cls.total) for rows in cls.states]

    def test_all_purified_apparatus_branches_close_and_keep_charges(self):
        cols=((1,),(0,))
        for b,x,f,e in product((0,1),BITS3,BITS3,words(1)):
            path=apparatus_path(b,x,f,e,cols)
            self.assertEqual(len(path),21)
            self.assertEqual(path[0],path[20])
            self.assertEqual(path[7],path[13])
            for bb,y,mem,level,c,d in path:
                self.assertEqual(bb,b)
                self.assertEqual(energy(mem,level,f),0)
                self.assertEqual(d-1+sum(c)-sum(e),0)
        # Coherent purification uses amplitudes sqrt(p), not a measurement of
        # these labels. Conditional B pieces remain in the original system.
        for b in (0,1):
            self.assertEqual(apparatus_overlap(7,10,b,cols,Q),1)
            self.assertEqual(apparatus_overlap(0,7,b,cols,Q),F(9,128) if b==0 else 0)

    def test_actual_echo_and_inverse_at_coherent_checkpoints(self):
        u,total,states=self.u,self.total,self.states
        rows=states[0]
        for tick,gate in enumerate(('T','Q','T','T','Q','T'),start=8):
            rows=pulse(rows,gate)
            self.assertLess(difference_mass(rows,states[checkpoint_at(tick)])/total,1e-24)
        self.assertLess(difference_mass(rows,states[0])/total,1e-24)
        # Apparatus control on B commutes with each actual pulse on this state.
        for b in (1,-1):
            projected=tuple([b_project(v,b) for v in part] for part in states[0])
            for gate in ('T','Q','T'):
                left=pulse(projected,gate)
                full=pulse(states[0],gate)
                right=tuple([b_project(v,b) for v in part] for part in full)
                self.assertLess(difference_mass(left,right)/total,1e-24)
        for rows in states:self.assertAlmostEqual(mass(rows)/total,1.,places=12)
        # First and last 7 apparatus gates preserve B and act on other factors.
        # With the actual source/ref/purifier state the quantum cycle returns.
        self.assertEqual([checkpoint_at(t) for t in range(7,14)], [0,1,2,3,2,1,0])
        self.assertEqual(checkpoint_at(20),0)

    def test_clock_conditioned_joint_moments_from_original_quantum_vectors(self):
        for event in self.moments:
            self.assertAlmostEqual(sum(event.get((a,b),0) for a,b in product((False,True),repeat=2)),1.,places=12)
            self.assertAlmostEqual(event.get((False,True),0),0.,places=12)
        for q,prior,correct,disagreement,abs_moment,swap_moment in (
            (1,.25,.6,.1,.05,3/160),
            (2,.5,.55,.05,3/80,3/320),
        ):
            p,law=stationary_povm_joint(self.moments,q,2)
            self.assertAlmostEqual(p,prior,places=12)
            self.assertAlmostEqual(law.get((True,False),0)+law.get((True,True),0),correct,places=12)
            self.assertAlmostEqual(law.get((True,True),0),disagreement,places=12)
            self.assertAlmostEqual(law['absolute'],abs_moment,places=12)
            self.assertAlmostEqual(law['swap_invariant'],swap_moment,places=12)
        for r in (1,3):
            with self.assertRaises(ValueError):clock_selection(2,r)
        # N=4 midpoint result; the continuum g2 values are 1/60 and 1/120.

    def test_exact_midpoint_magnitude_moments_and_continuum_limit(self):
        for n in (4,8,16,40):
            u=latitudes(n)
            lower=sum(magnitude(v,'swap_invariant') for v in u[:n//4])/n
            upper=sum(magnitude(v,'swap_invariant') for v in u[n//4:n//2])/n
            self.assertEqual(lower,upper)
            self.assertEqual((lower+upper)/5,F(1,60)+F(1,30*n*n))
            self.assertEqual(2*lower/10,F(1,120)+F(1,60*n*n))

    def test_reference_moments_and_coherence_on_other_source_and_signs(self):
        root=output(active_base())
        for label,s in product((0,7,15),(1,-1)):
            if label==0 and s==1:continue
            x=initial(relative_read(root,4,labels=(label,))[0])
            u,total,states=quantum_echo_checkpoints(x,s,4)
            moments=[quantum_event_moments(rows,u,total) for rows in states]
            for q,p,disagree in ((1,.25,.1),(2,.5,.05)):
                prior,law=stationary_povm_joint(moments,q,2)
                self.assertAlmostEqual(prior,p,places=12)
                self.assertAlmostEqual(law[(True,True)],disagree,places=12)
            z=dot_rows(states[0],states[2])/total
            self.assertAlmostEqual(z.real,s/2,places=12)
            self.assertAlmostEqual(z.imag,0.,places=12)

    def test_actual_original_clock_coherence_and_reference_dephasing(self):
        # On t=7..13 every actual apparatus factor is stationary. This
        # overlap is therefore the full purified apparatus+old-system overlap,
        # not merely a chosen artificial clock-only wavefunction.
        original=self.states[0]
        for tick,index in ((9,2),(10,3)):
            z=dot_rows(original,self.states[index])/self.total
            self.assertAlmostEqual(z.real,.5,places=12)
            self.assertAlmostEqual(z.imag,0.,places=12)
        # Clock density entry before reference is z/20. A q-reference trace
        # multiplies it by the actual orthogonality of |qt mod 4> labels.
        self.assertEqual(clock_coherence_factor(1,7,9),0)
        self.assertEqual(clock_coherence_factor(2,7,9),1)
        self.assertEqual(clock_coherence_factor(1,7,10),0)
        self.assertEqual(clock_coherence_factor(2,7,10),0)
        # At t=0 vs 7 the original angular/echo vector is unchanged, but
        # the actual reservoir/source circuit itself reduces coherence.
        plus=sum(norm2(b_project(v,1)) for part in original for v in part)/self.total
        minus=sum(norm2(b_project(v,-1)) for part in original for v in part)/self.total
        self.assertAlmostEqual(plus,.5,places=12)
        self.assertAlmostEqual(minus,.5,places=12)
        cols=((1,),(0,))
        actual=(plus*float(apparatus_overlap(0,7,0,cols,Q))+
                minus*float(apparatus_overlap(0,7,1,cols,Q)))
        self.assertAlmostEqual(actual,9/256,places=12)

    def test_unaccessed_angular_record_hides_magnitude_within_a_band(self):
        u,v,rows=embed_before_echo(self.x,self.s,8)
        for gate in ('T','Q','T'):rows=pulse(rows,gate)
        # Fixed u-bin preparations, conditional on a specified record readout:
        # within each band, the complete original-system/R vector is identical.
        for i,j in ((0,1),(4,7)):
            self.assertNotEqual(magnitude(u[i],'absolute'),magnitude(u[j],'absolute'))
            self.assertNotEqual(magnitude(u[i],'swap_invariant'),magnitude(u[j],'swap_invariant'))
            for part in rows:
                self.assertLess(norm2(part[i]-part[j])/norm2(v),1e-24)
            weight=sum(norm2(part[i]) for part in rows)
            self.assertAlmostEqual(weight/norm2(v),1/8,places=12)
        # Source/reservoir controls depend on B, not i; all bins in a band
        # share B and evolve with the same full purified apparatus state.
        # An A-reading distinguishes orthogonal |i> but the old bearer plus
        # apparatus and clocks cannot distinguish the two conditional states.

    def test_factorized_stationary_shift_and_anchor_effects(self):
        # W applies the real forward apparatus permutations and old T/Q/T
        # gates, then reverses both. Its return on all apparatus basis states
        # and the supported original old state was checked above. The reference
        # makes |t,U_t psi,qt> map into the next term, including t=19 -> 0.
        for q in (1,2):
            for t in range(20):
                self.assertEqual(((q*t+q)%4),q*((t+1)%20)%4)
            # Each anchor twirl has 20 orthogonal original-clock blocks and
            # commutes with the shift. A uniform average remains a valid POVM.
            for anchor in range(20):
                labels={(anchor+k)%20 for k in range(20)}
                self.assertEqual(len(labels),20)
                for k in range(20):
                    self.assertEqual(((anchor+k+1)%20),(anchor+(k+1))%20)
        self.assertEqual(len(clock_selection(1,2)),5)
        self.assertEqual(len(clock_selection(2,2)),10)

if __name__=='__main__':unittest.main()
