# Öttinger’s dissipative QFT: uploaded excerpt and limit audit

## Decision

**Update:** A later attachment includes the full book. See the [scalar and QED follow-up](OTTINGER_FULL_BOOK_SCALAR_QED_FOLLOWUP.md). The missing-chapter statements below describe only the earlier `qft_teaser.pdf`.

The supplied `qft_teaser.pdf` is not a paper or the complete book. It contains the front matter and Chapter 1 of Hans Christian Öttinger’s *A Philosophical Approach to Quantum Field Theory* (2017), ending **mid-sentence at printed page 109**. The later scalar-field, QED, gravity-related perspectives, appendices and bibliography listed in its contents are not included. The chapter proposes a thermodynamic quantum master-equation approach in which dissipation acts as a dynamical UV regulator; it does not, in the supplied excerpt, establish a complete interacting QFT, a unique ontology, a Planck-scale law, or a solution of the measurement problem.

A specific useful constraint follows already in the book’s **free zero-temperature equation**. Even in its invariant vacuum/one-particle sector, equilibration and removal of dissipation need not commute. With initially one quantum, the final excitation probability is zero if one equilibrates first at fixed positive damping, but one if one sets the damping to zero first. Along joint limits intermediate values occur. Moreover, damping vanishes on each fixed momentum while failing to vanish uniformly over arbitrarily high momenta. These are elementary consequences of a deliberately restricted free model—not a refutation of the book’s renormalized correlation-function proposal, which uses specified limiting prescriptions and additional structure.

## 1. Source, access and reading scope

