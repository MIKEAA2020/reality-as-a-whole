"""Exact controls for a joint causal-component / energy-flow proposal.

Oscillators are not subjects. The code does not establish valence, incidence,
phenomenal identity, actual cosmology, or a preferred universal time.
"""
from fractions import Fraction as F
import unittest


EDGES=((0,1),(1,2))


def energy(q,p,edges=EDGES):
    return sum((x*x+y*y)/2 for x,y in zip(q,p)) + sum((q[i]-q[j])**2/2 for i,j in edges)


def acceleration(q,edges=EDGES):
    force=[-x for x in q]
    for i,j in edges:
        force[i] -= q[i]-q[j]
        force[j] -= q[j]-q[i]
    return force


def local_rates(q,p,edges=EDGES):
    # Symmetric division of each spring's interaction energy between endpoints.
    out=[F(0) for _ in q]
    for i,j in edges:
        flow=(q[j]-q[i])*(p[i]+p[j])/2
        out[i]+=flow
        out[j]-=flow
    return out


def flux_to(q,p,subsystem,edges=EDGES):
    included=set(subsystem)
    total=F(0)
    for i,j in edges:
        flow=(q[j]-q[i])*(p[i]+p[j])/2 # into i from j
        if i in included and j not in included: total+=flow
        elif j in included and i not in included: total-=flow
    return total


def scc(n,edges):
    # Structural Hamiltonian influence graph: p_i -> q_i, q_i -> p_i,
    # plus q_i -> p_j and q_j -> p_i for each coupling edge.
    graph={i:set() for i in range(2*n)}
    for i in range(n):
        graph[n+i].add(i)
        graph[i].add(n+i)
    for i,j in edges:
        graph[i].add(n+j)
        graph[j].add(n+i)
    def reachable(start):
        seen={start}; todo=[start]
        while todo:
            for v in graph[todo.pop()]-seen:
                seen.add(v); todo.append(v)
        return seen
    reach={i:reachable(i) for i in graph}
    remaining=set(graph); result=[]
    while remaining:
        v=min(remaining)
        comp={u for u in remaining if u in reach[v] and v in reach[u]}
        result.append(frozenset(comp)); remaining-=comp
    return result


class JointSubjectEnergyCandidateTests(unittest.TestCase):
    def setUp(self):
        self.q=list(map(F,(1,0,-1)))
        self.p=list(map(F,(1,-1,0)))

    def test_positive_total_energy_and_exact_conservation(self):
        self.assertEqual(energy(self.q,self.p),3)
        a=acceleration(self.q)
        derivative=sum(q*p+p*dp for q,p,dp in zip(self.q,self.p,a))
        derivative+=sum((self.q[i]-self.q[j])*(self.p[i]-self.p[j]) for i,j in EDGES)
        self.assertEqual(derivative,0)
        self.assertEqual(sum(local_rates(self.q,self.p)),0)

    def test_local_rates_and_subject_environment_boundary_flux(self):
        rates=local_rates(self.q,self.p)
        self.assertEqual(rates,[0,F(1,2),F(-1,2)])
        # Test subsets without claiming oscillator nodes are subjects.
        for subset in ((0,),(1,),(0,1),(0,2),(0,1,2),()):
            self.assertEqual(sum(rates[i] for i in subset),flux_to(self.q,self.p,subset))
        self.assertEqual(sum(rates[i] for i in (0,1)),F(1,2))

    def test_actual_incidence_weights_cannot_be_silently_dropped(self):
        rates=local_rates(self.q,self.p)
        masses=list(map(F,(1,2,3)))
        v=[rate/mass for rate,mass in zip(rates,masses)]
        self.assertEqual(sum(m*x for m,x in zip(masses,v)),0)
        self.assertNotEqual(sum(v),0)
        # Weights as mass are a proposed identity, not evidence of subjects.

    def test_reciprocal_connected_hamiltonian_graph_is_one_component(self):
        components=scc(3,EDGES)
        self.assertEqual(components,[frozenset(range(6))])
        self.assertEqual(scc(3,((0,1),)),[frozenset((0,1,3,4)),frozenset((2,5))])

    def test_canonical_normal_modes_change_raw_scc_count(self):
        # K for V=(sum q_i² + (q0−q1)² + (q1−q2)²)/2.
        K=((2,-1,0),(-1,3,-1),(0,-1,2))
        modes=((1,1,1),(1,0,-1),(1,-2,1))
        eigenvalues=(1,2,4)
        for v,lam in zip(modes,eigenvalues):
            self.assertEqual(tuple(sum(K[i][j]*v[j] for j in range(3)) for i in range(3)),
                             tuple(lam*x for x in v))
        for i in range(3):
            for j in range(i):
                self.assertEqual(sum(x*y for x,y in zip(modes[i],modes[j])),0)
        # Normalizing these orthogonal vectors yields a canonical orthogonal
        # transformation Q=O^T q, P=O^T p. H is then three uncoupled modes.
        self.assertEqual(len(scc(3,EDGES)),1)
        self.assertEqual(len(scc(3,())),3)

    def test_equal_split_is_not_unique_subsystem_energy_accounting(self):
        # Edge 0-1 has dU/dt=2, and onsite dE0/dt=-1.
        # E0^theta=onsite+theta*U, so dE0^theta/dt=-1+2 theta.
        # Direct derivative: d onsite0 = q0*p0+p0*acceleration0.
        a=acceleration(self.q)
        onsite_rate=self.q[0]*self.p[0]+self.p[0]*a[0]
        interaction_rate=(self.q[0]-self.q[1])*(self.p[0]-self.p[1])
        self.assertEqual(onsite_rate,-1)
        self.assertEqual(interaction_rate,2)
        self.assertEqual([onsite_rate+theta*interaction_rate
                          for theta in (F(0),F(1,2),F(1))],[-1,0,1])
        self.assertEqual(local_rates(self.q,self.p)[0],0)

    def test_single_scc_subject_has_zero_instantaneous_net_energy_gain(self):
        components=scc(3,EDGES)
        rates=local_rates(self.q,self.p)
        physical_nodes={v for v in components[0] if v<3}
        self.assertEqual(sum(rates[i] for i in physical_nodes),0)
        self.assertTrue(any(x for x in rates))

    def test_local_time_scale_does_not_identify_experiential_scale(self):
        q=local_rates(self.q,self.p)
        weights=[F(1),F(1),F(1)]
        for kappa in (F(1),F(2),F(-1)):
            felt=[kappa*x for x in q]
            self.assertEqual(sum(w*v for w,v in zip(weights,felt)),0)
        # This only shows algebraic underdetermination, not possible worlds.


if __name__ == '__main__': unittest.main()
