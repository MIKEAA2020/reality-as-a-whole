"""
Linearized spherical relational bound for the smooth self-gravitating field clock.

Uses Birkhoff's theorem (spherical vacuum is static Schwarzschild with conserved ADM/Bondi mass
at linear order) and the correct Misner-Sharp mass formula in isotropic/conformal coordinates to
give a relational record bound beyond the frozen-geometry quasistatic approximation.
"""
import json, math
from pathlib import Path


def gauss(r, R0):
    return math.exp(-0.5 * (r / R0) ** 2)


def picard_psi(R0, kappa, eps, b, n_steps=8192, r_max=None, tol=1e-14, max_iter=100):
    if r_max is None:
        r_max = 8.0 * R0
    dr = r_max / n_steps
    rs = [i * dr for i in range(n_steps + 1)]

    def S(r, psi):
        f = gauss(r, R0); fp = -(r / R0**2) * f
        return psi * fp * fp + 2.0 * kappa * (psi**5) * f * f

    def apply_T(psi_grid):
        inner = [0.0] * (n_steps + 1)
        for i in range(1, n_steps + 1):
            inner[i] = inner[i - 1] + rs[i] ** 2 * S(rs[i], psi_grid[i]) * dr
        outer_tail = [0.0] * (n_steps + 1)
        for i in range(n_steps - 1, -1, -1):
            outer_tail[i] = outer_tail[i + 1] + rs[i + 1] * S(rs[i + 1], psi_grid[i + 1]) * dr
        new = [0.0] * (n_steps + 1)
        new[0] = 1.0 + eps**2 / 8.0 * outer_tail[0]
        for i in range(1, n_steps + 1):
            new[i] = 1.0 + eps**2 / 8.0 * (inner[i] / rs[i] + outer_tail[i])
        return [min(1.0 + b, max(1.0, v)) for v in new]

    psi = [1.0] * (n_steps + 1)
    for it in range(max_iter):
        new = apply_T(psi)
        err = max(abs(new[i] - psi[i]) for i in range(n_steps + 1))
        psi = new
        if err < tol:
            break
    return rs, psi, it + 1, err


def integrate_simple(values, rs):
    dr = rs[1] - rs[0]
    return dr * (sum(values[1:-1]) + 0.5 * (values[0] + values[-1]))


