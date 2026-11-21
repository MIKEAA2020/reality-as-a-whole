#!/usr/bin/env python3
"""Aggregate order/RT metadata; no reported pain values or participant outputs."""
import argparse
import collections
import json
from fractions import Fraction
from pathlib import Path

from paingen_condition_subset_diagnostic import obtain_events
from paingen_response_time_reconstruction import rt_status
from paingen_trial_provenance_audit import COMMIT, PATH, finite, parse_run, percentile

ORDERS = ('intensity_first', 'unpleasantness_first')
STATUSES = ('below', 'in_range', 'above', 'unavailable')


def timing_category(duration, rt, tol=0.001):
    d, r = finite(duration), finite(rt)
    if d is None or r is None or d <= 0 or r < 0:
        return 'unusable', None
    diff = d-r
    if abs(diff) <= tol:
        return 'within_0.001', diff
    return ('duration_greater' if diff > 0 else 'response_time_greater'), diff


def person_summary(people):
    positive = negative = zero = missing = eligible = 0
    total = Fraction()
    for orders in people.values():
        if not all(sum(orders[o].values()) > 0 for o in ORDERS):
            continue
        eligible += 1
        missing += any(orders[o]['unavailable'] > 0 for o in ORDERS)
        x, y = orders[ORDERS[0]], orders[ORDERS[1]]
        num_x, den_x = x['in_range'], sum(x.values())
        num_y, den_y = y['in_range'], sum(y.values())
        cross = num_x*den_y - num_y*den_x
        positive += cross > 0
        negative += cross < 0
        zero += cross == 0
        total += Fraction(num_x, den_x) - Fraction(num_y, den_y)
    return {'eligible_people': eligible, 'intensity_first_higher': positive,
            'unpleasantness_first_higher': negative, 'equal': zero,
            'with_any_unavailable_rt': missing,
            'mean_person_rate_difference': float(total/eligible) if eligible else None,
            'mean_person_rate_difference_exact': str(total/eligible) if eligible else None}


def synthetic_selection():
    # O and U independent fair bits; Y(O)=U and R depends on their agreement.
    joint = {}
    for order in (0, 1):
        for outcome in (0, 1):
            for retained in (0, 1):
                prob_r1 = Fraction(3, 4) if order == outcome else Fraction(1, 4)
                joint[(order, outcome, retained)] = Fraction(1, 4)*(prob_r1 if retained else 1-prob_r1)
    retained = {}
    selected_means = {}
    full_means = {}
    for o in (0, 1):
        po = sum((joint[(o, y, r)] for y in (0, 1) for r in (0, 1)), Fraction())
        por = sum((joint[(o, y, 1)] for y in (0, 1)), Fraction())
        retained[o] = por/po
        selected_means[o] = joint[(o, 1, 1)]/por
        full_means[o] = sum((joint[(o, 1, r)] for r in (0, 1)), Fraction())/po
    return {'joint': {f'O={o},Y={y},R={r}': str(joint[(o,y,r)]) for o,y,r in joint},
            'retention_given_order': {str(k): str(v) for k,v in retained.items()},
            'outcome_mean_given_order_and_retained': {str(k): str(v) for k,v in selected_means.items()},
            'full_outcome_mean_given_order': {str(k): str(v) for k,v in full_means.items()},
            'population_effect': str(full_means[1]-full_means[0]),
            'retained_contrast_order1_minus_order0': str(selected_means[1]-selected_means[0])}


def timing_summary(vals):
    if not vals:
        return {'count': 0, 'min': None, 'p25': None, 'median': None, 'p75': None, 'max': None}
    return {'count': len(vals), 'min': min(vals), 'p25': percentile(vals,.25),
            'median': percentile(vals,.5), 'p75': percentile(vals,.75), 'max': max(vals)}


