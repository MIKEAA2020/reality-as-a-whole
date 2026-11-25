# A conserved sphere sign at maximal orientation

## Result: the trade-off can be bypassed, but not by recovering the old sign

The [previous result](ZERO_ORIENTATION_EXTENSION_AND_DYNAMIC_REPORT_BOUNDARY.md) left a precise question: does increasing the additional orientation's nontrivial support from 90 to **108 local dimensions**, while retaining the original paired source and sphere instrument, rule out *any* conserved binary sign report? **No.** The old chirality gate fails for the 108-dimensional orientation, but another gate, acting on the existing sphere factor rather than on the orientation spectator, works exactly.

The construction uses the actual 256-by-256 paired source, old six sphere branches, old local lab charges and Hamiltonians, and the alternative 108-dimensional orientation. It adds a neutral two-state pointer and a later, explicitly chosen sphere readout. The sign is available on **all 190 dimensions of the old exact-qubit sphere complement**, whose weight in the original source is **190/256 = 95/128**. The other **66/256 = 33/128** are retained as an explicit *no-sign* sector, not discarded from the whole. On every joint old sphere branch, each of the two new signs carries half of that branch's exact-qubit weight, and the paired total orientation remains zero in each reported branch.

This is a relative **sphere handedness readout**, not the old four-spin chirality, and not a unique experiential sign. Its transverse axis uses the existing measurement directions *and* the already chosen identification between the labs' sphere conventions. Its pointer and timing are stipulated. The sign is genuinely accessible through a concrete interaction, but which sign is identified as positive, which observable is read, and whether any such label has a felt meaning are not fixed by zero total orientation.

Executable verifier: [`verification/zero_conserving_sphere_handedness_report_test.py`](verification/zero_conserving_sphere_handedness_report_test.py).

## 1. Why a neutral pointer cannot split the spin-three-halves singlet alone

On the 72-dimensional block, the original paired four-dimensional spectator is the normalized maximally paired state \(|\Phi_4\rangle\). With the alternative spin-three-halves generators \(X_i=2J_i\), its total generators are

\[
 K_i=X_i\otimes I-I\otimes X_i^T.
\]

The verifier obtains total Casimir eigenvalues \(0,8,24,48\), with multiplicities \(1,3,5,7\); \(|\Phi_4\rangle\) spans the unique zero sector. This yields a useful exact statement, without overstating it:

> If a unitary commutes with every \(K_i\), starts with this unique spectator singlet, and acts on it and an orientation-neutral pointer alone, its output remains \(|\Phi_4\rangle\) tensor a pointer state. Resolving the pointer cannot yield two distinct nonzero spectator states. Equivalently, a conserved spectator-only projective observable is scalar on that singlet.

The proof is simply that the invariant subspace of spectator plus trivial-representation pointer is the one-dimensional singlet tensored with the pointer space. A pointer can still be flipped or randomized independently; that is not a distinct spectator sign. **The conclusion changes** if the pointer/reference carries orientation charge, if different total-charge sectors are admitted, or if other neutral multiplicity degrees of freedom are available. The last possibility is exactly how the following construction works. This is not a theorem that invariant reporting in the whole model is impossible.

The old diagonal swap \(G=S_{AF}S_{DE}\), written in the canonical spectator basis, is the identity on the unique singlet, but its commutator with the alternative total generators is nonzero away from it. Thus it is not automatically a global symmetry of the new orientation. Our comparison below uses its previously specified action on the old report sector; it does not promote that action to a universal gauge law.

## 2. The actual readout

On the 190-dimensional exact-qubit part the old physical instrument factors into a sphere qubit and a spectator/irrep factor. The new orientation acts only on the latter. Put the existing Bob sphere measurement in its actual logical convention as

\[
 B=\mathbf b\cdot\boldsymbol\sigma,\qquad
 \mathbf b=(1/5,2\sqrt3/5,-2\sqrt3/5).
\]

The old first Alice effect, transformed using the already stipulated sphere convention \(J\), supplies the unit direction \(\mathbf u=(-1,0,0)\). They are nonparallel. Define the ordered transverse direction and the new observable by

\[
 \mathbf c={\mathbf b\times\mathbf u\over|\mathbf b\times\mathbf u|}
 =(0,1/\sqrt2,1/\sqrt2),\qquad
 V=\mathbf c\cdot\boldsymbol\sigma.
\]

Hence \(V^2=I\) and \(BV+VB=0\). Both direction vectors come from the already specified effects; the ordering, orientation convention, identification by \(J\), and decision to measure this cross-product observable remain substantive choices. A simultaneous proper rotation of the sphere coordinates rotates all three vectors together; a reversal of the ordered pair flips the sign. This covariance does not establish invariance under every possible physical or gauge transformation, especially an orientation-reversing one.

Let \(P\) be the physical projector onto the 190-dimensional exact-qubit part on Bob's side, and let \(\widetilde V\) be the actual lifted \(V\), zero on the 66-dimensional remainder. Define

