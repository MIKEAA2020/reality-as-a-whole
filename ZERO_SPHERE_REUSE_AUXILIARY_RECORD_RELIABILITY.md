# Recovering a reused record inside the zero-charge sphere history

## Result

I extended the **existing sphere-coupled, 14-tick finite-reservoir clock**, not an independent spectator example. Its first source-reference pair records the sphere sign, and three independently prepared source labels `y₀,y₁,y₂` are routed through a reused working bit. In the original thermal run, only the three reservoir bits `R` are accessible as the record; the best probability of recovering the entire source triple is `9/16`.

The extension copies selected *reset noise* from the same working bit into extra finite memory, using an extra finite energy store. It finds the following **exact** success probabilities, under the access and gate restrictions below:

| Extra memory | Initial preparation | Best full-triple success | What is proved |
|---|---|---:|---|
| none | — | `9/16 = 0.5625` | Original accessible record |
| 1 qubit | pure blank | `3/4 = 0.75` | Achievable; optimal even for arbitrary quantum encoding and decoding within the specified fixed-record access model |
| 2 qubits | pure blanks | `1` | Achievable; one qubit cannot be perfect in that access model |
| 1 bit | Gibbs, `q=1/4` | `9/16` | Optimum in the specified linear controlled-write family |
| 2 bits | independent Gibbs, `q=1/4` | `81/128 ≈ 0.6328` | Optimum in that family; redundant encoding beats naive separate noisy copies |
| 3 bits | independent Gibbs, `q=1/4` | `351/512 ≈ 0.6855` | Optimum in that same family |

Both the original and added signed charges remain exactly zero on every prepared history component. A 14-tick stationary history and its explicit inverse exist, so better **local** record access does not imply fundamental irreversibility. The new initial memories, stores, purification partners, clock and gates are stipulated—not derived from bare zero. The results are not a proof that the universe has zero energy, that experience is additive, or that a subjective experience has been constituted.

Reproduction: [verification/zero_sphere_reuse_noisy_auxiliary_memory_test.py](verification/zero_sphere_reuse_noisy_auxiliary_memory_test.py). The construction inherits the actual old sphere interface and 16-sector checks of [the previous model](ZERO_FINITE_RESERVOIR_RELATIONAL_CLOCK_ARROW.md), rather than reinterpreting an unrelated random input as a sphere signal.

## 1. The original physical starting point

Let `b=0,1` label the two eigenvalues of the old conserved, gauge-invariant sphere observable `B`. Three reference bits `xᵢ` are the readout labels of three initially prepared independent Bell pairs. The original sphere-controlled interface sets

`yᵢ = xᵢ XOR b`.

Every source/reference pair then carries the same B sign, although the source triple `y` itself is uniformly distributed and carries no B by itself. The gauge-compatible B interface disturbs old coherence between B sectors when the added source pairs are traced out; it is not an invisible spectator interaction. Its inverse later restores the complete original old state. For each of the 16 original old clock histories, the previous verifier checked the old constraints and the equal B-sector weights.

The working bit A is written from each `yᵢ` using the existing finite energy store `n`, and then swapped with the initially Gibbs reservoir bit `Rᵢ`. With `fᵢ` denoting Rᵢ's initial computational-basis value, the three `fᵢ` are independent with `P(fᵢ=1)=q=1/4`; each has an explicit purifier `Pᵢ` with the same correlated value. At the forward midpoint,

```text
R = ( y₀, y₁ XOR f₀, y₂ XOR f₁ ),    A = f₂.
```

`R` is uniformly distributed and is independent of `(f₀,f₁)`. The most likely noise pattern is `00`, with probability `9/16`, so guessing it gives the previous full-triple optimum. These labels describe correlations and Born weights; they do not by themselves assert irreducible objective chance or an interpretation of actual incidence.

**What is being recovered?** The full three-bit source triple, not three independent copies of the sphere sign. Each `(yᵢ,xᵢ)` carries the same B; if `R₀` and `x₀` are jointly accessible, B is already recovered perfectly without any new auxiliary memory. Conversely, R alone does not reveal B. Nothing here gives a confined inhabitant access to a source reference or another domain.

## 2. The added memory really uses the reused A

Add `k` memory qubits `C₁,…,Cₖ`, each with gap ε and initial excited-state probability `q_C`. For thermal preparation use `q_C=1/4`, the same initial Gibbs ratio `βε=ln 3` as the original R bits. Each `Cⱼ` is purified by an explicit untouched qubit `Eⱼ`, initially in `√(1−q_C)|0,0⟩+√q_C|1,1⟩`. For pure blanks use `q_C=0`; this is a different initial resource preparation.

