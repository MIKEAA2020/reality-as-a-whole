# Formalization recheck: errors, exact criteria and a constrained history

## Scope and method

The user's question calls for actual rechecking, not treating tests as certificates. This is a **targeted** audit of the recent [QFT/experience controls](CLAUDE_TIME_QFT_EXPERIENCE_AUDIT.md), [cross-field controls](CLAUDE_TIME_CROSSFIELD_RESEARCH_AUDIT_AND_CONTROLS.md), and their connection to the existing [zero-constraint relational model](ZERO_EXPERIENCE_INTRINSIC_IDENTITY_RELATIONAL_GRAVITY.md). It is not a repository-wide proof audit. The governing research thesis treats space and time as non-fundamental constructs, experience as intrinsic, and the whole's energy as zero; it does not assume the older universal-subject ontology. The calculations below explore a possible mathematical format for internal succession, not a derivation of that thesis or a replacement for it.

## 1. Concrete corrections and limits

1. **False cross-reference:** the cross-field audit said the QFT audit “gives a non-signalling control.” It distinguished correlations from signalling but did **not** actually calculate a no-signalling control. That was my error. Section 2 now gives a general CPTP proof and an explicit numerical example; the earlier cross-reference is corrected.
2. **Overstated verification inventory:** the QFT audit said its tests checked “all four” finite controls, but its sections contain **five** controls. The count is corrected. The tests for the affine example and subject/quality example mostly instantiate arithmetic and labels; they do not verify a source-specific categorical theorem or experiential identification. The latter remains a historical single-subject toy, not a model of the current plural-subject zero programme.
3. **Ideal erasure qualification:** the second CNOT reverses the *modeled* record only when the joint S–E system is isolated as specified. If another uncontrolled system copied or became correlated with the path record, applying CNOT to S–E does not necessarily restore interference in S. Section 2 gives an explicit counterexample and regression test.
4. **Flow comparison too narrow:** the original noncommutation example is correct for its stated qubit but only sampled a particular state and observable. Section 3 proves a necessary-and-sufficient state condition for its full dephasing/modular intertwining, including the maximally mixed case, and tests generic directions. This is an exact finite theorem, not a Wilsonian RG theorem.
5. **Integration gap:** the previous eraser example used an externally described gate sequence. That is a valid circuit, but it did not itself connect the examples to a timeless/constraint formulation. Section 4 constructs one finite constraint history with record formation and erasure using the *same* system and clock carrier. Its clock, gates and admissible physical state remain inputs; in particular its constraint zero is not an identified whole-level physical energy zero, and its system is not an experiential subject.
6. **Functional/physical status:** the two-scalar FLRW formulas for `χ[τ]` and the weak Dirac observable `a[τ]` were analytically checked on their stated `pφ≠0` domain; their prior [rational tests](verification/zero_intrinsic_identity_relational_gravity_test.py) exercise on/off-shell brackets. This conditional consistency is not a derivation of emergent spacetime, cosmic energy, a subject or qualitative identity. We have not thereby found a mathematical error in those checked equations.

## 2. No-signalling and records: precise statement

Let `ρ_SE` be any finite-dimensional joint density operator. A nonselective operation on E is a CPTP map `Λ_E(B)=Σ_j K_j B K_j†` with `Σ_j K_j†K_j=I`. Its S marginal satisfies

    Tr_E[(id ⊗ Λ_E)(ρ_SE)] = Tr_E ρ_SE.

Proof: for every S observable A, the duality of partial trace and cyclicity give

    Tr[(A ⊗ I) Σ_j (I ⊗ K_j)ρ_SE(I ⊗ K_j†)]
      = Tr[(A ⊗ Σ_j K_j†K_j)ρ_SE]
      = Tr[(A ⊗ I)ρ_SE].

Equality for all A gives the marginal equality. Different nonselective choices on E thus cannot signal to S in this tensor-product scenario. If E's outcome j is **selected** and communicated, S's conditional state can differ; the required classical communication is not instantaneous signalling. In QFT further locality, domain and operational hypotheses are needed; this finite proof is not a general multi-region QFT theorem.

