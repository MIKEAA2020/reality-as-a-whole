# A three-direction chirality record on the original spherical echo

## Main result

The [previous symmetry–Langlands pass](ZERO_SPHERE_REPRESENTATIONS_GAUGE_LANGLANDS.md) exhibited a three-direction pseudoscalar but did not couple it to the original recorded echo. This pass makes that connection at the post-echo checkpoint. It supplies a third direction, a neutral pointer, and a bounded rotationally invariant interaction. It acts on the **actual old record vectors and constrained opposite-pair representation**, not just a separate classical sample.

For the full-strength readout on the original normalized uniform four-bin spherical state:

- Each pointer sign has probability `1/2`; conditional on either sign, **all old effects diagonal in the original angular coordinates**, including the full old-record effects and bin tests, have their original probabilities. Both original pair model charges still sum to zero on each recorded branch.
- The new sign is informative about the added relational chirality `t`: `E[t | pointer ±]=±2/9`, and the probability that the pointer sign agrees with the sign of t is `1/2+π/16≈0.69635`. It is an **unsharp** record, not a perfect readout of sign.
- The complete enlarged three-direction state is a common-rotation singlet. Nevertheless the old two-direction subsystem alone is no longer strictly confined to its own rotational singlet: its exact non-singlet weight is `2(1−ln 2)/9≈0.06819`, including in either pointer branch. This is angular-momentum correlation with the new reference, **not** violation of the enlarged common-rotation symmetry.

This is a constructive symmetry-and-backaction result, not a derived apparatus. The third sphere, pointer, interaction, and coupling strength are added inputs. The extra non-singlet component matters if one wants the **old** scalar quotient to remain separately physical: an enlarged diagonal-gauge constraint admits it, while insisting separately on the old constraint forbids treating this output as an unchanged state of that old physical sector.

[Ten executable controls](verification/zero_sphere_chirality_echo_test.py) check the actual N=4 old source histories and pair encoding, continuous spherical integrals, gate unitarity, rotation covariance and the exact singlet-leakage expression. They do not independently prove the original full continuum or physical realization.

## 1. State, measurement and unitary

At the same post-echo checkpoint used in the [spherical lift](ZERO_SYMMETRY_POINT_SPHERE_QUANTUM_PLENITUDE.md), write the old continuous state as a vector-valued function `Ψ(m,n)`. Its values contain the existing old quantum/record factors and may include the finite constrained pair. It is invariant under joint rotations of m and n in the specified scalar representation. For the previously demonstrated four-bin states its norm density is uniform on `S²×S²`; the old record vector changes across the bins. The implementation tests all 16 old source labels and both old sign-pointer values; that finite check does not by itself cover every possible source or the entire clock/reservoir evolution.

Add an independent direction `p∈S²` with normalized round area and a neutral two-level pointer M in `|0⟩`. Set

```text
u=m·n,                     t=m·(n×p),
a_λ(t)=√((1+λt)/2),        b_λ(t)=√((1−λt)/2),
0≤λ≤1.
```

The added input is uniform in p, so its scalar wavefunction is 1. Define the unitary pointwise on the pointer by

```text
U_λ(t) = [[a_λ, −b_λ], [b_λ, a_λ]],
U_λ(t)|0⟩ = a_λ(t)|+⟩ + b_λ(t)|−⟩.
```

The pointer labels `±` are the two orthogonal basis states, not eigenvalues of t. A bounded self-adjoint generator is `H_λ=θ_λ(T) σ_y`, where `T` multiplies by t and `θ_λ(t)=½ arccos(λt)`; `U_λ=e^(−iH_λ)` for a unit pulse. The interaction is explicitly specified, but its physical origin, duration and energetic resources are not derived. For `λ=0`, the pointer is rotated to an unbiased superposition independent of t; no chirality information is obtained.

The effects on the three directions are

```text
E_± = (I ± λ T)/2,       E_+ + E_− = I.
```

Thus the pointer is an unbiased, generally unsharp probe: at a fixed configuration `E[pointer sign|t]=λt`. The gate is a multiplication operator in `(m,n,p)` and the identity on all old record, clock and pair fibers. The associated direct-integral construction is well defined on the specified `L²` carrier; no delta-normalized copies of a continuous angle are introduced.

