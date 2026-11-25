# One internal reference: zero, geometry, measurement and experience

> **Continuation:** [A reference from the paired state, and what a confined subject could report](ZERO_INTERNAL_REFERENCE_CONFINED_REPORT_NECESSITY.md) extracts the reference from the existing pre-measurement marginal, derives local discrimination limits, and tests whether a direct work-sign report preserves the later reference constraints.

> **Full-program synthesis:** [One reality, zero, experience and necessary plenitude](ZERO_ONE_REALITY_NECESSARY_PLENITUDE_SYNTHESIS.md) integrates the user's fourteen requirements and tests how gauge identity constrains experiential sign-pairing in the conserving report circuit.

## The broad proposal

A possible route to a self-sufficient whole is to treat its physical and experiential sides as aspects of **one internally articulated reality**, rather than first constructing a physical mechanism and then attaching experience to it. The zero would characterize the whole without external position, time or uncancelled externally specified surplus; internal distinctions would be real relations within it. The point–sphere picture expresses that distinction: one whole externally, a potentially rich internal organization.

This is a substantive proposal, not a deduction from the number zero. The demand is stronger than finding some mathematical structure compatible with zero: zero's own constitution must determine why there is physical differentiation, which subjects and experiences are actual, how they relate, and how incidences are weighted, without an unexplained selection. The user's further claims that no alternative framework can meet that demand if zero cannot, and that genuine possibility entails actuality, remain part of the inquiry rather than assumptions this calculation proves or refutes.

This continuation makes one connection concrete: **the same internal reference can normalize the sphere's relativistic directions and the quantum effects used by the existing noncommuting complement instruments.** It then identifies what this mathematical connection does and does not settle about a subject and felt sign.

Verifier: [`verification/zero_covariant_sphere_subject_bridge_test.py`](verification/zero_covariant_sphere_subject_bridge_test.py). It uses the existing sphere and physical complement constructions, not an unrelated second toy: see [`ZERO_POINT_SPHERE_TO_LORENTZ_CONE.md`](ZERO_POINT_SPHERE_TO_LORENTZ_CONE.md), [`ZERO_GEOMETRY_HISTORY_INCIDENCE_BRIDGE.md`](ZERO_GEOMETRY_HISTORY_INCIDENCE_BRIDGE.md), and [`ZERO_NONCOMMUTING_COMPLEMENT_SPHERE_HISTORY.md`](ZERO_NONCOMMUTING_COMPLEMENT_SPHERE_HISTORY.md).

## 1. Sphere and cone: one piece of mathematics, two roles

Represent a direction \(n\) on the unit sphere by

\[
 K(n)=I+n\cdot\sigma.
\]

This is a nonzero positive rank-one Hermitian matrix, with zero determinant. The same matrix is proportional to a pure qubit density operator and represents a future null ray in the usual Hermitian-matrix representation of a Lorentz cone. Under \(A\in SL(2,\mathbb C)\),

\[
 K\mapsto K'=AKA^\dagger,\qquad \det K'=\det K.
\]

Thus the **same projective sphere** can play the mathematical role of quantum effect directions and relativistic null directions. That is a nontrivial structural unification. It is not, by itself, a derivation of physical spacetime, quantum theory, or a subject from a bare zero. The complex projective structure, spinor lift and physical interpretation remain inputs.

