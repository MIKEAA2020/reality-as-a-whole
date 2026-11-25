# A nontrivial relational history inside the complementary-zero kernel

## Result

The preceding [autonomous program](ZERO_AUTONOMOUS_BALANCED_REFERENCE_RELATIONAL_CLOCK.md) conserved the declared charges, but its unselected history did not obey the proposed complementary zero at every clock reading. Here is a different construction that **does**:

- Start with the existing all-sector internal-reference state in the exact common kernel of the three complementary balances `C₁,C₂,C₃`, with `L=S=+1`.
- Construct a time-independent Hamiltonian that commutes with **all** those operators, the orientation charge and the previously declared work charges.
- Add one explicit neutral memory and one finite internal reference clock. The normalized stationary constraint state, the unselected whole, and **every conditional reference-clock reading** retain the same complementary zeros.
- The history is nevertheless nontrivial: the current record can change and a new memory becomes correlated with it. For one specified setting, an ideal clock reading gives **0.702 bits** of record–memory mutual information and a **0.1** probability that the current record differs from the earlier copied Bob pointer.

This is an exact conditional finite-model solution to the specific all-history constraint problem. It is not yet a derivation of the zero-whole, the Hamiltonian, the clock, a subject or actual experience. In particular, it **starts inside** the common kernel rather than dynamically preparing that kernel from the earlier uncorrelated seed. The construction also uses explicit potentially nonlocal interactions and a periodic, finite-resolution clock; it is not a demonstration of a relativistic, irreversible measuring apparatus.

Verifier: [verification/zero_invariant_all_history_record_clock_test.py](verification/zero_invariant_all_history_record_clock_test.py).

## 1. The invariant zero kernel has an internal logical degree of freedom

The [reference construction](ZERO_RELATIONAL_ORIENTATION_AND_INTERNAL_REFERENCE.md) defined the active R–W–T–F system and

```text
U₀ = −Z_R X_W X_T,       U₁ = −Z_R Z_W X_T,
C₁ = U₀−X_F,             C₂ = U₁−Y_F,
C₃ = J_W+Z_F,             L = Z_R J_W Z_T,
S = (U₀ X_F+U₁ Y_F)/2.
```

The common state has `C_i|Ψ⟩=0` and `L|Ψ⟩=S|Ψ⟩=|Ψ⟩`. Earlier we found a two-dimensional common kernel—one dimension for each R value. This round uses, rather than discards, that degeneracy. Define

```text
X_L = X_R J_W X_T,        Z_L = Z_R.
```

On the active space `X_L²=Z_L²=I` and `{X_L,Z_L}=0`. Both commute with each `C_i`, L and S, so they are nontrivial operators **inside** the same exact balanced sector. `X_L` flips the current R and T labels while acting on W. It does not flip Bob's original pointer, so after this operation R is no longer necessarily a faithful copy of that earlier pointer. No traveler or player is identified with the confined record register.

This supplies a concrete physical alternative to treating a vanishing whole as featureless. It does not derive why this encoded algebra is the unique constitution of zero: the active representation, the internal reference and the specified operator factors are still inputs.

## 2. A time-independent memory interaction preserving every zero

Add a neutral memory qubit M initially in `|0⟩`. Set

```text
H = ω X_L + g Z_L Y_M,
ν = √(ω²+g²),             ω=1/2,  g=1.
```

The two terms anticommute on the active space, so `H²=ν²I` and

```text
U(θ)=exp(−iθ H/ν)=cos θ I−i sin θ H/ν.
```

Because both logical operators commute with the balances,

```text
[H,C_i]=[H,L]=[H,S]=[H,J_W+Z_F]=0.
```

Thus if the state starts in the specified common kernel, it remains there at **all** θ. This is an actual operator commutator, not an expectation cancellation or a different balance defined at every reading.

The verifier extends W from its active pair to the original 16-state four-bit work register and checks the commutators there, together with all previously specified total-work and work-pair number operators. It also verifies that the encoded `X_R` can be implemented by swapping the two physical record states `|01⟩` and `|10⟩`, conserving their pair number. The old labs and clock factors are untouched; M and the new reference clock are assigned neutral old energy. The old declared zero-energy and directional constraints are therefore retained as in the prior model. Neither that bookkeeping nor the new constraint below proves objective cosmic energy zero.

The Hamiltonian includes an explicit multiregister `X_R J_W X_T` interaction and an R–M interaction. The test establishes their algebraic existence, not their spacetime locality, material implementation, switching cost or derivation from zero.

## 3. One stationary whole, with nontrivial relational readings

Use a two-level internal reference clock C with energies `+ν,−ν`. On the active space let

