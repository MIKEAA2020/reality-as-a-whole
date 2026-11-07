"""Audit maintenance/broadcast interventions using the existing workspace model.

No phenomenal labels, neural data, or third-party analysis are used. The
comparisons concern a declared REDUCED core (workspace, feedback), not complete
physical equivalence. These checks are separate from research/run_checks.py.
"""
from dataclasses import replace
from itertools import product
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = '_workspace_intervention_audit_model'
spec = importlib.util.spec_from_file_location(NAME, ROOT/'research/realized_workspace/model.py')
w = importlib.util.module_from_spec(spec)
sys.modules[NAME] = w
spec.loader.exec_module(w)

CONTENTS = tuple(w.Content(s, v) for s, v in product(w.SOURCES, (0, 1)))
UNSET = object()


def core(state):
    return state.workspace, state.feedback


def run(state, proposals=(), config=None, forced=UNSET):
    kwargs = {} if forced is UNSET else {'force_workspace': forced}
    return w.step(state, proposals, config=config or w.Config(), **kwargs)


def closed_loop_replacement(state, proposals=(), config=None, forced=UNSET):
    """Disable distribution; replace feedback by a new content-sensitive route.

This matches the REDUCED update, not the physical causal path or all effects
of interventions on omitted consumer variables.
"""
    cfg = config or w.Config()
    if not cfg.distribute:
        raise ValueError("Reference configuration must enable distribution")
    out = run(state, proposals, replace(cfg, distribute=False), forced)
    new_w = out.state.workspace
    feedback = new_w.source if new_w is not None and cfg.feedback and cfg.action else None
    return replace(out, state=replace(out.state, feedback=feedback))


def fixed_feedback_replay(outcome, value):
    return replace(outcome, state=replace(outcome.state, feedback=value))


def main():
    auditory = (w.Proposal(w.Content('auditory', 1)),)
    competing = (w.Proposal(w.Content('visual', 0)), w.Proposal(w.Content('auditory', 1)))
    initial = w.State()
    normal = run(initial, auditory)
    cut = run(initial, auditory, w.Config(distribute=False))
    assert normal.state.workspace == cut.state.workspace
    assert normal.report == cut.report
    assert normal.state.feedback == 'auditory' and cut.state.feedback is None
    next_normal = run(normal.state, competing)
    next_cut = run(cut.state, competing, w.Config(distribute=False))
    assert next_normal.winner.source == 'auditory'
    assert next_cut.winner.source == 'visual'

    replay = fixed_feedback_replay(cut, normal.state.feedback)
    assert core(replay.state) == core(normal.state)
    # A content intervention exposes what the fixed replay fails to preserve.
    forced = w.Content('visual', 0)
    normal_do = run(initial, auditory, forced=forced)
    cut_do = run(initial, auditory, w.Config(distribute=False), forced)
    replay_do = fixed_feedback_replay(cut_do, normal.state.feedback)
    assert normal_do.state.workspace == replay_do.state.workspace
    assert normal_do.state.feedback == 'visual'
    assert replay_do.state.feedback == 'auditory'

    repaired = closed_loop_replacement(initial, auditory)
    repaired_do = closed_loop_replacement(initial, auditory, forced=forced)
    assert core(repaired.state) == core(normal.state)
    assert core(repaired_do.state) == core(normal_do.state)
    assert normal.action == 1 and repaired.action is None
    assert normal.comparison is True and repaired.comparison is None
    assert repaired.report == normal.report

    proposals = [()]
    proposals.extend((w.Proposal(c),) for c in CONTENTS)
    proposals.extend((w.Proposal(w.Content('visual', a)), w.Proposal(w.Content('auditory', b)))
                     for a, b in product((0, 1), repeat=2))
    states = [w.State(c, m, f) for c, m, f in product((None,)+CONTENTS, (None,)+CONTENTS, (None,)+w.SOURCES)]
    configs = [w.Config(entry=e, maintain=m, action=a, feedback=f)
               for e, m, a, f in product((False, True), repeat=4)]
    count = 0
    for state, inp, cfg, forced_value in product(states, proposals, configs, (UNSET, None)+CONTENTS):
        ordinary = run(state, inp, cfg, forced_value)
        repair = closed_loop_replacement(state, inp, cfg, forced_value)
        assert core(ordinary.state) == core(repair.state)
        count += 1
    assert count == 64800

    # Multiple steps with changing input, and matched report-off condition.
    sn, sr = w.State(), w.State()
    trajectory = []
    for inp in (auditory, competing, (), (w.Proposal(w.Content('visual', 1), 2),), competing):
        on = run(sn, inp, w.Config(report=False))
        rr = closed_loop_replacement(sr, inp, w.Config(report=False))
        assert core(on.state) == core(rr.state)
        assert on.report is None and rr.report is None
        trajectory.append({'workspace': None if on.state.workspace is None else
                           [on.state.workspace.source, on.state.workspace.value],
                           'feedback': on.state.feedback})
        sn, sr = on.state, rr.state

    result = {
        'scope': 'controlled reduced-state comparisons; not neural or phenomenal evidence',
        'reduced_core': ['workspace', 'feedback'],
        'excluded_from_core': ['consumer memory', 'action', 'comparison', 'report', 'physical feedback pathway'],
        'lesion_witness': {
            'current_workspace_and_report_match': True,
            'next_equal_competition_normal_winner': next_normal.winner.source,
            'next_equal_competition_cut_winner': next_cut.winner.source,
        },
        'fixed_replay_witness': {
            'baseline_reduced_state_matches': True,
            'under_forced_visual_content_normal_feedback': normal_do.state.feedback,
            'under_forced_visual_content_replay_feedback': replay_do.state.feedback,
        },
        'closed_loop_replacement': {
            'one_step_comparisons': count,
            'prepared_states': len(states), 'input_sets': len(proposals),
            'configurations': len(configs), 'workspace_interventions_including_natural': 6,
            'reduced_updates_all_match': True,
            'consumer_outputs_can_differ': True,
            'full_physical_equivalence_claimed': False,
            'matching_report_off_trajectory': trajectory,
        },
        'consciousness_assignment_supplied': False,
        'research_suite_count_changed': False,
    }
    (ROOT/'verification/workspace_intervention_audit.json').write_text(json.dumps(result, indent=2)+'\n')
    print(f'Verified lesion and replay witnesses and {count:,} reduced-state update comparisons; no phenomenal assignment.')

if __name__ == '__main__':
    main()
