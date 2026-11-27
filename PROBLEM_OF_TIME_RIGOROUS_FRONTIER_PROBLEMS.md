# Problem of time: rigorous frontier problems and a constructive foothold

## 0. Answer and scope

**Yes.** We can formulate concrete mathematical problems whose solutions or counterexamples would close identifiable gaps. Below are quantified benchmarks, not just labels for gaps. They are a proposed sufficient programme for the relational/modular approach being pursued here, **not a proof that every valid solution must use this formalism**. A full physical solution means recovering the appropriate quantum and relativistic predictions from one physically justified theory, including domain-dependent clock descriptions; it does not require a universal clock. An account of the user's stronger physical–experiential constitution is a further explicit target, not silently equated with an ordinary quantum-gravity theorem.

We do not claim to have solved the general problem. Section 10 supplies an analytical partial solution, in one specified constrained model, rather than stopping at a list. Existing controls and their limitations are linked in [the prior frontier](PROBLEM_OF_TIME_EXACT_FRONTIER_AND_SOLVABLE_TARGET.md), [modular analytical gate](LIGHTHOUSE_MODULAR_SCHRODINGER_ANALYTIC_GATE.md), and [FRW analysis](FRW_MODULAR_CLOCK.md). The new programme explicitly permits analytical work to proceed without waiting for detector constructions.

### Common notation and comparison discipline

Choose a candidate generally covariant or otherwise background-independent theory **T**. Its mathematical data must specify an observable algebra and allowed states, or a kinematical system with constraints and a physical state construction; choosing these data is itself part of the problem. Let `λ→0` denote a *specified* semiclassical/continuum regime, not automatically ħ→0. Let `K_λ` be a stated common family of physical preparations; cutoffs and energy bounds must be declared. Let `A_λ` be a test algebra, and let `J` denote a finite operational experiment (state preparation, available interventions and records, including no-reading where relevant). For probability distributions use `TV(p,q)=½ Σ|p−q|` (or the corresponding supremum over measurable events).

Error statements below must say whether they are uniform over all allowed states, energy-bounded states, observables or finite lists of experiments. A variable called time or a declared limit is not by itself a physical clock, a semiclassical limit, or a derivation.

## F1. Construct a nontrivial physical theory and probability rule

**Input:** an action, algebraic model, spin-foam/covariant construction, or another precise candidate T, including spatial/boundary conditions and matter. In a Dirac route, specify `H_kin`, a dense test space Φ, regulated constraint operators and, if using group averaging, a rigging map `η:Φ→Φ*`.

**Problem:** construct a nonzero positive physical inner product such that

    <ηf,ηf>_phys ≥ 0,          <ηf,ηg>_phys = overline(<ηg,ηf>_phys),
    η(C_a f)=0,

with null vectors quotiented and the result completed. Define normalized physical states and a separating family of physical effects `0≤E≤I` with probabilities `p_ρ(E)`. For continuous-spectrum constraints, specify the rigging measure and operator domains rather than treating generalized solutions as normalizable kinematic vectors. Include boundary charges when present; `C=0` does not prove total physical energy is zero.

**Success:** a positive, nontrivial physical space and well-defined normal probabilities, including at least one nonconstant relational observable in a gravity–matter model. **Counter-result:** a specified candidate/regulator cannot meet positivity, nontriviality or constraint implementation. Other quantization approaches may replace η with an equally explicit construction.

**Current status:** positive rigging examples exist in models, including §10 below, but neither §10 nor the JT truncations establish a full gravitational theory.

## F2. Gauge covariance and local gravitational dynamics

**Input:** F1 plus local gravitational variables and a regulator. For the ADM route, write smeared classical normal and tangential constraints `H[N]`, `D[v]`, and fix a common dense domain or a suitable observable-level replacement. The classical normal bracket has the schematic, convention-dependent form

    {H[N],H[M]} = D[q^(ab)(N ∂_b M − M ∂_b N)].

