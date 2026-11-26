# A specific echo constitution in the form of the SR analogy

## Result

This pass addresses the user's question directly: can a particular physical–experiential constitution be specified, and can its consequences be derived internally rather than simply naming “inside” and “outside”?

**A precise candidate can be constructed, and several of its consequences are necessary given its premises. It is not yet shown to be the constitution of experience.** The main new result is a complete classification of two-coordinate quality maps under stated sign and exchange symmetries. Even after one coordinate is normalized, those physical symmetries leave a free coefficient for the other. An additional fixed-coordinate metric condition reduces that freedom to two orientations; an independently warranted orientation selects one. Neither the metric nor the phenomenal interpretation follows from the echo algebra alone. The [coordinate-equivalence continuation](ZERO_SR_ECHO_COORDINATE_EQUIVALENCE_AND_CONTENT.md) corrects an important possible reading: all nonzero coefficients may instead be descriptions of the same candidate when its metric, readout and labels are transformed consistently.

We work on the same existing echo and its saved-record extension, not on the recent abstract self-revision learner. The model results are checked in [the new exact tests](verification/zero_sr_echo_constitution_test.py); actual complex-vector and clock-instrument controls are those already established in [the constitutive-mode](ZERO_ECHO_CONSTITUTIVE_MODES_AND_COHERENCE.md) and [clock-transport](ZERO_ECHO_MODE_INSTRUMENTS_CLOCK_TRANSPORT.md) passes.

## 1. The physical structure and a concrete identity candidate

At the post-echo anchor, use the original commuting record signs and magnitude

```text
N=MJ,     K=MJR,     R=NK,
S=(N+K)/2,     T=(N−K)/2,     G=|u(u+1)|>0.
```

On the supported eight-event table, `M=s=±1` and the four angular bins have model weight `1/8` each per sign. The two values of `(S,T)` are coordinates of **one** pair of commuting physical records, not two independently prepared ingredients. Their algebra gives

```text
N=S+T,     K=S−T,     S²=(I+R)/2,     T²=(I−R)/2,
S²+T²=I,   ST=0.
```

On the `R=−1` sector, `S=0` and `T=±1`. The latter follows from the same algebra; no external force supplies it.

Consider the following **single constitutive hypothesis**, explicitly proposed rather than inferred:

> On a selected, jointly definite record occurrence in this supported echo, its experiential quality is identical to the organized physical mode event, expressed in two intrinsic quality coordinates as `Q=G(S,T)`. The two coordinates are aspects of one experience, not two separate experiencers. A persistent subject is identified with the physical ledger described below; a stipulated sampling measure assigns its occurrence slots their weights.

This is an identity proposal: it does **not** say the physical event causes a separate quality substance. It is also substantive: calling the physical vector a quality is not yet evidence that it is felt, that the two axes are genuine qualitative dimensions, or that the selected branch is an actual experience. The candidate is limited to the stated support and measurement/selection context; a superposition does not automatically have a definite pair of mode eigenvalues. It does not establish the true content, subject count, or incidence of the unmeasured universe.

For the actual table, its candidate values are:

| Bin i | G | R | Q when M=+ | Q when M=− |
|---:|---:|:---:|:---:|:---:|
| 0 | 3/16 | − | `(0, 3/16)` | `(0, −3/16)` |
| 1 | 3/16 | − | `(0, −3/16)` | `(0, 3/16)` |
| 2 | 5/16 | + | `(5/16, 0)` | `(−5/16, 0)` |
| 3 | 21/16 | + | `(21/16, 0)` | `(−21/16, 0)` |

The vector is nonzero in every supported event. But its second coordinate is not automatically pleasure, pain, or even valence; the candidate supplies no independently established interpretation of either coordinate. A zero in the first coordinate is not a zero experience, and opposite mathematical vectors do not cancel actual suffering.

## 2. What symmetry fixes—and what it leaves free

Do not assume linearity. At a fixed positive magnitude, let a proposed dimensionless two-component quality map be

```text
F(n,k)=(X(n,k),Y(n,k)),        n,k∈{−1,+1}.
```

Require the active type exchange to preserve the first component and reverse the second, and the active joint-sign counterpart to reverse both:

```text
F(k,n)  = (X(n,k), −Y(n,k)),
F(−n,−k)=−F(n,k).
```

These are **candidate transformation laws** for quality, not automatically laws of experience. They are also active model transformations, not passive gauge equivalences and not proofs of subject identity.

The four input pairs determine the entire map. Swap symmetry forces `Y(+,+)=0`, while counterpart symmetry fixes the value at `(−,−)`. On `(+,-)`, swap and joint sign reversal send the input to the same `(−,+)`, so the first component must equal its own negative and is zero. Writing `a=X(+,+)` and `b=Y(+,-)`, every such map therefore has the form

