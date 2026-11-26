"""Reference shifts and relational observables in compact FLRW minisuperspace.

Exact rational algebra for a specified classical GR-plus-scalar model; these
checks do not derive GR, measure cosmic energy, or establish any experience.
"""
from fractions import Fraction as F
from itertools import product
import unittest

KAPPA=F(6)


def constraint(a,pa,pphi,vacuum_potential,cosmological_constant):
    return (-KAPPA*pa**2/(12*a) + pphi**2/(2*a**3) +
            a**3*(vacuum_potential+cosmological_constant/KAPPA))


def derivatives(a,pa,pphi,vacuum_potential,cosmological_constant):
    """(∂C/∂a, ∂C/∂pa, ∂C/∂pphi); constant potential, so ∂C/∂phi=0."""
    u=vacuum_potential+cosmological_constant/KAPPA
    return (KAPPA*pa**2/(12*a**2) - 3*pphi**2/(2*a**4) + 3*a**2*u,
            -KAPPA*pa/(6*a), pphi/a**3)


def local_quantities(a,pa,pphi,vacuum_potential,cosmological_constant):
    """Matter/effective density, proper Hubble squared, da/dphi for pphi ≠ 0."""
    rho_m=pphi**2/(2*a**6)+vacuum_potential
    rho_eff=rho_m+cosmological_constant/KAPPA
    h2=(KAPPA*pa/(6*a**2))**2
    slope=(-KAPPA*pa/(6*a))/(pphi/a**3)
    return rho_m,rho_eff,h2,slope


class ZeroConstraintReferenceRecoveryTests(unittest.TestCase):
    def test_compensating_constant_moves_between_terms_not_the_full_action(self):
        for a,pa,p, v, lam,delta in product(
            (F(1,2),F(1),F(2)), (F(-2),F(0),F(1)), (F(-1),F(1)),
            (F(0),F(1)), (F(0),F(3)), (F(-1,3),F(0),F(2))):
            c=constraint(a,pa,p,v,lam)
            cp=constraint(a,pa,p,v+delta,lam-KAPPA*delta)
            self.assertEqual(c,cp)  # valid off shell as well
            self.assertEqual(derivatives(a,pa,p,v,lam),
                             derivatives(a,pa,p,v+delta,lam-KAPPA*delta))
            rho,rhoeff,h2,slope=local_quantities(a,pa,p,v,lam)
            rho2,rhoeff2,h22,slope2=local_quantities(a,pa,p,v+delta,lam-KAPPA*delta)
            self.assertEqual(rho2,rho+delta) # split-dependent label
            self.assertEqual((rhoeff,h2,slope),(rhoeff2,h22,slope2))

    def test_uncompensated_shift_changes_physical_constraint(self):
        for a in (F(1,2),F(1),F(2)):
            for delta in (F(-1),F(1,3),F(2)):
                before=constraint(a,F(-1),F(1),F(0),F(0))
                after=constraint(a,F(-1),F(1),delta,F(0))
                self.assertEqual(after-before,a**3*delta)
                if before==0:
                    self.assertNotEqual(after,0)

    def test_two_zero_constraint_histories_have_distinct_relational_expansion(self):
        # Same kappa, a, pphi and branch; distinct effective vacuum U.
        cases=((F(0),F(-1),F(1,2),F(1),F(1)),
               (F(3,2),F(-2),F(2),F(4),F(2)))
        for u,pa,rho,h2,slope in cases:
            self.assertEqual(constraint(F(1),pa,F(1),u,F(0)),0)
            rho_m,rho_eff,actual_h2,actual_slope=local_quantities(F(1),pa,F(1),u,F(0))
            self.assertEqual((rho_m,rho_eff,actual_h2,actual_slope),(rho,rho,h2,slope))
            self.assertEqual(h2,KAPPA*rho_eff/3)
            self.assertGreater(rho_eff,0)
            self.assertGreater(slope,0)
        self.assertNotEqual(cases[0][3:],cases[1][3:])

    def test_equal_constraint_zero_does_not_equal_local_quasilocal_energy(self):
        # Spatially flat FLRW: Misner-Sharp E/π = 4 H² R³/κ.
        # Coordinate volume one torus and a=1: R=1/4 lies in a local ball.
        radius=F(1,4)
        values=[]
        for pa,u in ((F(-1),F(0)),(F(-2),F(3,2))):
            self.assertEqual(constraint(F(1),pa,F(1),u,F(0)),0)
            _,rho,h2,_=local_quantities(F(1),pa,F(1),u,F(0))
            geometric=4*h2*radius**3/KAPPA
            density=F(4,3)*radius**3*rho
            self.assertEqual(geometric,density)
            self.assertGreater(geometric,0)
            values.append(geometric)
        self.assertEqual(values,[F(1,96),F(1,24)])

    def test_lapse_constraint_rescaling_preserves_on_shell_flow(self):
        # C'=f(a) C, f=a³; rescale lapse N'=N/f. The additional
        # ∂f·C term vanishes on the original constraint surface.
        for a,pa,p in ((F(1),F(-1),F(1)),(F(2),F(-1,2),F(1)),
                       (F(1),F(-2),F(1))):
            # U is chosen to put each specified physical state on shell.
            u=(KAPPA*pa**2/(12*a)-p**2/(2*a**3))/a**3
            c=constraint(a,pa,p,u,F(0)); self.assertEqual(c,0)
            dcda,dcdpa,dcdp=derivatives(a,pa,p,u,F(0))
            factor=a**3; dfda=3*a*a
            # flow of H'=N' fC, with N held to 1 and N'=1/f
            self.assertEqual((factor*dcdpa)/factor,dcdpa)
            self.assertEqual(-(factor*dcda+c*dfda)/factor,-dcda)
            self.assertEqual((factor*dcdp)/factor,dcdp)
            self.assertNotEqual(dcdp,0)  # scalar is a local monotonic clock
        # Away from C=0, the ∂f term means fixed-lapse vector fields need not
        # agree; no off-shell gauge equivalence is asserted.
        a=F(1); c=constraint(a,F(0),F(1),F(0),F(0))
        self.assertNotEqual(c,0)
        self.assertNotEqual(c*3*a*a/a**3,0)


if __name__=='__main__':
    unittest.main()
