#!/usr/bin/env python3
"""Published summary arithmetic and model-scope controls, not detector reanalysis."""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from scipy.stats import gamma

ROOT = Path(__file__).resolve().parent.parent


def lindblad(a, rho):
    return -0.5 * (a @ (a @ rho - rho @ a) - (a @ rho - rho @ a) @ a)


def main():
    n, baseline, a = 576, 508., 1.756e-29
    rmin = 1e-14
    max_mean = baseline + a / rmin**3
    cdf_max = gamma.cdf(max_mean, n + 1)
    q = gamma.ppf(.95 * cdf_max, n + 1)
    cdf_min = gamma.cdf(baseline, n + 1)
    q_physical = gamma.ppf(cdf_min + .95 * (cdf_max - cdf_min), n + 1)
    radius = (a / (q - baseline)) ** (1 / 3)
    radius_physical = (a / (q_physical - baseline)) ** (1 / 3)
    assert abs(q - 617.0710335865) < 1e-8
    assert abs(radius / 1e-11 - 5.44007675954) < 1e-8
    assert q_physical > q and radius_physical < radius
    # Exact finite-dimensional adjoint master-equation derivative controls.
    # A is dimensionless, kappa=1. Unit convention hbar=1.
    sx = np.array([[0, 1], [1, 0]], complex)
    sz = np.diag([1., -1.]).astype(complex)
    h = sx
    number = (np.eye(2) - sz) / 2
    rho = np.diag([1., 0.]).astype(complex)
    energy_rate = np.trace(h @ lindblad(h, rho)).real
    n_rate = np.trace(number @ lindblad(h, rho)).real
    t = 1.
    # For A=H=sigma_x, E_t(rho)=(1+e^-2t)/2 rho + (1-e^-2t)/2 H rho H.
    decohered = (1 + np.exp(-2*t))/2 * rho + (1 - np.exp(-2*t))/2 * h @ rho @ h
    assert abs(energy_rate) < 1e-14 and abs(n_rate - 1) < 1e-14
    assert np.allclose(np.trace(decohered), 1)
    assert abs(np.trace(h @ decohered) - np.trace(h @ rho)) < 1e-14
    assert abs(np.trace(number @ decohered).real - (1 - np.exp(-2))/2) < 1e-14
    # Include the Hamiltonian term, with hbar=1, and a fixed bare observable.
    u = expm(-1j * h * t)
    full_state = u @ decohered @ u.conj().T
    full_excitation = np.trace(number @ full_state).real
    assert abs(full_excitation - (1 - np.exp(-2*t)*np.cos(2*t))/2) < 1e-14
    # The true ground state of H is invariant under energy dephasing.
    ground = (np.eye(2) - h)/2
    assert np.linalg.norm(lindblad(h, ground)) < 1e-14
    # In a finite position representation, monitor how kinetic energy changes.
    # The finite matrix mirrors the commutator structure; the continuum identity
    # is stated separately because no finite matrix exactly satisfies [x,p]=i.
    loc_h = sx
    x = sz
    state = (np.eye(2) + sx)/2
    loc_energy_rate = np.trace(loc_h @ lindblad(x, state)).real
    assert abs(loc_energy_rate + 2) < 1e-14
    out = {
        'scope': 'Summary-value arithmetic and idealized finite-dimensional checks; no detector data, background or radiation calculation.',
        'paper_inputs': {'n_observed': n, 'nominal_background_counts': 506,
                         'authors_fixed_baseline_including_plus_two': baseline,
                         'a_m3': a, 'r_min_m': rmin},
        'authors_flat_mean_prior_arithmetic': {'gamma_shape': n + 1,
            'upper_mean_cutoff': max_mean, 'gamma_cdf_at_upper_cutoff': cdf_max,
            'mean_95_percent_quantile': q, 'signal_scale_at_quantile_counts': q - baseline,
            'radius_lower_m': radius, 'gamma_mass_below_physical_baseline': cdf_min,
            'signal_scale_at_5e-12_m_counts': a/(5e-12)**3},
        'truncated_below_baseline_sensitivity_not_paper_reanalysis': {
            'mean_95_percent_quantile': q_physical, 'radius_lower_m': radius_physical},
        'two_level_global_energy_dephasing': {
            'H': 'sigma_x', 'A': 'H', 'initial_state': '|0_z>',
            'measured_observable': '(I-sigma_z)/2', 'kappa': 1, 'time': t,
            'energy_initial_derivative': energy_rate,
            'bare_excitation_initial_derivative': n_rate,
            'bare_excitation_at_time_dissipator_only': np.trace(number @ decohered).real,
            'bare_excitation_at_time_full_unitary_plus_dissipator': full_excitation,
            'energy_ground_state_dephasing_norm': float(np.linalg.norm(lindblad(h, ground)))},
        'position_like_toy': {'H': 'sigma_x', 'A': 'sigma_z', 'initial_state': '+x',
                              'energy_initial_derivative': loc_energy_rate}
    }
    (ROOT / 'verification/underground_collapse_scope.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
