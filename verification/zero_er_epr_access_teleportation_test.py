"""ER=EPR reading: conditional access and teleportation in the actual echo.

No wormhole or physical subject is assumed. Teleportation is a separately
stipulated intervention; the original 20-step program contains no such gate.
"""
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np
from verification.zero_all_sector_noncommuting_sphere_test import I,X,Y,Z,kron
from verification.zero_clock_finite_reservoir_reuse_test import BITS3,Q as THERMAL
from verification.zero_sphere_reuse_noisy_auxiliary_memory_test import words,distribution
from verification.zero_sphere_local_constitution_echo_test import twenty_tick_path
from verification.zero_joint_constitution_incidence_echo_test import coarse_table
from verification.zero_tensor_network_sphere_pair_echo_test import actual_pair_reduced,controlled_pair_mps,partial_trace,negativity


def pair_given_b(t,b,qaux=F(0)):
    # Actual b,z,s Born law, normalized conditional on B bit b; all
    # apparatus stores and purifiers are retained as environment labels.
    sectors=[(int(bb==-1),int(z==-1),p*2)
             for (bb,z,s),p in coarse_table().items() if int(bb==-1)==b]
    rho=np.zeros((4,4),complex);cols=((1,),(0,))
    for (_,z,p),x,f,e in product(sectors,BITS3,BITS3,words(1)):
        w=p*F(1,8)*distribution(THERMAL,f)*distribution(qaux,e)
        if not w:continue
        state,zz,r=twenty_tick_path(b,x,f,e,cols,z)[t]
        xf=(x[0]^1,x[1],x[2]);other,zzz,rr=twenty_tick_path(b,xf,f,e,cols,z)[t]
        index=2*state[1][0]+x[0];op=2*other[1][0]+xf[0]
        rho[index,index]+=float(w)
        if state[2:]==other[2:] and state[1][1:]==other[1][1:] and (zz,r)==(zzz,rr):
            rho[index,op]+=float(w)
    return rho


def bell(b=0):
    v=np.zeros(4,complex)
    for x in (0,1):v[2*(x^b)+x]=1/np.sqrt(2)
    return np.outer(v,v.conj())


def teleport(input_state,resource,deliver=True):
    # Input Q, sender S, receiver F. Bell measurement Q,S followed by
    # outcome-dependent local correction X^m Z^n on F if bits arrive.
    full=kron(input_state,resource);out=np.zeros((8,8),complex)
    for m,n in product((0,1),repeat=2):
        u=np.linalg.matrix_power(X,m)@np.linalg.matrix_power(Z,n)
        v=kron(I,u)@np.array([1,0,0,1],complex)/np.sqrt(2)
        p=np.outer(v,v.conj());corr=u if deliver else I
        op=kron(p,corr);out+=op@full@op.conj().T
    return np.trace(out.reshape(4,2,4,2),axis1=0,axis2=2)


def avg_fidelity(resource):
    # Six Pauli eigenstates form a qubit projective 2-design, so their
    # average is exactly the uniform pure-state average for this channel.
    score=0.
    for op,sign in product((X,Y,Z),(1,-1)):
        inp=(I+sign*op)/2;score+=np.trace(inp@teleport(inp,resource)).real/6
    return score


class ErEprAccessTests(unittest.TestCase):
    def test_actual_conditional_pair_and_echo_record(self):
        z=Z;phi=bell(0)
        for q,b in product((F(0),THERMAL),(0,1)):
            for t in range(21):
                rho=pair_given_b(t,b,q)
                want=(phi if t in (0,20) else bell(b) if t in (1,19)
                      else (np.eye(4)+(-1)**b*kron(z,z))/4)
                np.testing.assert_allclose(rho,want,atol=1e-13,err_msg=f'{q},{b},{t}')
                self.assertAlmostEqual(negativity(rho),.5 if t in (0,1,19,20) else 0,places=12)
            for x,f,e,zbit in product(BITS3,BITS3,words(1),(0,1)):
                _,_,r=twenty_tick_path(b,x,f,e,((1,),(0,)),zbit)[10]
                self.assertEqual(r,b)
        # Echo memory r can specify b at tick 10 only to an interface that
        # actually accesses it; reading it is a physical intervention.

    def test_standard_teleportation_channels_at_representative_ticks(self):
        samples=[(I+op)/2 for op in (X,Y,Z)]+[(I-Z)/2]
        for t in (0,1,2,10,18,19,20):
            resource=actual_pair_reduced(t,F(0))
            for inp in samples:
                output=teleport(inp,resource)
                if t in (0,20):target=inp
                elif t in (1,19):target=(inp+X@inp@X)/2
                else:target=I/2
                np.testing.assert_allclose(output,target,atol=1e-13,err_msg=f't={t}')
            self.assertAlmostEqual(avg_fidelity(resource),
                1 if t in (0,20) else 2/3 if t in (1,19) else 1/2,places=13)

    def test_b_record_corrects_bell_not_lost_coherence(self):
        samples=[(I+op)/2 for op in (X,Y,Z)]+[(I-Z)/2]
        for t,b in product((1,10,19),(0,1)):
            r=pair_given_b(t,b);xb=np.linalg.matrix_power(X,b)
            corrected=kron(I,xb)@r@kron(I,xb)
            for inp in samples:
                result=teleport(inp,corrected)
                want=inp if t in (1,19) else (inp+Z@inp@Z)/2
                np.testing.assert_allclose(result,want,atol=1e-13)
            self.assertAlmostEqual(avg_fidelity(corrected),1 if t in (1,19) else 2/3,places=13)
            if t==10:self.assertAlmostEqual(negativity(corrected),0,places=13)
        # Access to a record does not, on its own, reverse all the reservoir
        # writes. Gate the inverse program before measuring/using a resource
        # if one wants recovery; teleporting is an intervention itself.

    def test_no_signal_without_two_classical_outcome_bits(self):
        for t,b in product((0,1,10,19,20),(0,1)):
            r=pair_given_b(t,b);expected=I/2
            for op,sign in product((X,Y,Z),(1,-1)):
                inp=(I+sign*op)/2
                np.testing.assert_allclose(teleport(inp,r,deliver=False),expected,atol=1e-13)
        # Sending Bell outcomes (and B if needed) is extra causal access,
        # not a signal transmitted by shared entanglement alone.

    def test_actual_source_pair_monogamy_by_conditional_purity(self):
        psi=controlled_pair_mps().reshape(2,2,2,2,2,2,2)
        # Condition B. SF0 is exactly pure Bell and thus uncorrelated with
        # the remaining two pairs. This explicitly realizes the general
        # statement that a pure bipartite marginal factors from the rest.
        for b in (0,1):
            vector=psi[b].reshape(64)*np.sqrt(2)
            pair=partial_trace(vector,[0,1],(2,2,2,2,2,2))
            rest=partial_trace(vector,[2,3,4,5],(2,2,2,2,2,2))
            np.testing.assert_allclose(pair,bell(b),atol=1e-13)
            np.testing.assert_allclose(np.outer(vector,vector.conj()),kron(pair,rest),atol=1e-13)
        # Dropping B makes SF0 separable, not doubly maximally entangled.
        unconditioned=partial_trace(psi.reshape(128),[1,2],(2,2,2,2,2,2,2))
        self.assertAlmostEqual(negativity(unconditioned),0,places=13)

if __name__=='__main__':unittest.main()
