# An invariant upstream source for the differentiated history

**Subsequent extension and sharper accounting:** [Extending the balanced orientation and opening a report boundary](ZERO_ORIENTATION_EXTENSION_AND_DYNAMIC_REPORT_BOUNDARY.md) extends this chosen charge to additional sectors without changing the old sign gate. It also shows that only 54 of the 72 report-sector dimensions carry a nontrivial local orientation representation; the other 18 form a local singlet. A separate alternative reaches 108 nontrivial dimensions but does not preserve the old neutral-pointer report gate.

## Result

There is a constructive way around the specific obstruction in the [previous F-transfer result](ZERO_INTERNAL_F_REFERENCE_TRANSFER_AND_ORIENTATION_LEDGER.md): **do not prepare the old oriented A qubit as an extra physical system and then swap it into the labs**. Instead, use the lab's existing H qubit *as* the A orientation qubit from the start. Its F partner is already present in the original paired state.

On the same 72-dimensional lab sector, this gives the sphere pair, the D/E pair and the A/F pair simultaneously. The last two pairs are singlets of a specified orientation algebra. A neutral pointer-controlled operation then builds the old record–work–target history in an additional four-dimensional **orientation-neutral degeneracy space**. After decoding the logical record–work–target algebra, its entire reference-extended output is exactly the earlier source, at every old relative-clock label. The old gauge-even sign report and its conserved branches carry over.

The construction also retains the full original paired lab state, not just the selected sector. The specified orientation generators act trivially outside the 72-dimensional support; with that explicit choice, **the whole unconditioned lab state**, and every tested sphere-outcome branch, have zero total of all three new orientation generators. This does not make the remainder physically empty, experience-free or unimportant. The representation choice, the validity sector and neutral controls are inputs, and the sign report is only constructed in the selected sector. The finite orientation charge is not objective whole-universe energy.

This is a different **upstream physical preparation and subsystem encoding**, not a charge-conserving conversion of the earlier already-oriented A input. It therefore does not contradict the previous no-go. It removes the previously retained nonzero-spin partner from this particular construction, while making the change of preparation and the remaining assumptions visible.

Verifier: [`verification/zero_upstream_invariant_internal_history_test.py`](verification/zero_upstream_invariant_internal_history_test.py). It uses the actual lab basis and three-pair amplitudes from [`verification/zero_internal_f_reference_transfer_test.py`](verification/zero_internal_f_reference_transfer_test.py), and the existing sphere, old history, reference and sign operators.

## 1. The same lab state supplies both balancing pairs

As before, the original 256-dimensional-per-lab paired state has, on the selected 72-dimensional local sector, the normalized factorization