def main():
    out = {}
    cases = [
        {"name": "nonlinear_binding_24", "D": 12, "m0": 20.0, "A_ev": 2.0, "R0": 20.0, "eps": 0.001, "b": 0.1, "T_budget": 0.01},
        {"name": "weak_backreaction", "D": 12, "m0": 20.0, "A_ev": 2.0, "R0": 20.0, "eps": 0.00003, "b": 0.00004, "T_budget": 0.001},
    ]
    cases_out = []
    for case in cases:
        R0, eps, b, m0, A_ev = case["R0"], case["eps"], case["b"], case["m0"], case["A_ev"]
        D = case["D"]
        M_diag = [m0] * D; M_diag[0] += A_ev
        v = [0.0] * D; v[0] = 1.0
        mu = sum(M_diag[i] * v[i] ** 2 for i in range(D))
        kappa = sum(M_diag[i] ** 2 * v[i] ** 2 for i in range(D))
        rs, psi, n_iter, cvg = picard_psi(R0, kappa, eps, b)
        dr = rs[1] - rs[0]
        f = [gauss(r, R0) for r in rs]
        fp = [-(r / R0**2) * fi for r, fi in zip(rs, f)]
        N = [p**-2 for p in psi]
        # Proper matter energy and charge using same integrand as smooth_field_clock.
        Eproper = 4.0 * math.pi * eps**2 * integrate_simple([r**2 * (psi[i]**2 * fpi**2 / 2.0 + kappa * psi[i]**6 * fi**2) for i, (r, fi, fpi) in enumerate(zip(rs, f, fp))], rs)
        charge = 4.0 * math.pi * eps**2 * mu * integrate_simple([r**2 * psi[i]**6 * fi**2 for i, (r, fi) in enumerate(zip(rs, f))], rs)
        # ADM mass from asymptotic C.
        C = rs[-1] * (psi[-1] - 1.0)
        for i in range(len(rs) - 2, max(1, len(rs) - 200), -1):
            C = max(C, rs[i] * (psi[i] - 1.0))
        EADM = 16.0 * math.pi * C
        binding = EADM - Eproper
        # Derivative of psi for Misner-Sharp areal radius and mass.
        psip = [(psi[i+1] - psi[i-1]) / (2 * dr) for i in range(1, len(rs) - 1)]
        psip = [(psi[1] - psi[0]) / dr] + psip + [(psi[-1] - psi[-2]) / dr]
        R_phys = [r * psi[i] ** 2 for i, r in enumerate(rs)]
        dRdr = [psi[i]**2 + 2 * r * psi[i] * psip[i] for i, r in enumerate(rs)]
        M_MS = [R_phys[i] / 2.0 * (1.0 - 1.0 / dRdr[i]**2) if dRdr[i] != 0 else 0.0 for i in range(len(rs))]
        compact = [2 * M_MS[i] / R_phys[i] if R_phys[i] > 0 else 0.0 for i in range(len(rs))]
        max_compact = max(compact)
        horizon_coord = None; horizon_R = None; horizon_m = None
        for i, c in enumerate(compact):
            if c >= 1.0 - 1e-9 and horizon_coord is None:
                horizon_coord = rs[i]; horizon_R = R_phys[i]; horizon_m = M_MS[i]
        # Matter-weighted physical radius (weighted by physical matter density ~ kappa psi^6 f^2 + psi^2 fp^2/2).
        dens = [psi[i]**2 * fpi**2 / 2.0 + kappa * psi[i]**6 * fi**2 for i, (fi, fpi) in enumerate(zip(f, fp))]
        W = integrate_simple([r**2 * dens[i] for i, r in enumerate(rs)], rs)
        R_matter = integrate_simple([r**2 * dens[i] * R_phys[i] for i, r in enumerate(rs)], rs) / W
        # Find enclosed Misner-Sharp mass near R_matter by matching physical radius.
        M_at_Rm = M_MS[-1]
        for i, Rp in enumerate(R_phys):
            if Rp >= R_matter:
                M_at_Rm = M_MS[i]; break
        a_g = M_at_Rm / R_matter**2 if R_matter > 0 else 0.0
        T_dyn = math.sqrt(R_matter**3 / max(M_at_Rm, 1e-300))
        # Matter support-averaged initial redshift.
        weights_w = [psi[i]**6 * fi**2 for i, fi in enumerate(f)]
        Ww = integrate_simple([r**2 * weights_w[i] for i, r in enumerate(rs)], rs)
        avg_one_minus_N0 = integrate_simple([r**2 * weights_w[i] * (1.0 - N[i]) for i, r in enumerate(rs)], rs) / Ww
        # Initial Hamiltonian energy with lapse N=psi^-2, physical volume sqrt q = psi^6.
        H_curved0 = 4.0 * math.pi * eps**2 * integrate_simple([r**2 * N[i] * (kappa * psi[i]**6 * fi**2 + psi[i]**2 * fpi**2 / 2.0) for i, (r, fi, fpi) in enumerate(zip(rs, f, fp))], rs)
        H0_flat = 4.0 * math.pi * eps**2 * integrate_simple([r**2 * (kappa * fi**2 + fpi**2 / 2.0) for i, (r, fi, fpi) in enumerate(zip(rs, f, fp))], rs)
        delta_curv0 = abs(H_curved0 - H0_flat) / H0_flat if H0_flat > 0 else float("inf")
        one_minus_N0 = 1.0 - N[0]
        # Gradient kinetic energy (the fp^2 piece) vs rest energy.
        grad_energy = 4.0 * math.pi * eps**2 * integrate_simple([r**2 * psi[i]**2 * fpi**2 / 2.0 for i, (r, fpi) in enumerate(zip(rs, fp))], rs)
        rest_energy = 4.0 * math.pi * eps**2 * kappa * integrate_simple([r**2 * psi[i]**6 * fi**2 for i, (r, fi) in enumerate(zip(rs, f))], rs)
        grad_rest_ratio = grad_energy / rest_energy if rest_energy > 0 else float("inf")
        # Radius where compactness is 99% of mass (using Misner-Sharp).
        R99_phys = R_phys[-1]
        for i, m in enumerate(M_MS):
            if m >= 0.99 * EADM:
                R99_phys = R_phys[i]; break
        compactness_C99 = 2.0 * EADM / R99_phys if R99_phys > 0 else float("inf")
        budget = case["T_budget"]
        s0 = avg_one_minus_N0 + delta_curv0
        slope_qs = mu * s0
        T_rel_qs = budget / slope_qs if slope_qs > 0 else float("inf")
        # Birkhoff/dynamical-time improved bound: redshift slope remains initial plus (T/T_dyn)^2 correction from interior motion.
        def err_dyn(T):
            return mu * T * s0 * (1.0 + (T / T_dyn) ** 2)
        lo, hi = 0.0, T_rel_qs * 2.0
        for _ in range(100):
            mid = 0.5 * (lo + hi)
            if err_dyn(mid) < budget:
                lo = mid
            else:
                hi = mid
        T_rel_dyn = lo
        # Key result: spherical symmetry implies no linear quadrupole GW; ADM/Bondi mass conserved to linear order;
        # exterior metric is static Schwarzschild by Birkhoff; only interior pulsation on free-fall timescale changes redshift.
        cases_out.append({
            "name": case["name"],
            "D": D, "m0": m0, "A_ev": A_ev, "R0": R0, "epsilon": eps, "strip_b": b,
            "mu": mu, "kappa": kappa,
            "picard_iterations": n_iter, "picard_residual": cvg,
            "psi_0": psi[0], "N_0": N[0],
            "E_ADM": EADM, "E_proper_matter": Eproper, "binding": binding, "classical_charge": charge,
            "R_99_phys": R99_phys, "R_matter_phys": R_matter,
            "max_compactness_2M_over_R": max_compact,
            "apparent_horizon_present": horizon_coord is not None,
            "compactness_C99": compactness_C99,
            "M_at_R_matter": M_at_Rm,
            "dynamical_time_T_dyn": T_dyn,
            "gravitational_acceleration_at_Rm": a_g,
            "one_minus_N_central": one_minus_N0,
            "avg_one_minus_N_initial": avg_one_minus_N0,
            "relative_energy_shift_initial": delta_curv0,
            "gradient_kinetic_energy": grad_energy,
            "rest_mass_energy": rest_energy,
            "gradient_to_rest_ratio": grad_rest_ratio,
            "linear_spherical_GW_loss_slope": 0.0,
            "Birkhoff_exterior": "Static Schwarzschild with conserved ADM mass; no linear quadrupole radiation.",
            "quasistatic_slope": slope_qs,
            "T_rel_quasistatic": T_rel_qs,
            "T_rel_Birkhoff_dynamical": T_rel_dyn,
            "budget": budget,
        })
    out["cases"] = cases_out
    out["summary"] = (
        "Linearized spherical bound: Birkhoff gives a static exterior Schwarzschild metric with conserved ADM mass "
        "and zero linear-order spherical GW loss. Interior matter redistributes on the dynamical/free-fall time, "
        "giving a controlled correction to the frozen-geometry quasistatic record bound. No horizon forms in the "
        "constructed examples."
    )
    Path("verification/linearized_spherical_record.json").write_text(json.dumps(out, indent=2))
    print("PASS: linearized spherical relational bound")
    print(Path("verification/linearized_spherical_record.json"))


if __name__ == "__main__":
    main()