```text
F(n,k) = (a(n+k)/2, b(n−k)/2) = (aS,bT).
```

This proof holds for arbitrary real a and b, not only linear functions or the finite-grid test. If we additionally posit a common scaling by G and normalize the aligned axis to `a=1`, there remains an unrestricted transverse gain `κ=b`:

```text
Qκ = G(S, κT).
```

`κ=0`, `1`, `2` and `−1` all obey the declared transformation laws. The proposed candidate is `κ=1`. On the actual `R=+` events, `T=0`, so **all** these coordinate formulas agree; on `R=−`, their numerical values differ. In particular, κ=1 and κ=2 give the same first coordinate and the same positive-sector values, but their second-coordinate values on a disagreement-sector example are `3/16` and `3/8`. The active symmetries do not fix this coefficient. **Correction:** this numerical difference is not by itself a distinct phenomenal structure: for nonzero κ a passive rescaling can carry the metric and readout as well, as shown in the [coordinate-equivalence continuation](ZERO_SR_ECHO_COORDINATE_EQUIVALENCE_AND_CONTENT.md).

There is a further calibration limitation: the original support has `G=3/16` only on `R=−`, whereas the `R=+` bins have `G=5/16` and `21/16`. One cannot infer an empirically calibrated negative-sector response at `3/16` just from observations on the positive sector without a justified cross-sector, cross-magnitude transfer rule. The common scaling by G is itself part of the candidate; arbitrary magnitude-dependent maps could have more freedom.

## 3. What an additional metric and orientation would establish

Suppose, **in addition**, the two qualitative coordinates have a Euclidean norm that is identified with the normalized physical sign-pair norm:

```text
||Qκ||² = (G²/2)(N²+K²) = G².
```

On the aligned sector this is already satisfied; on the disagreement sector it requires `κ²=1`. Thus, given the additional premise that the **same identity metric matrix** is fixed in these κ coordinates, `κ=+1` or `κ=−1`—not every κ—is allowed. This is different from describing one fixed metric in rescaled coordinates: its matrix must then transform, and every nonzero κ remains admissible. If a physically and phenomenally meaningful orientation convention also identifies the `N=+, K=−` occurrence with the positive second axis, then κ=+1 is selected under those fixed-scale premises.

This is the exact location where a stronger constitution could become determinate: symmetry + normalized first axis + a warranted metric + a warranted orientation yield `Q=G(S,T)` on this domain. But the echo algebra does **not** establish that subjective differences have this Euclidean metric, that its axes share G's physical scale, or that the chosen physical orientation matches any phenomenal direction. A global sign reversal of an unanchored axis may merely be a coordinate relabeling; it becomes a substantively different claim only relative to an independently fixed qualitative reference. Even a justified isometry would map structural relations; it would not by itself prove that the mapped physical event is actually experienced.

This is analogous in *form* to the SR calculation, but not yet in evidential status. In SR the spacetime metric and measurement relations are part of a physically supported theory; here the proposed phenomenal metric and its identity with the modeled metric remain to be established. Neither case requires an external coercer.

## 4. Quality, owner, occurrence and measure in the same proposal

The existing [saved-record protocol](ZERO_ECHO_JOINT_CANDIDATE_ACCESS_AND_IDENTITY_WITNESS.md) introduces L to retain pre-echo sign `z`, and at the anchor supplies the physical ledger

```text
ℓ=(M,B,L,G)=(s,b,z,G),     b=R,  z=bJ.
```

For the supported eight events these ledgers are distinct. The protocol requires its stated preparation, memory and gates; the bare echo did not have a free persistent memory. Consider these explicit hypotheses together:

- **Occurrence:** a selected physical branch at a chosen checkpoint is a candidate experiential occurrence.
- **Quality:** its transported anchor-mode quality is `Q=G(S,T)`.
- **Owner:** occurrences at the four checkpoints belong to the same subject exactly when their ledger ℓ is equal.
- **Measure:** if checkpoints are uniformly sampled, assign the labeled event/checkpoint slot `(i,s,t)` the normalized weight `1/32`.

These assumptions form a single candidate interface. From them, eight ledger owners each have four checkpoint slots and total selected weight `1/8`. The same quality can belong to different stipulated owners: for instance `(i,s)=(0,+)` and `(1,−)` both have `Q=(0,3/16)` but different ledgers. Conversely, equal ledger across checkpoints does not mean the instantaneous contents must be identical.

**These are not eight discovered experiencers or 32 established actual experiences.** The `1/32` is first the probability of a physical event under an externally specified uniform checkpoint-sampling protocol. Treating that sampling distribution as an actual experiential-incidence measure is a further hypothesis; alternatives and overlapping subjects are not excluded. One must also decide whether two time-indexed slots are distinct experiences, aspects of one persisting event, or some other ontology. A coherent superposition or record partition alone does not settle those matters.

