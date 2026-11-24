"""Autonomous pointer coupled inside a positive-root FLRW constraint.

The homogeneous, band-projected model and its physical norm are defined
analytically. A Chebyshev/midpoint discretization checks selected values;
no local field detector, stable irreversible record, subject or total energy
is derived. Uses only Python's standard library and existing project modules.
"""
import cmath
import math
import unittest

from verification.zero_sphere_finite_resolution_clock_instrument_test import (
    mesh, effects, apply, dot
)
from verification.zero_sphere_flrw_normalizable_clock_test import omega
from verification.zero_five_ray_record_current_unification_test import (
    joint_state, local_density, norm2, probabilities
)
from verification.zero_sphere_mismatch_experience_comparison_test import subject_density
from verification.zero_sphere_relativistic_relational_time_test import components,initial
from verification.zero_spin_constitution_test import close

LAMBDA=.4


def translated(f,p,x0=-15):
    return [a*cmath.exp(-1j*x*x0) for a,x in zip(f,p)]


def spectral_interval(lam):
    # For p in (-7,-6), h in {0,1}, ||E||<=1.
    return 6-2-2*abs(lam), 49/6+2*abs(lam)


def root_evolution(p,E,h,d,t,v,lam=LAMBDA,degree=120,quadrature=256):
    """exp(i t sqrt(Theta_h,d))v, using Chebyshev quadrature.

    Theta_h,d = p²/6 - 2h - 2 lam d E. The interval bounds the
    spectrum by the continuum operator inequalities. Nystrom matrices are
    checked separately for contraction in tests.
    """
    lo,hi=spectral_interval(lam)
    if lo <= 0: raise ValueError('the chosen interval is not positive')
    c=(hi+lo)/2; r=(hi-lo)/2
    theta=[math.pi*(j+.5)/quadrature for j in range(quadrature)]
    sample=[cmath.exp(1j*t*math.sqrt(c+r*math.cos(x))) for x in theta]
    coeff=[2/quadrature*sum(z*math.cos(k*x) for z,x in zip(sample,theta))
           for k in range(degree)]
    def x_action(w):
        ew=apply(E,w)
        return [((p[i]**2/6-2*h-c)*w[i]-2*lam*d*ew[i])/r for i in range(len(p))]
    t0=list(v)
    out=[coeff[0]*x/2 for x in t0]
    if degree==1:return out
    t1=x_action(t0)
    out=[a+coeff[1]*b for a,b in zip(out,t1)]
    for k in range(2,degree):
        xt=x_action(t1)
        t2=[2*x-y for x,y in zip(xt,t0)]
        out=[a+coeff[k]*b for a,b in zip(out,t2)]
        t0,t1=t1,t2
    return out


def channel(p,E,f,t,lam=LAMBDA,degree=120):
    """Initial logical amplitudes (1,i)/sqrt2; pointer starts in |0_z>."""
    result=[]
    for h in (0,1):
        up=root_evolution(p,E,h,1,t,f,lam,degree)
        um=root_evolution(p,E,h,-1,t,f,lam,degree)
        result.append(([ (a+b)/2 for a,b in zip(up,um) ],
                       [ 1j*(a-b)/2 for a,b in zip(up,um) ]))
    return result


def p_pointer_one(ch):
    return sum(dot(ch[h][1],ch[h][1]).real/2 for h in (0,1))


def p_pointer_zero(ch):
    return sum(dot(ch[h][0],ch[h][0]).real/2 for h in (0,1))


def logical_y(ch, r=None):
    rs=(0,1) if r is None else (r,)
    # c0*=1/sqrt2, c1=i/sqrt2 => Y=Re(sum <u0|u1>).
    numerator=sum(dot(ch[0][j],ch[1][j]).real for j in rs)
    prob=sum(sum(dot(ch[h][j],ch[h][j]).real/2 for h in (0,1)) for j in rs)
    return numerator/prob if prob>1e-14 else None


def pointer_at_reading(ch,r):
    return sum(dot(ch[h][r],ch[h][r]).real/2 for h in (0,1))


