# A balanced relational sign with a charge-preserving record

## Result

The preceding [reference and confined-report analysis](ZERO_INTERNAL_REFERENCE_CONFINED_REPORT_NECESSITY.md) found that copying the old sign \(j=Z_RZ_T\) directly to a neutral pointer disturbs two of the existing exact orientation-zero constraints. Here is a constructive alternative in the **same code-plus-complement clock/work model**:

- Add a pair of internal spin-half references in a stipulated singlet, so their *total* orientation charge starts at zero although their individual charges fluctuate.
- Form a rotationally invariant relational **chirality** from the old record/work/target algebra and the two new references.
- Copy its opposite signs to a neutral pointer with an explicit unitary. Each recorded branch preserves the **enlarged total** orientation zero and the old record–work balance.
- The new sign and record remain compatible with the existing later relational-clock dynamics; the relevant operators commute exactly.

The test uses every old clock label in the code, qubit, spin-1, spin-4 and scalar-remainder state types. Each sign has weight one half and remains paired with the other under an explicit reference-exchange transformation. This is a genuine noncommuting, charge-preserving report construction, not merely a table in which a label has been declared accessible.

There are important qualifications. The additional reference pair, its singlet preparation, its location and the controlled measurement interaction are **supplied**, not derived from zero. The new sign is **not** the old sign \(j\): a sequential test gives no predictive correlation between them. The enlarged total charges stay zero, but the original subsystem's orientation charges do not each remain zero after the interaction. Finally, the report is accessible only to an interface that actually includes the named record/work/target factors, both new references and the pointer. The construction does not establish that any existing confined subject has such an interface, that the sign is felt, or that opposite report values are opposite experiences.

Executable check: [`verification/zero_relational_chirality_report_test.py`](verification/zero_relational_chirality_report_test.py).

## 1. The actual old orientation algebra

Use the earlier active record \(R\), work \(W\), target \(T\), and reference \(F\). The previously specified operators

\[
 A_1=U_8=-Z_R X_W X_T,\quad
 A_2=U_1=-Z_R Z_W X_T,\quad
 A_3=J_W
\]

obey the Pauli algebra \([A_i,A_j]=2i\epsilon_{ijk}A_k\). The old reference carries \(B=(-X_F,-Y_F,Z_F)\), so the three orientation constraints are \(C_i=A_i+B_i\). The old states satisfy \(C_i|\psi\rangle=0\) and \(L|\psi\rangle=|\psi\rangle\). On this active support the prior balance \(Q_0=0\) follows from \(L=+1\).

The old sign \(j=Z_RZ_T\) is, on \(L=+1\), the same component as \(A_3=J_W\). It is therefore a *component* of an orientation algebra, not by itself a scalar relative to a complete orientation reference. A direct neutral-pointer readout need not preserve the three old component constraints, as the preceding report quantified.

## 2. Add a balanced reference and build a scalar

Add two distinguishable internal spin registers \(D,E\), transforming under the same orientation algebra, in the spin singlet

\[
 |s\rangle_{DE}=(|01\rangle-|10\rangle)/\sqrt2.
\]

The enlarged declared charges are

\[
 \mathcal C_i=C_i+\sigma^D_i+\sigma^E_i.
\]

Because the old state has \(C_i=0\) and the added pair has \((\sigma_i^D+\sigma_i^E)|s\rangle=0\), the combined input satisfies \(\mathcal C_i=0\) exactly. This is a balanced *resource*, not absence of local structure.

Define the relational pseudoscalar

\[
 \chi=\frac{1}{2\sqrt3}\sum_{ijk}\epsilon_{ijk}A_i\sigma_j^D\sigma_k^E.
\]

It is Hermitian, commutes with every \(\mathcal C_i\), and commutes with \(L\). On the full active spin algebra, its spectrum is \(\{-1,0,+1\}\); the actual old zero-sector state with the new singlet lies entirely in the \(\chi^2=1\) support. Thus both signs are nonzero and the zero eigenvalue has no weight for this input.

This scalar has a concrete interaction-algebra interpretation. With the invariant exchange operators

\[
 S_{AD}=(I+A\cdot\sigma^D)/2,\qquad
 S_{AE}=(I+A\cdot\sigma^E)/2,
\]

\[
 \chi=-\frac{i}{\sqrt3}[S_{AD},S_{AE}].
\]

Their noncommutativity supplies a directed, relational distinction while each exchange commutes with the enlarged charges. This algebra does not by itself select a Hamiltonian or construct an autonomous device; the specified interaction is an input.

## 3. A concrete pointer unitary, with branchwise zero

Let

\[
 P_+=(\chi^2+\chi)/2,\quad P_-=(\chi^2-\chi)/2,\quad P_0=I-\chi^2.
\]

For a neutral report qubit \(M\) initially in \(|0\rangle\), the explicitly unitary interaction

\[
 U_{\rm rep}=(I-P_-)\otimes I_M+P_-\otimes X_M
\]

writes \(+\) to \(M=0\) and \(-\) to \(M=1\) on the actual \(\chi^2=1\) support. On the unused zero eigenspace it leaves the pointer unchanged. This gate is generated in a unit parameter interval by the specified Hamiltonian