```text
P_± = (I±H/ν)/2,
W|ξ⟩ = |+⟩_C P_+|ξ⟩ + |−⟩_C P_-|ξ⟩,
𝒞 = H − ν Z_C.
```

`W†W=I` and `𝒞W=0`. The projectors commute with all the complementary balances, L and S, so W intertwines them exactly. Consequently the **whole stationary state itself**, not merely its selected final branch, is in their common zero/eigenvalue sectors. This applies linearly to the coherent code/complement superposition and all earlier clock labels.

For the finite clock phase states `|θ⟩=(e^(iθ)|+⟩+e^(−iθ)|−⟩)/√2`, `0≤θ<π`, the effects `2|θ⟩⟨θ|dθ/π` resolve the identity. The normalized conditional internal state is `U(θ)|ξ⟩`; the phase density is `1/π`. This phase POVM is nonorthogonal and its exact real-valued reading is a probability-density statement. It is not an operationally derived detector, an actual selected outcome, or an externally preferred time coordinate.

The verifier separately checks both physical lab sectors and **all 16** pre-existing relative-clock branches. The new Hamiltonian acts on different factors, so the old clock instrument and this evolution commute. The coherent sector superposition is never replaced by a flag-dephased mixture.

## 4. Explicit record dynamics and finite-resolution results

Initially the current R equals the earlier copied Bob pointer j, and R has an unbiased marginal in either normalized lab sector. Read M in the X basis, with outcomes `m=±1`; write the current R value as `r=±1`. At an ideal clock phase θ the model predicts

```text
P(r,m | θ) = [1 + r m (g/ν) sin(2θ)]/4.
```

At `θ=π/4`, `g/ν=1/√1.25≈0.894427`. The two diagonal probabilities are approximately 0.473607 each and the off-diagonal probabilities 0.026393 each. The mutual information is **0.701882 bits**. At that reading the probability that the current R differs from its earlier Bob-pointer value is **0.1**. This is real state evolution of the specified encoded operators while all the complementary constraints remain exact.

For a finite phase window centered at `π/4` with half-width `π/8`, the window probability is 1/4 and the conditional record–memory agreement is approximately **0.902634**, with mutual information **0.539409 bits**. These are correlations in specified readout statistics, not proof of a conscious report or a selected occurrence. Reading or comparing R and M requires the stated interface; it is not automatically available to a separate confined system.

Two matched controls distinguish the roles of the two interactions:

- `ω=0`: R stays equal to the old pointer while the memory becomes perfectly correlated with R at the corresponding reading.
- `g=0`: R can change, but M carries no information about it in the X readout.

The clock is cyclic. At `θ=π/2` the chosen R–M_X table is uniform again, and at `θ=π` the state returns up to an overall phase. Ignoring the new clock over its complete phase cycle also leaves this particular R–M_X table uniform. Thus the result is **clock-relative, reversible correlation**, not a permanent record or irreversible arrow.

## 5. The preparation obstruction is still present

This construction answers the prior *compatibility* question: nontrivial relational motion and record correlations can coexist with the same exact complementary zeros at every reading. It does not derive the initial zero state.

Indeed, the earlier upstream product seed has `||C₁|seed⟩||²=2`. Since `[H,C₁]=0`, the norm of `C₁|Ψ⟩` is constant under this closed evolution. The verifier checks that the earlier seed keeps norm-squared 2 at several readings. Therefore this particular Hamiltonian **cannot** convert that seed into the common kernel while preserving C₁ throughout. Starting inside the kernel, or deriving a different whole-level constraint that includes compensating resources, is necessary for this route. This is not a general no-go theorem for all zero-whole theories.

The order of the remaining work is now sharper:

1. Derive why the common-kernel state and the internal work/reference pairing are intrinsic to zero, rather than prepare them as inputs.
2. Derive or constrain the encoded Hamiltonian and its coefficients; the symmetry permits many invariant dynamics, not just the one used here.
3. Build a physically localized, autonomous memory/clock interface and account for its full resources and any irreversible record.
4. Establish actual subject incidences, their accessible relations and a signed experiential quantity. None follows from the logical qubit or memory correlation; a balanced quantity would not erase local suffering.
5. Connect the conserved quantities to an objectively meaningful whole-level account in an emergent or covariant physical theory.

The new result makes the demand more concrete: **zero at every internal reading is compatible with a nontrivial encoded record history**, given the displayed algebra and initial state. It does not show that these ingredients already follow from zero itself.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_invariant_all_history_record_clock_test -v
```

The eight tests cover the exact commutant/logical algebra, physical work and record extensions, stationary constraint and clock isometry, all sectors and old clock labels, finite-window statistics, controls, periodicity and the outside-kernel obstruction. They do not establish objective total energy, operational spacetime locality, actual outcomes, subjecthood, experience, or metaphysical necessity.
