# Sourcing F internally—and tracking the orientation it displaces

**Subsequent upstream construction:** [An invariant upstream source for the differentiated history](ZERO_UPSTREAM_INVARIANT_ENCODED_HISTORY.md) changes the preparation: H is the logical A from the outset, rather than the recipient of a swap from a separately prepared A. It reproduces the old reference-extended history while retaining a specified all-sector orientation zero; the different encoding and its assumptions are explicit.

## Result

The original paired lab state can supply not only the sphere pair and the D/E sign reference but also the previously added F reference, on a **72-dimensional sector**. An explicit swap between the old record–work–target orientation qubit and F's original partner produces exactly the earlier F-extended source, including its phases and its correlations with the rest of the old history. The original 190-dimensional complement sphere instrument is unchanged before this new operation.

There is an important price. The swap transfers the old orientation to the partner, called H. It conserves the **enlarged** orientation algebra, but the resulting full orientation is not zero: the old F-extended subsystem is zero while H carries the missing spin. The same is true in each subsequent relative-sign report branch. The 72-dimensional sector is not the whole state, and the construction does **not** derive the initial state, controls, interface or total cosmic energy.

This is both a resource reduction and a precise obstruction to an attractive but incorrect conclusion: **obtaining a zero subsystem by transferring its charge to an uncounted partner does not establish a zero whole**. It identifies the exact upstream issue rather than treating the partner as acceptable residue. The proposed zero-whole remains a substantive demand; this finite example neither derives it nor proves that no other constitution can satisfy it.

Verifier: [`verification/zero_internal_f_reference_transfer_test.py`](verification/zero_internal_f_reference_transfer_test.py). The calculation imports the actual source isometry from [`verification/zero_relational_orientation_reference_test.py`](verification/zero_relational_orientation_reference_test.py), the relative-sign circuit from [`verification/zero_relative_gauge_invariant_report_test.py`](verification/zero_relative_gauge_invariant_report_test.py), and the physical sphere encoding from [`ZERO_NESTED_SPHERE_REFERENCE_COVERAGE_FRONTIER.md`](ZERO_NESTED_SPHERE_REFERENCE_COVERAGE_FRONTIER.md).

## 1. Three pairs already inside one part of the original state

In the \((1,1)\) charge block the original lab representation contains nine equivalent copies, each of dimension nine. Use the first eight copies as

\[
 \mathbb C^2_S\otimes\mathbb C^2_D\otimes\mathbb C^2_H\otimes\mathbb C^9_{\rm irrep}
\]

