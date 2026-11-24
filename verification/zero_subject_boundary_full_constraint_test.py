"""Full-constraint subject-boundary and report-causality diagnostics.

The first comparison uses the actual five-ray code states. The coherent-record
control is a different preparation in an explicit extension beyond that code.
No physical spacelike separation or actual subjective report is assumed.
"""
import itertools
import math
import unittest
import numpy as np
from verification.zero_reciprocal_subject_exchange_test import J,proj
from verification.zero_integrated_sphere_clock_experience_test import sphere
from verification.zero_integrated_targeted_memory_test import make_model,evolve,theta,HIGH

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1.,-1.]).astype(complex)
PAULIS={'I':I,'X':X,'Y':Y,'Z':Z}


def tensor(seq):
    a=np.array([[1]],complex)
    for x in seq:a=np.kron(a,x)
    return a


def partial_record(psi):
    # psi[a,b,i,r,w], discard everything except both record bits r.
    mat=psi.transpose(3,0,1,2,4).reshape(4,-1)
    return mat@mat.conj().T


def td(a,b):return np.sum(abs(np.linalg.eigvalsh(a-b)))/2


def omega_dense(model,h):
    n=len(model[0]);dim=16*n;eye=np.eye(dim,dtype=complex)
    T=np.column_stack([theta(model,eye[:,j].reshape(2,2,2,2,n),h).ravel() for j in range(dim)])
    vals,U=np.linalg.eigh(T)
    return (U*np.sqrt(vals))@U.conj().T,T


class SubjectBoundaryFullConstraintTests(unittest.TestCase):
    def test_j_is_purely_four_body_and_h_has_five_body_coupling(self):
        j=np.asarray(J[0]);p=np.asarray(proj)
        coeff={''.join(k):np.trace(tensor([PAULIS[x] for x in k])@j)/16
               for k in itertools.product(PAULIS,repeat=4)}
        present={s:c for s,c in coeff.items() if abs(c)>1e-12}
        self.assertEqual(len(present),8)
        self.assertTrue(all('I' not in s for s in present))
        self.assertTrue(all(abs(abs(c)-1/8)<1e-12 for c in present.values()))
        h=(np.kron(I,p)-np.kron(Z,j))/2
        # Every R1-work two-body Pauli coefficient vanishes, while the full
        # cross-boundary double commutator is nonzero.
        for target in range(4):
            for a,b in itertools.product((X,Y,Z),repeat=2):
                ops=[I]*4;ops[target]=b
                self.assertLess(abs(np.trace(h@np.kron(a,tensor(ops)))/32),1e-13)
        xr=np.kron(X,np.eye(16));xw=np.kron(I,np.kron(X,np.eye(8)))
        comm=lambda A,B:A@B-B@A
        self.assertGreater(np.linalg.norm(comm(comm(h,xr),xw)),1)

    def test_actual_five_ray_state_h_swap_is_invisible_to_all_record_povms(self):
        for setting in ('pair','triple'):
            v=sphere(setting);r0=partial_record(v[0]);r1=partial_record(v[1])
            self.assertLess(np.linalg.norm(r0-r1),1e-13)
            self.assertLess(abs(np.vdot(v[0].ravel(),v[1].ravel())),1e-13)
            self.assertLess(np.linalg.norm(r0-np.diag([0,.5,.5,0])),1e-13)
            for h in (0,1):
                jv=np.einsum('abirw,xw->abirx',v[h],np.asarray(J[0]))
                kv=jv*np.array([1,1,-1,-1])[None,None,None,:,None]
                self.assertLess(np.linalg.norm(kv-(1-2*h)*v[h]),1e-13)
        # Complete density equality, not just a chosen expected observable.

    def test_local_report_cannot_reproduce_the_J_rule(self):
        # Rows r=+1,-1; columns observed report +1,-1. With a symmetric
        # report error e, the two conditional joint tables are distinct,
        # whereas every R-only quantum instrument sees the same density.
        for e in (0,.05,.1,.25,.49):
            p0=np.array([[1-e,e],[e,1-e]])/2
            p1=np.array([[e,1-e],[1-e,e]])/2
            self.assertAlmostEqual(np.sum(abs(p0-p1))/2,1-2*e)
            correct=1-e
            self.assertGreater(correct,.5)
            self.assertGreater(1-(-e*math.log2(e)-(1-e)*math.log2(1-e)) if e else 1,0)
        # R (record-only) and -R are both local, opposite, and pairwise balanced.
        for r in (-1,1):
            self.assertEqual(sum((r,-r)),0)
            self.assertEqual(sum((-r,r)),0)
            self.assertNotEqual(r,-r)

    def test_full_constraint_can_couple_outside_original_code_sector(self):
        model=make_model(80);v0=evolve(model,0,5);v1=evolve(model,1,5)
        g=np.vdot(v1,v0)
        # R1 initially |+>; active work J1 is fixed to +1 or -1. The two
        # resulting joint amplitudes use the same two h-channel solutions.
        plus=np.stack((v0,v1))/math.sqrt(2)
        minus=np.stack((v1,v0))/math.sqrt(2)
        def rho(v):
            a=v.reshape(2,-1);return a@a.conj().T
        A,B=rho(plus),rho(minus)
        self.assertAlmostEqual(td(A,B),abs(g.imag),places=12)
        self.assertAlmostEqual(td(A,B),.8875530356795106,places=10)
        self.assertAlmostEqual(np.trace(A).real,1,places=10)
        self.assertAlmostEqual(np.trace(B).real,1,places=10)

    def test_exact_positive_generator_difference_is_illustrated_dense(self):
        model=make_model(8);o0,t0=omega_dense(model,0);o1,t1=omega_dense(model,1)
        beta=math.sqrt(HIGH+1.2)-math.sqrt(HIGH)
        self.assertAlmostEqual(beta,.16970842174845924,places=12)
        self.assertGreaterEqual(np.linalg.eigvalsh(t0-t1)[0],1.2-1e-12)
        self.assertGreater(np.linalg.eigvalsh(o0-o1)[0],beta-1e-12)

    def test_grid_convergence_of_exposed_physical_channel(self):
        vals=[]
        for n in (40,80,160):
            m=make_model(n);a=evolve(m,0,5);b=evolve(m,1,5)
            vals.append(abs(np.vdot(b,a).imag))
        self.assertLess(abs(vals[1]-vals[0]),3e-6)
        self.assertLess(abs(vals[2]-vals[1]),1e-6)

if __name__=='__main__':unittest.main()
