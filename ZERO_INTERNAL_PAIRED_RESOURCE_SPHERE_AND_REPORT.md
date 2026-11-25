# An internal reference pair from the original paired state

## Result

The previously added D/E singlet need not be an independently prepared pair on **every part of the example on which it is used**. In the original two-lab state, there is an explicit 96-dimensional local support on which the actual paired state already factors into:

1. a Bell pair used for the genuinely noncommuting sphere instrument;
2. a **separate singlet** used as the D/E relative-sign reference; and
3. an entangled spectator carrying the remaining representation labels.

Both logical qubits are encoded in multiplicity spaces of the **same original lab systems**. The sphere operations commute with the reference algebra and preserve the singlet, branch by branch. The previous conserving, gauge-even relative-sign circuit therefore applies to this sector without supplying another D/E state. The construction retains the original two-dimensional code and all 158 remaining dimensions; an explicit validity flag distinguishes where the new sign report applies. The original state is not globally replaced by this sector or silently renormalized to it.

This is a real reduction of an independent *state-preparation* assumption, not a derivation of the whole apparatus. The factorization, initial paired lab state, F reference, clock, flag, pointer and nonlocal control interactions are still stipulated. In particular, D is encoded in Alice's lab and E in Bob's: the joint D/E–work–F report is **not automatically accessible to either confined lab**. The tested charges are not identified with objective cosmic energy, and no felt valence or subject follows from a sign record.

The exact calculations are in [`verification/zero_internal_pair_sphere_report_test.py`](verification/zero_internal_pair_sphere_report_test.py), using the existing representation and instrument from [`verification/zero_all_sector_noncommuting_sphere_test.py`](verification/zero_all_sector_noncommuting_sphere_test.py), the report in [`ZERO_CONSERVING_RELATIONAL_CHIRALITY_REPORT.md`](ZERO_CONSERVING_RELATIONAL_CHIRALITY_REPORT.md), and the gauge-even version in [`ZERO_RELATIVE_SIGN_GAUGE_COUNTERPART_CONSTRUCTION.md`](ZERO_RELATIVE_SIGN_GAUGE_COUNTERPART_CONSTRUCTION.md).

## 1. The original state, not a replacement

Each lab has a 256-dimensional four-site Hilbert space. Write \(P_C\) for the original rank-two code, \(C\) for its isometry and \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\). In the same amplitude-matrix convention as the original verifier, the unmodified paired state is

\[
 M=\frac{(CJC^T+I-P_C)^T}{16}.
\]

The inherited construction decomposes the lab representation into irreducibles \((j_a,j_b)\), each with multiplicity \(m\) and irrep dimension \(d=(2j_a+1)(2j_b+1)\). We leave the old code separate. Within each remaining multiplicity we group four equivalent copies into a pair of commuting qubits, with all remaining multiplicity and irrep indices forming a spectator:

\[
 \mathbb C^m\otimes\mathbb C^d\supset
 \mathbb C^2_{\rm sphere}\otimes\mathbb C^2_{\rm ref}
 \otimes\mathbb C^{\lfloor m/4\rfloor d}.
\]

Only three blocks have at least four remaining copies:

| block | multiplicity \(m\) | irrep dimension \(d\) | selected dimension \(4\lfloor m/4\rfloor d\) |
|---|---:|---:|---:|
| \((0,1)\) | 6 | 3 | 12 |
| \((1,0)\) | 6 | 3 | 12 |
| \((1,1)\) | 9 | 9 | 72 |
| all others, after retaining the code | less than 4 each | — | 0 |
| **Total** | | | **96** |

In the existing decomposition, the original state on each selected block is \(P/16\), with the conjugate block on Bob's side. Choose the explicit Alice isometry \(F\) by taking these four-copy groups in the inherited basis; choose Bob's isometry

\[
 B=\overline F\,(I_2\otimes J^T\otimes I_t),
 \qquad t=\lfloor m/4\rfloor d.
\]

