# A relative sign that survives one genuine redundancy

**Subsequent resource reduction:** [An internal reference pair from the original paired state](ZERO_INTERNAL_PAIRED_RESOURCE_SPHERE_AND_REPORT.md) constructs the D/E singlet from the same original labs on a 96-dimensional sector, while retaining a genuinely noncommuting sphere there. It also states the sector-coverage tradeoff and remaining joint-interface assumptions.

## The question

The [whole-program synthesis](ZERO_ONE_REALITY_NECESSARY_PLENITUDE_SYNTHESIS.md) exposed a possible conflict. A sign that reverses under a transformation cannot be a nonzero, well-defined felt value **if** that transformation identifies its two labels as the same subject incidence. But not every symmetry is automatically such a redundancy. Can a sign be invariant under a real redescription while still having distinguishable opposite values related by a different symmetry?

For the **existing** conserving-report construction, the answer is yes—under a specific, explicitly identified equivalence. No second reference pair is needed. The prior reference and its paired resource already contain two interlocking orientation relations. Their **relative chirality**:

- is invariant under a simultaneous reversal of both relations;
- has sharp, nonzero opposite values on the entire enlarged orientation-zero sector;
- has an explicitly charge- and symmetry-preserving pointer Hamiltonian;
- reproduces the previous actual recorded state and clock results on the previous prepared input; and
- is reversed by a *different* operation that exchanges the recorded signs.

This does not prove that the opposite reports are actual subjects or felt valences. It also does not prove that the different sign-exchanging operation cannot itself be included in a larger gauge group. It is a concrete separation of **one transformation that acts trivially on all physical zero-sector states** from **another that acts nontrivially on a permitted relative record**. The latter is a candidate counterpart, not yet an experiential identity.

Verifier: [`verification/zero_relative_gauge_invariant_report_test.py`](verification/zero_relative_gauge_invariant_report_test.py). It imports the actual operators and histories in [`ZERO_CONSERVING_RELATIONAL_CHIRALITY_REPORT.md`](ZERO_CONSERVING_RELATIONAL_CHIRALITY_REPORT.md).

## 1. Two chirality conventions, already in the model

The earlier active orientation algebra has four Pauli triples:

- \(A\), encoded jointly in the original record–work–target factors;
- \(B=(-X_F,-Y_F,Z_F)\), carried by the original reference F;
- \(D,E\), the two spins in the added reference pair.

All four transform under the same total orientation algebra, with

\[
 \mathcal C_i=A_i+B_i+D_i+E_i,\qquad \mathcal C_i|\psi\rangle=0.
\]

The original chirality used in the recorded circuit was

\[
 \chi_A=\frac{A\cdot(D\times E)}{2\sqrt3}.
\]

We can form the corresponding relation using the **already present** F reference:

\[
 \chi_B=\frac{B\cdot(D\times E)}{2\sqrt3},\qquad
 V=\frac{\chi_A-\chi_B}{2}.
\]

This is not a new physical law or the addition of another reference pair. It is an operator defined from the existing four algebras. Both chiralities and \(V\) commute with all three enlarged charges and with the earlier balance \(L\). They also commute with the two generators of the previously used later clock Hamiltonian, so the relational-clock construction does not require a preferred external time.

## 2. A simultaneous swap acts as identity on the whole zero sector

Let \(S_{AB}=(I+A\cdot B)/2\) exchange the A and B spin algebras, and let \(S_{DE}\) exchange D and E. Define the diagonal transformation

\[
 G=S_{AB}S_{DE}.
\]

It exchanges A with B **and** D with E. Thus it reverses each orientation convention but preserves their relative sign:

\[
 GVG=V.
\]

More strongly, if \(P_{\mathcal C=0}\) is the projector onto the entire common-zero space of the three \(\mathcal C_i\), the tested operator identity is

\[
 G P_{\mathcal C=0}=P_{\mathcal C=0}.
\]

