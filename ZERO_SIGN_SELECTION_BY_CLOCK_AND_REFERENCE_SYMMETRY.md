# Sign selection by clock and reference symmetry

Follow-up: [A symmetry between the two signs—and a relational way to report one](ZERO_CONTEXTUAL_SIGN_SYMMETRY_AND_RELATIONAL_DRESSING.md) constructs a history-preserving transformation exchanging the two signs and a sharp report relative to a symmetry-transforming reference.

## Result

There is a genuine, conditional selection result in the **same 90-dimensional sign-preserving orientation and existing 72-dimensional report sector**. On the actual common-zero spin sector with the old work condition \(L=+1\), require a sharp Hermitian sign to:

1. commute with both generators of the old internal clock;
2. reverse under exchange of the two D/E reference spins; and
3. reverse under a specified antiunitary *spin reversal*.

If it acts trivially on the sphere, irrep, classical records and other unmodeled factors, these conditions select the existing relative chirality **uniquely up to an overall sign**. This holds even allowing arbitrary action on the old four-dimensional neutral multiplicity: spin-only action need not be assumed. The proof comes from two commuting qubit algebras already present in the old history.

However, those same conditions **do not select chirality once the existing Bob sphere factor is admitted**. The old Bob measurement axis \(B_s\) commutes with that sphere instrument, both clock generators, the work condition, the 90-dimensional orientation and the relevant lab charges and energies. With a specified reversal convention under which \(B_s\) is even, both

\[
 C\quad\text{and}\quad C B_s
\]

are sharp, conserved, exchange-odd and reversal-odd. They are not related by a single global sign and differ on **half** of the actual conditional history's Born weight. Their controls can be implemented with neutral sign pointers after the original sphere measurement, assuming the necessary joint interface. Thus even preserving the old instrument, the clock and the work constraint does not by itself select a sign. The earlier transverse sphere sign fails the nondisturbance requirement, but \(CB_s\) supplies a stronger counterexample that does not rely on that disturbance.

This is an exact result for the explicitly stated finite model and declared reversal action. The reversal and sign-selection criteria are proposed mathematical conditions, **not derived laws of physical time reversal or felt valence**. The 108-dimensional alternative has a different orientation algebra and is not the setting in which the old chirality is conserved. Verifier: [`verification/zero_spin_reversal_sign_selection_test.py`](verification/zero_spin_reversal_sign_selection_test.py).

## 1. What is being compared

As in the [old relative-chirality construction](ZERO_RELATIVE_SIGN_GAUGE_COUNTERPART_CONSTRUCTION.md), the encoded A/F/D/E orientation has total generators

\[
 K_i=A_i+F_i+D_i+E_i,
\]

using the actual spin conventions \(F=(-X,-Y,Z)\). In the four-spin factor, the common-zero projector \(P_0\) has rank two. The diagonal swap \(G=S_{AF}S_{DE}\) is the identity there. With the original four-dimensional neutral multiplicity retained, the old work condition selects

\[
 P=P_0\frac{I+L}{2},\qquad \operatorname{rank}P=4
\]

in the compressed 64-dimensional spin/work space. Define \(C=PVP\), where \(V\) is the actual old relative chirality, and \(S=PS_{DE}P\). Then

\[
 C^2=S^2=P,\qquad SC=-CS.
\]

The test explicitly transforms the **existing** compressed operators into the four-spin plus neutral basis and checks these identities; it does not replace the old model with an unrelated spin system. The common physical report sector occurs with weight \(72/256=9/32\) in the original full paired source. The remaining \(23/32\) is retained and not assigned either report by this construction.

There are two importantly different reversals:

- **Reference exchange** \(S_{DE}\) is a unitary operator already present in the finite model. It reverses \(C\); the diagonal \(G\) does not. The swap can be treated as a physical counterpart only if the physical interface and gauge specification justify that status.
- Define \(\Theta= (iY)^{\otimes4}K\) on A/F/D/E, extended by complex conjugation in the explicitly chosen neutral basis. It flips all four spin triples, has \(\Theta^2=+1\), leaves \(P,S\) even, and sends \(C\) to \(-C\). The prepared four-spin source is invariant up to phase. This is a **chosen antiunitary symmetry of the spin representation**, not a claim that the complete lab state, preparation, clock sequence and apparatus have a physical time-reversal symmetry. In particular, a psychological positive/negative sign is not known to be odd under physical time reversal. The requirement of reversal oddness is an input to the selection theorem, not a derived property of valence.

