"""Finite scope and fulfillment checks; not a consciousness or universe model.

Evidence completions below are descriptive assignments, not an assertion of
multiple actual or metaphysically possible worlds. Information scopes and due
standards are stipulated solely to test stated logical implications.
"""
from itertools import product
import json
from pathlib import Path


ASSIGNMENTS = tuple(product((False, True), repeat=2))
ALL = frozenset(ASSIGNMENTS)
PROPOSITIONS = tuple(
    frozenset(a for i, a in enumerate(ASSIGNMENTS) if mask & (1 << i))
    for mask in range(1 << len(ASSIGNMENTS))
)


def evidence(actual, scope):
    if scope == "complete":
        return frozenset((actual,))
    if scope == "first":
        return frozenset(a for a in ASSIGNMENTS if a[0] == actual[0])
    if scope == "second":
        return frozenset(a for a in ASSIGNMENTS if a[1] == actual[1])
    raise ValueError("Unknown descriptive scope")


def knows(actual, scope, proposition):
    return evidence(actual, scope) <= proposition


def run():
    factivity_checks = 0
    complete_checks = 0
    witnesses = []
    for actual in ASSIGNMENTS:
        for proposition in PROPOSITIONS:
            for scope in ("complete", "first", "second"):
                assert not knows(actual, scope, proposition) or actual in proposition
                factivity_checks += 1
            assert knows(actual, "complete", proposition) == (actual in proposition)
            complete_checks += 1
        for scope, omitted in (("first", 1), ("second", 0)):
            literal = frozenset(a for a in ASSIGNMENTS if a[omitted] == actual[omitted])
            assert actual in literal
            assert knows(actual, "complete", literal)
            assert not knows(actual, scope, literal)
            assert not knows(actual, scope, ALL - literal)
            ignorance = frozenset(a for a in ASSIGNMENTS if not knows(a, scope, literal))
            assert knows(actual, "complete", ignorance)
            # Scope-transfer would erase exactly the limitation being modeled.
            expanded = evidence(actual, scope) & literal
            assert len(expanded) == 1
            assert expanded <= literal
        witnesses.append({
            "actual_assignment": actual,
            "complete_evidence": sorted(evidence(actual, "complete")),
            "first_evidence": sorted(evidence(actual, "first")),
            "second_evidence": sorted(evidence(actual, "second")),
            "complete_knows_omitted_actual_literals": True,
            "local_omitted_literals_undecided": True,
            "complete_knows_local_ignorance": True,
        })

    # Hypothetical due/fulfillment profiles, NOT physical or metaphysical worlds.
    due = (1, 1)
    shortfall_profile = (1, 0)
    fulfilled_profile = (1, 1)
    shortfall = tuple(max(t - f, 0) for t, f in zip(due, shortfall_profile))
    repaired_shortfall = tuple(max(t - f, 0) for t, f in zip(due, fulfilled_profile))
    assert shortfall == (0, 1)
    assert repaired_shortfall == (0, 0)
    assert all(b >= a for a, b in zip(shortfall_profile, fulfilled_profile))
    assert any(b > a for a, b in zip(shortfall_profile, fulfilled_profile))
    # Either profile can be perfectly recorded; recording does not change it.
    for profile in (shortfall_profile, fulfilled_profile):
        recorded_profile = tuple(profile)
        assert recorded_profile == profile
    return {
        "status": "passed",
        "scope": "finite descriptive evidence and stipulated fulfillment only",
        "factivity_checks": factivity_checks,
        "complete_truth_equivalence_checks": complete_checks,
        "assignment_witnesses": witnesses,
        "fulfillment_witness": {
            "stipulated_due": due,
            "shortfall_profile": shortfall_profile,
            "fulfilled_profile": fulfilled_profile,
            "shortfall": shortfall,
            "fulfilled_shortfall": repaired_shortfall,
            "epistemic_completeness_alone_does_not_select_fulfillment": True,
        },
        "limitations": [
            "No intrinsic perspective selection or phenomenal identity is modeled.",
            "Finite propositional completeness is not a proof of absolute omniscience.",
            "No metaphysical admissibility of a less harmful universe is established.",
            "Due standards and comparison are supplied, not normatively grounded.",
            "No actuality, perfect goodness, or personal-survival claim is established.",
        ],
    }


if __name__ == "__main__":
    result = run()
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"PASS: finite scope and fulfillment checks; {output.name}")
