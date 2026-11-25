# Extending the balanced orientation and opening a report boundary

## Result

The previous [upstream construction](ZERO_UPSTREAM_INVARIANT_ENCODED_HISTORY.md) made its new orientation generators vanish outside the 72-dimensional sign-report sector. That was a chosen representation, not a requirement of the original paired state. Here the same original lab state and the same physical 190-dimensional complement sphere instrument support a **nontrivial orientation representation on additional sectors**, with exact whole-state orientation zero and branchwise zero after the sphere readout.

Counting actual nontrivial local representations rather than just the blocks in which operators were written gives a more precise result:

| construction | dimensions with nontrivial local orientation | keeps the old sign-report gate? |
|---|---:|---|
| Previous 72-dimensional report sector | **54** | yes |
| Extended orientation constructed here | **90** | yes |
| Alternative maximum-coverage orientation | **108** | not with the old neutral-pointer sign gate |

The earlier sector has 72 dimensions, but its local orientation representation is \(0\oplus1\): 18 dimensions carry the trivial spin-zero representation and 54 carry spin one. The new construction adds a spin-one representation on each of two 18-dimensional sectors. The alternative uses spin three-halves on the original 72-dimensional sector and spin one on the additional 36 dimensions; the old sign gate then violates the alternative orientation conservation even on the original source.

These are **conditional exact bounds** for the specified local charge commutant, old sphere instrument, retained separate code, and—in the 90-dimensional case—the old full-space report gate. They do not show that nature's orientation or energy takes this form. The remaining dimensions have a trivial representation of this particular additional charge, not no physical structure, no experience, or no relevance to the whole.

The same model also admits an explicit neutral interaction that gradually opens a **report interface** while leaving the sign probabilities and total orientation unchanged. It illustrates a dynamically varying distinction in what a specified interface can infer; it does not establish subjecthood or identify any report with felt experience.

Verifier: [`verification/zero_orientation_extension_operational_boundary_test.py`](verification/zero_orientation_extension_operational_boundary_test.py). It imports the actual decomposition, old instrument and sign history, rather than replacing them with an unrelated abstract example.

## 1. The orientation is available in the old sphere commutant

On each charge irrep of dimension \(d\), the old sphere instrument pairs adjacent equivalent copies. If \(m\) copies are available, its exact-qubit part has

\[
 \mathbb C^2_{\rm sphere}\otimes\mathbb C^r_{\rm spectator}
 \otimes\mathbb C^d_{\rm irrep},\qquad r=\lfloor m/2\rfloor.
\]

The old noncommuting sphere Kraus operators act on the first factor. Any spin algebra on the spectator factor commutes with that instrument as well as the original lab charges. The test uses the actual physical 256-dimensional matrices and the same Alice/Bob conjugation convention as before.

In the \((0,1)\) and \((1,0)\) blocks, \(m=6\), \(d=3\), so each has a three-dimensional spectator. Put a Pauli-normalized spin-one triple \(2J_i^{(1)}\) there. Each block now contributes \(2\cdot3\cdot3=18\) genuinely nontrivial dimensions. On the original \((1,1)\) report sector keep the existing local \(A_i+D_i\) triple **unchanged**. On Bob take the contragredient matrices \(-\overline{A_i}\); on the report sector these are exactly the existing \(B_i+E_i\).

The resulting physical generators satisfy

\[
 [G_i,G_j]=2i\epsilon_{ijk}G_k,\qquad
 G_i^{A}M+M(G_i^{B})^T=0,
\]

for the **full original paired amplitude** \(M\). They commute with the original lab charges, the declared lab Hamiltonians and all physical sphere Kraus operators. The verifier checks the same orientation zero after each of the six joint sphere-outcome branches. The full instrument keeps the old 190-dimensional exact sphere instrument; it uses neutral scalar effects on the remaining 66 dimensions, including the old code.

The local Casimir \(\sum_iG_i^2\) has eigenvalue 8 on 90 dimensions and 0 on 166. Of those 90, the earlier report block contributes 54 and the two added blocks contribute 18 each. **The existing 72-dimensional sign-report source, its preparation, its relative-clock histories and its sign gate are unchanged**: on that block the new generators equal the old ones. Therefore its two sign branches remain conserved and gauge-even by the earlier operator identities. No sign report has been constructed for the newly charged 36 dimensions.

## 2. Why 108 is the unrestricted maximum in this class

