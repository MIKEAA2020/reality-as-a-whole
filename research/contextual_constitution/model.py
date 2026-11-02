"""Context-extension tests, not a phenomenal identity or subject detector.

State variables, interventions, readouts and putative phenomenal targets are
supplied. In particular, 'phenomenal target' is a model interpretation, not a
measurement or a declaration that this automaton experiences anything.
"""
from itertools import product, combinations

STATES = tuple(product(range(4), range(2), range(2), range(2)))
# content q, affect-context v, report setting r, hidden memory z
ACTIONS = ('hold', 'plus', 'minus', 'flip_v', 'flip_r', 'flip_z')


def step(state, action, *, feedback=False):
    q, v, r, z = state
    if action not in ACTIONS:
        raise ValueError('Unknown intervention')
    if action == 'plus':
        q = (q + 1) % 4
    elif action == 'minus':
        q = (q - 1) % 4
    elif action == 'flip_v':
        v = 1-v
    elif action == 'flip_r':
        r = 1-r
    elif action == 'flip_z':
        z = 1-z
    if feedback and action == 'hold':
        q = (q + v) % 4
    return q, v, r, z


def content(state):
    return state[0]


def rich_target(state):
    """Synthetic affect-sensitive phenomenal interpretation H_QV."""
    return state[0], state[1]


def thin_target(state):
    """Alternative H_Q: content-only phenomenal interpretation."""
    return state[0]


def physical_reports(state):
    """Same physical readouts under either interpretation.

    The second component can be an affect report, representation, or label.
    Merely observing it does not decide whether v is itself experienced.
    """
    return state[0], state[1], state[2]


def project(state, indices):
    return tuple(state[i] for i in indices)


def factorization_witnesses(states, projection, target):
    """Pairs proving target does not factor through a proposed description.

    No assumption that the target is really phenomenal is checked here.
    """
    by_projection = {}
    witnesses = []
    for state in states:
        key = projection(state)
        for other in by_projection.get(key, []):
            if target(other) != target(state):
                witnesses.append((other, state))
        by_projection.setdefault(key, []).append(state)
    return tuple(witnesses)


def target_factors(states, projection, target):
    return not factorization_witnesses(states, projection, target)


def coordinate_subsets(n=4):
    return tuple(tuple(c) for k in range(n+1) for c in combinations(range(n), k))


def minimal_sufficient_supports(states, target):
    """Inclusion-minimal state-coordinate supports; not subject boundaries."""
    accepted = []
    for indices in coordinate_subsets(len(states[0])):
        if any(set(old).issubset(indices) for old in accepted):
            continue
        if target_factors(states, lambda s: project(s, indices), target):
            accepted.append(indices)
    return tuple(accepted)


def partition_code(values):
    names, code = {}, []
    for value in values:
        if value not in names:
            names[value] = len(names)
        code.append(names[value])
    return tuple(code)


def target_partition(states, actions, target, transition, horizon=None):
    """Conditional future-target congruence via exact partition refinement.

    The target is supplied: this is NOT a derivation of a phenomenal readout.
    With horizon=0 only current distinctions count. None means all finite words.
    """
    states = tuple(states)
    if not states or not actions:
        raise ValueError('Nonempty state and intervention families required')
    index = {s:i for i,s in enumerate(states)}
    code = partition_code(target(s) for s in states)
    history = [code]
    depth = 0
    while horizon is None or depth < horizon:
        refined = partition_code((code[i],tuple(code[index[transition(s,a)]] for a in actions))
                                 for i,s in enumerate(states))
        if refined == code:
            return code, tuple(history)
        code = refined
        history.append(code)
        depth += 1
    return code, tuple(history)


def history(state, word, target=physical_reports, *, feedback=False):
    output = [target(state)]
    for a in word:
        state = step(state,a,feedback=feedback)
        output.append(target(state))
    return tuple(output)


def realized_profiles(initial_states, target):
    """A list of supplied actual occurrence witnesses, not a state population.

    Entries stay distinct even if target profiles agree. No self-location weights.
    """
    return tuple((i, target(s)) for i,s in enumerate(initial_states))


def satisfies_current_data(target, data):
    """Data are explicit candidate experiential constraints, not assumed reports."""
    return all((target(a) != target(b)) == different for a,b,different in data)
