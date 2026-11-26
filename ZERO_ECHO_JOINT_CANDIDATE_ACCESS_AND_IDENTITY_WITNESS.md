# What can access the joint candidate—and what can test its ownership?

## Result

The [preceding joint candidate](ZERO_ECHO_OCCURRENCE_QUALITY_INCIDENCE_JOINT_CONSTRAINT.md) combines a time-indexed occurrence slot, structural content, an owner ledger and a stipulated sampling weight. This pass tests those connections against the existing physical echo and its added saved-record protocol.

- In the specified commuting-record table, the full candidate content and its ledger can be recovered at the anchor from either `{M,G,J}` or `{M,G,L}`. The sets overlap in the pointer M and magnitude G; they are **alternative logical readouts**, not evidence of two subjects or complete quantum-state recovery.
- The sign pointer is essential for this candidate's content: with all the other listed records, the best guess of M is **1/2** in the modeled distribution. Without G, even all remaining listed records identify the eight physical events only with probability **3/4**. These are restricted-interface results, not bounds for arbitrary measurements.
- Two coherent preparations of actual recorded echo branches can have identical reduced states on each of two subsystems while being perfectly distinguishable jointly. Copying a classical sign into L does not copy the relative phase of an arbitrary quantum state.
- Persistent and momentary ownership hypotheses leave the unchanged physical record table identical. A separate, target-specific identity witness could distinguish them under explicit error and sampling assumptions, but the existing physical comparison bit does not supply that calibration.

The results concern mathematical model states and specified effects—not observed subjects, a real identity assay, or a complete derivation of experience. [Implementation](verification/zero_echo_joint_candidate_access_witness.py), [focused tests](verification/zero_echo_joint_candidate_access_witness_test.py).

## 1. A single candidate and its actual physical records

Keep the earlier four-bin echo, sign pointer `M=s`, original record `J`, echo record `R`, and `G=|u(u+1)|`. A separately prepared memory `L` copies the pre-echo J sign z. After the actual T–Q–T sequence, the supported relations are

```text
J=bz,       R=b,       L=z,       H=zJ=b,
Q_now=MJ,   Q_echo=MJR=ML.
```

H is the **additional** ready comparison bit written from L and current J at the anchor. It physically reports b; interpreting it as a report of subject identity is not established. All listed signs are the values of specified commuting record queries on the given prepared support. The saved memory and H require their own preparation and controlled gates. G is the chosen swap-compatible *model* magnitude, not an established felt magnitude.

The proposed joint candidate uses, at checkpoint t,

```text
slot o=(i,s,t),
content C(o)=(Q_now(t), Q_echo(t), s, G),
owner ledger ℓ(o)=(s,b,z,G).
```

Its physical event table has eight equally weighted `(i,s)` labels. The proposed owner relation, identification of C with intrinsic quality and the relevant incidence measure remain hypotheses. In particular, a reporter is not given access to every global variable merely because the variables occur in this definition.

## 2. Minimal physical access sets

At each checkpoint, ask which **listed fields** determine the complete physical event `(i,s)`, the candidate content C, or the ledger ℓ on this finite supported table. In this model these three targets have the same minimal access sets:

| Echo checkpoint | Inclusion-minimal sets |
|---|---|
| Before T | `{M,G,J}`, `{M,G,L}` |
| After T | `{M,G,J}`, `{M,G,R}`, `{M,G,L}` |
| After Q | `{M,G,J}`, `{M,G,R}`, `{M,G,L}` |
| After final T | `{M,G,J}`, `{M,G,L}` |