For the old sphere instrument the two noncommuting qubit effects generate the full \(M_2\) algebra on the sphere factor. A lab-only orientation commuting with both the original charge algebra and the instrument can therefore act only on its multiplicity spectator. On a spectator of dimension one it is scalar and cannot carry a nontrivial SU(2) representation. On dimension \(r\geq2\), one can choose an irreducible spin \((r-1)/2\) acting nontrivially on all \(r\) dimensions.

Only three paired blocks have \(r\geq2\):

| block | \(m\) | \(d\) | \(r\) | maximum nontrivial local dimension |
|---|---:|---:|---:|---:|
| \((0,1)\) | 6 | 3 | 3 | 18 |
| \((1,0)\) | 6 | 3 | 3 | 18 |
| \((1,1)\) | 9 | 9 | 4 | 72 |
| all other paired blocks | 2 or 3 | varies | 1 | 0 |
| **Total** | | | | **108** |

The unpaired one-copy irreps have only scalar charge-commuting operations. The retained code's two states have different declared lab energies, so energy-commuting operations cannot put a nontrivial spin representation across them. Requiring the code separate also prevents it being mixed with the other copies of the same irrep. Inequivalent charge irreps cannot be mixed by a local charge-commuting generator. The full noncommuting sphere algebra likewise prevents mixing its two-dimensional irreducible factor with the scalar instrument's one-dimensional factors.

The verifier attains the bound: use spin one in both \(r=3\) blocks and **spin three-halves** in the \(r=4\) block. The Casimir has eigenvalues 8 on 36 dimensions, 15 on 72, and 0 on 148. The original full state and every tested sphere branch remain exactly zero for the paired total orientation, with the old lab charges and energies still respected. This is an alternative orientation algebra; it is not the previous report's four-spin algebra.

This upper bound does **not** cover charged apparatus, changes to the sphere instrument or code, nonlocal generators, approximate symmetry, a different lab representation, or non-SU(2) charges. It is not a statement about the maximal differentiation of the universe.

## 3. Why preserving the old sign report caps this construction at 90

The tension between 90 and 108 is not merely that one convenient spin-three-halves basis happened not to work. In the four-dimensional multiplicity spectator of the old 72-dimensional report sector, choose a canonical Bob basis in which the actual A/F–D/E source is \(|\Phi_4\rangle\). Any paired total generator preserving this source has the form

\[
 K(X)=X\otimes I-I\otimes X^T.
\]

The old negative-sign projector is rank one on the four-spin factors. Write its normalized vector as \(|Z\rangle\!\rangle\), where \(Z\) is a \(4\times4\) matrix in these canonical bases. The verifier checks that \(Z\) is normal, has nonzero trace, and has eigenspace multiplicities **three and one**. If a Hermitian \(X\) preserves the full sign projector, then \(K(X)|Z\rangle\!\rangle=\lambda|Z\rangle\!\rangle\), equivalently

\[
 [X,Z]=\lambda Z.
\]

The trace gives \(\lambda\operatorname{tr}Z=0\), hence \(\lambda=0\). Thus X preserves the one-dimensional eigenspace of Z. An SU(2) algebra has only the trivial representation on that line, leaving at most the other three spectator dimensions nontrivial. With the two-dimensional sphere and nine-dimensional irrep, the report sector therefore contributes at most \(2\cdot3\cdot9=54\), and the two \(r=3\) blocks add at most 36. The 90-dimensional construction attains the resulting bound.

This argument requires the **actual full-space sign projector** to be conserved by a neutral-pointer gate and the original maximally paired source to be invariant under the chosen paired generators. It is not a no-go for a charged pointer, a modified sign observable, a weaker source-only requirement, or a different instrument. The test additionally finds a four-dimensional complex symmetry space for the full \(V\) operator itself (identity plus the old spin generators), while the negative-projector symmetry space is larger, dimension ten. Thus the bound does not depend on incorrectly assuming that conserving the projector and conserving every eigenvalue of V are the same condition.

For the explicit spin-three-halves alternative, each sign branch has probability \(1/2\) on the original selected source, but its normalized total-orientation Casimir is \(44/3\), rather than zero. So that particular gate fails not only as an operator identity: its actual reported branches fail the alternative charge constraint. This does not exclude paying the difference with a properly included charged apparatus.

## 4. A changing operational boundary, without assuming a subject

