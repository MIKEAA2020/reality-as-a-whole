"""One invariant, frustration-free relational selector in the existing sphere model.

This is conditional on the specified representation, tensor factors and rules;
it does not identify records with subjects or derive experience from physics.
"""
import math
import unittest
from verification.zero_spin_constitution_test import X,Y,Z,add,close,eye,kron,mm,mv,scale,inner,rank
from verification.zero_invariant_sphere_instrument_test import adj
from verification.zero_spherical_plenitude_opposite_records_test import TETRA,op,vecnorm,initial
from verification.finite_tetrahedral_zero_reference_test import S,V,prod,outer,sub,comm,rotor,global_rotation,recorded_whole,maxabs
from verification.abaee_additive_dynamics_audit_test import ab_reduction,purity


def vadd(*vectors): return [sum(x) for x in zip(*vectors)]
def vscale(a,v): return [a*x for x in v]
def tensor(*ops):
    a=[[1]]
    for b in ops: a=kron(a,b)
    return a

def projector(v): return outer(v,v)
def pointwise_close(test,v,w): test.assertAlmostEqual(vecnorm([x-y for x,y in zip(v,w)]),0)

# C⊗AB (dimension 16), followed by two pointer qubits.
psi=[0,1/math.sqrt(2),-1/math.sqrt(2),0]
s=prod(S,psi)
t=vscale(1/math.sqrt(3),vadd(*[prod(V[k],mv(kron(sig,eye(2)),psi)) for k,sig in enumerate((X,Y,Z))]))
ps=projector(s); pt=projector(t); pinv=add(ps,pt)
g=add(outer(s,t),outer(t,s)); d=sub(ps,pt)
id2=eye(2); iz=kron(Z,id2); flip=kron(X,X)
P=kron(pinv,eye(4)); K=kron(g,iz); Q=kron(d,flip)
# Equal-record-sector projector (R=00 or 11).
Esame=scale(.5,add(eye(4),kron(Z,Z)))
# Exactly identity outside P, and three commuting unit penalties inside P.
H=add(sub(eye(64),P),add(kron(pinv,Esame),add(scale(.5,sub(P,K)),scale(.5,sub(P,Q)))))


def tetra_control():
    out=scale(0,eye(16))
    for i,n in enumerate(TETRA):
        label=[complex(j==i) for j in range(4)]
        a=add(add(scale(n[0],X),scale(n[1],Y)),scale(n[2],Z))
        out=add(out,tensor(projector(label),a,eye(2)))
    return out

def write_records(v):
    # Work qubits ordered M1,W1,M2,W2; |0,1,0,1> is the blank/charged state.
    out=[0j]*len(v)
    for base in range(64):
        ra=(base>>1)&1
        for w in range(16):
            bits=[(w>>j)&1 for j in (3,2,1,0)]
            j=0 if ra==0 else 2
            bits[j],bits[j+1]=bits[j+1],bits[j]
            dst=sum(bits[k]<<(3-k) for k in range(4))
            out[16*base+dst]=v[16*base+w]
    return out


def embed_blank(v):
    out=[0j]*(len(v)*16)
    for i,x in enumerate(v): out[16*i+5]=x
    return out


def apply_base(matrix,v):
    out=[0j]*len(v)
    for work in range(16):
        col=mv(matrix,[v[16*i+work] for i in range(64)])
        for i,x in enumerate(col): out[16*i+work]=x
    return out


def aux_penalty(w):
    m1,b1,m2,b2=[(w>>j)&1 for j in (3,2,1,0)]
    return m1+(1-b1)+m2+(1-b2)


def lifted_h(v):
    x=write_records(v)
    y=apply_base(H,x)
    y=[z+aux_penalty(i%16)*x[i] for i,z in enumerate(y)]
    return write_records(y)