The full table is computed from the earlier coherent echo rules and checked against the [joint candidate's actual saved-memory checkpoint tests](verification/zero_echo_joint_identity_balance_test.py). It assumes the prepared angular/sign sector and correct clock alignment; `R` at an intermediate checkpoint is not automatically its final value b. H exists only after its explicitly added comparison write, and gives another B readout, but adds no minimal complete set here.

Why are M and G needed? The other listed records are independent of s under this specific equal-pointer distribution. Thus all of them together, without M, guess s only with probability `1/2`. G separates the two positive-b bins that otherwise have the same displayed signs. Without G, all other listed fields together guess the eight-event label with probability `3/4`. Conversely M and G without an additional J/R/L field also yield `3/4`, because they leave the two negative-b bins ambiguous. The candidate requires the listed field values, not just knowledge that a global state has them.

These statements are **not** universal no-go theorems. Other quantum observables, off-support states, a different magnitude, an imperfect readout, changes of timing or a different apparatus can alter the access structure. Measuring J and L may disturb the old coherent history; the earlier physical construction found a `5/8` fidelity for the old sign-slice state after retaining and tracing out L. Whether M, G, J or L is available within a putative subject's actual interface is an additional question.

For an operationally noisy version, suppose a declared three-field decoder is exact on a reference support; the source's joint distribution of the true event and its three true fields is independently within total-variation distance `ζ` of a reference distribution on that support, and the three matched readout error probabilities are at most `e₁,e₂,e₃`. A union bound gives an event-guess error no larger than `min(1,ζ+e₁+e₂+e₃)` without assuming independent errors. Each bound must apply to the **same selected source and timing**; a calibration on different references does not establish it. This estimates a physical event, not the accuracy of an experiential or ownership report.

## 3. Same classical content is not a copied quantum state

At the anchor, take the actual recorded sign slice `s=+` and select bins 0 and 1. Both have `G=3/16`; their original J signs are opposite, and the added L has opposite saved-z signs. The new checks extract these two branches from the actual complex echo vectors for source labels 0, 7 and 15. Each has weight `1/4` in its original sign slice, so selecting their union has weight `1/2`. The old-carrier branches are orthogonal because their angular bins are orthogonal.

Normalize and write them as `|e₀⟩,|e₁⟩`, with L states relabeled `|0⟩,|1⟩`. The postselection gives, up to absorbed branch phases, one of the joint preparations

```text
|Ψ₊⟩ = (|e₀⟩|0⟩_L + |e₁⟩|1⟩_L)/√2.
```

An additional stipulated phase flip on the second angular bin gives

```text
|Ψ₋⟩ = (|e₀⟩|0⟩_L − |e₁⟩|1⟩_L)/√2.
```

Both the old-carrier reduced state and the L reduced state are identical for these two preparations. Thus any measurement confined to either subsystem alone has the same outcome distribution for `Ψ₊` and `Ψ₋`. The joint states are orthogonal: the effect `|Ψ₊⟩⟨Ψ₊|` distinguishes them perfectly. In the isometric two-branch representation their global trace distance is 1, while each local trace distance is 0.

This is a control on the *same echo branches*, not a claim that the phase-flip intervention or joint effect is spatially local, autonomously available or available to a subject. It also does not show that the relative phase is felt. It establishes a narrower physical point: J and L can redundantly expose a classical record while neither isolated subsystem contains the whole encoded coherence. Multiple ways of reading an event are not automatically multiple subjects, and failure of a local record to reveal phase is not proof that the distinction is absent globally.

## 4. Clock selection is not an incidence law

The prior candidate assigns a sampling weight `π_t/8` to slot `(i,s,t)` with `Σπ_t=1`; π was explicitly supplied. For the same proposed ledger `(i,s)=(0,+)`, the `Q_now` signs over the four checkpoints are

```text
−, −, +, +.
```

Uniformly sampling checkpoints gives positive frequency `1/2`. Sampling them with `π=(1,2,3,4)/10` gives `7/10`. In the stated persistent-owner hypothesis the owner ledger is unchanged; in both sampling protocols the four weighted slots of that ledger sum to `1/8` because `Σπ=1`.

The change of a **measurement-selection protocol** therefore changes reported time-conditioned statistics without by itself establishing a change in the owner or in how many experiences exist. If a theory instead claims π is the actual experiential-incidence measure, it needs an independent argument tying that measure to the chosen clock and explaining how it transforms under other clock choices. Neither alternative follows merely from normalization or from the echo dynamics.

## 5. A target-specific ownership witness

Compare two deliberately simple ownership hypotheses for the same supported ledger at two **different** checkpoints:

```text
P: the slots have the same owner;
F: the slots have different, momentary owners.
```

Both leave the state, gates, physical comparison H and all stipulated physical-outcome laws unchanged; ownership is not an input to the echo circuit. This is an indistinguishability result for these two formal extensions when the allowed outputs do not depend on their additional ownership labels, not a theorem that a deeper physical theory or a real first-person witness can never bear on identity.

Suppose an independently justified witness Y answers the *same target question for the same reporter, time window and population*, with `Y=1` meaning “same owner.” Let its separately supported error bounds be

```text
P(Y=1 | different owner) ≤ f,
P(Y=0 | same owner)      ≤ g.
```

Then F permits `q=P(Y=1)≤f`, while P requires `q≥1−g`. When `f+g<1`, these ranges do not overlap. Neither physical accuracy of H relative to b nor a simulated bit supplies f or g for identity. A first-person observation can be direct evidence for its own occurrence, but its translation into this specific cross-time witness, its reporter correspondence and any numerical error bound require separate justification.

For `N` iid witness answers with k positives, let

```text
q̂=k/N,     R=sqrt[log(2/δ)/(2N)],
q_L=max(0,q̂−R),    q_U=min(1,q̂+R).
```

On the confidence event, reject F if `q_L>f`; reject P if `q_U<1−g`. Failure probability for this sampling statement is at most δ, **conditional** on the population, iid sampling and calibration bounds. If f or g is estimated, its failure probability and uncertainty must also be included. Neither candidate being rejected is not evidence that it is true; the two hypotheses are not exhaustive.

Illustration only: for **hypothetical**, not observed, `N=1000`, `k=950`, `δ=.05` and separately assumed `f=g=.1`, `R≈.04295` and `[q_L,q_U]≈[.90705,.99295]`. F is rejected on the stated event; P is not rejected. With k=500 instead, the interval is approximately `[.45705,.54295]` and **both** are rejected under the same premises. With weak bounds such as `f=.6,g=.4`, even sharply measured intermediate rates need not separate the hypotheses. These examples are sensitivity calculations, not evidence about an actual subject.

Repeated or interleaved reports are not automatically iid; a shared error, selection process or memory can correlate trials. The [earlier ownership calibration diagnosis](ZERO_ECHO_OWNERSHIP_REPORT_CALIBRATION_ROOT_CAUSE.md) gives a concrete correlated-error control. A report whose output is affected by an additional truth-sensitive interface also changes the physical model; its access, intervention, preservation and resources must be specified.

## 6. The continuing why-chain

1. **Why can two supports read the candidate ledger?** On this prepared sector, saved L and current J carry enough correlated classical sign information; M and G supply the distinctions neither record contains. This is a property of a specified state and interface, not a general identity of the supports.
2. **Why not count each support as an owner?** Their sign data overlap, their readouts share M and G, and local reduced states can miss global coherence. Recoverability of one variable does not establish a subject, its boundary or exclusivity. It also does not rule out distinct overlapping subjects if a warranted constitution supports them.
3. **Why does a physical H report not settle persistence?** The gates compute `zJ=b`; they do not compute an independently defined ownership truth. Better accuracy about b cannot by itself validate an identity interpretation.
4. **Why would a witness settle even these candidates?** Only an appropriately aligned and calibrated relation to the identity question, plus controlled selection and sampling, gives the conditional exclusion above. Direct first-person evidence must be taken seriously, while equating a physical bit to such evidence without a bridge is circular.
5. **Why choose this content, owner and weight at all?** They are a coherent **candidate** using actual model relations and a supplied clock sampling law. The physical–experiential identity, actual incidence measure, completeness of the subject boundary and choice of carrier/dynamics are not yet derived from the proposed self-sufficient whole. Further work must address that constitution and its actuality, not rename these remaining assumptions as a completed explanation. This boundary is not proved ultimate bedrock, and no external temporal cause of the whole is assumed.

## 7. Next work

- Develop and compare explicit physical–experiential bridge candidates that make different predictions about accessible identity or quality, while preserving real positive and negative experience and allowing overlapping subjects.
- Justify or bound reference preparation, timing and readout for the relevant interface; analyze complete clock-frame transport of the candidate, not merely a shift of a state against fixed effects.
- Continue the constitutive chain: what in the whole fixes occurrence equivalence, real subject boundaries and incidence rather than only permitting several mathematical bookkeeping rules?

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_echo_joint_candidate_access_witness_test -v
```

The tests verify the modeled record sets, actual branch extraction and isometric coherence control, sampling examples and conditional statistical calculations. They do not validate the witness, physical locality, experiential identity or complete historical-source coverage.
