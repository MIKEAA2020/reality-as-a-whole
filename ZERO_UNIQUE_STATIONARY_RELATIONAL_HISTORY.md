# A unique zero-eigenstate for an entire relational history

## The advance

The [previous construction](ZERO_ALL_HISTORY_COMPLEMENTARY_BALANCE_RECORD_CLOCK.md) showed that nontrivial record dynamics can remain in the same exact complementary-zero kernel at every internal clock reading. But it took a suitable initial kernel state as an input. Here we formulate the **entire clock–record history as the unique zero eigenstate of one explicit, time-independent operator**. No temporal preparation is needed to state the eigencondition.

The construction is exact in the finite model. It also makes the remaining dependence explicit: the complementary balances and clock condition by themselves leave **eight** states. Three additional, chosen relational constraints reduce that space successively to four, two and finally one. A continuous family of alternative constraints yields different, equally unique zero states. Thus the result is a concrete stationary zero-eigencondition, **not** a proof that zero alone determines this history or that a nonzero-balance seed can dynamically relax into it.

The selected minimal history can be mapped isometrically to the earlier coherent two-sector state, with its old clock and laboratory degrees retained. But this mapping is built from that already specified state; its projectors are generally nonlocal and state-dependent. It is not a derived physical preparation or a mechanism that independently generates the old lab amplitudes.

Executable checks: [verification/zero_stationary_whole_unique_history_test.py](verification/zero_stationary_whole_unique_history_test.py).

## 1. Reduce the earlier zero sector to its logical content

Work on the active R–W–T–F space. The earlier conditions are

```text
C₁=C₂=C₃=0,          L=+1,
H_cas = (C₁²+C₂²+C₃²)/8,
K = (I−H_cas)(I+L)/2.
```

The explicit definitions of `C_i` and `L` are in the [previous report](ZERO_ALL_HISTORY_COMPLEMENTARY_BALANCE_RECORD_CLOCK.md). `H_cas` and `(I−L)/2` are commuting projectors. `K` is their common-zero projector, of rank two. On this kernel the operators

```text
X_L = X_R J_W X_T,       Z_L = Z_R
```

form logical Pauli operators. Introduce a reference/pointer qubit B and a memory M. B is initially an abstract two-dimensional encoding of the retained old degrees of freedom—not an assertion that an individual old observer has access to it. Define the internal Hamiltonian and the two-level clock isometry as before:

```text
H = ω X_L + g Z_L Y_M,       ν = √(ω²+g²),
P_± = (I±H/ν)/2,
W = |+⟩_C P_+ + |−⟩_C P_−,
𝒞 = H − ν Z_C.
```

B is a spectator under H. We use `ω=1/2`, `g=1` for the numerical example. W here is an **isometry** from the B–R–W–T–F–M system into the clock-extended whole; it should not be confused with the earlier work register W. It is unitary onto its image, `W†W=I`, and `𝒞W=0`.

The clock condition alone is highly degenerate. Even after imposing the complementary balances and `L=+1`, the stationary kernel has dimension

```text
2 (B) × 2 (logical L) × 2 (M) = 8.
```

This count is verified directly. It identifies the missing selection rather than hiding it inside the word “zero.”

## 2. Three relational selectors

On the clock-free system choose three commuting involutions:

```text
A₁ = Z_B Z_L,       A₂ = X_B X_L,       A₃ = Z_M.
```

The first says that B and the logical record agree in Z; the second fixes their complementary relative phase; the third chooses M's ready state. `A₁` and `A₂` commute because both their B and logical factors anticommute. All three commute with the complementary balances and L. They are **additional constraints**, not consequences of those balances.

Dress their violation projectors into the stationary whole:

```text
R_j = W (I−A_j) W† / 2,             j=1,2,3,
Q_clock = 𝒞²/(4ν²),
Q_balance = H_cas,                  Q_branch = (I−L)/2,
H_whole = Q_balance + Q_branch + Q_clock + R₁ + R₂ + R₃.
```

Identities on omitted factors are understood. Each displayed term is a positive projector; the six projectors commute. In particular, the `R_j` are **clock-dressed**: even when the corresponding undressed `A_j` does not commute with H, the dressed constraint commutes with `𝒞`. They encode relational conditions on the entire history, not a sequence of interventions in external time.

The numerical spectrum and projector algebra give

```text
rank ker(Q_balance+Q_branch+Q_clock)                 = 8,
rank ker(Q_balance+Q_branch+Q_clock+R₁)              = 4,
rank ker(Q_balance+Q_branch+Q_clock+R₁+R₂)           = 2,
rank ker(H_whole)                                     = 1.
```

The unique normalized zero eigenvector is, up to overall phase,

```text
|Ω⟩ = W [ (|0⟩_B |0⟩_L + |1⟩_B |1⟩_L)/√2  ⊗ |0⟩_M ],
```

where `|0⟩_L,|1⟩_L` are the two normalized vectors in K with Z_L eigenvalues `+1,−1`, and `|1⟩_L=X_L|0⟩_L`. For the chosen unit coefficients the smallest nonzero eigenvalue is **1**. The numerical coefficient and spectral gap are properties of the stipulated constraint operator; multiplying it by a positive scale changes the gap but not its kernel. `H_whole` is not identified with objective cosmological energy.

Since the sum is positive, `H_whole|Ω⟩=0` is equivalent to each of its six terms annihilating `|Ω⟩`. It also implies `C_i|Ω⟩=0`, `L|Ω⟩=S|Ω⟩=|Ω⟩` and `𝒞|Ω⟩=0`. These are exact properties of the unselected stationary vector.