## 2. A constructive selection theorem

Let \(X_c=P X_LP\) and \(Z_c=P Z_LP\), using the two actual clock generators. The verifier checks that \(S,C\) and \(X_c,Z_c\) each form a Pauli pair on the rank-four sector, and that the two pairs commute with one another:

\[
 \{S,C\}=0,\qquad \{X_c,Z_c\}=0,\qquad
 [S,X_c]=[S,Z_c]=[C,X_c]=[C,Z_c]=0.
\]

Each squares to \(P\). The 16 products of

\[
 (P,S,C,iSC)\quad\text{and}\quad(P,X_c,Z_c,iX_cZ_c)
\]

are orthogonal Hermitian matrices and span the full operator algebra on this four-dimensional sector. Hence an arbitrary Hermitian operator commuting with **both** clock generators has the form

\[
 O=aP+bS+cC+d\,iSC,\quad a,b,c,d\in\mathbb R.
\]

Exchange oddness removes \(P,S\). Antiunitarity matters: \(\Theta C\Theta^{-1}=-C\), but \(\Theta(iSC)\Theta^{-1}=+iSC\), since conjugation also reverses \(i\). Reversal oddness therefore removes \(iSC\), leaving \(O=cC\). If a valid sign is required to satisfy \(O^2=P\), then \(O=\pm C\).

This argument does **not** require guessing an operator ansatz or discarding the neutral multiplicity. The verifier also computes the full real linear constraint map on all 64 Hermitian operators on the rank-eight spin-zero sector before imposing \(L=+1\). Its null space has dimension two, spanned by the old sign and that sign multiplied by \(L\); they agree on the declared \(L=+1\) sector. The numerical rank check is backed by the explicit Pauli-algebra argument above. Outside \(P\), no sign is asserted and the full source is not truncated.

The theorem singles out an **oriented relation**, not which of its two values is pleasure or suffering. Reversing the convention still exchanges \(+C\) and \(-C\). Also, commuting with these two specified clock generators is a stronger condition than merely preserving one chosen clock state. Why this clock algebra, D/E exchange, spin reversal, and the absence of dependence on other factors should be constitutive requirements remains to be explained.

## 3. The existing sphere defeats uniqueness in a sharper way

The old Bob sphere instrument is a two-outcome projective measurement of the actual Bloch observable

\[
 B_s=\mathbf b\cdot\boldsymbol\sigma,\quad
 \mathbf b=(1/5,2\sqrt3/5,-2\sqrt3/5).
\]

This is not the later transverse sign \(\mathbf c\cdot\boldsymbol\sigma\). \(B_s\) commutes with both old Bob Kraus operators, and Alice's sphere operations act on the other lab. The verifier lifts \(B_s\) into the original physical 256-dimensional Bob lab and checks its commutators with the actual Bob instrument, old lab charges, declared lab Hamiltonians and the sign-preserving orientation extension. It acts on the sphere factor, whereas the old chirality acts on the spectator/encoded work factor.

Let the stipulated reversal on the sphere be complex conjugation in a \(B_s\) eigenbasis. It fixes \(B_s\) and squares to identity. With that explicit extension of \(\Theta\), both \(C\) and \(CB_s\) are odd under D/E exchange and under \(\Theta\), commute with the old clock and work operators, and square to the valid-sector identity. Both preserve the old lab and orientation constraints. One may write either sign into a neutral pointer using

\[
 U_O=(I-P_-^{O})\otimes I_M+P_-^{O}\otimes X_M,
 \qquad P_-^{O}=(P_{\rm valid}-O)/2,
\]

with a separate valid/no-sign flag for the retained remainder. The gate acts as the identity on the invalid sector. The sign interactions and joint access are stipulated; their autonomous implementation and complete apparatus energy are not derived. **Commuting with the old sphere Kraus operators is an operator statement; it does not mean the pointer gate commutes with every earlier record-writing interaction.** The proposed order is the old instrument and history first, sign reporting afterward.