## 2. What is preserved—and what must be enlarged

A simultaneous proper rotation of **all three** directions preserves t, so U commutes with that enlarged rotation representation. If the original state is an old common-rotation singlet and p starts in the invariant constant wavefunction, the complete recorded output remains a singlet under the enlarged action, including each pointer branch.

The original two-direction frame constraint cannot simply be imposed independently after adding a transforming p. Its old rotational generators act only on m,n, whereas the enlarged constraint acts on m,n,p together. The new state is generally not in the old-only singlet; section 4 calculates the exact amount. Thus the gate preserves the **enlarged** rotational gauge sector, not the old-only rotational gauge sector. In the existing gauge-fixed linked-frame description, extending the link/diagonal action to p is a stated additional construction, not an already implemented independent gauge link for p.

The separate constrained opposite-pair projectors at the anchor are pointwise in the old angular bin and old/pair fiber. Since U is scalar on those fibers and does not change u, it commutes with these projectors. Every component still satisfies the original matching and zero-sum constraints; multiplication by the new pointer amplitudes does not alter either pair sign. The existing explicit finite encoding is checked on source labels 0, 7 and 15 for both signs and all four bins, and the pointwise commutation supplies the general argument. These are the old **model** charges, not an energy accounting for the added p, pointer and interaction.

The scalar t changes sign under an improper reflection. Reflection followed by exchange of the two pointer outcomes maps the recorded output built from an old reflection-even input to itself. For a general old state, it relates the output for that state to the output for its reflected input; no arbitrary old state is assumed reflection invariant. This statement concerns the output on the ready pointer, not invariance of the entire unitary under pointer conjugation. If reflection is itself gauge, the status of a parity-odd t record requires a separate reference/observable analysis.

The old clock/reservoir history is not re-simulated here. On a declared pointwise extension in which the old clock-step gates leave the directional coordinates fixed and act trivially on p and the new pointer, U commutes with those steps, so applying it to a stationary history gives another stationary history. That produces a correlated pointer throughout the history; it does **not** show an autonomous, localized event that starts from a ready pointer at an earlier clock reading. A clock-controlled write with retention and switching would change or extend the dynamics and needs its own construction.

## 3. Exact old-record preservation and chirality statistics

For any fixed m,n, uniform p gives

```text
t = √(1−u²) v,       v uniformly distributed on [−1,1].
```

Hence `E_p[t|m,n]=0` and `E_p[t²|m,n]=(1−u²)/3`. In particular,

```text
E_p[E_±|m,n]=1/2.
```

For any old effect that is diagonal in the m,n coordinates, with arbitrary action on the old record and pair fibers, the **unnormalized** expectation in each new pointer branch is exactly half its old value. After conditioning on that pointer outcome it equals the original expectation. This includes all old-only record observables after tracing out the directional coordinates and any bin-conditioned old-record effects. It does not include arbitrary operators that connect different angular configurations, for which off-diagonal coherence matters.

For the original continuous four equal-width bins, define `q_i=E[t² | u in bin i]`. Exact integration, rather than evaluating at a midpoint, gives

```text
bins:  [−1,−1/2], [−1/2,0], [0,1/2], [1/2,1]
q_i:       5/36       11/36     11/36      5/36.
```

For every tested original source and old sign, each bin has weight `1/4`, so `E[t²]=2/9` and

```text
P(pointer ±)=1/2,       E[t | pointer ±]=±(2λ/9),
E[(pointer sign)·t]=2λ/9.
```

These are predictions for the **added** p and pointer, not a reinterpretation of the earlier spin-chirality sign. Conditioned on a particular old bin, the mean t is `±λq_i`: the old bin remains equally likely, but its geometry influences the magnitude of the new conditional chirality.

Since `E|t|=π/8` for the uniform old angular marginal, if one also had access to the sharp sign of t then

```text
P(pointer sign agrees with sign(t)) = 1/2 + λπ/16.
```

At `λ=1` this is about `0.69635`. This is a model comparison with a sharp sign observable, not a demonstrated real calibration or a claim that t itself is directly accessible. The value is not a joint-distribution claim for the separate old spin-chirality reporter.

