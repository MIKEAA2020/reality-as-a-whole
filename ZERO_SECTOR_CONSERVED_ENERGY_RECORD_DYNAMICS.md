# Conserved energy exchange writes zero-sector records

## Main result

The earlier [zero-sector memory construction](ZERO_SECTOR_MEMORY_CAUSAL_INCIDENCE_CONSTRUCTION.md) used assigned opposite signs for a record source and receiver. Here the signs instead arise from an actual Hamiltonian exchange in the **same conserved-sphere measurement setting**.

A three-outcome pointer controls two energy-conserving interactions. Each writes a bit of a memory by transferring one energy unit from a corresponding battery. Every pointer outcome leaves a distinct nonblank memory pattern, and in every conditioned outcome the memory energy gained equals the battery energy lost. The pointer, memories and batteries are encoded in physical spin-zero sectors, so the entire evolution also preserves exact physical total spin zero.

This supplies a concrete connection between **relational records, physical conservation, signed local exchange, and the previously derived quantum weights**. The signed quantities are actual model energy changes, not values imposed solely to make a sum vanish. They are not yet shown to be feelings, and the fact that the batteries balance the memories does not establish that the batteries are subjects. The model's conserved bare energy is positive, not an objective demonstration that the whole's energy is zero.

## 1. From the conserved sphere to a three-label record

Use the asymmetric [five-ray construction](ZERO_SPHERE_CONSERVATION_QUANTUM_PROBABILITY_BRIDGE.md), with intrinsic triple fractions

```text
q₀ = 1/8,      q₁ = 2/5,      q₂ = 19/40.
```

As in the [zero-sector sphere instrument](ZERO_INVARIANT_SPHERE_STEERING_INSTRUMENT.md), encoded four-spin systems `A,B` are prepared in a logical singlet, and a six-spin zero-sector pointer `R` is coupled to `A` using the stipulated POVM `F_i=2q_iΠ_i`. The post-instrument state is

```text
|Ψ⟩_ABR = Σ_i (K_i⊗I)|Ψ⁻_L⟩_AB |i⟩_R,
K_i = √(2q_i) Π_i,
Pr(i) = q_i.
```

The pointer labels `i=0,1,2` are orthogonal physical spin-singlet states. Preparation, the pointer interaction, the link between ray directions and the logical Bloch frame, and the Born rule are specified inputs. The three outcomes are alternative pointer outcomes, not three simultaneously established experiences.

Add four more four-spin zero-sector logical blocks: memory bits `M₁,M₂` and battery bits `W₁,W₂`. Each encoded bit has logical states `|0⟩,|1⟩`, with bare energy observable

```text
N = |1⟩⟨1| = (I−Z_L)/2.
```

The initial memory and battery state is `|0,1⟩_(M₁W₁)|0,1⟩_(M₂W₂)`. Each battery starts with one unit and each memory starts blank. The complete model uses `4+4+6+4+4+4+4=30` physical spin-½ factors. The factorization, zero-sector encodings and initial battery preparation are assumptions.

## 2. A Hamiltonian rather than an assigned sign

For the first memory channel activate when `R` has label 0 or 2, and for the second activate when it has label 1 or 2:

```text
F₁^R = |0⟩⟨0|_R + |2⟩⟨2|_R,
F₂^R = |1⟩⟨1|_R + |2⟩⟨2|_R.
```

Put `ħ=1` and choose energy and interaction units so that the interaction strength is one. On the encoded sectors define

```text
H₀ = N_M₁ + N_W₁ + N_M₂ + N_W₂,
H_int = Σ_(j=1,2) F_j^R ⊗ (X_Mj X_Wj + Y_Mj Y_Wj)/2.
```

The interaction exchanges a logical excitation between memory and battery when its pointer flag is on. Each logical operator can be realized as an operator within the corresponding physical-spin-singlet subspace, extended by zero outside. Since physical rotations act trivially on that subspace, these observables and the extended interaction commute with the physical total-spin components. The same is true of the pointer flags. Hence a state initially in the individually spin-zero blocks remains in physical total spin zero during the process; no sharp individual constituent spin is required.