A further issue matters. Normalizing every \(K'\) to trace two using a fixed \(I\) is a choice of frame; it is not an invariant definition of the original balance. In the existing three-ray configuration the directions lie in the xy plane and

\[
 \sum_iq_i n_i=0,\qquad q=(1/8,2/5,19/40).
\]

Apply a boost \(A=\operatorname{diag}(e^{\eta/2},e^{-\eta/2})\) along z. Each ray acquires the same normalization factor \(\cosh\eta\), so these particular \(q_i\) remain the normalized weights, but the new ordinary spatial mean is

\[
 \sum_iq_i n'_i=(0,0,\tanh\eta),
\]

not zero. The test checks this explicitly at \(\eta=0.61\). Thus a zero spatial mean in one frame is not, by itself, an observer-independent whole-level zero.

## 2. Covariant balance relative to the internal reference

Supply a positive-definite Hermitian reference \(N\), and in its rest representation take \(N=I\). The three given null matrices satisfy

\[
 \sum_i q_iK_i=N,\qquad \sum_iq_i(K_i-N)=0.
\]

Now transform **both** the directions and reference:

\[
 K'_i=AK_iA^\dagger,\qquad N'=ANA^\dagger.
\]

The same weights obey the same matrix relation in every such representation. The nonzero individual contrasts \(K_i-N\) cancel as matrices; the matrices \(K_i\) themselves are positive, not positive and negative energies.

For a reference-relative comparison direction \(B\), also transported by \(B'=ABA^\dagger\), define

\[
 d_i=\tfrac12\operatorname{tr}\!\left[N^{-1}(K_i-N)N^{-1}B\right].
\]

This is unchanged by simultaneous congruence transformations. For the prior example it equals \((-1/5,1/2,-7/19)\), with \(\sum_iq_id_i=0\), although every \(d_i\) is nonzero. The example has \(\operatorname{tr}(N^{-1}K_i)=2\), \(\operatorname{tr}(N^{-1}B)=0\), and a unit reference-relative norm for \(B\); these conditions are also preserved.

**Why the qualification matters:** if the rays and an *independently determined* reference \(N\) are given, the full matrix relation fixes the example's weights uniquely. If instead we simply *define* \(N=\sum_iq_iK_i\), the zero is automatic and does not explain the weights. Indeed, a different, equilateral three-ray configuration with equal weights also has \(N=I\); its relative angles differ from the unequal-weight example. The test checks both. Closure alone has not selected the physical geometry or measure.

The reference is an internal geometrical structure here, **not yet** the earlier reference qubit F, a global time direction, an objective whole energy, or a subject. Identifying those things requires a further physical construction. Allowing different local references would not by itself impose a preferred cosmic foliation.

## 3. The same reference produces the measurement effects

Normalize the directions relative to \(N\), rather than to an external frame:

\[
 E_i=q_iN^{-1/2}K_iN^{-1/2},\qquad \sum_i E_i=I.
\]

These are positive rank-one qubit effects. In the rest representation they are exactly the earlier sphere effects \(q_i(I+n_i\cdot\sigma)\). Under simultaneous transformation of \(K_i\) and \(N\), define

\[
 U=(N')^{-1/2}A N^{1/2}.
\]

This \(U\) is unitary, and the normalized effects transform as \(E'_i=UE_iU^\dagger\). The normalized comparison direction is rotated by the same \(U\), so all \(d_i\) remain unchanged. This connects, in a single equation chain, the **same reference**, the causal-cone representation, the balanced directional contrasts, and the quantum POVM.

The verifier applies this connection to the actual prior complement instruments:

- for the paired qubit blocks, it reconstructs the existing noncommuting qubit POVM;
- for the odd-multiplicity spin-1 and spin-4 blocks, it lifts the same relative rotation into their higher-spin representations, retaining their genuinely noncommuting but unsharp effects;
- it checks equality of the *full six-pointer amplitude Gram matrix* before and after re-expression, not just setting marginals;
- it checks the physical lifted rotations commute with all three declared lab charges and with the stated lab energies; and
- it follows the compressed outputs through the old relative-clock, record–work and target circuit and representative later reference-memory phases. Their corresponding joint tables agree.

These complement blocks cover 190 dimensions in the exact-qubit alternative, or 229 in the wider unsharp alternative. The old two-dimensional code and scalar remainder are retained in the preceding complete models but are **not newly proven here to carry an active spacetime boost**. In fact, \(A\) is generally nonunitary. The calculation is a covariant change of representation followed by a compact reference-relative rotation; it is not a physical implementation of a Lorentz boost, a derivation of the Lorentz action on the entire apparatus, or a demonstration that the earlier finite reference clock is \(N\). The declared complement energy is highly degenerate, and interaction/control energy remains outside the established accounting.

## 4. A candidate physical–experiential connection

The unified hypothesis would go further than a measurement device:

1. A locally unified physical organization has an internally realized reference against which changes and contrasts are meaningful.
2. Some such organizations are actual subjects; their first-person life is the intrinsic aspect of that organization, not an extra observer sitting outside it.
3. Records within the organization relate its states and support experienced succession; neither external time nor access to the whole is presumed.
4. A physically grounded signed relation might also have a felt aspect. If so, a genuine positive/negative experiential pair must reverse *that felt aspect*, not merely a coordinate sign.

This is a program for an identity of physical and experiential constitution. Merely calling a reference or a record a subject would not establish it. A defensible subject criterion must say what is integrated, what relations are accessible within that boundary, and how overlapping or refined descriptions relate to actual incidences. A boundary cannot automatically register richer-domain activity; in particular, a traveler’s room activity is not simply a surface inhabitant's experience. The proposed account must also deal with first-person quality and felt valence, not just the ability to produce a physical report.

The work witness in the current model gives a concrete place to test the program. In the earlier record–work sector, let \(r,t\in\{+1,-1\}\) be the two accessible signs and \(j=rt\). A physical involution pairs opposite \(j\) while preserving the tested history. If a suitable actual incidence measure is invariant under it, then any integrable *genuinely felt* value odd under the same pairing would have zero global sum. Positive and negative experiences would remain individually real. A physical matrix involution, a spatial mirror, or a reversal of energy does not by itself prove such a felt reversal; nor does a formal negative contribution establish suffering.

## 5. A stronger test of the experiential bridge

Even adding the reference-relative geometry does not force a unique felt sign. On the **same fixed physical histories and joint labels**, provisionally consider two normalized candidate assignments:

\[
 v_1=j,\qquad v_2=\operatorname{sgn}(d_i)\,j.
\]

Both have values \(\pm1\). Both are odd under the specified physical pairing, and both have zero weighted mean in the tested histories. Their dependence on \(d_i\) is invariant under the simultaneous reference changes above; \(j\) is an unchanged internal witness in this representation test, **not** a separately established relativistic scalar of an actual spacetime theory.

They nevertheless give opposite signs on exactly the settings with \(d_i<0\). For the geometric marginal those settings have weight

\[
 q_1+q_3=1/8+19/40=3/5.
\]

The verifier checks the 3/5 disagreement, both zero means, and the weighted-state pairing for the actual code, paired-qubit, spin-1 and spin-4 circuit states, each old-clock label in the selected window, and three later relative phases. This is stronger than contrasting a balanced value with a value that fails the mirror rule: **both candidates meet the same covariance and mirror-oddness tests**.

These are mathematical candidate assignments, not a proof that either is felt or that both are genuinely metaphysically possible. If the relevant i, r and t are not accessible within a proposed subject boundary, neither should be attributed to that subject on the strength of this joint calculation. If independently justified reports reveal felt sign, they can help distinguish proposals—but the report's veracity and access must themselves be accounted for. Likewise, a transformation that is merely gauge cannot by itself generate two physically or experientially distinct incidences.

This counterexample gives the next task a precise target: derive a **constitutive reason** for selecting a signed experiential relation, or show why apparently different assignments are not distinct under a justified subject/observable identity. It is not enough simply to call one candidate impossible.

## 6. Necessity, incidence, and a constructive path

The broad picture remains compatible with an unselected necessary whole: distinct internal histories and subject-perspectives might all be actual without being chosen by irreducible objective chance. Probability could then describe self-location or incidence within the whole. This is a conditional interpretation, not an inference that quantum support automatically means actual experiences. The earlier refinement examples show that mathematical labels are not automatically distinct subjects, and mirror support alone does not fix incidence weights.

The most direct program is therefore a *mutually constrained closure*, not a chain of unrelated identifications:

- **Reference:** derive a relational reference from the internal organization instead of merely defining it to make an average zero.
- **Geometry and dynamics:** determine how references and their cones fit together; recover physical interactions, energy accounting and accessible record histories, with no preferred external time.
- **Subject boundary:** derive which organized processes are genuine incidences and which descriptions or transformations are redundant.
- **Felt sign:** test whether the same constitutive dynamics fixes a first-person signed value and a real counterpart, rather than only producing several compatible formal signs.
- **Measure and whole zero:** derive how actual incidences contribute to the relevant globally additive quantity, including convergence if infinitely many occur, and whether its zero relates to objective whole energy or to experience or both.

This is an attempt to meet the full no-residue demand, not a proposal to accept any of the remaining structures as brute facts. The present construction provides a shared mathematical interface and an exact discrimination test; it does not yet show that the interface, the physical laws or a unique experience law are necessitated by zero.

## Verification

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps \
  python -m unittest verification.zero_covariant_sphere_subject_bridge_test -v
```

The finite-matrix comparisons use NumPy. The verifier clips eigenvalues below `1e-14` when taking square roots of effects, to avoid spurious order-\(\sqrt{\epsilon}\) differences at exactly zero eigenvalues; it checks the squared roots against the original effects. A comparison with the previous routine, which retains such tiny positive roundoff eigenvalues, uses `1e-8` tolerance. Continuum covariance follows from the displayed matrix algebra; the executable tests use representative transformations and relative phases.