## 3. The unique state contains the earlier nontrivial history

For the phase readout of the finite reference clock, the conditional system vector at phase θ is

```text
|ψ(θ)⟩ = exp(−iθ H/ν) |ψ(0)⟩,
|ψ(0)⟩ = (|0⟩_B |0⟩_L + |1⟩_B |1⟩_L)|0⟩_M/√2.
```

Every conditional vector and the stationary whole satisfy the same `C_i=0`. The phase POVM is nonorthogonal, so a precise phase is a probability-density statement; finite windows are handled in the preceding report. For R measured in Z and M in X, the joint probabilities are

```text
P(r,m | θ) = [1+r m (g/ν) sin(2θ)]/4,      r,m∈{+1,−1}.
```

At θ=`π/4` the ideal-reading mutual information is approximately `0.701882` bits. It vanishes for that readout at `π/2`; at `π` the conditional state returns up to phase. This is a reversible relational record correlation, not a permanent memory or a realized subjective outcome. The full cycle-averaged R–M_X correlation vanishes, as independently checked in the previous verifier.

## 4. Connection to both old sectors and all old clock labels

The existing normalized code and complement vectors have a Schmidt decomposition across `(old environment)` versus `(R,W,T,F)` with equal weights. More explicitly, choose the same logical `|0⟩_L,|1⟩_L` as above; for the stated coherent superposition of both sectors there are orthonormal old-environment vectors `|f₀⟩,|f₁⟩` such that

```text
|old balanced state⟩ = (|f₀⟩|0⟩_L + |f₁⟩|1⟩_L)/√2,
V|0⟩_B=|f₀⟩,       V|1⟩_B=|f₁⟩.
```

The verifier constructs `f₀,f₁` from the actual earlier arrays, checks their orthonormality, and reconstructs both normalized sectors and coherent combinations, including the earlier `1/128` and `127/128` sector weights. The sector flag in this calculation is a direct-sum representation of the already distinct physical sector embeddings; it is kept coherent, not dephased. The old relative clocks and lab records are inside `f₀,f₁`, not thrown away. In particular, applying any of the old clock-label effects to the reconstructed state reproduces its action on the original state by linearity. Their 16-label constraint preservation is separately checked in the previous all-history verifier.

One can lift the selectors into the larger environment using V and add the positive environment-support constraint `I−VV†`. The resulting full construction selects the mapped history, with all the old degrees retained. But this is **not a free derivation**: V was obtained from the particular old vector. Its two environment states encode that vector's sector amplitudes, lab correlations, clock resources and phases. The support and selector operators need not be local or accessible to a confined inhabitant. The test shows an exact embedding, not that these large, state-dependent operators arise naturally or that an observer can measure them.

## 5. Why uniqueness under a specified operator is not uniqueness from zero

Replace only `A₂` by

```text
A₂(φ) = (cos φ X_B + sin φ Y_B) X_L.
```

It still commutes with `A₁`, `A₃`, and all the original balance conditions. Repeating the construction produces a unique zero state `|Ω_φ⟩` for **every** φ, with

```text
|⟨Ω₀|Ω_φ⟩|² = cos²(φ/2).
```

The family includes orthogonal states at `φ=π`. In the fixed reference/readout algebra, the ideal θ=0 joint witnesses satisfy

```text
⟨X_B X_L⟩ = cos φ,       ⟨Y_B X_L⟩ = sin φ.
```

Thus a phase choice can change observable joint correlations if this B phase reference and these observables are physically available. If the relevant rotation is instead a gauge redundancy, its physical status must be justified; it is not settled by the matrix alone. Either way, the construction shows that **zero eigenvalue plus the previously specified balances and clock does not mathematically select φ**. The same goes for the selection of a memory-ready orientation, the environment isometry and the dynamical coefficients.

Nor does this evade the conservation obstruction. `H_whole` commutes with C₁, so closed evolution generated by it preserves `||C₁ψ||`. It cannot take the previous nonzero-C₁ seed into the C₁-zero kernel. A unique zero eigenvector is a timeless **constraint specification**, not a claim that the system dynamically arrived there from that seed.

## 6. Consequence for the proposed zero constitution

This construction sharpens the route from zero to a Hamiltonian: one can explicitly exhibit a positive, time-independent `H_whole` whose **unique zero eigenstate** contains a balanced internal history, record motion and finite clock-relative memory correlations. It shows that a whole-level eigencondition need not be a frozen, empty internal structure.

The no-residue demand now falls on the displayed ingredients: why these representations, why these relational selectors rather than their alternatives, why this environment embedding and these couplings, and why the particular physical and experiential interpretation? The model does not settle which possibilities are genuine, whether all are actual, how incidences are measured, or whether an opposite physical sign corresponds to opposite felt valence. Nor does it identify the constraint with a globally meaningful gravitational energy. An individual instance of suffering would not become unreal through a proposed signed total.

A constructive next task is to investigate whether a principle stronger than mere zero eigenvalue can determine the selector algebra or make the apparent φ-family physically equivalent **without** simply declaring alternatives impossible. Another is to replace the state-dependent environment projector by a physically justified local or covariant mechanism. Neither step is accomplished by the present uniqueness theorem.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_stationary_whole_unique_history_test \
  verification.zero_invariant_all_history_record_clock_test -v
```

The tests cover exact projector commutation, kernel ranks and gap, the stationary and conditional balances, nontrivial readouts, the φ-family, the old-environment isometry and the no-relaxation obstruction. NumPy is required. They do not establish a physical preparation, locality, cosmological energy, actual outcomes, subjecthood, experience or metaphysical necessity.
