# Additive dynamics, zero balance and an exact diamond radius

**Constructive continuation:** [the relational selector and conserved transfer](ZERO_RELATIONAL_CONSTITUTION_TO_CONSERVED_RECORD_TRANSFER.md) uses a specified joint state-sensitive Hamiltonian, outside the channel-only composition-additive assumptions, to select the sphere state and correlate its records with conserved transfers. This does not derive that Hamiltonian or experience from zero.

## Result and scope

Amin Abaee's [No-Go Theorem for Additive Dynamics on Decorated Quantum Channels](https://doi.org/10.5281/zenodo.21808030), v1 (2026), addresses a specific universal **scalar action on channels**, additive under serial composition. It does not rule out a conserved signed quantity, a Hamiltonian, the sphere model, or the user's proposal that a zero whole differentiates internally. Its classification nevertheless sets a useful design constraint: a universal, channel-only action with those axioms cannot select the joint organization we seek.

There is also a mathematical correction to the preprint's remark after Lemma 5.2: **the certified diamond radius 2/d² is the exact geometric in-radius**, for every d ≥ 2, not strictly smaller than it. The bound in Theorem 5.3 remains valid; exactness of the in-radius does not prove that the compression bound is the optimal coding error. A proof and checks are below. This is an independent analysis, not a claim that the author has accepted the correction.

