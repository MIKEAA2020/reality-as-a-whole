# Relational dynamics in one stationary constrained state

## 1. Constructive target and result

The [infinite coherence construction](INFINITE_COHERENCE_CONSTRUCTION.md) determines a stationary algebraic state. Here we add a precise internal clock relation without treating that state's mathematical construction as a process occurring in an external time.

The result is an exact class of constrained models in which:

1. one global state is annihilated by a positive constraint;
2. clock-conditioned states undergo nontrivial unitary transport;
3. the entire original observable algebra embeds faithfully into the constraint commutant;
4. these commuting, relational observables reproduce the conditioned probabilities;
5. consistency around different clock paths is determined by holonomy;
6. the construction applies to general unital C*-algebras, not just finite density matrices.

This resolves the frozen-formalism obstruction **within this specified class**. It does not solve the full problem of time in general relativity or derive the clock, causal order, metric, or experiential passage. The history-state mechanism is established Feynman-Kitaev / relational-clock mathematics; it is not claimed as a new discovery. The contribution here is an explicit proof package, its algebraic extension, and an exact continuation of the previous AKLT construction.

Executable: [relational_constraint.py](verification/relational_constraint.py). Results: [relational_constraint.json](verification/relational_constraint.json). The finite examples use rational arithmetic; the general results below are analytic.

## 2. A local propagation constraint

Let G be a finite connected graph with M>=2 vertices. Choose an orientation for each edge. Attach a system unitary U_e to an edge e:u->v. In this section the system Hilbert space S has dimension d.

A history is a vector psi in C^M tensor S, written as components psi_v. Define

    D_e psi = psi_v - U_e psi_u,
    C = sum_e D_e^* D_e >= 0.

Equivalently, the edge contributes

    (|u><u|+|v><v|) tensor I
      - |v><u| tensor U_e - |u><v| tensor U_e^*.

Positivity gives the exact equivalence

    C psi = 0  iff  psi_v = U_e psi_u for every edge.

Thus the zero-constraint equation is already a discrete relational evolution law, not merely a demand that an externally evolving state stop changing. Orientations and transports are supplied data; their physical origin is not derived by this definition.

## 3. General consistency theorem: holonomy, not mandatory flatness

Choose a root r and a spanning tree. Let P_v transport from r to v along that tree, using inverse unitaries when traversing an edge backwards; P_r=I. For every edge define its root-frame loop operator

    W_e = P_v^* U_e P_u.

Tree-edge W_e are identity. Let

    F = intersection_e ker(W_e-I).

Then the map

    J:F -> C^M tensor S,
    J phi = (1/sqrt(M)) sum_v |v> tensor P_v phi

is an isometry onto ker(C). In particular,

    dim ker(C) = dim F.

**Proof.** Tree constraints force every component to be P_v times the root component. Remaining edge constraints become W_e phi=phi. Conversely any such phi solves every edge equation. Unitarity gives ||J phi||=||phi||. These two directions exhaust the kernel.

Changing the spanning tree cannot change the physical history space: two root-to-vertex transports differ by a loop, which fixes the allowed root vectors. Changing the root gives a unitarily equivalent root space. Hence these computational choices do not select a physical history.

Nontrivial holonomy is permitted if it fixes a nonzero sector. Operator flatness is sufficient, not necessary. For a two-dimensional root space, a loop I allows dimension two, diag(1,-1) allows dimension one, and -I permits no nonzero coherent history satisfying these amplitude constraints.

The last case is instructive: -I preserves every density matrix by conjugation but fixes no nonzero vector. Consistency of transported conditional densities is therefore weaker than consistency of the full coherent amplitude history. A scalar loop phase is not automatically removable by vertex rephasing.

This is a consistency theorem for this propagation law, not a claim that all physical gauge connections or all causal-set matter models must be flat or have zero covariant derivative.

## 4. Flat case: an exact spectral solution

Suppose the transports are flat, so U_e=P_v P_u^* on every edge. Let Q be the block-diagonal unitary with blocks P_v, and L_G the ordinary graph Laplacian. Then

    C = Q (L_G tensor I) Q^*.

This determines the entire constraint spectrum from the graph. Its zero space has dimension d and its first positive eigenvalue is the graph gap lambda_2(L_G). For the three-vertex path the clock Laplacian eigenvalues are 0,1,3.

For any system density matrix rho define the single stationary history state

    rho_hist = J rho J^*
             = (1/M) sum_vw |v><w| tensor P_v rho P_w^*.

It satisfies C rho_hist = rho_hist C = 0. Consequently exp(-isC) leaves it unchanged for every auxiliary parameter s. That parameter is not introduced as physical clock time.

