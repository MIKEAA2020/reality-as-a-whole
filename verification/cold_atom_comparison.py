"""Five-trace empirical clock comparison. Descriptive interpolation, not dynamics validation."""
from fractions import Fraction as Q
from pathlib import Path
from bisect import bisect_left
from collections import defaultdict
from itertools import combinations
from math import sqrt
import hashlib
import json

BASE = Path(__file__).parent/'sources'/'barontini_2026'


def load():
    manifest = json.loads((BASE/'manifest.json').read_text())
    out = {}
    old = json.loads((BASE.parent/'barontini_2026_clock_subset.json').read_text())
    for name, info in manifest['files'].items():
        path = BASE/info['path']
        raw = path.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == info['normalized_sha256']
        lines = raw.decode().splitlines()
        assert lines[0].split() == ['t', 'tau', 'phi', 'sigma']
        original = ('\r\n'.join('\t'.join(line.split()) for line in lines)+'\r\n').encode()
        assert len(original) == info['original_size']
        assert hashlib.md5(original).hexdigest() == info['original_md5']
        rows = [[Q(x) for x in line.split()] for line in lines[1:]]
        assert all(len(row)==4 for row in rows)
        assert all(a[1]<=b[1] for a,b in zip(rows,rows[1:]))
        assert len({row[0] for row in rows}) == len(rows)
        assert all(row[2]>0 and row[3]>=0 for row in rows)
        if name in old['traces']:
            assert [(int(row[0]), str(row[1])) for row in rows] == [
                (int(t), str(Q(tau))) for t, tau in old['traces'][name]['t_tau']]
            by_t = {int(row[0]): row for row in rows}
            for r in old['traces'][name]['selected_tied_readouts']:
                assert by_t[r['t']][2:] == [Q(r['phi']), Q(r['sigma'])]
        out[name] = sorted(rows)
    assert sum(map(len, out.values())) == 272
    return out, manifest


def orientation(xs, threshold):
    """Causal hysteresis: new direction only after reversal of threshold from running extremum."""
    assert threshold>0
    direction, leg, extremum, start = 0, 0, xs[0], xs[0]
    labels = [(0, 0)]
    for x in xs[1:]:
        if direction == 0:
            if x-start >= threshold:
                direction, extremum = 1, x
            elif start-x >= threshold:
                direction, extremum = -1, x
        elif direction == 1:
            extremum = max(extremum, x)
            if extremum-x >= threshold:
                direction, leg, extremum = -1, leg+1, x
        else:
            extremum = min(extremum, x)
            if x-extremum >= threshold:
                direction, leg, extremum = 1, leg+1, x
        labels.append((direction, leg))
    return labels


def features(rows):
    phi = [r[2]*10**6 for r in rows]
    path = [Q(0)]
    for a, b in zip(phi, phi[1:]):
        path.append(path[-1]+abs(b-a))
    labels = orientation(phi, Q(1))
    return {
        'laboratory_t': [(0, r[0]) for r in rows],
        'entropy_tau': [(0, r[1]) for r in rows],
        'instant_position': [(0, x) for x in phi],
        'oriented_position': [(label[0], x) for label, x in zip(labels, phi)],
        'leg_record_position': [(label, x) for label, x in zip(labels, phi)],
        'position_path_length': [(0, x) for x in path],
    }, phi, path, labels


def interpolate(train, x):
    groups = defaultdict(list)
    for xx, value in train:
        groups[xx].append(value)
    xs = sorted(groups)
    if not xs or x<xs[0] or x>xs[-1]:
        return None
    values = {xx: sum(v)/len(v) for xx, v in groups.items()}
    j = bisect_left(xs, x)
    if xs[j] == x:
        return values[x]
    a, b = xs[j-1], xs[j]
    return values[a]+(values[b]-values[a])*(x-a)/(b-a)