**Problem:** construct continuum constraint/observable actions or regulator limits for which the quantum analogue is anomaly-free on a specified domain, or show that physical amplitudes are invariant under the corresponding two local deformations. Because `q^(ab)` is a phase-space-dependent structure function, a formal Lie-algebra calculation with constants does not suffice. Establish that the algebra acts nontrivially and consistently on the physical relational observables, and specify any boundary terms. For non-ADM approaches give an equivalent test of local covariance.

**Success:** an explicit limit and a domain/observable-level refoliation consistency result in a nontrivial inhomogeneous sector, with controlled errors if approximate. **Failure:** an explicitly computed anomaly, incompatible domain, or mismatch for matched physical events under the stated assumptions. Closure alone is not a complete reconstruction of geometry or matter.

## F3. Relational evolution and the ordinary Schrödinger limit

**Input:** F1, a physical clock chart i with reading τ in an interval `I_i`, a system Hilbert space `H_i`, and maps `R_i(τ)` from a declared physical domain into conditional system states. For a channel formulation, let `E^λ_{τ,τ0}` be the physical reduced evolution between two readings; it must be derived from T and the clock prescription, not stipulated as its answer.

**Problem:** find a self-adjoint canonical Hamiltonian `H_eff^λ(τ)` on a common invariant core (or a well-defined unitary propagator `U^λ(τ,τ0)`) and an explicit bound, for each finite T,

    sup_(|τ−τ0|≤T, ρ∈K_λ)
      ½ ||E^λ_{τ,τ0}(ρ) − U^λ(τ,τ0) ρ U^λ(τ,τ0)†||₁
       ≤ ε_Q(λ,T),        ε_Q(λ,T) → 0.

When a density-operator formulation is inappropriate, replace this with the corresponding uniform bound for a specified separating test family of physical expectation values. State the clock's preparation and finite-resolution error, the normalization/conditional-probability denominator, and include backreaction in `ε_Q`. For time-independent `H_eff`, derive `iħ∂_τ ψ=H_eff ψ` on its domain. Nonunitary finite-clock corrections are allowed if controlled and correctly interpreted.

**Success:** prove the estimate in a gravitational model on a nonempty physical family, and identify the physical meaning and calibration of τ. **Obstruction:** exhibit a valid family with error bounded away from zero or loss of a well-defined generator on the declared domain. This task is independent of a universal time and can be solved locally even if a given clock turns elsewhere.

## F4. Modular-to-Schrödinger bridge (WP5, conditional route)

**Input:** a specified gravitational/crossed-product model from F1, a family of faithful normal reference states `ω_λ` on algebras `M_λ`, a physical system subalgebra `N_λ`, a clock calibration `s_λ(τ)`, and comparison maps `ι_λ` into a common observable representation. If flows are cocycle perturbed, give the cocycle `u_λ(s)` and the exact algebra on which it acts.

**Problem:** prove either that the relevant modular/cocycle action preserves `N_λ`, or define the reduced channel and its controlled deviation from automorphic dynamics. On a specified dense `D` of test observables, prove a common-core generator result (or work directly with flows):

    sup_(|τ|≤T) || ι_λ[Ad(u_λ(s_λ(τ))) σ^ω_λ_{s_λ(τ)}(A_λ)]
                         − α^can_τ(ι_λ A_λ) ||_{test} ≤ ε_M(λ,T,A),
    ε_M(λ,T,A) → 0.

Here `α^can` is independently obtained from F3 or the canonical limit; `||·||_test` must be specified, e.g. operator norm on a bounded code sector or a uniform seminorm over `K_λ`. Establish self-adjointness of any candidate generator and the needed derivative of the cocycle, or prove a concrete failure. Track calibration, state preparation and regulator errors separately. In unbounded/type III settings do not assume norm differentiability; a faithful trace has trivial modular flow, and an ambient flow need not preserve a subsystem.

**Success:** a nontrivial controlled semiclassical instance in the declared gravity algebra, not merely a finite Gibbs identity. **Obstruction:** a demonstrated derivative/domain failure, noninvariant subalgebra, or mismatch with independent canonical dynamics in the proposed regime. This is required only if the proposed resolution identifies physical time through modular flow; an alternative route need not pass F4.