on Alice and corresponding \(S',E,F\) factors on Bob. Order the old copy labels as \(p_{4h+2r+s}\), with sphere \(s\), D/E index \(r\), and H/F index \(h\). Thus the old adjacent-copy sphere pairing is preserved. With the corresponding Bob basis rotation \(I\otimes J^T\otimes X\otimes I_9\), the actual amplitude of the original 256-by-256 paired state on this block is

\[
 \frac{I_2\otimes J^T\otimes X\otimes I_9}{16}
 =\sqrt{\frac{72}{256}}\,
 \left(\frac{I_2}{\sqrt2}\right)_{{SS'}}
 \otimes\left(\frac{J^T}{\sqrt2}\right)_{DE}
 \otimes\left(\frac{X}{\sqrt2}\right)_{HF}
 \otimes\left(\frac{I_9}{3}\right)_{\rm spectator}.
\]

The lab spectator is an entangled pair of nine-dimensional irrep spaces; it is not discarded or identified with a subject. In the reference convention used below, the \(X/\sqrt2\) pair is an orientation singlet of H and F. All three pairs are factors of the **original** state on the selected sector, not separately prepared replacements.

The verifier checks the actual physical sphere Kraus matrices restricted to this sector against the earlier 190-dimensional instrument, their full six post-instrument amplitudes, both reference-pair zero relations and the lab-charge and declared lab-energy commutators. The new reference algebras commute with the sphere operators. All the unselected original sectors remain present; the selected sector has weight \(72/256=9/32\), and the rest has weight \(184/256\). A validity flag and the conditional control are still apparatus inputs.

## 2. An exact swap replaces the added F isometry

The old record–work–target system has an encoded orientation Pauli triple

\[
 A=(U_8,U_1,J_W),
\]

and the old F convention is \(B_F=(-X_F,-Y_F,Z_F)\). Give the already encoded H factor the same spin convention as A. The internally present F/H pair is

\[
 |\Psi^+\rangle_{FH}=(|01\rangle+|10\rangle)/\sqrt2,
 \qquad (B_{F,i}+\sigma^H_i)|\Psi^+\rangle=0.
\]

On the 32-dimensional active RWT–F–H space define

\[
 W_{AH}=\tfrac12\bigl(I+\sum_i A_i\sigma^H_i\bigr).
\]

This is the swap of the A and H spin algebras. The verifier checks unitarity, the swaps of all three Pauli operators, and

\[
 [W_{AH},\ K_i]=0,\qquad K_i=A_i+B_{F,i}+\sigma^H_i.
\]

A time-independent generator for this gate on its active support is \(H_{AH}=\frac\pi2(I-W_{AH})\), for which \(e^{-iH_{AH}}=W_{AH}\). The full old work-space extensions of A commute with the previously declared total and pair-number work operators; H commutes with the lab charges and declared lab energies. Thus the conditional swap has the corresponding finite-model commutators, including an identity extension outside the selected lab/active-work support. This does not supply an autonomous switch, spacetime-local implementation or complete control-energy ledger.

For the *actual* earlier history \(|v\rangle\), including all environment and pointer amplitudes and for each of its 16 old relative-clock labels, the old orientation satisfies

\[
 A_x|v\rangle=|v\rangle.
\]

If \(V_F\) denotes the earlier `with_reference` isometry, direct complex-amplitude calculation gives

\[
 W_{AH}\bigl(|v\rangle\otimes|\Psi^+\rangle_{FH}\bigr)
 =V_F|v\rangle\otimes|+x\rangle_H.
\]

This is not merely equality of local marginals or sign probabilities. It is equality of the full old source vector, now realized with the internally encoded F, and with the previously unaccounted partner H explicitly retained. It applies to the given old source histories; it is not claimed for an arbitrary input with a different A orientation.

## 3. What the swap conserves—and what it does not

The original F-extended orientation constraint is \(C_i=A_i+B_{F,i}\). Before the swap the F/H singlet is independent of the old history. The actual normalized source satisfies

\[
 \langle C_1^2+C_2^2+C_3^2\rangle=6,
 \qquad \langle C_3^2\rangle=2.
\]

After the swap, every \(C_i\) annihilates the old F-extended source, exactly as in the earlier construction. This does **not** violate conservation: \(W_{AH}\) does not commute with \(C_i\) alone. It commutes with \(K_i=C_i+\sigma_i^H\), and the actual state satisfies before and after

\[
 \langle K^2\rangle=3,\qquad \langle K_x\rangle=1.
\]

After the swap \(C_i=0\) and H is explicitly \(|+x\rangle\), so the entire conserved orientation is in H. These are Pauli-normalized orientation charges defined for the chosen encoding; they are not the old physical lab directional charges or objective cosmic energy. There is no justification for silently leaving H out of a claim about the whole enlarged orientation system.

The preparation also changes the original old history. For each normalized old-clock conditional vector, tracing F from \(V_F|v\rangle\) gives a state with fidelity \(1/2\) and trace distance \(1/2\) from \(|v\rangle\langle v|\). In fact it is an equal mixture of the original history and an orthogonal history. The old RWT orientation reduced state changes from \(|+x\rangle\langle+x|\) to \(I/2\). Thus the construction preserves the pre-transfer sphere instrument and yields the old **reference-extended** target state, but it does not leave the old unextended history unchanged.

## 4. The gauge-even sign survives, but the full balance does not

The already present D/E singlet is untouched by the swap. Attach it to the transferred source and use the earlier relative-sign operator \(V\) and projectors \(Q_\pm\). For every old clock label the verifier checks:

- the complete old report input and both projected branch amplitudes, including the retained H factor;
- the earlier \(A+B_F+D+E=0\) constraint, old balance and diagonal-swap invariance in each sign branch;
- the old report table \(P(i,V=\pm1)=q_i/2\) conditional on a normalized valid sector and clock label; and
- conservation of the enlarged orientation, with \((A+B_F+D+E+H)^2=3\) on each normalized branch, not zero.

The old report projectors commute with the subsystem charge and act trivially on H; the old clock-generator commutators therefore transfer to the enlarged charge when H is retained. On the original input, each sign has whole-state weight \(9/64\), before clock conditioning, within the validity sector. A \(k\)-label window multiplies it by \(k/16\); no ± report is claimed on the other \(184/256\) weight. The construction still requires the joint D/E–F–work interface and a report pointer; it does not endow either confined lab with access to the full relation.

The two previously identified formal assignments, \(V\) and \(\operatorname{sgn}(d_i)V\), still both have zero modeled Born mean but disagree on settings of total weight \(3/5\). Supplying F internally therefore does **not** select a felt sign. Neither assignment has been shown to be experience, and Born weights are not automatically subject-incidence weights.

## 5. The no-go is broader than a missing gate

Two separate facts isolate the issue.

**For the five explicitly transforming spin halves** \(A,F,H,D,E\), every total-spin representation is half-integer. The verifier computes the full five-spin Casimir and confirms its minimum is 3 in Pauli normalization: there is no simultaneous zero of all three total components, for **any** state of those five spins. Spectator multiplicities do not change this parity. An additional half-integer transforming factor, a different representation, or a different constraint could change the situation; this is not a theorem about all of reality.

**More generally, the original history itself is not a global SU(2) singlet under a factorized orientation action that includes A.** Its A marginal is the pure \(|+x\rangle\) state. If a joint state were invariant under every common rotation \(u_A\otimes U_{\rm rest}\), its reduced A state would commute with every spin-half rotation and hence be \(I/2\). The actual pure marginal rules that out, irrespective of how many other systems are appended without changing the old history. A unitary commuting with the complete chosen total charge cannot turn a nonzero-Casimir input into a zero-Casimir output.

This does **not** prohibit a different upstream, jointly balanced preparation that changes the old A state, nor a different physical action or charge algebra. It does mean that adding further uncorrelated references after this particular old history cannot make that history already globally invariant. The earlier [upstream preparation](ZERO_BALANCED_REFERENCE_PREPARATION_TOPOLOGICAL_PROGRAM.md) addressed a specific orientation component by starting from a different balanced seed; it is not itself a demonstrated all-components global singlet for this enlarged five-spin system.

## 6. Consequence for the larger project

The next constructive target is now sharper than “find another reference”: start from a **whole** input invariant under the desired complete orientation algebra, and derive the old differentiated sphere/report relations as internal correlations without first inserting a pure oriented A and later hiding its compensator. A successful candidate must retain all partners and controls, explain how the sphere instrument is implemented without breaking the proposed total constraint, and compare its actual outputs—not merely relabel the current nonzero \(K^2\) as zero.

At the same time, invariant physical records do not by themselves explain intrinsic experience or negative felt valence. A bridge must determine a subject's constitution and the signed experiential quantity, and why the relevant actual incidences and measure pair, rather than simply naming pointer outcomes. Nor has this finite orientation accounting supplied the objective whole-energy ledger, the origin of the algebra, necessary plenitude, or a fully self-sufficient constitution. Those are constraints on the next construction, not dispensable leftovers.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
  python -m unittest verification.zero_internal_f_reference_transfer_test -v
```

The sector factorization, physical Kraus and charge commutators, swap, all 16 source vectors, report branches, retained H charge, competing sign tables and five-spin spectrum are checked numerically. The general reduced-state invariance argument states explicitly what additional assumptions are needed.
