"""Exact response geometry, NOT a law assigning consciousness to states."""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product
import math

@dataclass(frozen=True)
class Family:
    probabilities: dict
    derivatives: dict
    def __post_init__(self):
        object.__setattr__(self, "probabilities", {o: F(p) for o, p in self.probabilities.items()})
        object.__setattr__(self, "derivatives", {o: tuple(map(F, d)) for o, d in self.derivatives.items()})
        if not self.probabilities or self.probabilities.keys() != self.derivatives.keys():
            raise ValueError('Matching nonempty outcome domains required')
        if any(p < 0 for p in self.probabilities.values()) or sum(self.probabilities.values()) != 1:
            raise ValueError('Normalized nonnegative probabilities required')
        dims = {len(v) for v in self.derivatives.values()}
        if len(dims) != 1 or next(iter(dims)) == 0:
            raise ValueError('Fixed positive tangent dimension required')
        if any(sum(d[j] for d in self.derivatives.values()) != 0 for j in range(self.dimension)):
            raise ValueError('Probability derivatives must sum to zero')
        if any(p == 0 and any(self.derivatives[o]) for o, p in self.probabilities.items()):
            raise ValueError('Only fixed-support regular families supported')
    @property
    def dimension(self):
        return len(next(iter(self.derivatives.values())))


def packet(theta):
    """Two independent Bernoulli responses with interior propensity parameters."""
    if len(theta) != 2:
        raise ValueError('Two parameters required')
    x, y = map(F, theta)
    if not 0 < x < 1 or not 0 < y < 1:
        raise ValueError('Interior propensities required')
    p, d = {}, {}
    for a, b in product((0, 1), repeat=2):
        pa, pb = (x if a else 1-x), (y if b else 1-y)
        p[a, b] = pa*pb
        d[a, b] = ((1 if a else -1)*pb, pa*(1 if b else -1))
    return Family(p, d)


def fisher(family):
    n = family.dimension
    return tuple(tuple(sum((family.derivatives[o][i]*family.derivatives[o][j]/p
                            for o, p in family.probabilities.items() if p), F(0))
                       for j in range(n)) for i in range(n))


def pushforward(family, kernel):
    """Parameter-independent physical channel, NOT a state-coordinate change."""
    if kernel.keys() != family.probabilities.keys():
        raise ValueError('Kernel must cover input domain')
    if any(not row or any(w < 0 for w in row.values()) or sum(row.values()) != 1
           for row in kernel.values()):
        raise ValueError('Stochastic rows required')
    outcomes = {v for row in kernel.values() for v in row}
    p = {v: F(0) for v in outcomes}
    d = {v: [F(0)]*family.dimension for v in outcomes}
    for o, po in family.probabilities.items():
        for v, weight in kernel[o].items():
            p[v] += weight*po
            for j in range(family.dimension):
                d[v][j] += weight*family.derivatives[o][j]
    return Family(p, {v: tuple(dv) for v, dv in d.items()})


def deterministic_channel(family, function):
    return pushforward(family, {o: {function(o): F(1)} for o in family.probabilities})


def coordinate_pullback(family, jacobian):
    """d(old)/d(new). Only invertible square Jacobians are chart changes."""
    if len(jacobian) != family.dimension or not jacobian or not jacobian[0]:
        raise ValueError('Compatible nonempty Jacobian required')
    n = len(jacobian[0])
    if any(len(row) != n for row in jacobian):
        raise ValueError('Rectangular Jacobian required')
    return Family(dict(family.probabilities),
                  {o: tuple(sum(d[i]*jacobian[i][j] for i in range(family.dimension))
                            for j in range(n)) for o, d in family.derivatives.items()})


def matmul(a, b):
    return tuple(tuple(sum(x*y for x, y in zip(row, col)) for col in zip(*b)) for row in a)


def transpose(a):
    return tuple(zip(*a))


def quadratic(g, v):
    return sum(v[i]*g[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))


def difference(a, b):
    return tuple(tuple(x-y for x, y in zip(ar, br)) for ar, br in zip(a, b))


def psd_two(g):
    if len(g) != 2 or any(len(row) != 2 for row in g) or g[0][1] != g[1][0]:
        raise ValueError('Symmetric two-dimensional matrix required')
    return g[0][0] >= 0 and g[1][1] >= 0 and g[0][0]*g[1][1]-g[0][1]**2 >= 0


def noisy_monitor(family, error):
    error = F(error)
    if not 0 <= error <= 1:
        raise ValueError('Channel error must be a probability')
    return pushforward(family, {(a, b): {(a, b, a): 1-error, (a, b, 1-a): error}
                                for a, b in family.probabilities})


def independent_repetitions(family, count):
    """Genuine independent repetitions, not faithful copies."""
    if type(count) is not int or count < 1:
        raise ValueError('Positive integer count required')
    p, d = {}, {}
    for outcomes in product(family.probabilities, repeat=count):
        terms = [family.probabilities[o] for o in outcomes]
        p[outcomes] = math.prod(terms)
        d[outcomes] = tuple(sum(family.derivatives[outcomes[k]][j]
                               *math.prod(terms[:k]+terms[k+1:]) for k in range(count))
                            for j in range(family.dimension))
    return Family(p, d)


def angular_coordinates(theta):
    packet(theta)
    return tuple(2*math.asin(math.sqrt(float(t))) for t in theta)


def packet_distance(theta, other):
    u, v = angular_coordinates(theta), angular_coordinates(other)
    return math.sqrt(sum((a-b)**2 for a, b in zip(u, v)))
