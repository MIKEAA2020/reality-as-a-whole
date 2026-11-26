"""Bounded evidence-driven concept revision; not a consciousness test.

Two separate contexts contain binary concepts over a one-bit input. State is
only a tuple of four-bit candidate masks. Incoming (context, input, label)
filters a mask; the selected concept is its least-numbered surviving member.
No label sequence is retained and an empty mask signals inconsistent evidence.
Run: python -m unittest verification.zero_version_space_revision_test -v
"""
from itertools import product
import unittest


ALL = 0b1111


def prediction(hypothesis, x):
    if hypothesis not in range(4) or x not in (0, 1):
        raise ValueError("invalid hypothesis or input")
    return (hypothesis >> x) & 1


def candidates(mask):
    if mask not in range(16):
        raise ValueError("invalid mask")
    return tuple(h for h in range(4) if mask & (1 << h))


def select(mask):
    possible = candidates(mask)
    return possible[0] if possible else None


def observe(state, context, x, label):
    """Deterministically evaluate all current candidates against evidence."""
    if len(state) != 2 or context not in range(2) or x not in (0, 1) or label not in (0, 1):
        raise ValueError("invalid observation")
    candidates(state[0]); candidates(state[1])
    keep = sum(1 << h for h in range(4) if prediction(h, x) == label)
    result = list(state)
    result[context] &= keep
    return tuple(result)


def run(observations):
    state = (ALL, ALL)
    for context, x, y in observations:
        state = observe(state, context, x, y)
    return state


class VersionSpaceRevisionTests(unittest.TestCase):
    def test_exact_retention_under_every_realizable_short_stream(self):
        # All pairs of true functions; every context/input schedule of length
        # up to 5. The environment supplies only observations, not the rule.
        pairs = tuple(product(range(2), repeat=2))
        runs = 0
        for truth in product(range(4), repeat=2):
            for length in range(6):
                for schedule in product(pairs, repeat=length):
                    state = (ALL, ALL)
                    evidence = [[], []]
                    for context, x in schedule:
                        label = prediction(truth[context], x)
                        previous = state
                        state = observe(state, context, x, label)
                        evidence[context].append((x, label))
                        self.assertEqual(state[1-context], previous[1-context])
                        for c in range(2):
                            expected = tuple(h for h in range(4) if all(
                                prediction(h, old_x) == old_y
                                for old_x, old_y in evidence[c]))
                            self.assertEqual(candidates(state[c]), expected)
                            self.assertIn(truth[c], expected)
                            chosen = select(state[c])
                            self.assertIsNotNone(chosen)
                            self.assertTrue(all(prediction(chosen, old_x) == old_y
                                                for old_x, old_y in evidence[c]))
                    runs += 1
        self.assertEqual(runs, 21840)

    def test_updates_can_change_selected_rules_without_supplying_a_rule(self):
        state = (ALL, ALL)
        self.assertEqual(select(state[0]), 0)
        state = observe(state, 0, 0, 1)
        self.assertEqual(candidates(state[0]), (1, 3))
        self.assertEqual(select(state[0]), 1)
        state = observe(state, 0, 1, 1)
        self.assertEqual(candidates(state[0]), (3,))
        self.assertEqual(select(state[0]), 3)
        self.assertEqual(state[1], ALL)

    def test_complete_consistent_coverage_identifies_true_rules(self):
        for h0, h1 in product(range(4), repeat=2):
            obs = [(c, x, prediction((h0, h1)[c], x))
                   for c, x in product(range(2), repeat=2)]
            state = run(obs)
            self.assertEqual(candidates(state[0]), (h0,))
            self.assertEqual(candidates(state[1]), (h1,))

    def test_equal_time_equal_last_input_same_state_but_different_history(self):
        a = ((0, 0, 0), (0, 1, 0), (0, 0, 0))
        b = ((0, 1, 0), (0, 0, 0), (0, 0, 0))
        self.assertNotEqual(a, b)
        self.assertEqual(a[-1], b[-1])
        self.assertEqual(run(a), run(b))
        self.assertEqual(run(a), (1, ALL))

    def test_no_inverse_for_known_observation(self):
        initial = (ALL, ALL)
        partial = observe(initial, 0, 0, 0)
        self.assertNotEqual(initial, partial)
        self.assertEqual(observe(initial, 0, 0, 0),
                         observe(partial, 0, 0, 0))

    def test_exact_history_cost_even_when_all_evidence_is_true(self):
        # True rule 0 always gives label 0. Fix final x=0 and require at
        # least one x=1 in the prefix. Every such history identifies rule 0.
        for t in range(3, 10):
            histories = [prefix + (0,) for prefix in product((0, 1), repeat=t-1)
                         if 1 in prefix]
            finals = {run(tuple((0, x, 0) for x in xs)) for xs in histories}
            self.assertEqual(finals, {(1, ALL)})
            self.assertEqual(len(histories), 2**(t-1)-1)
            # Since count > 2^(t-2), a lossless deterministic decoder
            # requires at least t-1 extra bits without an external log.
            self.assertGreater(len(histories), 2**(t-2))

    def test_contradictory_evidence_empties_set_not_auto_recovery(self):
        state = observe((ALL, ALL), 0, 0, 0)
        state = observe(state, 0, 0, 1)
        self.assertEqual(state, (0, ALL))
        self.assertIsNone(select(state[0]))
        self.assertEqual(observe(state, 0, 1, 0)[0], 0)
        self.assertEqual(state[1], ALL)

    def test_wrong_label_can_persist_under_finite_realizable_evidence(self):
        # A misleading first example compatible with some wrong function is
        # not known to be wrong until contradictory evidence appears.
        state = observe((ALL, ALL), 0, 0, 1)
        self.assertTrue(all(prediction(h, 0) == 1 for h in candidates(state[0])))
        self.assertNotIn(0, candidates(state[0]))  # true function could be 0
        self.assertEqual(select(state[0]), 1)

    def test_invalid_input(self):
        for obs in ((2, 0, 0), (0, 2, 0), (0, 0, 2)):
            with self.assertRaises(ValueError):
                observe((ALL, ALL), *obs)
        with self.assertRaises(ValueError):
            candidates(16)


if __name__ == "__main__":
    unittest.main()
