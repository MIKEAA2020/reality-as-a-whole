"""Minimal implemented workspace, not a validated neural or phenomenal theory.
Selection, one-slot maintenance, multiple causal consumers, control feedback,
and report are explicitly distinct. All timing and gains are stipulated.
"""
from dataclasses import dataclass
import math

SOURCES=('visual','auditory')
RULES=('copy','invert')
_UNSET=object()

@dataclass(frozen=True)
class Content:
    source: str
    value: int
    def __post_init__(self):
        if self.source not in SOURCES or type(self.value) is not int or self.value not in (0,1):raise ValueError('Declared specialist and binary content required')

@dataclass(frozen=True)
class Proposal:
    content: Content
    salience: float=1.
    def __post_init__(self):
        if not isinstance(self.content,Content) or not math.isfinite(self.salience) or self.salience<0:raise ValueError('Valid content and nonnegative finite salience required')

@dataclass(frozen=True)
class State:
    workspace: Content|None=None
    memory: Content|None=None
    feedback: str|None=None
    def __post_init__(self):
        if any(v is not None and not isinstance(v,Content) for v in (self.workspace,self.memory)) or self.feedback not in (*SOURCES,None):raise ValueError('Invalid state')

@dataclass(frozen=True)
class Config:
    entry: bool=True
    distribute: bool=True
    maintain: bool=True
    report: bool=True
    feedback: bool=True
    action: bool=True
    def __post_init__(self):
        if any(type(v) is not bool for v in self.__dict__.values()):raise ValueError('Boolean switches required')

@dataclass(frozen=True)
class Outcome:
    state: State
    winner: Content|None
    monitor: Content|None
    local: tuple
    action: int|None
    comparison: bool|None
    report: int|None


def select(proposals,feedback=None):
    proposals=tuple(proposals)
    if any(not isinstance(p,Proposal) for p in proposals) or len({p.content.source for p in proposals})!=len(proposals) or feedback not in (*SOURCES,None):raise ValueError('At most one valid proposal per specialist required')
    if not proposals:return None
    # Explicit toy attention bias and tie rule, not derived neural constants.
    winner=max(proposals,key=lambda p:(p.salience+(.25 if p.content.source==feedback else 0),-SOURCES.index(p.content.source)))
    return winner.content


def step(state,proposals=(),rule='copy',target=1,config=Config(),force_workspace=_UNSET,force_monitor=_UNSET):
    if not isinstance(state,State) or not isinstance(config,Config) or rule not in RULES or type(target) is not int or target not in (0,1):raise ValueError('Invalid state, task, target, or configuration')
    proposals=tuple(proposals);winner=select(proposals,state.feedback if config.feedback else None)
    workspace=(winner if winner is not None else state.workspace if config.maintain else None) if config.entry else None
    if force_workspace is not _UNSET:
        if force_workspace is not None and not isinstance(force_workspace,Content):raise ValueError('Valid workspace intervention required')
        workspace=force_workspace
    monitor=workspace
    if force_monitor is not _UNSET:
        if force_monitor is not None and not isinstance(force_monitor,Content):raise ValueError('Valid monitor intervention required')
        monitor=force_monitor
    available=workspace if config.distribute else None
    memory=available if available is not None else state.memory
    action=(available.value if rule=='copy' else 1-available.value) if available is not None and config.action else None
    comparison=(available.value==target) if available is not None else None
    feedback=available.source if config.feedback and action is not None else None
    report=workspace.value if workspace is not None and config.report else None
    return Outcome(State(workspace,memory,feedback),winner,monitor,tuple((p.content.source,p.content.value) for p in proposals),action,comparison,report)


def signature(outcome):
    """Observable consumer outputs, not a consciousness/integration score."""
    return (outcome.state.memory,outcome.action,outcome.comparison,outcome.report)
