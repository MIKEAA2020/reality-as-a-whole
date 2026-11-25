# Keeping the sphere while sourcing its reference internally

## Main result: the earlier tradeoff was too strong

The [previous construction](ZERO_INTERNAL_PAIRED_RESOURCE_SPHERE_AND_REPORT.md) obtained an internal D/E singlet on 96 dimensions, but used a different sphere pairing and a neutral instrument elsewhere. That implementation **did not need to give up** the previous 190-dimensional exact-qubit sphere instrument.

There is a different ordering of the same multiplicity basis in which:

- the actual Alice and Bob Kraus operators on all **190 complement dimensions are exactly the earlier physical sphere operators**, not merely statistically equivalent;
- within 96 of those dimensions the original paired state simultaneously supplies an undisturbed D/E singlet;
- the same conserving, gauge-even joint relative-sign report can be applied on that 96-dimensional sector, with an explicit validity flag; and
- the old two-dimensional code and all other sectors remain present.

Thus the sphere has its previous exact-qubit coverage of **192/256 including the code**, while the internal sign-reference report has validity weight **96/256**. The sign is not claimed on the other 160 dimensions. The old physical instrument is unchanged **before** the subsequent flag and sign-report operations; the latter add operations and can change the full joint state. They are not automatically accessible to either confined observer.

We can also reproduce the earlier **229-dimensional noncommuting complement coverage**, while sourcing the reference internally, if we reduce the valid reference sector to 60 dimensions and replace—not preserve—the old spin-4 instrument. The resulting coverage/reference frontier is explicit below.

Verifier: [`verification/zero_nested_sphere_internal_reference_test.py`](verification/zero_nested_sphere_internal_reference_test.py). This builds directly on [`verification/zero_all_sector_noncommuting_sphere_test.py`](verification/zero_all_sector_noncommuting_sphere_test.py), [`verification/zero_internal_pair_sphere_report_test.py`](verification/zero_internal_pair_sphere_report_test.py) and the earlier [relative-sign report](ZERO_RELATIVE_SIGN_GAUGE_COUNTERPART_CONSTRUCTION.md).

## 1. One basis ordering preserves the old physical instrument

In the old exact-qubit construction, the selected copies within each irrep are paired adjacently: \((0,1),(2,3),\ldots\). On an irrep with \(m\) copies, group them four at a time and define an Alice isometry with columns in this order:

\[
 F=\big[\,p_{4g+2r+s}\,\big]_{s=0,1;\ r=0,1;\ g<\lfloor m/4\rfloor},
 \qquad t=\lfloor m/4\rfloor d.
\]

Each \(p_j\) contains all \(d\) irrep columns. The tensor order is sphere qubit \(s\), reference qubit \(r\), group \(g\), irrep. On Bob use

\[
 B=\overline F(I_2\otimes J^T\otimes I_t).
\]

The logical sphere qubit now connects **the old adjacent pairs** \((0,1)\), \((2,3)\), and so on, whereas the reference qubit connects the two adjacent pairs in each four-copy group. The previous 96-dimensional construction chose a different order and therefore did not establish this identity.

For every selected block and for all physical instrument Kraus operators, the new test verifies

\[
 K_i^{\rm old}P=F(K_i\otimes I_2\otimes I_t)F^\dagger,
 \qquad
 B_j^{\rm old}\overline P=B(B_j\otimes I_2\otimes I_t)B^\dagger.
\]

Here \(P=FF^\dagger\), and the Bob identity includes the original conjugate-basis convention. The reference Pauli operators commute with the old sphere operators, the original local charges and both declared lab Hamiltonians. The verifier checks the full \(256\times256\) matrices, not just their traces or outcome probabilities.

The actual paired-state amplitude still factors exactly as

\[
 F^\dagger(P/16)\overline B
 =\sqrt{4t/256}\left(I_2/\sqrt2\right)\otimes
 \left(J^T/\sqrt2\right)\otimes\left(I_t/\sqrt t\right).
\]

Consequently the sphere pair, D/E singlet and spectator are all already present in that sector of the original paired state. Sphere measurement leaves the reference intact. The tested logical-reference source is then exactly the one required by the previous relative-sign circuit.

