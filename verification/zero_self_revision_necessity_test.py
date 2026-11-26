"""Finite engineering controls for Lotfabadi's self-revision necessity claim.

The finite table is a deliberately narrow learner, not a model of minds or an
implementation of the paper's full seven-invariant architecture.
Run: python -m unittest verification.zero_self_revision_necessity_test -v
"""
from itertools import product
import unittest


def revise(state, command):
    """Replace one binary classification, leaving all other entries alone."""
    index, value = command
    if not 0 <= index < len(state) or value not in (0, 1):
        raise ValueError("invalid command")
    result = list(state)
    result[index] = value
    return tuple(result)


def run(initial, commands):
    state = initial
    for command in commands:
        state = revise(state, command)
    return state


class SelfRevisionNecessityTests(unittest.TestCase):
    def test_exhaustive_narrow_stability(self):
        # A guarantee for any command sequence up to length four and any
        # initial three-bit table, not an empirical estimate of reliability.
        commands = tuple(product(range(3), (0, 1)))
        runs = 0
        for initial in product((0, 1), repeat=3):
            for length in range(5):
                for sequence in product(commands, repeat=length):
                    state = initial
                    expected = list(initial)
                    for index, value in sequence:
                        before = state
                        state = revise(state, (index, value))
                        expected[index] = value
                        self.assertEqual(state[index], value)
                        for j in range(3):
                            if j != index:
                                self.assertEqual(state[j], before[j])
                        self.assertEqual(state, tuple(expected))
                    runs += 1
        self.assertEqual(runs, 12440)

    def test_genuine_replacement_with_current_not_historical_state(self):
        initial = (0, 1, 0)
        revised = revise(initial, (0, 1))
        self.assertEqual(revised, (1, 1, 0))
        self.assertNotEqual(revised[0], initial[0])
        self.assertEqual(revised[1:], initial[1:])
        # Both distinct old tables map to the same post-state under the same
        # known command: no inverse reconstructs both from post-state alone.
        self.assertEqual(revise((0, 1, 0), (0, 1)),
                         revise((1, 1, 0), (0, 1)))

    def test_equal_length_different_histories_same_current_and_last_input(self):
        initial = (0, 0, 0)
        a = ((0, 1), (0, 0), (0, 1))
        b = ((0, 0), (0, 1), (0, 1))
        self.assertEqual(a[-1], b[-1])
        self.assertNotEqual(a, b)
        self.assertEqual(run(initial, a), run(initial, b))
        self.assertEqual(run(initial, a), (1, 0, 0))
        # Even a clock reading and the most recent input do not distinguish
        # these histories. No external input log is included in this model.

    def test_exact_history_requires_growing_information_in_this_family(self):
        # Known initial state, known time horizon, index, and final input.
        # Among T binary inputs whose last value is 1, all have the same
        # final table but distinct full input histories.
        for t in range(1, 9):
            inputs = [prefix + (1,) for prefix in product((0, 1), repeat=t-1)]
            finals = {run((0, 0, 0), tuple((0, v) for v in h)) for h in inputs}
            self.assertEqual(finals, {(1, 0, 0)})
            self.assertEqual(len(inputs), 2 ** (t-1))
            # At least t-1 binary metadata bits are needed for a deterministic
            # decoder to distinguish all these histories, absent external logs.
            for k in range(t-1):
                self.assertLess(2**k, len(inputs))

    def test_identity_is_separate_from_the_transition_theorem(self):
        # Logical model check only: S -> M and M -> C entail S -> C;
        # S -> M alone does not. It makes no assertion about actual qualia.
        rows = list(product((False, True), repeat=3))
        implies = lambda a, b: (not a) or b
        for stable, modeled, conscious in rows:
            if implies(stable, modeled) and implies(modeled, conscious):
                self.assertTrue(implies(stable, conscious))
        witness = (True, True, False)
        self.assertTrue(implies(witness[0], witness[1]))
        self.assertFalse(implies(witness[0], witness[2]))
        # A truth-table valuation is not evidence of a possible physical world.

    def test_invalid_commands_rejected(self):
        for command in [(-1, 1), (3, 1), (0, 2)]:
            with self.assertRaises(ValueError):
                revise((0, 0, 0), command)


if __name__ == "__main__":
    unittest.main()