Direct operator calculation gives

```text
[H_int,H₀] = 0,
[H_int, N_Mj+N_Wj] = 0  for each j,
[F_j^R,H_int] = 0.
```

So `H₀` and each pair's bare energy are exactly conserved, while the memory and battery energies can change. With the autonomous, time-independent Hamiltonian `H=H₀+H_int`, the evolution on the prepared `H₀=2` sector is the interaction evolution times the common phase `e^(−2it)`. The tests use that equivalent interaction picture.

At `τ=π/2`, the controlled exchange maps an activated pair as `|0,1⟩→−i|1,0⟩`. Both exchanges commute, including when label 2 activates both. Consequently:

| Pointer outcome | Memory `(M₁,M₂)` | Batteries `(W₁,W₂)` | Total memory gain | Total battery gain |
|---|---|---|---|---|
| 0 | `(1,0)` | `(0,1)` | `+1` | `−1` |
| 1 | `(0,1)` | `(1,0)` | `+1` | `−1` |
| 2 | `(1,1)` | `(0,0)` | `+2` | `−2` |

The three patterns are distinguishable, and `(0,0)` is the common blank. A phase accompanies each transfer; it does not alter the stated record and energy probabilities. Under the specified Born rule, the row weights are `q₀,q₁,q₂`. Reading out the record is a further operation; the coherent output state itself does not select a definite experienced row.

## 3. Exact currents and endpoint changes

In the Heisenberg picture, for `H=H₀+H_int`, define the bare-energy current into each memory and battery by

```text
J_Mj = i[H,N_Mj],          J_Wj = i[H,N_Wj].
```

Because each pair's energy commutes with `H`,

```text
J_Mj + J_Wj = 0
```

is an **operator identity**, for all states and at all times. The sign now has an operational meaning: energy enters one block and leaves the other. The flag for each exchange commutes with its current and `F_j^R J_Mj=J_Mj`. This illustrates the earlier [commuting-incidence/current construction](ZERO_LOCAL_INCIDENCE_QUANTUM_CURRENT_CONSTRUCTION.md) with an actual encoded pointer flag, rather than an added independent bookkeeping register. A pointer flag is still not a subject criterion.

For the finite writing interval let `U=exp(−iHτ)` and define the endpoint-change operators on the initial Hilbert space:

```text
ΔN_Mj = U† N_Mj U − N_Mj,
ΔN_Wj = U† N_Wj U − N_Wj,
ΔN_Mj + ΔN_Wj = 0.
```

These are also exact operator identities. In the specified initial energy eigenstate, an ideal initial-and-final energy measurement yields the opposite branchwise changes in the table. At the full-swap endpoint the tested change operator also commutes with its initial local memory energy. This does not mean arbitrary intermediate current values and energy records are simultaneously sharp: in this same model

```text
[N_Mj,J_Mj] ≠ 0.
```

Thus a criterion equating sharp excitation presence with an instantaneous signed current still faces the earlier noncommutation obstruction. The conserved pointer flag commutes with the current because it is a different subsystem, not because the memory's sharp energy does.

## 4. Record, flow and experience are not interchangeable

For the specified initial state, let `p₁=q₀+q₂=3/5` and `p₂=q₁+q₂=7/8`. At an intermediate interaction time `t`, the model gives

```text
⟨N_Mj(t)⟩ = p_j sin²t,
⟨N_Wj(t)⟩ = 1 − p_j sin²t,
⟨J_Mj(t)⟩ = p_j sin(2t) = −⟨J_Wj(t)⟩.
```