## 2. Coherent whole-state accounting

Let \(Q\) be the old 190-dimensional exact-qubit complement projector, \(P\leq Q\) the new 96-dimensional reference-valid projector, \(R\) the old 64-dimensional scalar remainder, and \(P_C\) the old code. They give the orthogonal decomposition

\[
 I=P_C+P+(Q-P)+R,\quad
 \dim(P_C,P,Q-P,R)=(2,96,94,64).
\]

The original paired state is not replaced. The verifier applies the unchanged old Kraus operators to its full coherent complement and checks, for every joint sphere outcome, that the physical amplitude is the sum of its orthogonal valid and invalid pieces. The valid share of each such joint outcome is \(96/190\), a consequence of the explicit identical qubit instrument on both pieces—not a universal property of validity flags.

A neutral flag can be controlled by \(P\); it commutes with the old sphere Kraus operators. It can therefore be written before or after that instrument without changing the old sphere outcome probabilities. **Flagging is not literally no operation:** if the flag is ignored, it can decohere lab coherences between the valid and invalid sectors. The flag can be coherently uncomputed before the sign report; once a conditional report has correlated other systems with it, removing those correlations requires additional operations. The unchanged-instrument claim concerns the pre-report instrument and its old outcome statistics, not equality of the complete final state after reporting.

The circuit applies the new sign gate only for validity 1. The test reuses the full relative-report projectors on the actual source at all 16 earlier relative-clock labels and checks both sign branches, the enlarged orientation-zero conditions, old balance and diagonal-swap invariance. The previously verified operator commutators give compatibility with the later clock phases. If a window contains \(k\) of the 16 labels,

\[
 P(\mathrm{valid},i,V=\pm1,\mathrm{window})
 =\frac{k}{16}\,\frac{96}{256}\,\frac{q_i}{2},
 \qquad q=(1/8,2/5,19/40).
\]

The old code and invalid sectors carry no purported new ± report. In particular, the old record/target statistics checked **before** the sign gate must not be assumed undisturbed afterward merely because the sphere operators are unchanged. The joint gate, pointer, flag, F reference and timing remain stipulated, as does the required access to reference qubits encoded in different labs.

## 3. The wider coverage/reference frontier

The earlier wider construction used an irreducible spin-4 directional instrument on all nine multiplicity copies in the \((1,1)\) block. It covered 229 complement dimensions, but its actual spin-4 effects have a one-dimensional commutant on the nine-copy multiplicity space. The new verifier computes the commutant of two nonparallel old effects and checks that the 72-of-81 reference-valid projector does **not** commute with the old effect or its Kraus operator. Hence that particular old spin-4 instrument cannot coexist with this nontrivial, nondisturbing validity flag. This is an incompatibility of the specified operators, not a statement that all 229-dimensional coverage is impossible.

Two compatible replacements are now explicit:

| choice | valid internal reference | exact-qubit sphere on complement | unsharp noncommuting sphere | scalar complement | code |
|---|---:|---:|---:|---:|---:|
| Preserve old exact-qubit instrument | 96 | 190 | 0 | 64 | 2 |
| Wider sphere, maximum internal reference | 96 | 130 | 90 (spin 1) | 34 | 2 |
| Maximum sphere coverage, smaller internal reference | 60 | 94 | 45 (spin 2) + 90 (spin 1) | 25 | 2 |

Counts in a row are dimensions; reference-valid dimensions are **included** in the exact-qubit column, not additional. The spin labels refer to selected multiplicity-space representations, not physical lab charges. All instruments, flag and logical reference operators commute with the declared lab charges; the tested operators also commute with the declared lab Hamiltonians. The original input and code are unchanged, and the verifier checks physical post-instrument Gram matrices for the new spin-2 and spin-1 blocks, as well as the actual D/E singlet amplitudes.

For the 220-dimensional wider choice, use all eight \((1,1)\) copies available for the reference and leave its ninth copy scalar. The two nine-dimensional consequences are transparent: \(96+34+90=220\) complement dimensions support noncommuting sphere instruments; \(9+25=34\) are scalar.