The probability of clock vertex v is 1/M, and conditioning on it gives

    rho_v = P_v rho P_v^*,
    rho_v = U_e rho_u U_e^*  on e:u->v.

Uniform clock weights follow here from equal-norm unitary parallel transport, not from a cosmic measure principle. A graph label is an internal clock reading; no continuum time or preferred duration is inferred.

## 5. Gauge-invariant relational observables

Clock projectors need not commute with C. Therefore conditional formulas alone are not enough to establish that their predictions have a constraint-compatible observable representative.

For a system observable A and clock vertex v define

    R_v(A) = sum_w |w><w| tensor P_w P_v^* A P_v P_w^*.

Then

    [C,R_v(A)] = 0,
    R_v(AB) = R_v(A) R_v(B),
    R_v(A^*) = R_v(A)^*,   R_v(I)=I.

The map is injective. Thus the full noncommutative system algebra survives faithfully inside the constraint commutant.

**Proof.** Conjugating by Q sends C to L_G tensor I and R_v(A) to I tensor P_v^* A P_v. They commute; multiplication, adjoints, the unit, and injectivity follow from unitary conjugation.

Moreover,

    Tr(rho_hist R_v(A)) = Tr(rho_v A).

This reproduces every conditioned expectation and hence every POVM probability, using observables that commute with the constraint. Stationarity does not make the clock-indexed family constant: different v generally give different R_v(A).

For U_wv=P_w P_v^*, the precise covariance law is

    R_w(A) = R_v(U_wv^* A U_wv).

All clock readings use one common relational algebra; no new observer or independent reality is introduced at each reading.

In the nonflat finite-dimensional case, project onto F and replace P_v^* A P_v by B_v=Pi_F P_v^* A P_v Pi_F. The corresponding block observable still commutes with C because every W_e acts identically on F and preserves its orthogonal complement. It reproduces conditioned expectations on physical states. Compression is generally completely positive rather than multiplicative: the full faithful algebra statement above is specifically the flat case. The physical root algebra is End(F).

Independent system-basis changes G_v at each clock vertex transform U_e to G_v U_e G_u^*. The block unitary diag(G_v) conjugates C, states, and observables together, preserving probabilities. This vertex-basis covariance is not a proof of invariance under every alternative physical choice of clock.

## 6. The same theorem for an infinite observable algebra

Let A be any unital C*-algebra with state omega, and let P_v be unitaries in A. The transports U_e=P_v P_u^* define a flat connection. Work in

    A_clock = M_M(C) tensor A.

No trace or global density matrix on A is assumed. The normalized column j=(P_v/sqrt(M)) satisfies j^*j=I. Define

    omega_hat(X) = omega(j^* X j).

This is a normalized positive functional because compression by j is unital and completely positive. Explicitly,

    omega_hat(|v><w| tensor a) = omega(P_v^* a P_w)/M.

The constraint lies in M_M(A), is positive, and satisfies Cj=0. Hence omega_hat(C)=0; in the corresponding GNS representation the state vector is annihilated by C. Since C is bounded here, this follows also from 0<=C^2<=||C||C.

The relational embeddings are

    R_v(a) = diag_w(P_w P_v^* a P_v P_w^*),
    omega_hat(R_v(a)) = omega(P_v^* a P_v).

They are faithful unital *-homomorphisms commuting with C, by the same matrix-algebra conjugation proof. Thus no finite-dimensional density-matrix assumption is needed for relational evolution.

This applies directly to the previous infinite AKLT algebra with P_v chosen as finite-support local unitaries. More generally it is compatible with a supplied AQFT observable algebra and state. It does **not** construct an AQFT net, physically locate the clock factor, impose Einstein constraints, or assume that a field region has a finite tensor factorization. The clock factor is an explicit internal component of the model, not an external simulator.

## 7. State preparation is not the gauge constraint

A propagation law need not select the actual root state. The earlier construction supplies a way to do so without assigning a new arbitrary table: take a finite AKLT ring Hamiltonian H_0 with its unique normalized ground vector phi_0.

In the flat case with P_r=I define a preparation parent operator

    H_prep = C + |r><r| tensor H_0.

Positivity and the kernel theorem give

    ker(H_prep) = J ker(H_0).

Hence H_prep has a unique ground ray J phi_0. This fixes a coherent history from the previous local law plus the specified transports.

If H_0 has gap Delta>0, then a sufficient finite-size bound is

    gap(H_prep) >= min{ Delta/(2M), lambda_2(L_G)/(2M+1) }.

**Proof.** Conjugate by Q and resolve the H_0 eigenspaces. In its zero sector the operator is L_G. In a sector E>=Delta it is L_G+E|r><r|. Write f=a 1/sqrt(M)+g with g orthogonal to the constant vector. Since a=sqrt(M)(f_r-g_r),

    ||f||^2 <= 2M |f_r|^2 + (2M+1)||g||^2
             <= (2M/Delta) E|f_r|^2
                + [(2M+1)/lambda_2] <f,L_G f>.

