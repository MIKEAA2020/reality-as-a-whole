"""Static audit of pinned primary sources; never executes third-party analysis.

The Boolean witnesses check first-argmax semantics only, not participant data.
They are not included in the independent research-suite test count.
"""
import ast
from fractions import Fraction
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / 'sources/external/cogitate_analysis'
manifest = json.loads((SNAPSHOT / 'provenance.json').read_text())
for source in manifest['sources']:
    raw = (ROOT / source['local_path']).read_bytes()
    assert len(raw) == source['bytes']
    assert hashlib.sha256(raw).hexdigest() == source['sha256']

base = SNAPSHOT / 'coglib/ieeg/Experiment1ActivationAnalysis'
configs = {}
for role in ('ti', 'tr'):
    path = base / 'duration_tracking_config' / f'duration_tracking_high_gamma_iit_roi_face_{role}.json'
    cfg = json.loads(path.read_text())
    params = next(iter(cfg['analysis_parameters'].values()))
    configs[role] = {
        'conditions': params['conditions'],
        'roi_keys': list(cfg['rois']),
        'roi_entry_count': len(cfg['rois']['iit']),
        'roi_unique_entry_count': len(set(cfg['rois']['iit'])),
        'threshold_condition': params['threshold_condition'],
        'baseline': params['baseline'],
        'activation': params['activation'],
        'moving_average_ms': params['moving_average_ms'],
        'fast_track': params['fast_track'],
        'inaccuracy_threshold_seconds': params['inaccuracy_threshold'],
        'permutations': params['nperm'],
        'fdr_method': params['fdr_method'],
        'configured_data_phase': 'phase_2' if '/phase_2/' in cfg['BIDS_root'] else 'unspecified',
    }
    assert params['moving_average_ms'] == 300
    assert params['fast_track'] is True
    assert params['threshold_condition'] == '1500ms'
    assert params['inaccuracy_threshold'] == .15
    assert params['nperm'] == 1000

helper = ast.parse((base / 'activation_analysis_helper_function.py').read_text())
functions = {node.name: node for node in helper.body if isinstance(node, ast.FunctionDef)}
tracking = functions['compute_tracking_inaccuracy']
argmax = [node.lineno for node in ast.walk(tracking)
          if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
          and isinstance(node.func.value, ast.Name) and node.func.value.id == 'np'
          and node.func.attr == 'argmax']
assert len(argmax) == 2

# For a nonempty Boolean array, first-maximum returns 0 both when all
# entries are false and when the first entry is true. These are distinct
# threshold-crossing observations; this is not a raw-data finding.
def first_maximum(mask):
    return max(range(len(mask)), key=lambda i: int(mask[i]))

witnesses = []
for name, mask in [('never_below', [False]*5),
                   ('initially_below', [True, False, False, False, True]),
                   ('later_below', [False, False, False, True, True])]:
    old = first_maximum(mask)
    crossing = next((i for i, item in enumerate(mask) if item), None)
    witnesses.append({'case': name, 'mask': mask, 'first_argmax_index': old,
                      'first_actual_below_index_or_none': crossing})
assert witnesses[0]['first_argmax_index'] == witnesses[1]['first_argmax_index'] == 0
assert witnesses[0]['first_actual_below_index_or_none'] is None
assert witnesses[1]['first_actual_below_index_or_none'] == 0

# Analytic observation-model witness; not the source's uninspected filter.
duration = Fraction(1)
width = Fraction(3,10)
half_time = duration + width/2
assert 1 - (half_time-duration)/width == Fraction(1,2)
assert half_time - width/2 == duration

out = {
    'status': 'static source/configuration audit, not an executed neural analysis',
    'commit': 'e60764df21ab63d39ffa726a0dd38c2b6f1e3e9a',
    'hashes_verified': len(manifest['sources']),
    'configs': configs,
    'helper_function_range': [tracking.lineno, tracking.end_lineno],
    'argmax_call_lines': sorted(argmax),
    'boolean_semantics_witnesses': witnesses,
    'illustrative_trailing_filter': {
        'not_claimed_to_be_source_implementation': True,
        'duration_seconds': str(duration), 'width_seconds': str(width),
        'half_height_seconds': str(half_time),
        'corrected_endpoint_seconds': str(half_time-width/2),
    },
    'results_reproduced': False,
    'effect_on_published_inference_established': False,
    'research_suite_test_count_changed': False,
}
(ROOT / 'verification/cogitate_analysis_audit.json').write_text(json.dumps(out, indent=2)+'\n')
print('Verified source hashes, selected configuration values, AST call locations, and Boolean witnesses; no neural analysis executed.')