def predictions(rows, clock, scheme, positive_only=False):
    n = len(rows)
    folds = [i % 5 if scheme=='interleaved' else min(4, 5*i//n) for i in range(n)]
    eligible = [i for i in range(n) if not positive_only or rows[i][3]>0]
    out = {}
    for i in eligible:
        group, x = clock[i]
        train = [(clock[j][1], rows[j][3]*10**6) for j in eligible
                 if folds[j]!=folds[i] and clock[j][0]==group]
        prediction = interpolate(train, x)
        if prediction is not None:
            out[i] = prediction
    return out, len(eligible)


def error_summary(rows, pred, eligible, indices=None):
    ids = sorted(pred) if indices is None else sorted(indices)
    errors = [pred[i]-rows[i][3]*10**6 for i in ids]
    return {'covered': len(errors), 'eligible': eligible,
            'rmse_width_um': sqrt(float(sum(e*e for e in errors)/len(errors))) if errors else None,
            'mae_width_um': float(sum(abs(e) for e in errors)/len(errors)) if errors else None}


def heldout(rows, clock, scheme, positive_only=False):
    pred, eligible = predictions(rows,clock,scheme,positive_only)
    return error_summary(rows,pred,eligible)


def paired_comparisons(rows, clocks, scheme):
    pred = {label: predictions(rows,clock,scheme)[0] for label,clock in clocks.items()}
    reference = pred['entropy_tau']
    out = {}
    for label, values in pred.items():
        if label=='entropy_tau':
            continue
        common = set(reference).intersection(values)
        out[label] = {'common_indices': sorted(common),
                      'entropy_tau': error_summary(rows,reference,len(rows),common),
                      'other_clock': error_summary(rows,values,len(rows),common)}
    return out


def order_box(values, relative=Q(1,20)):
    # Exact feasibility for independent relative boxes, not a probability/confidence calculation.
    needed = max((max(Q(0),(a-b)/(a+b)) for a,b in combinations(values,2) if a+b),default=Q(0))
    lower, upper = [x*(1-relative) for x in values], [x*(1+relative) for x in values]
    gap = min((upper[j]-lower[i])/(j-i) for i in range(len(values)) for j in range(i+1,len(values)))
    witness = []
    if gap>0:
        for i, x in enumerate(lower):
            witness.append(x if not i else max(x,witness[-1]+gap/2))
        assert all(a<=w<=b for a,w,b in zip(lower,witness,upper))
        assert all(a<b for a,b in zip(witness,witness[1:]))
    return {'minimum_relative_half_band_percent': float(100*needed),
            'strict_order_feasible_in_5_percent_boxes': bool(witness),
            'strict_witness': [str(x) for x in witness],
            'assumption': 'independent adjustable relative boxes; not a joint statistical confidence region'}


def memory_bound(phi, widths, bin_width, readout_tolerance):
    groups = defaultdict(list)
    for i, (x, width) in enumerate(zip(phi, widths)):
        groups[int(x//bin_width)].append((width, i))
    best = None
    for label, points in groups.items():
        chosen, right = [], None
        for width, i in sorted(points):
            if right is None or width>right:
                chosen.append(i)
                right = width+2*readout_tolerance
        candidate = {'position_bin': label, 'distinct_record_labels_needed': len(chosen),
                     'witness_indices': chosen}
        if best is None or len(chosen)>best['distinct_record_labels_needed']:
            best = candidate
    k = best['distinct_record_labels_needed']
    best['record_bits_lower_bound'] = (k-1).bit_length()
    best['position_bin_um'] = str(bin_width)
    best['width_tolerance_um_assumed'] = str(readout_tolerance)
    return best


def run():
    data, manifest = load()
    result = {}
    for name, rows in data.items():
        clocks, phi, path, labels = features(rows)
        tau = [row[1] for row in rows]
        groups = defaultdict(list)
        for i, x in enumerate(tau):
            groups[x].append(i)
        tied = [idx for idx in groups.values() if len(idx)>1]
        widths = [r[3]*10**6 for r in rows]
        width_span = max((max(widths[i] for i in idx)-min(widths[i] for i in idx) for idx in tied), default=Q(0))
        sse_floor = Q(0)
        for idx in tied:
            mean = sum(widths[i] for i in idx)/len(idx)
            sse_floor += sum((widths[i]-mean)**2 for i in idx)
        total_pairs = len(rows)*(len(rows)-1)//2
        ranks = {}
        for label, values in (('entropy_tau', tau), ('instant_position', phi), ('position_path_length', path)):
            down = sum(b<a for a,b in combinations(values,2))
            ties_count = sum(b==a for a,b in combinations(values,2))
            ranks[label] = {'discordant_pairs': down, 'tied_pairs': ties_count,
                            'total_pairs': total_pairs}
        assert all(a<b for a,b in zip(path,path[1:]))
        variation_sensitivity = {}
        for stride in (1,2,3,4):
            ids = list(range(0,len(phi),stride))
            if ids[-1]!=len(phi)-1:
                ids.append(len(phi)-1)
            length = sum(abs(phi[b]-phi[a]) for a,b in zip(ids,ids[1:]))
            assert length<=path[-1]
            variation_sensitivity[str(stride)] = float(length/path[-1])
        decreases = [(a,b) for a,b in zip(tau,tau[1:]) if b<a]
        relative_drops = [100*(a-b)/a for a,b in decreases]
        benchmarks = {scheme: {label: heldout(rows,clock,scheme) for label,clock in clocks.items()}
                      for scheme in ('interleaved','blocked')}
        positive = {label: heldout(rows,clock,'interleaved',True) for label,clock in clocks.items()}
        result[name] = {
            'rows': len(rows), 'zero_width_rows': sum(x==0 for x in widths),
            'adjacent_tau_decreases': len(decreases),
            'largest_adjacent_relative_tau_drop_percent': float(max(relative_drops,default=Q(0))),
            'adjacent_tau_ties': sum(a==b for a,b in zip(tau,tau[1:])),
            'exact_tau_fibers_with_multiple_rows': len(tied),
            'largest_exact_tau_fiber_width_span_um': float(width_span),
            'central_value_minimax_width_error_floor_um': float(width_span/2),
            'central_value_global_rmse_floor_from_exact_tau_ties_um': sqrt(float(sse_floor/len(rows))),
            'rank_diagnostics': ranks,
            'entropy_clock_order_box_diagnostic': order_box(tau),
            'position_best_global_direction_half_band_percent': min(
                order_box(phi)['minimum_relative_half_band_percent'],
                order_box(list(reversed(phi)))['minimum_relative_half_band_percent']),
            'hysteresis_reversals_by_threshold_um': {str(e): max(leg for d,leg in orientation(phi,Q(e)))
                                                    for e in ('0.5','1','2','4')},
            'clock_group_counts': {label: len({g for g,x in values}) for label,values in clocks.items()},
            'path_length_retained_fraction_under_subsampling': variation_sensitivity,
            'descriptive_heldout_width_interpolation': benchmarks,
            'paired_same_rows_against_entropy_tau': {scheme: paired_comparisons(rows,clocks,scheme)
                                                   for scheme in ('interleaved','blocked')},
            'positive_width_only_interleaved_sensitivity': positive,
            'conditional_record_capacity_bounds': [memory_bound(phi,widths,Q(1),Q(e)) for e in ('0.25','0.5','1')],
        }
    for summary in result.values():
        assert summary['entropy_clock_order_box_diagnostic']['strict_order_feasible_in_5_percent_boxes']
        assert summary['position_best_global_direction_half_band_percent']>5
        for scheme in ('interleaved','blocked'):
            paired = summary['paired_same_rows_against_entropy_tau'][scheme]
            assert paired['laboratory_t']['common_indices'] == paired['position_path_length']['common_indices']
    # Synthetic assertions distinguish interpolation/uniqueness from actual physical prediction.
    assert interpolate([(Q(0),Q(2)),(Q(0),Q(4)),(Q(2),Q(7))],Q(1)) == 5
    assert interpolate([(Q(0),Q(2)),(Q(2),Q(7))],Q(-1)) is None
    toy = memory_bound([Q(0)]*3,[Q(0),Q(3),Q(6)],Q(1),Q(1))
    assert toy['distinct_record_labels_needed']==3 and toy['record_bits_lower_bound']==2
    assert order_box([Q(10),Q(8)])['minimum_relative_half_band_percent'] == float(Q(100,9))
    assert not order_box([Q(10),Q(8)])['strict_order_feasible_in_5_percent_boxes']
    assert order_box([Q(10),Q(10)])['strict_order_feasible_in_5_percent_boxes']
    assert not order_box([Q(0),Q(0)])['strict_order_feasible_in_5_percent_boxes']
    assert memory_bound([Q(0)]*2,[Q(0),Q(2)],Q(1),Q(1))['distinct_record_labels_needed']==1
    test_path = [Q(0),Q(2),Q(1),Q(0),Q(2)]
    test_labels = orientation(test_path,Q(1))
    assert test_labels == [(0,0),(1,0),(-1,1),(-1,1),(1,2)]
    for i in range(1,len(test_path)+1):
        assert orientation(test_path[:i],Q(1)) == test_labels[:i]
    return {
        'status': 'passed', 'observations': 272, 'source_files': 5,
        'all_original_md5_and_sizes_recovered': True,
        'manifest_sha256': hashlib.sha256((BASE/'manifest.json').read_bytes()).hexdigest(),
        'method': 'exact rational features/interpolation; floating-point summary errors, no extrapolation',
        'hysteresis_threshold_um': '1 (sensitivity 0.5,2,4 also reported)',
        'results': result,
        'interpretation_limits': ['laboratory chronology is used to construct every path/record feature',
                                  'interleaved and blocked splits hold out widths, not independent images or experiments',
                                  'entropy clock may share image-derived inputs with the target width',
                                  'RMSEs have different coverage; do not rank them without common test sets',
                                  'source has no per-row error/covariance model or entropy reconstruction inputs',
                                  '5 percent boxes are an illustrative feasibility diagnostic, not confidence intervals or an entropy reconstruction',
                                  'memory bounds are conditional central-value/resolution statements, not measured hardware requirements'],
    }


def make_plot(target):
    data, _ = load()
    colors = {'tau':'#2563eb','path':'#ea580c','phi':'#7c3aed'}
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1160" viewBox="0 0 1000 1160">',
           '<rect width="1000" height="1160" fill="#fff"/>',
           '<style>text{font-family:Arial,sans-serif;fill:#1f2937} .small{font-size:12px}</style>',
           '<text x="40" y="32" font-size="23" font-weight="bold">Five cold-atom traces: clock readings and recurrence</text>',
           '<text x="40" y="56" class="small">Each series normalized separately to [0,1] within its trace; central values, no smoothing or error bars.</text>']
    for k,(label,color) in enumerate((('Entropic clock',colors['tau']),('Position path length',colors['path']),('Instantaneous position',colors['phi']))):
        x=40+290*k
        svg.extend([f'<line x1="{x}" y1="78" x2="{x+25}" y2="78" stroke="{color}" stroke-width="3"/>',
                    f'<text x="{x+33}" y="82" class="small">{label}</text>'])
    for j,(name,rows) in enumerate(data.items()):
        top=115+j*190; left=72; width=720; height=132
        _,phi,path,_=features(rows)
        tau=[r[1] for r in rows]
        svg.append(f'<text x="35" y="{top+18}" font-size="15" font-weight="bold">{name}</text>')
        for y in (0,0.5,1):
            yy=top+height*(1-y)
            svg.append(f'<line x1="{left}" y1="{yy}" x2="{left+width}" y2="{yy}" stroke="#e5e7eb"/>')
            svg.append(f'<text x="{left-28}" y="{yy+4}" class="small">{y:g}</text>')
        for t in (0,40,80,120):
            xx=left+width*t/120
            svg.append(f'<line x1="{xx}" y1="{top}" x2="{xx}" y2="{top+height}" stroke="#f3f4f6"/>')
            svg.append(f'<text x="{xx-8}" y="{top+height+18}" class="small">{t}</text>')
        for label,values in (('tau',tau),('path',path),('phi',phi)):
            lo,hi=min(values),max(values)
            points=' '.join(f'{left+width*float(r[0])/120:.3f},{top+height*(1-float((v-lo)/(hi-lo))):.3f}' for r,v in zip(rows,values))
            svg.append(f'<polyline fill="none" stroke="{colors[label]}" stroke-width="2" points="{points}"/>')
        band=order_box(tau)['minimum_relative_half_band_percent']
        svg.extend([f'<text x="815" y="{top+26}" class="small">{len(rows)} observations</text>',
                    f'<text x="815" y="{top+48}" class="small">Order half-band:</text>',
                    f'<text x="815" y="{top+66}" font-size="17">{band:.3f}%</text>',
                    f'<text x="815" y="{top+86}" class="small">for entropic clock</text>',
                    f'<text x="{left+310}" y="{top+height+37}" class="small">Laboratory t (ms)</text>'])
    svg.extend(['<text x="40" y="1104" class="small">The path curve uses chronological position increments; its monotonicity is constructed, not an independent discovery of time.</text>',
                '<text x="40" y="1125" class="small">Data: Giovanni Barontini, Zenodo v1, DOI 10.5281/zenodo.19651064 (2026), CC BY 4.0. Analysis: this repository.</text>',
                '<text x="40" y="1146" class="small">Order half-band is an interval-feasibility diagnostic, not a statistical confidence level.</text>', '</svg>'])
    target.write_text('\n'.join(svg)+'\n')


if __name__ == '__main__':
    result = run()
    target = Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    make_plot(Path(__file__).with_suffix('.svg'))
    print('PASS: five source digests, 272 observations, clock fibers, heldout interpolation and record bounds')
    print(target)
