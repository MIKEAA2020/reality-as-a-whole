# Bell-pair preparation versus an infinite-temperature correlation

## Result

The [supplied Fischer et al. experiment](STRUCTURAL_EXPERIENTIAL_INTELLIGIBILITY_TWO_PAPER_AUDIT.md) measures a single-qubit expectation in a specially prepared state. For its particular dual-unitary circuit and observable, that expectation has the special interpretation of an infinite-temperature two-time correlation. The authors explicitly warn that this identification ceases to hold for their off-dual-unitary data.

A precise all-size check shows **why one must not transfer that interpretation automatically**. For the same `|+⟩` plus Bell-pair preparation, a single-qubit measurement after an otherwise arbitrary unitary can differ from the corresponding infinite-temperature correlator by as much as

```text
2(1 − 2^(−(N−1)))    for odd N ≥ 3.
```

This bound is sharp over unrestricted global unitaries. It approaches the algebraic maximum of 2 with increasing `N`; it is **not** a bound on the specific kicked-Ising perturbation in the experiment. A three-qubit, explicitly local gate gives a discrepancy of 1. This is a mathematical test of an interpretation, not a finding about the experiment's measured data.

A practical repair follows: estimate the actual correlation using two additional preparations, `|+⟩` and `|−⟩` on the first qubit, each with a maximally mixed remainder, and take half the difference of their measured signals. No dual-unitarity assumption is needed for this identity in the ideal unitary model. Implementing and validating it on a real device would require its own noise and sampling analysis.

The calculation is a project-specific application of standard quantum state distinguishability, not a claimed invention of the trace-norm bound or dual-unitary correlation theory. It improves a **structural** test only. Experience remains a valid datum, and neither this result nor information scrambling supplies the experiential constitution required for full structural **and experiential** intelligibility.

## 1. Same preparation, two different quantities

For odd `N=2m+1≥3`, let the first qubit be in `|+⟩` and let each remaining adjacent pair be in the Bell state `|Φ+⟩=(|00⟩+|11⟩)/√2`. Write

```text
D = 2^(N−1) = 4^m
P± = (I ± X₀)/2
B = |Φ+⟩⟨Φ+|^(⊗m)          on the remaining N−1 qubits
ρ = P+ ⊗ B
σ = P+ ⊗ I/D.
```

For an arbitrary `N`-qubit unitary `U`, let `O=U† Xₙ U`, with `Xₙ` a single-qubit Pauli X. It is Hermitian, unitary and traceless. Define the two quantities, in the same mathematical setting, as

```text
A = Tr(ρ O)                          prepared one-point expectation
C = Tr(X₀ O)/2^N                    infinite-temperature correlation.
```

Because `Tr(O)=0`, `C=Tr(σ O)`. Thus

```text
A − C = Tr[(ρ − σ) O].
```

The operational issue is immediate: `ρ` contains Bell-pair correlations; `σ` has the same first-qubit preparation but a maximally mixed remainder. Equality of their one-point expectations depends on the evolved observable and the circuit. It is not an automatic consequence of the state of qubit 0 alone.

For the experiment's **specified dual-unitary model and preparation**, the cited authors establish the equality and the exact analytic expression in their stated range. Their point is not contradicted here. The general identity above explains why an extension to a different circuit needs proof or measurement rather than simply retaining the earlier label.

## 2. Sharp bound and saturating observable

The known trace-norm inequality gives `|Tr(ΔO)| ≤ ||Δ||₁ ||O||∞` for `Δ=ρ−σ`. For this preparation,

```text
Δ = P+ ⊗ (B − I/D)
||Δ||₁ = (1−1/D) + (D−1)/D = 2(1−1/D).
```

The positive eigenvalue `1−1/D` occurs once, the negative eigenvalue `−1/D` occurs `D−1` times in the `P+` sector, and `Δ` vanishes in the `P−` sector. Since `||O||∞=1`, this gives the announced bound. The trace-distance/optimal-discrimination connection is standard; see Barnett and Croke's [*Quantum state discrimination*](https://arxiv.org/html/0810.1970).

The traceless, Pauli-spectrum restriction does not prevent saturation. Choose any normalized vector `|v⟩` in the remainder and put

```text
O* = P+ ⊗ (2B−I) + P− ⊗ (I−2|v⟩⟨v|).
```

Each block is a Hermitian unitary; `Tr(O*)=0`, so `O*` has equally many `+1` and `−1` eigenvalues. Hence some global unitary `U*` satisfies `O*=U*†XₙU*`. Its expectation is `A=1`, while `C=−1+2/D`, and therefore `A−C=2(1−1/D)`. This construction does **not** assert that the maximizing unitary is local, shallow, experimentally available, or a kicked-Ising circuit.

| Qubits | Remainder dimension D | Maximum `|A−C|` |
|---:|---:|---:|
| 3 | 4 | 3/2 |
| 5 | 16 | 15/8 |
| 7 | 64 | 63/32 |
| 91 | 2⁹⁰ | 2(1−2⁻⁹⁰) |