For `|Φ+⟩=(|00⟩+|11⟩)/√2`, either E-dephasing in Z or amplitude damping with parameter `γ∈[0,1]` leaves S's marginal `I/2`. Both outputs can have different joint correlations and E marginals. The tests evaluate both channels, including nonzero γ.

**Incomplete erasure counterexample.** Suppose instead of just S and E, an additional uncontrolled register F has copied the same path, giving `( |000⟩+|111⟩ )/√2` in S–E–F order. A second S-controlled NOT on E transforms this to `( |00⟩_SE|0⟩_F + |10⟩_SE|1⟩_F )/√2`. E is reset to 0, but tracing F still gives `ρ_S=I/2`: visibility remains zero. Thus resetting the named marker does not erase every record.

### Partial marking, exact visibility and distinguishability

For normalized marker states `|e₀⟩,|e₁⟩`, define

    |Ψ⟩ = (|0⟩|e₀⟩ + |1⟩|e₁⟩)/√2,     c = ⟨e₀|e₁⟩.

After `Uφ=diag(1,e^(iφ))` on S, X-basis recombination has

    P(+|φ) = [1 + Re(e^(iφ)c)]/2,        V = |c|.

For equal prior path probabilities, the optimal marker-only path discrimination success probability is `(1+D)/2`, where the Helstrom distinguishability is

    D = ½|| |e₀⟩⟨e₀| − |e₁⟩⟨e₁| ||₁ = sqrt(1−|c|²).

Hence `V²+D²=1` for these *pure, equally weighted* markers. This is a standard two-path quantum-information calculation, not a universal equality for mixed markers or unequal priors. It makes the original V=0 and V=1 endpoints part of a continuously quantifiable example.

For an explicit eraser at any `0≤θ≤π/2`, put `|e₀⟩=cos(θ/2)|0⟩+sin(θ/2)|1⟩`, `|e₁⟩=cos(θ/2)|0⟩−sin(θ/2)|1⟩`; then `c=cos θ`. Measuring the marker in the Y basis yields each outcome with probability 1/2 and equal conditional path probabilities, so the recorded outcome carries no Z-path information. The S conditional fringes have unit visibility and opposite phase shifts:

    P(+_X | φ, E=±Y) = [1+cos(φ±θ)]/2.

Forgetting E averages these to `[1+cos θ cos φ]/2`, the unconditioned visibility `cos θ`. Erasure does not permit signalling: the conditional patterns become identifiable only when the outcome is available.

## 3. Exact qubit criterion for dephasing–modular intertwining

Consider the trace-preserving self-dual channel `D_Z(A)=(A+ZAZ)/2`, and a faithful state `ρ=(I+**r**·**σ**)/2` with `R=|**r**|<1`. For `R>0` let `n_z=r_z/R` and `a=atanh(R)`. The reference output is `D_Z(ρ)=(I+r_z Z)/2`, also faithful. Define the proposed comparison

    D_Z ∘ σ_s^ρ  ?=  σ_s^(D_Z ρ) ∘ D_Z   on M₂(C), for all s.

**Criterion:** this identity holds for all s and all operators if and only if `[ρ,Z]=0` (including `R=0`).

For necessity use A=Z. Since `logρ = scalar I + a **n**·**σ**`, the Pauli rotation identity gives

    D_Z(σ_s^ρ(Z)) = [n_z²+(1−n_z²)cos(2as)] Z,
    σ_s^(D_Zρ)(D_Z Z) = Z.

If the equality holds for all s, `a>0` implies `n_z²=1`; hence `[ρ,Z]=0`. If R=0, ρ commutes automatically. For sufficiency, a Z-diagonal ρ has a modular unitary commuting with Z and D_Z, so the whole-channel identity holds for every A and s. This proof concerns the two explicitly stated modular flows and the dephasing map on **the same matrix algebra**. It neither identifies D_Z with renormalization nor rules out other modular/RG maps or scale calibrations.

