"""Exact sparse stationary POVM for the angular echo's reduced carrier.

This complements the large-vector echo/purified-reservoir checks. It tests
stationarity on the ENTIRE reduced basis, not on a single history orbit.
The extra random anchor is a specified physical protocol resource.
"""
import unittest
import numpy as np
from verification.zero_stationary_battery_bridge import (
    TICKS,STATES,PREFIX,INVERSE,advance,initial_amplitudes,
)
from verification.zero_coherent_clock_angular_history import checkpoint_at

INDEX={x:i for i,x in enumerate(STATES)}


def shift(v,q):
    out=np.zeros_like(v)
    for t in range(TICKS):
        for i,x in enumerate(STATES):
            out[(t+1)%TICKS,INDEX[advance(t,x)]] = np.roll(v[t,i],q,axis=0)
    return out


def twirled_anchor(q,anchor,reference,predicate):
    """Sum of orthogonal clock-block images of one anchor event."""
    effect=np.zeros((TICKS,len(STATES),4,4),float)
    for k in range(TICKS):
        target=(anchor+k)%TICKS; ref=(reference+q*k)%4
        for x in STATES:
            if predicate(x):
                y=PREFIX[target][INVERSE[anchor][x]]
                effect[target,INDEX[y],ref,:]=1
    return effect


def averaged_effect(q,reference,predicate):
    return sum(twirled_anchor(q,t,reference,predicate) for t in range(TICKS))/TICKS


def history(q):
    v=np.zeros((TICKS,len(STATES),4,4),complex)
    for (b,z,r,s),amp in initial_amplitudes().items():
        bins=range(2,4) if b==1 else (range(0,1) if z==-1 else range(1,2))
        for i in bins:
            for t in range(TICKS):
                y=PREFIX[t][b,z,r,s]
                v[t,INDEX[y],q*t%4,i]=amp/np.sqrt(TICKS*len(bins))
    return v


class ClockRelationalPovmTests(unittest.TestCase):
    def test_stationary_anchor_twirls_on_entire_basis_and_controls(self):
        for q in (1,2):
            psi=history(q)
            np.testing.assert_allclose(shift(psi,q),psi,atol=1e-13)
            self.assertAlmostEqual(np.vdot(psi,psi).real,1.,places=13)
            effects=[]
            for r in range(4):
                e=averaged_effect(q,r,lambda x:True)
                d=averaged_effect(q,r,lambda x:x[2]==-1)
                effects.append(e)
                self.assertGreaterEqual(e.min(),0)
                self.assertLessEqual(e.max(),1)
                self.assertTrue(np.all(d<=e))
                # Conjugating any diagonal effect is a permutation of its
                # diagonal; this checks commutation on every carrier basis.
                np.testing.assert_array_equal(shift(e,q),e)
                np.testing.assert_array_equal(shift(d,q),d)
            np.testing.assert_allclose(sum(effects),1,atol=1e-13)
            e=effects[2];d=averaged_effect(q,2,lambda x:x[2]==-1)
            p=np.vdot(psi,e*psi).real
            p_disagree=np.vdot(psi,d*psi).real/p
            self.assertAlmostEqual(p,.25 if q==1 else .5,places=13)
            self.assertAlmostEqual(p_disagree,.1 if q==1 else .05,places=13)
            # A bare reference reading is not stationary, unlike the twirl.
            bare=np.zeros_like(e);bare[:,:,2,:]=1
            self.assertFalse(np.array_equal(shift(bare,q),bare))

if __name__=='__main__':unittest.main()