Immediately after the first R swap, the **actual working bit A contains f₀**. Immediately after the second, A contains f₁. At each of these moments use A to control writes into selected C bits. No direct access to the source or purifier is needed for the write. The selected pattern is specified by two binary columns `L₀,L₁∈{0,1}ᵏ`:

```text
C = e XOR (f₀ L₀) XOR (f₁ L₁),
```

where `e` is the initial C string. These are controlled XORs in the occupied prepared sector, not free zero-cost operations. They are implemented by a second finite battery D with levels `0,…,2k`, initially `d=k`. Each controlled write swaps `|C=0,d⟩ ↔ |C=1,d−1⟩` where possible and fixes the unpaired endpoint states. It is a bijective, energy-conserving finite-level operation on *all* basis inputs; for the prepared histories there is enough battery range for the required XORs. A is left unchanged by this copy. With k=0 there is no extra memory or battery action.

The original signed charge and the new one are separately

```text
Q_old/ε = (n−3) + A + Σ(Rᵢ−Pᵢ),
Q_aux/ε = (d−k) + Σ(Cⱼ−Eⱼ).
```

Both are zero in every initially prepared component and remain zero under every gate; endpoint rules also conserve each corresponding charge off the prepared sector. The negative purifier terms and reference offsets are model choices. This exact constrained charge is **not** a demonstration of an objective whole-universe energy or a literal energetic interpretation of the sphere sign.

At the midpoint the allowed reader can use only all three R bits and all C bits, including a joint optimal measurement. It cannot use A, the source/reference pairs, either battery, the purifiers, or the old sphere. In this prepared model the relevant conditional R–C states are diagonal after tracing those excluded systems, so maximum-likelihood classical decoding is also optimal among quantum POVMs on R and C for the stated preparation.

## 3. Exact recovery and a restricted but strong lower bound

Because R is uniform independently of the two relevant noise bits, reconstructing `y` from R and C is equivalent to identifying `(f₀,f₁)`. Their probabilities are

```text
P(00)=9/16,   P(01)=P(10)=3/16,   P(11)=1/16.
```

**One pure blank:** copy `f₀` into C, and guess `f₁=0`. The probability of recovering all of y is `3/4`. Two pure blanks can copy `f₀,f₁` separately and recover y with certainty.

This is more than a comparison of those two algorithms. Fix the original R readout as a classical register with its original joint distribution, and allow **any** encoding into an accessible d-dimensional quantum memory, with any POVM on it conditional on R. Do not allow access to other side information. For every R value, recovering y is equivalent to identifying one of the four noise patterns above. Let `M_f` be the conditional POVM effects. Since each encoded state is a density matrix,

```text
P(success | R) = Σ_f p_f Tr(M_f ρ_f)
              ≤ Σ_f p_f min(1, Tr M_f),   Σ_f Tr M_f = d.
```

The right-hand side is at most the sum of the d largest prior weights. Thus `d=1` gives `9/16`, `d=2` gives `3/4`, and `d≥4` gives at most `1`. The explicit zero-charge gates achieve all three bounds. In this fixed-R, no-side-information access model, **one additional qubit is necessary and sufficient to exceed `9/16`; two are necessary and sufficient for perfect recovery**. The bound includes mixed initial memories and arbitrary quantum encodings into that final accessible dimension, but it does not apply if one changes the R register/distribution, accesses other registers, or uses a larger final accessible system.

This is a *memory dimension and accessibility* bound, not a general lower bound on low-entropy resource consumption. An arbitrarily designed device might use other systems as side information or alter R. A clean bit's initial purity and the battery's sharp energy are explicitly prepared resources here.

## 4. Why two noisy bits can help when one does not

In the specified **linear controlled-write family**, C starts as independent `q_C=1/4` Gibbs bits and each output is a noisy XOR of a chosen linear combination of `f₀,f₁`. Exhaustively search all `2^(2k)` choices of the two columns and use the optimal decoder:

```text
P_success(L) = Σ_c max_f P(f) P(e = c XOR Lf).
```

For `k=1`, every such code has optimum `9/16`: a single noisy observation is not strong enough to overcome the prior odds of 3:1 between `00` and either single-error pattern. In contrast, with `k=2`, one optimal code copies **the same `f₁` into both C bits**. Guess `f₀=0`; guess `f₁=1` only when both C bits are 1. The `f₁` success is `27/32`, giving `3/4 × 27/32 = 81/128`. Copying `f₀` and `f₁` separately into two noisy bits gives only `9/16`: each individual observation has the same error rate as simply guessing zero.