At selected values of s an individual mismatch may vanish even for a noncommuting state; the theorem requires **all** s. Regression tests include non-axis-aligned Bloch vectors, commuting states and several times.

## 4. One constrained finite history for record and erasure

Let the system Hilbert space be `H_S⊗H_E=(C²)²`, and a three-label clock `H_C=C³` with orthonormal basis `|0⟩,|1⟩,|2⟩`. Write `H_E` for the Hadamard on E and `V` for the S-controlled NOT. Define the three **supplied** reversible transitions

    W₀=V,         W₁=I⊗H_E,         W₂=V(I⊗H_E).

Their ordered product `W₂W₁W₀=I`. Define the unitary cyclic shift

    U = Σ_(k=0)² |k+1 mod 3⟩⟨k| ⊗ W_k,
    C = 2I − U − U†.

Because `U³=I`, C is positive with spectrum contained in `{0,3}`. For the initial state `ψ₀=|+⟩_S|0⟩_E`, let `ψ₁=W₀ψ₀`, `ψ₂=W₁ψ₁`; then `W₂ψ₂=ψ₀`. The normalized history

    |Hist⟩ = (|0⟩ψ₀ + |1⟩ψ₁ + |2⟩ψ₂)/sqrt(3)

satisfies `U|Hist⟩=|Hist⟩` and hence `C|Hist⟩=0`. Conditioning the **one** stationary history on a clock label gives:

| k | Conditional joint state | Operational feature |
|---|---|---|
| 0 | `|+⟩|0⟩` | S has X-fringe visibility 1; no Z-path record in E. |
| 1 | `(|00⟩+|11⟩)/√2` | Perfect S–E Z record; S alone has visibility 0. |
| 2 | `(I⊗H_E)(|00⟩+|11⟩)/√2` | E's Z outcome selects the ± interference patterns; forgetting it still gives visibility 0. |

At k=2, measuring E in Z gives the same eraser statistics as §1 of the original audit. To avoid treating a kinematic clock projection as though it automatically preserved the constraint, let `P_phys=(I+U+U²)/3` be the orthogonal projector onto `ker C`. For any system POVM `{M_a}` define the **physical compressed effects**

    E_(k,a)=P_phys (|k⟩⟨k| ⊗ M_a) P_phys,       Σ_(k,a) E_(k,a)=P_phys.

Each is positive and acts on the physical Hilbert space. In the specified history, `p(k,a)=⟨Hist|E_(k,a)|Hist⟩=(1/3)⟨ψ_k|M_a|ψ_k⟩`, so `p(a|k)=⟨ψ_k|M_a|ψ_k⟩`. This gives a normalized clock–outcome POVM on the constraint kernel, not just an illegitimate projection of a physical state. It does **not** by itself specify a complete physical measurement instrument, sequential measurement backaction or an implemented clock device. A [subsequent instrument recheck](ZERO_CONSTRAINED_HISTORY_INSTRUMENT_RECHECK.md) constructs one valid physical Lüders instrument, shows the clock-only outcomes are uniform and leave the physical state unchanged, and constructs a different instrument with the same effects and different retained outputs.

The “clock” is an internal finite register, and the equality is a stationary constraint on this history, not an external succession of whole-level states. The construction embeds the record and erasure correlations in a time-neutral description; it **does not** derive physical spacetime, identify a subject or prove that C is the physical total energy of reality. The transitions, the normalized history and the clock POVM are deliberately chosen. The periodic return and resetting are engineered; no fundamental temporal cycle or real-world reversible detector is implied.

## 5. Reproducibility and next step

[New tests](verification/claude_time_formalization_rigor_test.py) independently check the CPTP channels, unreset external record, partial-marking and eraser fringes, general qubit criterion, and constrained three-label history and spectrum. The analytical statements are proved above; numerical tests do not establish the metaphysical or gravitational programme. A productive next step is to put a *specified* effective relational record mechanism and its clock comparisons into the same gravity/zero candidate, then test its limit and physical–experiential interpretation, rather than calling this finite register the solution.