## F5. Recover relativistic duration and causal geometry

**Input:** a family of physical states from F1/F2 plus a declared set of clock/worldline observables and relational events. A target classical regime must be specified: e.g. states concentrated near a smooth Lorentzian metric `g` on a region, not a generic promise that geometry emerges.

**Problem:** construct operational elapsed-time random variables `T^λ_γ(a,b)` associated with declared clock trajectories γ, and prove for all γ in a specified finite family that

    P_λ( |T^λ_γ(a,b) − ∫_γ sqrt(−g_μν dx^μ dx^ν)/c| > δ_λ ) ≤ ε_g(λ),
    δ_λ → 0,      ε_g(λ) → 0.

Units and signature must be fixed, and clock response/calibration specified. Recover causal order, local dynamics and the weak-field/nonrelativistic comparisons from the same regime, with a noncircular construction of the geometry. Test two different paths with common endpoints. The integral is proper time **along γ**, not necessarily a maximum; a longest-chain construction normally approximates maximal Lorentzian distance after density/dimension calibration.

**Success:** the estimate plus the expected weak-field/QM and relativistic observables in the same model. **Failure:** an actual irreducible mismatch in the admissible state family, or failure to identify clock trajectories/metric. F5 is a geometry problem, not a consequence of F3 or F4 alone.

## F6. Clock changes and records on overlaps

**Input:** F1 and two clock descriptions i,j of the same theory. Specify overlap states `K_ij`, the same physical experiment J, its complete possible outputs (including clock failure), and transformations on preparations, effects, interventions and retained records. A clock-neutral theory and exact isometries can be used but are not mandatory.

**Problem:** prove for each declared finite experiment family `J_m` and `ρ∈K_ij`

    sup_(J∈J_m, ρ∈K_ij) TV(p_i^J(ρ), p_j^{transport(J)}(ρ)) ≤ ε_ij(λ,m).

For multiple interventions the probabilities are joint probabilities, not merely equality of one clock POVM. If a conditioning event d has probability ≥κ>0 in both pictures, joint TV error ε implies a conditional-TV error bounded by `min(1,2ε/κ)`; otherwise report rare/no-reading cases without hiding them through renormalization. On triple overlaps compare transported instruments after composition, allowing any explicitly identified physical holonomy. Include turning points and sectors outside a clock chart. Separately compare independently quantized reductions and their boundary conditions, rather than calling a change of coordinates a proof of their equivalence.

**Success:** exact agreement or a controlled bound on nonempty overlaps for a nontrivial interacting/gravitational theory; **failure:** a pair of truly matched preparations and events with an unavoidable gap, or a proved absent overlap. This is an operational validation of claims involving such events, not a prerequisite for every mathematical result in F3/F4.

## F7. Arrow and records (a distinct physical problem)

**Input:** a specified low-entropy boundary or other physically justified state condition, a coarse-graining/record algebra and a probability law on histories derived from T. Define finite ordered regions or clock readings, and a record event `R_{a←b}` meaning a present record encodes an earlier specified event (with an explicit reliability threshold).

**Problem:** establish quantitative conditions under which

    P(R_{later←earlier}) − P(R_{earlier←later}) ≥ δ_arrow > 0

for a stated class of records and times, with errors and possible exceptions. Alternatively prove a suitable conditional entropy-production inequality and connect it to the specified reliable records. A global modular automorphism group, a chosen parameter orientation, or monotonicity under an assumed coarse-graining does not alone establish this probabilistic asymmetry.

**Success:** a derivation of the observed direction in a specified regime from stated boundary and dynamics; **obstruction:** a time-reversed or symmetric admissible ensemble giving no such asymmetry. This is needed for the complete account of the thermodynamic/record arrow, not necessarily for F3's Schrödinger limit.

## F8. Empirical adequacy and non-vacuity

**Input:** F3–F6 with operational units, state-preparation conditions, and a candidate theory not tailored separately to each measurement. Let `P^T_λ(J)` be the predicted joint distribution and `P^ref(J)` the distribution from the relevant verified QM/GR effective description, with experimental uncertainty `δ_exp(J)`.

