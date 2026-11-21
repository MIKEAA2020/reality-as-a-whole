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
    ('subject_weight_no_signalling', 'verification/no_signalling_subject_measure_gate.py'),
    ('history_weight_consistency', 'verification/history_weight_martingale_gate.py'),
    ('quantum_friend', 'verification/subject_friend_quantum_extensions.py'),
    ('friend_history', 'verification/friend_history_selector_gate.py'),
    ('weak_record_coarse_graining', 'verification/weak_record_coarse_graining_gate.py'),
    ('quantum_access_subject_count', 'verification/quantum_access_subject_count_gate.py'),
    ('swapping_herald_selection', 'verification/swapping_herald_selection_gate.py'),
    ('complementary_correlations', 'verification/complementary_visibility_entanglement_gate.py'),
    ('bell_preparation_correlator', 'verification/bell_preparation_correlation_gate.py'),
    ('ur_spinor_classical_control', 'verification/ur_spinor_classical_control_gate.py'),
    ('noble_symmetry_selection', 'verification/noble_symmetry_selection_gate.py'),
    ('context_gated_variability', 'verification/context_gated_variability_gate.py'),
    ('timeless_whole_location', 'verification/timeless_whole_location_gate.py'),
    ('friend_record_tradeoff', 'verification/reversible_friend_record_tradeoff.py'),
    ('collapse_identifiability', 'verification/experience_collapse_identifiability.py'),
    ('shared_and_independent_reports', 'verification/shared_vs_independent_reports.py'),
    ('latent_experience', 'verification/latent_experience_three_probes.py'),
    ('experiential_anatomical_witness', 'verification/experiential_anatomical_witness_gate.py'),
    ('phenomenal_unity_partition', 'verification/phenomenal_unity_partition_gate.py'),
    ('phenomenal_facet_subject', 'verification/phenomenal_facet_subject_gate.py'),
    ('unity_triple_partition_calibration', 'verification/unity_triple_partition_calibration_gate.py'),
    ('shared_token_disagreement', 'verification/shared_token_disagreement_gate.py'),
    ('correlation_clustering_certificate', 'verification/correlation_clustering_asymmetric_certificate.py'),
    ('plural_ground_dominance_symmetry', 'verification/plural_ground_dominance_symmetry_gate.py'),
    ('experiential_mismatch_transport', 'verification/experiential_mismatch_transport_gate.py'),
    ('integrated_cross_scale_quality', 'verification/integrated_cross_scale_quality.py'),
    ('integrated_subject_context_dynamics', 'verification/integrated_subject_context_dynamics.py'),
    ('kemeny_snell_reversible_projection', 'verification/kemeny_snell_reversible_projection.py'),
    ('direct_stimulation_affect_arithmetic', 'verification/direct_stimulation_affect_audit.py'),
    ('awareness_ignition_calibration', 'verification/awareness_ignition_partial_identification.py'),
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
