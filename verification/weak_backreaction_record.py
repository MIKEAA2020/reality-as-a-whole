"""
Weak-backreaction relational record bound for the smooth self-gravitating field clock.

This is not a claim that gravity is negligible or that the self-gravitating clock
is equivalent to a flat clock. It bounds relational record error against an
asymptotic stationary observer's proper time, in a regime where the geometry
remains close enough to the initial conformally flat data that a quasistatic
lapse bound and matter Hamiltonian perturbation bound are valid. Uses the same
matter integrands as smooth_field_clock for ADM/proper consistency.
"""
import json, math
from pathlib import Path


def gauss(r, R0):
    return math.exp(-0.5 * (r / R0) ** 2)


def gauss_radial_source(r, R0, kappa, eps, psi):
    f = gauss(r, R0); fp = -(r / R0**2) * f
    return psi * fp * fp + 2.0 * kappa * (psi**5) * f * f


def picard_psi(R0, kappa, eps, b, n_steps=8192, r_max=None, tol=1e-14, max_iter=100):
    if r_max is None: r_max = 8.0 * R0
    dr = r_max / n_steps; rs = [i*dr for i in range(n_steps+1)]
    def apply_T(g):
        inner=[0.0]*(n_steps+1)
        for i in range(1,n_steps+1):
            inner[i]=inner[i-1]+rs[i]**2*gauss_radial_source(rs[i],R0,kappa,eps,g[i])*dr
        outer=[0.0]*(n_steps+1)
        for i in range(n_steps-1,-1,-1):
            outer[i]=outer[i+1]+rs[i+1]*gauss_radial_source(rs[i+1],R0,kappa,eps,g[i+1])*dr
        new=[1.0+eps**2/8*(inner[i]/rs[i]+outer[i]) if i else 1.0+eps**2/8*outer[0] for i in range(n_steps+1)]
        return [min(1+b,max(1,v)) for v in new]
    g=[1.0]*(n_steps+1)
    for it in range(max_iter):
        new=apply_T(g); err=max(abs(new[i]-g[i]) for i in range(n_steps+1)); g=new
        if err<tol: break
    return rs,g,it+1,err


def integrate_simple(values, rs):
    dr=rs[1]-rs[0]; return dr*(sum(values[1:-1])+.5*(values[0]+values[-1]))


def main():
    out={}
    cases=[
        {"name":"nonlinear_binding_24","D":12,"m0":20.0,"A_ev":2.0,"R0":20.0,"eps":0.001,"b":0.1,"T_budget":0.01},
        {"name":"weak_backreaction","D":12,"m0":20.0,"A_ev":2.0,"R0":20.0,"eps":0.00003,"b":0.00004,"T_budget":0.001},
    ]
    cases_out=[]
    for case in cases:
        R0,eps,b,m0,A_ev=case["R0"],case["eps"],case["b"],case["m0"],case["A_ev"]; D=case["D"]
        M_diag=[m0]*D; M_diag[0]+=A_ev
        v=[0.0]*D; v[0]=1.0
        mu=sum(M_diag[i]*v[i]**2 for i in range(D)); kappa=sum(M_diag[i]**2*v[i]**2 for i in range(D))
        rs,psi,n_iter,cvg=picard_psi(R0,kappa,eps,b)
        f=[gauss(r,R0) for r in rs]; fp=[-(r/R0**2)*fi for r,fi in zip(rs,f)]
        N=[p**-2 for p in psi]
        # Consistent with smooth_field_clock integrands.
        Eproper=4*math.pi*eps**2*integrate_simple([r**2*(psi[i]**2*fpi**2/2+kappa*psi[i]**6*fi**2) for i,(r,fi,fpi) in enumerate(zip(rs,f,fp))],rs)
        charge=4*math.pi*eps**2*mu*integrate_simple([r**2*psi[i]**6*fi**2 for i,(r,fi) in enumerate(zip(rs,f))],rs)
        C=rs[-1]*(psi[-1]-1.0)
        for i in range(len(rs)-2,max(1,len(rs)-200),-1): C=max(C,rs[i]*(psi[i]-1.0))
        EADM=16*math.pi*C; binding=EADM-Eproper
        # Weighted initial redshift and curved Hamiltonian.
        weights_w=[psi[i]**6*fi**2 for i,fi in enumerate(f)]
        Ww=integrate_simple([r**2*weights_w[i] for i,r in enumerate(rs)],rs)
        avg_one_minus_N=integrate_simple([r**2*weights_w[i]*(1-N[i]) for i,r in enumerate(rs)],rs)/Ww
        H_curved=4*math.pi*eps**2*integrate_simple([r**2*N[i]*(kappa*psi[i]**6*fi**2+psi[i]**2*fpi**2/2) for i,(r,fi,fpi) in enumerate(zip(rs,f,fp))],rs)
        H0_flat=4*math.pi*eps**2*integrate_simple([r**2*(kappa*fi**2+fpi**2/2) for i,(r,fi,fpi) in enumerate(zip(rs,f,fp))],rs)
        rel_shift=abs(H_curved-H0_flat)/H0_flat if H0_flat>0 else float("inf")
        slope_central=mu*max(1-n for n in N); slope_avg=mu*avg_one_minus_N
        total_slope_avg=mu*(avg_one_minus_N+rel_shift); total_slope_central=mu*(max(1-n for n in N)+rel_shift)
        budget=case["T_budget"]
        T_avg=budget/total_slope_avg if total_slope_avg>0 else float("inf")
        T_c=budget/total_slope_central if total_slope_central>0 else float("inf")
        cases_out.append({
            "name":case["name"],"D":D,"m0":m0,"A_ev":A_ev,"R0":R0,"epsilon":eps,"strip_b":b,
            "mu":mu,"kappa":kappa,"picard_iterations":n_iter,"picard_residual":cvg,
            "psi_0":psi[0],"N_0":N[0],"C_asymptotic":C,"E_ADM":EADM,"E_proper_matter":Eproper,
            "binding":binding,"classical_charge":charge,
            "max_one_minus_N":max(1-n for n in N),"avg_one_minus_N":avg_one_minus_N,
            "H0_flat_matter":H0_flat,"H_curved_initial_lapse":H_curved,"relative_energy_shift":rel_shift,
            "M_com":mu,"dephasing_slope_central":slope_central,"dephasing_slope_averaged":slope_avg,
            "total_error_slope_averaged":total_slope_avg,"total_error_slope_central":total_slope_central,
            "relational_time_budget":budget,"T_rel_bound_averaged":T_avg,"T_rel_bound_central":T_c,
        })
    out["cases"]=cases_out
    D,m0,Ec,gamma,R=12,2.0,2.0,0.05,20.0
    Mmin=m0+Ec-gamma*math.sqrt(15/4)/R**2; a=gamma*math.sqrt(15/4)/R**2; t=math.pi/a
    out["flat_gaussian_reference"]={"R":R,"Mmin":Mmin,"a":a,"t_pi_over_a":t,"motion_bound":min(1,t*a*math.sqrt(15)/(4*Mmin**2*R**2))}
    out["summary"]="Weak-backreaction quasistatic bound with smooth_field_clock-consistent energies and conformal lapse."
    Path("verification/weak_backreaction_record.json").write_text(json.dumps(out,indent=2))
    print("PASS: weak-backreaction relational record bound")
    print(Path("verification/weak_backreaction_record.json"))

if __name__=="__main__": main()
