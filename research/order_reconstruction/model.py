"""Coordinate-free finite order reconstruction, exact rational valuation checks.

Input is opaque node identifiers and a reflexive causal relation. Grid fixtures
are separate from reconstruction. Metric interpretation is conditional on a
null-rectangular realization, not inferred from finite order alone.
"""
from dataclasses import dataclass
from fractions import Fraction
from itertools import product


@dataclass
class Grid:
    nodes: tuple
    relation: frozenset
    chains: tuple
    coordinates: dict
    meet: dict
    join: dict

    @property
    def shape(self):
        return tuple(len(chain)+1 for chain in self.chains)


def grid_fixture(rows,columns,labels=None):
    """Generate test input plus truth; truth is NOT passed to reconstruct."""
    if rows<2 or columns<2:
        raise ValueError('Two nontrivial chains required')
    coords=tuple(product(range(rows),range(columns)))
    nodes=tuple(labels) if labels is not None else tuple(f'node-{k}' for k in range(len(coords)))
    if len(nodes)!=len(coords) or len(set(nodes))!=len(nodes):
        raise ValueError('Distinct labels matching fixture size required')
    truth=dict(zip(nodes,coords))
    rel=frozenset((x,y) for x in nodes for y in nodes if all(a<=b for a,b in zip(truth[x],truth[y])))
    return nodes,rel,truth


def reconstruct(nodes,relation):
    """Recognize exactly finite distributive lattices with J(P)=two chains."""
    nodes=tuple(nodes); rel=frozenset(relation)
    if not nodes or len(set(nodes))!=len(nodes):
        raise ValueError('Nonempty distinct node set required')
    allowed=set(nodes)
    if any(x not in allowed or y not in allowed for x,y in rel):
        raise ValueError('Relation refers to an unknown node')
    for x in nodes:
        if (x,x) not in rel:
            raise ValueError('Relation must be reflexive')
        for y in nodes:
            if x!=y and (x,y) in rel and (y,x) in rel:
                raise ValueError('Relation must be antisymmetric')
            for z in nodes:
                if (x,y) in rel and (y,z) in rel and (x,z) not in rel:
                    raise ValueError('Relation must be transitively closed')
    meet={}; join={}
    for x in nodes:
        for y in nodes:
            lower=[z for z in nodes if (z,x) in rel and (z,y) in rel]
            upper=[z for z in nodes if (x,z) in rel and (y,z) in rel]
            greatest=[z for z in lower if all((w,z) in rel for w in lower)]
            least=[z for z in upper if all((z,w) in rel for w in upper)]
            if len(greatest)!=1 or len(least)!=1:
                raise ValueError('Poset is not a lattice')
            meet[x,y]=greatest[0]; join[x,y]=least[0]
    for x,y,z in product(nodes,repeat=3):
        if meet[x,join[y,z]]!=join[meet[x,y],meet[x,z]] or join[x,meet[y,z]]!=meet[join[x,y],join[x,z]]:
            raise ValueError('Lattice is not distributive')
    irreducibles=[]
    for x in nodes:
        lower=[y for y in nodes if y!=x and (y,x) in rel]
        covers=[y for y in lower if not any(y!=z and (y,z) in rel for z in lower)]
        if len(covers)==1:
            irreducibles.append(x)
    remaining=set(irreducibles); chains=[]
    for first in irreducibles:
        if first not in remaining:
            continue
        component={first}; stack=[first]; remaining.remove(first)
        while stack:
            x=stack.pop()
            neighbours=[y for y in remaining if (x,y) in rel or (y,x) in rel]
            for y in neighbours:
                remaining.remove(y); component.add(y); stack.append(y)
        if any((x,y) not in rel and (y,x) not in rel for x in component for y in component):
            raise ValueError('Join-irreducible component is not a chain')
        chains.append(tuple(sorted(component,key=lambda x:sum((y,x) in rel for y in component))))
    if len(chains)!=2:
        raise ValueError('Join-irreducibles must have exactly two nonempty chain components')
    coords={x:tuple(sum((j,x) in rel for j in chain) for chain in chains) for x in nodes}
    expected=set(product(*(range(len(chain)+1) for chain in chains)))
    if set(coords.values())!=expected or len(set(coords.values()))!=len(nodes):
        raise ValueError('Coordinate reconstruction is not a bijection')
    if any(((x,y) in rel)!=all(a<=b for a,b in zip(coords[x],coords[y])) for x in nodes for y in nodes):
        raise ValueError('Coordinates do not preserve and reflect order')
    return Grid(nodes,rel,tuple(chains),coords,meet,join)


def interval_values(grid,weights):
    rows,cols=grid.shape
    if len(weights)!=rows-1 or any(len(row)!=cols-1 for row in weights):
        raise ValueError('One weight per elementary diamond required')
    return {(x,y):sum((Fraction(weights[i][j]) for i in range(grid.coordinates[x][0],grid.coordinates[y][0])
                       for j in range(grid.coordinates[x][1],grid.coordinates[y][1])),Fraction(0))
            for x,y in grid.relation}


def recover_weights(grid,values):
    if set(values)!=set(grid.relation):
        raise ValueError('A value for every causal interval, and no other interval, required')
    values={key:Fraction(value) for key,value in values.items()}
    inverse={coord:node for node,coord in grid.coordinates.items()}
    rows,cols=grid.shape
    weights=tuple(tuple(values[inverse[i,j],inverse[i+1,j+1]] for j in range(cols-1)) for i in range(rows-1))
    if any(value<=0 for row in weights for value in row):
        raise ValueError('Strictly positive elementary volume required')
    if interval_values(grid,weights)!=values:
        raise ValueError('Valuation is not null-zero rectangularly additive')
    return weights


def flat_widths(weights):
    """A flat null-grid realization exists iff the positive weight matrix has rank one."""
    weights=tuple(tuple(Fraction(x) for x in row) for row in weights)
    if not weights or not weights[0] or any(len(row)!=len(weights[0]) for row in weights) or any(x<=0 for row in weights for x in row):
        raise ValueError('Positive nonempty rectangular weight array required')
    pivot=weights[0][0]
    if any(weights[i][j]*pivot!=weights[i][0]*weights[0][j] for i in range(len(weights)) for j in range(len(weights[0]))):
        raise ValueError('No flat null-rectangular realization of these weights')
    du=tuple(row[0]/pivot for row in weights)
    dv=tuple(2*x for x in weights[0])
    return du,dv


def refine(weights,row_parts=2,column_parts=2):
    if not isinstance(row_parts,int) or not isinstance(column_parts,int) or row_parts<1 or column_parts<1:
        raise ValueError('Positive integer refinement factors required')
    return tuple(tuple(Fraction(weights[i//row_parts][j//column_parts],row_parts*column_parts)
                       for j in range(len(weights[0])*column_parts)) for i in range(len(weights)*row_parts))


def coarsen(weights,row_parts=2,column_parts=2):
    if (not isinstance(row_parts,int) or not isinstance(column_parts,int) or row_parts<1 or column_parts<1
            or not weights or not weights[0] or any(len(row)!=len(weights[0]) for row in weights)
            or len(weights)%row_parts or len(weights[0])%column_parts):
        raise ValueError('Compatible positive refinement factors and a rectangular array required')
    return tuple(tuple(sum((Fraction(weights[i+di][j+dj]) for di in range(row_parts) for dj in range(column_parts)),Fraction(0))
                       for j in range(0,len(weights[0]),column_parts)) for i in range(0,len(weights),row_parts))
