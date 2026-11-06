"""Exact finite checks supporting Zero_Residue_Chat_Audit_2.md.

These are toy-model calculations that test *formal* claims made in the
6 November 2026 DeepSeek chat ("Experience and non-optimal world"), not
experiments on consciousness and not proofs of a metaphysics.  They run on
Python 3 with the standard library only and write audit2_results.json.

Checks
------
A. Transcript statistics (words, turns, citation placeholders per response).
B. Leibniz modus tollens is valid; but under strict necessitarianism
   "best possible world" becomes vacuously true, so criterion C2 cannot be
   the modal-comparative claim used in the chat's first response.
C. In a one-world S5 frame, "possibly p" collapses to "p": the chat's
   "locally, structural coherence is not actual selection" must use a
   non-modal notion of coherence.
D. A joint functional F = f(integration, richness) that is merely monotone
   in both arguments does NOT fix which subsystems are selected: different
   monotone combinations, and different richness definitions, pick
   different subject boundaries and different numbers of local maxima.
   Hence "F is derived from unity-and-richness, so it is not a free
   parameter" is false as stated.
E. "Privation relative to the F-optimum" inherits that underdetermination:
   which subsystem is *more deprived* flips with the choice of f.
"""
from __future__ import annotations

import itertools
import json
import math
import re
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
TRANSCRIPT = HERE.parent / "uploads" / (
    "DeepSeek_Experience-and-non-optimal-world_20261106-2010.txt")

results: dict = {}