There is an even stronger restricted classification. If the only additionally admitted factor is this Bob sphere qubit, and the candidate must commute with its old two-outcome instrument, then its sphere component lies in \(\operatorname{span}\{I,B_s\}\). Using the same clock, work, exchange and reversal requirements as above gives

\[
 O=C(aI+bB_s),\qquad a,b\in\mathbb R.
\]

Requiring \(O^2=P\otimes I\) gives \(a^2+b^2=1\) and \(ab=0\). Therefore the **only** sharp candidates in this restricted class are

\[
 O=\pm C,\quad O=\pm CB_s.
\]

They are two choices up to global sign, not an arbitrary continuum. This classification assumes the specified reversal action on the sphere and excludes other factors and context-dependent admissibility rules. It shows exactly how adding a real, conserved relational degree of freedom restores ambiguity after a mathematically meaningful selection on the smaller algebra.

## 4. What the actual history says about the two candidates

After the old Bob outcome \(j=0,1\), the actual sphere state satisfies \(B_s=(-1)^j\). The verifier checks this on the complete compressed history for **all 16 old relative-clock labels**, including each old chirality branch. It is a state-dependent relation, not an operator identity between the sphere and the classical record. The actual outcome table, normalized within each clock label and report sector, is

\[
 P(i,j)=\begin{pmatrix}3/40&1/20\\1/10&3/10\\13/40&3/20\end{pmatrix}.
\]

Both \(C=s\) and \(CB_s=s(-1)^j\) are equally likely \(\pm1\) conditional on every \((i,j)\). They agree when \(j=0\) and disagree when \(j=1\); the latter has total weight **1/2**. Each sign gate leaves the old \(i,j\) registers intact, the \(L=+1\) condition and total orientation zero in every branch. Neither sign is a mere fixed global relabeling of the other. If both \(j\) and one sign are available, either sign can be computed from the other; whether such a context-dependent relabeling is a physical change of question or an admissible gauge identification is a further interpretive decision, not fixed by the matrices.

The verifier separately constructs the version \(CZ_j\) using the already existing classical outcome register \(Z_j\). It is an independent joint-interface implementation that agrees with \(CB_s\) **on the prepared histories**. This is not an assertion that either factor is automatically accessible to a confined subject, nor that the two global operators are identical outside those histories.

## 5. Pairing and plenitude: what follows, conditionally

The old D/E swap preserves each unselected prepared history up to phase, leaves the old records and \(B_s\) unchanged, and reverses both candidate signs. Consequently, its two sign branches have equal Born weight. More generally, if a proposed incidence measure is invariant under this swap and treats its two branches as distinct incidences, then their measures are equal and any equal-magnitude sign assignment odd under the swap has zero mean. This is a conditional pairing theorem, **not** a derivation of the physical-to-subject incidence measure.

If instead the swap is a gauge identification of the *same* incidence, an odd absolute sign is not gauge invariant; the two branches cannot simply be counted as distinct opposite subjects. Conversely, a physical state symmetry does not by itself prove that all related branches are actual or that a subject-weighting measure is invariant. Necessary plenitude might support such a pairing only once the theory establishes genuine possibility, physical versus gauge equivalence, subject incidence, measure and convergence. Neither assigning equal Born weights nor asserting that alternatives are impossible settles those issues.

The constructive lesson is sharper than “any sign works”: clock and symmetry select a unique chirality on a specified algebra, while admitting an already-existing compatible sphere relation yields exactly two classes of sharp signs. To make zero's constitution determine **felt** sign, the theory must explain which algebra and reversal law characterize a subject, whether the sphere relation belongs to that incidence, why either operational sign has a particular qualitative character, and how physical counterparts receive experiential weights. None of these steps follows merely from relabeling a pointer. A zero formal mean does not erase locally felt suffering or equate negative experience with its absence.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.zero_spin_reversal_sign_selection_test -v
```

The calculations check finite operator identities and the actual modeled history. They are not neuroscience evidence, a derivation of objective cosmic energy, or a proof that bare zero selects this model.
