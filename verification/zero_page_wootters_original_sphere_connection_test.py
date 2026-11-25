"""Page--Wootters 1983: primary-source spin checks and sphere relation.

Finite clock constructions are models of relational observables, not claims
that the attached paper proves cosmic energy zero or phenomenal subjects.
"""
from fractions import Fraction as F
from itertools import product
from math import prod
import unittest
import numpy as np

from verification.zero_all_sector_noncommuting_sphere_test import I,X,Z,kron,active_base,output,relative_read
from verification.zero_relational_chirality_report_test import initial
from verification.zero_internal_contextual_reference_test import Bs,Zj,P,eye,value_history
from verification.zero_internal_reference_subject_valence_candidates_test import b_project,j_project
from verification.zero_sphere_local_constitution_echo_test import pulse_labels
from verification.zero_persistent_sphere_subject_selection_test import Q,norm2


def spin(j2):
    """Spin j=j2/2 in descending Jz eigenbasis."""
    j=j2/2;ms=np.arange(j,-j-1,-1);n=j2+1
    jp=np.zeros((n,n),complex)
    for k,m in enumerate(ms):
        if k>0:jp[k-1,k]=np.sqrt((j-m)*(j+m+1))
    jx=(jp+jp.conj().T)/2
    return jx,np.diag(ms)


def pinching_by_energy(a,energies):
    return a*(np.abs(energies[:,None]-energies[None,:])<1e-12)


def cnot(n,control,target):
    u=np.zeros((2**n,2**n),complex)
    for bits in product((0,1),repeat=n):
        out=list(bits);out[target]^=bits[control]
        i=sum(v*2**(n-1-k) for k,v in enumerate(bits))
        o=sum(v*2**(n-1-k) for k,v in enumerate(out));u[o,i]=1
    return u


def avg(w,a,n):
    out=np.zeros_like(a,dtype=complex);u=np.eye(len(a),dtype=complex)
    for _ in range(n):
        out+=u@a@u.conj().T/n;u=w@u
    return out


