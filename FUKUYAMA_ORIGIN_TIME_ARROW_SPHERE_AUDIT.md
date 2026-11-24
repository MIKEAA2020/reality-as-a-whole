# Fukuyama on cosmic origin and the arrow of time: audit and constructive connection

**Continuation:** [recollapse, sphere and record arrows in one constraint](ZERO_RECOLLAPSE_SPHERE_RECORD_ARROWS.md) constructs a dynamical turning geometry coupled to the actual sphere code, with explicit boundary and sequential-measurement controls.

## What the paper adds

The attached [paper](sources/uploads/Revisiting_the_Origin_of_the_Universe_and_the_Arro.pdf) is Takeshi Fukuyama, “Revisiting the Origin of the Universe and the Arrow of Time,” *Symmetry* **17**, 1688 (2025), [DOI](https://doi.org/10.3390/sym17101688). It discusses tunnelling/no-boundary cosmology, intrinsic clocks and a two-sided thermodynamic arrow. Its explicit clock/arrow construction uses a reduced **two-dimensional Jackiw–Teitelboim (JT) gravity** model; the author expressly says the four-dimensional extension has not been shown. The paper is relevant prior work, not a proof of our zero-point/sphere thesis or of general quantum gravity.

The strongest connection to our work is not the familiar idea that time can be internal, which both approaches already assume. It is the distinction between:

1. a geometry variable reaching a turning point;
2. a particular local clock coordinate becoming nonmonotonic;
3. a coarse-grained or decoherence arrow reversing; and
4. a subject's experienced or remembered direction.

These are not automatically the same event. Below we verify the paper's displayed Wheeler–DeWitt mode, identify a likely error in a printed classical equation, quantify the clock turning point, and give two exact counterexamples to overreading a coherence-width plot as a general thermodynamic theorem. We also construct a small, explicitly constrained two-sided record model. None of these checks reproduces the paper's cited 1989 influence-functional calculation in full.

The uploaded PDF has 11 pages and SHA-256 `22f4acce91b5c074d00b6a1b53ebe6708b77bbff699acf8f62db2353796fc2cb`. The journal HTML was checked against the PDF where mathematical text extraction was ambiguous. Tests: [verification/fukuyama_origin_arrow_audit_test.py](verification/fukuyama_origin_arrow_audit_test.py).

## 1. Claims and their scope

In §2 the paper reviews a particular closed FRW tunnelling construction with a scalar potential and a classically forbidden small-a region. It describes `a=0` as “nothing,” and proposes that the initial singularity is avoided by tunnelling. In §§3–4 it uses a homogeneous two-dimensional JT model, solves a Wheeler–DeWitt equation, introduces different local dynamical-time variables, and argues that the thermodynamic arrow reverses relative to a parameter at maximum expansion. The thermodynamic proxy is a **decreasing off-diagonal coherence width** of a matter-reduced density matrix. Its influence-functional calculation is referred to the earlier 1989 paper [1](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.39.462).

This is substantially more specific than “no external time.” A local clock patch, a choice of wavefunction, matter tracing, a preferred variable/coarse-graining, and boundary conditions are all part of the argument. The exact two-dimensional mode is a useful calculation, but it does not automatically establish a physical inner product, finite measurement protocol, four-dimensional arrow, or actual experience. “Quantum to classical” here refers to the author's decoherence proxy, not a demonstration that fundamental quantum coherence ceases everywhere or that a definite outcome is selected.

The author's use of “nothing” is not identical to the user's proposed self-sufficient zero with intrinsic sphere. A vanishing FRW scale factor is a configuration or boundary in a theory that already specifies action, fields and a wave equation; it does not by itself derive the theory, objective whole-energy zero, internal directions, subjects or experience. Conversely, identifying that gap does not refute the user's thesis.

## 2. Exact Wheeler–DeWitt mode and a printed-equation issue

For `Λ=−α²`, the reduced Wheeler–DeWitt equation (paper Eq. 30) is

```text
∂_N∂_χ ψ − α² N e^(2χ) ψ = 0.
```

For nonzero complex `c₁` the paper's mode is

```text
ψ(N,χ)=c₀ exp[c₁N²/2 + α² e^(2χ)/(2c₁)].
```

It does solve this equation: `∂_Nψ=c₁Nψ` and `∂_χψ=(α²/c₁)e^(2χ)ψ`, so the mixed derivative is `α²Ne^(2χ)ψ`. The current conservation claimed in Eqs. 32–33 also follows for this mode. These are exact checks of the displayed mathematical solution, not a complete verification of the physical solution space.

For `c₁=−β+iγ`, β>0, its modulus is Gaussian in N and `e^χ`; however, it approaches a nonzero function of N as χ→−∞. It is therefore not square-integrable under the **flat** measure `dN dχ`. That observation is not a claim that it is inadmissible under the appropriate physical/Klein–Gordon inner product, which may differ, or that suitable wavepackets cannot be built. The article does not establish those extra claims merely by displaying this mode.

### A likely typo in the printed classical equation

The uploaded PDF and the published HTML both print Eq. 24 as

```text
χ̈ + χ̇ = Λ,
```

then give `χ=ln[a_max sin(αt)]` with `Λ=−α²` in Eq. 28. These statements do **not** agree as written. For α=1 and t=π/3, the printed left side is `−4/3+1/√3≈−0.756`, not `−1`. The trajectory instead obeys

```text
χ̈ + χ̇² = −α².
```

The following printed N equation (25) is satisfied by `N=A cos(αt)` with that trajectory. This looks like a missing square, but that is an inference; the calculation above does not establish the author's intended correction or invalidate every later argument. We use the **explicitly stated trajectory** for the following clock check, not the inconsistent printed equation.

## 3. A scale turning point is not the same as a clock breakdown

Take the paper's Eqs. 28–29, α>0 and A>0:

```text
a=a_max sin(αt),       N=A cos(αt),       χ=ln a,
σ₋=(χ−N)/√2,           σ₊=(χ+N)/√2.
```

The maximum of a is at `αt=π/2`. Direct differentiation gives

```text
dσ₋/dt = α[ cot(αt)+A sin(αt) ]/√2,
dσ₊/dt = α[ cot(αt)−A sin(αt) ]/√2.
```

At maximum expansion, `dσ₋/dt=αA/√2>0`, so this particular clock does **not** turn there. Its turning point A is later, at

```text
cos(αt_A) = [1−√(1+4A²)]/(2A),      π/2 < αt_A < π.
```

For A=1, `αt_A≈2.2370`, versus `π/2≈1.5708` at maximum expansion. The paper's Fig. 2 likewise distinguishes A from B, the maximum. We also independently check its trajectory relation `σ₊(t)=σ₋(π/α−t)`.

This does not disprove a two-sided arrow. It does show why **clock-patch failure at A alone cannot establish an entropy-arrow reversal at B**. One must also specify the physical orientation and the actual coarse-grained history. On an overlap, if `W` is the same scalar diagnostic,

```text
dW/dt = (dW/dσ₋)(dσ₋/dt) = (dW/dσ₊)(dσ₊/dt).
```

A derivative's sign can change because a new coordinate is oppositely oriented, without changing the physical direction of a fixed history. Conversely, a genuine change in the entropy gradient is not erased by renaming the clock. A probability-current component likewise needs an oriented surface and a physical inner product; a negative component in one chart should not automatically be called a negative operational probability. We have not reconstructed the paper's full clock-transition or its underlying 1989 influence calculation, so this is a distinction and a specific check, not a claim to have disproved its model.

This directly complements [our geometry-clock work](ZERO_TWO_WINDOW_FULL_SLICE_CLOCK.md): unitary transport of a complete state and its observables between good slice representations is not by itself a derivation of a thermodynamic arrow. Our scalar-clock band model does not contain this closed recollapsing trajectory, so its observed memory stability is not evidence for or against a reversal at maximum expansion.

## 4. Narrower off-diagonal width need not mean larger entropy

The paper takes the direction of decreasing coherence width σ² as its thermodynamic proxy. A narrower width may indicate decoherence **under additional fixed coarse-graining and state assumptions**, but it does not generally determine the entropy direction by itself.

Consider the following normalized positive density operator on `L²(R)`:

```text
ρ_(a,b)(x,y)=√(2a/π) exp[−a(x²+y²)−b(x−y)²],    a>0, b≥0.
```

It is positive because it is a Gaussian mixture of phase-kicked pure Gaussian states. At fixed midpoint `(x+y)/2`, its off-diagonal factor has the paper's form with

```text
σ²=1/(a+2b),          Tr ρ²=√[a/(a+2b)].
```

Its eigenvalues are `(1−q)q^n`, where `q=(1−√[a/(a+2b)])/(1+√[a/(a+2b)])`; hence its von Neumann entropy is `S=−ln(1−q)−q ln(q)/(1−q)`. For the two valid states:

| a,b | σ² | purity | von Neumann entropy, nats |
|---|---:|---:|---:|
| 1,1 | 1/3 | 0.57735 | 0.79395 |
| 4,1 | 1/6 | 0.81650 | 0.36410 |

The off-diagonal width **narrows while entropy decreases**. The diagonal distribution changes too; that is exactly why a width alone is insufficient. Our test independently diagonalizes a discretized kernel and reproduces the entropy. This counterexample is not the 1989 cosmological density matrix and does not show that its particular plotted width behaves this way; it identifies the extra information needed to infer a thermodynamic arrow from such a width.

More generally, subsystem entropy, coarse-grained thermodynamic entropy, decoherence, and subjective felt duration are related but distinct quantities. A globally pure state can have nonzero subsystem entropy, and unitary evolution alone does not make a record irreversible.

## 5. A constructive two-sided record model—with a boundary control

To connect the paper's proposal to our record work, take two qubits S,E with

```text
H = g X_S X_E,          C=p_t+H=0,
ψ(t)=exp(−iHt)|00⟩ = cos(gt)|00⟩−i sin(gt)|11⟩.
```

Here t is an ideal internal clock in a Page–Wootters/deparametrized model, not a fundamental external time. The history is an ideal generalized solution; no normalizable clock wavepacket is supplied. On `0≤t≤T=π/(2g)`, the reduced S entropy and the mutual information of computational-basis S/E readouts are both

```text
S_S(t)=I(S_z:E_z)=H₂(sin²(gt))  bits.
```

They begin at zero, reach one bit at `t=T/2`, and return to zero at T. For a *separately stipulated* recollapsing diagnostic `a(t)=a_max sin(πt/T)`, the record/entanglement arrow points toward maximum a from both ends. This is an exact illustration of two-sided internal arrows in one globally pure, reversible system. The prescribed a(t) is not derived from the constraint, S and E are not demonstrated subjects, and the finite system recoheres rather than providing irreversible thermodynamics.

The boundary control is decisive. Keep the **same H and the same a(t)**, but start instead in

```text
|ψ_δ(0)⟩=cos δ|00⟩−i sin δ|11⟩,       δ=π/8.
```

Then `S_S(t)=H₂(sin²(gt+δ))`; at t=T/4 it is 1 bit, whereas at the mirror reading 3T/4 it is zero. Its maximum is no longer tied to the maximum of a. Thus neither a recollapsing scale factor nor reversible dynamics alone forces a symmetric record arrow; initial correlations/boundary conditions matter. This is a deliberately different physical preparation, not a coordinate change. It does not settle which boundary condition the user's necessitarian proposal would require.

## 6. Curvature, topology and inflation

The paper's abstract says only a closed universe is free of singularities. Its actual construction uses particular FRW matter and boundary assumptions; the unrestricted statement is too broad. For example, spatially flat `k=0` FLRW with `a(t)=cosh t`, in units `8πG=1`, has

```text
H=tanh t,      ρ=3H²,      p=−(2 sech²t+3H²),
ρ+p=−2 sech²t<0,
R=6(1+tanh²t),       R_abcd R^abcd=12(1+tanh⁴t).
```

Curvature scalars are finite for every t and its causal geodesics are complete: a≥1 bounds the rate of affine/proper parameter accumulation away from zero as t→±∞. This explicitly uses **null-energy-condition-violating matter**, unlike the standard positive-energy setting; it is a counterexample to the unrestricted assertion, not a solution within the paper's original scalar model or an observational proposal. Here ρ itself is nonnegative: `ρ+p<0` is not by itself negative total energy or a globally cancelling energy ledger.

Separately, the open de Sitter patch `a=H⁻¹ sinh(Ht), k=−1` has constant curvature invariants despite `a→0`; that patch is geodesically incomplete and extendable, so curvature regularity alone is not geodesic completeness. Also k describes local spatial curvature, not by itself whether a global topology is compact.

The printed potential `V=ρ_v−m²φ²/2`, if taken as a complete global potential with nonzero m, is unbounded below and has no stable symmetry-breaking minimum; it can instead be interpreted as a local hilltop approximation with stabilizing terms supplied elsewhere. The article does not derive such a completion from zero. Inflation's occurrence also does not by itself establish natural low-entropy boundary conditions: the paper's own cited Carroll–Chen discussion [1](https://arxiv.org/abs/gr-qc/0505037) treats that initial-condition question as nontrivial and proposes additional cosmological assumptions.

Finally, the paper explicitly contrasts its symmetric-arrow proposal with the result of Hawking, Laflamme and Lyons [1](https://arxiv.org/abs/gr-qc/9301017), who study density perturbations and argue that their thermodynamic arrow continues through recollapse. These are **different models and boundary/perturbation assumptions**; neither result is established as a model-independent theorem merely by citing it. We inspected their abstract for the contrast, not their entire derivation.

## 7. Implication for the zero–sphere programme

The paper strengthens our research direction in a concrete way: a viable whole-level model should compare clock patches, record formation and coarse-grained entropy **in the same constrained state**, and check whether an arrow depends on its boundary conditions. The toy above shows how two-sided record arrows can coexist with an internally timeless constraint without positing an external time. It also shows why symmetry of the whole does not alone settle a local arrow.

The paper does not derive the sphere from zero, establish objective whole-energy zero, determine actual subject incidences, or explain why physical records are felt. No experiential total follows from a vanishing constraint or a coherence width. If a justified globally signed experiential sum vanishes, local negative felt valence is not erased. The user’s proposed necessity of all genuine possibilities remains a substantive proposal: neither the paper nor these conditional counterexamples identifies which histories are genuinely possible or actual.

A useful next calculation would add a genuinely recollapsing geometry and environment to the **existing autonomous sphere–memory constraint**, compare boundary states with the same physical operators, and compute record persistence and entropy on each branch after transporting observables between valid clock patches. That would be a new constrained model; the idealized qubit example here does not already do it.

## Reproduce

```sh
python -m pip install --target .arena/python-deps numpy  # if needed
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest verification.fukuyama_origin_arrow_audit_test -v
```

The tests check Eq. 30–31 and current conservation, the printed Eq. 24 discrepancy, the two local-clock derivatives and their turning points, the explicit regular flat bounce and open patch, the Gaussian density spectrum and entropy, and the two record-arrow preparations. They do not verify the full 1989 influence functional, a measured cosmological entropy arrow, quantum-gravity singularity avoidance or actual experience.
