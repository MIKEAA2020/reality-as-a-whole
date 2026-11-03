"""Exact probability-set checks; no observations or consciousness assignments.

The theorem concerns a supplied binary target and hypothetical assay bounds.
It does not calibrate a real assay or validate a physical constitutive basis.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def interval(value):
    if len(value) != 2:
        raise ValueError("Two endpoints required")
    lo, hi = map(F, value)
    if not F(0) <= lo <= hi <= F(1):
        raise ValueError("Ordered probability bounds in [0,1] required")
    return lo, hi


def observable(theta, sensitivity, false_positive):
    theta, sensitivity, false_positive = map(F, (theta, sensitivity, false_positive))
    for value in (theta, sensitivity, false_positive):
        interval((value, value))
    return false_positive + (sensitivity - false_positive) * theta


def project(theta_bounds, sensitivity_bounds, false_positive_bounds):
    bounds = tuple(map(interval, (theta_bounds, sensitivity_bounds, false_positive_bounds)))
    values = [observable(*corner) for corner in product(*bounds)]
    return min(values), max(values)


def intersects(left, right):
    left, right = interval(left), interval(right)
    return max(left[0], right[0]) <= min(left[1], right[1])


def compatible(evidence, candidates):
    return [name for name, predicted in candidates.items() if intersects(evidence, predicted)]


def text(bounds):
    return [str(v) for v in bounds]


def run_checks():
    grid = tuple(F(i, 10) for i in range(11))
    for q in grid:
        assert observable(1, q, 0) == q
        assert observable(0, 1, q) == q

    deterministic_count = 0
    for alpha, beta in product(grid, repeat=2):
        maintenance = project((1, 1), (1-beta, 1), (0, alpha))
        distribution = project((0, 0), (1-beta, 1), (0, alpha))
        assert maintenance == (1-beta, F(1))
        assert distribution == (F(0), alpha)
        assert (not intersects(maintenance, distribution)) == (alpha+beta < 1)
        deterministic_count += 1

    boxes = (
        ((F(4,5), 1), (F(4,5), 1), (0, F(1,5))),
        ((0, F(1,5)), (F(4,5), 1), (0, F(1,5))),
        ((F(1,4), F(3,4)), (F(1,5), F(3,5)), (F(2,5), F(4,5))),
    )
    box_rows = []
    interior_count = 0
    for theta, sensitivity, false_positive in boxes:
        projected = project(theta, sensitivity, false_positive)
        points = tuple((F(a), (F(a)+F(b))/2, F(b)) for a,b in (theta, sensitivity, false_positive))
        for point in product(*points):
            q = observable(*point)
            assert projected[0] <= q <= projected[1]
            interior_count += 1
        # Where fU <= sL, the monotone formula is independently checked.
        if false_positive[1] <= sensitivity[0]:
            assert projected == (
                observable(theta[0], sensitivity[0], false_positive[0]),
                observable(theta[1], sensitivity[1], false_positive[1]),
            )
        box_rows.append({
            "target_probability": text(theta),
            "sensitivity": text(sensitivity),
            "false_positive": text(false_positive),
            "projected_observation_probability": text(projected),
        })

    separated = {"H_M1": (F(4,5), F(1)), "H_D1": (F(0), F(1,5))}
    assert compatible((0, 1), separated) == ["H_M1", "H_D1"]
    assert compatible((F(9,10), 1), separated) == ["H_M1"]
    assert compatible((0, F(1,10)), separated) == ["H_D1"]
    assert compatible((F(2,5), F(3,5)), separated) == []
    assert intersects((F(1,2), 1), (0, F(3,5)))
    assert intersects((F(1,2), 1), (0, F(1,2)))  # endpoints touch

    invalid_count = 0
    for bad in ((-1, 0), (0, 2), (1, 0), (0, 1, 1)):
        try:
            interval(bad)
        except ValueError:
            invalid_count += 1
        else:
            raise AssertionError("Invalid bounds accepted")

    return {
        "status": "passed",
        "scope": "exact rational observation-set projection only",
        "unrestricted_q_grid_cases": len(grid),
        "deterministic_error_bound_pairs": deterministic_count,
        "deterministic_separation_criterion": "alpha + beta < 1",
        "interior_witness_checks": interior_count,
        "box_examples": box_rows,
        "invalid_intervals_rejected": invalid_count,
        "touching_endpoints_count_as_overlap": True,
        "sampling_model_assumed": False,
        "calibration_empirically_warranted": False,
        "physical_preservation_established": False,
        "consciousness_assignments": False,
        "rival_selected": None,
        "core_research_count_changed": False,
    }


if __name__ == "__main__":
    result = run_checks()
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print("PASS: exact observation identifiability checks; no empirical calibration or rival selected.")
