# Two autonomous records in the constrained geometry–sphere model

## Result

The preceding model had one memory inside the constraint but needed an additional external projection to compare a past pointer reading with later memory. Here **two memory qubits are included in the same closed constraint**, coupled to the pointer through different finite-resolution geometry windows. There is no intermediate projective operation or externally scheduled on/off switch in the primary calculation.

For a selected packet, the first memory begins changing before the second; both later retain correlated readout statistics. With a balanced pointer preparation, their final z-readouts agree with probability **0.8682** and have mutual information **0.4247 bits**. The same calculation includes geometry, the encoded sphere–record logical qubit, pointer and both memories.

This is a finite, reversible, imperfect record model—not proof of irreversible history, definite unmeasured earlier outcomes or experienced time. The scalar clock is still ideal, the geometric interaction is band-projected and nonlocal, the windows overlap, and the underlying constraint and parameters remain assumed. The model's genuinely different window operators also mean the previous one-window continuum slice theorem **cannot simply be imported**.

Code: [verification/zero_autonomous_two_window_records_test.py](verification/zero_autonomous_two_window_records_test.py). Previous model and domain encoding: [autonomous pointer–memory](ZERO_AUTONOMOUS_SPHERE_GEOMETRY_POINTER_MEMORY.md) and [domain/code recovery](ZERO_DOMAIN_SECTOR_CLOCK_RECOVERABILITY.md).

## 1. A single autonomous constraint

Retain `p=p_α∈(−7,−6)`, scalar φ, the two encoded sphere–record levels `h=0,1`, pointer D, and two memory qubits M₁,M₂. Let `P₁ᴰ=(I−σ_zᴰ)/2`. For the same finite-resolution Gaussian-smoothed α-window as before, define its shifted, band-compressed effects

```text
E_a(p,q) = exp[−i(p−q)a] K(p−q),
K(x)=exp(−x²/2) sin(2x)/(πx),      0≤E_a≤I.
```

Choose three geometry centers and coupling strengths

```text
a_D=−5,    a₁=0,    a₂=5,
λ=0.5,     κ₁=0.65, κ₂=0.65.
```

The sole selected rescaled constraint is

```text
C̃ = p_φ²/2 − p²/12 + h
     + λ E_(−5) σ_yᴰ
     + κ₁ E_0 P₁ᴰ σ_yᴹ¹
     + κ₂ E_5 P₁ᴰ σ_yᴹ² = 0.
```

Thus

```text
Θ = p²/6 − 2h − 2[λ E_(−5) σ_yᴰ
                    + κ₁ E_0 P₁ᴰ σ_yᴹ¹
                    + κ₂ E_5 P₁ᴰ σ_yᴹ²],
p_φ=Ω=√Θ,          U(φ)=exp(iΩφ).
```

All couplings are independent of φ and included in Θ. Because `||E_a||≤1` and the spin factors are contractions,

```text
4 − 2(λ+κ₁+κ₂) ≤ Θ ≤ 49/6 + 2(λ+κ₁+κ₂),
0.4 ≤ Θ ≤ 11.7666667.
```

Hence Ω is a well-defined bounded positive self-adjoint operator on the specified physical Hilbert space, including both encoded h sectors and the three qubits. The reduced scalar-clock evolution is exactly unitary, and it lifts to the selected positive-frequency constraint branch using the earlier physical inner product. No external time is required, although the scalar reading used below is an idealized internal clock.

The interactions are **continuously present**, with strength conditioned on the internal geometry observable. The windows are not sharp gates: E_a are positive effects with finite width, and band projection makes them nonlocal in α. They overlap and have tails, so this construction does not impose a perfect order or a perfectly local crossing. Their locations, strengths, initial state and band are chosen for this test, not derived from zero.

## 2. An unmeasured pair of records

Use the earlier normalized geometry packet initially centered near α=−15 and the sphere–record logical state `(|0⟩+i|1⟩)/√2`. Initialize both memories in z=0. For the main run prepare D in the balanced state `|+y⟩=(|0⟩+i|1⟩)/√2`, which tests the memories against two initially balanced D_z alternatives. This is a **chosen input**, not evidence that a detector has already selected an outcome. Because it is a σ_y eigenstate, the first detector term alone does not flip this particular pointer preparation; the D=0 incident control below tests a detector flip separately.

At N=80 momentum samples the memory marginals are:

| Scalar reading φ | `Pr(M₁=1)` | `Pr(M₂=1)` |
|---:|---:|---:|
| 20 | 0.05475 | 0.00862 |
| 30 | 0.30366 | 0.12673 |
| 40 | 0.43360 | 0.35479 |
| 60 | 0.43124 | 0.41539 |
| 100 | 0.43271 | 0.41709 |
| 150 | 0.43220 | 0.41767 |

M₁ responds earlier for this preparation and arrangement. That is an observed feature of the calculated **probability history**, not proof that every branch has a single sharp trajectory or that the stored bits alone reveal a unique sequence of crossings.

At φ=100 the actual joint memory readout distribution is

| M₁ | M₂=0 | M₂=1 |
|---|---:|---:|
| 0 | 0.509184 | 0.058104 |
| 1 | 0.073726 | 0.358986 |