In the compressed 64-dimensional spin/interface space that zero sector has rank 8. A representation-theoretic reason is that the AB and DE pairs each have spin 0 or 1; total spin zero requires the two pair spins to agree. The exchange eigenvalue is \(-1\) for a singlet and \(+1\) for a triplet, so their product is \(+1\) in either allowed pairing.

Hence, **within this declared physical constraint sector**, the diagonal swap is not merely a symmetry of one specially chosen state: it acts identically on every zero-sector state. Treating that action as a redundancy on this sector is mathematically justified. Whether the final theory has additional gauge identifications, extra physical degrees of freedom, or different constraints is not decided.

On the same entire zero sector,

\[
 V P_{\mathcal C=0}=\chi_A P_{\mathcal C=0},\qquad
 V^2P_{\mathcal C=0}=P_{\mathcal C=0}.
\]

So the old chirality report has a globally diagonal-swap-invariant **relative representative** on the constrained physical states. Its opposite values are not removed merely by identifying this simultaneous swap. This is a more precise result than simply saying that a mathematical chirality is gauge invariant: the physical sector and the particular action being quotiented are stated.

## 3. The relative sign and its exact report

On the full compressed space, \(V\) has spectrum

\[
 \{0,\ \pm1/\sqrt3,\ \pm1\}.
\]

Its \(\pm1\) eigenspaces are exactly the two halves of the total-zero sector. The corresponding full-space projectors can be written

\[
 Q_\pm=\frac34 V^2\left(V^2-\frac I3\right)(I\pm V),
 \qquad Q_++Q_-=P_{\mathcal C=0}.
\]

Each has rank four, or rank two after imposing the old \(L=+1\) condition. The other eigenvalues lie outside the total-zero sector; the pointer described below does not purport to measure their signs.

For a neutral report pointer M initially in \(|0\rangle\), set

\[
 H_{\rm rel}=\frac\pi2Q_-\otimes(I-X_M),\qquad
 U_{\rm rel}=e^{-iH_{\rm rel}}
 =(I-Q_-)\otimes I_M+Q_-\otimes X_M.
\]

This writes the two relative signs into M on the total-zero sector. The verifier checks the exponential and exact matrix commutation of \(H_{\rm rel}\) and \(U_{\rm rel}\) with the enlarged charges, \(L\), and the diagonal transformation \(G\). Each recorded branch therefore keeps the enlarged orientation zero and old work balance. The pointer and control are still stipulated; their complete energy ledger and autonomous operation are not derived.

There is also a full physical-work-space extension, including the inactive 16-state work complement. The test checks the relative operator's enlarged-charge, diagonal-swap and previously declared work-number commutators there. The old lab and clock factors are untouched. These are finite-model conservation statements, not a derivation of a zero total energy for the universe.

## 4. This is an exact strengthening, not a new independent experiment

The previous input had the old A–B zero state, \(L=+1\), and the D–E singlet. Let \(P_{\rm source}\) denote that whole prepared spin support. The test establishes

\[
 Q_\pm P_{\rm source}=P_\pm^{(\chi_A)}P_{\rm source},
\]

where \(P_\pm^{(\chi_A)}\) are the old chirality report's projectors. With the pointer ready in \(|0\rangle\), the new and old unitaries therefore produce the **same full post-interaction state on every input in that source subspace**, not just the same probabilities.

This is why the earlier calculation's results transfer without selecting a new branch or changing the lab state. That calculation checked all 16 old clock labels for the code, qubit, spin-1, spin-4 and scalar-remainder instrument types. The new test additionally checks the actual code and three noncommuting complement types in the three-label window. The new report commutes with the later clock generators, so preservation extends to all their relative phases.

For the actual specified source and a normalized old-clock label,

\[
 P(i,V=+1)=P(i,V=-1)=q_i/2,
 \qquad q=(1/8,2/5,19/40).
\]

These are Born statistics of the finite circuit. The new insight is the **invariant interpretation and full-space implementation**, not an observational distinction from the old report on this prepared source. Source preparation, the resource pair, the interaction, and the physical significance of the relevant interface remain inputs.

