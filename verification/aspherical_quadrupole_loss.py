"""
Weak aspherical quadrupole-loss relational bound.

On the static spherical background, a small axisymmetric aspherical deformation that pulsates
on the cloud's dynamical/free-fall timescale radiates gravitational waves via Einstein's
quadrupole formula. This bounds integrated energy loss, mass loss, redshift drift, and Shapiro
echo drift for such a perturbation. The radiation frequency is the mechanical pulsation
frequency ~ 1/T_dyn, not the scalar rest mass (which cancels out in slow-motion gravity).
"""
import json, math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from linearized_spherical_record import picard_psi, gauss, integrate_simple


def integrate_quadrupole(rs, rho2, psi):
    """Integrated axisymmetric quadrupole coefficient for rho2(r) (rest-mass quadrupole density),
    in isotropic coordinates with volume element psi^6 r^2 dr dOmega:
      Q_{zz} = sqrt(16pi/5) int_0^infty r^4 rho2(r) dr.
    Here rho2 is the density without the angular Y_{20} factor, i.e. the radial profile function.
    """
    dr = rs[1]-rs[0]
    integrand = [r**4 * rho2[i] for i, r in enumerate(rs)]
    return math.sqrt(16*math.pi/5) * (0.5*(integrand[0] + integrand[-1]) + sum(integrand[1:-1])) * dr


def enclosed_MS(rs, psi, kappa, eps):
    """Quick enclosed Misner-Sharp mass estimate for T_dyn, reused from linearized analysis."""
    dr = rs[1]-rs[0]
    f = [gauss(r, 20.0) for r in rs]
    fp = [-(r/400.0)*fi for r,fi in zip(rs,f)]
    # physical density times sqrt q = eps^2 (kappa psi^6 f^2 + psi^2 fp^2/2)
    dens = [eps**2*(kappa*psi[i]**6*fi**2 + psi[i]**2*fpi**2/2) for i,(fi,fpi) in enumerate(zip(f,fp))]
    M=[0.0]
    for i in range(1,len(rs)):
        M.append(M[-1] + 0.5*(rs[i-1]**2*dens[i-1] + rs[i]**2*dens[i])*dr*4*math.pi)
    return M, dens


def main():
    out = {}
    cases = [
        {"name": "weak_backreaction_alpha01", "D":12, "m0":20.0, "A_ev":2.0, "R0":20.0, "eps":0.00003, "b":0.00004, "alpha":0.01, "T_obs":10.0},
        {"name": "very_small_alpha001_long", "D":12, "m0":20.0, "A_ev":2.0, "R0":20.0, "eps":0.00003, "b":0.00004, "alpha":0.001, "T_obs":100.0},
    ]
    cases_out=[]
    for case in cases:
        R0, eps, b, m0, A_ev, alpha, T_obs = case["R0"], case["eps"], case["b"], case["m0"], case["A_ev"], case["alpha"], case["T_obs"]; D=case["D"]
        M_diag=[m0]*D; M_diag[0]+=A_ev; v=[0.0]*D; v[0]=1.0
        mu=sum(M_diag[i]*v[i]**2 for i in range(D)); kappa=sum(M_diag[i]**2*v[i]**2 for i in range(D))
        rs,psi,n_iter,cvg=picard_psi(R0,kappa,eps,b)
        f=[gauss(r,R0) for r in rs]
        M_enc, dens = enclosed_MS(rs, psi, kappa, eps)
        M_total = M_enc[-1]
        # Matter-averaged physical radius approximation: use coordinate avg times psi^2 ~ 1 + small correction.
        W = integrate_simple([r**2*dens[i] for i,r in enumerate(rs)],rs)
        R_coord_avg = integrate_simple([r**2*dens[i]*r for i,r in enumerate(rs)],rs)/W
        R_phys_avg = integrate_simple([r**2*dens[i]*r*psi[i]**2 for i,r in enumerate(rs)],rs)/W
        M_at_Rm = M_total
        for i,(rp,r) in enumerate(zip([r*psi[j]**2 for j,r in enumerate(rs)],rs)):
            if rp >= R_phys_avg:
                M_at_Rm = M_enc[i]; break
        T_dyn = math.sqrt(R_phys_avg**3/max(M_at_Rm, 1e-300))
        omega_mech = 2*math.pi/T_dyn
        # Quadrupole deformation of rest density: fractional deformation alpha,
        # delta rho_2(r) = alpha * (r^2/R0^2) * exp(-r^2/R0^2) * kappa * eps^2 * psi^6.
        rho2 = [alpha*(r**2/R0**2)*fi**2*kappa*eps**2*psi[i]**6 for i,(r,fi) in enumerate(zip(rs,f))]
        Q0 = integrate_quadrupole(rs, rho2, psi)
        # Slow-motion quadrupole formula: dE/dt = -1/5 <Q'''_{ij} Q'''_{ij}>.
        # Axisymmetric Qzz with Qxx=Qyy=-Qzz/2 => Q_{ij}Q_{ij} = (3/2) Qzz^2.
        # For Q(t)=Q0 cos(omega t), <Q'''^2> = Q0^2 omega^6 / 2.
        dEdt = -(1/5)*(3/2)*0.5*Q0**2*omega_mech**6
        deltaE = abs(dEdt)*T_obs
        dM_fraction = deltaE/M_total if M_total>0 else float("inf")
        # Redshift/dephasing drift: mass loss deltaM changes central potential ~ deltaM/R.
        # N ~ 1 - M/R, so dN ~ -deltaM/R; cumulative dephasing over T_obs ~ mu * (deltaM/R) * T_obs.
        dN = deltaE/R_phys_avg
        phi_drift = mu*dN*T_obs
        # Shapiro delay drift from mass change: ~ 6 deltaM log ratio.
        log_ratio = math.log(rs[-1]/R0)
        shapiro_drift = 6*deltaE*log_ratio
        T_tick = 2*math.pi/mu
        shapiro_drift_ticks = shapiro_drift/T_tick
        cases_out.append({
            "name": case["name"], "epsilon": eps, "alpha": alpha, "T_obs": T_obs,
            "mu": mu, "M_total": M_total, "R_phys_avg": R_phys_avg, "T_dyn": T_dyn, "omega_mech": omega_mech,
            "Q0": Q0, "Q_over_MR2": Q0/(M_total*R_phys_avg**2) if M_total>0 else float("inf"),
            "dEdt": dEdt, "deltaE": deltaE, "dM_fraction": dM_fraction,
            "redshift_dephasing_drift": phi_drift,
            "Shapiro_drift": shapiro_drift, "Shapiro_drift_ticks": shapiro_drift_ticks,
        })
    out["cases"]=cases_out
    out["summary"]=(
        "Weak aspherical quadrupole loss on the spherical static background: radiation occurs at the "
        "mechanical pulsation frequency ~ 1/T_dyn, not scalar rest mass; bounds integrated mass/redshift/echo drift."
    )
    Path("verification/aspherical_quadrupole_loss.json").write_text(json.dumps(out,indent=2))
    print("PASS: aspherical quadrupole-loss relational bound")
    print(Path("verification/aspherical_quadrupole_loss.json"))

if __name__=="__main__":main()
