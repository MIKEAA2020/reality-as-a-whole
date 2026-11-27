# Rechecking the constrained eraser history: effects versus instruments

## What changes

The previous [formalization recheck](CLAUDE_TIME_FORMALIZATION_RIGOR_RECHECK.md) constructed a normalized three-label stationary history and compressed its clock–system POVM to the constraint kernel. Its probability formula is correct, but **the compressed effects do not uniquely determine measurement backaction**, and the earlier document did not specify a complete physical instrument. This pass constructs one and exposes a non-obvious limitation: an isolated clock-only reading is an uninformative uniform coin on the physical Hilbert space, and its Lüders instrument leaves a physical state unchanged. It does not produce a new whole-level state at a clock tick.

The calculation is a constrained finite example. The user’s present premise is that spacetime is non-fundamental and experience intrinsic; neither a clock register nor a zero constraint identifies actual total energy or creates an experiencer. The calculation gives a precise relational probability and instrument, not a completed ontology or physical detector.

## 1. Encoding the whole physical subspace

Use the same three clock labels `k=0,1,2`, system Hilbert space `H_S⊗H_E`, and transitions

    W₀=V,   W₁=I⊗H_E,   W₂=V(I⊗H_E),   W₂W₁W₀=I,
    U=Σ_k |k+1 mod 3⟩⟨k|⊗W_k,       C=2I−U−U†.

Let `V₀=I`, `V₁=W₀` and `V₂=W₁W₀`. The isometry J from the four-dimensional system carrier to the 12-dimensional history space is

    J|ψ⟩ = (1/√3) Σ_k |k⟩⊗V_k|ψ⟩.

Because the transition product is I, `UJ=J`; conversely every U-fixed vector has this form. Therefore `J†J=I` and `JJ†=P_phys=(I+U+U²)/3`, the projector onto `ker C`. These statements hold for **every** initial system state and its mixtures, not only the one Bell/eraser example. The induced physical inner product is inherited via J.

For a POVM `{M_a}` on the system, its compressed joint clock–outcome effect is

    E_(k,a)=P_phys(|k⟩⟨k|⊗M_a)P_phys
           = (1/3) J V_k† M_a V_k J†.

The effects sum to P_phys. If `ρ_phys=JρJ†`,

    p(k,a)=Tr(ρ_phys E_(k,a))=(1/3)Tr(ρ V_k†M_aV_k),
    p(k)=1/3,     p(a|k)=Tr(V_kρV_k† M_a).

The conditional probabilities reproduce the stipulated circuit's k-dependent correlations; the clock marginal alone is uniform for **every** ρ. Thus a clock label and a system effect together encode correlations even though the label alone does not distinguish physical states.

## 2. A valid physical instrument and its limitations

A legitimate chosen instrument on the physical subspace is the Lüders instrument

    I_(k,a)(ρ_phys) = sqrt(E_(k,a)) ρ_phys sqrt(E_(k,a)),
    sqrt(E_(k,a)) = (1/√3) J V_k† sqrt(M_a) V_k J†.

Every operation is completely positive and trace-nonincreasing; the sum is trace-preserving on `P_phys H`, since `ΣE_(k,a)=P_phys`. Its poststate is a **physical history state**. The instrument is one possible implementation of the effects, not the only one, and it is not derived as an autonomous local measurement mechanism. Classical conditioning on k is used to interpret the joint statistics; no external temporal evolution of the whole is introduced.

For the clock-only POVM (M=I),

    E_k=P_phys/3,        I_k(ρ_phys)=ρ_phys/3.

After normalization, the conditional physical state is identical for all k. This does not negate internal correlations, but it prevents an unjustified reading: projecting onto a clock label and treating the resulting *kinematic* branch as the final physical state is not the same as this constraint-compatible measurement. In particular, for `|Hist⟩=J|ψ⟩`, the normalized kinematic branch `|k⟩⊗V_k|ψ⟩` is not physical:

    ||(I−P_phys)(|k⟩⊗V_k|ψ⟩)|| = sqrt(2/3),
    ||C(|k⟩⊗V_k|ψ⟩)|| = sqrt(6)                (||ψ||=1).

The old probability computation may still use the kinematic decomposition; it must not call that isolated branch a state satisfying C=0. A richer clock/detector model with additional dynamics or relational instruments may have different properties; this example is **not** a general impossibility theorem about reading time.

## 3. Same effects need not mean same poststates

Let `R` be any nontrivial unitary on the four-dimensional initial-system carrier. Define

    I′_(k,a)(ρ_phys) = (J R J†) I_(k,a)(ρ_phys) (J R† J†).

Both instruments have the same outcome effects and probabilities, because the post-operation is physical and unitary on `P_phys H`; but they generally give different retained poststates. For the clock-only case, use the logical Pauli Z on S, `R=Z⊗I`, and input `ψ=|+⟩|0⟩`. The normalized outputs are orthogonal physical histories `J|+0⟩` and `J|−0⟩`; their trace distance is 1 even though each clock outcome has probability 1/3 in both instruments. This is an explicit version of why probability-level clock equivalence does not establish instrument-level equivalence.

This example does not assert that an experimental clock in our universe has either backaction. It shows why the operator, state, reference and intervention transformations must all be specified before making that claim.

## 4. Verification and follow-through

[Tests](verification/zero_constrained_history_instrument_recheck_test.py) verify the full kernel isometry, all effects and Lüders operations, the nonphysical branch residuals, and the same-probability/different-poststate example using a pure state and a mixed state. The constructions are analytical finite-dimensional identities; tests are controls, not a proof that arbitrary gravitational constraints admit the same construction. Next, extend this discipline to an actual two-clock constrained model and determine the complete instrument transformation and physical detector coupling without treating a selected clock projection as a physical state or assuming a universal clock.
