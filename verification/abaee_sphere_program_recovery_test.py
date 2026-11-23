"""Finite checks of process-program and reference-resolution distinctions.

No proof of the whole paper, no empirical experience identity, and no
inference from a conditional quantum model to metaphysical impossibility.
"""
import math
import unittest
from verification.zero_spin_constitution_test import X,Y,Z,add,close,eye,inner,mm,mv,scale
from verification.zero_invariant_sphere_instrument_test import adj
from verification.zero_spherical_plenitude_opposite_records_test import (
    PAIR,TETRA,op,projector,recorded,vecnorm,
)


def sub(a,b): return add(a,scale(-1,b))
def trace(a): return sum(a[i][i] for i in range(len(a)))
def dot(a,b): return sum(x*y for x,y in zip(a,b))


def cap_effect(center,delta,sign=1):
    # Exact angular integration of a uniform normalized spherical cap.
    c=(1+math.cos(delta))/2
    n=add(add(scale(center[0],X),scale(center[1],Y)),scale(center[2],Z))
    return scale(.5,add(eye(2),scale(sign*c,n)))


def cap_midpoint_mean(delta,ntheta=200,nphi=360):
    # Independent angular quadrature for cap about +z; integration weight
    # sin θ dθ dφ, normalized by its independently summed mass.
    norm=0.; z=0.; x=0.; y=0.
    for i in range(ntheta):
        theta=delta*(i+.5)/ntheta
        s=math.sin(theta); c=math.cos(theta)
        for j in range(nphi):
            phi=2*math.pi*(j+.5)/nphi
            norm+=s
            x+=s*s*math.cos(phi); y+=s*s*math.sin(phi); z+=s*c
    return x/norm,y/norm,z/norm


