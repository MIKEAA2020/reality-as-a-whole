# Clock-choice equivalence in one fixed constrained system

## 1. Direct problem-of-time target

This work returns explicitly to the problem of time. The recent preparation/access results are supporting mathematics, not themselves a solution of clock choice.

We construct two noncommuting clock descriptions of **one and the same constrained physical space**, prove an exact equivalence criterion, transport sequential intervention records, and exhibit a proposed clock that destroys information. The two successful descriptions are not merely a relabelling of clock vertices.

The result resolves clock-choice consistency for this specified finite constrained model and gives tests applicable to other reductions. It does not solve the general multiple-choice problem of gravitational time, derive a preferred clock, or turn a two-reading clock into an autonomous globally monotonic time variable.

Code: [clock_choice.py](verification/clock_choice.py). Output: [clock_choice.json](verification/clock_choice.json). Exact rational checks include the constraint in the new clock basis, conditional maps, frame observables and records, and failed-clock recovery.

## 2. One physical space, multiple clock evaluations

Let C>=0 be a fixed constraint on H_kin=H_clock tensor H_S. Let J:H_phys -> ker(C) be an isometry onto its kernel. The physical inner product is fixed by J, not separately chosen for each clock.

For an orthonormal clock basis {|c>}, define

    E_c=(<c| tensor I)J,
    G_c=E_c^*E_c,
    sum_c G_c=I_phys.

E_c maps a physical vector to its unnormalized conditional system vector. For physical density rho,

    p(c|rho)=Tr(G_c rho),
    rho_c=E_c rho E_c^*/p(c|rho),

when the probability is nonzero. This is a reduction of one constraint, not a replacement of C by a new Hamiltonian selected after the clock choice.

Call a reading an **ideal full-sector frame** when E_c=sqrt(w_c)V_c, with w_c>0 independent of rho and V_c unitary onto the chosen reduced system space. For equal finite physical/system dimensions this is equivalent to

    G_c=w_c I.

Proof: polar decomposition gives V_c=E_c/sqrt(w_c), with V_c^*V_c=I and, by equal dimension, surjectivity. Conversely the unitary form gives the stated G_c. For unequal or infinite spaces, an isometry alone is insufficient; specify the image or prove surjectivity.

This is a precise notion of ideal conditional frame, not a complete physical definition of a clock. Order, calibration, robust readings and clock dynamics require additional conditions.

## 3. Exact change of ideal clock frame

For any two ideal readings, possibly from different noncommuting clock bases, define

    W_(d<-c)=V_d V_c^*.

Then

    rho_d=W_(d<-c) rho_c W_(d<-c)^*,
    W_(e<-d) W_(d<-c)=W_(e<-c).

For a physical observable A on H_phys its representation is

    pi_c(A)=V_c A V_c^*.

All algebraic products, adjoints and Born expectations are preserved. This equivalence concerns the same physical/root events, not equality of the two clock-reading distributions or identity of the clock measurement instruments. The noncommuting clock observables remain distinct observables. A constraint-compatible representative on ker(C) is J A J^*, extended by zero on its orthogonal complement; it commutes with C. Thus these are representations of the **same physical observable**, not just equal numerical predictions for unrelated quantities.

If a lab operator k is attached to the old clock event n with transport P_n, its physical root operator is P_n^* k P_n. In another clock frame it must be represented by pi_d(P_n^* k P_n). Keeping the same matrix k at a newly named reading generally asks a different physical question.

### Sequential records

Let K_j be the physical/root Kraus operators of the anchored events, including their earlier transport pullbacks. In frames c_0,...,c_n define

    U_j=V_(c_j) V_(c_(j-1))^*,
    K_j^(c_j)=V_(c_j) K_j V_(c_j)^*.

The reduced chronological branch product is

    K_n^(c_n) U_n ... K_1^(c_1) U_1
        = V_(c_n) (K_n ... K_1) V_(c_0)^*.

Hence branch probabilities, sums over unresolved Kraus labels, feedback and normalized record distributions agree in the two descriptions. This is a kinematic equivalence theorem for the specified instruments. It does not independently supply the physical event order. Dropping an event or replacing it with a different intervention is not a clock transformation.

## 4. Worked noncommuting clocks

Use a qubit system and the earlier rational rotation

    U=[[3/5,-4/5],[4/5,3/5]],
    J phi=(|0> tensor phi+|1> tensor U phi)/sqrt(2),
    C=[[I,-U^*],[-U,I]].

C J=0 and C=2(I-JJ^*). The original Z-clock gives E_0=I/sqrt(2), E_1=U/sqrt(2), equal weights 1/2 and frames I,U.

Now use the X-clock |+>=(|0>+|1>)/sqrt(2), |->=(|0>-|1>)/sqrt(2). It does not commute with the old clock observable. Its evaluation maps are

    E_+=(I+U)/2=[[4/5,-2/5],[2/5,4/5]],
    E_-=(I-U)/2=[[1/5,2/5],[-2/5,1/5]].

Direct multiplication gives

    G_+=(4/5)I,  G_-=(1/5)I.

Both readings are ideal. Their unitary frames and relative transport are

    V_+=(1/sqrt(5))*[[2,-1],[1,2]],
    V_-=(1/sqrt(5))*[[1,2],[-2,1]],
    W_(-<-+)=[[0,1],[-1,0]].

The apparent two-reading transport is different from U, but anchored observables and records transform with it and retain their physical predictions. The unequal reading weights are retained; they do not become equal by declaration.

