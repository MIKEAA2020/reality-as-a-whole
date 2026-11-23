"""Retained surface labels and optional quantum interface on the five-ray state.

A specified memory rule and finite unitary circuits; no fundamental time,
actual consciousness, derived metaphysical planes, or physical wormholes.
"""
import math
import unittest
from fractions import Fraction as F
from itertools import product
from verification.zero_five_ray_record_current_unification_test import (
    joint_state, probabilities, local_density, norm2, apply_work, index
)
from verification.zero_reciprocal_subject_exchange_test import J
from verification.zero_spin_constitution_test import close, inner

A=(F(1),F(0),F(0)); B=(F(-1),F(0),F(0))

def chord(t): return (1-2*t,F(0),F(0))
def alternate(t): return (1-2*t,2*t*(1-t),F(0))
def sqnorm(x): return sum(y*y for y in x)
def retained(t,start=A,end=B):
    # Rule for one specifically declared excursion; not radial projection.
    return start if t<1 else end

def hidden(phi):
    # H P(phi) H |0>, where P=diag(1,exp(i phi)).
    z=complex(math.cos(phi),math.sin(phi))
    return [(1+z)/2,(1-z)/2]

def tensor(v,w): return [x*y for x in v for y in w]
def trace_hidden(v):
    # v contains [|0,0>,|0,1>,|1,0>,|1,1>], record then H
    return [[sum(v[2*r+h]*v[2*s+h].conjugate() for h in range(2))
             for s in range(2)] for r in range(2)]
def untouched(psi): return tensor(psi,[1,0,0,0])
def rich_after(psi,phi):
    v=hidden(phi)
    return tensor(psi,[v[0],v[1],0,0])
def fixed_update(psi,phi):
    v=hidden(phi)
    return tensor(psi,[0,0,v[0],v[1]])
def coupled_update(psi,phi):
    # CNOT: target = record R, control = H; R starts |0>.
    v=hidden(phi)
    return tensor(psi,[v[0],0,0,v[1]])