The existing invariant sign circuit has a neutral sign pointer M and an earlier sphere-outcome record \(i\). On its valid history, for every checked old clock label,

\[
 P(i,s)=q_i/2,\quad s=\pm1,\quad
 q=(1/8,2/5,19/40).
\]

Two previously compared **formal** signed assignments are

\[
 h_1=s,\qquad h_2=\operatorname{sgn}(d_i)s,
 \quad d=(-1/5,1/2,-7/19).
\]

They disagree on \(3/5\) of this modeled weight, while each has zero Born mean. Consider two explicitly stipulated classical readout algebras, not an assumed subject:

- **M only:** \(h_1\) is read perfectly; the best inference of \(h_2\) succeeds with probability \(3/5\), because the sign of \(d_i\) is not available in this interface.
- **M plus Alice's record \(i\):** both values can be determined perfectly. By contrast, \(i\) alone has no information about either sign in this particular table.

For \(h_2\), M alone carries \(1-H_2(3/5)\simeq0.0290\) bits of mutual information; M plus i carries one bit. The difference concerns these *specified record algebras*. It is not a bound on all other possible local quantum measurements, and adding Alice's record requires a real interface—not an assumption that a confined observer automatically has it. The M pointer and i record are even under the earlier diagonal G transformation, but whether a larger gauge identification is warranted remains open.

We can make the boundary dynamical without changing its interpretation. Prepare a separate neutral reader R in \(|0\rangle\), and after the sign has been recorded apply

\[
 U_\theta=\exp[-i\theta\,|1\rangle\!\langle1|_M\otimes Y_R].
\]

This commutes with the specified orientation charges, the old sign pointer \(Z_M\), and the diagonal G action. It leaves the \(i,s\) distribution intact, although ignoring R can decohere correlations between the sign branches. For \(0\leq\theta\leq\pi/2\), the optimal single-copy reader-only discrimination probabilities are

\[
 P_{\rm guess}(h_1\mid R)=\frac{1+\sin\theta}{2},\quad
 P_{\rm guess}(h_2\mid R)=\frac{1+\tfrac15\sin\theta}{2}.
\]

If i is also available, the optimal reader-based inference of \(h_2\) equals that of \(h_1\). The verifier derives these from the actual sign distribution and the trace distance of the reader's two quantum states. At \(\theta=0\) the reader has no sign information; at \(\pi/2\) it reads M exactly. The pointer, reader, control and access path are stipulated and their complete energy cost is not established. The coupling parameter can be considered relative to the earlier clock, but no preferred fundamental time is posited.

## 5. Connection to the meditation evidence—and its limits

This provides a specific **structural analogy**, not a neuroscience derivation: an underlying invariant history can remain the same in its modeled sign distribution while the interface's access to relations changes. That is a more discriminating target than calling two equal timescales “unity.” It also illustrates why an operational report boundary and a phenomenal boundary cannot simply be identified: \(h_1\) and \(h_2\) are equally balanced formal candidates, yet their recoverability differs with the available record.

The [Saketh et al. analysis](NONDUAL_MEDITATION_NEURAL_TIMESCALES_AND_ONE_REALITY.md) concerns human EEG and self-reports, not this finite circuit. A possible empirical successor would test whether **preregistered, within-person relational-access measures** predict reported self–world boundary changes beyond neural timescale summaries and attention/arousal controls. The model does not currently specify a validated mapping from EEG features to M, i, R or \(\theta\); without such a mapping it makes no quantitative prediction for that paper. Equal probability, a changing interface and a gauge-even pointer do not establish experience, determine felt valence, or make local suffering disappear.

The broader task remains to derive the charge representation, selected measurement, clock, access conditions and experiential law together from the proposed self-sufficient constitution, rather than declaring a chosen representation necessary. The original lab-charge balance and the new orientation zero are not established to be objective global cosmic energy. The 166 local dimensions that are orientation-trivial in the sign-preserving representation are retained in the whole state; their designation is not a resolution of their structural or experiential status.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
  python -m unittest verification.zero_orientation_extension_operational_boundary_test -v
```

The code checks physical matrices, total-zero source and measurement branches, Casimir ranks, the actual sign-projector symmetry calculation and the neutral-reader Helstrom probabilities. Representation-theoretic maximality is conditional on the assumptions above; its numerical singular-value and spectrum checks are not an ontology proof.