class RelationalStabilizerConstitutionTests(unittest.TestCase):
    def test_irrep_basis_is_orthonormal_and_invariant(self):
        self.assertAlmostEqual(inner(s,s).real,1); self.assertAlmostEqual(inner(t,t).real,1)
        self.assertAlmostEqual(abs(inner(s,t)),0)
        self.assertEqual(rank(pinv),2)
        for u in (rotor((.2,-.3,.7),.73),rotor((1,1,1),2*math.pi/3)):
            big=global_rotation(u)
            for v in (prod(s,[1,0,0,0]),prod(t,[1,0,0,0])):
                pointwise_close(self,mv(big,v),v)
            self.assertLess(maxabs(comm(big,H)),1e-9)

    def test_direction_matching_is_compressed_physical_control(self):
        a=tetra_control()
        close(self,mm(a,a),eye(16))
        pointwise_close(self,mv(a,s),t)
        pointwise_close(self,mv(a,t),s)
        close(self,mm(mm(pinv,a),pinv),g)

    def test_scalar_vector_parity_is_AB_singlet_parity(self):
        singlet=projector(psi)
        dab=kron(eye(4),sub(scale(2,singlet),eye(4)))
        close(self,mm(mm(pinv,dab),pinv),d)
        close(self,mm(g,g),pinv); close(self,mm(d,d),pinv)
        close(self,add(mm(g,d),mm(d,g)),scale(0,pinv))

    def test_record_matching_and_coherence_commute(self):
        close(self,mm(K,K),P); close(self,mm(Q,Q),P)
        self.assertLess(maxabs(comm(K,Q)),1e-10)
        same=kron(pinv,Esame)
        self.assertLess(maxabs(comm(K,same)),1e-10)
        self.assertLess(maxabs(comm(Q,same)),1e-10)
        self.assertEqual(rank(P),8)

    def test_recorded_state_satisfies_all_three(self):
        omega=recorded_whole()
        pointwise_close(self,mv(P,omega),omega)
        pointwise_close(self,mv(K,omega),omega)
        pointwise_close(self,mv(Q,omega),omega)
        self.assertAlmostEqual(vecnorm(mv(kron(pinv,Esame),omega)),0)
        self.assertAlmostEqual(vecnorm(mv(H,omega)),0)

    def test_unique_ground_state_and_integer_gap(self):
        close(self,H,adj(H))
        # On P, all three terms are commuting projectors. On P-perp H=I.
        # Projector on simultaneous success is rank 1 and equals |Ω><Ω|.
        one=eye(64); good=mm(mm(sub(P,kron(pinv,Esame)),scale(.5,add(P,K))),scale(.5,add(P,Q)))
        self.assertEqual(rank(good),1)
        close(self,good,projector(recorded_whole()))
        # Exact spectrum lies in {0,1,2,3}; rank H = 63 and there are
        # explicit eigenvectors at eigenvalue 1, so spectral gap is 1.
        self.assertEqual(rank(H),63)
        fail=prod(s,[1,0,0,0])
        # Instead use an outside-invariant reference/AB basis vector.
        basis=[complex(i==0) for i in range(64)]
        outside=mv(sub(one,P),basis)
        self.assertGreater(vecnorm(outside),0)
        pointwise_close(self,mv(H,outside),outside)

    def test_alternative_same_zero_record_statistics_fails_direction_matching(self):
        plus=[0,1/math.sqrt(2),1/math.sqrt(2),0]
        minus=[0,1/math.sqrt(2),-1/math.sqrt(2),0]
        alternative=prod(s,minus)
        self.assertAlmostEqual(abs(inner(alternative,recorded_whole())),0)
        pointwise_close(self,mv(P,alternative),alternative)
        self.assertAlmostEqual(vecnorm(mv(kron(pinv,Esame),alternative)),0)
        self.assertAlmostEqual(inner(alternative,mv(K,alternative)).real,0)
        pointwise_close(self,mv(Q,alternative),vscale(-1,alternative))
        self.assertAlmostEqual(inner(alternative,mv(H,alternative)).real,1.5)
        # Additional failure control: switching the relative branch phase
        # preserves K and exact record zero, but flips Q.
        twisted=prod(vscale(1/math.sqrt(2),vadd(s,t)),[0,1/math.sqrt(2),0,0])
        twisted=vadd(twisted,prod(vscale(1/math.sqrt(2),vadd(s,vscale(-1,t))),[0,0,-1/math.sqrt(2),0]))
        pointwise_close(self,mv(K,twisted),twisted)
        pointwise_close(self,mv(Q,twisted),vscale(-1,twisted))
        self.assertAlmostEqual(abs(inner(twisted,recorded_whole())),0)

    def test_singlet_probability_and_relational_purity(self):
        omega=recorded_whole(); a=ab_reduction(omega)
        singlet=projector(psi)
        self.assertAlmostEqual(inner(psi,mv(a,psi)).real,.5)
        self.assertAlmostEqual(purity(a),1/3)
        expected=add(scale(.5,singlet),scale(1/6,sub(eye(4),singlet)))
        close(self,a,expected)

    def test_every_reference_record_branch_has_opposite_bloch_vectors(self):
        omega=recorded_whole()
        # Conditional joint A,B states for each reference label and record.
        for i,n in enumerate(TETRA):
            for pointer,sign in ((1,1),(2,-1)):
                ab=[omega[16*i+4*ab+pointer] for ab in range(4)]
                prob=inner(ab,ab).real
                self.assertAlmostEqual(prob,1/8)
                A=add(add(scale(n[0],X),scale(n[1],Y)),scale(n[2],Z))
                self.assertAlmostEqual((inner(ab,mv(kron(A,eye(2)),ab))/prob).real,sign)
                self.assertAlmostEqual((inner(ab,mv(kron(eye(2),A),ab))/prob).real,-sign)

    def test_controlled_writing_conserves_each_memory_battery_pair(self):
        for i in range(64):
            for work in range(16):
                v=[0j]*1024; v[16*i+work]=1
                w=write_records(v)
                j=w.index(1)
                old=[(work>>k)&1 for k in (3,2,1,0)]
                new=[((j%16)>>k)&1 for k in (3,2,1,0)]
                self.assertEqual(old[0]+old[1],new[0]+new[1])
                self.assertEqual(old[2]+old[3],new[2]+new[3])
                self.assertEqual(j//16,i)
                self.assertEqual(write_records(w),v)

    def test_joint_direction_record_and_signed_physical_transfer(self):
        v=write_records(embed_blank(recorded_whole()))
        self.assertAlmostEqual(inner(v,v).real,1)
        for base in range(64):
            for work in range(16):
                amp=v[16*base+work]
                if abs(amp)<1e-10: continue
                ra=(base>>1)&1; rb=base&1
                self.assertNotEqual(ra,rb)
                m1,b1,m2,b2=[(work>>k)&1 for k in (3,2,1,0)]
                self.assertEqual((m1,b1,m2,b2), (1,0,0,1) if ra==0 else (0,1,1,0))
                self.assertEqual(m1-m2,1-2*ra)
                self.assertEqual((b1-1)+(b2-1),-(m1+m2))
        # Verify the full coherent operator identity, not only branch values.
        weighted=[]
        for i,x in enumerate(v):
            w=i%16; m1=(w>>3)&1; m2=(w>>1)&1
            weighted.append((m1-m2)*x)
        result=apply_base(kron(tetra_control(),eye(4)),weighted)
        pointwise_close(self,result,v)
        # Writing transports the joint coherence operator with the state.
        pointwise_close(self,write_records(apply_base(Q,write_records(v))),v)
        self.assertAlmostEqual(inner(v,apply_base(Q,v)).real,0)

    def test_local_record_sign_candidate_needs_substantive_incidence_rule(self):
        v=write_records(embed_blank(recorded_whole()))
        for i,amp in enumerate(v):
            if abs(amp)<1e-10: continue
            w=i%16; m1=(w>>3)&1; m2=(w>>1)&1
            # Conditional proposal v_j=2N_Mj−1 gives opposite nonzero
            # values, but labels blank memory as negative: the mathematics
            # does not establish that either memory feels anything.
            q1,q2=2*m1-1,2*m2-1
            self.assertEqual(q1+q2,0)
            self.assertEqual(abs(q1),1)
        self.assertAlmostEqual(sum(abs(a)**2*(2*((i%16>>3)&1)-1) for i,a in enumerate(v)),0)
        self.assertAlmostEqual(sum(abs(a)**2*(2*((i%16>>1)&1)-1) for i,a in enumerate(v)),0)

    def test_lifted_selector_ground_state_and_conservation(self):
        v=write_records(embed_blank(recorded_whole()))
        self.assertAlmostEqual(vecnorm(lifted_h(v)),0)
        # H_lift=W(H⊗I+I⊗H_aux)W†. Unique ground and gap 1 follow
        # from the two unique gapped summands and W's unitarity.
        for index in (0,5,16*13+5,1023):
            x=[0j]*1024; x[index]=1
            hx=lifted_h(x)
            # H0 is diagonal and equals sum of four work occupation bits.
            e=bin(index%16).count('1')
            for j,amp in enumerate(hx):
                if abs(amp)>1e-10: self.assertEqual(bin(j%16).count('1'),e)
        # Ground bare energy H0=2; no global zero-energy conclusion follows.
        self.assertAlmostEqual(sum(abs(x)**2*bin(i%16).count('1') for i,x in enumerate(v)),2)

    def test_energy_fidelity_bound_and_no_channel_only_selection(self):
        omega=recorded_whole(); alternative=prod(s,[0,1/math.sqrt(2),-1/math.sqrt(2),0])
        for p in (0,.1,.5,.9,1):
            # Classical mixture ρ=p|Ω><Ω|+(1-p)|Ω₀><Ω₀|.
            energy=p*inner(omega,mv(H,omega)).real+(1-p)*inner(alternative,mv(H,alternative)).real
            fidelity=p
            self.assertGreaterEqual(energy+1e-10,1-fidelity)
        # H≥I−|Ω><Ω| implies this bound for every density matrix, by the
        # commuting-projector spectral decomposition, not just these samples.

if __name__=='__main__': unittest.main()
