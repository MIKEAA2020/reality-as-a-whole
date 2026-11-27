# Modular flow to Schrödinger dynamics: an analytical gate

## Why this is a priority

The analytical route is not subsidiary to detector engineering. The [Lighthouse v2.2](https://github.com/MIKEAA2020/arena-max--physics/blob/703239cb9849bec4e2d23a414db63d500be4ad2e/v2.2/Lighthouse-and-Plan-v2.2.md), §15.7, names T4/WP5: an effective Hamiltonian from a cocycle-perturbed restricted flow, with a controlled limit, **on the crossed-product algebra**. G9 names potential nonexistence of the cocycle derivative as a blocking risk. The original order puts WP0 first, but that is a proposed schedule, not a mathematical reason to defer WP5. The present calculation is a finite-dimensional analytical control for WP5, not the crossed-product or semiclassical theorem.

Existing results are stronger than a bare proposal: [RELATIONAL_MODULAR_CLOCK.md](RELATIONAL_MODULAR_CLOCK.md) has an exact constrained finite history with matching conditional and modular dynamics, including an if-and-only-if Gibbs condition; [FRW_MODULAR_CLOCK.md](FRW_MODULAR_CLOCK.md) derives an FRW scalar-clock Hamiltonian before applying a finite regulator and proves a continuum normal-state obstruction. [MODULAR_CLOCK_SELECTION.md](MODULAR_CLOCK_SELECTION.md) derives translations from an infinite modular inclusion rather than identifying dilation directly with translation. These are partial analytical results, not a completed semiclassical derivation.

## 1. Exact correspondence, with conventions and physical inputs visible

Let H be self-adjoint on a finite-dimensional system Hilbert space, β>0 and ρ₀=e^(−βH)/Z faithful. Use σ_s(A)=ρ₀^(is) A ρ₀^(−is) and U(t)=e^(−iHt/ħ). Then

    σ_s(A) = e^(−iβsH) A e^(iβsH) = U(t)† A U(t),   t=−βħs.

For any initial density operator r, not necessarily ρ₀, duality gives r(t)=U(t)rU(t)† and

    iħ ∂ₜr(t) = [H,r(t)].

For an initial pure vector, iħ∂ₜ|ψ(t)⟩=H|ψ(t)⟩ (up to an irrelevant scalar energy/phase). Although the reference Gibbs state is stationary, a different state r with energy coherences and observables not commuting with H evolve nontrivially. The modular parameter s is dimensionless; β and the clock map supply its physical scale and orientation. This is exact and valid at all t. It does **not** derive H, β, the system split, a gravitational clock, or a semiclassical limit: the Gibbs preparation already encodes the target dynamics. The existing relational-history construction links the flow to an independently specified clock only under its displayed matching assumptions.

## 2. Controlled noncommuting perturbation and cocycle

On the same finite space let H,V be arbitrary Hermitian matrices, ε real, β,ħ>0. Define the faithful states

    ρ₀ = exp(−βH)/Z₀,     ρ_ε = exp[−β(H+εV)]/Z_ε,
    u_ε(s) = ρ_ε^(is) ρ₀^(−is).

No commutation of H and V is assumed. The cocycle satisfies u(s+r)=u(s) σ⁰_s(u(r)), and σ^ε_s(A)=u(s)σ⁰_s(A)u(s)†. It is norm differentiable, with

    u′_ε(0) = i(logρ_ε−logρ₀)
              = −iβεV − i log(Z_ε/Z₀) I.

The scalar term affects no observable. In physical time t=−βħs the corresponding exact Hamiltonian is H+εV; this is a bounded, self-adjoint cocycle correction. Thus the finite analogue of G9 is explicitly passed under these hypotheses. It does not establish differentiability in the type II/III crossed product.

Set U_ε(t)=exp[−i(H+εV)t/ħ] and U₀(t)=exp(−iHt/ħ). Duhamel's identity and unitarity yield

    ||U_ε(t)−U₀(t)|| ≤ |t ε| ||V||/ħ,
    ||U_ε(t)† A U_ε(t) − U₀(t)† A U₀(t)||
        ≤ 2 |t ε| ||V|| ||A|| / ħ,
    ½ ||U_ε(t) r U_ε(t)† − U₀(t) r U₀(t)†||₁
        ≤ |t ε| ||V|| / ħ,

for every A and density operator r. The bounds remain valid with an arbitrary reference/ancilla (tensor identities); they may be capped at their trivial maxima. Consequently any single common POVM's outcome distributions, **including a no-reading effect if supplied**, differ in total variation by at most the last bound. No particular measurement or post-measurement instrument is constructed by this statement. For |t|≤T and fixed ||V||, the error is O(εT). This is a genuine norm-controlled limit as ε→0, but ε is merely a perturbation parameter: calling it semiclassical requires an independently specified semiclassical family and physical justification of its scaling.

A concrete noncommuting test is H=(E/2)σ_z, V=vσ_x, E,v≠0. The Gibbs reference is tilted in the x–z plane; the effective Hamiltonian has frequency scale sqrt((E/2)²+ε²v²), not merely shifted diagonal energies. The [verification script](verification/lighthouse_modular_schrodinger_gate_test.py) checks the exact cocycle, signs, noncommutation, estimate, stationary Gibbs state and the following restriction failure. The proof above, not finite numerical sampling, establishes the bound.

## 3. A restriction is not automatically a subsystem flow

For two qubits take K=σ_x⊗σ_x and the observable algebra N=M₂⊗I. For A=σ_z⊗I, conjugation by exp(i tK) produces a nonzero σ_y⊗σ_x term for generic t (coefficient proportional to sin 2t), hence leaves N. A global automorphism restricted as a map N→M₄ is therefore not generally an automorphism of N. One must prove invariant-subalgebra/conditional-expectation hypotheses, or instead specify a reduced channel, which need not be unitary. A cocycle relation on one algebra also does not, by itself, identify physically different gravitational clock-dressed algebras, their domains, or interventions. This is a technical gate on the formulation of WP5, not a proof that WP5 fails.

## 4. What a genuine semiclassical WP5 result would require

Choose one gravitational or crossed-product model and physical subsystem algebra; provide a state family ω_ε and embeddings to a common comparison algebra/domain, identify an independently justified semiclassical parameter and internal clock calibration t_ε(s), and prove the chosen (possibly cocycle-perturbed) action is well-defined on the relevant observables. Establish strong differentiability on a common invariant core or another precise generator notion, self-adjointness of the effective Hamiltonian, and controlled convergence of the actual flows/conditional predictions to Schrödinger dynamics on a stated time interval. Give an explicit bound including clock-calibration and gravitational/semiclassical remainder terms, and identify when it fails (turning points, nonfaithfulness, noninvariant subalgebras, loss of domain control, etc.). Show the Hamiltonian agrees with independently obtained canonical dynamics; a WKB/Born–Oppenheimer derivation on its own is not automatically a modular derivation. Then test the appropriate GR/proper-time and multi-clock observables. The finite norm result above is a benchmark, not evidence these infinite-dimensional hypotheses hold.

The FRW example shows why regulator removal matters: e^(−βh) for the continuous positive-momentum branch is not trace-class, so the finite Gibbs density cannot simply be carried to the full B(H) continuum. This does not rule out KMS states on other algebras. A faithful trace has trivial modular automorphisms; literal identification of a trace with the nontrivial time-generating state therefore requires amendment, but nontracial and relative constructions remain possible.

## 5. Coverage, chess and the requested conversations

A successful WP5 theorem could recover a physically calibrated quantum evolution in its stated regime and substantially address the problem of time. If the same theorem also derives clock observables, records, finite-device instruments, frame changes and gravity corrections with bounds, those items would be covered too. They are not automatic consequences of the Schrödinger equation alone. In particular an instrument involves outcome probabilities *and post-measurement maps*; the bound above covers only probabilities for a specified common POVM. The previous cursor construction is an optional operational probe, not a prerequisite for an analytical derivation. Neither route by itself derives an entropy arrow, unique physical time, or subjective experience.

**Source correction after user re-upload:** The user supplied [DeepSeek-Claude time reconciliation critique.txt](sources/uploads/DeepSeek-Claude%20time%20reconciliation%20critique.txt), SHA-256 `a6d47ada9edda469b430419dd8700c4c1775c1c544a9ab266d9debd169d1492c`, a 142-message source conversation. Selected passages were read directly; this is not a line-by-line audit of its 1 MB. The [v2.0 consolidation](https://github.com/MIKEAA2020/arena-max--physics/blob/703239cb9849bec4e2d23a414db63d500be4ad2e/clues/clue-04-time-without-external-clock-v2.0.md) clearly summarizes this conversation: it identifies 142 messages and its opening critique, chess and sphere, the modular research programme and the retraction. Previously we read that consolidation but failed to trace it back to the named original, and our search did not establish whether an earlier session attachment was inaccessible or overlooked. The current copy is preserved locally. See [source correction and focused review](LIGHTHOUSE_CLAUDE_TIME_CHAT_SOURCE_CORRECTION.md).

In the original chat, the user explicitly sets the players' proper time **aside**, not out of existence, to examine intrinsic half-move intervals; the sphere/room analogy illustrates confinement to admissible internal paths. In this view the notation-only game does not contain the players' elapsed durations. The assistant initially mishandled this distinction and later corrected it. The user subsequently asked for the modular-to-Schrödinger derivation, identified as T4 in the conversation's final architecture. The chat later retracts an apparent metaphysical derivation and a proposed locality lemma. Chess supplies motivation, not by itself a Hamiltonian; the analogy also does not prove that physical time requires a primitive discrete move sequence.

A separate accessible [DeepSeek time-as-output transcript](https://github.com/MIKEAA2020/arena-max--physics/blob/703239cb9849bec4e2d23a414db63d500be4ad2e/clues/clue-09-deepseek-time-as-output.md) asks whether time can be an output for creatures. It distinguishes emitted clock order from the generator's own step index; that supports the distinction between emergent readings and a presumed meta-time, not an assertion that modular flow is already physical duration. The related [assessment](https://github.com/MIKEAA2020/arena-max--physics/blob/703239cb9849bec4e2d23a414db63d500be4ad2e/v2.2/assessments/time-as-output-review.md) criticizes several transcript inferences, including taking cycles of machine states to mean cyclic time. Its stronger claim that the modular programme is the *only* meta-time-free account is not established here. The user has now supplied the separately named [chess-move-number chat](sources/uploads/DeepSeek_Chess-move-number-time_20261127-0610.txt); its [audit, steelman and analytical implementation](CHESS_TIME_AUDIT_STEELMAN_AND_IMPLEMENTATION.md) corrects that chat's erroneous proposed cocycle invariant and develops a controlled index-to-dynamics limit.
