"""Exact response distributions through the existing realized workspace.

TWO RESET TRIALS: first visual, then auditory. Not one claimed episode.
No trial, register, or probability distribution is labeled conscious.
"""
import importlib.util
from pathlib import Path
import sys
from model import deterministic_channel

_name = '_constitutive_geometry_workspace'
_spec = importlib.util.spec_from_file_location(_name, Path(__file__).resolve().parents[1] / 'realized_workspace' / 'model.py')
workspace = importlib.util.module_from_spec(_spec)
sys.modules[_name] = workspace
_spec.loader.exec_module(workspace)


def outputs(values, config=None, override_monitor=False):
    config = config or workspace.Config()
    results = []
    for source, value in zip(workspace.SOURCES, values):
        kwargs = {'force_monitor': workspace.Content(source, 1-value)} if override_monitor else {}
        results.append(workspace.step(workspace.State(),
                       (workspace.Proposal(workspace.Content(source, value)),),
                       config=config, **kwargs))
    return results


def response_family(family, channel='action', config=None, override_monitor=False):
    if channel not in ('action', 'report', 'monitor'):
        raise ValueError('Declared evidence channel required')
    def read(values):
        result = outputs(values, config, override_monitor)
        if channel == 'monitor':
            return tuple(r.monitor.value if r.monitor else None for r in result)
        return tuple(getattr(r, channel) for r in result)
    return deterministic_channel(family, read)
