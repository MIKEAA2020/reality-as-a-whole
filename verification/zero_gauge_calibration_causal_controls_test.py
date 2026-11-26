"""Tests for selection, transfer counterexamples, and robust intervals."""
import random
import unittest

from verification.zero_gauge_calibration_causal_controls import (
    CONTEXTS, selected_null_tables, product_mean, robust_interval)
from verification.zero_gauge_clock_meta_root import (
    adversarial_output, counterfeit_a, target_output, target_post_mu)


class CausalCalibrationTests(unittest.TestCase):
    def test_selection_creates_signal_without_readout_error_context(self):
        eps=.8; pb=.05; pc=.1; r=.9
        s=2*eps/81
        p,tables=selected_null_tables(r,s,pb,pc)
        gain=(1-2*pb)*(1-2*pc)
        self.assertAlmostEqual(p,r)
        self.assertAlmostEqual(product_mean(tables[1]),gain*s)
        self.assertAlmostEqual(product_mean(tables[0]),-gain*r*s/(1-r))
        for b,c in CONTEXTS:
            self.assertAlmostEqual(tables[1][b,c],(1+b*c*gain*s)/4)
        # Single-sign late rates both equal r, yet product-conditioned rates differ.
        for b in (1,-1):
            self.assertAlmostEqual(sum(r*(1+s*b*c)/2 for c in (1,-1)),r)
        for c in (1,-1):
            self.assertAlmostEqual(sum(r*(1+s*b*c)/2 for b in (1,-1)),r)
        self.assertNotAlmostEqual(r*(1+s),r*(1-s))
        with self.assertRaises(ValueError):selected_null_tables(.99,.1,pb,pc)

    def test_shared_cause_implements_context_error_without_direct_signal(self):
        # Lambda carries independent latent bits u,v. Source b=u,c=v; the
        # B-side receives u,v from the common past, not a signal from C.
        pb=.05;pc=.1;a=-.008888888888888889
        joint={key:0. for key in CONTEXTS}
        for u,v in CONTEXTS:
            b,c=u,v
            fb=pb+a*b*v
            for eb in (0,1):
                for ec in (0,1):
                    p=.25*(fb if eb else 1-fb)*(pc if ec else 1-pc)
                    joint[(b*(-1)**eb,c*(-1)**ec)]+=p
        rival,*_=adversarial_output(pb,pc,a)
        for key in CONTEXTS:self.assertAlmostEqual(joint[key],rival[key],places=15)

    def test_matched_reference_and_source_mode_distinction(self):
        # A hidden apparatus mode perfectly predicts calibration vs source.
        # Both rival and target agree on every reference, but the source mode
        # changes to the previous contextual channel. Source data then match.
        pb=.05;pc=.1;eps=.8;q=2/9
        a=counterfeit_a(q,eps,1,1,pb)
        rival,*_=adversarial_output(pb,pc,a)
        target=target_output(target_post_mu(q,eps,1,1,pb,pc))
        for key in target:self.assertAlmostEqual(rival[key],target[key],places=14)
        # With the same clock and blank behavior, even the complete coarse
        # (early/late, blank-or-sign B, sign C) joint table is identical.
        from verification.zero_gauge_clock_joint_instrument import clock_model
        f,_,_,_=clock_model(40,.05,.1)
        ppost=sum(f[10:]**2)
        def whole_table(sign_table):
            result={}
            for y in (0,1):
                wrate=.9 if y else .1
                brate=.05 if y else .95
                for b,c in CONTEXTS:result[y,b,c]=ppost*wrate*sign_table[b,c]
                for c in (1,-1):result[y,0,c]=(1-ppost)*brate/2
            return result
        first=whole_table(target);second=whole_table(rival)
        self.assertAlmostEqual(sum(first.values()),1.)
        for key in first:self.assertAlmostEqual(first[key],second[key],places=14)
        for b,c in CONTEXTS:
            ideal=(1-2*pb)*(1-2*pc)*b*c
            cal_for_target=cal_for_rival=ideal
            self.assertEqual(cal_for_target,cal_for_rival)
            source_rival=(1-2*pc)*((1-2*pb)*b*c-2*a)
            self.assertAlmostEqual(abs(source_rival-cal_for_rival),2*(1-2*pc)*abs(a))
        # Sources differ: target preselection true correlation 2 eps/81 vs zero.
        self.assertGreater(2*eps/81,0)

    def test_hypothetical_calibration_and_nonzero_uncertainty(self):
        m=1_000_000
        calibration={(b,c):(860000 if b*c==1 else 140000,m) for b,c in CONTEXTS}
        out=robust_interval(.01769,100000,.025,calibration,.025,.993,.995,.72,
                            contamination=.0005,transport=.001,selection_tv=.0002,
                            blank_mean_bound=.005)
        self.assertAlmostEqual(out['cal_discrepancy'],0.,places=15)
        self.assertAlmostEqual(out['blank_allowance'],.000035,places=15)
        self.assertGreater(out['lower'],0.)
        self.assertLess(out['lower'],out['upper'])
        self.assertAlmostEqual(out['cal_radius'],(2*__import__('math').log(320)/m)**.5)
        # If the signal-scale transfer uncertainty is not independently bounded,
        # the same counts cannot certify its sign.
        no_transfer_bound=robust_interval(.01769,100000,.025,calibration,.025,
                                          .993,.995,.72,transport=2.)
        self.assertEqual(no_transfer_bound['lower'],-1.)
        self.assertEqual(no_transfer_bound['upper'],1.)

    def test_bound_for_arbitrary_context_response_and_selection(self):
        # Exact synthetic population means; large samples make finite-shot
        # allowances tiny. Context response need not arise from independent flips.
        m=100_000_000;gain=.72
        hs={(1,1):.726,(1,-1):-.718,(-1,1):-.711,(-1,-1):.715}
        calibration={k:(round((1+h)*m/2),m) for k,h in hs.items()}
        true_probs={(1,1):.32,(1,-1):.18,(-1,1):.22,(-1,-1):.28}
        z=sum(b*c*p for (b,c),p in true_probs.items())
        w=.94;mean=w*sum(true_probs[k]*hs[k] for k in CONTEXTS)
        out=robust_interval(mean,m,.01,calibration,.01,w,w,gain)
        self.assertLessEqual(out['lower'],z)
        self.assertGreaterEqual(out['upper'],z)
        self.assertAlmostEqual(out['cal_discrepancy'],.009,places=12)

    def test_preselection_tv_and_blank_cover_worst_perturbation(self):
        m=100_000_000;gain=.72
        calibration={(b,c):(int(m*(1+gain*b*c)/2),m) for b,c in CONTEXTS}
        # Accepted product z=.3, preselection .2, TV=.05; blank bias .2.
        w=.9;mean=w*gain*.3+(1-w)*.2
        out=robust_interval(mean,m,.01,calibration,.01,.89,.91,gain,
                            selection_tv=.05,blank_mean_bound=.2)
        self.assertLessEqual(out['lower'],.2)
        self.assertGreaterEqual(out['upper'],.2)
        missing_w=robust_interval(mean,m,.01,calibration,.01,0.,.91,gain)
        self.assertEqual((missing_w['lower'],missing_w['upper']),(-1.,1.))

    def test_random_context_channels_and_weights(self):
        rng=random.Random(501);m=100_000_000;gain=.72
        for _ in range(500):
            ps=[rng.random() for k in CONTEXTS];total=sum(ps)
            probs={k:p/total for k,p in zip(CONTEXTS,ps)}
            hs={k:gain*k[0]*k[1]+rng.uniform(-.04,.04) for k in CONTEXTS}
            cal={k:(round(m*(1+h)/2),m) for k,h in hs.items()}
            w=rng.uniform(.5,.99);blank=rng.uniform(-.1,.1)
            mu=w*sum(probs[k]*hs[k] for k in CONTEXTS)+(1-w)*blank
            z=sum(k[0]*k[1]*probs[k] for k in CONTEXTS)
            out=robust_interval(mu,m,.01,cal,.01,max(.01,w-.01),min(1.,w+.01),
                                gain,blank_mean_bound=.1)
            self.assertLessEqual(out['lower'],z)
            self.assertGreaterEqual(out['upper'],z)

    def test_input_validation(self):
        cal={(b,c):(1,2) for b,c in CONTEXTS}
        with self.assertRaises(ValueError):robust_interval(0.,10,.05,{},.05,.9,1.,.72)
        with self.assertRaises(ValueError):robust_interval(0.,10,.05,cal,.05,.9,1.,0.)
        with self.assertRaises(ValueError):robust_interval(0.,10,.05,cal,.05,.9,1.,.72,selection_tv=2.)
        with self.assertRaises(ValueError):robust_interval(0.,10,.05,{k:(3,2) for k in CONTEXTS},.05,.9,1.,.72)

if __name__=='__main__':unittest.main()
