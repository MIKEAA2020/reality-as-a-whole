# WdW oscillator interfaces: explicit corrections

**Status:** This audit identifies precise mathematical failures in the claimed chain linking a square-root Wheeler–DeWitt reduction, a dressed oscillator, an exact commuting propagator and a quartic correction. It does not show that all models in the repository fail, or that an appropriate harmonic or quartic Hamiltonian cannot be made self-adjoint. It does show that the cited calculations do not prove the prior claims. Numerical checks: [verification/wdw_interface_audit.py](verification/wdw_interface_audit.py) and [output](verification/wdw_interface_audit.json).

## 1. Three different Hamiltonians were treated as interchangeable

[WDW_HARMONIC_EVOLUTION.md](WDW_HARMONIC_EVOLUTION.md) starts with a square-root operator `sqrt(p² + μ²x² + V)` and then approximates it as `ω(N+1/2)`. [WDW_SELF_ADJOINT.md](WDW_SELF_ADJOINT.md) instead writes `H(l)=p²+ω(l)²x²` and says the argument applies identically to its square-root form. [WDW_MAGNUS_EXACT.md](WDW_MAGNUS_EXACT.md) assumes `H(l)=ω(l)(N+1/2)` for one fixed number operator. These can be separately meaningful models, but no derivation establishing their exact equivalence is supplied.

In particular, for `V=0`, `p²+ω²x²` has eigenvalues `ω(2n+1)`, so its positive square root has eigenvalues `sqrt(ω(2n+1))`, not a constant multiple of `(n+1/2)` across all n. Their n=1 to n=0 eigenvalue ratios are `sqrt(3)` and `3` respectively. A narrow-band approximation may be possible with explicit state-dependent error bounds, but is not the claimed exact equality. Standard harmonic-oscillator formulas are used here, not asserted as new.

## 2. The exact Magnus formula has a conditional scope

For a **fixed** self-adjoint number operator N and real scalar function ω(l), the family `H(l)=ω(l)(N+1/2)` commutes at different l and its integrated-phase propagator follows under the appropriate regularity assumptions. That conditional result is valid; what is not proved is that the actual variable-frequency Hamiltonian used in the preceding document has this form in one fixed basis.

In fact, for the displayed canonical family `H_i=p²+ω_i²x²`, with `[x,p]=i`,

    [H_1,H_2] = (ω_2²−ω_1²)[p²,x²],
    [p²,x²] = −2i(px+xp).

For unequal positive frequencies this commutator is nonzero on a common invariant core. In a unit-frequency oscillator basis its matrix element `<2|[H_1,H_2]|0>` is `2√2(ω_2²−ω_1²)`; the verification script reproduces it in a separately chosen basis. Thus variable frequency does not generally imply commuting Hamiltonians or zero nonadiabatic transitions. This does not contradict the distinct fixed-N model.

Similarly, self-adjointness of each instantaneous H is not, by Stone's theorem alone, a proof of a unique time-dependent propagator: a family requires additional common-domain and regularity conditions or an applicable nonautonomous evolution theorem. No conclusion about the specific gravitational model follows without those hypotheses.

## 3. Quartic interaction is not H₀-bounded

[WDW_ANHARMONIC.md](WDW_ANHARMONIC.md) and its historical script assert that `x⁴` is infinitesimally operator-bounded by the ordinary harmonic oscillator `H₀=p²/2+ω²x²/2`. That is false. On the normalized oscillator eigenstate |n>, standard oscillator identities give

    H₀|n> = ω(n+1/2)|n>,
    <n|x⁴|n> = 3(2n²+2n+1)/(4ω²).

By Cauchy–Schwarz, `||x⁴|n>|| >= <n|x⁴|n>`, which grows quadratically in n, while `||H₀|n>||` grows linearly. Hence no finite constants a,b can satisfy `||x⁴ψ|| <= a||H₀ψ||+b||ψ||` for all oscillator eigenstates, much less an infinitesimal bound. A low-ground-state expectation or a bound in terms of `H₀²` does not establish an H₀ operator bound.

For a positive quartic coupling there are other standard approaches to defining a self-adjoint semibounded anharmonic oscillator. This counterexample invalidates the **specific claimed Kato–Rellich argument**, not self-adjointness by every possible method. It also does not address negative coupling or a time-dependent gravitational domain.

The asserted convergence of the standard quartic energy perturbation series is also not correct in general: the familiar weak-coupling series is divergent/asymptotic; see Bender and Wu (1969), as discussed in [this review](https://arxiv.org/abs/2308.11848). Divergence of the series does not imply a first-order estimate cannot be accurate at small coupling; an explicit remainder or other error control is needed.

Finally, with `x=(a+a†)/sqrt(2ω)`, the claimed transition matrix element has a factor-of-two error:

    <2|x⁴|0> = 3√2/(2ω²),

not `3√2/(4ω²)`. For ω=2 the ladder calculation gives 0.5303300859, versus the earlier 0.2651650429. The resulting claimed transition probability is not established merely by replacing this factor: it also depends on a specified interaction and time evolution.

## 4. Consequence for integration

Do **not** carry the older chain's exact propagation, numerical operator-norm bounds, particle-production suppression, or gravitational extension into a unified conclusion without a fresh derivation from one declared constrained Hamiltonian, domain, physical inner product and clock reduction. Repairing one oscillator estimate would not alone establish a full gravitational constraint or a phenomenal interpretation.

The finite `ω(N+1/2)` example can remain as a legitimate toy model with its assumptions. The first-order ground-state formula `<0|x⁴|0>=3/(4ω²)` also remains correct for the standard harmonic oscillator. Neither verifies the unproved interfaces to the square-root gravitational operator.