class PageWoottersOriginalSphereTests(unittest.TestCase):
    def test_original_spin_clock_exact_probabilities_and_mean(self):
        for j2 in (1,2,3,4,6,8):
            j=F(j2,2);jx,jz=spin(j2);d=j2+1
            vals,vec=np.linalg.eigh(jx);v=vec[:,-1];p=np.outer(v,v.conj())
            psi=np.kron(v,v);rho=np.outer(psi,psi.conj())
            energies=(np.diag(jz)[:,None]+np.diag(jz)[None,:]).ravel()
            twirl=pinching_by_energy(rho,energies)
            clock=kron(p,np.eye(d));joint=kron(p,p)
            den=np.trace(twirl@clock).real
            same=np.trace(twirl@joint).real/den
            # Eq. 15: product_{l=1}^{2j} [1-1/(4l-2)^2].
            exact=prod((F(1)-F(1,(4*l-2)**2) for l in range(1,j2+1)),start=F(1))
            self.assertAlmostEqual(same,float(exact),places=12)
            avg=np.trace(twirl@kron(p,jx)).real/den
            self.assertAlmostEqual(avg,float(2*j*j/(2*j+1)),places=12)
            self.assertGreater(same,1/np.sqrt(2))
        self.assertEqual(prod((F(1)-F(1,(4*l-2)**2) for l in range(1,2)),start=F(1)),F(3,4))
        # Paper's large-j limit: exact-max outcome tends to 1/sqrt(2),
        # although the mean fraction E[Jx]/j tends to one.

    def test_twirl_joint_not_product_and_energy_zero_purification(self):
        p=(I+X)/2;p1=kron(p,I);p2=kron(I,p);both=p1@p2
        energies=np.array([1,0,0,-1]);psi=np.ones(4)/2;rho=np.outer(psi,psi)
        one=pinching_by_energy(p1,energies);two=pinching_by_energy(p2,energies)
        joint=pinching_by_energy(both,energies)
        np.testing.assert_allclose(one@two,np.eye(4)/4,atol=1e-13)
        self.assertGreater(np.linalg.norm(joint-one@two),.3)
        self.assertAlmostEqual(np.trace(rho@joint).real,3/8,places=13)
        self.assertAlmostEqual(np.trace(rho@one).real,1/2,places=13)
        self.assertAlmostEqual(np.trace(rho@joint).real/np.trace(rho@one).real,3/4,places=13)
        # Exact finite counterpart purification for the dephased two spins.
        # The reference has energies -1,0,+1; this stipulated signed
        # Hamiltonian is not itself objective cosmological energy.
        refE=np.array([-1.,0.,1.]);v=np.zeros(12,complex)
        for k,energy in enumerate(energies):v[3*k+int(1-energy)]=psi[k]
        total=(energies[:,None]+refE[None,:]).ravel()
        np.testing.assert_allclose(total*v,0,atol=1e-13)
        pure=np.outer(v,v.conj())
        reduced=np.trace(pure.reshape(4,3,4,3),axis1=1,axis2=3)
        np.testing.assert_allclose(reduced,pinching_by_energy(rho,energies),atol=1e-13)
        self.assertAlmostEqual(np.trace(pure@pure).real,1,places=13)
        # Stationary mixed and definite-energy states on the SAME Hilbert
        # space need not agree on all stationary effects.
        mixed=I/2;up=np.array([[1.,0.],[0.,0.]]);energy_up=up
        self.assertAlmostEqual(np.trace(mixed@energy_up).real,.5,places=13)
        self.assertAlmostEqual(np.trace(up@energy_up).real,1,places=13)
        np.testing.assert_allclose(energy_up@Z,Z@energy_up,atol=1e-13)

    def test_actual_echo_joint_relation_all_16_old_histories(self):
        # This is the original W-history's actual Born state. The echo
        # operator identities were established on valid P; recheck them.
        t=kron((eye+Zj)/2,I)+kron((eye-Zj)/2,X)
        echo=t@kron(Q,I)@t;valid=kron(P,I)
        np.testing.assert_allclose(valid@echo@kron(Zj,I)@echo@valid,
                                   valid@kron(Bs@Zj,I),atol=1e-13)
        self.assertLess(np.linalg.norm(valid@(kron(Zj,I)@echo@kron(Zj,I)@echo-
                                              echo@kron(Zj,I)@echo@kron(Zj,I))@valid),1e-12)
        base=output(active_base());target={(1,1):.5,(1,-1):.25,(-1,1):.25,(-1,-1):0.}
        for label in range(16):
            x=initial(relative_read(base,4,labels=(label,))[0]);mass=norm2(x)
            table={key:0. for key in target}
            for s,b,z in product((1,-1),repeat=3):
                v=b_project((x+s*value_history(x))/2,b);v=j_project(v,z)
                table[z,b*z]+=norm2(v)/mass
            for k in target:self.assertAlmostEqual(table[k],target[k],places=12)
        # Commuting transported observables, not independently unmeasured
        # hidden trajectory. A practical joint readout remains additional.

    def test_relational_average_and_two_time_echo_on_cyclic_clock(self):
        # Reduced B,j,echo representation of the valid label action, not
        # a dense construction of the full quantum sphere/reservoir state.
        T=cnot(3,1,2);Qb=cnot(3,0,1);g=[np.eye(8,dtype=complex) for _ in range(20)]
        g[7:13]=[T,Qb,T,T,Qb,T];us=[np.eye(8,dtype=complex)]
        for a in g:us.append(a@us[-1])
        np.testing.assert_allclose(us[20],np.eye(8),atol=1e-13)
        for b,z,r in product((0,1),repeat=3):
            for u,name in ((T,'T'),(Qb,'Q')):
                v=np.zeros(8);v[4*b+2*z+r]=1
                zp,rp=pulse_labels(b,z,r,name)
                self.assertAlmostEqual(abs((u@v)[4*b+2*zp+rp]),1,places=13)
        n=20;d=8;w=np.zeros((n*d,n*d),complex)
        for t,a in enumerate(g):w[((t+1)%n)*d:((t+1)%n+1)*d,t*d:(t+1)*d]=a
        np.testing.assert_allclose(np.linalg.matrix_power(w,n),np.eye(n*d),atol=1e-13)
        j=kron(I,Z,I);flag=kron(Z,I,I);clock0=np.zeros((n,n));clock0[7,7]=1
        # Build relational observables via dressed-block theorem; average
        # a single anchor directly as an independent group-average check.
        def rel(t,a):
            out=np.zeros((n*d,n*d),complex);back=us[t].conj().T@a@us[t]
            for k in range(n):out[k*d:(k+1)*d,k*d:(k+1)*d]=us[k]@back@us[k].conj().T
            return out
        r7=rel(7,j);r10=rel(10,j)
        np.testing.assert_allclose(w@r7,r7@w,atol=1e-13)
        np.testing.assert_allclose(w@r10,r10@w,atol=1e-13)
        np.testing.assert_allclose(r7@r10,r10@r7,atol=1e-13)
        np.testing.assert_allclose(n*avg(w,kron(clock0,j),n),r7,atol=1e-13)
        np.testing.assert_allclose(avg(w,kron(clock0,np.eye(d)),n),np.eye(n*d)/n,atol=1e-13)
        ff=kron(np.eye(n),flag);np.testing.assert_allclose(w@ff,ff@w,atol=1e-13)
        p0=(np.eye(n*d)+ff)/2;p1=(np.eye(n*d)-ff)/2
        a=kron(clock0,kron(X,I,I))
        dep=lambda m:p0@m@p0+p1@m@p1
        np.testing.assert_allclose(dep(avg(w,a,n)),avg(w,dep(a),n),atol=1e-13)
        # Coherent realization of the same valid-support b,z distribution.
        psi=np.zeros(d,complex);psi[0]=np.sqrt(.5);psi[4]=.5;psi[6]=.5
        hist=np.concatenate([u@psi for u in us[:-1]])/np.sqrt(n)
        np.testing.assert_allclose(w@hist,hist,atol=1e-13)
        vals={(1,1):.5,(1,-1):.25,(-1,1):.25,(-1,-1):0.}
        for (x,y),prob in vals.items():
            effect=(np.eye(n*d)+x*r7)@(np.eye(n*d)+y*r10)/4
            self.assertAlmostEqual(np.vdot(hist,effect@hist).real,prob,places=12)
        self.assertAlmostEqual(np.vdot(hist,r7@r10@hist).real,0,places=12)

if __name__=='__main__':unittest.main()