For the 229-dimensional choice, use only **four** of the nine \((1,1)\) copies for the reference and put the remaining five in a spin-2 unsharp instrument. The selected reference dimensions are \(12+12+36=60\), while all but the original multiplicity-one \((2,2)\) block support noncommuting sphere effects:

\[
 60+34+45+90=229, \qquad (229+2)/256=231/256.
\]

The valid reference weight is \(60/256=15/64\), and each sign has weight \(15/128\) before clock conditioning. This scheme preserves the **coverage** of the old 229-dimensional construction, not its spin-4 Kraus operators or all its correlations. In particular, it uses a five-copy spin-2 block instead of the old nine-copy spin-4 block.

### Why these endpoints are maximal within the stated class

The local charge commutant acts on irrep multiplicities. A valid sector carrying two commuting full qubit algebras uses a multiple of four copies. With the old code separate, only multiplicities 6, 6 and 9 can contribute; the other available multiplicities are 1, 2 or 3. The two six-copy blocks each contribute at most four copies, i.e. 12 dimensions apiece. The nine-copy block contributes at most eight copies, i.e. 72 dimensions. Thus 96 is the maximum exact internal-reference support in this class.

Require also that the validity projector commute with the sphere instrument, so valid and invalid sectors are not mixed. If all eight eligible copies of the nine-copy block are valid, its one remaining copy carries an irreducible nine-dimensional charge representation. By Schur's lemma, a charge-commuting lab effect is scalar there. The other unavoidable scalar block has dimension 25. So with 96 valid dimensions, at most \(254-9-25=220\) complement dimensions can carry noncommuting charge-preserving lab effects; the middle row attains it.

To attain all 229 noncommuting complement dimensions, the invalid part of the nine-copy block must have at least two copies, so its valid part can use at most four copies. This limits validity to \(12+12+36=60\), attained in the last row. These bounds assume the original representation, separate code, an invariant validity sector, charge-preserving **local** instruments and two full commuting qubit algebras on the valid sector. Approximate or disturbed references, nonlocal effects, altered charges, added resources, or a different state are outside the claim.

## 4. What can and cannot be inferred from the tables

For the code-plus-complement histories, the verifier checks the old \(i\), record, and target table at the full old clock and at the three-label window. The 220-dimensional replacement gives exactly the same table as the old 190-dimensional qubit scheme, despite having different physical effects: the spin-1 visibility on 90 dimensions equals the aggregate contribution of 60 exact-qubit dimensions plus 30 scalar dimensions. Equal tables do **not** make their instruments identical or imply equal postmeasurement lab states.

For the 229-dimensional replacement, the corresponding direction–record witness, averaged over all 16 old-clock labels, is

\[
 \langle d_i r\rangle=-56833/486400,
\]

whereas the previous full spin-4 construction gave \(-97727/972800\). They agree on the geometric \(q_i\) marginal but not the complete correlation. These are finite-circuit Born statistics, not established weights of actual subjects and not measurements of felt experience.

## 5. Significance and limits

This improves the previous result in a substantive way: **the same sphere apparatus and the internally sourced sign reference can coexist**, rather than requiring a blanket choice between them. It also shows how maximum reference support, maximum noncommuting sphere coverage and preservation of one particular physical instrument differ. The remaining 25-dimensional Schur obstruction and the 96-versus-60 frontier are conditional, explicit representation facts—not unexplained cosmic residues.

None of this derives the initial paired state, lab representation, choice of encoding, old F reference, flag, pointer, joint operation, clock or measurement weights from zero's constitution. The orientation constraints and declared lab energies are not objective whole-universe energy, and the complete control energy is not accounted for. The gauge-even report is not automatically a subject or a felt value; opposite labels do not by themselves cancel suffering. The point–sphere and experiential–physical synthesis still requires those structural and intrinsic links, rather than their being assumed here.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
  python -m unittest verification.zero_nested_sphere_internal_reference_test -v
```

The proof of the stated dimension frontier is representation-theoretic; the finite matrix equalities, actual encoded amplitudes, clock histories and commutant ranks are numerical checks with the tolerances in the verifier.
