#!/usr/bin/env python3
"""Exact audit of a proposed conflict proxy, not a pain or consciousness model."""
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path


def gap(losses, weights):
    """Weighted optimum minus sum of separately attainable optima."""
    assert losses and len(losses) == len(weights)
    n_actions = len(losses[0])
    assert n_actions and all(len(row) == n_actions for row in losses)
    assert all(w >= 0 for w in weights) and sum(weights) == 1
    total = [sum(w * row[a] for w, row in zip(weights, losses))
             for a in range(n_actions)]
    separate = sum(w * min(row) for w, row in zip(weights, losses))
    return min(total) - separate, total


def text(x):
    return str(x)


def main():
    grid = (Q(0), Q(1, 2), Q(1))
    weights = (Q(1, 2), Q(1, 2))
    n = positive = 0
    for vals in product(grid, repeat=4):
        losses = (vals[:2], vals[2:])
        f, total = gap(losses, weights)
        assert f >= 0
        # Merging objectives preserves the aggregate loss for every action,
        # but erases this decomposition-dependent incompatibility metric.
        merged, total_merged = gap((total,), (Q(1),))
        assert total == total_merged and merged == 0
        positive += f > 0
        n += 1

    opposed, opposed_total = gap(((Q(0), Q(1)), (Q(1), Q(0))), weights)
    common, common_total = gap(((Q(0), Q(1)), (Q(0), Q(1))), weights)
    blocked, blocked_total = gap(((Q(1), Q(1)),), (Q(1),))
    merged_opposed, _ = gap((opposed_total,), (Q(1),))
    assert (opposed, common, blocked, merged_opposed) == (Q(1, 2), Q(0), Q(0), Q(0))
    result = {
        "status": "passed",
        "scope": "Exact finite control-proxy arithmetic only; no human data, experience, or validated pain marker.",
        "grid_cases": n,
        "positive_gap_cases": positive,
        "opposed_objectives": {"conflict_gap": text(opposed), "aggregate_loss": list(map(text, opposed_total))},
        "merged_same_aggregate": {"conflict_gap": text(merged_opposed), "aggregate_loss": list(map(text, opposed_total))},
        "aligned_objectives": {"conflict_gap": text(common), "aggregate_loss": list(map(text, common_total))},
        "one_fully_blocked_objective": {"conflict_gap": text(blocked), "aggregate_loss": list(map(text, blocked_total))},
    }
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
