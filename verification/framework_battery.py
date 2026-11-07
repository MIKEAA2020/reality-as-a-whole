#!/usr/bin/env python3
"""Run selected bounded regression checks, NOT a verdict on the framework.

Each underlying script checks its own stipulated mathematical toy. Passing
cannot prove necessity, experience, real subjects, physical laws, a continuum
limit, or zero-residue explanation. Read the consolidated dossier first.
"""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
TESTS = [
    ('modality', 'verification/necessity_nonempty_modal_audit.py'),
    ('self_location', 'verification/self_existing_plenitude_centers.py'),
    ('modal_and_symmetry', 'verification/plenitude_foundation_symmetry_gates.py'),
    ('subject_dynamics', 'verification/coupled_subject_boundary_gate.py'),
    ('causal_subject_candidate', 'verification/causal_influence_subject_gate.py'),
    ('subject_identity_and_representation', 'verification/subject_cohesion_identity_redescription.py'),
    ('quantum_friend', 'verification/subject_friend_quantum_extensions.py'),
    ('friend_history', 'verification/friend_history_selector_gate.py'),
    ('friend_record_tradeoff', 'verification/reversible_friend_record_tradeoff.py'),
    ('collapse_identifiability', 'verification/experience_collapse_identifiability.py'),
    ('shared_and_independent_reports', 'verification/shared_vs_independent_reports.py'),
    ('latent_experience', 'verification/latent_experience_three_probes.py'),
    ('random_report_audit', 'verification/random_audit_experience_bridge.py'),
    ('valence_proxy', 'verification/phase_frustration_audit.py'),
    ('relational_modular_clock', 'verification/relational_modular_clock.py'),
    ('clock_choice', 'verification/clock_choice.py'),
    ('cutoff_causality', 'verification/cross_framework_causal_cutoff.py'),
    ('instrument_energy_bound', 'verification/cutoff_instrument_uniformity.py'),
    ('oph_capacity_arithmetic', 'verification/oph_capacity_restriction_current_check.py'),
    ('oph_calibration_interface', 'verification/oph_cutoff_calibration_bridge.py'),
    ('oph_koide_controls', 'verification/oph_unification_koide_gate.py'),
]


def main():
    rows = []
    for label, script in TESTS:
        try:
            p = subprocess.run([sys.executable, script], cwd=ROOT, capture_output=True,
                               text=True, timeout=90, check=False)
            result = 'passed' if p.returncode == 0 else 'failed'
            row = {'name': label, 'script': script, 'result': result, 'exit_code': p.returncode}
            if p.returncode != 0:
                row['stderr_tail'] = p.stderr[-3000:]
                row['stdout_tail'] = p.stdout[-2000:]
        except subprocess.TimeoutExpired:
            row = {'name': label, 'script': script, 'result': 'timeout', 'exit_code': None}
        rows.append(row)
        print(f"{row['result'].upper():7} {label} ({script})", flush=True)
    success = all(r['result'] == 'passed' for r in rows)
    report = {
        'status': 'all_selected_scripts_exited_zero' if success else 'one_or_more_scripts_failed_or_timed_out',
        'count': len(rows),
        'scope': 'Regression checks for selected finite models only. No pass/fail judgment on the full philosophical framework, factual truth of assumptions, human consciousness, empirical claims, or quantum gravity. Script exit codes are not independent verification of their claims. Historical closure-claim aggregators intentionally excluded.',
        'results': rows,
    }
    (ROOT / 'verification/framework_battery.json').write_text(json.dumps(report, indent=2) + '\n')
    print('\n' + report['scope'])
    return 0 if success else 1


if __name__ == '__main__':
    raise SystemExit(main())
