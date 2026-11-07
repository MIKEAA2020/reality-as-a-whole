"""Finite episode-support identifiability; NOT a subject or consciousness detector.

Vertices are supplied candidate content-OCCURRENCES unless explicitly mapped to
content types. Hyperedges are candidate episode supports. No edge is declared
phenomenal by constructing it. Temporal scope is supplied, not derived.
"""
from itertools import combinations


def subsets(items, *, nonempty=False):
    items = tuple(sorted(items))
    return tuple(frozenset(c) for n in range(1 if nonempty else 0, len(items)+1)
                 for c in combinations(items,n))


def validate(vertices, episodes):
    vertices, episodes = frozenset(vertices), frozenset(frozenset(e) for e in episodes)
    if not vertices or any(not e or not e.issubset(vertices) for e in episodes):
        raise ValueError('Nonempty vertex domain and nonempty valid supports required')
    return vertices, episodes


def joint_profile(vertices, episodes, arity):
    """All distinct-vertex sets of size <= arity lying in a candidate episode.

    This is a support-existence projection, not a measured report, probability,
    or a count of episodes. It intentionally forgets duplicate witnesses.
    """
    vertices,episodes=validate(vertices,episodes)
    if arity < 1:
        raise ValueError('Positive arity required')
    return frozenset(s for s in subsets(vertices,nonempty=True)
                     if len(s)<=arity and any(s.issubset(e) for e in episodes))


def covers(vertices, episodes):
    return frozenset().union(*episodes)==frozenset(vertices)


def antichain(episodes):
    episodes=frozenset(episodes)
    return not any(a<b for a in episodes for b in episodes)


def all_families(vertices, *, require_cover=True, maximal_only=False):
    options=subsets(vertices,nonempty=True)
    for mask in range(1<<len(options)):
        family=frozenset(e for i,e in enumerate(options) if mask & (1<<i))
        if require_cover and not covers(vertices,family):
            continue
        if maximal_only and not antichain(family):
            continue
        yield family


def compatible_families(vertices, observations, arity, *, maximal_only=False):
    return tuple(f for f in all_families(vertices,maximal_only=maximal_only)
                 if joint_profile(vertices,f,arity)==observations)


def maximal_supports(family):
    family=frozenset(family)
    return frozenset(a for a in family if not any(a<b for b in family))


def overlap_amalgamates(family):
    """Substantive optional closure law: intersecting supports have a joint union."""
    family=frozenset(family)
    return all(not (a & b) or any((a|b).issubset(c) for c in family)
               for a in family for b in family)


def amalgamation_closure(family):
    """Enforce rather than derive the optional law. No phenomenal authority."""
    family=frozenset(family)
    while True:
        expanded=family|frozenset(a|b for a in family for b in family if a & b)
        if expanded==family:
            return expanded
        family=expanded


def is_partition(vertices,family):
    return covers(vertices,family) and all(not(a&b) for a in family for b in family if a!=b)


def partitions(items):
    items=tuple(sorted(items))
    if not items:
        yield frozenset()
        return
    first,*rest=items
    for p in partitions(rest):
        yield p|{frozenset({first})}
        for block in p:
            yield (p-{block})|{block|{first}}


def rename(family,mapping):
    flat=set().union(*family)
    if not flat.issubset(mapping) or len({mapping[v] for v in flat})!=len(flat):
        raise ValueError('Passive rename must preserve distinct occurrences')
    return frozenset(frozenset(mapping[v] for v in e) for e in family)


def type_projection(family,type_of):
    """A lossy projection. It is not passive renaming or numerical identity."""
    return frozenset(frozenset(type_of[v] for v in e) for e in family)


def physical_joint_report(state):
    """A single joint output. Its existence makes no episode-membership claim."""
    return tuple(state)