The last row is a mathematical worst case, **not an error estimate for the 91-qubit device**. Neither equality nor maximal difference follows merely from size or chaos. The construction's purpose is to establish that the interpretation requires structural information beyond the single prepared expectation.

## 3. Explicit three-qubit local control

For qubits `0,1,2`, use the same input `|+⟩₀|Φ+⟩₁₂`, and measure `X₁` after the two-qubit unitary

```text
U(θ) = exp(−i θ Z₁Y₂).
```

It acts only on the already Bell-paired qubits, not on qubit 0. Direct Pauli algebra gives

```text
U†X₁U = cos(2θ) X₁ − sin(2θ) Y₁Y₂,
A = sin(2θ),        C = 0.
```

At `θ=π/4`, the prepared expectation is `1` while the correlator is `0`; at `θ=0` both are zero, but equality fails continuously as the gate is changed. This is an explicit bounded counterexample using a local operation, not a claim that it is a perturbation of the Fischer kicked-Ising gate or that it simulates quantum chaos. It also illustrates why a selected vanishing correlation is not, by itself, the absence of a physical record or any experiential occurrence.

The [verifier](verification/bell_preparation_correlation_gate.py) checks the three-, five- and seven-qubit saturating constructions, constructs a saturating three-qubit unitary, and checks three local-gate settings. Numerical checks complement the algebra above; they are not an experimental test.

## 4. A direct operational check of the correlation

Define two reference input states

```text
σ+ = P+ ⊗ I/D,      σ− = P− ⊗ I/D,
A± = Tr(σ± U†XₙU).
```

Then for **any** unitary U,

```text
(A+ − A−)/2 = Tr(X₀ U†XₙU)/2^N = C.
```

In an ideal implementation, the maximally mixed remainder can be realized by uniformly randomizing independently over each pair's four Bell states and averaging, or by another correctly randomized preparation of `I/D`. Measure the same final observable for the original Bell input and for both reference ensembles. Their difference tests whether the special one-point/correlation identification holds in the circuit actually run, including off the analytically solved point.

This is a **proposed protocol**, not an assertion about results already obtained. On hardware, prepare and readout errors, drift, randomized-ensemble finite sampling, learned noise, mitigation bias, covariance and uncertainty across the three preparations all need accounting for. Predetermine reference ensembles, calibration, shot budget, randomized order, estimand and acceptance criterion; do not calibrate the same data used as the independent benchmark. Noise-corrected agreement is only as reliable as its assumptions. Neither a successful operational test nor disagreement alone establishes anything about phenomenal experience.

## 5. Framework connection and remaining obligations

- **Structural intelligibility and physics alignment:** this supplies an exact preparation-dependent diagnostic that can be used against an assumed physical realization. It does not derive the circuit, spacetime, gravity or its laws from the proposed timeless whole.
- **Experience and experiential intelligibility:** the framework takes actual experience as valid evidence. No count of qubits, correlator value, dual-unitarity condition or entropy yields subject incidence, felt quality or first-person structure. A proposed experiential constitution must connect its independently stated experiential and physical terms without simply defining the answer.
- **Plural subjects and substrate independence:** the circuit's arbitrary tensor decomposition and the observable's support do not by themselves determine subject boundaries or substrate-independent identity. Any candidate rule must survive relevant redescriptions and specify which local structures count.
- **Generativity and parsimony:** the new two-reference check provides a concrete prospective discrimination between two *physical estimands*. It does not distinguish experiential and neutral bases that are constructed to share all physical and experiential predictions. A criterion for experiential fundamentality, necessity and self-sufficiency remains an independent requirement; parsimony cannot be claimed just from using this short formula.

Thus the result strengthens a bounded interface under C4–C5 while explicitly leaving **full structural and experiential intelligibility** unmet. It neither denies experience nor proposes that the whole is a universal subject or agent.

## Source and reading scope

- Fischer et al., [*Dynamical simulations of many-body quantum chaos on a quantum computer*](https://doi.org/10.1038/s41567-025-03144-9): the previously supplied eight-page article, including methods and main figures, was read and inspected; see the [source audit](STRUCTURAL_EXPERIENTIAL_INTELLIGIBILITY_TWO_PAPER_AUDIT.md). Its [supplement](https://static-content.springer.com/esm/art%3A10.1038%2Fs41567-025-03144-9/MediaObjects/41567_2025_3144_MOESM1_ESM.pdf) and [data/code record](https://doi.org/10.6084/m9.figshare.29069759) failed to load through the page-fetch tool and were not audited. No claim is made that they are globally unavailable. The actual experiment is not reanalyzed here.
- Barnett and Croke, [*Quantum state discrimination*](https://arxiv.org/html/0810.1970): HTML chunks 1–2 of 18 were previously read and chunk 1 revisited; the remaining available text and its figures were not independently inspected. The trace-distance result is standard prior work, not attributed as a new result of this gate.
- Bertini, Kos and Prosen, [*Exact Correlation Functions for Dual-Unitary Lattice Models in 1+1 Dimensions*](https://doi.org/10.1103/PhysRevLett.123.210601): abstract/search excerpts only, full source not read. Cited as prior work identified by Fischer et al.; no independent derivation audit is claimed.
