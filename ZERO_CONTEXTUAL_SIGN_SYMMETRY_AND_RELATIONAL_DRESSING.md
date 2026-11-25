# A symmetry between the two signs—and a relational way to report one

Follow-up: [An internal reference from an existing record—and its unavoidable trade-off](ZERO_INTERNAL_CONTEXTUAL_REFERENCE_AND_RECORD_TRADEOFF.md) realizes the transforming reference as a logical qubit in the old sphere and record, and identifies exactly what the new sign gate does to the old record.

## Result

The [previous construction](ZERO_SIGN_SELECTION_BY_CLOCK_AND_REFERENCE_SYMMETRY.md) found two conserved signs, \(C\) and \(CB_s\), on the same old 90-dimensional orientation history. Here they are connected by an **explicit unitary that leaves the complete prepared history unchanged**, preserves the stated constraints and old sphere instrument, and exchanges the two sign observables:

\[
 UCU^\dagger=CB_s,\qquad U(CB_s)U^\dagger=C,\qquad U|\Psi\rangle=|\Psi\rangle.
\]

This makes their relationship more precise than either “two completely unrelated signs” or “obviously the same sign.” The symmetry is **nontrivial on the full physical constraint sector** and exchanges two possible sign-report interactions. It is not automatically a gauge redundancy, nor does fixing the earlier state alone fix which later sign gate is part of the physical history.

The construction yields two conditional alternatives:

1. If this symmetry is required to be a gauge identification and the previous clock, exchange and reversal requirements are retained, no sharp \(\pm1\) sign exists over the whole valid sphere sector in the previous restricted algebra. There is a gauge-invariant **three-valued** report: \(+1\), \(-1\), or an explicit zero/no-sign outcome. On the actual conditional history these carry weights \(1/4,1/4,1/2\).
2. A sharp, symmetry-invariant **relative** sign can be restored by coupling a two-state reference that transforms nontrivially under the symmetry. It may start in a symmetric state, without preselecting either reference label. Its report is a concrete joint gate, but the reference, its transformation law and the joint interface are stipulated—not derived from zero or identified with a subject.

All statements concern the existing 72-dimensional report sector with its retained remainder, not a cosmic no-go or a derivation of phenomenal sign. The exact verifier is [`verification/zero_contextual_sign_symmetry_and_dressed_report_test.py`](verification/zero_contextual_sign_symmetry_and_dressed_report_test.py).

## 1. The history-preserving transformation

In the notation of the previous result, \(C\) is the old relative chirality on the constrained \(L=+1\) sector. \(B_s\) is the original Bob sphere measurement axis, and \(S=S_{DE}\) exchanges the D/E reference spins. On the valid sector,

\[
 C^2=I,\quad B_s^2=I,\quad S^2=I,\quad SCS=-C,\quad [B_s,C]=[B_s,S]=0.
\]

Put \(P_\pm=(I\pm B_s)/2\) and define the joint operation

\[
 U=P_+ -P_- S,\qquad U^2=I.
\]

The minus sign is important. The original D/E reference is a singlet, so \(S=-1\) on the prepared input. Therefore \(U=I\) on that input **for either sphere outcome**, including their coherent superposition. On the other hand, on the full constrained sector,

\[
 UCU=CB_s,\qquad U(CB_s)U=C.
\]

The verifier uses the actual encoded four-spin/neutral factorization, the actual Bob sphere direction and all 16 earlier relative-clock histories. It checks \(U|\Psi_\ell\rangle=|\Psi_\ell\rangle\) and maps each \(C\) sign branch exactly to the corresponding \(CB_s\) sign branch. \(U\) commutes with the total orientation generators, the old clock generators and work constraint, the old diagonal \(G\), \(S\), and \(B_s\). It consequently respects the old Bob sphere instrument; the Alice instrument acts on the separate Alice sphere factor. The older physical lifts check that the reference-spin and sphere operators commute with the specified lab charges and declared lab energies. The operation can be extended as identity outside the separately flagged report sector, retaining the other \(23/32\) of the original paired state.

A concrete generator is

\[
 H_U=\frac{\pi}{2}(I-U)=\pi P_-\frac{I+S}{2},
 \qquad e^{-iH_U}=U
\]

for unit interaction parameter. The factors in the last expression are commuting projectors. This is a **joint D/E–sphere control**: it preserves the total orientation, but not the individual local orientation generators. Implementing it requires an actual cross-interface interaction; neither a confined inhabitant's access nor an autonomous device has been derived. The stated lab/clock charges are not established objective energy of the universe.

The specified spin-reversal antiunitary from the previous theorem, extended to keep \(B_s\) even, also leaves \(U\) even. This is an algebraic property of that chosen reversal, **not** a proof of physical time reversal of the whole preparation and apparatus.

## 2. Why state symmetry is not automatically gauge

For the ready sign pointer, the two specified report circuits are related by conjugating the system with \(U\). Since the input is invariant, their output branches are related by applying \(U\) to the system while retaining the same pointer label. Yet \(U\) is not the identity on the full constrained sector; the test explicitly finds nonzero action there. Consequently, a device calibrated to measure \(C\) and one calibrated to measure \(CB_s\) are distinct modeled interactions if that calibration and the relevant joint observables belong to the physical description.

Indeed, with the *same* fixed pointer labeling, the two pure post-gate states on the actual conditional history have overlap \(1/2\), fidelity \(1/4\), and pure-state trace distance \(\sqrt3/2\). The verifier checks the coherent states, not just their pointer marginal. Their \((i,j,\text{pointer})\) probabilities nevertheless agree; distinguishing the full states requires access beyond those specified marginal records. When both signs are read jointly, they agree on the \(B_s=+1\) branch and disagree on \(B_s=-1\). Thus this is not a global \(+\leftrightarrow-\) relabeling.

