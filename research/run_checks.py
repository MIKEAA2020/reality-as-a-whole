"""Run independent research folders in separate processes to avoid module-name collisions."""
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
results = []
for folder in ('contrast_covariance', 'contextual_constitution', 'episodic_unity', 'presentation_gluing', 'episode_reconstruction', 'constitution_monitoring', 'interventional_core', 'differentiation_unity', 'weak_coupling', 'boundary_identifiability', 'framework_overlap', 'dynamical_locality', 'quasilocal_limit', 'continuum_scaling', 'fermionic_lift', 'quasifree_vacuum', 'spacetime_net', 'local_scaling', 'causal_geometry', 'order_reconstruction', 'refinement_completion', 'curved_dirac', 'hamiltonian_state_limit', 'wilson_regulator', 'conformal_stress', 'relative_subtraction', 'cell_current_limit', 'wilson_thermal_composite', 'wilson_nonthermal_universality', 'wilson_wavepacket_composite', 'wilson_multimode_composite', 'wilson_infinite_rank', 'wilson_ultraviolet_tails', 'wilson_particle_hole', 'wilson_coherent_rotation', 'wilson_nonquasifree_mixture', 'event_composition_obstruction', 'temporal_episode_selection', 'constitutive_relabeling', 'causal_exclusion_candidate', 'realized_workspace', 'rigorous_closures', 'constitutive_geometry'):
    run = subprocess.run([sys.executable, '-m', 'unittest', '-v', 'test_model.py'],
                         cwd=root / folder, capture_output=True, text=True)
    log = run.stdout + run.stderr
    (root / folder / 'results.log').write_text(log)
    results.append({'folder': folder, 'exit_code': run.returncode,
                    'command': [sys.executable, '-m', 'unittest', '-v', 'test_model.py'],
                    'log_tail': log.splitlines()[-5:]})
    print(folder, 'exit', run.returncode)
(root / 'check_results.json').write_text(json.dumps(results, indent=2) + '\n')
raise SystemExit(0 if all(r['exit_code'] == 0 for r in results) else 1)
