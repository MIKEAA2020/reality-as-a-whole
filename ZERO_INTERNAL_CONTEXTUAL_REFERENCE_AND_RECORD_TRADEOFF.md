# An internal reference from an existing record—and its unavoidable trade-off

## Result

The [previous construction](ZERO_CONTEXTUAL_SIGN_SYMMETRY_AND_RELATIONAL_DRESSING.md) made a sharp symmetry-invariant relative sign by adding a transforming qubit \(R\). **That reference need not be added to the modeled history.** In the existing 72-dimensional report sector, Bob's sphere outcome and its already-written outcome register contain exactly the redundant correlation needed to encode the reference internally.

Let \(B\) be the old Bob sphere observable and \(Z_j\) the old outcome record, with eigenvalues \((-1)^j\). Every one of the 16 actual relative-clock histories obeys

\[
 BZ_j|\Psi\rangle=|\Psi\rangle.
\]

The two operators

\[
 X_R=BZ_j,\qquad Z_R=X_j
\]

square to one and anticommute. They are a **logical qubit inside the original sphere-plus-record factors**, initially in the symmetric \(X_R=+1\) state. No independent reference qubit is appended. Using it gives a sharp, gauge-covariant relative sign with a concrete conserving pointer gate.

There is a consequential cost: the gate does **not** preserve the previously written physical \(j\) register. After the sign pointer is ignored, that register disagrees with its old value on **one quarter** of the conditional modeled weight. The original outcome remains recoverable from the unchanged sphere observable \(B\), if the interface has access to it. Thus the construction reuses a real redundancy rather than conjuring a free reference—but it does not preserve every old record in place.

This is an exact finite-model result, not a demonstration of experience or a universal no-go. Verifier: [`verification/zero_internal_contextual_reference_test.py`](verification/zero_internal_contextual_reference_test.py).

## 1. The old source already contains the reference

In the old instrument, Bob's recorded outcome \(j=0,1\) corresponds to \(B=(-1)^j\). This holds as a **state-dependent relation on the actual complete history**, not as an operator identity between the sphere and record. With \(Z_j|j\rangle=(-1)^j|j\rangle\), the operator \(X_R=BZ_j\) therefore stabilizes the old history. The original test checks this separately for every old clock label, including the actual Alice/Bob sphere correlations and encoded work state.

Take \(Z_R=X_j\), the bit-flip on the existing Bob record. Since the sphere and record act on different factors,

\[
 X_R^2=Z_R^2=I,\qquad \{X_R,Z_R\}=0.
\]

Both commute with \(B\), the old internal clock, work constraint and modeled orientation charges. They define an exact logical qubit whose \(+X_R\) state is already present. The information is not in the sphere alone or the record alone: it is their *relative agreement*. In the encoded tensor-factorization this logical qubit is pure on the prepared history, even though the original physical sphere and record can each be correlated with the rest.

The old pointer must remain available as a manipulable quantum system: the required \(X_j\) operations are not implied by a merely readable classical printout. The neutral sign pointer M and interaction control are still assumed. Internalizing R does not derive the initial correlation, control, valid-sector flag or energy cost from the proposed zero whole.

## 2. A sharp sign using the internal reference

Let \(C\) be the old chirality sign, \(S=S_{DE}\) the reference exchange, and

\[
 U=P_+^B-P_-^B S,\qquad P_\pm^B=(I\pm B)/2,
\]

be the previously constructed history-preserving unitary. It exchanges \(C\) and \(CB\), while leaving \(B\), \(Z_j\), the old clock and work observables unchanged. Because \(U\) commutes with both logical reference Pauli operators, the prior reference-dressed symmetry can now be realized within the old factors as

\[
 \widetilde U=UX_R=UBZ_j.
\]

Both \(U\) and \(X_R\) fix the old input, so \(\widetilde U\) does too. Define

\[
 C_{\rm int}
 =C\frac{I+Z_R}{2}+CB\frac{I-Z_R}{2}
 =C\left(P_+^B+P_-^B X_j\right).
\]

On the valid constrained sector,

\[
 C_{\rm int}^2=I,\quad
 \widetilde U C_{\rm int}\widetilde U=C_{\rm int},\quad
 SC_{\rm int}S=-C_{\rm int}.
\]

It commutes with the old total orientation, clock generators, work condition, diagonal \(G\), and \(B\). With the earlier **specified mathematical** spin-reversal convention extended to the record by complex conjugation, it is reversal odd. That is not a claim about the physical time reversal of an actual brain, apparatus or felt valence.

The actual report uses the neutral pointer M initially ready in \(|0\rangle\), with

\[
 P_-^{\rm int}=\frac{P_{\rm valid}-C_{\rm int}}2,\qquad
 U_{\rm report}=(I-P_-^{\rm int})\otimes I_M+P_-^{\rm int}\otimes X_M.
\]

The complete gate is unitary, commutes with \(\widetilde U\) and the stated constraints, and leaves the old sphere observable available. The valid-sector projector and identity extension keep the original remainder, whose paired-state weight is \(23/32\). For each old clock label the verifier constructs both sign branches: each has conditional Born weight \(1/2\), preserves the total orientation zero, old work condition and diagonal \(G\), and is invariant under \(\widetilde U\). Relative to the original full source, the two valid signs carry \(9/64\) each; the separately flagged remainder carries \(23/32\).