One may propose to identify states related by \(U\) as gauge, **provided the identification is applied to the full system and apparatus description**. Then the bare \(C\)-pointer and \(CB_s\)-pointer gates transform into each other; retaining a fixed bare calibration while declaring only the system transformation gauge would be inconsistent. Alternatively, the symmetry may relate distinct physically admissible interactions. The mathematics alone does not decide which ontology or which subject incidences are correct.

## 3. Conditional no-go, with a nonzero invariant remainder

In the previously specified restricted class, the most general exchange-odd, reversal-odd, clock-compatible Hermitian candidate commuting with the Bob instrument is

\[
 O=aC+bCB_s.
\]

Since \(U\) exchanges the two terms, \(UOU=O\) implies \(a=b\). Its square is then

\[
 O^2=2a^2(I+B_s)=4a^2P_+,
\]

on the valid sector. This vanishes on \(P_-\), so it cannot equal the valid-sector identity. Thus **no everywhere-sharp \(\pm1\) sign in that stated class is invariant under \(U\)**. This is a conditional algebraic theorem, not a universal theorem about signs, consciousness, or possible reference systems.

A useful nonzero invariant is

\[
 O_0=CP_+=\tfrac12(C+CB_s),\qquad O_0^2=P_+.
\]

It gives \(\pm1\) on the \(B_s=+1\) sector and 0 on \(B_s=-1\). For each of the 16 normalized relative-clock histories the verifier obtains

\[
 \Pr(O_0=+1)=\tfrac14,\quad
 \Pr(O_0=-1)=\tfrac14,\quad
 \Pr(O_0=0)=\tfrac12.
\]

The 0 is an **operational no-sign outcome** of this chosen observable. It is not proof that experience or value is absent on that branch. The whole invalid-sector flag remains separate from this zero outcome. Including the full original paired-state sector weights, the two nonzero outcomes each carry \(9/128\), the valid zero outcome carries \(9/64\), and the retained invalid sector carries \(23/32\); these sum to one.

## 4. A sharp sign relative to a symmetric reference

Introduce a two-state reference \(R\) and extend the candidate symmetry by

\[
 \widetilde U=U\otimes X_R.
\]

Here R is neutral under the existing orientation and lab-energy constraints, but **transforms nontrivially under the proposed \(U\) identification**. Its basis labels are exchanged; they are not an unchanging outside coordinate. Define

\[
 C_{\rm rel}=C\otimes|0\rangle\langle0|_R
              +CB_s\otimes|1\rangle\langle1|_R.
\]

Since \(U\) swaps \(C\) with \(CB_s\) and \(X_R\) swaps the reference labels,

\[
 \widetilde U C_{\rm rel}\widetilde U^\dagger=C_{\rm rel},
 \qquad C_{\rm rel}^2=I
\]

on the valid sector. It still commutes with the old total orientation, clock, work condition and sphere instrument. A neutral sign pointer M can record it with the usual controlled-projector unitary; the verifier checks that **the entire gate**, not only the observable, commutes with \(\widetilde U\). The pointer is assumed degenerate/neutral under the declared charges; the complete apparatus energy and control remain unspecified.

Prepare R in \(|+\rangle=(|0\rangle+|1\rangle)/\sqrt2\). The initial enlarged history is invariant under \(\widetilde U\) because \(U\) fixes the original history and \(X_R|+\rangle=|+\rangle\). The verifier explicitly constructs both sign branches for every old clock label: each is invariant under \(\widetilde U\), preserves the old records, orientation zero and work condition, and has Born weight \(1/2\) within the valid sector. Including the original paired-state sector weights, each sign carries \(9/64\), while the retained invalid sector carries \(23/32\). Thus a symmetry-invariant sharp *relational* report is possible **without preparing a definite 0-versus-1 reference label**.

This is not a free derivation of a phenomenal sign. R is a new stipulated degree of freedom and must be physically coupled to the system and pointer. The two branches become correlated with R; no claim is made that a confined observer automatically accesses the whole joint record. The result also does not pick an absolute convention for which pointer state means positive feeling. If a larger gauge group additionally identifies the old D/E exchange itself, a sign odd under that exchange is not a gauge-invariant absolute valence. The transformation law and gauge group must be justified independently of the result desired.

## 5. Implication for zero, plenitude and subjects

This construction advances the original question from *which formal sign should we choose?* to a more structured alternative: under a possible symmetry identification, an unreferenced sharp sign is forbidden in a specified algebra, whereas an invariant relative sign exists with an explicitly transforming reference. Zero-compatible relational differentiation is not erased by identifying a symmetry, but its surviving observables and interfaces change.

The existence of a gauge-invariant pointer does not establish a real subject or that its two values are opposite felt valences. Neither the symmetry nor the equal Born weights alone establishes which outcomes are actual, which are distinct subject incidences, or whether a subject measure is symmetry-invariant. Necessary plenitude may constrain those questions, but declaring \(U\) gauge or declaring both branches actual simply to obtain cancellation would assume what needs to be shown. A balanced formal mean does not remove suffering.

The next substantive target is to derive, rather than stipulate, the relevant **reference and incidence structure** from the proposed whole: determine whether an existing internal degree of freedom can play R's role while retaining the full old history and conserving the specified charges, and whether its transformation should be physical or gauge. The current result supplies the exact interface and constraints such a construction must meet.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.zero_contextual_sign_symmetry_and_dressed_report_test -v
```

These finite-dimensional checks do not establish consciousness, the actual-world energy ledger, or the necessity of any particular quantum model.