class AbaeeSphereProgramRecoveryTests(unittest.TestCase):
    def test_channel_state_space_affine_dimension_qubit(self):
        # Channel(E,E): e²(e²−1)=12; states on m-dimensional system: m²−1.
        e=2; target=e*e*(e*e-1)
        self.assertEqual(target,12)
        self.assertFalse(any(m*m-1==target for m in range(1,100)))
        self.assertEqual(e**4-e**2+1,13)

    def test_affine_dimension_gap_for_all_small_nontrivial_sizes(self):
        for e in range(2,100):
            v=e**4-e**2+1
            self.assertLess((e*e-1)**2,v)
            self.assertLess(v,(e*e)**2)

    def test_distinct_sharp_measurements_force_orthogonal_programs(self):
        # tr(P_n+ P_m-)=|<+_n|-_m>|²=(1−n·m)/2 > 0
        # for distinct n,m; perfect opposite classical outcomes then force
        # <program_n|program_m>=0 by isometric overlap preservation.
        for n in TETRA+PAIR:
            for m in TETRA+PAIR:
                if n==m: continue
                overlap=trace(mm(projector(n,1),projector(m,-1))).real
                self.assertAlmostEqual(overlap,(1-dot(n,m))/2)
                self.assertGreater(overlap,1e-9)

    def test_finite_restricted_family_can_be_programmed_exactly(self):
        # Classical orthogonal program of four allowed directions; the same
        # block-diagonal processor works for arbitrary logical input.
        n=8
        u=[[0j]*n for _ in range(n)]
        for j,direction in enumerate(TETRA):
            # For pointer outcome +, the block effect is P_+(n).
            p=projector(direction,1)
            for a in range(2):
                for b in range(2): u[2*j+a][2*j+b]=p[a][b]
        for j,direction in enumerate(TETRA):
            block=[[u[2*j+a][2*j+b] for b in range(2)] for a in range(2)]
            close(self,block,projector(direction,1))
        close(self,mm(u,u),u)
        # This is a fixed PVM effect, with program |j> fixing its block;
        # it does not implement all directions with this finite register.

    def test_cap_normalization_and_analytic_mean(self):
        delta=math.pi/3
        x,y,z=cap_midpoint_mean(delta)
        self.assertAlmostEqual(x,0,places=10); self.assertAlmostEqual(y,0,places=10)
        self.assertAlmostEqual(z,(1+math.cos(delta))/2,places=5)
        self.assertAlmostEqual((1-math.cos(delta))/2,.25) # cap measure

    def test_cap_gives_unsharp_not_exact_target_measurement(self):
        center=(0,0,1); delta=math.pi/3
        plus=cap_effect(center,delta); minus=cap_effect(center,delta,-1)
        close(self,add(plus,minus),eye(2))
        c=(1+math.cos(delta))/2
        self.assertAlmostEqual(c,.75)
        # Worst-case difference in a + outcome probability equals operator
        # norm of E_plus−P_plus = (1−c)/2, attained by Z eigenstates.
        error=(1-c)/2
        self.assertAlmostEqual(error,1/8)
        self.assertAlmostEqual(abs(plus[0][0]-1),error)
        self.assertAlmostEqual(abs(plus[1][1]),error)
        self.assertAlmostEqual((1-math.cos(delta))/4,error)
        close(self,cap_effect(center,math.pi),scale(.5,eye(2)))

    def test_cap_accuracy_improves_but_nonzero_for_positive_width(self):
        ds=(math.pi/2,math.pi/4,math.pi/8,math.pi/16)
        errors=[(1-math.cos(d))/4 for d in ds]
        self.assertTrue(all(e>0 for e in errors))
        self.assertTrue(all(errors[i]>errors[i+1] for i in range(len(errors)-1)))
        self.assertLess(errors[-1],.005)

    def test_finite_reference_superposition_keeps_opposite_records(self):
        # Four mutually orthogonal reference labels, arbitrary coherent
        # complex amplitudes, and a single matched-direction processor.
        ws=[.5,.5j,-.5,.5j]
        self.assertAlmostEqual(sum(abs(w)**2 for w in ws),1)
        total=add(op(Z,2),op(Z,3))
        for w,n in zip(ws,TETRA):
            v=[w*x for x in recorded(n)]
            self.assertAlmostEqual(vecnorm(mv(total,v)),0)
        # This exact correlation does not imply a continuum of selectable
        # exact projective measurements in finite program dimension.

    def test_complementary_record_channel_is_input_dependent(self):
        # Coherent CNOT copy |0>|0>→|00>, |1>|0>→|11>: discarding
        # the pointer yields dephasing, while the complementary pointer
        # channel distinguishes |0> and |1>.
        p0=projector((0,0,1),1); p1=projector((0,0,1),-1)
        rho_plus=scale(.5,[[1,1],[1,1]])
        dephased=add(mm(mm(p0,rho_plus),p0),mm(mm(p1,rho_plus),p1))
        close(self,dephased,scale(.5,eye(2)))
        self.assertNotAlmostEqual(abs(dephased[0][1]-rho_plus[0][1]),0)
        # Hence no recovery from the reduced channel for all inputs: |+>
        # and |-> have identical outputs; their missing coherent information
        # remains recoverable only if the full coherent dilation is retained.
        rho_minus=scale(.5,[[1,-1],[-1,1]])
        close(self,add(mm(mm(p0,rho_minus),p0),mm(mm(p1,rho_minus),p1)),dephased)

    def test_recorded_complement_can_be_uncomputed_globally(self):
        # Previous complete unitary is self-inverse per factor; distinguish
        # physical reversal with the pointer from reduced-channel recovery.
        from verification.zero_spherical_plenitude_opposite_records_test import record_unitary, initial
        n=TETRA[0]; ua=record_unitary(n,0,2); ub=record_unitary(n,1,3)
        v=mv(ua,mv(ub,recorded(n)))
        self.assertAlmostEqual(vecnorm([a-b for a,b in zip(v,initial())]),0)

if __name__=='__main__': unittest.main()
