"""Five-ray conservation -> POVM -> singlet steering -> opposite records/current.

Conditional logical-qubit construction; no subject or phenomenal identification.
"""
from fractions import Fraction as F
import cmath
import math
import unittest
from verification.zero_spin_constitution_test import X,Y,Z,add,eye,kron,mm,mv,scale,inner,close
from verification.zero_invariant_sphere_instrument_test import adj,instrument_unitary
from verification.zero_sphere_conservation_born_bridge_test import bridge,ray
from verification.zero_reciprocal_subject_exchange_test import (
    a as work_a,b as work_b,J,proj,exchange,g
)
from verification.zero_sharp_opposition_and_experiential_response_test import clock_expm


def sub(a,b): return add(a,scale(-1,b))
def pauli(n): return add(add(scale(n[0],X),scale(n[1],Y)),scale(n[2],Z))
def pure(n,sign=1): return scale(.5,add(eye(2),scale(sign,pauli(n))))
def outer(v): return [[x*y.conjugate() for y in v] for x in v]
def norm2(v): return inner(v,v).real
def plus(a,b): return [x+y for x,y in zip(a,b)]
def vecscale(a,v): return [a*x for x in v]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def total(mats):
    out=scale(0,mats[0])
    for m in mats: out=add(out,m)
    return out

q=[1/8,2/5,19/40]
ns=[(1,0,0),(.5,math.sqrt(3)/2,0),(-13/19,-8*math.sqrt(3)/19,0)]
axis=(-1/5,2*math.sqrt(3)/5,2*math.sqrt(3)/5)
psi=[0,1/math.sqrt(2),-1/math.sqrt(2),0]
work={1:mv(exchange(math.pi/4),work_a),-1:mv(exchange(math.pi/4),work_b)}


def setting(name):
    if name=='pair': return ([.5,.5],[axis,tuple(-x for x in axis)])
    if name=='triple': return (q,ns)
    raise ValueError(name)


def index(a,b,i,rec,w): return ((((a*2+b)*5+i)*4+rec)*16+w)


def joint_state(name):
    # Start AB singlet, Alice's 5-level pointer blank, Bob's paired pointer
    # blank |01>, and work |a>. Apply the conservation POVM, Bob's ±axis
    # record isometry, record-controlled preparation and quarter exchange.
    qs,dirs=setting(name); out=[0j]*(2*2*5*4*16)
    for i,(qi,n) in enumerate(zip(qs,dirs)):
        ka=scale(math.sqrt(2*qi),pure(n))
        for sign,record in ((1,1),(-1,2)):
            pb=pure(axis,sign)
            for a in range(2):
                for b in range(2):
                    amp=sum(ka[a][x]*pb[b][y]*psi[2*x+y] for x in range(2) for y in range(2))
                    for w in range(16): out[index(a,b,i,record,w)]+=amp*work[sign][w]
    return out


def probabilities(v):
    out={}
    for i in range(5):
        for record in (1,2):
            out[(i,record)]=sum(abs(v[index(a,b,i,record,w)])**2
                                 for a in range(2) for b in range(2) for w in range(16))
    return out


def local_density(v):
    # Trace Alice qubit and her 5-level pointer. Bob system consists of
    # his logical qubit, both record bits and four work bits (dimension 128).
    rho=[[0j]*128 for _ in range(128)]
    for a in range(2):
        for i in range(5):
            u=[v[index(a,b,i,r,w)] for b in range(2) for r in range(4) for w in range(16)]
            nonzero=[j for j,x in enumerate(u) if abs(x)>1e-14]
            for j in nonzero:
                for k in nonzero: rho[j][k]+=u[j]*u[k].conjugate()
    return rho


def apply_work(v,operator):
    out=[0j]*len(v)
    for a in range(2):
        for b in range(2):
            for i in range(5):
                for r in range(4):
                    u=mv(operator,[v[index(a,b,i,r,w)] for w in range(16)])
                    for w in range(16): out[index(a,b,i,r,w)]=u[w]
    return out


class FiveRayRecordCurrentUnificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pair=joint_state('pair'); cls.triple=joint_state('triple')

    def test_original_null_rays_recover_same_asymmetric_fractions(self):
        rays=[ray(0),ray(1),ray(3),ray(0,1),ray(0,2)]
        data,weights,dots=bridge(rays)
        ids=data['triple']
        self.assertEqual([weights[i] for i in ids],[F(1,8),F(2,5),F(19,40)])
        for i in range(3):
            for j in range(3): self.assertAlmostEqual(dot(ns[i],ns[j]),float(dots[ids[i]][ids[j]]))
        self.assertAlmostEqual(dot(axis,axis),1)
        for j,x in enumerate([dot(axis,n) for n in ns]):
            self.assertAlmostEqual(x,float(dots[data['pair'][0]][ids[j]]))
            self.assertAlmostEqual(-x,float(dots[data['pair'][1]][ids[j]]))
        for x,y in zip([dot(axis,n) for n in ns],[-1/5,1/2,-7/19]): self.assertAlmostEqual(x,y)
        for j in range(3): self.assertAlmostEqual(sum(q[i]*ns[i][j] for i in range(3)),0)

    def test_conservation_effects_define_trace_preserving_instruments(self):
        for name in ('pair','triple'):
            qs,dirs=setting(name)
            kraus=[scale(math.sqrt(2*qi),pure(n)) for qi,n in zip(qs,dirs)]
            close(self,total([mm(adj(k),k) for k in kraus]),eye(2))
            u=instrument_unitary(kraus)
            close(self,mm(adj(u),u),eye(10))
            for i,k in enumerate(kraus):
                for s in range(2):
                    for t in range(2): self.assertAlmostEqual(abs(u[5*t+i][5*s]-k[t][s]),0)

    def test_asymmetric_joint_table_uses_same_geometric_weights(self):
        p=probabilities(self.triple)
        want=[(F(3,40),F(1,20)),(F(1,10),F(3,10)),(F(13,40),F(3,20))]
        for i,(pplus,pminus) in enumerate(want):
            self.assertAlmostEqual(p[(i,1)],float(pplus))
            self.assertAlmostEqual(p[(i,2)],float(pminus))
            self.assertAlmostEqual(p[(i,1)]+p[(i,2)],q[i])
        self.assertAlmostEqual(sum(p[(i,1)] for i in range(3)),.5)
        self.assertAlmostEqual(sum(p[(i,2)] for i in range(3)),.5)
        self.assertAlmostEqual(norm2(self.triple),1)

    def test_conservation_weights_produce_conditioned_current_correlations(self):
        for name,v in (('pair',self.pair),('triple',self.triple)):
            qs,dirs=setting(name); p=probabilities(v)
            for i,(qi,n) in enumerate(zip(qs,dirs)):
                conditional=(p[(i,1)]-p[(i,2)])/qi
                self.assertAlmostEqual(conditional,-dot(axis,n))
                self.assertAlmostEqual(p[(i,1)],qi*(1-dot(axis,n))/2)
                self.assertAlmostEqual(p[(i,2)],qi*(1+dot(axis,n))/2)
            self.assertAlmostEqual(sum(p[(i,1)]-p[(i,2)] for i in range(len(qs))),0)

    def test_pair_and_triple_have_same_full_local_density_not_just_means(self):
        a=local_density(self.pair); b=local_density(self.triple)
        close(self,a,b)
        self.assertAlmostEqual(sum(a[i][i].real for i in range(128)),1)
        # Explicit local state is an equal mixture of opposite spin/record/
        # current pure states. No claim that the whole selects an event.
        expected=total([
            scale(.5,kron(kron(pure(axis,sign),outer([complex(j==rec) for j in range(4)])),outer(work[sign])))
            for sign,rec in ((1,1),(-1,2))])
        close(self,a,expected)

    def test_branchwise_opposite_records_and_sharp_equal_current(self):
        for v in (self.pair,self.triple):
            w=apply_work(v,J[0]); p=apply_work(v,proj)
            for a in range(2):
                for b in range(2):
                    for i in range(5):
                        for r,sgn in ((0,0),(1,1),(2,-1),(3,0)):
                            for k in range(16):
                                idx=index(a,b,i,r,k)
                                self.assertAlmostEqual(abs(w[idx]-sgn*v[idx]),0)
                                self.assertAlmostEqual(abs(p[idx]-v[idx]),0)
            opposite=apply_work(v,add(J[0],J[2]))
            self.assertAlmostEqual(norm2(opposite),0)

    def test_each_context_keeps_complete_local_record_distribution(self):
        for v in (self.pair,self.triple):
            p=probabilities(v)
            self.assertAlmostEqual(sum(p[(i,1)] for i in range(5)),.5)
            self.assertAlmostEqual(sum(p[(i,2)] for i in range(5)),.5)
            self.assertAlmostEqual(norm2(v),1)
        # Other operators on the entire Bob lab have the same statistics by
        # full density equality, not just equality of these two records.

    def test_no_signal_breaks_if_conditional_means_are_definite_local_values(self):
        pairmeans=[-1,1]
        triplemeans=[F(1,5),F(-1,2),F(7,19)]
        self.assertTrue(set(pairmeans).isdisjoint(triplemeans))
        self.assertEqual(sum(x*y for x,y in zip([F(1,8),F(2,5),F(19,40)],triplemeans)),0)
        # Exact locally accessible value would reveal context, despite equal
        # means. Actual ± current measurements instead have equal marginals.

    def test_positive_sign_sensitive_incidence_is_a_branchwise_residue(self):
        eta=.2; k=2
        for sign in (1,-1):
            values=(sign,-sign)
            equal=sum(k*x for x in values)
            weighted=sum(k*x*(1+eta*x) for x in values)
            self.assertEqual(equal,0)
            self.assertAlmostEqual(weighted,2*k*eta)
        # Counting or experience identification is a hypothesis, not physics.

    def test_autonomous_clock_calibration_transports_both_work_branches(self):
        t=math.pi/4; z=clock_expm(1,t)[2]; zm=clock_expm(-1,t)[2]
        self.assertAlmostEqual(abs(z-zm.conjugate()),0)
        phi=cmath.phase(-z); u=exchange(math.pi/4+phi)
        for initial,sign in ((work_a,1),(work_b,-1)):
            gp=scale(.5,add(proj,g)); gm=scale(.5,sub(proj,g))
            # Independently build the clock-2 amplitude from the ±G sectors.
            raw=plus(vecscale(z,mv(gp,initial)),vecscale(zm,mv(gm,initial)))
            got=mv(u,raw)
            for a,b in zip(got,work[sign]): self.assertAlmostEqual(abs(a+abs(z)*b),0)
            self.assertAlmostEqual(abs(inner(got,mv(J[0],got))-sign*abs(z)**2),0)
        self.assertAlmostEqual(abs(z)**2,.3597392417856652)

if __name__=='__main__': unittest.main()
