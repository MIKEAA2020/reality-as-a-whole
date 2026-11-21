#!/usr/bin/env python3
"""Audit published supplement arithmetic and two-value oracle fit; not a clinical analysis."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product
import json,math
from pathlib import Path

# Each side: (frequency Hz, duration seconds, supplement per-pulse charge µC,
# supplement per-trial charge µC). Numbers transcribed from supplement table 2;
# the participant/electrode descriptors retain the source's contextual identity.
ROWS=[
 ('8','OFC1-OFC3',(50,1,'0.8','40'),(5,1,'0.8','4')),
 ('8','OFC1-OFC3',(5,1,'0.8','4'),(2,1,'0.8','1.6')),
 ('8','REF-OFC3',(2,1,'0.8','1.6'),(50,1,'0.8','40')),
 ('8','REF-OFC3',(5,1,'1.6','8'),(10,1,'1.6','16')),
 ('8','REF-OFC3',(20,1,'1.6','32'),(2,1,'1.6','3.2')),
 ('8','REF-OFC3',(2,1,'1.6','3.2'),(5,1,'1.6','8')),
 ('10','OFC1-OFC3',(50,1,'1','100'),(2,5,'1','50')),
 ('10','OFC1-OFC3',(2,5,'1','50'),(5,5,'1','125')),
 ('10','OFC1-OFC3',(5,5,'1','125'),(10,5,'1','250')),
 ('10','OFC1-OFC3',(10,5,'1','50'),(20,3,'1','60')),
 ('10','OFC1-OFC2',(10,5,'1','50'),(20,1,'1','20')),
 ('12','OFC1-OFC2',(5,1,'1.2','36'),(2,1,'1.2','14.4')),
 ('12','OFC1-OFC2',(50,1,'0.4','20'),(5,1,'1.2','6')),
 ('15','INS1-INS2',(20,1,'1.2','24'),(50,1,'0.8','40')),
 ('15','INS1-INS2',(10,1,'2','20'),(20,1,'0.8','16')),
]
VALUES=tuple(map(F,(10,20,40,60)))

def audit(rows=ROWS):
    diffs=[];cells=0;affected=0; settings=defaultdict(set)
    for sub,site,*sides in rows:
        row_bad=False
        for index,(freq,dur,pulse,reported) in enumerate(sides):
            true=F(freq)*F(dur)*F(pulse);printed=F(reported);cells+=1
            settings[(sub,site,freq,dur,F(pulse))].add(printed)
            if true!=printed:
                row_bad=True
                diffs.append({'subject':sub,'site':site,'side':index+1,'frequency_hz':freq,
                  'duration_seconds':dur,'given_pulse_uC':pulse,'printed_trial_uC':reported,
                  'formula_trial_uC':str(true),'printed_over_formula':str(printed/true)})
        affected+=row_bad
    collisions=[{'subject':sub,'site':site,'frequency_hz':freq,'duration_seconds':dur,
                 'pulse_uC':str(pulse),'different_printed_trial_uC':sorted(map(str,vals))}
                for (sub,site,freq,dur,pulse),vals in settings.items() if len(vals)>1]
    return {'paired_rows':len(rows),'cells':cells,'discrepant_cells':len(diffs),
            'affected_rows':affected,'different_displayed_trial_charge_for_same_listed_settings':collisions,
            'differences':diffs}

def oracle(values=VALUES):
    """Exhaust binary labels; optimize centers for each assignment and loss."""
    if not values:raise ValueError('nonempty required')
    values=tuple(F(x) for x in values);best=None
    for labels in product((0,1),repeat=len(values)):
        clusters=[[v for v,l in zip(values,labels) if l==c] for c in (0,1)]
        clusters=[sorted(c) for c in clusters if c]
        sq=sum(sum((v-sum(c)/len(c))**2 for v in c) for c in clusters)/len(values)
        ae=sum(sum(abs(v-c[(len(c)-1)//2]) for v in c) for c in clusters)/len(values)
        mx=max((c[-1]-c[0])/2 for c in clusters)
        if best is None:best={'mse':sq,'mae':ae,'max':mx}
        else:
            for k,v in (('mse',sq),('mae',ae),('max',mx)):best[k]=min(best[k],v)
    return {'published_values_percent':[str(v) for v in values], 'assignments_examined':2**len(values),
            'minimum_mean_squared_error':str(best['mse']),'minimum_rmse':math.sqrt(float(best['mse'])),
            'minimum_mean_absolute_error':str(best['mae']), 'minimum_max_absolute_error':str(best['max'])}

def main():
    r={'supplement_charge_audit':audit(),'four_report_two_level_oracle':oracle(),
       'scope':'arithmetic checks on transcribed displayed reports and formula, not delivered charge, q, experience measurement or battery pass'}
    text=json.dumps(r,indent=2)+'\n';Path(__file__).with_suffix('.json').write_text(text);print(text)
if __name__=='__main__':main()