def ancilla_density(v):
    # Trace original 640-dimensional five-ray state.
    return [[sum(v[4*k+i]*v[4*k+j].conjugate() for k in range(len(v)//4))
             for j in range(4)] for i in range(4)]

def record_density(v):
    d=ancilla_density(v)
    return [[sum(d[2*i+h][2*j+h] for h in range(2)) for j in range(2)] for i in range(2)]

def original_marginal(v):
    # Enough for exact table and work-current checks: summed norms and
    # expectation of J are computed without tracing Alice's pointer separately.
    return [[v[4*k+r] for k in range(len(v)//4)] for r in range(4)]

class ConfinedRealmsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.triple=joint_state('triple'); cls.pair=joint_state('pair')

    def test_surface_label_retained_on_true_chord(self):
        for n in range(17):
            t=F(n,16); x=chord(t)
            self.assertEqual(retained(t),A if n<16 else B)
            self.assertLessEqual(sqnorm(x),1)
            if 0<n<16: self.assertLess(sqnorm(x),1)
        self.assertEqual(chord(F(0)),A); self.assertEqual(chord(F(1)),B)

    def test_multiple_room_routes_have_the_same_confined_history(self):
        for n in range(17):
            t=F(n,16); x=alternate(t)
            if 0<n<16:
                self.assertLess(sqnorm(x),1)
                self.assertNotEqual(x,chord(t))
            self.assertEqual(retained(t),A if t<1 else B)
        self.assertEqual(alternate(F(0)),A); self.assertEqual(alternate(F(1)),B)

    def test_retained_position_is_history_not_geometric_projection(self):
        # Forward and reverse meet at identical room point. Their retained
        # surface descriptions differ; no function of position alone does this.
        t=F(1,2); self.assertEqual(chord(t),chord(1-t))
        self.assertEqual(retained(t,A,B),A)
        self.assertEqual(retained(t,B,A),B)
        self.assertNotEqual(A,B)

    def test_duration_retiming_leaves_half_move_order_unchanged(self):
        # An ordered half-move sequence can have any positive rational dwell
        # times. Event labels and the move clock do not determine these times.
        moves=('e4','e5','Nf3','Nc6')
        schedules=[]
        for durations in ((F(1),F(2),F(1),F(2)),(F(100),F(1,2),F(5),F(9))):
            times=[F(0)]
            for d in durations: times.append(times[-1]+d)
            self.assertTrue(all(a<b for a,b in zip(times,times[1:])))
            schedules.append(times)
        self.assertNotEqual(schedules[0],schedules[1])
        # Move-index at every point before the first event stays zero despite
        # the distinct elapsed durations in the two schedules.
        for times in schedules:
            tick=lambda elapsed:sum(event<=elapsed for event in times[1:])
            self.assertEqual(tick(times[1]/2),0)
            self.assertEqual([tick(t) for t in times],list(range(len(moves)+1)))
        self.assertNotEqual(schedules[0][1]-schedules[0][0],schedules[1][1]-schedules[1][0])

    def test_confinement_covaries_when_the_geometry_and_labels_are_transported(self):
        # An actual rotation (x,y,z)->(-y,x,z); both endpoints and room curve
        # must be transported, not just the names A and B.
        rot=lambda x:(-x[1],x[0],x[2])
        for n in range(17):
            t=F(n,16)
            self.assertEqual(rot(retained(t)),retained(t,rot(A),rot(B)))
            self.assertEqual(sqnorm(rot(alternate(t))),sqnorm(alternate(t)))

    def test_hidden_phase_does_not_change_register_before_interface(self):
        for psi in (self.pair,self.triple):
            for phi in (0,math.pi/2,math.pi):
                v=rich_after(psi,phi)
                self.assertAlmostEqual(norm2(v),1)
                close(self,record_density(v),[[1,0],[0,0]])
        # Hidden states after phase-and-recombination are genuinely distinct
        # as rays within the stipulated tensor factor, not global phases.
        self.assertAlmostEqual(abs(inner(hidden(0),hidden(math.pi))),0)

    def test_inaccessible_setting_remains_indistinguishable_at_completion(self):
        # Both protocols have the same fixed final X on R; arbitrary hidden
        # phases are invisible to all R-only operations in this product circuit.
        for phi in (0,math.pi/2,math.pi):
            v=fixed_update(self.triple,phi)
            close(self,record_density(v),[[0,0],[0,1]])
        self.assertNotEqual(ancilla_density(fixed_update(self.triple,0)),
                            ancilla_density(fixed_update(self.triple,math.pi)))

    def test_specified_interface_exposes_phase_only_at_the_update(self):
        for phi,want in ((0,0),(math.pi/2,.5),(math.pi,1)):
            before=rich_after(self.triple,phi); after=coupled_update(self.triple,phi)
            close(self,record_density(before),[[1,0],[0,0]])
            d=record_density(after)
            self.assertAlmostEqual(d[1][1].real,want)
            self.assertAlmostEqual(d[0][0].real,1-want)
            self.assertAlmostEqual(abs(d[0][1]),0)
            self.assertAlmostEqual(norm2(after),1)

    def test_both_extensions_preserve_five_ray_table_and_current(self):
        for phi in (0,math.pi/2,math.pi):
            for full in (rich_after(self.triple,phi),fixed_update(self.triple,phi),coupled_update(self.triple,phi)):
                blocks=original_marginal(full)
                p0=probabilities(self.triple)
                for key in p0:
                    self.assertAlmostEqual(sum(probabilities(block)[key] for block in blocks),p0[key])
                jv=[apply_work(block,J[0]) for block in blocks]
                current=sum(inner(block,jblock).real for block,jblock in zip(blocks,jv))
                self.assertAlmostEqual(current,0)
                for i in range(5):
                    for r,sign in ((1,1),(2,-1)):
                        # Joint branchwise current follows by tensor-product
                        # commutation with all gates of the new ancillas.
                        for block,jblock in zip(blocks,jv):
                            for a,b,w in product(range(2),range(2),range(16)):
                                k=index(a,b,i,r,w)
                                self.assertAlmostEqual(abs(jblock[k]-sign*block[k]),0)

    def test_alice_choice_does_not_change_bob_state_or_output(self):
        close(self,local_density(self.pair),local_density(self.triple))
        for phi in (0,math.pi/2,math.pi):
            for proc in (rich_after,fixed_update,coupled_update):
                close(self,ancilla_density(proc(self.pair,phi)),ancilla_density(proc(self.triple,phi)))
        # Full Bob+ancilla equality follows by product factorization; all
        # ancilla gates are Bob-local with respect to the stipulated lab split.

if __name__=='__main__': unittest.main()
