# Abaee's process-recovery distinction in the autonomous clock model

## Why revisit the DOI?

The supplied [Zenodo DOI](https://doi.org/10.5281/zenodo.21795780) is the same Amin Abaee preprint already examined in [our earlier audit](ABAEE_NO_UNIVERSAL_PROCESS_CURRYING_SPHERE_AUDIT.md): *No Universal Process Currying: The Intercept Principle, Environmental Currying, and Finite-Dimensional Obstructions to Exact Process Storage, Evaluation, and Recovery*, v4, published 4 August 2026. The record calls it a preprint; that is not evidence of peer review. The earlier audit inspected selected claims and did not run the supplementary verifier. This continuation focuses on the later **autonomous two-memory model**, rather than repeating the original audit or claiming a complete verification of the paper.

Abaee's central categorical claim concerns a natural universal representation of **all** processes in specified finite-dimensional channel categories. It is not a claim that no single interaction can ever be reversed. The paper also recalls a different, standard result: a specified quantum channel has an exact CPTP left inverse on all its inputs precisely when a complementary channel carries no input information. A fixed code and its tailored recovery are not a universal processor.

## 1. A continuum recovery test inside our constrained model

Take a controlled limit of the [two-window constraint](ZERO_AUTONOMOUS_TWO_GEOMETRY_WINDOW_RECORDS.md): retain h=0, turn off the detector rotation and second memory, and retain the finite-window coupling between pointer D and M₁,

```text
λ=0,   κ₂=0,   κ₁=κ=0.65,
Θ = T − 2κ E_0 P₁ᴰ σ_yᴹ,      T=p²/6,
U(φ)=exp(iφ√Θ),               0≤E_0≤I.
```

M starts in z=0, and f is any normalized geometry-band wavefunction. The branch is positive: `Θ≥6−1.3=4.7`. Define

```text
Ω₀=√T,        Ω₊=√(T−2κE_0),        Ω₋=√(T+2κE_0),
U_j(φ)=exp(iΩ_jφ).
```

Since D_z is conserved in this controlled model, starting with D=0 leaves M=0. Starting with D=1 gives the M=1 amplitude, up to an irrelevant fixed phase,

```text
[U₊(φ)−U₋(φ)] f / 2.
```

This amplitude is nonzero for all sufficiently small nonzero φ, **for every nonzero f**. To see why, E₀ is strictly positive as a quadratic form: its Gaussian-smeared window is positive everywhere, and a nonzero band-limited function has a nonzero Fourier transform. Thus `T+2κE₀ > T−2κE₀` strictly in quadratic form. The square-root integral representation implies

```text
√(T+2κE₀) − √(T−2κE₀) > 0
```

in quadratic form as well. In detail, with `A=T−2κE₀`, `B=T+2κE₀`, the resolvent difference `(A+t)⁻¹−(B+t)⁻¹` is strictly positive for every t>0 by inverse order, since `B−A=4κE₀` is strictly positive in quadratic form. Integrating it against `√t/π` gives `√B−√A`. The derivative at φ=0 of `(U₊−U₋)f` is `i(Ω₊−Ω₋)f`, which is nonzero. Norm differentiability of the bounded generators then gives a positive memory-1 probability for sufficiently small nonzero φ. The suitable time interval may depend on f; it is not asserted to hold at every later time.

So in this **specific continuum constrained model**, the complementary environment (geometry plus memory) distinguishes two pointer inputs, while the D=0 and D=1 pointer states themselves remain unchanged. Consequently no CPTP operation on D alone can exactly recover **every quantum input** at such a time. A direct demonstration uses `|±⟩=(|0⟩±|1⟩)/√2`: the controlled interaction multiplies their coherence by the environment overlap γ. Because D=1 has a nonzero M=1 component while D=0 does not, `|γ|<1`; their initially orthogonal reduced outputs have trace distance `|γ|<1`. A recovery acting only on D cannot increase trace distance back to 1.

This proves something sharper than “records disturb a system”: the z basis states are individually preserved **exactly**, yet phase information for arbitrary superpositions is not recoverable from D alone. It is a controlled limit of our autonomous model, not a theorem that every record in the full two-window dynamics has the same behavior.

## 2. Quantitative checks at a finite scalar reading

For the previous normalizable packet centered near α=−15, the N=80 Nyström calculation in the QND controlled model gives, at φ=100,

```text
Pr(M₁=1 | D initially 1) ≈ 0.809857,
|γ| for pointer |±⟩ inputs ≈ 0.415473.
```

The D=0 branch has `Pr(M₁=1)=0` exactly in this controlled model. These values are numerical finite-grid illustrations; the strict small-φ nonrecoverability statement above is the continuum analytic result. The test does not supply a rigorous continuum error bound at φ=100.

There is also a quantitative lower bound on any attempted D-only recovery at that specified numerical channel. Let ε be the **larger** of the two output trace-distance errors for the |+⟩ and |−⟩ inputs. By the triangle inequality and trace-distance contractivity,

```text
1 ≤ 2ε + |γ|,      hence ε ≥ (1−|γ|)/2 ≈ 0.2923.
```

This is a lower bound for this pair under the finite-grid channel and the stated trace-distance convention, not an optimum recovery value or a general diamond-norm theorem.

## 3. The actual two-window calculation

We also checked the **unmodified** two-window model with λ=0.5, κ₁=κ₂=0.65, both memories and both logical h components, using pointer inputs D=0 and D=1 and identical geometry/memory preparation. At N=80 and φ=100:

```text
Trace distance between reduced D outputs       ≈ 0.955273,
Trace distance between reduced M₁M₂ outputs   ≈ 0.959535,
Overlap of full evolved input states            ≈ 0.
```

The two initial D states are orthogonal. For this **finite numerical channel**, the D outputs are not perfectly distinguishable, so no D-only recovery can exactly restore both; the two-input worst-case trace-distance error is at least about 0.02236. The separate memory reductions are strongly input-dependent. N=40,80,160 results converge closely, but that is **not** a certified proof of the continuum strict inequality at φ=100.

There is no conflict with global reversibility: geometry + D + M₁ + M₂ evolve by a unitary on the selected physical branch, so access to the coherent full output and the appropriate inverse U† reverses this particular interaction. It is the restriction to the pointer alone, after other degrees of freedom have been ignored, that causes the recovery obstruction. In particular, retaining a quantum memory coherently, discarding it, and retaining an irreversible classical outcome are distinct operations.

The earlier sphere-code recovery is also a different task: its environmental isometry recovers a **specified encoded logical subsystem** after restriction, under its code assumptions. It neither recovers arbitrary states from the present reduced D channel nor supplies the universal process evaluator excluded by Abaee's theorem.

## 4. Meaning for the larger proposal

The useful connection is not that the preprint proves or disproves the point–sphere thesis. It specifies what an internal record can and cannot be assumed to do: the whole can retain coherent information while a subsystem loses recoverability, and a finite memory can record a chosen family of distinctions without encoding and deterministically evaluating every possible quantum process.

This gives a concrete physical distinction between whole-level reversible organization and a domain's restricted access. It does not demonstrate an actual higher realm, a conscious subject, felt duration, signed experiential cancellation or objective total energy zero. The controlled measurement is nonlocal after band projection; the chosen constraint, coupling and state remain inputs rather than consequences of zero's constitution. Local suffering is not erased by a proposed whole-level balance.

## Reproduce

```sh
python -m pip install --target .arena/python-deps numpy  # if needed
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest verification.abaee_autonomous_memory_recovery_test -v
```

The tests verify the finite-grid QND channel, reduced trace distances and full-state orthogonality, and N=40/80/160 convergence for the two-window comparison. They do not run or certify Abaee's supplemental verifier or prove the entire preprint; the continuum QND witness is the analytic argument in §1.
