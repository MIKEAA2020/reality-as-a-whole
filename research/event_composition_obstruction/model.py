"""Graph obstruction for an actual-event strong-connectivity composition rule.
No consciousness labels or empirical targets are supplied.
"""
SOURCE=('x','y')
ALL=('x','y','u','v')


def dependency_edges(include_monitor=False):
    edges={('y','x'),('x','y'),('y','y')}
    if include_monitor:edges|={('y','u'),('x','v'),('y','v')}
    return edges


def type_graph(include_monitor=False):
    nodes=set(ALL if include_monitor else SOURCE)
    return nodes,dependency_edges(include_monitor)


def event_graph(steps,include_monitor=False,active=None):
    if not isinstance(steps,int) or steps<1:raise ValueError('Positive integer number of transitions required')
    if active is None:active=set(range(steps))
    if any(not isinstance(t,int) or not 0<=t<steps for t in active):raise ValueError('Invalid active time')
    labels=ALL if include_monitor else SOURCE
    nodes={(t,label) for t in range(steps+1) for label in labels}
    edges=set()
    for t in range(steps):
        if t in active:
            edges|={((t,a),(t+1,b)) for a,b in dependency_edges(include_monitor)}
        else:
            edges|={((t,a),(t+1,a)) for a in labels}
    return nodes,edges


def reachable(nodes,edges,start):
    if start not in nodes:raise ValueError('Unknown node')
    adjacent={v:set() for v in nodes}
    for a,b in edges:
        if a not in nodes or b not in nodes:raise ValueError('Edge outside vertex set')
        adjacent[a].add(b)
    seen={start};pending=[start]
    while pending:
        for b in adjacent[pending.pop()]:
            if b not in seen:seen.add(b);pending.append(b)
    return seen


def strong_components(nodes,edges):
    reach={v:reachable(nodes,edges,v) for v in nodes};unused=set(nodes);parts=[]
    while unused:
        v=next(iter(unused));part={u for u in unused if u in reach[v] and v in reach[u]};parts.append(frozenset(part));unused-=part
    return frozenset(parts)


def weak_components(nodes,edges):return strong_components(nodes,edges|{(b,a) for a,b in edges})


def quotient(nodes,edges,projection):
    mapping={v:projection(v) for v in nodes}
    return set(mapping.values()),{(mapping[a],mapping[b]) for a,b in edges}


def all_forward(edges):return all(a[0]<b[0] for a,b in edges)


def support_graph(epsilon):
    if not 0<=epsilon<=1:raise ValueError('Probability in [0,1] required')
    return (set(SOURCE),dependency_edges() if epsilon else {('x','x'),('y','y')})


def no_update_probability(epsilon,steps):
    if not 0<=epsilon<=1 or not isinstance(steps,int) or steps<0:raise ValueError('Valid probability and horizon required')
    return (1-epsilon)**steps