### Transform the constraint too

Let H be the clock Hadamard matrix. The same constraint in the X-coordinate description is

    C_X=(H tensor I) C (H tensor I),
    J_X=(H tensor I)J,
    C_X=2(I-J_X J_X^*).

The conditional components obey the weighted relation

    psi_- = sqrt(w_-/w_+) W_(-<-+) psi_+ = (1/2) W_(-<-+) psi_+.

Equivalently C_X=2*w_+ D^*D with D=[-(1/2)W_(-<-+), I]. Replacing this by an equal-weight path constraint would change the physical kernel. Clock-dependent weights are part of the transformed reduction, not disposable normalization conventions.

The script checks this identity without floating point, and checks the earlier two-event qubit record distribution

    [[81/625,144/625],[256/625,144/625]]

in both ideal X frames as well as the root description. Frame transformations carry the state and both Kraus operators, not just the final measurement.

## 5. When the superposed clock fails

For a general two-reading unitary U,

    G_+=(2I+U+U^*)/4,
    G_-=(2I-U-U^*)/4.

Both are nonzero ideal full-sector frames exactly when U+U^*=2cI with -1<c<1. The worked real rotation satisfies this. A general multi-frequency evolution need not.

For the sharp counterexample U=Z=diag(1,-1),

    E_+=|0><0|,  E_-=|1><1|.

The X reading probabilities depend on the physical state. Each conditional output has rank one and loses part of the physical input. The two physical states (|0>+|1>)/sqrt(2) and (|0>-|1>)/sqrt(2) give identical classical-reading/conditional-system outputs, although their original coherent histories are orthogonal. Discarding the cross-reading coherence has erased information.

There is no unitary clock-frame transformation on the whole physical qubit sector. This does not reveal inconsistent predictions by one quantum theory: the proposed reading is a state-dependent filter, not an equivalent ideal clock on that sector. Restricted-sector constructions must state their smaller domains explicitly.

## 6. Nonideal but invertible readings: metric versus physical filtering

If E is invertible but G=E^*E is not scalar, its normalized conditional map is not generally a state-independent linear quantum channel. It contains the filter G^(1/2) through E=V G^(1/2).

One can recover a mathematical isometry by equipping the image with the pulled-back physical metric

    <x,y>_phys=<x,(E E^*)^(-1)y>_S.

The transported operator E A E^(-1) is self-adjoint in that metric when A is physically self-adjoint. It is not generally self-adjoint in the ordinary system metric. Changing the inner product in a description does not remove a real conditioning filter or change the apparatus's ordinary Born rule for free.

There is an explicit physical recovery when E is invertible. Let m=lambda_min(E^*E)>0 and

    R=sqrt(m) E^(-1).

R is a contraction and R E=sqrt(m)I. Completed with (I-R^*R)^(1/2), it reverses the reading on success. Its **joint** success probability (clock outcome followed by recovery) is m for every input; conditional on the clock outcome it is m/Tr(G rho). No bounded exact universal inverse with nonzero state-independent success exists when E has a kernel.

The script checks an invertible nonideal example E=diag(3/5,4/5): m=9/25, R=diag(1,3/4), and R E=(3/5)I. This is a general filter-recovery check, not a claim that this E is the X reduction of the rotation in section 4.

## 7. Infinite clocks and modular candidates

The [infinite relational construction](INFINITE_RELATIONAL_CLOCK.md) already gives a common physical Hilbert space by rigging. Its evaluations at integer readings are the unitary transports P_n. The ideal-frame transformation and anchored-instrument theorem apply to these evaluations directly. They must **not** be normalized into a uniform probability over all integer readings; no such normal clock distribution exists. Section 2's sum of effects belongs to the finite normal history model, not a countably infinite uniform history vector.

Modularly supplied transports can likewise act as ideal frames once embedded in this common constrained model. But two modular flows built from separately chosen states/inclusions are not automatically two clock reductions of one fixed constraint. A Connes cocycle alone does not establish that equivalence. One must identify the same physical space and state, valid evaluation maps, and the corresponding anchored event algebra.

Thus the modular work has not selected physical time merely by providing automorphisms. The present result supplies a concrete equivalence test that a proposed modular clock must pass.

## 8. What is resolved and what remains

**Resolved in this class:** noncommuting ideal clock descriptions of one fixed constraint have explicit unitary frame changes, correctly weighted transformed constraints and identical anchored record probabilities. A precise evaluation-map test separates them from lossy clock conditioning; invertible imperfections have a metric treatment and a probabilistic physical recovery with stated cost.

**Not resolved:** generic interacting/gravitational clock choices, global monotonicity and turning points, continuum Hamiltonian-constraint/refoliation algebra, state/localization selection, metric calibration or a preferred physical time. The event order and finite clock-system split remain supplied. A two-reading quantum reference frame is not yet a realistic autonomous clock.

This is direct problem-of-time progress within M0/W1-W6, using established constrained-system and quantum-reference-frame mathematics. It is not a solution of quantum gravity, phenomenal passage, necessary actuality or the full no-residue account.


## Continuation: clocks with turning points

[The turning-clock atlas](TURNING_CLOCK_ATLAS.md) replaces a single global reading by orientation-resolved cosine/sine charts of a continuum periodic constrained history. It derives the coordinate weights, regular transitions and recorded probabilities through a turn, and distinguishes orientation loss from a coordinate singularity. Recurrence remains a separate global clock limitation.
