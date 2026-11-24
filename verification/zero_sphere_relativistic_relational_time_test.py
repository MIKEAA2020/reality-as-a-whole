"""Sphere-record clock under finite relational and relativistic constraints.

Numerical finite-sector checks of specified special/static backgrounds, not a
quantization of full GR, proof of global energy zero, or experience detection.
"""
import cmath
import math
import unittest
from fractions import Fraction as F
from itertools import product
from verification.zero_five_ray_record_current_unification_test import (
    joint_state,probabilities,local_density,apply_work,norm2,index
)
from verification.zero_sphere_mismatch_experience_comparison_test import subject_density,phase_flip
from verification.zero_confinement_coherence_experience_test import phase_state
from verification.zero_reciprocal_subject_exchange_test import J,proj
from verification.zero_spin_constitution_test import close,inner

M=3.0
N=5


def add(a,b): return [x+y for x,y in zip(a,b)]
def sub(a,b): return [x-y for x,y in zip(a,b)]
def scale(c,a): return [c*x for x in a]
def kval(v):
    jv=apply_work(v,J[0]); out=[]
    for a,b,i,r,w in product(range(2),range(2),range(5),range(4),range(16)):
        out.append((1-2*((r>>1)&1))*jv[index(a,b,i,r,w)])
    return out

def yval(v): return scale(-1j,kval(phase_flip(v)))

def components(v):
    p=apply_work(v,proj); k=kval(v)
    return scale(.5,add(p,k)),scale(.5,sub(p,k)),sub(v,p)

def energies(p,m=M): return tuple(math.sqrt(p*p+(m+h)**2) for h in (0,1,.5))
def lapse_energies(lapse,m=M): return tuple(lapse*(m+h) for h in (0,1,.5))

def frw_energies(p_alpha=-6.0):
    # Positive scalar momentum p_phi=+sqrt(p_alpha^2/6−2 h); reduced
    # Hamiltonian for increasing phi is H_phi=−p_phi. Real sector only.
    return tuple(-math.sqrt(p_alpha*p_alpha/6-2*h) for h in (0,1,.5))

def advance(v,t,es):
    out=[0j]*len(v)
    for part,e in zip(components(v),es): out=add(out,scale(cmath.exp(-1j*e*t),part))
    return out

def initial(v): return phase_state(v,math.pi/4)
def sequence(v,es): return [scale(1/math.sqrt(N),advance(v,k,es)) for k in range(N)]
def hinner(a,b): return sum(inner(x,y) for x,y in zip(a,b))

def prop(blocks,es):
    out=[[0j]*len(blocks[0]) for _ in range(N)]
    for k in range(N-1):
        residual=sub(blocks[k+1],advance(blocks[k],1,es))
        out[k+1]=add(out[k+1],scale(.5,residual))
        out[k]=sub(out[k],scale(.5,advance(residual,-1,es)))
    return out

def edge_energy(blocks,es):
    return sum(norm2(sub(blocks[k+1],advance(blocks[k],1,es)))/2 for k in range(N-1))

def relative_y(blocks,k,es):
    # R_k(Y)=Σ_l |l><l| U(l−k)Y U(k−l) in the existing path model.
    return [advance(yval(advance(block,k-l,es)),l-k,es)
            for l,block in enumerate(blocks)]

def ymean(v): return inner(v,yval(v)).real/norm2(v)
def zmean(v): return inner(v,phase_flip(v)).real/norm2(v)
def normalized_matrix(a,p): return [[x/p for x in row] for row in a]


class SphereRelativisticRelationalTimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.triple=joint_state('triple'); cls.pair=joint_state('pair')
        cls.v=initial(cls.triple); cls.vp=initial(cls.pair)

    def test_internal_logical_clock_is_a_real_qubit_on_active_support(self):
        psi_plus=self.triple; psi_minus=phase_flip(psi_plus)
        self.assertAlmostEqual(abs(inner(psi_plus,psi_minus)),0)
        self.assertAlmostEqual(norm2(sub(kval(psi_plus),psi_plus)),0)
        self.assertAlmostEqual(norm2(add(kval(psi_minus),psi_minus)),0)
        self.assertAlmostEqual(norm2(sub(yval(yval(self.v)),self.v)),0)
        self.assertAlmostEqual(ymean(self.v),1)

    def test_positive_frequency_mass_shell_holds(self):
        for p in (0,4):
            for h,e in zip((0,1,.5),energies(p)):
                self.assertAlmostEqual(-e*e+p*p+(M+h)**2,0)
        e0,e1,_=energies(4)
        self.assertAlmostEqual(e0,5); self.assertAlmostEqual(e1,4*math.sqrt(2))
        self.assertAlmostEqual(e1-e0,4*math.sqrt(2)-5)

    def test_finite_relational_history_is_stationary_and_constraint_positive(self):
        for p in (0,4):
            es=energies(p); blocks=sequence(self.v,es)
            self.assertAlmostEqual(hinner(blocks,blocks).real,1)
            self.assertAlmostEqual(sum(norm2(x) for x in prop(blocks,es)),0)
            self.assertAlmostEqual(edge_energy(blocks,es),0)
            arbitrary=[scale(complex(k+1,1),x) for k,x in enumerate(blocks)]
            self.assertGreater(edge_energy(arbitrary,es),0)
            self.assertAlmostEqual(hinner(arbitrary,prop(arbitrary,es)).real,edge_energy(arbitrary,es))

    def test_constraint_commuting_relational_observable_matches_conditioning(self):
        for p in (0,4):
            es=energies(p); h=sequence(self.v,es)
            for k in range(N):
                obs=relative_y(h,k,es)
                self.assertAlmostEqual(hinner(h,obs).real,ymean(h[k]))
                before=prop(relative_y(h,k,es),es)
                after=relative_y(prop(h,es),k,es)
                self.assertAlmostEqual(sum(norm2(sub(x,y)) for x,y in zip(before,after)),0)
            # Also check commutation on a nonphysical state, not just ker(C).
            arbitrary=[scale(complex(k+1,1),x) for k,x in enumerate(h)]
            before=prop(relative_y(arbitrary,2,es),es)
            after=relative_y(prop(arbitrary,es),2,es)
            self.assertAlmostEqual(sum(norm2(sub(x,y)) for x,y in zip(before,after)),0)

    def test_confined_state_and_five_ray_table_fixed_for_all_clocks(self):
        expected=[(F(3,40),F(1,20)),(F(1,10),F(3,10)),(F(13,40),F(3,20))]
        reference=subject_density(self.triple)
        for p in (0,4):
            for block in sequence(self.v,energies(p)):
                q=norm2(block)
                close(self,normalized_matrix(subject_density(block),q),reference)
                table=probabilities(block)
                for i,(plus,minus) in enumerate(expected):
                    self.assertAlmostEqual(table[(i,1)]/q,float(plus))
                    self.assertAlmostEqual(table[(i,2)]/q,float(minus))

    def test_relative_clock_phase_exact_and_classical_limit(self):
        for p in (0,4):
            es=energies(p); delta=es[1]-es[0]
            for k in range(N):
                v=advance(self.v,k,es)
                self.assertAlmostEqual(ymean(v),math.cos(delta*k))
                self.assertAlmostEqual(zmean(v),math.sin(delta*k))
        for gap in (1e-2,1e-4,1e-6):
            rate=(math.hypot(4,3+gap)-5)/gap
            self.assertLess(abs(rate-F(3,5)),gap/10)
        self.assertGreater(abs((4*math.sqrt(2)-5)-F(3,5)),.05)

    def test_fixed_velocity_worldline_requires_spatial_phase(self):
        # Same v=4/5; two internal energies require different momenta.
        m=F(3); v=F(4,5); gamma=F(5,3); h=F(3,4)
        p0=gamma*v*m; p1=gamma*v*(m+h)
        e0=gamma*m; e1=gamma*(m+h)
        self.assertEqual((p0,p1,e0,e1),(F(4),F(5),F(5),F(25,4)))
        self.assertEqual((e1-e0)-v*(p1-p0),h/gamma)
        self.assertNotEqual(e1-e0,h/gamma)  # omitting p·x is wrong

    def test_superposed_momenta_dephase_reduced_clock_but_recover_conditionals(self):
        e0=energies(0); e4=energies(4)
        d0=e0[1]-e0[0]; d4=e4[1]-e4[0]
        t=math.pi/(d0-d4)
        v0=advance(self.v,t,e0); v4=advance(self.v,t,e4)
        y=(ymean(v0)+ymean(v4))/2; z=(zmean(v0)+zmean(v4))/2
        self.assertAlmostEqual(y,0); self.assertAlmostEqual(z,0)
        for v in (v0,v4):
            self.assertAlmostEqual(ymean(v)**2+zmean(v)**2,1)
        self.assertAlmostEqual(abs((cmath.exp(-1j*d0*t)+cmath.exp(-1j*d4*t))/2),0)

    def test_static_gravitational_redshift_is_recovered_when_assumed(self):
        n1=1.0; n2=1/math.sqrt(2)
        for t in (0,1,2,math.pi):
            a=advance(self.v,t,lapse_energies(n1))
            b=advance(self.v,t,lapse_energies(n2))
            self.assertAlmostEqual(ymean(a),math.cos(n1*t))
            self.assertAlmostEqual(ymean(b),math.cos(n2*t))
            close(self,subject_density(a),subject_density(b))
        self.assertAlmostEqual(n2/n1,1/math.sqrt(2))

    def test_same_null_cone_does_not_determine_proper_time_scale(self):
        dt,dx=F(6),F(3)
        base=dt*dt-dx*dx
        changed=4*base
        self.assertEqual(base,F(27)); self.assertEqual(changed,F(108))
        self.assertAlmostEqual(math.sqrt(changed),2*math.sqrt(base))
        for t,x in ((F(1),F(1)),(F(2),F(-2))):
            self.assertEqual(t*t-x*x,0); self.assertEqual(4*(t*t-x*x),0)

    def test_frw_constraint_positive_matter_and_exact_clock_balance(self):
        # At p_alpha=−6, h=0,1,1/2, p_phi²=6,4,5. The rescaled
        # gravitational, scalar and clock terms cancel on each sector.
        for h,p_phi_sq in ((F(0),F(6)),(F(1),F(4)),(F(1,2),F(5))):
            grav=F(-36,12); scalar=p_phi_sq/2
            self.assertEqual(grav+scalar+h,0)
            self.assertGreater(scalar,0)
            self.assertGreaterEqual(h,0)
        es=frw_energies()
        self.assertAlmostEqual(es[0],-math.sqrt(6))
        self.assertAlmostEqual(es[1],-2)
        self.assertAlmostEqual(es[1]-es[0],math.sqrt(6)-2)

    def test_frw_scalar_clock_history_preserves_sphere_data(self):
        es=frw_energies(); blocks=sequence(self.v,es)
        self.assertAlmostEqual(edge_energy(blocks,es),0)
        self.assertAlmostEqual(sum(norm2(x) for x in prop(blocks,es)),0)
        for k,block in enumerate(blocks):
            q=norm2(block)
            self.assertAlmostEqual(ymean(block),math.cos((math.sqrt(6)-2)*k))
            close(self,normalized_matrix(subject_density(block),q),subject_density(self.triple))
            table=probabilities(block); original=probabilities(self.triple)
            for key in original: self.assertAlmostEqual(table[key]/q,original[key])

    def test_frw_branch_domain_and_clock_orientation(self):
        # p_phi>0, p_alpha=−6 gives d(alpha)/d(phi)=1/p_phi > 0.
        for h,p_sq in ((0,6),(1,4)):
            p_phi=math.sqrt(p_sq)
            self.assertGreater(1/p_phi,0)
            self.assertAlmostEqual(p_sq,36/6-2*h)
        self.assertLess(36/6-2*4,0)  # energy 4 is outside this real sector

    def test_pair_triple_full_receiver_state_no_signalling(self):
        for es in (energies(0),energies(4),lapse_energies(1/math.sqrt(2)),frw_energies()):
            for t in (0,1,2):
                close(self,local_density(advance(self.v,t,es)),
                           local_density(advance(self.vp,t,es)))
        # The same receiver-side clock-history isometry transports equal full
        # initial receiver states to equal receiver+clock states.

    def test_global_energy_offset_is_not_fixed_by_relative_phase(self):
        for p in (0,4):
            e=energies(p); shifted=tuple(x+7 for x in e)
            for t in (0,1,2):
                v=advance(self.v,t,e); w=advance(self.v,t,shifted)
                for x,y in zip(v,w): self.assertAlmostEqual(abs(y-cmath.exp(-7j*t)*x),0)
                self.assertAlmostEqual(ymean(v),ymean(w))

if __name__=='__main__': unittest.main()
