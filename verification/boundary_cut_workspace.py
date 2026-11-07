"""Boundary-cut bound and pre-existing-record audit of the existing workspace.

Exact finite arithmetic; neither a neural experiment nor a consciousness test.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import importlib.util
import json
import sys

root = Path(__file__).resolve().parents[1]
model_dir = root / 'research' / 'realized_workspace'
sys.path.insert(0, str(model_dir))
from model import Content, Config, State, step, signature  # noqa: E402


def tv(p, q):
    return sum(abs(p.get(k,F(0))-q.get(k,F(0))) for k in p.keys() | q.keys())/2


def joint(mu, kernels):
    return {(e,b):mu[e]*(kernels[e] if b else 1-kernels[e]) for e,b in product(range(2),repeat=2)}


def output(p, f):
    out=defaultdict(F)
    for (e,b),weight in p.items():
        out[f[2*e+b]] += weight
    return dict(out)


def finite_bound_check():
    vals=(F(0),F(1,2),F(1))
    checks=0
    for a0,a1 in product(vals,repeat=2):
        mu0={0:1-a0,1:a0};mu1={0:1-a1,1:a1}
        for kernel_flat in product(vals,repeat=4):
            k0=kernel_flat[:2];k1=kernel_flat[2:]
            p0=joint(mu0,k0);p1=joint(mu1,k1)
            delta=tv(mu0,mu1)+sum(mu0[e]*abs(k0[e]-k1[e]) for e in range(2))
            assert tv(p0,p1)<=delta
            for f in product(range(2),repeat=4):
                assert tv(output(p0,f),output(p1,f))<=min(F(1),delta)
                checks+=1
    return checks


def workspace_check():
    controls=0
    memories=[None]+[Content(s,v) for s in ('visual','auditory') for v in (0,1)]
    for source,memory,feedback,rule,target in product(('visual','auditory'),memories,
                                                       (None,'visual','auditory'),
                                                       ('copy','invert'),range(2)):
        state=State(memory=memory,feedback=feedback)
        values=[Content(source,v) for v in (0,1)]
        no_report=[step(state,rule=rule,target=target,config=Config(distribute=False,report=False),force_workspace=x) for x in values]
        with_report=[step(state,rule=rule,target=target,config=Config(distribute=False,report=True),force_workspace=x) for x in values]
        assert signature(no_report[0])==signature(no_report[1])
        assert with_report[0].report==0 and with_report[1].report==1
        assert signature(with_report[0])!=signature(with_report[1])
        controls+=1
    # The complete environment varies with the earlier content: disabling new
    # distribution cannot erase an already written consumer memory.
    records=[]
    for bit in (0,1):
        content=Content('visual',bit)
        past=step(State(),force_workspace=content)
        assert past.state.memory==content
        cut=step(past.state,config=Config(distribute=False,report=False),force_workspace=content)
        assert cut.state.memory==content and cut.action is None and cut.comparison is None and cut.report is None
        records.append(cut.state.memory.value)
    assert records==[0,1]
    # Re-intervening on present C while holding a specific prior fixed does not
    # change that prior record. It nevertheless records earlier content.
    past=step(State(),force_workspace=Content('visual',0))
    changed=step(past.state,config=Config(distribute=False,report=False),force_workspace=Content('visual',1))
    assert changed.state.memory.value==0 and changed.state.workspace.value==1
    return controls,records


def main():
    count=finite_bound_check()
    controls,records=workspace_check()
    result={'status':'passed','finite_cut_contraction_checks':count,
            'workspace_fixed_environment_cases':controls,
            'cut_with_direct_report_exposes_current_bit':True,
            'cut_without_direct_report_blocks_current_bit_in_checked_outputs_when_prior_fixed':True,
            'retained_consumer_memory_after_cut_for_past_bits':records,
            'intervening_current_source_does_not_erase_prior_record':True,
            'scope':'existing discrete workspace and finite probability kernels; no clinical or experiential claim'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