- User-supplied `/tmp/arena-coding-uploads/qft_teaser.pdf`, SHA-256 `d4cc12e3495bdc1f7e08a0aa52ca071ac06e3fb7efe1b625a6ca77ddf7e32dba`; 120 PDF pages, including cover, front matter and printed pp. 1–109. The upload location is temporary and may not persist; the original has **not** been added to the public repository because the supplied copyright page reserves reproduction rights and no specific republication permission for this book was established. This note retains the bibliographic identification and hash, not the book text.
- Hans Christian Öttinger, [*A Philosophical Approach to Quantum Field Theory*](https://doi.org/10.1017/9781108227667), Cambridge University Press, 2017, ISBN 978-1-108-41511-8. The publisher record confirms the book and bibliographic context. Claims about chapter text below are from the **uploaded excerpt**, not a review of the complete book. Publisher record’s listings of later citing papers were not treated as reading those papers.
- We read the extracted text of all text-bearing pages of the upload. Seven image-only pages containing printed pp. 24, 77, 79, 82, 94, 95 and 97 were visually read, including their figures; the image-only cover was inspected. Printed p. 62, including eq. (1.44), was also visually checked. We did not visually inspect every other figure or verify every displayed equation against its typeset original; text extraction is imperfect for formulas. Chapter 2 starts on p. 110 and is missing; we did **not** read or reproduce its scalar-field calculations, the QED chapter, later perspectives, references or appendices.

A page number below refers to the **book’s printed page**, not the PDF index. The source is an argument for an alternative physical image, not a statement of settled consensus. Attributions to Kant, Boltzmann, other philosophers or earlier physics are the book’s unless independently checked; this audit does not certify its historical interpretation.

## 2. The proposed physical image

Öttinger regards mathematical theories as revisable images constrained by empirical success and motivates four *guiding metaphysical postulates*, not four mathematical theorems (pp. 2–3, 10, 18, 21, 24):

1. mathematical consistency and elegance;
2. space and time as prerequisites for physical descriptions, rather than necessarily things whose emergence must be explained by the theory;
3. treatment of infinities through limiting procedures, with countability restrictions;
4. naturally arising irreversible terms in the relevant quantum-field evolution.

The second postulate and the project’s investigation of a timeless self-sufficient whole are **different foundational commitments**. A local dynamical parameter can be used as an internal ordering within a larger timeless description, but that alone neither establishes Öttinger’s background-space proposal nor derives the project’s spacetime. Neither is automatically ruled out by the other.

In the concrete scalar illustration (pp. 48–49, 57–69), the author starts with finite-volume, finite momentum-mode Fock space, a free Hamiltonian plus collisions, and a heat-bath-type nonlinear density-matrix evolution. He introduces a temperature and momentum-dependent dissipation. A representative ansatz is

```text
γ_k = γ_0 + γ |k|^4,       ℓ_γ = γ^(1/3),       ħ = c = 1.
```

The latter length follows from the dimensions of this **chosen** rate; it is not a measured cutoff or a deduction of the Planck length. The author expects large momenta to relax rapidly and the dissipative regulator to control short-scale behavior. He explicitly treats fast-mode elimination and effective autonomous thermodynamics, including extension to self-similar systems without a clean time-scale gap, as assumptions (pp. 28–30, 81). Uncontrolled fast degrees do not logically entail a memoryless bath or a unique dissipator.

The full finite-temperature equation is generally **nonlinear** in the density operator. The book derives a free-theory linear form, an equilibrium linearization, and different formal zero-temperature expressions; at p. 68 it explicitly warns that naive zero-temperature limiting and linearization give different interacting equations. Its simplified irreversible dynamics (SID, p. 92) discards interaction-dependent dissipative terms in practical calculations and is expected to agree in the relevant vanishing-dissipation perturbative limit; at nonzero regulator it does not preserve all the original thermodynamic structure. These are distinct equations and their limits must not be silently interchanged.

The author uses primary multitime correlations for the nonlinear evolution, and secondary left/right-decoupled correlations only after restricting to a linear evolution (pp. 70–75). Stochastic unravelings represent density operators through expectations of trajectory objects; their construction is explicitly **not unique** (pp. 92–103). A particular unraveling may motivate an ontology but does not by itself establish that its jumps are unique observer-independent events. The book presents its preferred picture and the associated motivations, not a theorem forcing it on all QFTs.

## 3. What finite regulators do—and do not—guarantee

The author lists separate limits for the number of momentum modes, volume, dissipation and temperature (pp. 21–22, 105–106). Finite mode number avoids some infinite-mode difficulties at an intermediate stage; it does **not** make a bosonic Fock space finite-dimensional, since one bosonic mode has arbitrarily many occupation states. A separable Hilbert space has a countable orthonormal basis, not a countable set of all vectors or states. A Fock basis indexed by occupation sequences is countable when the **total occupation is finite**; arbitrary infinite zero/one sequences are uncountable. The book’s p. 51 statement that a countable list of integer entries is itself enough to make all sequences countable needs that finite-occupation restriction, or another specified restriction, for the usual Fock basis.

Several further hypotheses are needed even at a regulated stage:

- A Hamiltonian being bounded below does not by itself guarantee `Tr(exp(-βH))<∞` on an infinite-dimensional space: `H=0` on an infinite-dimensional Hilbert space is a counterexample. A Gibbs density matrix needs a finite partition function at the relevant β.
- Nonnegative entropy production and a stationary Gibbs state do not **alone** prove convergence to that particular state from every initial condition. For example, zero dissipative couplings have zero production but do not relax an excited stationary state. One needs suitable irreducibility/ergodicity, domains and convergence results for the equation under consideration. The book motivates its coupling choice by ergodicity; this audit has not proved those conditions for the interacting master equation.
- Pointwise finite answers do not establish a joint cutoff-removal limit, uniformity, Lorentz covariance, gauge invariance, microcausality, or physically appropriate positivity for every interacting evolution. The author himself acknowledges finite-volume and spatial-dissipation Lorentz violation and requires appropriate final predictions or a covariant finite-regulator formulation (pp. 87–88, 105–106). If dissipation remains physically nonzero, appealing only to the zero-dissipation limit is insufficient.

The book’s definition of a well-defined theory is a **criterion**: suitably tuned model parameters, existence of specified correlation-function limits and recovery of required symmetries (pp. 105–106). Stating the criterion is not proving it for all models, temperatures, observables or orders of limits. The author notes that the order might be subtle; our diagnostic below makes one aspect explicit.

## 4. Exact free-sector limit obstruction

Take one free bosonic mode of frequency `ω>0` and the zero-temperature master equation (1.66), with its source convention:

```text
L_κ(ρ) = −i[ω a†a,ρ] + κ(2aρa† − {a†a,ρ}),       κ ≥ 0.
```

Here `κ` is the rate for the chosen mode, not the coefficient `γ` multiplying `|k|⁴` above. The subspace spanned by vacuum `|0⟩` and one excitation `|1⟩` is invariant for states initially supported there. Starting at `ρ₀=|1⟩⟨1|`, solve the diagonal master equation:

```text
p_κ(t) = Tr(|1⟩⟨1| ρ_t) = exp(−2κt).
```

At any finite `t`, the zero-damping limit is 1. At each positive `κ`, the long-time limit is 0. Therefore

```text
lim_{κ→0+} lim_{t→∞} p_κ(t) = 0,
lim_{t→∞} lim_{κ→0+} p_κ(t) = 1.
```

No convention in these expressions requires that `p` be a measurable detector outcome in an interacting QFT; it is an exact population in the specified finite sector. At κ=0 the Hamiltonian preserves this initial excited population; no relaxation to the vacuum occurs. As the author emphasizes in another context, long-time free unitary dynamics generally need not converge for off-diagonal states. This example uses a diagonal initial state so that both displayed limits exist and differ.

The book uses the Abel-weighted resolvent `sR_s` to represent equilibrium when the dynamical relaxation assumptions hold (pp. 74–75). Here its excited population is

```text
A(s,κ) = s ∫₀∞ e^(−st) p_κ(t) dt = s/(s+2κ),     s>0.
```

For `κ>0`, `s→0` gives 0; for `s>0`, `κ→0` gives 1. Jointly, `s=κ²` tends to 0, `s=κ` stays **1/3**, and `s=√κ` tends to 1. More generally, `s=cκ` yields `c/(c+2)` for `c>0`. These are **path-dependent Abel means** of a specific nonstationary initial population, not the book’s renormalized interacting scattering amplitude. At a fixed positive damping the book takes the long-time/Abel limit first, which is consistent with the 0 result; the warning is against dropping or swapping that order without a separate argument.

There is also no contradiction with fixed-time small-damping control. For `0≤t≤T`, `|p_κ(t)−1|≤2κT`. But this bound is not uniform as `T→∞`. One must declare whether the target is a fixed-duration process, a relaxed equilibrium, or a jointly scaled observation.

## 5. Momentum dependence and spatial localization

Consider the particular family `γ_k=γ|k|⁴` with `γ₀=0`, over an unbounded set of momenta and fixed `t>0`. For every fixed `k`, the one-excitation survival `exp(−2γ|k|⁴t)` tends to 1 as `γ→0`. Yet

```text
sup_k [1 − exp(−2γ|k|⁴t)] = 1   for every γ>0,
```

when arbitrarily large momenta are available. For example, set `k=n` and `γ=n⁻⁴`: the survival is always `e⁻²ᵗ`. This is a comparison of a **moving, higher-energy input** with the undamped evolution, not a failure of convergence for each fixed finite-energy state. The finite-cutoff estimate `1−exp(−2γ|k|⁴t)≤2γK⁴t` for `|k|≤K` makes the required joint-scale condition explicit. Energy constraints, smearing, a state-independent renormalization prescription and the declared topology can alter what convergence is required; this one-particle calculation supplies no general no-go theorem.

There is a useful positive counterpart for a **restricted observable and state class**. Suppose the initial state lies in the vacuum-plus-one-particle sector, the free energy is `H=Σ_k ω_k N_k` with `ω_k≥|k|`, and `Tr(Hρ)≤E`. Let `N_tot=Σ_k N_k`. For independent mode losses with `γ₀=0`, the change in its expectation satisfies, for any `K>0`,

```text
0 ≤ ⟨N_tot⟩₀ − ⟨N_tot⟩ₜ ≤ 2γt K⁴ + E/K.
```

Indeed the low-momentum loss is at most `2γtK⁴` times the initial particle probability, which is at most one; the high-momentum initial occupation is at most `E/K` by the energy bound. Optimizing at `K=(E/(8γt))^(1/5)` for `E,γ,t>0` gives the uniform upper bound `(5/4)(8γt)^(1/5) E^(4/5)`. Thus fixed-energy control can restore uniform convergence for **this number expectation** even though the unconstrained moving-mode example fails it. The estimate is conservative, may exceed one, and does not give a trace-norm, diamond-norm, interacting-field or arbitrary-observable bound. It concerns prepared states with at most one free excitation; no such constraint is asserted for an interacting QFT vacuum.

A separate spatial warning comes from the book’s finite-mode scalar construction, not from the dissipator alone. On a one-dimensional periodic box of length `L`, retain Fourier modes `n=−N,…,N` and canonical oscillator commutators. The equal-time bracket of the truncated field and its conjugate momentum is

```text
[φ_N(x),π_N(y)] = i D_N(x−y),
D_N(z) = L⁻¹ Σ_{n=−N}^N exp(2πinz/L).
```

At `z=L/2`, `D_N(z)=(-1)^N/L`, nonzero for spatially distinct points. This is the **band-limited periodic delta kernel**, not the continuum Dirac delta at finite `N`. Equation (1.44), printed p. 62, displays a delta; read with the earlier finite momentum set, it needs this finite-cutoff qualification unless its delta symbol is intended to denote the truncated kernel. The distinction is not a diagnosis of superluminal signaling: the regulator's observables have global tails, and a result about ideal point fields is not a calibrated operational signal.

Distributionally, `D_N` approaches the periodic delta on appropriate smooth test functions; pointwise behavior away from the diagonal is not sufficient to establish convergence of complete measurement instruments. The existing [3+1 smooth-probe gate](THREE_DIMENSIONAL_SMOOTH_PROBE_CAUSALITY_GATE.md) derives a cutoff-order bound for its **different**, reversible two-field model, and its follow-on establishes a restricted continuum instrument result. Those results cannot be automatically imported to the dissipative interacting master equation. Conversely this finite-mode observation does not invalidate those established restricted results.

## 6. Ontology, information and measurement

The excerpt offers three real conceptual benefits: it separates free quanta from interaction-dependent particle-like “clouds”; it explicitly declares bath, statistics, regulator and observables; and it seeks a controlled dynamical formulation rather than simply declaring all divergences meaningless. It also says spatial resolution of the interacting construction and its relation to low-energy quantum mechanics require further work (pp. 107–108).

The author argues that ensemble correlation functions let his particle-physics formulation avoid the **most challenging** version of the measurement problem, while acknowledging that the problem may reappear in other quantum contexts (pp. 106–108). That is an interpretation and a limited modeling scope, not a derivation of a unique single outcome. A density matrix can encode different ensembles; nonlinear evolution and its treatment of preparations, conditioning, entangled auxiliaries, and empirical statistics require explicit analysis. Complete positivity is a linear-map criterion: one cannot call a general nonlinear density-matrix evolution CPTP merely because a particular linear limit is CPTP. Our finite free-sector verification below does establish a CPTP channel for that restricted case, not for the full thermodynamic equation.

For the present project, dissipative QFT is a serious **physical alternative or effective description** to compare with unitary QFT, not a direct account of first-person quality, subject boundaries or universal experience. Nor does its use of correlation functions prove that an observer or external simulator creates reality. A complete comparison must recover the stipulated physical targets, give a well-defined physical realization and connect any experiential hypothesis through independent arguments and evidence. Macroscopic entropy production, information loss in a coarse description and phenomenal unity are distinct questions.

## 7. Reproducibility and next test

Run:

```sh
python verification/dissipative_qft_limit_gate.py
PYTHONPATH=verification python -m unittest dissipative_qft_limit_gate_test
```

For the vacuum/one-particle amplitude-damping channel, the [verifier](verification/dissipative_qft_limit_gate.py) checks all 15 principal minors of the Choi matrix at nine exact rational coherence-damping parameters, trace preservation, and the channel composition law for 81 parameter pairs on three selected inputs. It also checks exact rational samples of the three Abel paths, the moving-momentum construction, and nine numerical examples of the energy-bounded number-loss estimate; [the receipt](verification/dissipative_qft_limit_gate.json) records them. Three focused tests check the receipt, coherence/population map and the balanced Abel path. The general formulas and limiting statements are analytic, not justified by finite enumeration. The verifier does not calculate the interacting thermal equation, renormalization, QED, or an observable quantum-gravity result.

A worthwhile next physical step would specify a **fixed class of smeared observables and energy-bounded states**, an explicit `V,N,γ,T,t` limit schedule, and the comparison dynamics, then bound the complete output or the selected correlations with all rates and dependencies shown. For interactions, add trace-class equilibrium, existence, positivity, gauge/relativistic tests and the difference between full and SID evolution; none is supplied here. The missing book chapters would be needed before assessing its detailed scalar and QED calculations.

C3 remains **full structural and experiential intelligibility**, jointly with C1–C7. B4–B5/F2, B9/F3 and B10 remain open. This chapter audit and free-sector check are not an external empirical validation or a substantive framework pass.