## 3. Why this does not automatically settle the gauge choice

This is an internal realization of the **previous extended action** \(U\otimes X_R\), expressed using an existing logical qubit. It is not invariant under bare \(U\) acting alone: \(UC_{\rm int}U\ne C_{\rm int}\). If bare \(U\) must remain a gauge identification *in addition* to \(\widetilde U\), this report is not an admissible gauge-invariant absolute sign. Equivalently, requiring both would also identify their product \(X_R\), under which the report is not invariant.

On the old recorded/core observable algebra generated by \(C,B,S,Z_j\), and the specified old clock and work observables, bare \(U\) and \(\widetilde U\) have the same conjugation action. They also both stabilize the prepared history. But they act differently on the previously unqueried \(X_j\) record-control operation, and can differ on other observables. Thus old data and this restricted algebra do **not** select one extension as the full physical gauge law. Which action is genuinely a redundancy, a physical counterpart, or neither remains a substantive question; it must not be chosen solely to manufacture a sign.

## 4. The record trade-off is exact

The relative sign uses \(X_j\) in the \(B=-1\) sector, so neither \(C_{\rm int}\) nor its sign gate commutes with the physical old record \(Z_j\). In the actual history, before the sign readout,

\[
 P(i,j)=\begin{pmatrix}3/40&1/20\\1/10&3/10\\13/40&3/20\end{pmatrix}.
\]

After applying the sign gate and ignoring M, the same physical register has

\[
 P_{\rm after}(i,j)=
 \begin{pmatrix}1/10&1/40\\1/4&3/20\\2/5&3/40\end{pmatrix}.
\]

Alice's old record \(i\) and the joint \((i,B)\) table are unchanged, and \(B\) remains a perfect record of the **earlier** \(j\), because \(B\) is conserved by the gate. But comparing the final physical \(j\) register with the preserved sphere value yields disagreement probability **1/4** within the valid history. The old record has not vanished from the whole: its information survives in B and correlations. It is nevertheless false to say that the old physical record is left intact or that an observer restricted to the register alone can always recover it. A joint interface to B is required; reversible operation and any subsequent record restoration have their own resource requirements.

The trade-off is not merely a flaw of this particular gate. Assume an operator is exchange odd, commutes with \(B\), preserves \(Z_j\), and is invariant under \(\widetilde U\). In the joint block \(B=-1\), \(Z_j=z=\pm1\),

\[
 \widetilde U=(-S)(-Z_j)=zS.
\]

Invariance in that block therefore requires the operator to be **even** under S, whereas the stipulated sign condition requires it to be **odd**. Its block must vanish. Because it also commutes with B and \(Z_j\), there are no off-block matrix elements to restore a sharp sign there. Hence no such operator can square to the identity on the entire valid sector. This projector argument does not assume a special chirality ansatz or the previous clock/reversal conditions; it also permits arbitrary additional degrees of freedom on which these stated symmetry actions are trivial. A new gauge-transforming reference, a changed symmetry, a disturbed record, or relaxing another premise can evade it.

A related, stronger statement holds for the **bare** \(U\): on \(B=-1\), \(U=-S\). Thus any B-preserving, S-odd operator invariant under bare U vanishes on that entire block, irrespective of clock details and any U-neutral ancillas. The prior restricted-algebra no-go is an instance of this more general obstruction. If a sign is not required to be S-odd, or may fail to commute with B, this particular proof does not apply.

## 5. Consequence for the whole-reality program

This is a concrete way to strengthen the internal connections: an existing correlation supplies the transforming reference, the same original modeled history supplies the clock and orientation, and a single explicit interaction produces the invariant relational record. The information needed to maintain one earlier record is transferred to another existing degree of freedom rather than silently assumed away. It is also a precise example of why an interface boundary matters: one interface sees a changed register; another with access to the sphere can reconstruct the earlier outcome.

Nothing in the construction equates a pointer sign with positive or negative **felt** experience. The selected gauge extension, observer access, causal role of the record, subject incidence, and correspondence to phenomenal quality are not derived. Nor do paired Born probabilities establish necessary plenitude or a globally additive experiential cancellation. A local suffering experience, if present, is not removed by a compensating formal sign. The result is progress on internal self-sufficiency of a finite relational mechanism, not a claim that the proposed zero constitution or objective whole-energy has been derived.

## Subsequent common-domain subject comparison

[One disturbed history, two experiential bridges](ZERO_INTERNAL_REFERENCE_SUBJECT_VALENCE_COMPARISON.md) tests two explicit conditional quality assignments on all 16 histories. Both are compatible with the stated dressed gauge and Born-weighted mirror balance, but disagree after this disturbance on one quarter of the weight; their access and subject-incidence assumptions are separate.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.zero_internal_contextual_reference_test -v
```

The verifier checks the actual 16 modeled clock histories, encoded reference algebra, symmetry-covariant gate, source/branch constraints and the full joint record tables. It does not analyze neuroscience data or establish subjecthood.
