#!/usr/bin/env python3
"""Audit a pinned public table; numerical examples, not the authors' full analysis."""
import argparse
import base64
import csv
from fractions import Fraction as F
import hashlib
import io
import json
import math
from pathlib import Path
import subprocess

COMMIT = 'fa6408b3e86a72c7a490d9cb6af461e1d8f79ee8'
EXPECTED_SHA = 'eccd45d0ac8d750d3e6574b6d2850948322a84026068d2d79cbc884783a90acd'
PAPER_TOPO_CHANCE = {'BT': F(1,5), 'NR': F(1,4), 'TJ': F(1,4), 'LJ': F(1,5)}


def exact_two_sided(k, n, p):
    probabilities = [F(math.comb(n, j))*p**j*(1-p)**(n-j) for j in range(n+1)]
    return sum(x for x in probabilities if x <= probabilities[k])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--csv', help='locally cached, unmodified pinned CSV; otherwise use gh api')
    args = ap.parse_args()
    if args.csv:
        content = Path(args.csv).read_bytes()
    else:
        encoded = subprocess.check_output([
            'gh', 'api',
            f'repos/selinbekir/splitbrain-disconnection-analysis/contents/data/disconnect_data.csv?ref={COMMIT}',
            '--jq', '.content',
        ])
        content = base64.b64decode(encoded)
    digest = hashlib.sha256(content).hexdigest()
    if digest != EXPECTED_SHA:
        raise ValueError(f'CSV SHA mismatch: {digest}')
    rows = list(csv.DictReader(io.StringIO(content.decode('utf-8-sig'))))
    topo = [r for r in rows if r['task'] == 'topognosis']
    assert len(topo) == 8
    discrepancies = []
    for row in topo:
        stated = F(row['chance_level'])
        paper = PAPER_TOPO_CHANCE[row['patient']]
        if stated != paper:
            discrepancies.append({
                'patient':row['patient'], 'condition':row['condition'],
                'successes':int(row['num_corr']), 'trials':int(row['total_trialno']),
                'csv_chance':str(stated), 'paper_methods_chance':str(paper),
                'p_two_sided_csv_chance':float(exact_two_sided(int(row['num_corr']), int(row['total_trialno']), stated)),
                'p_two_sided_paper_chance':float(exact_two_sided(int(row['num_corr']), int(row['total_trialno']), paper)),
            })
    assert len(discrepancies) == 4
    lj_intra = next(d for d in discrepancies if d['patient']=='LJ' and d['condition']=='intra_uncrossed')
    tj_inter = next(d for d in discrepancies if d['patient']=='TJ' and d['condition']=='inter_crossed')
    assert (lj_intra['successes'],lj_intra['trials']) == (3,4)
    assert exact_two_sided(3,4,F(1,5)) == F(17,625)
    assert exact_two_sided(3,4,F(1,4)) == F(13,256)
    assert (tj_inter['successes'],tj_inter['trials']) == (4,30)
    p25 = exact_two_sided(4,30,F(1,4))
    p20 = exact_two_sided(4,30,F(1,5))
    p50 = exact_two_sided(4,30,F(1,2))
    assert abs(float(p25)-0.20359772225731598)<1e-14
    assert float(p20)>0.49 and float(p50)<0.00006
    # 4/30 with p=.5 is an example in the notebook, not proof of the paper's simulation choices.
    bt = {(r['condition'], int(r['num_corr']), int(r['total_trialno']))
          for r in topo if r['patient']=='BT'}
    assert bt == {('intra_uncrossed',10,10), ('inter_crossed',10,10)}
    p_lower = .05**(1/10)
    assert .741 < p_lower < .742
    # Raw score = p_intra-p_inter; chance baselines differ by task.
    score_at_chance20 = F(1)-F(1,5)
    score_at_chance25 = F(1)-F(1,4)
    assert (score_at_chance20,score_at_chance25)==(F(4,5),F(3,4))
    receipt = {
        'status':'passed',
        'source_repository':'https://github.com/selinbekir/splitbrain-disconnection-analysis',
        'source_commit':COMMIT,
        'source_csv_sha256':digest,
        'source_csv_rows':len(rows),
        'topognosis_chance_field_discrepancies':discrepancies,
        'tj_4_of_30_two_sided_p_by_chance':{'0.20':float(p20),'0.25':float(p25),'0.50':float(p50)},
        'lj_3_of_4_two_sided_p_by_chance':{'0.20':float(exact_two_sided(3,4,F(1,5))),'0.25':float(exact_two_sided(3,4,F(1,4)))},
        'bt_topognosis_two_10_of_10_conditions':True,
        'bt_10_of_10_one_sided_95pct_binomial_lower_bound':p_lower,
        'raw_difference_perfect_intra_at_20pct_chance':str(score_at_chance20),
        'raw_difference_perfect_intra_at_25pct_chance':str(score_at_chance25),
        'scope':'Independent calculations on aggregate CSV and paper-method entries; no patient-level trials, MRI replay, full-author pipeline or proof of causal/experiential interpretation.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))


if __name__=='__main__':
    main()