# ---------------------------------------------------------------------------
# A. Transcript statistics
# ---------------------------------------------------------------------------
def transcript_stats(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    words = len(text.split())
    prompts = sum(1 for ln in lines if ln.strip() == "you asked")
    responses = sum(1 for ln in lines if ln.strip() == "deepseek response")
    per_response: dict[int, int] = {}
    n = 0
    for ln in lines:
        if ln.strip() == "deepseek response":
            n += 1
        c = len(re.findall(r"\[reference:\d+\]", ln))
        if c:
            per_response[n] = per_response.get(n, 0) + c
    times = [ln.split("message time:")[1].strip()
             for ln in lines if ln.startswith("message time:")]
    return {
        "lines": len(lines),
        "words": words,
        "prompts": prompts,
        "responses": responses,
        "citation_placeholders_total": sum(per_response.values()),
        "citation_placeholders_by_response": per_response,
        "first_prompt_time": times[0] if times else None,
        "last_prompt_time": times[-1] if times else None,
    }


if TRANSCRIPT.exists():
    results["A_transcript"] = transcript_stats(TRANSCRIPT)
    assert results["A_transcript"]["prompts"] == 30
    assert results["A_transcript"]["responses"] == 30
else:  # pragma: no cover - transcript is shipped alongside this script
    results["A_transcript"] = {"error": f"missing {TRANSCRIPT}"}


# ---------------------------------------------------------------------------
# B. Leibniz, modus tollens, and vacuous optimality under necessitarianism
# ---------------------------------------------------------------------------
def modus_tollens_rows():
    rows = []
    for P, B in itertools.product([False, True], repeat=2):
        leibniz = (not P) or B          # P -> B
        if leibniz and not B:
            rows.append({"P": P, "B": B})
    return rows


mt_rows = modus_tollens_rows()
# Every valuation satisfying (P -> B) and not-B has not-P.
assert all(not r["P"] for r in mt_rows) and mt_rows


def is_best(actual, worlds, better):
    """actual is 'best' iff no world is strictly better than it."""
    return not any(better(w, actual) for w in worlds if w != actual)


# Three toy value orders over a three-world comparison class.
three_worlds = ["w_actual", "w1", "w2"]
value_orders = {
    "actual_lowest": {"w_actual": 0, "w1": 1, "w2": 2},
    "actual_middle": {"w_actual": 1, "w1": 0, "w2": 2},
    "actual_highest": {"w_actual": 2, "w1": 0, "w2": 1},
    "all_tied": {"w_actual": 1, "w1": 1, "w2": 1},
}
optimality_rows = []
for name, val in value_orders.items():
    better = lambda a, b, v=val: v[a] > v[b]
    optimality_rows.append({
        "value_order": name,
        "best_with_three_possible_worlds": is_best("w_actual", three_worlds, better),
        # Strict necessitarianism: the comparison class is the singleton.
        "best_with_one_possible_world": is_best("w_actual", ["w_actual"], better),
    })
assert all(r["best_with_one_possible_world"] for r in optimality_rows)
assert not all(r["best_with_three_possible_worlds"] for r in optimality_rows)
results["B_leibniz_and_necessitarianism"] = {
    "valuations_with_(P->B)_and_not_B": mt_rows,
    "modus_tollens_valid": True,
    "optimality_table": optimality_rows,
    "reading": (
        "If exactly one total world is possible, that world is trivially "
        "'best' under every value order, so an account with global modal "
        "collapse entails B vacuously and makes the first response's N "
        "('some possible world is better') false. C2 must therefore be an "
        "axiological claim (genuine privation exists; optimality is not an "
        "explanatory principle), not a modal-comparative one."),
}


# ---------------------------------------------------------------------------
# C. One-world S5: possibility collapses to actuality
# ---------------------------------------------------------------------------
def s5_collapse(n_worlds: int):
    """Count valuations where 'possibly p' holds but p fails at world 0."""
    bad = 0
    total = 0
    for vals in itertools.product([False, True], repeat=n_worlds):
        total += 1
        possible = any(vals)
        if possible and not vals[0]:
            bad += 1
    return {"worlds": n_worlds, "valuations": total,
            "possible_but_not_actual_at_w0": bad}


c_rows = [s5_collapse(1), s5_collapse(2), s5_collapse(3)]
assert c_rows[0]["possible_but_not_actual_at_w0"] == 0
assert c_rows[1]["possible_but_not_actual_at_w0"] > 0
results["C_one_world_modal_collapse"] = {
    "rows": c_rows,
    "reading": (
        "With a single possible world nothing is possible-but-unactual. The "
        "chat's 'locally, structural coherence != actual selection' is "
        "consistent only if 'coherence' means description-consistency, not "
        "metaphysical possibility - the consistency/possibility/actuality "
        "distinction already drawn in the first audit (section 4.3)."),
}


# ---------------------------------------------------------------------------
# D. Monotone functionals of (integration, richness) disagree about boundaries
# ---------------------------------------------------------------------------
def log2(x: float) -> float:
    return math.log(x, 2) if x > 0 else 0.0


def entropy(dist: dict) -> float:
    return -sum(p * log2(p) for p in dist.values() if p > 0)


def marginal(joint: dict, idx: tuple) -> dict:
    out: dict = {}
    for state, p in joint.items():
        key = tuple(state[i] for i in idx)
        out[key] = out.get(key, 0.0) + p
    return out


def mutual_information(joint: dict, a: tuple, b: tuple) -> float:
    return (entropy(marginal(joint, a)) + entropy(marginal(joint, b))
            - entropy(marginal(joint, a + b)))


def correlation(joint: dict, i: int, j: int) -> float:
    """Pearson correlation of spins taking values -1/+1."""
    m = marginal(joint, (i, j))
    ei = sum(p * s[0] for s, p in m.items())
    ej = sum(p * s[1] for s, p in m.items())
    eij = sum(p * s[0] * s[1] for s, p in m.items())
    vi = sum(p * s[0] ** 2 for s, p in m.items()) - ei ** 2
    vj = sum(p * s[1] ** 2 for s, p in m.items()) - ej ** 2
    if vi <= 0 or vj <= 0:
        return 0.0
    return (eij - ei * ej) / math.sqrt(vi * vj)


def integration(joint: dict, subset: tuple) -> float:
    """Minimum-information-bipartition proxy: min over bipartitions of MI.

    This is the classic 'weakest link' integration measure (in the spirit of
    early IIT), chosen because it is exactly computable here. It is not IIT
    4.0's phi; the point of the check does not depend on that choice.
    """
    best = None
    elems = list(subset)
    n = len(elems)
    for r in range(1, n // 2 + 1):
        for part in itertools.combinations(elems, r):
            rest = tuple(e for e in elems if e not in part)
            if r == n - r and part > rest:
                continue  # avoid double counting mirror bipartitions
            mi = mutual_information(joint, tuple(part), rest)
            best = mi if best is None else min(best, mi)
    return best if best is not None else 0.0


def richness_v1(joint: dict, subset: tuple) -> float:
    """Entropy plus summed absolute pairwise correlations."""
    h = entropy(marginal(joint, subset))
    c = sum(abs(correlation(joint, i, j))
            for i, j in itertools.combinations(subset, 2))
    return h + c


def richness_v2(joint: dict, subset: tuple) -> float:
    """Entropy per element plus mean absolute pairwise correlation."""
    h = entropy(marginal(joint, subset)) / len(subset)
    pairs = list(itertools.combinations(subset, 2))
    c = sum(abs(correlation(joint, i, j)) for i, j in pairs) / len(pairs)
    return h + c


def ising_block(nodes: tuple, couplings: dict, beta: float = 1.0) -> dict:
    """Boltzmann distribution over +/-1 spins with pairwise couplings."""
    states = list(itertools.product([-1, 1], repeat=len(nodes)))
    weights = []
    for s in states:
        e = 0.0
        for (i, j), J in couplings.items():
            e += J * s[nodes.index(i)] * s[nodes.index(j)]
        weights.append(math.exp(beta * e))
    z = sum(weights)
    return {s: w / z for s, w in zip(states, weights)}


def product_joint(blocks: list[tuple[tuple, dict]], n: int) -> dict:
    """Combine independent blocks into one joint over n spins."""
    joint: dict = {}
    for combo in itertools.product(*[list(d.items()) for _, d in blocks]):
        state = [0] * n
        p = 1.0
        for (nodes, _), (s, q) in zip(blocks, combo):
            for node, val in zip(nodes, s):
                state[node] = val
            p *= q
        joint[tuple(state)] = p
    return joint


# System: block A = tightly coupled pair {0,1}; block B = loosely coupled
# chain {2,3,4,5}. Blocks are independent, so any subset that straddles
# them has zero integration.
N = 6
block_a = ((0, 1), ising_block((0, 1), {(0, 1): 1.2}))
block_b = ((2, 3, 4, 5), ising_block((2, 3, 4, 5),
                                      {(2, 3): 0.35, (3, 4): 0.35, (4, 5): 0.35}))
JOINT = product_joint([block_a, block_b], N)
assert abs(sum(JOINT.values()) - 1.0) < 1e-12

candidates = [c for r in range(2, N + 1)
              for c in itertools.combinations(range(N), r)]
measures = {}
for c in candidates:
    # Round away floating-point noise (independent blocks give exactly zero
    # mutual information across the block boundary).
    measures[c] = {
        "phi": max(0.0, round(integration(JOINT, c), 10)),
        "R1": round(richness_v1(JOINT, c), 10),
        "R2": round(richness_v2(JOINT, c), 10),
    }

phi_max = max(m["phi"] for m in measures.values())
r1_max = max(m["R1"] for m in measures.values())
r2_max = max(m["R2"] for m in measures.values())

# All functionals below are strictly increasing in both arguments on the
# positive orthant (weakly where an argument is zero).
functionals = {
    "sum_R1": lambda phi, r1, r2: phi + r1,
    "product_R1": lambda phi, r1, r2: phi * r1,
    "phi_heavy_R1": lambda phi, r1, r2: phi + 0.1 * r1,
    "richness_heavy_R1": lambda phi, r1, r2: 0.1 * phi + r1,
    "normalized_min_R1": lambda phi, r1, r2: min(phi / phi_max, r1 / r1_max),
    "sum_R2": lambda phi, r1, r2: phi + r2,
    "product_R2": lambda phi, r1, r2: phi * r2,
    "lexicographic_phi_then_R1": lambda phi, r1, r2: (round(phi, 9), r1),
    # Integration as a necessary condition (gate), richness as the score
    # that is maximized among integrated candidates. Weakly monotone in phi.
    "gated_richness_R1": lambda phi, r1, r2: r1 if phi > 1e-9 else 0.0,
}


def pareto_front(points: dict) -> list:
    """Candidates not dominated in (phi, R1) by any other candidate."""
    front = []
    for c, (p, r) in points.items():
        dominated = any((p2 >= p and r2 >= r) and (p2 > p or r2 > r)
                        for c2, (p2, r2) in points.items() if c2 != c)
        if not dominated:
            front.append(c)
    return front


pareto = pareto_front({c: (m["phi"], m["R1"]) for c, m in measures.items()})
assert (0, 1) in pareto and (2, 3, 4, 5) in pareto and tuple(range(N)) in pareto

# No weighted sum w_phi*phi + w_R*R1 (w > 0) can select the quad {2,3,4,5}:
# beating the full set needs w_phi/w_R > (R1_full - R1_quad)/phi_quad, while
# beating the pair needs w_phi/w_R < (R1_quad - R1_pair)/(phi_pair - phi_quad).
quad, pair, full = (2, 3, 4, 5), (0, 1), tuple(range(N))
lower = (measures[full]["R1"] - measures[quad]["R1"]) / measures[quad]["phi"]
upper = ((measures[quad]["R1"] - measures[pair]["R1"])
         / (measures[pair]["phi"] - measures[quad]["phi"]))
weighted_sum_can_pick_quad = lower < upper
assert not weighted_sum_can_pick_quad


def overlaps(a: tuple, b: tuple) -> bool:
    return bool(set(a) & set(b))


d_rows = {}
global_winners = set()
for name, f in functionals.items():
    scores = {c: f(m["phi"], m["R1"], m["R2"]) for c, m in measures.items()}
    winner = max(scores, key=lambda c: scores[c])
    # Local maxima in the exclusion sense: no overlapping candidate scores
    # strictly higher. (A global argmax is always one of them.)
    local_maxima = [c for c in candidates
                    if all(scores[o] <= scores[c] for o in candidates
                           if o != c and overlaps(o, c))]
    # Greedy exclusion: repeatedly take the best remaining non-overlapping
    # candidate - one way of turning F into a partition into "subjects".
    remaining = list(candidates)
    chosen = []
    while remaining:
        best = max(remaining, key=lambda c: scores[c])
        chosen.append(best)
        remaining = [c for c in remaining if not overlaps(c, best)]
    global_winners.add(winner)
    d_rows[name] = {
        "global_argmax": list(winner),
        "argmax_phi": round(measures[winner]["phi"], 4),
        "argmax_R1": round(measures[winner]["R1"], 4),
        "local_maxima_count": len(local_maxima),
        "local_maxima": [list(c) for c in local_maxima],
        "greedy_exclusion_partition": [list(c) for c in chosen],
        "subjects_under_greedy_exclusion": len(chosen),
    }

distinct_winners = sorted(list(w) for w in global_winners)
assert len(distinct_winners) >= 3, distinct_winners
subject_counts = {r["subjects_under_greedy_exclusion"] for r in d_rows.values()}
assert len(subject_counts) >= 2, subject_counts

results["D_functional_underdetermination"] = {
    "system": {
        "nodes": N,
        "block_A": {"nodes": [0, 1], "coupling": 1.2},
        "block_B": {"nodes": [2, 3, 4, 5], "chain_couplings": 0.35},
        "blocks_independent": True,
        "candidate_subsets": len(candidates),
    },
    "measures_of_key_subsets": {
        str(list(c)): {k: round(v, 4) for k, v in measures[c].items()}
        for c in [(0, 1), (2, 3), (2, 3, 4, 5), (0, 1, 2, 3, 4, 5), (3, 4)]
    },
    "functionals": d_rows,
    "distinct_global_winners": distinct_winners,
    "distinct_subject_counts_under_exclusion": sorted(subject_counts),
    "pareto_front_phi_R1": [list(c) for c in pareto],
    "weighted_sum_window_for_quad": {
        "needs_w_phi_over_w_R_greater_than": round(lower, 3),
        "and_less_than": round(upper, 3),
        "window_nonempty": weighted_sum_can_pick_quad,
    },
    "reading": (
        "Every functional is monotone in integration and in richness - the "
        "only content 'unity and richness' supply - yet they select different "
        "global boundaries, different numbers of exclusion-maxima, and "
        "different numbers of subjects. The additive functionals even select "
        "the full six-node set, whose integration is exactly zero because it "
        "straddles two independent blocks. The trade-off form, the richness "
        "definition, the maximization-versus-threshold choice and the "
        "exclusion rule are all free choices not fixed by phenomenology."),
}


# ---------------------------------------------------------------------------
# E. Privation relative to the F-optimum inherits the underdetermination
# ---------------------------------------------------------------------------
compare = [(0, 1), (2, 3, 4, 5), (3, 4)]
e_rows = {}
orderings = set()
for name in ["sum_R1", "product_R1", "phi_heavy_R1", "richness_heavy_R1"]:
    f = functionals[name]
    scores = {c: f(m["phi"], m["R1"], m["R2"]) for c, m in measures.items()}
    top = max(scores.values())
    deficits = {c: top - scores[c] for c in compare}
    order = sorted(compare, key=lambda c: deficits[c])
    orderings.add(tuple(order))
    e_rows[name] = {
        "deficit_from_optimum": {str(list(c)): round(deficits[c], 4)
                                 for c in compare},
        "least_to_most_deprived": [list(c) for c in order],
    }
assert len(orderings) >= 2, orderings
results["E_privation_inherits_underdetermination"] = {
    "rows": e_rows,
    "distinct_deprivation_orderings": len(orderings),
    "reading": (
        "'Evil as privation of the F-optimum' needs a determinate optimum and "
        "a determinate measure of distance from it. Both change with the "
        "free choices in F, so the privation account adds a reference-class "
        "choice on top of the residue it inherits from F."),
}

# ---------------------------------------------------------------------------
# Write results
# ---------------------------------------------------------------------------
out = HERE / "audit2_results.json"
out.write_text(json.dumps(results, indent=2), encoding="utf-8")

summary = {
    "transcript": {k: results["A_transcript"].get(k) for k in
                   ("words", "prompts", "responses",
                    "citation_placeholders_total")},
    "B_necessitarian_best_world_vacuous": all(
        r["best_with_one_possible_world"]
        for r in results["B_leibniz_and_necessitarianism"]["optimality_table"]),
    "C_one_world_possible_but_unactual": c_rows[0]["possible_but_not_actual_at_w0"],
    "D_distinct_global_winners": distinct_winners,
    "D_subject_counts": sorted(subject_counts),
    "E_distinct_privation_orderings": len(orderings),
}
print(json.dumps(summary, indent=2))
print("all assertions passed; results written to", out)