**Problem:** establish

    TV(P^T_λ(J), P^ref(J)) ≤ ε_model(λ,J),

for a declared nonempty suite containing clock comparisons in different gravitational potentials/trajectories, interference and local quantum evolution, and assess `ε_model` against the relevant data and experimental resolution. For any claimed *distinctive* prediction, specify the alternative model, parameter values, likelihood or test statistic, achievable sensitivity and what outcome would disconfirm the claim. Never infer a universal no-go from a null result outside its sensitivity or assume the limiting theory is experimentally selected merely because a formal limit exists.

**Success:** quantitative agreement within a physically justified regime and a discriminating test where the theory predicts one; **failure:** robust conflict beyond combined uncertainty or a model whose proposed regime is empty/unphysical. Observed covariance and standard QM constrain, but do not by themselves uniquely select, a fundamental theory.

## F9. The user's constitutive and experiential extension

**Input needed before a theorem:** an explicit candidate `Z` for the self-sufficient physical–experiential whole; an admissible mathematical notion of realization/isomorphism; a defined subject/occurrence relation and observational/first-person comparison rules. Do not reduce Z to the numeric equation `0=0`, or assume experience is a pointer value.

**Problem:** construct a map or constitutive relation from Z to physical models satisfying F1–F8 **and** to subject-indexed occurrences. State a non-vacuity/selection criterion: for example, in a declared class `C(Z)`, prove either uniqueness up to a physically defined equivalence or a law for the allowed alternatives, with the clock, probabilities, causal/temporal relations and experiential incidence not inserted as unexplained independent axioms. Formulate a comparison that distinguishes at least one rival occurrence/subject assignment compatible with the same coarse physical record. Show how occurrence ordering and experienced succession are related without positing an external time in which the whole is manufactured.

**Success:** explicit definitions plus a proof of the stated implication/selection and physically and phenomenologically discriminating consequences, or a precise countermodel showing a particular proposed Z underdetermines those outputs. **Current status:** this is a research specification, not yet a well-posed theorem in a complete formal language: no accepted definition of Z or criterion for experiential identity has been supplied. Naming that typing gap is necessary; it is not a claim of impossibility or an instruction to give up on the target.

## Dependency and alternatives

F1 supplies a physical theory for F2–F7; F2 and F5 support a gravitational interpretation. F3 and F4 can proceed analytically in parallel; F4 is only mandatory for a modular proposal. F6 tests overlapping clock claims, and F7 is separate from reversible dynamics. F8 tests physical recovery. F9 is the stronger foundational/experiential objective and may guide the choice of T from the start; it is not a device to postpone F1–F8. A single theorem can discharge multiple items if it actually proves their conclusions. No particular ordering of all research activity is required.

## 10. An analytical partial solution: unregulated oscillator modular flow in a constrained gravity-inspired model

This solves an explicit **subproblem**, not F2–F5 in general. It removes the finite oscillator cutoff and the false inference that the entire reduced gravitational factor must possess a Gibbs density. It uses a selected clock-window state and a deparametrized extension, not a derived gravitational KMS state.

Let `H_kin=L²(R,dφ) ⊗ L²(R_+,dp) ⊗ ℓ²(N₀)`, and set

    C = −iħ∂_φ + κp + ħωN,     κ,ω>0,
    N|n> = n|n>.

The p term is the positive-momentum reduced Hamiltonian of the massless-scalar flat-FRW branch studied in [FRW_MODULAR_CLOCK.md](FRW_MODULAR_CLOCK.md); the oscillator is **added after reduction**. We do not claim that this additive constraint follows from a covariant FRW action with an oscillator or contains its gravitational backreaction. On the natural sum domain C is self-adjoint: in the Fourier representation of φ and the p,n representation it is real multiplication by `E+κp+ħωn`.

Take Φ to be finite sequences of smooth compactly supported functions of `(E,p)` with `p>0`. Define the rigging form by restriction to the constraint surface:

    <ηf,ηg>_phys = Σ_n ∫_0^∞ dp overline(f_n(−κp−ħωn,p)) g_n(−κp−ħωn,p).