def analyze(files):
    orders = {o: collections.Counter() for o in ORDERS}
    unpleasantness_orders = {o: collections.Counter() for o in ORDERS}
    joint = collections.Counter()
    cats = collections.defaultdict(collections.Counter)
    diffs = collections.defaultdict(list)
    people = collections.defaultdict(lambda: {o: collections.Counter() for o in ORDERS})
    reasons = collections.Counter()
    seen = set()
    for path, blob in sorted(files.items()):
        m = PATH.fullmatch(path)
        if not m:
            raise ValueError('unexpected BIDS path')
        person, run = m['person'], m['run']
        if (person, run) in seen:
            raise ValueError('duplicate person/run')
        seen.add((person, run))
        episodes, reason = parse_run(blob)
        if reason:
            reasons[reason] += 1
            continue
        reasons['accepted'] += 1
        for _, _, first, second in episodes:
            order = 'intensity_first' if first['trial_type'] == 'int_rating' else 'unpleasantness_first'
            events = {first['trial_type']: first, second['trial_type']: second}
            if any('response_time' not in events[t] for t in ('int_rating','unp_rating')):
                raise ValueError('missing response_time column')
            si = rt_status(events['int_rating']['response_time'])
            su = rt_status(events['unp_rating']['response_time'])
            orders[order][si] += 1
            unpleasantness_orders[order][su] += 1
            people[person][order][si] += 1
            joint[(si,su)] += 1
            for t in ('int_rating','unp_rating'):
                category, diff = timing_category(events[t]['duration'], events[t]['response_time'])
                group = t+':'+order
                cats[group][category] += 1
                if diff is not None:
                    diffs[group].append(diff)
    totals = {o: sum(orders[o].values()) for o in ORDERS}
    if len(files) != 1574 or reasons['accepted'] != 1566 or totals != {'intensity_first':6200,'unpleasantness_first':6328}:
        raise ValueError('pinned prior file/run/order count mismatch')
    status_totals = {s: sum(orders[o][s] for o in ORDERS) for s in STATUSES}
    if status_totals != {'below':140, 'in_range':11022, 'above':1366, 'unavailable':0}:
        raise ValueError('pinned prior intensity RT totals mismatch')
    if sum(joint.values()) != 12528:
        raise ValueError('joint RT accounting mismatch')
    result_orders = {}
    for o in ORDERS:
        if sum(unpleasantness_orders[o].values()) != totals[o]:
            raise ValueError('unpleasantness status accounting mismatch')
        result_orders[o] = {'total': totals[o], 'intensity_rt_status': {s:orders[o][s] for s in STATUSES},
                            'intensity_in_range_proportion_all_episodes': orders[o]['in_range']/totals[o],
                            'unpleasantness_rt_status': {s:unpleasantness_orders[o][s] for s in STATUSES},
                            'unpleasantness_in_range_proportion_all_episodes': unpleasantness_orders[o]['in_range']/totals[o]}
    timing = {}
    for t in ('int_rating','unp_rating'):
        for o in ORDERS:
            key = t+':'+o
            category_counts = {k: cats[key][k] for k in ('within_0.001','duration_greater','response_time_greater','unusable')}
            if sum(category_counts.values()) != totals[o] or sum(category_counts[k] for k in category_counts if k != 'unusable') != len(diffs[key]):
                raise ValueError('timing summary accounting mismatch')
            timing[key] = {'categories': category_counts, 'duration_minus_response_time': timing_summary(diffs[key])}
    unp_totals = {s:sum(joint[(i,s)] for i in STATUSES) for s in STATUSES}
    result = {'status':'completed', 'scope':'retrospective metadata-only descriptive audit, not outcome or causal analysis',
              'dataset_commit':COMMIT, 'event_files_verified':len(files), 'accepted_runs':reasons['accepted'],
              'rejection_reasons':{k:v for k,v in sorted(reasons.items()) if k != 'accepted'},
              'episodes':12528, 'orders':result_orders, 'intensity_status_total':status_totals,
              'unpleasantness_status_total':unp_totals,
              'joint_intensity_by_unpleasantness_status': {i:{u:joint[(i,u)] for u in STATUSES} for i in STATUSES},
              'timing_fields':timing, 'person_level_descriptive':person_summary(people),
              'synthetic_selection_control': synthetic_selection(),
              'privacy':'No identifiers, individual records, rating values, outcome tables or MRI saved.'}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tree', required=True)
    parser.add_argument('--archive', required=True)
    args = parser.parse_args()
    result = analyze(obtain_events(args.tree, args.archive))
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
