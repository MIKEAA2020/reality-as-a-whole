"""Check representational sufficiency on actual source-designated report onsets.

R is a recorded report label, not independently measured experience. Declared
pair metadata is not the actual sensory input or a complete physical state.
This is an exact data/logic check, not a neural model or an identity discovery.
"""
from collections import defaultdict
from pathlib import Path
import json

from reported_rivalry_case_audit import SOURCE, audit, read_sheet


def factorization_diagnostic(basis, target):
    if len(basis) != len(target) or not basis:
        raise ValueError('Nonempty equally sized observations required')
    fibers = defaultdict(set)
    for b, t in zip(basis, target):
        fibers[b].add(t)
    ambiguous = {str(b): sorted(values) for b, values in fibers.items()
                 if len(values) > 1}
    return {
        'observations': len(basis),
        'distinct_basis_values': len(fibers),
        'factors_on_observed_support': not ambiguous,
        'ambiguous_fibers': ambiguous,
    }


def run():
    source_result = audit()
    rows = read_sheet(SOURCE / 'rivalry_pair_01_sess_1.xlsx', 'Default')[1:]
    onsets = [r for r in rows if r['B'] in ('11', '12')]
    reports = ['A' if r['B'] == '11' else 'B' for r in onsets]
    assert reports == source_result['dominance_report_onset_sequence']
    pair = factorization_diagnostic(['declared_pair_1'] * len(onsets), reports)
    code = factorization_diagnostic([r['B'] for r in onsets], reports)
    timestamp = factorization_diagnostic([r['A'] for r in onsets], reports)
    assert pair['ambiguous_fibers'] == {'declared_pair_1': ['A', 'B']}
    assert not pair['factors_on_observed_support']
    assert code['factors_on_observed_support']
    assert timestamp['factors_on_observed_support']
    assert timestamp['distinct_basis_values'] == len(onsets)
    for basis, target in [([], []), (['x'], [])]:
        try:
            factorization_diagnostic(basis, target)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid input accepted')
    return {
        'status': 'passed',
        'source_commit': source_result['commit'],
        'source_hashes_checked': source_result['source_hashes_checked'],
        'target': 'source-designated dominance report A/B, not measured phenomenal character',
        'declared_pair_metadata': pair,
        'report_event_code': code,
        'unique_timestamp': timestamp,
        'report_code_success_is_definition_not_neural_constitution': True,
        'timestamp_success_is_observed_support_fit_not_explanation': True,
        'pair_failure_is_not_proof_of_constant_actual_sensory_input': True,
        'independently_validated_experiential_fibers_available': False,
        'qualitative_identity_established': False,
        'subject_incidence_established': False,
        'scope': 'exact representational test on seven recorded report onsets; no new assigned experiences or synthetic consciousness model',
    }


if __name__ == '__main__':
    result = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print('PASS: seven recorded report onsets distinguish inadequate metadata, circular report encoding, and injective timestamp fit; no phenomenal identity inferred.')
