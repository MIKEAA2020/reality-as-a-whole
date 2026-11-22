#!/usr/bin/env python3
"""Post-hoc S09 3-state EEG/report pilot, not experiential calibration."""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy.io import loadmat
from roy_s09_scan1_alignment_gate import sample_indices
from roy_s09_eeg_report_transfer import feature, sha

TRAIN = (1, 2, 3)
TEST = (5, 7)
CLASSES = (1, 2, 3)


def label_window(state):
    state = np.asarray(state)
    if state.ndim != 1 or state.size == 0 or np.any(~np.isin(state, (0, 1, 2, 3))):
        raise ValueError('Invalid report state')
    counts = [int(np.count_nonzero(state == k)) for k in CLASSES]
    best = int(np.argmax(counts))
    return CLASSES[best] if 4 * counts[best] >= 3 * len(state) else 0


def read_windows(path, expected_sha):
    if sha(path) != expected_sha:
        raise ValueError('Source EEG hash mismatch')
    fields = ['EEG', 'sampling_freq', 'freqtag1', 'freqtag2', 'chanlabels',
              'latency_s1', 'latency_s2', 'latency_s3', 'latency_trial', 'bad_epoch']
    d = loadmat(path, squeeze_me=True, struct_as_record=False, variable_names=fields)
    fs = int(d['sampling_freq'])
    eeg = d['EEG']
    names = [str(x) for x in np.atleast_1d(d['chanlabels'])]
    if fs != 250 or float(eeg.srate) != fs or names.count('POz') != 1:
        raise ValueError('Unexpected sample rate or channel')
    x = np.asarray(eeg.data)
    mask = np.atleast_1d(d['bad_epoch'])
    if x.ndim != 2 or x.shape != (len(names), len(mask)) or not np.all(np.isin(mask, (0, 1))):
        raise ValueError('Unexpected EEG/mask dimensions or coding')
    signal = x[names.index('POz')]
    starts = sample_indices(d['latency_trial']) - 1
    if len(starts) != 5 or np.any(np.diff(starts) < 42*fs):
        raise ValueError('Invalid trial markers')
    events = sorted((int(t)-1, k) for k in CLASSES for t in sample_indices(d['latency_s'+str(k)]))
    if len({t for t, _ in events}) != len(events):
        raise ValueError('Ambiguous event ordering')
    low, high = sorted((float(d['freqtag1']), float(d['freqtag2'])))
    if not (abs(low-6.6666666667)<1e-6 and abs(high-8.5714285714)<1e-6):
        raise ValueError('Unexpected tag frequencies')
    result = []
    width = 2*fs
    for start in starts:
        end = int(start) + 42*fs
        if start < 0 or end > len(mask):
            raise ValueError('Trial out of bounds')
        state = np.zeros(42*fs, dtype=np.uint8)
        local = [(t, k) for t, k in events if start <= t < end]
        for i, (t, k) in enumerate(local):
            right = local[i+1][0] if i+1 < len(local) else end
            state[t-start:right-start] = k
        for slot in range(21):
            offset = slot*width
            bad = bool(np.any(mask[start+offset:start+offset+width]))
            # Computed for all clean windows, irrespective of report outcome.
            z = None if bad else feature(signal[start+offset:start+offset+width], fs, low, high)
            result.append({'slot': slot, 'label': label_window(state[offset:offset+width]),
                           'bad': bad, 'feature': z})
    if len(result) != 105:
        raise ValueError('Unexpected window count')
    return result


def majority(labels, fallback=1):
    counts = [labels.count(k) for k in CLASSES]
    return min(k for k in CLASSES if counts[k-1] == max(counts)) if labels else fallback