\[
 |\Phi^+\rangle_{SS'}\otimes|\psi^-\rangle_{DE}
 \otimes|\Psi^+\rangle_{HF}\otimes|\Phi_9\rangle_{\rm spectator}.
\]

The first pair supports the unchanged old exact-qubit sphere instrument; D/E is the sign reference; H/F is the former F resource. Use

\[
 A_i=\sigma^H_i,\qquad B_i=(-X_F,-Y_F,Z_F)_i,
 \qquad \mathcal C_i=A_i+B_i+D_i+E_i.
\]

The H/F state is a singlet of \(A+B\), and D/E is a singlet of \(D+E\). Therefore \(\mathcal C_i\) annihilates the selected initial state before the sphere measurement, before any work-history preparation, and before the sign report. The sphere operators act on S/S′ and commute with all four reference spins, so their branches retain this zero.

The re-identification \(A=H\) is the crucial difference from the previous construction. There is no separately prepared old \(|+x\rangle_A\) spin and no swap that transfers its orientation into a fifth partner. The specified apparatus is different; the two input states are not claimed to be unitarily interchangeable under the old full charge.

## 2. Exact whole-lab orientation accounting

Let \(P_A\) be Alice's rank-72 encoded-sector projector and \(P_B=\overline{P_A}\) Bob's. The original paired state has matching support: \(P_AM=M P_B^T\). Define the four encoded spin triples on their respective selected local sectors, with each operator zero on the orthogonal local sector. This is a direct-sum representation: **trivial outside the selected sector**, not a claim that other degrees of freedom have no physical structure.

The verifier checks the actual 256-dimensional local matrices obey the Pauli and commuting-factor algebras and, for the original full amplitude \(M\),

\[
 (A_i+D_i)M+M(B_i+E_i)^T=0\quad(i=x,y,z).
\]

No sector projection or renormalization occurs in this identity. The local new spin operators also commute with the model's original local charges and declared lab Hamiltonians. The test uses complete Alice and Bob instruments which preserve the earlier physical qubit sphere Kraus operators on all **190 complement dimensions** and use neutral scalar effects on the remaining 66 dimensions, including the original code. On every one of the six joint sphere branches it checks:

- the same total new orientation zero;
- the earlier paired lab-charge relation and declared lab energy balance; and
- completeness of both full-space instruments.

The code's old nontrivial instrument is **not** preserved in this particular complete instrument; the 190-dimensional complement instrument is. The rest has weight \(184/256\) relative to the 72-dimensional report sector, stays in the state, and receives no invented ± sign. A coherent validity flag may distinguish the sectors, at the usual cost of correlating with them. Setting the new orientation action to the trivial representation there is a deliberate model choice, not a derivation of its status from zero or a demonstration of a universal charge for all physical degrees of freedom.

## 3. Build the old history from a neutral degeneracy

The old active record–work–target space is eight-dimensional. Its actual orientation operators \((U_8,U_1,J_W)\) form a full qubit algebra with multiplicity four. The test constructs an explicit unitary \(T\) such that

\[
 T^\dagger(U_8,U_1,J_W)T=(X,Y,Z)\otimes I_4.
\]

Thus an old RWT state can be represented as an orientation qubit A and a four-dimensional neutral factor N. For each Bob pointer value \(j=0,1\), let \(|w_j\rangle\) be the **actual** old RWT output after the old work and target operations. The verifier factors it as

\[
 T^\dagger|w_j\rangle=|+x\rangle_A\otimes|\eta_j\rangle_N,
 \qquad \langle\eta_j|\eta_k\rangle=\delta_{jk}.
\]

It then constructs explicit unitary matrices \(U_j\) on N satisfying \(U_j|0\rangle=|\eta_j\rangle\). The coherent control

\[
 U_{jN}=|0\rangle\langle0|_j\otimes U_0+
         |1\rangle\langle1|_j\otimes U_1
\]

acts on the existing sphere pointer and the neutral factor. It commutes with all \(\mathcal C_i\), since it acts on neither the A/F nor D/E spins. This is a stipulated joint interaction with a prepared neutral blank; its existence is not inferred from a confined observer's access.

Instead of creating the old pure \(|+x\rangle_A\), use the lab H/F singlet and apply \(U_{jN}\). Decoding \(A\otimes N\) back to the old eight-dimensional logical RWT space gives, for the **entire** unconditioned valid-sector history,

\[
 |\Psi_{\rm new}\rangle=\mathrm{initial}(|\Psi_{\rm old}\rangle),
\]

where `initial` is the actual earlier reference isometry followed by the D/E singlet. This is equality of complex amplitudes including the sphere and clock environment and all pointer labels, after the stated encoding—not just the equality of outcome tables. The test independently applies all 16 old relative-clock effects to the new preparation and verifies the same equality at each label.

The old code's active total work number and the previously tested pair-number operators are scalar on its two-dimensional work subspace; their encoded logical counterparts commute with the new neutral control. The existing lab-energy operators are likewise respected. This is an algebraic accounting of those **declared finite-model observables**, not a construction of physical excitations, control energy, a complete work reservoir, or cosmological energy.

## 4. The relative-sign circuit is an operation on the encoded spins

The old 64-dimensional relative-sign operator \(V\), expressed in the T basis, equals the same four-spin operator on \(A,F,D,E\) tensored with identity on N. The verifier checks this entire operator identity and its commutators with the four-spin orientation generators. Consequently its spectral projectors and controlled pointer gate can be assembled from the actual encoded lab spin algebras; no separately added F or fifth H spin is needed.

For each old clock label, the test verifies the old source projector, \(V^2=1\), both sign-branch amplitudes, the old balance and diagonal-swap invariance, and \(\mathcal C_i=0\) in each branch. The previously verified report and later-clock commutators extend the result to the later relative-clock dynamics. The required gate is still a **joint** operation coupling encoded spins across the two labs and a pointer. It is not established as accessible to either confined lab, autonomous, or local in an emergent spacetime.

Conditional on the valid sector and a normalized old-clock label, \(P(i,V=\pm1)=q_i/2\). The valid weight in the unselected original state is \(72/256=9/32\), so each sign has whole-state weight \(9/64\) before clock conditioning. These are statistics of the specified apparatus; neither ± label is identified with a subject or with felt valence. The old two formal sign assignments still disagree on settings of weight \(3/5\), so reproducing the physical source does not select an experiential law.

## 5. Why this does not contradict the previous obstruction

In the earlier swap construction, the **old physically distinct** A was already in a pure \(|+x\rangle\) state. Along with the internally paired F/H resource it made five transforming spin halves once D/E were included. The invariant swap created an A/F singlet but left H carrying the orientation; the full five-spin representation had no singlet.

Here the old physical A is not an additional input. H *is* the encoded A; the transforming factors are the four spins \(A,F,D,E\), initially in two singlets. The old oriented A is present only in the mathematical factorization used to identify the neutral \(|\eta_j\rangle\); it is not added to the new physical source. No nonzero partner is dropped after a swap. Rather, a different preparation reproduces the old **reference-extended** state in a different subsystem encoding.

This distinction matters: the previous no-go still applies to the previous input and conserved algebra. The current result is not a proof that any already oriented source can be made zero by a conserving unitary, or that the alternative blank, encoding and correlations arise automatically.

## 6. What this advances

Within one finite model we now have a single original paired lab input that simultaneously supports a noncommuting sphere, internal reference pairs, an upstream orientation-zero state, a conserving preparation of the old relational history, and a gauge-even sign report—without introducing the previous uncounted spin partner. This is a stronger connection among the ingredients than the late-stage transfer.

The construction remains conditional. The orientation action is specially chosen and trivial on the invalid sector; only part of the whole state has the new report. The lab state, measurement geometry, N blank, controlled interaction, logical encoding, clock and pointer are stipulated. The logical RWT tensor factors are now encoded across a lab qubit and N; equality of abstract amplitudes does not establish the same physical locality or subject boundary. The operational sign remains underdetermined as felt valence, and the required incidence measure is not derived. Neither this orientation zero nor the declared lab energy balance proves a zero total objective cosmological energy or derives structure and experience from zero's own constitution.

The next task is to reduce these remaining *joint* assumptions: in particular, determine whether the orientation representation, neutral history-control and subject-relevant interface follow from a common principle rather than being selected to recover an existing circuit. The invalid sectors must be accounted for in any whole-level claim, not equated with nonexistence.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
  python -m unittest verification.zero_upstream_invariant_internal_history_test -v
```

The physical lab charge identities and all-sector outcome branches are numerical matrix checks. The representation factorization, pointer control, exact decoded histories, 16 old clock labels, relative-sign operator identity and both sign branches are checked independently at the tolerances in the verifier.