Source: the DOI record and [PDF](https://zenodo.org/records/21808030/files/paper_B_corrected.pdf?download=1), especially §§3–6 and the remark immediately following Lemma 5.2. The public record gives PDF MD5 `a88a0e7a578b8b16459304ef95f56edc` and TeX MD5 `7ec6a4da5ccdea72715786ee8b954fe4`. The supplementary ZIP was listed but not downloaded or run. The focused independent checks are in [the standard-library test](verification/abaee_additive_dynamics_audit_test.py); this is not a complete proof or code audit of the preprint.

## 1. Why the valuation becomes a boundary term

For ordinary finite-dimensional CPTP channels, assume a real g for **every** channel and g(Ψ∘Φ)=g(Ψ)+g(Φ). Let !A be the unique trace-discard A→I, and set h(A)=g(!A). Since every trace-preserving Φ:A→B satisfies !B∘Φ=!A,

    g(Φ) + h(B) = h(A),   hence   g(Φ) = h(A) − h(B).

This elementary proof does not require continuity, local-unitary invariance or tensor additivity. It is the availability of discards in the domain and the demand of exact composition additivity for all such maps that eliminate channel dependence. In particular every endochannel has g=0, including identity, decoherence, a recording interaction, and a nontrivial unitary.

The paper decorates A→B by an environment E and a channel Φ:A⊗E→B; environments multiply under composition. Its Theorem 4.3 derives

    s(E,Φ) = f(dim E) + h(A) − h(B).

The proof additionally uses arbitrary preparations, discards and the relevant composition law. With the paper's tensor additivity and trivial-environment normalization, h vanishes and f(mn)=f(m)+f(n). Monotonicity yields c log d with c≥0; alternatively a continuous multiplicative-additive extension to positive reals yields c log d with real c. Without dimension regularity, f can assign independent real weights to primes. In a dimension-varying variational problem the paper describes the cases c>0, c=0, c<0; the negative case belongs to the continuous-extension alternative, not the monotone-nondecreasing one. Fixed dimensions instead give a channel-independent constant on that component.

**Precision about escapes.** Dropping refinement additivity, or restricting the category so that the required preparation/discard composites are not all available, genuinely evades the classification. Non-edge-local, interacting or state/history-dependent actions likewise lie outside its assumptions. Dropping LU invariance alone or Choi continuity alone does **not** restore nontrivial channel dependence while retaining universal composition additivity and the discard/preparation argument. The paper's §6 lists these as possible escape routes, but relaxing either axiom in isolation is insufficient for this particular classification. Likewise, varying the poset or category does not automatically evade the local lemma on every fixed category where its premises continue to hold; one must say which premise changes.

## 2. Additive action is not conserved energy or experience

A conserved observable is a function of a *state and physical subsystem*, not necessarily a scalar attached to the bare channel. In a two-qubit example take N=|1⟩⟨1|, H=N⊗I+I⊗N and U=SWAP. The unitary commutes with H. On |10⟩, the two local changes are −1 and +1; on |01⟩, the **same U** gives +1 and −1. The whole change is zero in either case. No channel-only scalar can encode both local changes; in fact its value on this endochannel would be zero. This is compatible with the earlier [energy-exchange construction](ZERO_SECTOR_CONSERVED_ENERGY_RECORD_DYNAMICS.md), not a derivation of it.

For state-labelled histories, ΔE=E(ρout)−E(ρin) is additive over compatible sequential segments and telescopes. That is a boundary term on the richer state-labelled category, not an action that selects a nontrivial channel by itself. Energy conservation in the closed example concerns the total observable; it does not require the paper's normalized scalar action, and positive bare qubit energy is not a demonstrated global zero.

This distinction gives the point/sphere thesis a precise constructive direction: zero can be an invariant **of the whole joint state or conserved total**, while local differences and correlations carry its internal differentiation. It is not enough to declare an additive number on isolated process arrows. For experience, the analogous signed quantity and its actual subject-incidence measure must be justified, rather than identifying an energy current with felt valence. A negative felt experience is real for its subject; a formal positive counterterm would not erase that suffering. No preferred fundamental foliation is introduced here. The state/history examples use a specified finite clock or sequential circuit and are not a relativistic spacetime model.

## 3. Purity and the finite sphere: distinguish structure without pretending it is experience

For a normalized Choi state on input H⊗E and output K with TP marginal ρHE=I/(dH dE), the paper gives four independent nonconstant quadratic local-unitary invariants: purities QK, QHK, QEK and QHEK, for all three dimensions ≥2. Independence and spanning at this degree are not classification of all LU orbits or complete parametrization of channels. The amplitude-damping example in the paper shows that factor purities alone do not determine composite purity: equal-purity preparations |0⟩ and |+⟩, followed by damping at γ=1/2, give output purities 1 and 7/8. Our test reproduces these two values, not the full invariant-classification proof.

The previously constructed [tetrahedral zero reference](FINITE_SPHERE_ZERO_REFERENCE_AND_SYMMETRIC_RECORDS.md) illustrates why relational information matters. Its invariant recorded state |Ω⟩ and the previously specified distinct invariant |Ω₀⟩ have identical reference-label statistics, exact opposite record-operator balance and each local A and B marginal I/2. Yet their AB reduced purities are respectively 1/3 and 1. These are **state** purities, not the paper's four Choi invariants; the comparison is structural, not an identification of the two classifications. It independently reinforces that symmetry, zero, and individual marginals do not select the internal relation. Even AB purity is not a subject rule, a unique dynamics, or an experiential quality; both states already depend on a stipulated Hilbert space and representation. Thus the proposed whole remains a substantive target, not established by this distinction.

## 4. Continuous universal compression

For d-dimensional E, the real affine dimension of all CPTP E→E channels is D=d⁴−d². If the encoder from that entire channel body into a memory state space is continuous and the latter embeds into R^r with r<D, Theorem 5.3 gives

    sup_Φ ||Dec(Enc(Φ)) − Φ||⋄ ≥ 2/d².

The decoder may be arbitrary, even discontinuous, but must output channels. For an m-dimensional quantum memory, r=m²−1, so the condition is m²−1<d⁴−d². In particular for qubits d=2, D=12, m≤3 is covered and the unhalved diamond-norm error is at least 1/2. This is a worst-case lower bound for coding **every** channel, not a statement about each channel, a finite reference alphabet, physical programming capacity, or diamond distance divided by two. It uses Borsuk–Ulam and an ambient ball around the depolarizing channel; the finite-query encoder is continuous under the paper's specified comb setup. The result does not say that all finite memories fail, nor that attaining this bound is possible.

Our four-direction tetrahedral reference implements a stipulated restricted controlled interaction; it is not a continuous encoder for all qubit channels, and has never established a universal evaluator. The earlier [currying audit](ABAEE_NO_UNIVERSAL_PROCESS_CURRYING_SPHERE_AUDIT.md) distinguishes finite exact universal evaluation, abstract coding, and approximate direction resolution. The finite sphere model is consequently not a counterexample to this theorem, and this theorem is not a no-go for that restricted construction.

## 5. Exact geometric in-radius: an explicit correction

Work in the affine space of Hermiticity-preserving trace-preserving linear maps, equipped with the **unhalved** diamond norm. Let Ω(X)=Tr(X)I/d. Lemma 5.2 proves that every affine perturbation Δ of Ω with ||Δ||⋄≤2/d² is CPTP. The paper then asserts that the *true geometric* in-radius is strictly larger. We show the reverse inequality, so the lemma's bound is exact.

For d≥2 let U=diag(1,ω,…,ω^(d−1)), ω=e^(2πi/d), and write 𝒰(X)=UXU†. Define the trace-annihilating, Hermiticity-preserving map Ψ=id−𝒰, and

    Φ_t = Ω + t Ψ.

On a normalized maximally entangled vector |Φ⟩=(1/√d)Σj|j j⟩, set |Φ_U⟩=(I⊗U)|Φ⟩. Their inner product is Tr(U)/d=0. The normalized Choi matrix is

    Ĵ(Φ_t) = I/d² + t (P−Q),
    P=|Φ⟩⟨Φ|,   Q=|Φ_U⟩⟨Φ_U|.

P,Q are orthogonal rank-one projectors; the eigenvalues are 1/d²+t, 1/d²−t, and 1/d² on the remaining d²−2 dimensions. Their output partial traces are both I/d, so the affine TP constraint holds for every t. At t=1/d² the Choi matrix is positive with a zero eigenvalue, hence Φ_t is a channel on the boundary. For any t>1/d² it has a negative eigenvalue and is not completely positive.

Because the maximally entangled input produces P−Q with trace norm 2, ||Ψ||⋄≥2; the triangle inequality and unit diamond norms of channels give ||Ψ||⋄≤2. Therefore ||Ψ||⋄=2. The boundary channel is at diamond distance exactly 2/d² from Ω, and non-CPTP affine maps occur at distances arbitrarily close above it. Combined with Lemma 5.2, the geometric in-radius is **exactly 2/d²**, including the closed ball. This proof is independent of a solver and works for all d≥2. It is not based on the paper's id−Ω direction, which does not establish the claimed strict improvement.

A concrete qubit instance is U=Z and Φ=(2 id+Ad_X+Ad_Y)/4. It is a valid Pauli channel with normalized Choi eigenvalues (1/2,1/4,1/4,0) and diamond distance 1/2 from Ω; extending the same perturbation even slightly is not CP. The regression tests check normalized Choi states, trace-preserving marginals, boundary rank and negative beyond-boundary eigenvalue for small d; the all-d conclusion and diamond norm rely on the analytical argument above, not numerical estimation. This correction does not disprove the compression floor: the same 2/d² remains valid. Nor does it establish optimality of that floor as a function of memory size.

## 6. Consequence for the programme

The combined result is stronger than simply dismissing the no-go: **universal process-additive scalar action cannot, under these assumptions, explain why the whole has this internal pattern**, while an actual conserved joint quantity can still support nonzero, opposing local transfers. Relational structure can distinguish equally balanced candidates; it must be part of the proposed constitution or dynamics, not smuggled in as an arbitrary edge scalar. A serious next step is to formulate and discriminate a symmetry-respecting joint state/history principle that selects the relational organization *and* supplies independently justified subject and signed experiential incidence, while recovering the quantum and emergent-spacetime constraints. The current paper supplies neither a no-go nor a derivation of that experiential bridge. The user's thesis that zero's own constitution achieves this remains the proposed explanation, not something established or refuted by the channel theorem.