\[
 P_\pm=(P\pm\widetilde V)/2,\qquad
 U=(I-P_-)\otimes I_M+P_-\otimes X_M.
\]

For a pointer initialized in \(|0\rangle_M\), this writes plus as 0 and minus as 1 *on the valid sector*. It acts trivially on the remainder: pointer 0 there is **not** a plus sign. A valid report must also use the conserved sector flag \(P\); reading only M would conflate plus with no-sign. Because \(P_-\) is a projector, this is a unitary, generated for example by \(H_{\rm gate}=(\pi/2)P_-\otimes(I-X_M)\) over unit parameter time. This supplies a mathematical gate and conserved control Hamiltonian, not a complete autonomous device or a derivation of a physical clock.

The verifier constructs the physical 256-dimensional lifts, checks the projectors and gate algebra, and checks their commutators with the declared local lab charges, both lab Hamiltonians, and each alternative orientation generator. The pointer is assumed neutral under those charges, including its own degenerate/free Hamiltonian for this gate. The original instrument runs **first and unchanged**. The new readout is generally incompatible with repeating Bob's old sphere measurement: conditional on a definite old Bob outcome and either new sign, a fresh old Bob measurement gives either outcome with probability 1/2. Thus conservation does not mean nondisturbance.

## 3. Exact source, records, and the origin of the bit

After Bob's old outcome \(j=0,1\), the Bob sphere state has eigenvalue \((-1)^j\) of \(B\). Since \(V\) anticommutes with \(B\), both new signs have probability 1/2 for **every** Alice/Bob outcome pair, not just after averaging. The physical branch computation checks each separately against all three 108-dimensional total orientation constraints, the old pairwise lab-charge constraints, and the declared sum of lab energies. The complement and no-sign remainder keep their original joint sphere-outcome weights when the pointer is ignored.

The compressed actual old record–work–target history gives, for each of the 16 relative-clock labels, the following table on the valid 72-dimensional report sector, normalized within that sector and clock label:

\[
 P(i,j)=\begin{pmatrix}3/40&1/20\\1/10&3/10\\13/40&3/20\end{pmatrix},\qquad
 P(i,j,v)=P(i,j)/2,\quad v=\pm1.
\]

The verifier applies the old history before the new sign projectors and checks its actual record table, old work constraint and old \(G\)-invariance in both sign branches. Since the new gate acts on the sphere factor, it leaves those old work/target factors and already written classical \(i,j\) records intact; it can, however, decohere correlations involving the postmeasurement sphere when its pointer is ignored. The 72-dimensional result concerns the existing conditional history, not an assertion that the same report apparatus already exists on the other 118 exact-qubit dimensions.

**Where the bit comes from:** it is the outcome of measuring a direction transverse to a qubit prepared by the previous Bob measurement, using an explicitly selected pair of instrument directions and a newly supplied pointer. The state is not initially prepared with a definite \(V\) sign. In the conditional history the transformation \(T_0=Z_j B\), where \(Z_j\) acts on the old outcome register, leaves the pre-report history fixed and exchanges the two new sign branches. Appending an \(X_M\) pointer flip exchanges the corresponding recorded alternatives. This is an exact counterpart symmetry of this modeled history, not automatically a gauge redundancy or a necessity theorem. Equal Born weights do not decide whether both outcomes occur, how outcomes are selected, or how self-location is weighted.

## 4. A sharper experiential underdetermination

In the *90-dimensional* orientation, where the old chirality sign is actually conserved, the same old history admits both old chirality and the new sphere sign as commuting reports: they act on different factors. The verifier applies both actual old sign projectors and the new ones for all 16 clock labels. Each of the four sign pairs has weight \(1/4\), both branches retain the old total-orientation zero and old \(G\)-invariance, and the two signs agree on half the Born weight and disagree on half. Their differently chosen pointer readings are therefore **inequivalent operational structures, not merely a global relabeling**. This comparison does not pretend that the old chirality gate conserves the alternative 108-dimensional orientation: it does not.

Consequently even these strengthened physical constraints—balanced orientation, preserved records and a symmetry-respecting sign gate—do not by themselves select an experiential valence. The two observables answer different operational questions, and there is no established experiential mapping from either. A physical distinction between reporting circuits is not yet a distinction between actual subjects, pain and pleasure, or positive and negative fundamental experience. Nor can their formal mean-zero values be used to erase suffering. To make the proposed zero constitution genuinely determine experience rather than leave an unexplained choice, a further derivation must fix the admissible relational readout, its access/subject boundary and the experiential correspondence; simply declaring one choice necessary is not that derivation.

Likewise the added orientation and lab Hamiltonians are specified finite-model charges, not an identification of objective cosmic energy. The result strengthens the constructive link between zero-balanced structure and internally readable differentiation, but does not derive the sphere, the instrument, \(J\), the pointer, the 108-dimensional representation, plenitude or the law connecting structure to experience from bare zero.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
 python -m unittest verification.zero_conserving_sphere_handedness_report_test -v
```
