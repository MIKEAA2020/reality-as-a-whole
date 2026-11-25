"""Two explicitly hypothesized incidence types on the actual sphere history.

The direct-sum space encodes a proposed incidence measure, not an added
physical branch, objective random selector or proof that either port feels.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import I,X,Z,kron,active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial,apply64,SWAP
from verification.zero_internal_contextual_reference_test import Bs,Zj,Gint,S,P,value_history
from verification.zero_internal_reference_subject_valence_candidates_test import (
    b_project,j_project,born_table,
)
from verification.zero_dynamic_subject_memory_echo_test import jwrite
from verification.zero_persistent_sphere_subject_selection_test import norm2


def coarse_table():
    out=defaultdict(F)
    for (i,b,z,s),w in born_table().items():out[(b,z,s)]+=w
    return dict(out)


def incidence(alpha,measure=None):
    """Weighted hypothesis: one type per port, Born within each type."""
    table=coarse_table() if measure is None else measure
    return {(typ,b,z,s):(alpha if typ=='B' else 1-alpha)*w
            for (b,z,s),w in table.items() for typ in ('B','j')}


def post_joint_table():
    out=defaultdict(F)
    for (b,z,s),w in coarse_table().items():
        r=b;j=b*z
        out[(s*r,s*r*j,s*j)]+=w # sphere, pre-j, current-j
    return dict(out)


class JointConstitutionIncidenceEchoTests(unittest.TestCase):
    def test_two_observables_are_gauge_invariant_distinct_and_commuting(self):
        vb=kron(Bs,Z);vj=kron(Zj,Z);p=kron(P,I)
        gauge=kron(Gint,I);counter=kron(S,X)
        for v in (vb,vj):
            np.testing.assert_allclose(v@gauge,gauge@v,atol=1e-13)
            np.testing.assert_allclose(counter@v@counter,-v,atol=1e-13)
            np.testing.assert_allclose(v@p,p@v,atol=1e-13)
        np.testing.assert_allclose(vb@vj,vj@vb,atol=1e-13)
        self.assertGreater(np.linalg.norm((vb-vj)@p),1)
        # Both can be copied into distinct neutral ready pointers by
        # commuting projective controlled-X gates. This is physical output,
        # not proof that either pointer is an experiencing subject.
        projs={(a,b):p@(np.eye(512)+a*vb)@(np.eye(512)+b*vj)/4
               for a,b in product((1,-1),repeat=2)}
        np.testing.assert_allclose(sum(projs.values()),p,atol=1e-13)
        for key,proj in projs.items():
            np.testing.assert_allclose(proj@proj,proj,atol=1e-13)
            for other in projs:
                if other!=key:np.testing.assert_allclose(proj@projs[other],0,atol=1e-13)

    def test_actual_quantum_signs_disagree_and_counterparts_all_16(self):
        state=output(active_base())
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0]);mass=norm2(x)
            branches={s:(x+s*value_history(x))/2 for s in (1,-1)}
            mismatch=0.
            for s,v in branches.items():
                np.testing.assert_allclose(apply64(SWAP,v),-branches[-s],atol=1e-13)
                # The actual echo's Q is odd under this counterpart, so its
                # final coherent density is still counterpart-invariant.
                np.testing.assert_allclose(apply64(SWAP,value_history(v)),
                                           value_history(branches[-s]),atol=1e-13)
                for b,z in product((1,-1),repeat=2):
                    u=j_project(b_project(v,b),z)
                    if b!=z:mismatch+=norm2(u)/mass
            self.assertAlmostEqual(mismatch,.25,places=12)
        # The tested gauge fixes BOTH parities and cannot exchange them.
        # This does not rule out a different equivalence of a full
        # physical-experiential theory.

    def test_simultaneous_port_values_and_incidence_symmetry(self):
        tab=coarse_table()
        self.assertEqual(len(tab),6)
        for (b,z,s),w in tab.items():self.assertEqual(w,tab[(b,z,-s)])
        for alpha in (F(1,4),F(1,2),F(2,3),F(3,4)):
            mu=incidence(alpha)
            self.assertEqual(sum(mu.values()),1)
            self.assertTrue(all(w>0 for w in mu.values()))
            self.assertEqual(sum(w for (t,b,z,s),w in mu.items() if t=='B'),alpha)
            for typ in ('B','j'):
                total=sum(w*s*(b if t=='B' else z) for (t,b,z,s),w in mu.items() if t==typ)
                after=sum(w*s*(b if t=='B' else b*z) for (t,b,z,s),w in mu.items() if t==typ)
                self.assertEqual(total,0)
                self.assertEqual(after,0)
            for (t,b,z,s),w in mu.items():self.assertEqual(w,mu[(t,b,z,-s)])
        self.assertEqual(sum(w for (b,z,s),w in tab.items() if b!=z),F(1,4))
        # Positive/negative balance is conditioned on taking the assignments
        # as actual felt signs and these weights as incidence weights.

    def test_effect_consistency_and_physical_certainty_leave_type_weight_free(self):
        # General direct-sum counterexample: a pure fixed physical state rho
        # embedded twice as two hypothesized incidence types. It verifies the
        # operator algebra; the actual two parities are checked separately.
        psi=np.array([1,1j],complex)/np.sqrt(2);rho=np.outer(psi,psi.conj())
        def sigma(a):
            out=np.zeros((4,4),complex);out[:2,:2]=a*rho;out[2:,2:]=(1-a)*rho
            return out
        certainty=np.kron(np.eye(2),rho);type_b=np.diag([1,1,0,0])
        swap=np.kron(X,I)
        for a in (.5,2/3):
            st=sigma(a)
            self.assertAlmostEqual(np.trace(st).real,1,places=13)
            self.assertGreaterEqual(np.linalg.eigvalsh(st).min(),-1e-14)
            self.assertAlmostEqual(np.trace(st@certainty).real,1,places=13)
            self.assertAlmostEqual(np.trace(st@type_b).real,a,places=13)
            for effect in ((I+Z)/2,(I+X)/2,np.array([[.6,.1j],[-.1j,.3]])):
                ev=np.linalg.eigvalsh(effect)
                self.assertGreaterEqual(ev.min(),-1e-14);self.assertLessEqual(ev.max(),1+1e-14)
                self.assertAlmostEqual(np.trace(st@np.kron(I,effect)).real,np.trace(rho@effect).real,places=13)
        np.testing.assert_allclose(swap@sigma(.5)@swap,sigma(.5),atol=1e-14)
        self.assertGreater(np.linalg.norm(swap@sigma(2/3)@swap-sigma(2/3)),.1)
        # Passive relabeling transforms both state and queried effects and
        # leaves probabilities unchanged at any a. Active swap-invariance
        # is a distinct extra premise and fixes a=1/2.
        st=sigma(2/3);e=type_b
        self.assertAlmostEqual(np.trace(st@e).real,np.trace((swap@st@swap)@(swap@e@swap)).real,places=13)
        # More importantly, swapping type blocks alone does not preserve a
        # fixed intrinsic value diag(V_B,V_j) when V_B != V_j.
        vv=np.block([[Z,np.zeros((2,2))],[np.zeros((2,2)),X]])
        self.assertGreater(np.linalg.norm(swap@vv@swap-vv),1)

    def test_equal_overall_type_weight_does_not_imply_equal_local_conditional_weight(self):
        # On the actual commuting-record algebra, let type B have weight
        # 3/4 in b=+ and 1/4 in b=-. Its global weight is still 1/2.
        # Counterpart s->-s is preserved and both types have positive weight.
        weights={}
        for (b,z,s),p in coarse_table().items():
            a=F(3,4) if b==1 else F(1,4)
            weights[('B',b,z,s)]=p*a
            weights[('j',b,z,s)]=p*(1-a)
        self.assertEqual(sum(weights.values()),1)
        self.assertEqual(sum(w for (t,b,z,s),w in weights.items() if t=='B'),F(1,2))
        mismatch=sum(w for (t,b,z,s),w in weights.items() if b!=z)
        mb=sum(w for (t,b,z,s),w in weights.items() if b!=z and t=='B')
        self.assertEqual(mb/mismatch,F(1,4))
        for (t,b,z,s),w in weights.items():
            self.assertEqual(w,weights[t,b,z,-s])
        for t in ('B','j'):
            self.assertEqual(sum(w*s*(b if t=='B' else z) for (tt,b,z,s),w in weights.items() if tt==t),0)
        # This state-dependent assignment is valid on the commuting record
        # algebra, but cannot extend to all effects with the SAME PURE
        # physical marginal: positive sigma_B <= |psi><psi| forces
        # sigma_B to be a scalar multiple of that rank-one projector.
        psi=np.array([1,1],complex)/np.sqrt(2);rho=np.outer(psi,psi.conj())
        for a in (0,.25,.5,.75,1):
            sb=a*rho
            pplus=(I+Z)/2;pminus=(I-Z)/2
            self.assertAlmostEqual(np.trace(sb@pplus).real/np.trace(rho@pplus).real,a)
            self.assertAlmostEqual(np.trace(sb@pminus).real/np.trace(rho@pminus).real,a)

    def test_label_counting_is_not_automatically_physical_weight(self):
        tab=coarse_table()
        self.assertEqual(sum(w for (b,z,s),w in tab.items() if b!=z),F(1,4))
        unit={key:F(1,len(tab)) for key in tab}
        self.assertEqual(sum(w for (b,z,s),w in unit.items() if b!=z),F(1,3))
        # Split each b=z=+ effect into two equal aliases; coarsen them
        # immediately back to the same operational event.
        refined=[]
        for (b,z,s),w in tab.items():
            mult=2 if (b,z)==(1,1) else 1
            for alias in range(mult):refined.append(((b,z,s,alias),w/mult))
        self.assertEqual(len(refined),8)
        self.assertEqual(sum(w for key,w in refined),1)
        self.assertEqual(sum(w for (b,z,s,a),w in refined if b!=z),F(1,4))
        self.assertEqual(F(sum(1 for (b,z,s,a),w in refined if b!=z),len(refined)),F(1,4))
        # If labels represent genuinely different experiences rather than
        # aliases, the ontology and physical experiment have changed; the
        # calculation does not decide that.

    def test_echo_joint_disagreement_distribution_from_actual_quantum_states(self):
        # All three signs are jointly readable AFTER the echo using s,r,j':
        # sphere=s*r, pre-echo j=s*r*j', current j=s*j'.
        expected={(0,0):F(1,2),(1,0):F(1,4),(0,1):F(1,4),(1,1):F(0)}
        state=output(active_base())
        for label in range(16):
            x=initial(relative_read(state,4,labels=(label,))[0]);mass=norm2(x)
            seen=defaultdict(float)
            for s in (1,-1):
                v=(x+s*value_history(x))/2
                a,c=jwrite(v,0*v);a,c=value_history(a),value_history(c);a,c=jwrite(a,c)
                for r,u in ((1,a),(-1,c)):
                    for j in (1,-1):
                        part=j_project(u,j); w=norm2(part)/mass
                        dpre=int(j==-1);dpost=int(j!=r)
                        seen[dpre,dpost]+=w
            for key,w in expected.items():self.assertAlmostEqual(seen[key],float(w),places=12)
        self.assertEqual(sum(post_joint_table().values()),1)

    def test_incidence_type_prediction_and_report_noise(self):
        for a in (F(1,2),F(2,3)):
            mu=incidence(a)
            den=sum(w for (t,b,z,s),w in mu.items() if b!=z)
            sphere=sum(w for (t,b,z,s),w in mu.items() if b!=z and t=='B')
            self.assertEqual(sphere/den,a)
            for eps in (F(0),F(1,10),F(1,2)):
                self.assertEqual((sphere*(1-eps)+(den-sphere)*eps)/den,eps+(1-2*eps)*a)
        # This is a conditional prediction of the postulated incidence and
        # calibrated report channel, not an observed person or experiment.

if __name__=='__main__':unittest.main()
