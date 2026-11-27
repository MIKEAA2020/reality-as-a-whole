# Recheck: normalized incidence, locality and zero balance

## Scope and constructive result

This pass rechecks and strengthens selected claims in [normalized incidence versus local experience](ZERO_INCIDENCE_NORMALIZATION_LOCALITY_CORRECTION.md). It uses a finite tensor-product model, not an empirical claim about subjects or a proof that every actual subject is confined to a tensor factor. The user's current thesis concerns zero whole-energy, intrinsic experience and genuinely plural finite subjects, with spacetime non-fundamental. Locality here is an **effective operational assumption in this toy**, not a fundamental spacetime postulate or a denial of the proposed whole.

The earlier two-qubit example is correct but can be made quantitative. Its globally normalized A-share is at least `1/4` away in operator norm from **every** A-local observable, and this bound is attained. We also prove that exact opposite balance for all states of an unrestricted tensor product forces two strictly local contributions to be scalars, while a correlated physical subspace allows nonconstant local contributions to balance exactly. This identifies why the physical-sector assumption matters without declaring the zero programme impossible or equating formal signs with felt valence.

## 1. Best possible local approximation to a global share

Let `P` and `Q` be nonzero, nonidentity orthogonal projections on finite nontrivial A and B spaces. Define `P_A=P⊗I`, `P_B=I⊗Q`, `S=P_A+P_B`. The Moore–Penrose inverse is taken on `supp(S)`. The earlier A-share is

    E_A=S^(−1/2) P_A S^(−1/2)
       = P ⊗ (I−Q/2).

The equality follows by decomposing into the four commuting sectors of P and Q. Thus E_A assigns `1/2` where both incidences are present, `1` where only A is present, and `0` where A is absent.

For **every** A-local self-adjoint operator F,

    ||E_A−F⊗I|| ≥ 1/4.

Indeed, choose normalized `u∈ran(P)`, `v∈ran(Q)` and `w∈ker(Q)`. The expectations in `u⊗v` and `u⊗w` are respectively `1/2` and `1`, while `F⊗I` has the same real expectation `c=⟨u|F|u⟩` in both. The operator norm bounds each expectation difference, so it is at least `max(|c−1/2|,|c−1|)≥1/4`.

The bound is attained by the valid local effect `F=(3/4)P`: on `ran(P)` the difference has eigenvalues `−1/4,+1/4`, and it vanishes on `ker(P)`. Consequently

    inf_(F=F†) ||E_A−F⊗I|| = 1/4.

This strengthens the earlier exact nonlocality claim into a sharp, state-uniform approximation obstruction for the given global-normalization rule. It applies to local effects as well as unrestricted local self-adjoints. It does not say that actual subjects are qubits or that actual experienced quality equals E_A. A global accounting/self-location weight can depend on the reference class without being a locally measurable physical signal.

For product states, `Tr[(ρ_A⊗ρ_B)E_A]=p_A(1−p_B/2)`, with `p_A=Trρ_A P` and `p_B=Trρ_B Q`. If B's state can be independently changed while A's is fixed, the global share changes by `p_A Δp_B/2`; an A-local POVM cannot report that difference without further communication. The conditional claim about signalling still requires the additional premise that a locally accessible report actually implements that global quantity.

## 2. Exact balance on all states versus a physical sector

Let A and B be Hermitian local observables and suppose on the **full** tensor-product Hilbert space

    A⊗I + I⊗B = 0.

Taking partial traces over B and A gives

    A=−(Tr B/d_B)I_A,       B=−(Tr A/d_A)I_B.

So `A=cI_A` and `B=−cI_B`: exact operator cancellation on every unrestricted state permits no nonconstant independent local terms. The same proof works for nonzero fixed coefficients after rescaling. The statement is a finite tensor-product theorem, not a theorem that a gravitationally constrained whole cannot have zero energy.

A physical sector can avoid the premise. For two qubits let

    K=Z_A Z_B,    P_phys=(I+K)/2=|00⟩⟨00|+|11⟩⟨11|,
    V_A=Z_A⊗I,   V_B=−I⊗Z_B.

Both local operators are nonconstant on the full space, yet

    (V_A+V_B)P_phys=0.

The sector includes the coherent normalized state `(|00⟩+|11⟩)/√2`, not just one classical configuration. On `|01⟩`, outside the sector, the sum is `+2`: cancellation is a consequence of the specified physical constraint, not a full-space operator identity. `X_B` alone maps physical states outside the sector; `X_A X_B` preserves it. Thus one may not simultaneously use unrestricted independent B interventions and the claim that all resulting states remain in this physical sector. Z_B preserves the sector. Which operations are physically admissible and local is a model question; constraints do not automatically select an actual universe.

This comparison matters for both zero and subject plurality: nonzero local model quantities can be mutually constrained without an outside matching agent, and a shared physical constraint need not imply just one subject. But the two qubits, their local observables, their constraint and signs do **not** establish actual subjects, felt quality, physical gravitational energy or the total energy law. Opposite values do not erase a negative lived occurrence.

## 3. Verification and next step

[Tests](verification/zero_incidence_locality_balance_rigor_test.py) independently check the sharp operator norm bound, its optimal local effect, remote changes, the full-space scalar theorem on a basis of qubit Hermitians, and the constrained-sector counterexample including coherence and operator-domain preservation. The partial-trace proof covers finite dimensions generally. Next connect a **specified** subject-incidence proposal and local-access algebra to an actual candidate constraint, check admissible operations on its physical sector, and derive rather than insert the physical–experiential correspondence and objective whole-level energy.
