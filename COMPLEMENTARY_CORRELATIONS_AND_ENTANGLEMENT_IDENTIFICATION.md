# What complementary correlations establish—and what they leave undetermined

## Main result

The preceding [swapping and selection gate](SWAPPING_HERALDING_AND_PERSPECTIVE_SELECTION_GATE.md) showed that one fixed-basis scan can be compatible with both an entangled and a separable state. There is a stronger, constructive follow-up:

> With trusted qubit measurements, correlations in **two complementary bases** can certify entanglement and put a sharp lower bound on its negativity, without assuming Werner noise. Yet even complete correlations for all measurement directions in the plane spanned by those two bases can leave both the amount of entanglement and the existence of a CHSH violation under other settings undetermined.

This uses established entanglement-witness and CHSH results, not a claim to have discovered either. The explicit three-state comparison below is a finite application to the framework's information-and-measure problem. It strengthens, rather than replaces, the earlier single-basis ambiguity. It is not a reanalysis of the Nobel experiments, evidence for subjects, or a solution of the framework's foundational gaps.

## Source and reading scope

- Tóth and Gühne, [*Two Measurement Settings Can Suffice to Verify Multipartite Entanglement*](https://arxiv.org/html/quant-ph/0409132): all three extracted HTML chunks read. Their stabilizer-witness method for GHZ states includes the two-qubit case; the paper refers detailed proofs to their other work. Figures were not independently inspected. The full underlying proof paper, [*Detecting Genuine Multipartite Entanglement with Two Local Measurements*](https://arxiv.org/abs/quant-ph/0405165), was identified from their references but **not read for this gate**.
- Hyllus, Gühne, Bruß and Lewenstein, [*Relations between Entanglement Witnesses and Bell Inequalities*](https://arxiv.org/html/quant-ph/0504079): first two of seven extracted chunks read, including definitions, witness/Bell distinction and the Horodecki criterion; remaining text and proofs not read. Available, not inaccessible.
- Quan et al., [*Steering Bell-Diagonal States*](https://arxiv.org/html/1601.00113): first three of nine chunks read, including the Bell-diagonal correlation representation and theorem statement; remaining text not read. Available, not inaccessible.
- Jin et al., [*Entanglement Swapping with Quantum-Memory-Compatible Photons*](https://arxiv.org/html/1506.03704v1): **all six text chunks now read**, including the appendix. In the earlier gate only the first chunk had been read. The authors report conditional visibility `56.2 ± 5.7%`, then use tomography to avoid assuming a Werner state and report concurrence `0.36 ± 0.07`. Their stated signal and heralding efficiencies and non-white-noise discussion matter. I did not independently inspect their figures, raw event records, tomography code, or statistical analysis.
- Pan et al., [*Experimental Entanglement Swapping: Entangling Photons That Never Interacted*](https://web.physics.ucsb.edu/~quopt/swap.pdf): extracted main text read previously; see [Nobel audit](NOBEL_ENTANGLEMENT_BELL_TELEPORTATION_SOURCE_AUDIT.md) for provenance and limitations. The authors used additional orientations, not merely one fixed-basis curve. No numbers below are presented as fitted to their experiment.

## 1. Two trusted, complementary measurements

Let `X,Z` be the Pauli operators on each of two trusted qubits, with common, calibrated local reference axes. Write

```text
cx = ⟨X⊗X⟩,    cz = ⟨Z⊗Z⟩,
F = ⟨Φ+|ρ|Φ+⟩,    |Φ+⟩ = (|00⟩+|11⟩)/√2,
N(ρ) = (||ρ^(T_B)||₁ − 1)/2.
```

Here `N` is the convention in which a maximally entangled pair has negativity `1/2`. Under the stated quantum-state and calibration assumptions, the established two-setting stabilizer witness gives

```text
cx + cz ≤ 1                           for every separable state,
F ≥ (cx + cz)/2,
N ≥ max[0, (cx + cz − 1)/2].
```

The sign and target state depend on the basis/label convention; one must choose and document the appropriate local sign relabelings. The first inequality is the `N=2` form of the cited stabilizer witness. For a concise certificate of the other displayed bounds: the commuting `+1` stabilizer projectors have intersection `|Φ+⟩`, so their union bound yields the fidelity bound; the partial transpose of the Bell projector is half the swap operator, giving `F ≤ 1/2+N`. This is a direct application of standard projector and partial-transpose facts, not an independent novelty claim about negativity witnesses.

At `cx=cz=16/25`, we get

```text
cx+cz = 32/25 > 1,
F ≥ 16/25 = 0.64,
N ≥ 7/50 = 0.14.
```

The lower bounds are **sharp given those two constraints**: the first explicit state below attains both. Therefore two complementary correlations can do more than merely distinguish the two examples in the preceding gate: assuming trusted qubits, they exclude every separable two-qubit state, not just the particular separable comparison previously constructed. This conclusion does not require a Werner-state model.

## 2. Three states, identical full planar statistics

Define Bell states as usual and consider the following Bell-diagonal states. Entries in each row are the probabilities of `Φ+`, `Φ−`, `Ψ+`, `Ψ−`:

| State | `Φ+` | `Φ−` | `Ψ+` | `Ψ−` | `⟨YY⟩` | Negativity | optimized `Smax` |
|---|---:|---:|---:|---:|---:|---:|---:|
| Lower-bound saturator | 16/25 | 9/50 | 9/50 | 0 | −7/25 | 7/50 | `32√2/25` ≈ 1.810 |
| White-noise model | 73/100 | 9/100 | 9/100 | 9/100 | −16/25 | 23/100 | `32√2/25` ≈ 1.810 |
| CHSH-violating model | 41/50 | 0 | 0 | 9/50 | −1 | 8/25 | `2√881/25` ≈ 2.375 |

All have maximally mixed local marginals and satisfy

```text
⟨XX⟩ = ⟨ZZ⟩ = 16/25,     ⟨XZ⟩ = ⟨ZX⟩ = 0.
```

Thus, for **any** two locally chosen Bloch directions `n,m` in the `XZ` plane, their full ±1 outcome distribution is identical:

```text
P(a,b | n,m) = [1 + ab (16/25)(n_x m_x+n_z m_z)]/4.
```

No amount of noise-free sampling restricted to this plane can distinguish these three ideal models. This includes all linear-polarization directions under the usual polarization-qubit convention. But the unmeasured `YY` correlations, negativities, and maximal CHSH values differ. The last state violates CHSH using appropriate settings involving the missing direction; it does **not** violate CHSH with settings restricted to the identical `XZ` plane. The other two do not violate CHSH under arbitrary single-copy, two-setting projective measurements, by the cited Horodecki criterion. This is not a statement about every possible Bell scenario or sequential protocol.

The first row attains `F=16/25` and `N=7/50`, proving the bounds in §1 cannot be improved solely from `cx=cz=16/25`, even if the full planar distribution above is also known. A `Y⊗Y` correlation measurement distinguishes these three candidates; full tomography would reveal more. The explicit formulas explain why fitting a single white-noise parameter can give a definite answer that the planar data alone do not warrant.

This is not an isolated numerical accident. For every `1/2 < w ≤ 1/√2`, the two Bell-diagonal states with weights

```text
(w, (1−w)/2, (1−w)/2, 0)
((1+w)/2, 0, 0, (1−w)/2)
```

have identical full `XZ`-plane distributions, both are certified entangled by `cx+cz=2w>1`, but the first has `Smax=2√2 w≤2` and the second has `Smax=2√(1+w²)>2`. The first attains `N=w−1/2`, so the general two-correlator negativity lower bound is sharp throughout this interval. These conclusions follow by applying the cited Bell-diagonal and Horodecki results to the stated families; they are not claimed as new general entanglement theorems.

## 3. Experimental interpretation and an actionable test

A well-controlled experiment could measure the same predeclared heralded ensemble in two complementary bases, record both outcomes and losses, and estimate `cx,cz`. If a **joint** confidence region gives lower bounds `Lx,Lz` with `Lx+Lz>1`, it certifies entanglement within the trusted-qubit description; it also implies `N ≥ (Lx+Lz−1)/2` at that confidence level under the analysis assumptions. The confidence region must account for the actual sampling plan, drift, uncertainty in axes, selection and background corrections. Simply adding two separately quoted one-standard-deviation errors is not automatically a joint confidence statement.

Record the physical outcome alphabet, herald definition, lost trials, calibration and the construction of the paired dataset. If different settings select different uncontrolled subensembles, the two estimates need not refer to a common state and the witness cannot be applied as written. Real photons can occupy additional modes; mapping measurements onto `X` and `Z` needs its own justification. This trusted-device entanglement witness is not a loophole-free Bell test or a device-independent statement.

Jin et al. demonstrate why these caveats matter: their tomography went beyond a Werner assumption, and they discuss non-white noise, finite efficiencies and conditional coincidences. Their result cannot be substituted for the synthetic values in §2. The original Pan et al. visibility is likewise not automatically the two aligned correlators above, nor an error bar for the derived bound. Applying this proposal to those data would require the original setting-resolved counts and calibrations; I have not done that analysis.

## 4. Implication for the relational and experiential account

The constructive lesson is neither that a relation is unknowable nor that more measurements are useless. Two calibrated correlations can establish a relational property and a nonzero **minimum** entanglement; the very same partial evidence can still fail to fix other quantum properties. A framework that proposes a physical relation as a constituent of a perspective must therefore say **which operational equivalence class** it uses, which measurements and selections support it, and which conclusions remain invariant across all states consistent with those observations.

This is a constraint on physical reconstruction, not an experiential bridge. No one of the three states entails a subject, subject count or qualitative experience; different possible subject assignments are not derived from their differing negativities. Nor does the exercise establish that spacetime, measurement choices or the weights of perspectives emerge from a timeless whole. Those remain independent obligations.

## Reproduction

`python verification/complementary_visibility_entanglement_gate.py` uses rational arithmetic to construct the three density matrices, diagonalize their partial transposes by their explicit Bell-diagonal blocks, calculate the Horodecki CHSH expressions from their correlation matrices, and verify 64 complete joint outcome probabilities for rational `XZ`-plane directions. The analytic correlation formula above extends equality to every planar direction; the 64 tests alone would not. The script checks the concrete states and bounds, not the cited general theorems or any experimental data.