## 4. The original singlet acquires an exact non-singlet component

The old-record probabilities above can all agree while the quantum state changes. To see this in an observable, let `P₀^(mn)` project only the original two-direction angular system onto its diagonal-rotation singlet, leaving p, old records and pointer alone. This is the orthogonal projector in the enlarged **unquotiented** carrier, obtained by averaging rotations of m,n while holding p fixed; it is not an operation asserted to be locally available within the old quotient.

At fixed `u`, write `a=√(1−u²)`. In either pointer branch, averaging the square-root amplitude over old-frame rotations yields

```text
c_λ(a) = (1/2) ∫_(−1)^1 √((1+λ a v)/2) dv.
```

Both signs have the same c by `v→−v`. Since each branch has probability `1/2`, its normalized old-only singlet weight at that u is `2c_λ(a)²`. For full strength `λ=1`, direct integration gives

```text
P₀^(mn)(u) = 2(|u|+2)² / [9(1+|u|)].
```

It is `8/9` at `u=0` and tends to 1 at `|u|=1`. Averaging over the original uniform `du/2` gives the exact same value for the unconditioned output and for either pointer branch:

```text
P(old pair still in its own singlet) = 7/9 + 2 ln(2)/9 ≈ 0.93181048,
P(old pair outside its own singlet)  = 2(1−ln(2))/9 ≈ 0.06818952.
```

The derivation uses only the uniform old angular norm density and the fact that the old record vectors depend on u, which hold for each of the tested post-echo source/sign states. It does **not** identify where that rotational charge is locally stored or assert a detector could measure `P₀^(mn)` without additional resources. It shows exactly why an unchanged old-record marginal is weaker than unchanged full old state, and why adding a symmetry-carrying reference can preserve a combined zero charge without preserving the old subsystem's separate zero.

The interaction admits a continuous trade-off. As `λ→0`, its new pointer–chirality correlation is `2λ/9`, whereas the old-pair non-singlet weight is

```text
λ²/18 + O(λ⁴).
```

At every nonzero λ, some old-only singlet weight is lost for nonparallel directions; at zero strength there is no chirality information. This is a property of this specific readout, not a general optimality or no-go theorem for all possible instruments.

An independent coherence control also distinguishes the states. For `m⊥n` and `n'=-n`, the pointer overlap at fixed p is `√(1−t²)` and its p-average is `π/4`, not 1. This is one kernel value in the unquotiented representation, not a full trace-distance or operational error bound. Applying `U_λ†` coherently restores the input **and erases the new pointer correlation**; it is not retention of a durable record.

## 5. Relation to the other symmetry programmes

The old [spin-chirality report](ZERO_CONSERVING_RELATIONAL_CHIRALITY_REPORT.md) also preserved an enlarged zero charge while transferring nonzero charge to subsystems. That reporter uses a different spin operator and reference pair. The present result provides a mathematical parallel and an actual coupling to the old spherical echo, not an operator identification or an experimentally calibrated joint measurement of the two chirality signs.

The [Satake interface](ZERO_SPHERE_REPRESENTATIONS_GAUGE_LANGLANDS.md) remains separate: this scalar readout does not overcome the central-action obstruction or construct the proposed spinorial line bundle. Nor does preservation of the finite opposite-pair constraints identify the directional rotation action with an internal Yang–Mills gauge group. A concrete map preserving actions and observables, and a computed dual gauge correlator, remain open.

Next work should test whether the three-direction reference and recorded pointer can be carried through an explicit **clock-localized** interaction with retained records; identify which enlarged gauge constraints and possible boundary charges are physical; and compare the scalar and spin chirality reporters under an actual intertwiner or joint instrument. It must also account for all energy and locality assumptions. No result here establishes subjects, felt valence, cosmic energy or a physical law from a bare point.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_sphere_chirality_echo_test -v
```

The prior echo vectors and linear algebra checks use NumPy; the sphere moments and closed forms are derived analytically, with numerical quadrature as a control. The sign-agreement, leakage and backaction claims concern this declared toy model and preparation, not every rotationally invariant state or measurement.