The agreement probability is `0.868170`; the mutual information is `0.424712` bits. In particular, `Pr(M₂=1 | M₁=1)≈0.8296`, whereas `Pr(M₂=1 | M₁=0)≈0.1024`. Both are calculated from the one unmeasured closed-system state at φ=100; no projection was inserted at φ=30 or 40.

At φ=100 the three window expectations are approximately `(0.000621, 0.000634, 0.000443)`. The joint memory distribution changes by less than 0.003 in total absolute difference between the sampled readings φ=100 and 150. This shows finite-interval numerical persistence, **not** strictly permanent storage: the total evolution is unitary and reversible, and the effects never have perfectly compact support in the band-limited representation.

## 3. Controls: disturbance, input and coherence

**Second-record backaction.** If the second coupling is removed (`κ₂=0`) while all other initial data are matched, `Pr(M₁=1)` at φ=100 is approximately 0.424870 rather than 0.432712. The later record changes the first one's statistics. Different couplings define different physical models, not different coordinate descriptions of the same experiment.

**Receding packet.** With the geometry packet instead centered near α=+15 and moving away in the selected branch, the same φ=100 calculation gives `Pr(M₁=1)≈0.000906` and `Pr(M₂=1)≈0.002458`. This is a matched control for this packet/window arrangement, not a universal first-crossing probability.

**Detector initially at D=0.** For the incident packet, the final pointer probability is `Pr(D=1)≈0.97774`; memory marginals are `Pr(M₁=1)≈0.85660` and `Pr(M₂=1)≈0.82311`. Because those readouts are strongly biased, their 0.7419 agreement hides a mutual information of only about 0.00126 bits. High agreement by itself is not reliable evidence of useful records.

**Matched incoherent pointer mixture.** Replacing the initial balanced coherent D state by the equal incoherent mixture of D=0 and D=1 gives final memory mutual information about **0.4178 bits**, close to 0.4247 for the coherent preparation. Their distributions differ, but the correlation is largely also present in the mixture. It should not be presented as a distinctive quantum-interference effect.

No intermediate pointer value was measured in the primary model. The conditional couplings establish physical correlations in a unitary state; assigning an actual earlier outcome, an observer, or a felt memory needs a separate interpretation or physical incidence account. The optional projective history in the earlier report is a different intervention.

## 4. Clock comparison and the confined domain

The earlier single-window model admitted a full-state continuum geometry-slice map for almost every α after diagonalizing its constant internal coupling into scalar spectral channels. Here the shifted E_a do **not** in general commute after band compression, and `σ_yᴰ` does not commute with `P₁ᴰ`. There is no common fixed internal diagonalization of the previous kind. The positive root and scalar-clock physical evolution above are valid, but a full geometry-slice reconstruction and its domain for this new multi-window operator remain to be proved. A change of numerical basis is not by itself a geometry-clock switch.

The sphere logical h remains an engineered encoding in the earlier code. The new Θ acts on the logical index, geometry and D/M registers without acting on the confined label itself. The prior environment-isometry theorem therefore keeps the confined subsystem decoupled from arbitrary reference information carried by those degrees of freedom; one momentum/two-memory projected output is checked directly using the actual environment vectors. This is not evidence that a confined inhabitant registers either memory, or that the nonlocal encoded Hamiltonian is a physical local coupling.

## 5. Numerical method and limitations

The continuum operator is bounded and its positive-root bound above is analytic. Numerical figures use Nyström momentum meshes and Chebyshev approximation to `exp(iφ√Θ)`, treating all three qubits and both h sectors. The tests compare N=40,80,160, check φ=100 and 150 at polynomial degrees 260 and 320, and compare the full complex state against an independently diagonalized N=32 matrix. Degree 150 is deliberately shown to fail at φ=150: convergence cannot be inferred from running the code once. All quoted probabilities use the converged settings; no rigorous continuum error bound is claimed.

A stable statistical correlation in a reversible finite model is not an irreversible record, thermodynamic arrow, actual subject or observation. The window interaction is nonlocal after projection, memory levels carry no independent energy or entropy cost, and the ideal scalar clock and initial state are stipulated. The work does not establish a preferred foliation or the full inhomogeneous gravitational constraints; it also does not derive these structures, subjective incidence or a global signed experiential total from zero. Local suffering would remain real under any justified whole-level balance.

## 6. Next step

Analyze the **multi-window continuum spectral and geometry-slice problem**, rather than reusing the scalar-channel proof: establish what information its geometry slice retains, accounting for multiplicity and noncommuting interactions. In parallel, replace the compressed-window qubits with an explicitly local apparatus and finite-resolution scalar clock, and examine whether record persistence survives when memory resources and an environment are included. These are physically distinct tests: merely extending the numerical sequence does not establish a solution to the general problem of time.

## Reproduce

This test uses NumPy; no dependency is committed into the repository. If needed:

```sh
python -m pip install --target .arena/python-deps numpy
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest verification.zero_autonomous_two_window_records_test -v
```

The tests cover positivity, shifted window calibration, unitary evolution, independent dense diagonalization, resolution and polynomial convergence, temporal marginals, joint memory statistics, second-record backaction, receding and incoherent controls, on-branch constraint cancellation, and a confined-reference reduction. Numerical tests are not continuum spectral proofs or evidence of actual experience.
