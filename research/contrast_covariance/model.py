"""Finite contrast-covariance model; no consciousness detector.

Graph structure, episode scope, allowed interventions, reporting boundary,
phenomenal constraints and occurrence anchors are explicit supplied inputs.
All probabilities below concern a report channel, not observer weighting.
"""
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations


@dataclass(frozen=True)
class ContrastGraph:
    vertices: tuple
    edges: frozenset  # unordered two-element frozensets

    def __post_init__(self):
        if not self.vertices or len(set(self.vertices)) != len(self.vertices):
            raise ValueError("Nonempty distinct vertices required")
        if any(len(e) != 2 or not e.issubset(self.vertices) for e in self.edges):
            raise ValueError("Invalid undirected edge")

    def adjacent(self, a, b):
        return frozenset((a, b)) in self.edges

    def distance(self, a, b):
        if a not in self.vertices or b not in self.vertices:
            raise ValueError("Unknown vertex")
        todo, seen = deque([(a, 0)]), {a}
        while todo:
            v, d = todo.popleft()
            if v == b:
                return d
            for w in self.vertices:
                if w not in seen and self.adjacent(v, w):
                    seen.add(w)
                    todo.append((w, d + 1))
        return None

    def renamed(self, mapping):
        if set(mapping) != set(self.vertices) or len(set(mapping.values())) != len(self.vertices):
            raise ValueError("Bijective rename required")
        return ContrastGraph(tuple(mapping[v] for v in self.vertices),
                             frozenset(frozenset(mapping[v] for v in e) for e in self.edges))


def cycle(labels):
    labels = tuple(labels)
    if len(labels) < 3:
        raise ValueError("At least three cycle vertices required")
    return ContrastGraph(labels, frozenset(frozenset((labels[i], labels[(i + 1) % len(labels)]))
                                         for i in range(len(labels))))


def admissible_maps(physical, phenomenal, anchors=()):
    """All bijective exact adjacency correspondences, with optional calibrations.

    The phenomenal graph is independently supplied SYNTHETIC data, not inferred
    by defining experience to mean a physical state. Anchors are bridge data.
    """
    anchors = tuple(anchors)
    if any(a not in physical.vertices or b not in phenomenal.vertices for a, b in anchors):
        raise ValueError("Anchor outside model")
    if len(physical.vertices) != len(phenomenal.vertices):
        return []
    result = []
    for values in permutations(phenomenal.vertices):
        f = dict(zip(physical.vertices, values))
        if not all(f[a] == b for a, b in anchors):
            continue
        if all(physical.adjacent(a, b) == phenomenal.adjacent(f[a], f[b])
               for a in physical.vertices for b in physical.vertices):
            result.append(f)
    return result


def report_distribution(content, noise, labels=(0, 1, 2, 3)):
    """With probability noise replace the report by uniform noise.

    A deliberately downstream, no-feedback channel. No claim is made that
    real neural noise always has this location or preserves phenomenology.
    """
    noise = Fraction(noise)
    if not 0 <= noise <= 1 or content not in labels:
        raise ValueError("Invalid channel")
    return {r: noise / len(labels) + (1 - noise if r == content else 0) for r in labels}


def total_variation(p, q):
    if set(p) != set(q):
        raise ValueError("Same alphabet required")
    return sum(abs(p[r] - q[r]) for r in p) / 2


def optimal_binary_accuracy(p, q):
    """Equal-prior decision accuracy; not a self-location prior."""
    return (1 + total_variation(p, q)) / 2


def content_step(content, action, modulus=4):
    if action not in (-1, 0, 1):
        raise ValueError("Unknown intervention")
    return (content + action) % modulus


def joint_step(state, action):
    """Content and a fixed report-noise setting, with no noise-to-content edge."""
    content, noise = state
    return content_step(content, action), noise


def feedback_step(state, action):
    """Countermodel: the putative nuisance feeds into content and is not removable."""
    content, switch = state
    return (content + action + switch) % 4, switch


def moving_readout(storage, time):
    return storage[(-time) % 3]


def ring_step(storage):
    return storage[1], storage[2], storage[0]


@dataclass(frozen=True)
class RoleCertificate:
    """Supplied occurrence witness for one role-segment, not a derived subject.

    anchors are concrete update-event blocks at a declared logical grain.
    Values, locations and descriptive layers are metadata, not extra tokens.
    'provenance' must be supplied/justified by the implementation account.
    """
    anchors: tuple
    values: tuple
    locations: tuple
    layer: str = "direct"

    def __post_init__(self):
        if not self.anchors or any(not block for block in self.anchors):
            raise ValueError("Nonempty active event blocks required")
        events = [e for block in self.anchors for e in block]
        if len(events) != len(set(events)):
            raise ValueError("Occurrence reused across blocks")
        if len(self.values) != len(self.anchors) + 1 or len(self.locations) != len(self.anchors):
            raise ValueError("Incorrect cut/event metadata")

    def transported(self, rename):
        if len({rename(e) for block in self.anchors for e in block}) != sum(map(len, self.anchors)):
            raise ValueError("Transport must not merge occurrences")
        return RoleCertificate(tuple(frozenset(rename(e) for e in b) for b in self.anchors),
                               self.values, self.locations, self.layer)


def occurrence_key(certificate, provenance=None):
    """No inference of consciousness. Only normalize supplied occurrence provenance."""
    if provenance is None:
        return certificate.anchors
    translated = tuple(frozenset(provenance[e] for e in block) for block in certificate.anchors)
    source_n = sum(map(len, certificate.anchors))
    if len(set(e for block in translated for e in block)) != source_n:
        raise ValueError("Provenance must be injective within a certificate")
    return translated


def occurrence_count(certificates):
    """Count supplied anchored role-segments in THIS list, not all realizations."""
    return len({occurrence_key(c) for c in certificates})


def shared_step(x, y, c):
    return (x + c) % 4, (y + c) % 4, c
