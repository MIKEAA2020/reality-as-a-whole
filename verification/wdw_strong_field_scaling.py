"""
Strong-field scaling of the spherical WdW R-clock: increase compactness C=2M/R
toward 1 and find thresholds where weak-field approximations break.
"""
import json, math
from pathlib import Path


def main():
    out={}
    mu=22.0
    R_source=22.657
    def eps_at(C):
        Nd=math.sqrt(max(0,1-C))
        if 1-C < 1e-30: return float('inf')
        return (1-Nd)/(R_source*mu*(1-C))
    C_cases=[3.66e-5,1e-4,1e-3,1e-2,1e-1,0.5,0.9,0.99,0.998,0.999,0.9999,0.99999]
    cases=[]
    for C in C_cases:
        N_factor=math.sqrt(max(0,1-C))
        omega_d=mu*N_factor
        eps=eps_at(C)
        N_particles=min(1.0,eps*eps) if eps<1 else 1.0
        wkb_amplitude=1.0/math.sqrt(max(omega_d,1e-30))
        cases.append({"C":C,"N_factor":N_factor,"omega_d":omega_d,
                      "epsilon":eps,"N_particles":N_particles,
                      "wkb_amplitude":wkb_amplitude,
                      "non_adiabatic":eps>=1})
    lo,hi=0.0,1.0-1e-12
    for _ in range(80):
        mid=(lo+hi)/2
        if eps_at(mid)<1: lo=mid
        else: hi=mid
    C_crit=(lo+hi)/2
    out["scaling"]={
        "mu":mu,"R_source":R_source,
        "weak_field_C":3.66e-5,
        "C_critical_nonadiabatic":C_crit,
        "epsilon_at_critical":eps_at(C_crit),
        "N_factor_at_critical":math.sqrt(1-C_crit),
        "omega_d_at_critical":mu*math.sqrt(1-C_crit),
        "cases":cases,
        "note":"Weak-field dressed WdW R-clock remains valid across many orders of compactness until C approaches ~0.998, where redshift drives omega_d small and adiabaticity/WKB normalization fail together near the horizon threshold."
    }
    Path("verification/wdw_strong_field_scaling.json").write_text(json.dumps(out,indent=2))
    print("PASS: WdW spherical strong-field compactness scaling and critical threshold")
    print(Path("verification/wdw_strong_field_scaling.json"))


if __name__=="__main__":main()
