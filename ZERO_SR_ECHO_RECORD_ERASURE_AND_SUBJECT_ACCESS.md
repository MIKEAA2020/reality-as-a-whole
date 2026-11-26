# Record, recovery and subject access in the SR-inspired echo

## Result

The [previous pass](ZERO_SR_ECHO_INTRINSIC_DISTINGUISHABILITY_AND_ACCESS.md) found a physical information–coherence tradeoff for a specified clock-preserving pointer. This pass follows both the echo and the pointer after that write. The result is sharper:

- Loss of phase information from the **echo alone** need not be irreversible. Before a further which-branch record is made, an appropriate pointer measurement and conditional correction recover the original state for **every input state on the two-branch subspace**.
- This recovery changes what the pointer records: the eraser outcome contains no information about which T branch was present. It does not prove that branch information vanished from every possible part of the world.
- If a separate inaccessible environment receives a perfect T record, the same local eraser on the echo and original pointer cannot recover the phase distinction. The full echo–pointer–environment state still retains it in joint correlations.
- All operations implemented here respect the existing **reduced** stationary clock constraint. They are stipulated global model operations, not a demonstrated local apparatus or a first-person subject.

This is an internal relation among physical records, access and transformations, not an external force making an identity true. It does not establish which physical state is experienced, whether phase has a phenomenal counterpart, who owns an occurrence, or its actual incidence. [Tests](verification/zero_sr_echo_quantum_eraser_test.py).

## 1. Start with the existing coherent echo and pointer

Use the selected `M=+`, `R=−` echo sector and the two orthogonal **stationary reduced clock histories** `|E₊⟩,|E₋⟩` corresponding to anchor `T=+1,−1`. They represent the two selected physical record branches of the echo. Their construction and the link to selected original complex branches are described in the [previous report](ZERO_SR_ECHO_INTRINSIC_DISTINGUISHABILITY_AND_ACCESS.md); the reduced histories are not the full purified apparatus.

The pointer has an orthogonal ready state and two possible written states

```text
|m₊⟩ = |0⟩,
|m₋⟩ = r|0⟩ + √(1−r²)|1⟩,     0≤r≤1,
⟨m₊|m₋⟩ = r.
```

The clock-invariant controlled unitary U from the preceding pass writes these states from ready according to the two anchor projectors. For a general pure input in this subspace,

```text
|φ⟩=a|E₊⟩+b|E₋⟩,
U(|φ⟩|ready⟩)=a|E₊⟩|m₊⟩+b|E₋⟩|m₋⟩.
```

The state and pointer are now correlated. For the balanced `|ψ₊⟩=(|E₊⟩+|E₋⟩)/√2`, ignoring the pointer multiplies the off-diagonal coherence by r. At `r=3/5`, the echo's fidelity with its original balanced state is `4/5` and optimal T discrimination **from the pointer alone**, with equally likely definite branch inputs, has success probability `9/10`.

These are conditional physical statements. The bit is not a report by an established conscious observer, and a superposition is not assumed to have a definite T value before measurement.

## 2. Where did phase distinguishability go?

Compare two orthogonal input states

```text
|ψ₊⟩=(|E₊⟩+|E₋⟩)/√2,
|ψ₋⟩=(|E₊⟩−|E₋⟩)/√2.
```

For either input the T probabilities are the same. The global write is unitary, so the two **joint** echo–pointer outputs are orthogonal and have trace distance `D=1`. After the write, the accessible distinction depends on what is retained:

| Available system/effects | Trace distance for `ψ₊` vs `ψ₋` | Optimal equal-prior success |
|---|---:|---:|
| Echo alone, all effects on selected subspace | `r` | `(1+r)/2` |
| Pointer alone | `0` | `1/2` |
| Echo and pointer together, all joint effects | `1` | `1` |

At `r=3/5`, those success probabilities are respectively `4/5`, `1/2`, and `1`. The global phase distinction has not been destroyed by U; it is partly encoded in **correlations**. Losing access to a subsystem changes operational distinguishability without making the corresponding global states identical. Whether that distinction is experienced is still a separate question.

## 3. A clock-compatible eraser and recovery

Choose the pointer's orthonormal output-plane basis

```text
a=√[(1+r)/2],       b=√[(1−r)/2],
|u⟩=a|0⟩+b|1⟩,      |v⟩=b|0⟩−a|1⟩.
```

It satisfies

```text
⟨u|m₊⟩=a,   ⟨u|m₋⟩=a,
⟨v|m₊⟩=b,   ⟨v|m₋⟩=−b.
```

Thus the pointer measurement has the following two Kraus maps on the selected echo-history subspace:

```text
Kᵤ=a I,       Kᵥ=b Z,
Z|E₊⟩=|E₊⟩,  Z|E₋⟩=−|E₋⟩.
```

The `u` and `v` outcomes have probabilities `a²=(1+r)/2` and `b²=(1−r)/2` for **every input density matrix on the selected subspace**. In particular, neither outcome contains information about whether a definite T+ or T− branch was supplied. If v occurs, apply Z; otherwise apply I. The corrected, nonselective channel is

```text
ρ ↦ KᵤρKᵤ† + ZKᵥρKᵥ†Z† = (a²+b²)ρ = ρ.
```