## 5. A distinct counterpart transformation, and the remaining choice

Swapping only the D/E reference roles reverses the relative sign:

\[
 S_{DE}VS_{DE}=-V.
\]

It is **not** the diagonal operation G. On the recorded state, combine it with a flip of the report pointer:

\[
 T=S_{DE}\otimes X_M.
\]

The test finds that T preserves the unselected final state and maps its positive branch to its negative branch. Meanwhile

\[
 GZ_MG=Z_M,\qquad TZ_MT=-Z_M.
\]

The two recorded branch states are orthogonal and can be perfectly distinguished by \(Z_M\), which commutes with the enlarged charges and G. Thus they are operationally distinct **within the specified physical observable algebra and joint interface**, even though the unselected state is symmetric under T. This explicitly realizes the distinction between a redundancy that acts identically on the zero sector and a different state symmetry that exchanges two records.

But this is conditional on the admissible observable algebra. If a fuller theory also declares T itself a gauge identification of the same incidence, \(Z_M\) is T-odd and cannot be an absolute gauge-invariant sign; the previous gauge–incidence argument applies again. It would be circular to declare T physical or gauge solely to obtain the desired valence. Even when the records are operationally distinguishable, their identification with *distinct actual subjects*, and their interpretation as opposite felt experiences, are separate questions.

The needed joint interface includes the original record/work/target organization, its reference F, the D/E pair, and M for the full invariant implementation. It is not automatically available to a surface inhabitant, a chess piece, or either of the originally confined labs. A particular physical construction and subject boundary would have to establish access; no extra-domain activity is assumed to be registered.

## 6. The experience and measure test survives the improvement

The gauge-even relative sign narrows the gap but does not settle a psychophysical identity. On the same histories, compare the formal candidate values

\[
 v_1=V,\qquad v_2=\operatorname{sgn}(d_i)V,
\]

where the earlier reference-relative scalar values are \(d=(-1/5,1/2,-7/19)\). Both are invariant under G, odd under the candidate counterpart T, and have zero Born-weighted mean in the checked histories. Yet they disagree on settings of total weight \(3/5\). The verifier checks this on the actual code and noncommuting complement clock states; the source-operator identity transports it through the previous all-label calculation.

These are rival *formal assignments*, not two proven experiences or two demonstrated genuine metaphysical possibilities. In particular, the record of V does not supply Alice's setting \(i\) to a confined observer. If an account requires a local, veridical report of the second sign, its interface and the earlier discrimination limits must be addressed. If it treats experience as intrinsic to the one reality, it must still show which realized organization is a subject and why its felt character is one candidate rather than the other. An unreported feeling is not ruled out by lack of report access.

If a genuine experience law ultimately identifies the two record signs with opposite felt valence and the actual incidence measure pairs them, a zero sum is possible without erasing local suffering. The present physical symmetry, pointer Born weights and energy constraints do not establish any of those premises.

## 7. Consequence for the larger program

This result strengthens the connection between **zero, internal reference, relational differentiation, record dynamics and the distinction between gauge and physical counterparts**. It does so within the existing model and reuses the already prepared reference pair. It also makes the remaining task exact: determine the physically and phenomenally warranted gauge group, subject incidences and felt-sign identity, instead of assuming that every symmetry either creates a new subject or removes one.

It does not derive the reference state, spin representation, Hamiltonian, subject or measure from the proposed self-sufficient zero. It does not establish objective global cosmic energy zero or the necessity of all genuine possibilities. The distinction between exact finite orientation charges and total physical energy remains essential.

## Verification

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
  python -m unittest verification.zero_relative_gauge_invariant_report_test -v
```

The spin-zero, projector and commutator identities are finite matrix checks; the spin-pair argument above explains why the diagonal operation is identity on the declared total-zero sector. All-phase and all-old-label transport follows from the verified source-operator equality and the already verified clock commutators and prior all-label test. Tolerances, source assumptions and the limits of physical interpretation are explicit in the verifier.
