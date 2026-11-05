"""Bounded source-data audit and analytic-clock witnesses, not an experimental replication."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
import hashlib
import json


def run():
    source = Path(__file__).parent/'sources'/'barontini_2026_clock_subset.json'
    data = json.loads(source.read_text())
    traces = {}
    for name, trace in data['traces'].items():
        raw = [(int(t), Q(tau)) for t, tau in trace['t_tau']]
        assert len({t for t, tau in raw}) == len(raw)
        assert all(a[1] <= b[1] for a, b in zip(raw, raw[1:]))
        ordered = sorted(raw)
        drops, ties = [], []
        for (t0, tau0), (t1, tau1) in zip(ordered, ordered[1:]):
            if tau1 < tau0:
                drops.append({'from_t': t0, 'to_t': t1, 'drop': str(tau0-tau1),
                              'relative_percent': float(100*(tau0-tau1)/tau0)})
            if tau1 == tau0:
                ties.append([t0, t1])
        indexed = dict(ordered)
        selected = trace['selected_tied_readouts']
        witnesses = []
        for x, y in combinations(selected, 2):
            if indexed[x['t']] == indexed[y['t']]:
                dphi, dwidth = abs(Q(x['phi'])-Q(y['phi'])), abs(Q(x['sigma'])-Q(y['sigma']))
                if dphi or dwidth:
                    witnesses.append({'times': [x['t'], y['t']],
                                      'delta_phi_m': str(dphi), 'delta_width_m': str(dwidth)})
        assert drops and ties and witnesses
        traces[name] = {
            'rows': len(raw), 'file_order': 'nondecreasing tau, not chronological t',
            'chronological_adjacent_decreases': len(drops), 'decreases': drops,
            'chronological_equal_tau_neighbors': ties,
            'selected_equal_tau_distinct_central_readouts': witnesses,
            'uncertainty_significance': 'not established; no per-row covariance/error model in this subset',
        }
    assert traces['V0']['rows'] == 56 and traces['V1']['rows'] == 53
    assert traces['V0']['chronological_adjacent_decreases'] == 3
    assert traces['V1']['chronological_adjacent_decreases'] == 7
    # Eq. (3) on a recurrent synthetic trajectory, sigma/k_B set to one.
    phi = [Q(0), Q(1), Q(0), Q(-1), Q(0)]
    S = [Q(3)+2*x for x in phi]
    increments = []
    for a, b, sa, sb in zip(phi, phi[1:], S, S[1:]):
        increments.append((sb-sa)*(1 if b>a else -1))
    assert phi[0] == phi[-1] and S[0] == S[-1]
    assert increments == [Q(2)]*4 and sum(increments) == 8
    # Norm derivative of a real-coefficient Hermitian effective Hamiltonian is zero.
    H0 = [[Q(1), Q(2)], [Q(2), Q(0)]]
    for tau in (Q(0), Q(1), Q(3, 2)):
        H = [[(1+tau)*v+(tau*tau if i==j else 0) for j, v in enumerate(row)]
             for i, row in enumerate(H0)]
        assert H == [list(r) for r in zip(*H)]
    # Frozen-coefficient necessary sign check of the printed Eq. (4)->(5).
    mass, potential, square_root_momentum = Q(1), Q(1, 2), Q(1)
    assert square_root_momentum**2 == 2*mass*potential
    residual = square_root_momentum**2/(2*mass)+potential
    assert residual == 1  # not zero as the printed second-order equation would require
    return {
        'status': 'passed', 'source_subset_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'scope': 'two processed traces; manual column transcription, not raw-image or full-data replication',
        'trace_audits': traces,
        'synthetic_closed_trajectory': {'instantaneous_state_returns': True,
                                        'entropic_path_increment_sigma_units': '8',
                                        'interpretation': 'path memory needed; not an experiment on the paper data'},
        'real_time_dependent_H_is_Hermitian': True,
        'frozen_printed_equation_sign_probe_residual': str(residual),
        'analytic_not_established_from_samples': ['clock descent iff retained state is constant on clock fibers',
                                                'path derivative tau_dot=(sigma/k_B) S_dot sign(phi_dot)',
                                                'unitarity of Eq6 under real coefficients and self-adjoint Hgeom'],
        'not_claimed': ['statistically significant clock reversal', 'failure of measured cold-atom evolution',
                        'independent recomputation of entropy or tau', 'verification of original file MD5 bytes',
                        'general solution of gravitational time'],
    }


if __name__ == '__main__':
    result = run()
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: two source clock traces, recurrent path clock and printed-equation consistency probes')
    print(path)