\[
 H_{\rm rep}=\frac{\pi}{2}P_-\otimes(I-X_M),\qquad U_{\rm rep}=e^{-iH_{\rm rep}}.
\]

The generator itself commutes with the enlarged charges. Its pulse and control are still stipulated; the parameter is not an assumed external cosmic time. The verifier checks the exponential, full matrix unitarity and

\[
 [U_{\rm rep},\mathcal C_i\otimes I_M]=0,\qquad
 [U_{\rm rep},L\otimes I_M]=0.
\]

Consequently, both **individual recorded branches** have \(\mathcal C_i=0\), \(L=+1\), and the old \(Q_0=0\) condition. This is stronger than a vanishing average. A full-work-space extension is also checked: it acts trivially on the inactive work complement and commutes with the existing four stated work-number combinations. The lab and old clocks are untouched by the report operation. D, E and M are assigned no energy in the old energy accounting, and the preparation, switching/control and interaction energies are not derived; these finite constraints are not a proof of objective global cosmic energy zero.

**The zero being preserved is the enlarged charge**, not each \(C_i\) of the old subsystem. In either new sign branch the test obtains \(\langle C_i^2\rangle=4/3\) for each original orientation component. The new references compensate those nonzero subsystem contributions. Claiming the original \(C_i=0\) persists separately would be false.

## 4. Pairing and the existing histories

Exchange the new registers \(D\leftrightarrow E\). It reverses \(\chi\), commutes with the enlarged total charges, and takes the initially prepared singlet to itself up to minus sign. Combined with \(X_M\), it exchanges the two recorded branches while leaving the unselected final state invariant up to that same physically irrelevant global phase.

In the actual code and all four complement instrument types, for **every one of the 16 old relative-clock labels**, the test finds

\[
 P(i,\chi=+1)=P(i,\chi=-1)=\tfrac12 P(i),
 \qquad P(i)=q_i
\]

after normalizing that clock label. It checks the complete expanded state and both branch constraints, not just the probabilities. Thus the three-label old-clock window still has weight \(3/16\), and either chirality sign in that window has weight \(3/32\), in the stipulated Born description. The sign pairing itself does not determine actual subject incidence or prove a Born self-location rule.

The old later-clock Hamiltonian uses the logical operators \(X_L,Z_L\). Both commute with \(\chi\), \(P_\pm\), and all enlarged charges. Therefore its unitary relative evolution and the associated clock isometry preserve the report, its branchwise charge balance and the pairing for **all phases**. This is an operator consequence, not an extrapolation from only sampled phases. It does not establish an irreversible or permanent memory under arbitrary future interactions.

Exchange of D and E reverses the formal sign, but whether exchanging those roles identifies a gauge redundancy or relates physically distinct reference configurations is a separate interpretive question. The extra pointer does record distinguishable outcomes in the specified circuit. Neither fact establishes two subjects, felt opposition or suffering.

## 5. What the new sign does—and does not—resolve

The invariant chirality is not simply a concealed version of the old \(j\). On the old common-zero sector with the new singlet, a sequential diagnostic—first record \(\chi\), then hypothetically read the old \(j\)—has

\[
 P(\chi=\pm1,j=\pm1)=1/4
\]

for all four sign combinations. The second sharp measurement is a diagnostic and is **not** claimed to preserve the enlarged constraints. The result demonstrates why the new construction avoids the old obstruction: it records a different, relationally invariant observable rather than perfectly recovering a frame-dependent component for free.

It gives a sharper version of the experiential problem. Two formal assignments on the same joint cells are

\[
 v_1=\chi,\qquad v_2=\operatorname{sgn}(d_i)\chi.
\]

Both are odd under the reference-exchange pairing and have zero Born-weighted mean. Because \(\chi\) and the sphere label \(i\) have the joint distribution above, their signs disagree on the negative-\(d_i\) settings, of weight \(3/5\). An interface that can read \(\chi\) does not thereby have access to Alice's \(i\). For the complement blocks, the preceding single-copy local-discrimination bounds still apply to a report of \(\operatorname{sgn}(d_i)\) if the new pair is prepared independently and no information is communicated from Alice.

This neither proves that \(v_1\) is felt nor rules out an unreportable experience. Rather, it exhibits a physically conserving **candidate sign plus a real report channel** and distinguishes that channel from the extra, unprovided access needed by \(v_2\). A justified psychophysical identity, actual subject boundary and incidence measure remain essential. If a future derivation identifies one negative branch as suffering and pairs it with positive felt valence, global signed cancellation would not remove the suffering within that branch.

## 6. Next constitutive question

The construction changes the problem from “can a signed report coexist with zero?” to the more demanding question: **can the extra reference pair, its interaction and the appropriate subject/interface boundary be selected or generated by the same self-sufficient constitution, rather than inserted by hand?** A continuation should also reconcile the reference-relative quantum construction with a physical, noncompact relativistic reference, and derive the physical–experiential identity and actual incidence measure. Nothing here establishes the whole's objective total energy or exhausts genuine possibilities.

## Verification

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
  python -m unittest verification.zero_relational_chirality_report_test -v
```

The checks use finite NumPy matrices and exact operator identities up to numerical tolerance. The spinor/clock input, new singlet, controlled pointer interaction, local access and physical significance are stipulated. Tests do not establish consciousness, truthful experiential reports, or zero's metaphysical necessity.