The verifier calculates the actual amplitude in these coordinates, including complex conjugation:

\[
 F^\dagger (P/16)\,\overline B
 =\frac{I_2\otimes J^T\otimes I_t}{16}
 =\sqrt{\frac{4t}{256}}\left(
 \frac{I_2}{\sqrt2}\otimes\frac{J^T}{\sqrt2}
 \otimes\frac{I_t}{\sqrt t}\right).
\]

Thus the **normalized** selected-block state is exactly \(|\Phi_2\rangle_{\rm sphere}\otimes|\mathrm{singlet}\rangle_{DE}\otimes|\Phi_t\rangle\), in the stated local coordinates. This is an identity of amplitudes of the original state, not merely a matching of marginal statistics. Choosing the isometries is a choice of physical subsystem algebra; it is not derived from zero or from a preferred spatial geometry.

The 96-dimensional capacity is maximal **within this particular demand**: two full qubit matrix algebras must act on charge-commuting multiplicities while the old energy-split code stays separate. Schur's lemma forces each irreducible block's multiplicity support to be a multiple of four. This is not a bound on arbitrary POVMs, approximate references, other encodings, joint/nonlocal operations, or a different model.

## 2. A noncommuting sphere and an undisturbed reference

On the selected blocks, let Alice's sphere Kraus operators be the inherited \(K_i\otimes I_D\otimes I_t\), and Bob's be the corresponding inherited \(B_j\otimes I_E\otimes I_t\), lifted with their respective isometries. The verifier checks:

- completeness on each selected support, and a nonzero commutator of Alice's two physical sphere effects;
- commutation of every lifted sphere and reference operator with all original local charges and both previously declared lab Hamiltonians;
- commuting sphere/reference operators and exact Pauli commutators for each encoded reference;
- the **entire physical post-instrument amplitude** for each of the six \((i,j)\) outcomes, including the spectator and Bob's conjugation; and
- \((D_k+E_k)|\psi_{ij}\rangle=0\) for all three reference components and each outcome.

The result is stronger than obtaining the right table: the sphere readout genuinely acts on one factor while the other pair remains exactly singlet in every branch. All physical lab operations in this construction preserve the original local charges, and the encoding preserves the declared lab energy operators. This does not establish the full energy cost of the control and pointers.

The separation is not cosmetic. If the same reference qubit is subjected to one of the inherited rank-one Alice sphere Kraus operators, the pair becomes rank one and its conditional fidelity with the original singlet is \(1/2\). More generally, a purely local isometry with initially independent apparatus that leaves a full-Schmidt-rank singlet exactly unchanged must leave the apparatus in an input-independent state: comparison of Schmidt coefficients gives \(W|0\rangle=|0\rangle|\eta\rangle\) and \(W|1\rangle=|1\rangle|\eta\rangle\). Its POVM effects are therefore scalar. This is a precise no-information-without-disturbance statement under those assumptions, not a ban on feedback, nonlocal operations, or approximate/disturbed references.

## 3. Relative sign, conservation and the joint interface

For each selected block the previous report's source is the old record–work–target and F state tensored with this **already present** D/E singlet. The verifier transports the actual sphere output into the previous full 64-dimensional report calculation at every one of the 16 old relative-clock labels. It checks the source condition, the \(V^2=1\) relation, both sign branches, their enlarged orientation-zero constraint and old balance, and the diagonal-swap invariance. The previous verifier establishes the complete relative-projector gate, its commutators with the old clock generators, and equality with the earlier report on the source. Consequently the transport includes arbitrary later clock phases under that same specified dynamics.

The total orientation constraint is the earlier

\[
 \mathcal C_k=C_k+D_k+E_k,
\]

not a claim that the original \(C_k\) remains zero separately after reporting. The original *lab* charges also remain conserved: the lifted D and E and the sphere operations commute with them, so a report operator assembled from these logical reference operators and the old external interface does as well. The old F reference and the original active record–work–target organization are still inputs. A control that couples that interface to encoded D in one lab and E in the other is an additional joint operation; no device, locality, accessibility, autonomous implementation, or energy ledger is derived here.

