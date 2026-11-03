"""Standard-library audit of one source-selected reported-content event log.

No Excel formulas/macros, MATLAB code, stimuli, or pickle files are executed.
Exact decimal arithmetic describes the recorded timestamps, not clock accuracy.
"""
from decimal import Decimal
import hashlib
import json
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'sources/external/reported_rivalry_case'
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
REL = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'


def read_sheet(path, name):
    """Read literal cells of these pinned small XLSX files; reject formulas."""
    with ZipFile(path) as z:
        if sum(i.file_size for i in z.infolist()) > 2_000_000:
            raise ValueError('Workbook exceeds this bounded reader')
        strings = []
        if 'xl/sharedStrings.xml' in z.namelist():
            strings = [''.join(si.itertext()) for si in
                       ET.fromstring(z.read('xl/sharedStrings.xml'))]
        book = ET.fromstring(z.read('xl/workbook.xml'))
        selected = [s for s in book.findall('s:sheets/s:sheet', NS)
                    if s.attrib['name'] == name]
        if len(selected) != 1:
            raise ValueError('Named sheet missing or ambiguous')
        rid = selected[0].attrib[f'{{{REL}}}id']
        rels = ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
        matches = [r for r in rels if r.attrib['Id'] == rid]
        if len(matches) != 1 or matches[0].attrib.get('TargetMode') == 'External':
            raise ValueError('Invalid sheet relationship')
        target = matches[0].attrib['Target']
        if '..' in PurePosixPath(target).parts:
            raise ValueError('Unsafe relationship')
        target = target.lstrip('/') if target.startswith('/') else 'xl/' + target
        rows = []
        for row in ET.fromstring(z.read(target)).findall('s:sheetData/s:row', NS):
            values = {}
            for cell in row:
                if cell.find('s:f', NS) is not None:
                    raise ValueError('Formula cell not accepted')
                v = cell.find('s:v', NS)
                if v is None:
                    continue
                text = v.text
                if cell.attrib.get('t') == 's':
                    text = strings[int(text)]
                elif cell.attrib.get('t') not in (None, 'n'):
                    raise ValueError('Unsupported cell type')
                column = ''.join(c for c in cell.attrib['r'] if c.isalpha())
                values[column] = text
            rows.append(values)
        return rows


def summarize(events):
    if len(events) < 2 or events[0][1] != 1 or events[-1][1] != 2:
        raise ValueError('Trial boundaries required')
    if any(not t.is_finite() for t, _ in events):
        raise ValueError('Nonfinite time')
    if any(b[0] <= a[0] for a, b in zip(events, events[1:])):
        raise ValueError('Strictly increasing times required')
    active = None
    durations = {'A_report': Decimal(0), 'B_report': Decimal(0),
                 'other_unresolved': Decimal(0)}
    onsets = []
    counts = {}
    for i, (time, code) in enumerate(events):
        counts[str(code)] = counts.get(str(code), 0) + 1
        if code == 1:
            if i != 0:
                raise ValueError('Repeated start')
        elif code in (11, 12):
            if active is not None:
                raise ValueError('Overlapping dominance reports')
            active = code
            onsets.append('A' if code == 11 else 'B')
        elif code in (21, 22):
            if active != code - 10:
                raise ValueError('Mismatched report termination')
            active = None
        elif code == 2:
            if i != len(events) - 1:
                raise ValueError('Early end')
        else:
            raise ValueError('Unrecognized code in selected trial')
        if i < len(events) - 1:
            key = {11: 'A_report', 12: 'B_report'}.get(code, 'other_unresolved')
            durations[key] += events[i+1][0] - time
    span = events[-1][0] - events[0][0]
    assert sum(durations.values()) == span
    return {
        'event_count': len(events),
        'event_counts_by_code': counts,
        'first_timestamp': str(events[0][0]),
        'last_timestamp': str(events[-1][0]),
        'recorded_span': str(span),
        'durations_in_recorded_time_units': {k: str(v) for k, v in durations.items()},
        'dominance_report_onset_sequence': onsets,
        'changes_between_successive_dominance_reports': sum(a != b for a, b in zip(onsets, onsets[1:])),
        'active_report_at_trial_end': {11: 'A', 12: 'B', None: None}[active],
        'unresolved_is_not_assumed_entirely_mixed_experience': True,
    }


def self_test():
    D = Decimal
    result = summarize([(D(0), 1), (D(1), 11), (D(2), 21), (D(3), 12), (D(4), 2)])
    assert result['durations_in_recorded_time_units'] == {
        'A_report': '1', 'B_report': '1', 'other_unresolved': '2'}
    assert result['active_report_at_trial_end'] == 'B'
    invalid = [
        [(D(0), 1), (D(1), 11), (D(2), 12), (D(3), 2)],
        [(D(0), 1), (D(1), 11), (D(2), 22), (D(3), 2)],
        [(D(0), 1), (D(0), 11), (D(2), 2)],
        [(D(0), 1), (D(1), 9), (D(2), 2)],
        [(D(0), 1), (D(1), 11)],
        [(D(0), 1), (D('NaN'), 2)],
    ]
    for bad in invalid:
        try:
            summarize(bad)
        except ValueError:
            pass
        else:
            raise AssertionError('Malformed sequence accepted')


def audit():
    self_test()
    provenance = json.loads((SOURCE / 'provenance.json').read_text())
    for entry in provenance['files']:
        data = (SOURCE / entry['local_path']).read_bytes()
        assert len(data) == entry['bytes']
        assert hashlib.sha256(data).hexdigest() == entry['sha256']
    trial = read_sheet(SOURCE / 'rivalry_pair_01_sess_1.xlsx', 'Default')
    assert trial[0] == {'A': 'Time', 'B': 'TTL'}
    events = []
    for row in trial[1:]:
        code = Decimal(row['B'])
        assert code == code.to_integral_value()
        events.append((Decimal(row['A']), int(code)))
    params = SOURCE / 'BR_params_default.xlsx'
    pairs = read_sheet(params, 'Pairs')
    assert pairs[0]['A'] == 'StimA' and pairs[0]['B'] == 'StimB'
    ttl = read_sheet(params, 'TTLs')
    labels = {row['B']: row['C'] for row in ttl[1:]}
    assert labels['11'] == '<StimA> percept'
    assert labels['12'] == '<StimB> percept'
    assert 'piecemeal' in labels['21'] and 'piecemeal' in labels['22']
    assert labels['31'] == '<StimA> on' and labels['32'] == '<StimB> on'
    result = summarize(events)
    result.update({
        'status': 'passed',
        'commit': provenance['commit'],
        'source_hashes_checked': len(provenance['files']),
        'pair_1_stimulus_names': {'A': pairs[1]['A'], 'B': pairs[1]['B']},
        'selected_TTL_descriptions': {str(k): labels[str(k)] for k in (1, 2, 11, 12, 21, 22, 31, 32)},
        'source_parameters_Sessions': read_sheet(params, 'Sessions'),
        'clock_unit_independently_calibrated': False,
        'runtime_stimulus_frames_available': False,
        'motor_to_experience_error_calibrated': False,
        'paired_OKN_trace_available_in_selected_files': False,
        'neural_recordings_available_in_selected_files': False,
        'phenomenal_identity_established': False,
        'paper_or_MATLAB_analysis_reproduced': False,
        'scope': 'one source-selected trial; report-reference and event accounting, not a population or constitutive result',
    })
    return result


if __name__ == '__main__':
    result = audit()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(f"PASS: {result['source_hashes_checked']} source hashes; {result['event_count']} recorded events; report intervals accounted for without assigning experience to unresolved time.")