The claimed lower bound follows. No unproved spectral gap for an infinite Hamiltonian is used here.

Crucially, R_v(A) generally commutes with C but **not** with H_prep. The latter specifies preparation, not the relational gauge generator. Conflating these roles would invalidate the observable argument. Selecting one actual state is distinct from reducing the entire physical observable algebra to operators preserving that one ray.

Likewise, keeping the system inside the same one-dimensional AKLT ground ray at every clock reading would produce no changing system density matrix. Here the changing conditional states belong to a joint constrained history; the system is not separately required to remain in that original ray at every vertex.

## 8. Exact continuation of the four-site AKLT ring

Take the previously constructed four-site ring ground vector. In its integer coefficient convention its squared norm is 21; no new initial-state table is fitted. Use three clock readings 0,1,2 and let U act only on the first qutrit by the rational orthogonal matrix

    R = [[3/5, 0, -4/5],
         [0,   1,  0  ],
         [4/5, 0,  3/5]].

Choose P_0=I, P_1=U, P_2=U^2. The one stationary history contains the three conditional states phi_0,U phi_0,U^2 phi_0. For A=L_z(1)L_z(2), their exact expectations are

    clock 0: -10/21,
    clock 1: -2/7,
    clock 2:  2/15.

These are computed from the four-site ring, not substituted from the infinite-chain limit. Every one-site marginal remains I_3/3, so the changing two-site relation is invisible to a one-site state table.

The normalized system-vector Gram matrix is

    G = [[1,     11/15, 11/75],
         [11/15, 1,     11/15],
         [11/75, 11/15, 1    ]].

The reduced clock state is G/3 and is mixed; the joint history is entangled. The global interference observable (|0><1|+|1><0|) tensor I has expectation 22/45. Clock dephasing gives zero while leaving the individual conditioned states unchanged. It also raises the expectation of C from zero to 4/3, so the dephased state is not another physical zero-constraint history. An actual dephasing intervention would require an enlarged physical description, not an assertion that it preserves the closed constraint. Thus the construction retains more than a catalogue of conditional snapshots.

The executable also verifies a causal-diamond graph: its undirected loop can have trivial, partly fixing, or obstructing holonomy even though its edge orientation is acyclic. This gives an exact compatibility test for alternative directed routes, without claiming a causal-set dynamics or Lorentzian reconstruction.

## 9. Position reached and remaining work

**Infinite-clock continuation:** [The integer-clock construction](INFINITE_RELATIONAL_CLOCK.md) now proves the normal-state obstruction and constructs a group-averaged physical Hilbert space with coherent finite-corner states and window-independent relational probabilities. The coherent functional is not a normal weight; the original first-order transport conditions must be retained. This removes a global clock prior from the specified predictions, not the supplied clock structure or physical state.

**Sequential continuation:** [Interventions and records](RELATIONAL_INTERVENTIONS_AND_RECORDS.md) now supplies the missing sequential statistics for finite inner instruments: an explicit algebraic unitary completion, selective updates, feedback, persistent constraint-commuting record observables, and clock-refinement invariance. It distinguishes classical-record predictions from coherent implementation data needed for eraser experiments. The underlying clock/state/transport choices remain supplied.

**Constructed:** clock-relative unitary change inside one zero-constraint state; a faithful algebra of Dirac observables in the flat case; a holonomy classification in the general finite case; gauge covariance; a general C*-algebra extension; and a unique, gapped finite preparation built from the preceding AKLT law. Exact rational checks cover nontrivial changing correlations and coherence, not experience labels.

**Not derived:** why these transports, graph, clock, or preparation are actual or necessary; a continuum clock or arrow of time; unrestricted non-inner or unmodelled-memory instrument processes; arbitrary physical clock changes; the gravitational hypersurface-deformation constraint algebra; spacetime geometry; or finite qualitative ownership. A one-clock history does not by itself solve these additional problems.

This is a constructive result within physical adequacy M0 and the existing W1-W6 programme, not a new rival programme. The noncommutative observable algebra and its conditional predictions are preserved rather than replaced by a classical valuation. Normative and experiential obligations remain jointly binding.


## Clock-choice continuation

[Clock-choice equivalence](CLOCK_CHOICE_EQUIVALENCE.md) compares two noncommuting readings of the same constrained history. It proves when evaluations give unitary physical frames, checks the weighted transformed constraint and anchored record probabilities, and distinguishes failed clock conditioning from a genuine equivalent reduction. This addresses clock choice within the model, not gravitational refoliation.