On the selected sector only, the same gauge distinction survives: diagonal exchange \(G\) is identity on the enlarged orientation-zero space, \(V\) is G-even, and D/E exchange reverses \(V\). The required exchanges are logical joint operations in the chosen encoding, not evidence that confined inhabitants can perform or observe them. Whether a larger physical gauge group identifies the sign-exchanging operation remains open.

## 4. Whole-state accounting and the price paid

The selected sector carries Born weight \(96/256=3/8\) in the original state. The old code has weight \(2/256\); the other complement has weight \(158/256\). The verifier proves the three orthogonal amplitude pieces add back to the original \(M\), and their local projectors commute with the old lab charges and declared lab Hamiltonians. On the given paired state, Alice and Bob's corresponding sector projectors agree exactly.

A **coherent**, neutral validity flag can be controlled by the selected projector: flag 1 means that the internal reference and sign circuit are applicable; flag 0 contains both code and remaining complement. The two flagged amplitudes have weights \(3/8\) and \(5/8\) and add back to the input when the flag is erased. This is an isometric flag construction, not deterministic extraction of an exact D/E pair from the whole state. Reading flag 1 and renormalizing would be postselection; the whole-state version retains flag 0 and does not assign it a fabricated ± sign. Flag implementation and its control are stipulated.

For example, using the earlier normalized clock history, a clock window containing \(k\) of its 16 labels has probability \(k/16\). With the validity flag, the tested construction gives

\[
 P(\mathrm{valid},i,V=\pm1,\mathrm{window})
 =\frac{k}{16}\,\frac38\,\frac{q_i}{2},\quad
 q=(1/8,2/5,19/40).
\]

For the three-label window, the total valid weight is \(9/128\), with \(9/256\) in each sign. These probabilities refer to the specified circuit and Born rule; they are not an established measure of actual subject incidences. The verifier also checks the inherited \(i\) marginal and old record statistics when code and inactive complement use their existing and state-independent neutral instruments respectively. Those old record statistics are **not** the new sign report on invalid sectors.

There is a significant tradeoff: the earlier separate-reference construction could apply its genuine qubit sphere instrument on 190 complement dimensions (or the higher-spin construction on 229), because the D/E pair was separately supplied. This exact two-qubit multiplicity encoding retains the genuinely noncommuting sphere instrument together with the internal singlet on **96** dimensions, not the original 190. It uses a different multiplicity pairing and does not prove the old 190-dimensional physical instrument is unchanged. The remaining dimensions are retained, but the present all-sector table uses neutral, state-independent operations on that remainder, not a genuine noncommuting sphere there. Improving this coverage or proving a broader bound is a substantive next question.

## 5. Significance and limits

The constructive link is now sharper: part of the same balanced paired state can internally support two commuting relational structures, one for sphere differentiation and one for a conserved relative-sign report. A paired relation need not be imported as a completely separate state for that sector. It also illustrates why resource accounting matters: preserving both structures exactly costs representation multiplicity and requires a joint interface.

Nothing here shows that zero uniquely determines this state, encoding, dynamics, sphere, probability measure, or subject constitution. A mathematical singlet and opposite gauge-even pointer values are not themselves positive and negative felt experience; they do not erase suffering or establish cancellation of phenomenal valence. Nor does the finite-model orientation balance demonstrate whole-universe energy zero. Those are the framework's live constructive requirements, not consequences smuggled into the calculation.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
  python -m unittest verification.zero_internal_pair_sphere_report_test -v
```

The tests use finite-dimensional numerical matrix identities; the block capacity and local no-disturbance arguments state their assumptions explicitly. The pointer, flag, control and interface remain stipulated, and all probability claims are conditional on the modeled preparation and measurement rules.