def train(rows):
    eligible = [r for r in rows if r['label'] in CLASSES and not r['bad']]
    counts = {k: sum(r['label'] == k for r in eligible) for k in CLASSES}
    if any(counts[k] == 0 for k in CLASSES):
        raise ValueError('Missing training class: ' + str(counts))
    means = {}
    for k in CLASSES:
        vals = [r['feature'] for r in eligible if r['label'] == k]
        if any(v is None or not np.isfinite(v) for v in vals):
            raise ValueError('Invalid training feature')
        means[k] = float(np.mean(vals))
    default = majority([r['label'] for r in eligible])
    slots = []
    for slot in range(21):
        labels = [r['label'] for r in eligible if r['slot'] == slot]
        counts_slot = [labels.count(k) for k in CLASSES]
        # Unlike smallest-code global ties, within-slot ties fall back to global.
        slots.append(CLASSES[counts_slot.index(max(counts_slot))]
                     if labels and counts_slot.count(max(counts_slot)) == 1 else default)
    return {'means': means, 'majority': default, 'slot_rules': slots, 'class_counts': counts}


def predictions(row, model):
    if row['bad']:
        return None
    value = row['feature']
    if value is None or not np.isfinite(value) or not 0 <= row['slot'] < 21:
        raise ValueError('Invalid clean window')
    return {'eeg': min(CLASSES, key=lambda k: (abs(value-model['means'][k]), k)),
            'majority': model['majority'], 'time_only': model['slot_rules'][row['slot']]}


def assess(rows, model):
    if not rows:
        raise ValueError('No test windows')
    confusion = {key: [[0]*3 for _ in CLASSES] for key in ('eeg', 'majority', 'time_only')}
    unlabeled_pred = {key: [0]*3 for key in confusion}
    for row in rows:
        pred = predictions(row, model)
        if pred is None:
            continue
        for key, value in pred.items():
            if row['label'] in CLASSES:
                confusion[key][row['label']-1][value-1] += 1
            else:
                unlabeled_pred[key][value-1] += 1
    outcomes = {}
    for key, cm in confusion.items():
        counts = [sum(row) for row in cm]
        total = sum(counts)
        correct = sum(cm[k][k] for k in range(3))
        recall = [cm[k][k]/counts[k] if counts[k] else None for k in range(3)]
        outcomes[key] = {'confusion_true_rows_pred_columns': cm, 'class_counts': counts,
                         'class_recalls': recall, 'labeled_clean_accuracy': correct/total if total else None,
                         'macro_recall': sum(recall)/3 if all(r is not None for r in recall) else None,
                         'full_grid_correct_fraction': correct/len(rows),
                         'clean_unresolved_predictions': unlabeled_pred[key]}
    unlabeled = sum(r['label'] == 0 for r in rows)
    bad = sum(r['bad'] for r in rows)
    overlap = sum(r['label'] == 0 and r['bad'] for r in rows)
    return {'total_windows': len(rows), 'report_unresolved_windows': unlabeled,
            'artifact_windows': bad, 'unresolved_artifact_overlap': overlap,
            'labeled_clean_windows': len(rows)-unlabeled-bad+overlap, 'models': outcomes}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    rows = {}
    for scan in TRAIN + TEST:
        path = args.directory / f'S09_scan{scan}_filtered_gac_cbc.mat'
        info = json.loads((root/f'roy_s09_scan{scan}_inspection.json').read_text())
        rows[scan] = read_windows(path, info['sha256'])
    model = train([r for scan in TRAIN for r in rows[scan]])
    summary = {'scope': 'Previously inspected single participant: exploratory fit-held-out 3-state report prediction, not experience calibration.',
               'input_hashes_match_prior_inspections': True, 'train_scans': list(TRAIN), 'test_scans': list(TEST),
               'scoring': '2 s windows, >=75% same nonzero report code; unknown or transitions unresolved; artifact abstention',
               'training_model': model, 'test_by_scan': {str(s): assess(rows[s], model) for s in TEST},
               'test_pooled': assess([r for s in TEST for r in rows[s]], model)}
    text = json.dumps(summary, indent=2, allow_nan=False) + '\n'
    args.output.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