This restores all states on the two-branch subspace, including complex superpositions and mixtures, not just one balanced vector. For `r=3/5`, the eraser outcomes have probabilities `4/5` and `1/5`. Once the outcome-dependent correction is made, the restored echo can again distinguish `ψ₊` from `ψ₋` perfectly.

This is a **specified reversible quantum protocol**, not a claim that all observations or environmental interactions can be undone. It uses the pointer before its branch information has been irreversibly copied elsewhere. The eraser outcome is retained as a classical control record, but is independent of the input T branch. The system itself can still carry a T state; what is lost in this protocol is the independent T information in this pointer record.

### Stationarity and resource scope

The existing twirled projector `Π₋` commutes with the cyclic clock shift W. The correction `Z=I−2Π₋` is unitary and commutes with W; pointer-only measurement and conditional application of this Z preserve the reduced W=1 subspace. The test checks actual 160-dimensional stationary conditional vectors, not just the two-dimensional Kraus formulas.

The pointer measurement, its outcome-conditioned control, and its extra memory are nonetheless supplied operations. No locality, autonomously acting subject, energy budget or physical implementation of the full clock/apparatus is established. A zero-probability v outcome at r=1 needs no correction; the formula still applies.

## 4. Reading the branch instead is a different protocol

If the pointer is measured in the optimal basis for discriminating `|m₊⟩` from `|m₋⟩`, it gives the previously calculated T-branch success `(1+√(1−r²))/2`. But this measurement is different from the eraser-basis measurement above. In the specified model, after the **optimal T measurement**, the joint classical-pointer-outcome plus remaining echo state has phase trace distance `r`, not 1. A later operation on those retained systems cannot increase that distance.

For `r=3/5`, the two alternatives are:

| Pointer protocol | Pointer-only T-branch success | Phase-pair distance available in retained output |
|---|---:|---:|
| T-optimal readout | `9/10` | `3/5` |
| Eraser basis plus outcome-dependent correction | `1/2` | `1` |

The table compares **specified protocols**, not a theorem that every possible measurement must have those values. The second row does not claim that the restored echo has forgotten its T basis; it says that the pointer outcome contains no independently retrievable T-branch information. A previously copied or externally witnessed record is not undone by merely changing the pointer basis.

## 5. An explicit environment-copy obstruction

Add a separate binary environment record, initially zero, and an ideal controlled operation that copies the orthogonal T branch to it:

```text
|E₊⟩|0⟩env → |E₊⟩|0⟩env,
|E₋⟩|0⟩env → |E₋⟩|1⟩env.
```

This is an additional interaction, not an inferred property of the original echo. The reduced implementation uses the same clock-invariant `Π₋` as a controlled bit flip and checks the copied conditional histories still satisfy the W=1 constraint.

After that copy, trace out the environment. For `ψ₊` and `ψ₋`, the **entire accessible echo-plus-original-pointer density matrices are identical**: their difference is in correlations with the inaccessible environmental record. Their trace distance on that accessible composite is zero. Therefore no deterministic or conditional protocol acting only on that composite can distinguish the two phase inputs from this point, or restore both unknown inputs as distinguishable echo states. The eraser-and-correction procedure above now returns the maximally mixed two-branch echo state for the balanced input, with fidelity `1/2` to `ψ₊`.

The full echo–pointer–environment pure states are still orthogonal. Accessing and coherently reversing the environment interaction would be a different, more global protocol. The obstruction does not mean all physical distinctions vanished, and it does not infer a hidden experiencer or its absence. It identifies **which record is outside the stated access boundary** and why ignoring it matters.

## 6. Consequence for the proposed subject–quality constitution

This result gives a more demanding criterion than simply finding a physically measurable T or phase. A candidate subject and its access structure must say:

1. Which subsystem and retained records constitute the candidate's interface at the relevant time;
2. Whether its available operations can distinguish the physical states in question, including their coherence and any relevant environment;
3. Which interactions, correlations and losses are part of the candidate itself, and which are inaccessible;
4. Why those distinctions are identical to or constrain its **lived** quality, rather than only changing a mathematical report; and
5. How ownership through time and actual occurrence measure are fixed, rather than counted from pointer or clock labels.

The example also cautions against identifying “the full state” with “one subject” by default: a joint global effect can reveal phase that neither subsystem alone reveals, yet the existence or unity of an experiencer is not determined by that fact. Conversely, a restricted interface missing phase does not prove no experience. Multiple, nested or overlapping subjects remain possible hypotheses; the present reduced circuit does not decide them.

The SR analogy remains constructive: record coherence, its transport and recoverability follow from one specified structure without an external coercive force. But the analogy does not itself establish that any state is felt. The next step is to combine a **defined physical access boundary and independently supported qualitative/ownership references** on one target, then state outcomes that could challenge the proposed identity. If a successful identity is constitutive, no separate ontological cause must attach the feeling; the required reference supplies evidence for which identity is correct.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_sr_echo_quantum_eraser_test \
 verification.zero_sr_echo_intrinsic_access_test \
 verification.zero_echo_mode_clock_transport_test -v
```

The tests check reduced-clock stationary states and unitaries, recovery for a basis of quantum operations and representative mixed/complex states, alternative pointer measurements, and the added environment-copy control. They do not establish subjective access, a qualitative metric, locality, the full apparatus, or an actual subject census.
