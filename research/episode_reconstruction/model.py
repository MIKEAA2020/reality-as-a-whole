"""Episode-first identification design: SYNTHETIC predictions only.

The three mechanisms supply physical storage/readout dynamics plus candidate
presentational readouts. Identifying these readouts with experience is an
explicit bridge hypothesis, not an output of the simulator. Source-event
identity, presentation-token identity, and reported labels remain distinct.
"""
from dataclasses import dataclass
from itertools import combinations

KINDS = ('persistent', 'sequential', 'late_replay')


@dataclass(frozen=True)
class InputEvent:
    key: str
    label: str


@dataclass(frozen=True)
class Protocol:
    # Items are source-event occurrence identifiers, not qualitative types.
    inputs: tuple
    report_tick: int
    clear_workspace_before: frozenset = frozenset()
    clear_record_before: frozenset = frozenset()
    skip_record_at: frozenset = frozenset()
    suppress_emission: bool = False

    def __post_init__(self):
        if self.report_tick < len(self.inputs) or self.report_tick < 0:
            raise ValueError('Report at or after end of input sequence required')
        keys = [e.key for row in self.inputs for e in row]
        if len(keys) != len(set(keys)):
            raise ValueError('Source occurrence identifiers must be distinct')
        ticks = self.clear_workspace_before | self.clear_record_before | self.skip_record_at
        if any(not isinstance(t, int) or not 0 <= t <= self.report_tick for t in ticks):
            raise ValueError('Intervention tick outside protocol')


@dataclass(frozen=True)
class CandidatePresentation:
    run: str
    tick: int
    sources: frozenset

    def occurrence_tokens(self):
        # Retained/replayed source information is not the same presentation token.
        return frozenset((self.run, self.tick, source) for source in self.sources)


@dataclass(frozen=True)
class Trace:
    kind: str
    run: str
    presentation: tuple
    workspace: tuple
    record: tuple
    report: frozenset | None

    def source_profile(self):
        return tuple(p.sources for p in self.presentation)


def simulate(kind, protocol, *, run='run-0'):
    if kind not in KINDS:
        raise ValueError('Unknown mechanism')
    workspace, record = frozenset(), frozenset()
    presentations, workspaces, records = [], [], []
    output = None
    for tick in range(protocol.report_tick+1):
        current = frozenset(e.key for e in protocol.inputs[tick]) if tick < len(protocol.inputs) else frozenset()
        if tick in protocol.clear_workspace_before:
            workspace = frozenset()
        if tick in protocol.clear_record_before:
            record = frozenset()
        if tick not in protocol.skip_record_at:
            record |= current
        if kind == 'persistent':
            workspace |= current
            proposed = workspace
        elif kind == 'late_replay' and tick == protocol.report_tick:
            workspace = record
            proposed = workspace
        else:
            workspace = current
            proposed = current
        presentations.append(CandidatePresentation(run,tick,proposed))
        workspaces.append(workspace)
        records.append(record)
        if tick == protocol.report_tick and not protocol.suppress_emission:
            output = record
    return Trace(kind,run,tuple(presentations),tuple(workspaces),tuple(records),output)


def baseline():
    return Protocol(tuple((InputEvent(label+'@input',label),) for label in 'ABC'),3)


def label_report(report, protocol):
    if report is None:
        return None
    labels={e.key:e.label for row in protocol.inputs for e in row}
    return frozenset(labels[key] for key in report)


def identify(traces, observations):
    """Use stipulated candidate episode observations (tick -> source support).

    Actual first-person evidence needs calibration and uncertainty; these exact
    comparisons are a finite test design, not a phenomenal measurement oracle.
    """
    return tuple(t.kind for t in traces
                 if all(t.presentation[tick].sources == support for tick,support in observations.items()))


def identify_uncertain(traces, observations):
    """Each tick maps to a SET of admissible source-support judgments.

    Returns a compatibility set, not likelihoods or a posterior. The uncertainty
    set itself must be justified by the evidence, not tuned to save a model.
    """
    return tuple(t.kind for t in traces
                 if all(t.presentation[tick].sources in allowed
                        for tick, allowed in observations.items()))


def minimal_temporal_designs(traces):
    """Smallest sets of times separating the specified candidate profiles.

    This presupposes access to those presentation contrasts. Physical-report
    observations alone do not have the same separating power.
    """
    traces=tuple(traces)
    if not traces:
        raise ValueError('Need candidate traces')
    ticks=range(len(traces[0].presentation))
    for n in range(len(traces[0].presentation)+1):
        selected=[]
        for times in combinations(ticks,n):
            profiles=[tuple(t.presentation[i].sources for i in times) for t in traces]
            if len(set(profiles))==len(traces):
                selected.append(times)
        if selected:
            return tuple(selected)
    return ()


def report_identification(traces, report):
    return tuple(t.kind for t in traces if t.report==report)


def passive_relabel(protocol,mapping):
    keys={e.key for row in protocol.inputs for e in row}
    if set(mapping)!=keys or len(set(mapping.values()))!=len(keys):
        raise ValueError('Need bijective source-event rename')
    return Protocol(tuple(tuple(InputEvent(mapping[e.key],e.label) for e in row) for row in protocol.inputs),
                    protocol.report_tick,protocol.clear_workspace_before,protocol.clear_record_before,
                    protocol.skip_record_at,protocol.suppress_emission)