def branch_constraint_expectation(p,E,h,d,t,v,lam=LAMBDA,degree=120):
    """Each norm is represented on the specified on-shell root; return
    gravitational, scalar and interaction constraint contributions."""
    u=root_evolution(p,E,h,d,t,v,lam,degree)
    eu=apply(E,u)
    e=dot(u,eu).real
    pp=sum(abs(x)**2*p0*p0 for x,p0 in zip(u,p))
    theta_u=[(p0*p0/6-2*h)*x-2*lam*d*y for p0,x,y in zip(p,u,eu)]
    grav=-pp/12
    scalar=dot(u,theta_u).real/2
    internal=h*dot(u,u).real
    interaction=lam*d*e
    return grav,scalar,internal,interaction


class AutonomousSphereDetectorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p,cls.f,cls.dp=mesh(40)
        cls.E=effects(cls.p,cls.dp)[0][0]
        cls.f=translated(cls.f,cls.p)
        cls.t40=channel(cls.p,cls.E,cls.f,40)
        cls.t100=channel(cls.p,cls.E,cls.f,100)

    def test_positive_root_and_hermitian_coupling(self):
        lo,hi=spectral_interval(LAMBDA)
        self.assertGreater(lo,0)
        self.assertGreater(hi,49/6)
        for i,row in enumerate(self.E):
            for j,x in enumerate(row):self.assertAlmostEqual(x,self.E[j][i])
        # E is a compressed multiplication by a function in [0,1]; hence
        # spectral inequalities hold in the continuum, independently of tests.

    def test_interaction_is_not_diagonal_in_free_geometry_momentum(self):
        ev=apply(self.E,self.f)
        p2v=[p*p*x for p,x in zip(self.p,self.f)]
        ep2=apply(self.E,p2v)
        comm=[p*p*x-y for p,x,y in zip(self.p,ev,ep2)]
        self.assertGreater(dot(comm,comm).real,1e-6)
        # The free p->p_phi Jacobian clock switch does not diagonalize this
        # interacting root; its reuse would silently discard the coupling.

    def test_zero_coupling_is_the_original_scalar_clock(self):
        for h in (0,1):
            u=root_evolution(self.p,self.E,h,1,40,self.f,lam=0)
            direct=[v*cmath.exp(1j*omega(p,h)*40) for v,p in zip(self.f,self.p)]
            self.assertLess(sum(abs(x-y)**2 for x,y in zip(u,direct)),1e-20)
        zero=channel(self.p,self.E,self.f,40,lam=0)
        self.assertAlmostEqual(p_pointer_one(zero),0,places=13)
        self.assertAlmostEqual(p_pointer_zero(zero),1,places=12)

    def test_initial_pointer_and_unitary_probability(self):
        initial=channel(self.p,self.E,self.f,0)
        self.assertAlmostEqual(p_pointer_one(initial),0,places=13)
        for ch in (initial,self.t40,self.t100):
            self.assertAlmostEqual(p_pointer_zero(ch)+p_pointer_one(ch),1,places=11)
            self.assertGreaterEqual(p_pointer_one(ch),0)
            self.assertLessEqual(p_pointer_one(ch),1)

    def test_chebyshev_convergence(self):
        for h,d in ((0,1),(0,-1),(1,1),(1,-1)):
            for t in (100,120):
                u=root_evolution(self.p,self.E,h,d,t,self.f,degree=120)
                v=root_evolution(self.p,self.E,h,d,t,self.f,degree=160)
                self.assertLess(sum(abs(x-y)**2 for x,y in zip(u,v)),1e-19)
                self.assertAlmostEqual(dot(u,u).real,1,places=11)

    def test_pointer_record_forms_from_internal_dynamics(self):
        initial=channel(self.p,self.E,self.f,0)
        self.assertAlmostEqual(p_pointer_one(initial),0,places=12)
        self.assertGreater(p_pointer_one(self.t40),.001)
        self.assertGreater(p_pointer_one(self.t100),p_pointer_one(self.t40))
        self.assertGreater(p_pointer_one(self.t100),.01)
        def overlap(ch):
            return sum(dot(ch[h][r],apply(self.E,ch[h][r])).real/2
                       for h in (0,1) for r in (0,1))
        self.assertGreater(overlap(self.t40),.23)
        self.assertLess(overlap(self.t100),.0001)

    def test_traversal_control_and_midpoint_convergence(self):
        p,f,dp=mesh(80); E=effects(p,dp)[0][0]
        traversing=channel(p,E,translated(f,p,-15),100)
        receding=channel(p,E,translated(f,p,15),100)
        self.assertAlmostEqual(p_pointer_one(traversing),.9588787979078999,places=9)
        self.assertAlmostEqual(p_pointer_one(receding),.0007605443459403026,places=9)
        self.assertLess(abs(p_pointer_one(traversing)-p_pointer_one(self.t100)),3e-5)
        # These are two preparations, not perfectly sharp path alternatives.

    def test_two_pointer_readouts_show_finite_record_persistence(self):
        earlier=channel(self.p,self.E,self.f,80)
        yes=p_pointer_one(earlier); flip=0.0
        for h in (0,1):
            recorded=earlier[h][1]
            up=root_evolution(self.p,self.E,h,1,40,recorded)
            um=root_evolution(self.p,self.E,h,-1,40,recorded)
            flipped=[-1j*(a-b)/2 for a,b in zip(up,um)]
            flip+=dot(flipped,flipped).real/2
        self.assertGreater(yes,.95)
        self.assertLess(flip/yes,5e-5)
        # A projective reading at 80 is assumed; persistence is conditional
        # on it and on this interval, not indefinitely or irreversibly.

    def test_on_shell_constraint_after_interaction(self):
        for h in (0,1):
            for d in (-1,1):
                for t in (0,40,100):
                    vals=branch_constraint_expectation(self.p,self.E,h,d,t,self.f)
                    self.assertAlmostEqual(sum(vals),0,places=12)
                    initial=branch_constraint_expectation(self.p,self.E,h,d,0,self.f)
                    self.assertAlmostEqual(vals[1],initial[1],places=11)
        # This is the spectral constraint identity, not a unique definition
        # of the whole's objective total energy.

    def test_joint_constraint_balance_in_pointer_basis(self):
        p2=sum(abs(self.t40[h][r][i])**2*p*p/2
               for h in (0,1) for r in (0,1) for i,p in enumerate(self.p))
        grav=-p2/12
        interaction=LAMBDA*sum(dot(self.t40[h][0],apply(self.E,self.t40[h][1])).imag
                               for h in (0,1))
        scalar_initial=sum(branch_constraint_expectation(self.p,self.E,h,d,0,self.f)[1]/4
                           for h in (0,1) for d in (-1,1))
        self.assertAlmostEqual(grav,-3.51921,places=4)
        self.assertAlmostEqual(interaction,-.00460,places=4)
        self.assertAlmostEqual(grav+scalar_initial+.5+interaction,0,places=10)

    def test_actual_pointer_effect_is_not_assumed_previous_e_squared(self):
        centered=translated(self.f,self.p,15)  # undo initial shift x0=-15
        centered_norm=dot(apply(self.E,centered),apply(self.E,centered)).real
        actual=channel(self.p,self.E,centered,0)
        self.assertGreater(centered_norm,.25)
        self.assertAlmostEqual(p_pointer_one(actual),0,places=12)
        # Different operational times and effects are not identified by fiat.

    def test_nonideal_record_and_logical_backaction(self):
        p1=p_pointer_one(self.t100)
        y0=logical_y(self.t100,0); y1=logical_y(self.t100,1)
        self.assertTrue(0<p1<1)
        self.assertGreater(abs(y0-y1),.005)
        self.assertAlmostEqual((1-p1)*y0+p1*y1,logical_y(self.t100),places=11)

    def test_reversibility_is_not_irreversible_memory(self):
        for h,d in ((0,1),(1,-1)):
            u=root_evolution(self.p,self.E,h,d,40,self.f)
            recovered=root_evolution(self.p,self.E,h,d,-40,u)
            self.assertLess(sum(abs(x-y)**2 for x,y in zip(recovered,self.f)),1e-19)

    def test_confined_state_and_receiver_match_for_all_logical_inputs(self):
        triple=components(initial(joint_state('triple')))
        pair=components(initial(joint_state('pair')))
        a,b=triple[:2]
        ref=subject_density([x*math.sqrt(2) for x in a])
        tab=probabilities([x*math.sqrt(2) for x in a])
        for c,d in ((1,0),(0,1),(1,1),(1,1j)):
            v=[c*x+d*y for x,y in zip(a,b)];n=norm2(v)
            close(self,[[x/n for x in row] for row in subject_density(v)],ref)
            for k,x in probabilities(v).items():self.assertAlmostEqual(x/n,tab[k])
            vp=[c*x+d*y for x,y in zip(pair[0],pair[1])]
            close(self,local_density(v),local_density(vp))

if __name__=='__main__': unittest.main()