It is positive, annihilates `Cf`, and its quotient completes to `H_phys=L²(R_+,dp)⊗ℓ²(N₀)`; compactly supported smooth physical data with finite n are obtainable by a test-space extension. Overall group-average normalization is chosen so that the displayed form holds. This is not a normalized kinematic history over all φ.

Fix `β>0`, let `q=e^(−βħω)∈(0,1)`, and take a normalized `f∈L²(R_+,dp)` (optionally supported away from zero) and

    |ψ₀> = sqrt(1−q) Σ_(n≥0) q^(n/2)|n>,
    Ψ_φ(p) = f(p)e^(−iκpφ/ħ) ⊗ e^(−iωNφ)|ψ₀>.

This is the physical conditional representative of normalized constraint data; `iħ∂_φ Ψ_φ=(κp+ħωN)Ψ_φ` holds in the appropriate domain (take f compactly supported to ensure it). The oscillator conditional state is `r_φ=|ψ_φ><ψ_φ|`. With `P=2π/ω`, define the **chosen uniform clock-window average**

    ρ_ref = (1/P)∫_0^P r_φ dφ = (1−q)Σ_n q^n |n><n|
          = exp(−βħωN)/Tr exp(−βħωN).

The integral is trace-norm well-defined; Fourier averaging eliminates `n≠m`. The state is faithful on `B(ℓ²)` and its reference modular flow satisfies

    σ_s(A) = ρ_ref^(is) A ρ_ref^(−is),
    σ^ref_{−φ/(βħ)}(A) = e^(iωNφ) A e^(−iωNφ),
    Tr(r_φ A) = Tr(r_0 σ^ref_{−φ/(βħ)}(A))

for every bounded oscillator observable A and every real φ. On the finite-matrix-unit algebra, differentiation gives the Schrödinger/Heisenberg generator explicitly; for general bounded A the action is understood in the appropriate weak/strong topology, not falsely asserted norm differentiable. The conditioned vector lies in `Dom(N)` and obeys `iħ∂_φ|ψ_φ>=ħωN|ψ_φ>`.

A concrete cutoff error is available: truncate to `n=0,…,L−1` and renormalize the conditional vector. Its omitted probability is `q^L`, so its trace distance to the full conditional pure state is exactly `q^(L/2)` for every φ; the trace distance of the normalized truncated Gibbs reference to ρ_ref (embedded by zero outside the cutoff) is `q^L`. Any common POVM has no larger TV error. These are uniform, analytic bounds, not numerical extrapolation. [The verification controls](verification/problem_of_time_rigorous_frontier_test.py) check truncation, phase averages, modular signs, rigging-surface cancellation and the structural obstruction below.

**What is and is not obtained:** a positive physical construction and an exact, infinite-dimensional oscillator relational/modular correspondence in this simplified constrained model. The gravitational p-sector has no normal Gibbs density at finite β on `B(L²(R_+))`, as shown in the existing FRW note; we did not assign one. β, the factorization, uniformly weighted φ-window, oscillator, clock branch and linear constraint are inputs. The window average is a defined state construction, not a demonstrated autonomous clock measurement. There is no semiclassical limit, covariant action/backreaction, type III/crossed-product derivation, refoliation theorem, arrow, or experience derivation here. Nevertheless this is a concrete proof target solved beyond the earlier finite-dimensional Gibbs control.

## 11. One exact structural obstruction and its resolution target

For any time-oriented Lorentzian metric g and constant `a>0`, `g'=a²g` has exactly the same causal order but `τ_{g'}(γ)=a τ_g(γ)` for each timelike γ. Therefore causal order alone cannot fix physical durations in fixed units. The chess move order has the analogous underdetermination: choosing identical ordinal labels with different tick scales gives different durations. This does **not** prohibit duration emerging from richer structure: F5 must show what supplies or calibrates the missing scale, such as an independently justified volume/state/clock relation. This is a proved obstruction to one insufficient input, not a no-go theorem for relational or modular time.
