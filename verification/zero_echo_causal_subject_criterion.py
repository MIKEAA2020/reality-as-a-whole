"""Causal-grain and subject-support controls on the reduced physical echo.

Each Boolean operation is the supported sign action of an existing gate.
The intervention graph and candidate supports are model choices, not subjects.
A copied J register is an isometric implementation, not a passive relabeling.
"""
from fractions import Fraction as F
from verification.zero_stationary_battery_bridge import OLD
from itertools import combinations,product

NAMES=('B','J','R','L','H')
# Save J; T-Q-T; comparison report. The two CNOTs writing H are explicit.
CIRCUIT=(('J','L'),('J','R'),('B','J'),('J','R'),('L','H'),('J','H'))
ENC_NAMES=('B','J1','J2','R','L','H')
ENC_CIRCUIT=(('J2','L'),('J1','R'),('B','J1'),('B','J2'),
             ('J1','R'),('L','H'),('J1','H'))
QUALITY_NAMES=NAMES+('M','K')
NOW_REPORT=CIRCUIT+(('M','K'),('J','K'))
ECHO_REPORT=NOW_REPORT+(('R','K'),)


def run(names,circuit,state):
    """Apply the listed reversible CNOTs to a dictionary of bits."""
    if set(state)!=set(names) or any(v not in (0,1) for v in state.values()):
        raise ValueError('invalid bit configuration')
    x=dict(state)
    for source,target in circuit:
        if source not in x or target not in x or source==target:raise ValueError('invalid gate')
        x[target]^=x[source]
    return x


def states(names):
    return (dict(zip(names,bits)) for bits in product((0,1),repeat=len(names)))


def influence(names,circuit):
    """Ordered pairs with a deterministic bit-flip intervention witness.

    At the chosen interval entrance only, vary one input holding the other
    bits fixed; include an edge iff some output bit changes. Self-edges omitted.
    This is a model channel test, not proof these clamps are physically local.
    """
    edges=set()
    for x in states(names):
        y=run(names,circuit,x)
        for a in names:
            xx=dict(x);xx[a]^=1
            yy=run(names,circuit,xx)
            edges.update((a,b) for b in names if a!=b and y[b]!=yy[b])
    return frozenset(edges)


def gate_support(circuit):
    return frozenset(frozenset((a,b)) for a,b in circuit)


def local_candidates(vertices,edge_weights):
    """Minimal nonempty S with total internal edge weight > boundary weight."""
    vertices=tuple(vertices);good=[]
    for k in range(1,len(vertices)+1):
        for c in combinations(vertices,k):
            s=frozenset(c)
            inside=sum(w for edge,w in edge_weights.items() if edge<=s)
            boundary=sum(w for edge,w in edge_weights.items() if len(edge&s)==1)
            if inside>boundary:good.append(s)
    return frozenset(s for s in good if not any(t<s for t in good))


def unit_graph(circuit):return {edge:F(1) for edge in gate_support(circuit)}


def quotient_graph(graph):
    """Coalesce both encoded J shares to J; deduplicate parallel relations.

    This presupposes identifying the code and its logical intervention. It
    does not mean physical subregions have become identical subjects.
    """
    def alias(v):return 'J' if v in ('J1','J2') else v
    edges={frozenset(alias(v) for v in edge) for edge in graph}
    return {edge:F(1) for edge in edges if len(edge)==2}


def encode(x):
    return {'B':x['B'],'J1':x['J'],'J2':x['J'],
            'R':x['R'],'L':x['L'],'H':x['H']}


def anchor_records():
    """Ready L/H and R, with the actual OLD seed and sign weights."""
    out=[]
    for (b,z),p in OLD.items():
        for s in (1,-1):
            row={'B':b,'J':b*z,'R':b,'L':z,'H':b,'M':s}
            out.append((row,p/2))
    return out


def target(row,kind):
    if kind=='B':return row['B']
    if kind=='now':return row['M']*row['J']
    if kind=='echo':return row['M']*row['J']*row['R']
    raise ValueError('unknown target')


def access_probability(fields,kind):
    """Bayes-optimal deterministic sign guess from a finite commuting record."""
    fields=tuple(fields);cells={}
    for row,p in anchor_records():
        key=tuple(row[f] for f in fields)
        values=cells.setdefault(key,{1:F(0),-1:F(0)})
        values[target(row,kind)]+=p
    return sum((max(v.values()) for v in cells.values()),F(0))


def minimal_access(kind):
    """All inclusion-minimal perfect classical-sign access sets."""
    names=NAMES+('M',);good=[]
    for n in range(len(names)+1):
        for c in combinations(names,n):
            s=frozenset(c)
            if access_probability(c,kind)==1 and not any(t<=s for t in good):
                good.append(s)
    return frozenset(good)


def subject_overlap(candidates,sites):
    return {site:sum(site in candidate for candidate in candidates) for site in sites}


def split_canonical(rates,candidates):
    """Equal-response allocation under stipulated complete local accounting."""
    m=subject_overlap(candidates,rates)
    if any(v==0 for v in m.values()):raise ValueError('uncovered site')
    return {s:sum((F(rates[i],m[i]) for i in s),F(0)) for s in candidates}
