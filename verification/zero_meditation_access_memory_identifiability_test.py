"""Exact synthetic response-channel examples, not experimental meditation data.

A is a hypothetical functional cue signal, not a measure of experience.
Cross-arm channel invariance and independent false alarms are assumptions.
"""
import itertools
import unittest
from fractions import Fraction as F


def bernoulli(p):
    return ((0, 1-p), (1, p))


def observables(a,m,fi,fr,cue,phenomenal_rule):
    """Enumerate joint (immediate, delayed, E) probabilities for a cue.

    One idealized common channel is evaluated here. An experiment with a
    response arm and an observational arm needs an extra invariance assumption.
    E is merely an assigned, unobserved interpretation; nothing in the channel
    establishes that either assignment describes a conscious system.
    """
    out={}
    for (signal,ps),(memory,pm),(alarm_i,pi),(alarm_r,pr) in itertools.product(
            bernoulli(a if cue else F(0)),bernoulli(m),bernoulli(fi),bernoulli(fr)):
        immediate=int(bool(signal or alarm_i))
        delayed=int(bool((signal and memory) or alarm_r))
        e=phenomenal_rule(signal)
        key=(immediate,delayed,e)
        out[key]=out.get(key,F(0))+ps*pm*pi*pr
    return out


def marginal(distribution,axes):
    out={}
    for key,p in distribution.items():
        k=tuple(key[i] for i in axes);out[k]=out.get(k,F(0))+p
    return out


def probability_one(distribution,axis):
    return sum(p for k,p in distribution.items() if k[axis]==1)


def rates(a,m,fi,fr):
    return fi+(1-fi)*a,fr+(1-fr)*a*m


def infer(immediate_hit, immediate_false, delayed_hit, delayed_false):
    a=(immediate_hit-immediate_false)/(1-immediate_false)
    if a==0:return a,None
    return a,(delayed_hit-delayed_false)/((1-delayed_false)*a)


class MeditationAccessMemoryIdentifiabilityTests(unittest.TestCase):
    def setUp(self):
        self.fi=self.fr=F(1,10)
        self.fast=(F(4,5),F(1,4))
        self.slow=(F(1,5),F(1))
        self.rules=(lambda signal:1,lambda signal:signal)

    def test_delayed_recognition_alone_has_exactly_same_distribution(self):
        for cue in (0,1):
            one=observables(*self.fast,self.fi,self.fr,cue,self.rules[0])
            two=observables(*self.slow,self.fi,self.fr,cue,self.rules[0])
            self.assertEqual(marginal(one,(1,)),marginal(two,(1,)))
            self.assertEqual(probability_one(one,1), F(7,25) if cue else F(1,10))
        self.assertEqual(self.fast[0]*self.fast[1],self.slow[0]*self.slow[1])

    def test_immediate_access_disambiguates_under_shared_channel_assumption(self):
        fast,slow=[rates(*x,self.fi,self.fr) for x in (self.fast,self.slow)]
        self.assertEqual(fast,(F(41,50),F(7,25)))
        self.assertEqual(slow,(F(7,25),F(7,25)))
        for a,m in (self.fast,self.slow):
            h,r=rates(a,m,self.fi,self.fr)
            self.assertEqual(infer(h,self.fi,r,self.fr),(a,m))
        # Equal priors, one cue trial, optimal discrimination from immediate
        # response alone: (1+total variation)/2, in this idealized model.
        self.assertEqual((1+abs(fast[0]-slow[0]))/2,F(77,100))

    def test_same_delayed_observations_admit_a_continuum(self):
        # p = a*m = .2. Every a in [.2,1] has m=.2/a.
        for a in (F(1,5),F(1,4),F(2,5),F(4,5),F(1)):
            m=F(1,5)/a
            self.assertLessEqual(m,1)
            self.assertEqual(rates(a,m,self.fi,self.fr)[1],F(7,25))
        # At a=0, m is not identified even if both hit and false rates agree.
        self.assertEqual(infer(self.fi,self.fi,self.fr,self.fr),(F(0),None))

    def test_phenomenal_interpretations_do_not_change_the_observables(self):
        # Same functional channel, E assigned present throughout or present
        # only when signal is available. These are illustrative labels, not
        # a proof that either corresponds to a genuinely possible subject.
        for cue in (0,1):
            a=observables(*self.fast,self.fi,self.fr,cue,self.rules[0])
            b=observables(*self.fast,self.fi,self.fr,cue,self.rules[1])
            self.assertEqual(marginal(a,(0,1)),marginal(b,(0,1)))
            self.assertEqual(probability_one(a,2),1)
            self.assertEqual(probability_one(b,2),self.fast[0] if cue else 0)

    def test_if_probe_changes_the_channel_cross_arm_inference_can_fail(self):
        # Response arm has a=.8; separately randomized nonresponse arm has
        # a=.2, m=1 after probe disruption. Observed (.82,.28) are identical
        # to the single-channel fast model, but inferred memory 1/4 is wrong
        # for BOTH actual arm-specific memory values below.
        immediate=rates(F(4,5),F(1,2),self.fi,self.fr)[0]
        delayed=rates(F(1,5),F(1),self.fi,self.fr)[1]
        self.assertEqual(infer(immediate,self.fi,delayed,self.fr),(F(4,5),F(1,4)))
        self.assertNotEqual(F(1,4),F(1,2));self.assertNotEqual(F(1,4),F(1))

if __name__=='__main__':unittest.main()