For `k=3`, the exact exhaustive search gives `351/512`. These statements are not claims of optimality over arbitrary nonlinear, coherent, adaptive, or additional-resource protocols. In particular the `9/16` result for **one thermal bit** is a result for the listed family, not a theorem that every possible use of a Gibbs qubit is useless.

The prior's asymmetry matters: a maximally mixed added bit with the same XOR encoding gives no information about the noise; the pure blank gives a perfectly distinguishable record. With q=1/4 the initially thermal bit has entropy `h₂(1/4)≈0.8113` bits. Two such marginals have entropy `≈1.6226` bits, or `≈0.3774` bits of entropy deficit relative to two maximally mixed bits; this number is **not** by itself a complete work or thermodynamic-resource comparison, since their energy, purifiers, batteries and correlations also matter.

## 5. Energy and exact reversal

The original A/R/store dynamics are unchanged because the added controls leave A unchanged. In units ε, their mean midpoint changes remain `Δn=−1`, `ΔA=+1/4`, `ΔΣR=+3/4`. For the added device:

| Protocol | Initial mean ΣC | Midpoint mean ΣC | Midpoint mean d | Δd |
|---|---:|---:|---:|---:|
| one pure bit copying f₀ | `0` | `1/4` | `3/4` | `−1/4` |
| two pure bits copying f₀,f₁ | `0` | `1/2` | `3/2` | `−1/2` |
| two thermal bits both copying f₁ | `1/2` | `3/4` | `7/4` | `−1/4` |

These are expectation values of the stipulated finite stores, not a full work accounting: the stores and memories can become mixed and correlated. Purifier energies remain fixed and balance the initially excited C components. We have not re-thermalized the new bits or paid for restoring the preparations. Their being initially Gibbs does not turn them into an infinite heat bath.

For the clock, insert each controlled auxiliary write immediately after its corresponding old swap, bundling it with that clock step. In the return half, reverse the auxiliary writes in reverse order **before** undoing their old swaps. All 14 conditional steps are reversible, and their composition is identity. The test constructs the coherent extended history using orthogonal B-sector, source-reference, and purifier labels and checks `D|H⟩=|H⟩`, with both signed charges zero at every tick. The old B control and old gauge compatibility are inherited; the additional operations do not act on the old sector.

Consequently, a reader restricted to R and C can see improved or degraded records at different clock readings, while the complete constructed state can be uncomputed exactly. No claim is made that a real observer has access to the whole inverse, that time's arrow is solved, or that all apparent dissipation is avoidable without resources.

## 6. Connection to the universal-principles question

The experiment sharpens the proposed distinction between **trigger**, **balance** and **record**. An A-controlled gate can direct a larger set of auxiliary changes, but the explicit energy store—not an unequal positive term magically canceling a larger negative one—pays their local energy change. A matched signed bookkeeping term balances each history. A local record can improve through redundant processing without becoming a permanent global ledger.

This is useful for the user's zero proposal in a limited but concrete way: *zero net modeled charge does not prohibit a locally meaningful asymmetric control, reliable records or local energy redistribution*. It does not establish that those ingredients are necessary consequences of zero's constitution. The gate law, initial low-entropy states, subsystem boundaries, observer access and the interpretation of a record as experienced remain explanatory demands. Nor does equal physical charge balance imply a compensating signed felt valence. A framework identifying experience as intrinsic and matter as extrinsic still owes the explicit composition and incidence bridge, including the status of suffering; no such bridge is smuggled in here.

A useful next discriminator would remove the artificially fixed R register: compare alternative zero-charge, same-total-dimension encodings while counting **all** accessible outputs, preparations and stores, then ask whether zero plus a principled symmetry can select one of them. Only such a selection would begin to address why this record structure rather than its equally admissible rivals arises. The current result provides a concrete bound against which those alternatives can be compared; it does not itself select them.

## Reproduce and scope

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.zero_sphere_reuse_noisy_auxiliary_memory_test -v
```

Seven tests check the finite write on all basis inputs; all prepared branches, clock ticks and linear codes through k=2; exact inverse on arbitrary basis inputs including battery endpoints for a representative code; the coherent stationary clock history; exact likelihood calculations and exhaustive linear codes through k=3; pure-blank controls; and mean energy. The general dimension bound above is analytic, not a numerical proof of arbitrary implementations. The old 16-history gauge/sector checks are in the inherited verifier.
