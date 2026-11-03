"""Frozen maintenance/distribution contrast; no phenomenal assignments.

This reuses the existing workspace intervention audit. Matching a declared
reduced core and recording report behavior does not establish full constitutive
preservation, neural applicability, or truth of either philosophical hypothesis.
"""
from dataclasses import asdict
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = "_maintained_disclosure_intervention_audit"
spec = importlib.util.spec_from_file_location(
    NAME, ROOT / "verification/workspace_intervention_audit.py"
)
audit = importlib.util.module_from_spec(spec)
sys.modules[NAME] = audit
spec.loader.exec_module(audit)
w = audit.w


def outcome_record(out):
    return {
        "workspace": None if out.state.workspace is None else asdict(out.state.workspace),
        "feedback": out.state.feedback,
        "memory": None if out.state.memory is None else asdict(out.state.memory),
        "action": out.action,
        "comparison": out.comparison,
        "report": out.report,
    }


def run_checks():
    rows = []
    forced_cases = (
        ("unforced", audit.UNSET),
        ("cleared", None),
        ("visual_zero", w.Content("visual", 0)),
        ("auditory_one", w.Content("auditory", 1)),
    )
    for value in (0, 1):
        for report in (False, True):
            cfg = w.Config(report=report)
            proposals = (w.Proposal(w.Content("visual", value)),)
            for label, forced in forced_cases:
                reference = audit.run(w.State(), proposals, cfg, forced)
                replacement = audit.closed_loop_replacement(w.State(), proposals, cfg, forced)
                assert audit.core(reference.state) == audit.core(replacement.state)
                assert reference.report == replacement.report
                if reference.state.workspace is not None:
                    assert reference.action is not None
                    assert replacement.action is None
                    assert reference.comparison is not None
                    assert replacement.comparison is None
                if not report:
                    assert reference.report is None and replacement.report is None
                rows.append({
                    "input_value": value,
                    "report_enabled": report,
                    "workspace_intervention": label,
                    "reference": outcome_record(reference),
                    "replacement": outcome_record(replacement),
                })
    assert len(rows) == 16

    auditory = (w.Proposal(w.Content("auditory", 1)),)
    normal = audit.run(w.State(), auditory)
    cut = audit.run(w.State(), auditory, w.Config(distribute=False))
    assert normal.state.workspace == cut.state.workspace
    assert normal.state.feedback != cut.state.feedback
    forced = w.Content("visual", 0)
    normal_forced = audit.run(w.State(), auditory, forced=forced)
    cut_forced = audit.run(w.State(), auditory, w.Config(distribute=False), forced)
    replay_forced = audit.fixed_feedback_replay(cut_forced, normal.state.feedback)
    assert normal_forced.state.workspace == replay_forced.state.workspace
    assert normal_forced.state.feedback != replay_forced.state.feedback

    return {
        "status": "passed",
        "scope": "one-slot physical contrast and observation contract only",
        "comparison_rows": len(rows),
        "rows": rows,
        "lesion_changes_reduced_feedback": True,
        "fixed_replay_fails_forced_content_counterfactual": True,
        "direct_report_equal_for_reference_and_replacement": True,
        "one_slot_not_a_two_quality_unity_model": True,
        "premise_status": {
            "P1_independently_warranted_qualitative_domain": "not supplied",
            "P2_physical_basis_and_interval": "reduced core stipulated; neural boundary/interval open",
            "P3_preservation": "reduced controlled update only; full constitutive preservation open",
            "P4_distribution_absence": "original consumers disconnected in model; full physical replacement audit open",
            "P5_constitution_or_necessity": "neither rival validated",
            "P6_observation_relation": "physical report rule known; phenomenal reliability not supplied",
        },
        "consciousness_assignments": False,
        "rival_selected": None,
        "empirical_evidence_generated": False,
        "research_suite_count_changed": False,
    }


if __name__ == "__main__":
    result = run_checks()
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: {len(result['rows'])} contrast rows; neither phenomenal rival selected.")