At the writing endpoint `τ`, the memory may hold a nonzero record energy but the instantaneous current is zero. If the interaction is left running, the memory occupations return to blank at `t=π`, with phases that need not restore the entire original state; applying the inverse unitary restores it. A stable stored record requires a further physical mechanism, for example a controlled decoupling and storage stage. The previous ideal mismatch-gap construction is a candidate, but joining and autonomously clocking those stages, with an energy budget, is not established here.

This difference bears directly on the experiential proposal. If experience were identified solely with *instantaneous* energy-transfer rate, this idealized state gives no nonzero rate at the writing endpoint even though the record remains present. A proposed relation to sustained experience would therefore need actual ongoing dynamics, a different signed quantity or an explicitly time-extended constitution. This is a constraint on that candidate, not a conclusion that stored information cannot be experienced.

The direction of physical energy transfer is more than an arbitrary reversal of a record-label convention: given the specified local energies and initial battery preparation, the memory gains and the battery loses energy. But physics alone does not identify gain or loss with positive or negative feeling. Reversing the proposed phenomenological identification would leave the measured energy exchange unchanged. There is no inference here that the donor is a suffering subject or that the recipient experiences pleasure; even a justified signed total would not remove suffering.

## 5. The subject boundary is the substantive test

If one **hypothesizes**, for the sake of a test, that only the memory blocks count as subjects and identifies their signed experiential contributions with the memory energy changes, their sum is positive in every row. Its Born-weighted mean is

```text
q₀·1 + q₁·1 + q₂·2 = 59/40.
```

Including the two battery changes gives the exact physical total zero, both per conditioned row and on average. But counting the batteries as experiencing subjects simply because their energy decreases would assume what needs proof. Conversely, this toy example does not rule out a different physical–experiential identity, actual subjects spanning both sides of a boundary, additional experiential incidences, or a whole-level balance in a more complete universe.

This makes the desired integration precise: the proposed constitution must explain **which physical exchanges have actual experiential incidence**, how a subject is constituted and persists, what fixes the sign and quality, and why their actual incidence-weighted sum—not just a physical sum including an unexperienced environment—has the whole's zero. The earlier local-budget construction gives a sufficient accounting condition, not a derivation of that condition from zero.

Unconditioned, the logical state of `B` remains `I/2` throughout this local-in-tensor-factors interaction. This verifies the standard no-signalling marginal in the finite model, not relativistic localization: the controlled interaction may be a many-body, nonlocal operation in an underlying physical layout. The logical Bloch sphere, physical spin singlets and the center-frame sphere remain linked by the earlier explicit identification, not by a derived Lorentz-covariant dynamics.

## 6. What this does and does not establish

The chain now includes a nontrivial physical mechanism:

```text
conserved ray fractions → specified logical quantum instrument
→ spin-zero pointer controls energy-conserving record writing
→ nonzero opposite local energy changes in every recorded branch.
```

The bare energy `H₀` starts at `2` and remains `2`; the interaction term belongs to the full Hamiltonian and is not ignored. Subtracting a constant from a finite Hamiltonian would not derive an objective cosmological zero. Nor does physical spin zero automatically imply zero experiential quantity, no external time, actual subjectivity or a unique complete history.

The result advances the no-residue programme by replacing the earlier *assigned* source/receiver signs with a physically derived exchange, and by locating exactly where physical conservation ceases to be enough. A self-sufficient constitution would still have to make the encoding, dynamics, actual records and physical–experiential relation intrinsic, rather than selecting them as independent inputs.

## Verification

```text
python -m unittest verification.zero_sector_record_energy_exchange_test -v
```

Nine standard-library tests check exact bare-energy conservation and the unitary, commuting exchange channels, the three distinct records and opposite endpoint changes, instantaneous-current identities and noncommutation, time-dependent energy and current expectations, reversibility, the unchanged remote reduced state, and the subject-boundary accounting example. They operate on the finite encoded logical sectors; the preceding zero-sector instrument tests verify the corresponding physical spin-singlet bases. They do not establish an empirical experience identity or a complete physical theory.