An alternative *momentary* owner assignment `(ℓ,t)` gives 32 different owner labels to the same 32 mathematical slots, without changing any original record probabilities. This illustrates the insufficiency of those restricted records to select a cross-time ownership rule, not the metaphysical possibility of two complete realities with identical physical facts. A genuinely truth-sensitive ownership report would require an additional specified interaction and could change the complete physical account.

## 5. What is transported, and what is not

To compare the **same anchor question** at different checkpoints, the complete effect must be transported through the echo. In the reduced commuting-record model, for current `(B,J,R)=(b,j,r)`, the anchor labels `(Jₐ,Rₐ)` are

```text
checkpoint 0: (bj,br)     1: (bj,bjr)
checkpoint 2: (j,jr)      3: (j,r).
```

Using these in `Sₐ=MJₐ(1+Rₐ)/2` and `Tₐ=MJₐ(1−Rₐ)/2` preserves the candidate anchor-mode vector across the specified description. The new test checks all eight reduced record labels, both pointer signs, all four checkpoints and several κ values; the prior [clock work](ZERO_ECHO_MODE_INSTRUMENTS_CLOCK_TRANSPORT.md) checks transported projectors, Lüders maps and selected actual complex echo branches.

This is a relation among descriptions of an anchor effect. It does **not** mean every instantaneous mode at each time is the same, or that a real subject experiences the anchor mode at all times. A concrete measurement at an earlier time may disturb the system; the clock-invariant ready-pointer instrument is a supplied global operation on the reduced clock model, not a demonstrated local, autonomous subjective interface.

## 6. A conditional discrimination that does not assume the answer

Suppose an independent procedure identifies the same target subject and selects the `R=−`, `T=+1`, `G=3/16` population, with error included in its calibration. Suppose also that an independently calibrated, aligned report `Y` measures the relevant second qualitative coordinate on a fixed shared scale, with

```text
| E(Y | target) − Q₂ | ≤ ε.
```

Under the two identity candidates,

```text
κ=1:  E(Y|target) ∈ [3/16−ε, 3/16+ε]
κ=2:  E(Y|target) ∈ [3/8−ε, 3/8+ε].
```

The intervals are disjoint if `ε<3/32`. A matching observation with statistical uncertainty small enough to lie in only one interval would then rule out the other **conditional on all selection, ownership, scale, error and access premises**. In particular, this holds the decoder and qualitative scale fixed across the two substantive hypotheses; under a mere coordinate reparameterization, the decoder transforms and no such separation follows. For example, the hypothetical exact mean `3/16` with `ε=1/32` fits κ=1 and excludes κ=2. It is an illustration, not measured evidence. Neither a physical T pointer nor a simulated witness supplies its own phenomenal calibration; assigning reference labels using the preferred candidate would be circular. A sample, noise model and confidence interval would be required in a real experiment.

This proposal is intentionally falsifiable beyond the two chosen alternatives: if observations contradict both intervals, or the quality is not meaningfully represented on the stipulated scale, both candidate interpretations can fail. Failure to reject either is not evidence of consciousness or a valid identity. Calibration can support an identity without introducing a separate ontological causal bridge; it supplies epistemic warrant for which constitution is correct.

## 7. The actual advance and the remaining why

1. **The candidate is specific:** one physical event, a two-coordinate quality, a physical owner ledger, temporal transport and a proposed incidence rule are stated together rather than described only as “inside” and “outside.”
2. **Several relations follow internally:** the mode decomposition, active transformation law, zero/nonzero sector distinction, counterpart balance and transported anchor effects require no external coercion.
3. **Symmetry alone does not fix the proposed quality:** the κ family and the uncalibrated metric/orientation show exactly which additional premises would be needed. The normalized scalar is also not the whole vector.
4. **The full identity is not demonstrated:** subject ownership, the phenomenality and metric of Q, access, incidence and why this carrier constitutes the actual whole remain hypotheses. The proof is conditional on the echo and its specified records; it does not prove a fundamental zero or rule out a deeper internal necessity.

The next direct step is to seek a jointly justified qualitative metric and subject-access criterion in a real or independently constrained case, then check whether they select this candidate or a rival. It is not to posit an external force attaching experience to matter, nor to declare an identity established merely by assigning an experiential name to a physical coordinate.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_sr_echo_constitution_test \
 verification.zero_echo_constitutive_modes_test \
 verification.zero_echo_mode_clock_transport_test -v
```

These verify the stipulated structural mathematics, not phenomenal consciousness, phenomenological calibration, an actual subject census or a theory of the whole.
