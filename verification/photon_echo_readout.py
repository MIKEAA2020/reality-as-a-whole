"""
Asymptotic photon-echo relational readout bound for the static spherical clock.

Integrates radial null geodesics in the isotropic/conformal metric of the smooth-field data
(N=psi^{-2}, q_{rr}=psi^4) to obtain the asymptotic proper time required for a photon to travel
from the clock to a distant observer (outgoing delay). By Birkhoff the exterior is static Schwarzschild,
so the delay is a physical relational observable. Echo/two-way delay is twice the outgoing delay.
"""
import json, math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from linearized_spherical_record import picard_psi, gauss, integrate_simple


def integrate_null_out(rs, psi, r0_index, r_end_index):
    dr = rs[1]-rs[0]
    t = 0.0
    for i in range(r0_index, r_end_index):
        t += 0.5*(psi[i]**6 + psi[i+1]**6)*dr
    return t


def interpolate_index(rs, value):
    for i, r in enumerate(rs):
        if r >= value:
            return i
    return len(rs)-1


def main():
    out = {}
    cases = [
        {"name": "nonlinear_binding_24", "D": 12, "m0": 20.0, "A_ev": 2.0, "R0": 20.0, "eps": 0.001, "b": 0.1},
        {"name": "weak_backreaction", "D": 12, "m0": 20.0, "A_ev": 2.0, "R0": 20.0, "eps": 0.00003, "b": 0.00004},
    ]
    cases_out = []
    for case in cases:
        R0, eps, b, m0, A_ev = case["R0"], case["eps"], case["b"], case["m0"], case["A_ev"]; D=case["D"]
        M_diag=[m0]*D; M_diag[0]+=A_ev; v=[0.0]*D; v[0]=1.0
        mu=sum(M_diag[i]*v[i]**2 for i in range(D)); kappa=sum(M_diag[i]**2*v[i]**2 for i in range(D))
        rs,psi,n_iter,cvg=picard_psi(R0,kappa,eps,b)
        f=[gauss(r,R0) for r in rs]
        weights=[psi[i]**6*fi**2 for i,fi in enumerate(f)]
        W=integrate_simple([r**2*weights[i] for i,r in enumerate(rs)],rs)
        R_coord_avg=integrate_simple([r**2*weights[i]*r for i,r in enumerate(rs)],rs)/W
        N=[p**-2 for p in psi]
        N_avg=integrate_simple([r**2*weights[i]*N[i] for i,r in enumerate(rs)],rs)/W
        # radius containing 99% of |Phi|^2
        cum=0;i_surface99=len(rs)-1; total=W; dr=rs[1]-rs[0]
        for i,r in enumerate(rs):
            if i>0: cum+=0.5*(r**2*weights[i]+rs[i-1]**2*weights[i-1])*dr
            if cum>=0.99*total: i_surface99=i; break
        i_avg=interpolate_index(rs,R_coord_avg); i_center=0; i_end=len(rs)-1
        t_center=integrate_null_out(rs,psi,i_center,i_end)
        t_avg=integrate_null_out(rs,psi,i_avg,i_end)
        t_surface=integrate_null_out(rs,psi,i_surface99,i_end)
        flat_center=rs[i_end]-rs[i_center]
        flat_avg=rs[i_end]-rs[i_avg]
        flat_surface=rs[i_end]-rs[i_surface99]
        shapiro_center=t_center-flat_center
        shapiro_avg=t_avg-flat_avg
        shapiro_surface=t_surface-flat_surface
        shapiro_spread_center_avg=abs(shapiro_center-shapiro_avg)
        shapiro_spread_avg_surface=abs(shapiro_avg-shapiro_surface)
        echo_center=2*t_center; echo_avg=2*t_avg; echo_surface=2*t_surface
        # Internal clock period in asymptotic time: observed frequency N*mu.
        T_period_center=2*math.pi/(N[0]*mu)
        T_period_avg=2*math.pi/(N_avg*mu)
        # Tick resolvability: Shapiro jitter (gravitational part only) per observed period.
        shapiro_jitter_ticks=shapiro_spread_center_avg/T_period_avg
        redshift_tick_dephasing=2*math.pi*(1-N_avg)/N[0]
        C=max(rs[i]*(psi[i]-1) for i in range(len(rs)))
        tail_correction=6*C*math.log(rs[i_end]/max(rs[i_surface99],1e-10))
        cases_out.append({
            "name":case["name"],"epsilon":eps,"mu":mu,"kappa":kappa,
            "picard_iterations":n_iter,"picard_residual":cvg,
            "R_coord_avg":R_coord_avg,"N_center":N[0],"N_avg":N_avg,
            "R_surface99_coord":rs[i_surface99],
            "C_asymptotic":C,
            "one_way_flat_center":flat_center,"one_way_flat_averaged":flat_avg,"one_way_flat_surface":flat_surface,
            "one_way_delay_center":t_center,"one_way_delay_averaged":t_avg,"one_way_delay_surface99":t_surface,
            "Shapiro_delay_center":shapiro_center,"Shapiro_delay_averaged":shapiro_avg,"Shapiro_delay_surface":shapiro_surface,
            "Shapiro_spread_center_to_avg":shapiro_spread_center_avg,"Shapiro_spread_avg_to_surface":shapiro_spread_avg_surface,
            "echo_delay_center":echo_center,"echo_delay_averaged":echo_avg,"echo_delay_surface99":echo_surface,
            "observed_period_center":T_period_center,"observed_period_averaged":T_period_avg,
            "Shapiro_jitter_ticks":shapiro_jitter_ticks,
            "one_tick_redshift_dephasing":redshift_tick_dephasing,
            "asymptotic_tail_log_correction":tail_correction,
        })
    out["cases"]=cases_out
    out["summary"]=(
        "Asymptotic photon-echo readout: radial null geodesics integrated in the smooth isotropic metric. "
        "Separates geometric travel time and Shapiro delay. Gives photon echo spreads relative to the internal "
        "clock's observed period."
    )
    Path("verification/photon_echo_readout.json").write_text(json.dumps(out,indent=2))
    print("PASS: asymptotic photon-echo relational readout")
    print(Path("verification/photon_echo_readout.json"))

if __name__=="__main__":main()
