# Why the local-magnitude anomaly arises—and a deeper relational resolution

## Answer

The deepest identifiable cause **inside the present construction** is that two different notions of symmetry were being combined:

1. A **change of internal reference frames** must leave an actual relation—and therefore its magnitude—unchanged.
2. An **independent active rotation of the two directions while their comparator is held fixed** changes their relative angle. If the magnitude is a nonconstant function of that angle, it must change too.

The previous dressed action is a mathematically valid version of the second operation. Its preservation of the whole state and zero sum did not make it a symmetry of every individual physical observable. This is not an error in the calculation, nor does zero require differentiated contributions to have identical magnitudes.

There is a deeper constructive resolution: make the **comparison itself relational**. Introduce a relative-frame link and transform it along with the two internal directions. Then independent frame changes preserve the true angle, both local signed magnitudes, the constrained zero sum, and the previously constructed clock/record history. The link is a gauge-coordinate device in this model, not a new external direction or an independently asserted physical substance. This recovers a common notion of symmetry without flattening real differentiation.

That resolution also reveals a deeper issue rather than concealing it: frame symmetry alone does **not** fix how the different relational angles are weighted. Zero total does not fix that weighting either. Necessary plenitude, symmetry, actual incidence and measure therefore need to be related by a constitutive principle—not by calling an arbitrary measure “no preference.” The mathematical result below does not establish that such a principle cannot be derived from zero; it identifies exactly what a successful derivation must determine.

The [implementation](verification/zero_relational_link_symmetry.py) and [tests](verification/zero_relational_link_symmetry_test.py) include explicit frame transformations, reconstruction of complete gauge orbits, the actual clock/pair records, and a nonuniform-state symmetry control.

## 1. The root: changing a relationship is not merely changing its description

Let the two internal directions m and n initially be expressed in one common frame. Their actual relative cosine is

```text
u = m·n.
```

A common rotation of both leaves u unchanged. But if we rotate only n while keeping the comparison frame fixed, u generally changes. Earlier we made that active change into a representation of `SO(3)×SO(3)` by dressing it with unitaries that transport the real records and pair. For `H₁=κ g(u)Z₁` on the physical pair sector,

```text
H₁² = κ² g(u)² I.
```

Since the active group is transitive on pairs `(m,n)`, an operator of this form can commute with every active transformation only if `g(u)²` is constant almost everywhere. This is the precise source of the apparent anomaly. It is not caused by a numerical error, failure of the reservoir dressing, or positive and negative contributions failing to cancel. It follows already from the combination of **transitivity, a nonconstant relational observable and a requirement of invariance of that observable**.

The preceding result remains correct. A dressed active rotation relates different configurations and their records, but it is not thereby a gauge redundancy. It may be appropriate for a covariant family of configurations; it is not a symmetry of all individual charges or automatically of a physical Hamiltonian. The individual charges can transform while their sum remains zero. Whether such an active transformation is a symmetry of the physical constitution is a further substantive question.

## 2. A link makes independent frame changes truly relational

Let m and n now be coordinates in two internal frames. Let `L∈SO(3)` transport n's coordinate vector into m's frame, and define the actual comparison

```text
u = m·(L n).
```

For independent internal-frame changes `A,B∈SO(3)`, transform **all three** entries:

```text
m ↦ A m,        n ↦ B n,        L ↦ A L B⁻¹.
```

Then `m·Ln` is exactly unchanged. For instance, in the gauge `L=I`, independently rotating n **without changing L** is not a gauge change; it changes the relationship. A genuine frame change includes the transformation of L. The model's local sign and magnitude observables can now remain real and invariant:

```text
H₁=κ g(m·Ln) Z₁,       H₂=−H₁  on the physical sector.
```

Both individual values and their zero sum are unchanged by these frame transformations. The same is true of all functions of u, including the two earlier magnitude laws, and of the retained physical sign k. This does not identify positive and negative values, identify the two pair carriers, or treat suffering as absence of experience.

The link does not secretly add a new physical direction in this mathematical model. It can be set to identity by a frame transformation. Indeed, two triples `(m,n,L)` and `(m',n',L')` are related by the independent frame transformations **if and only if** their u values agree. The nontrivial direction is constructive: rotate the ordered pair `(m,Ln)` onto `(m',L'n')` by A, then choose `B=L'⁻¹ A L`. The construction works at the endpoints as well as for non-collinear pairs. After fixing `L=I`, the residual frame rotations are common rotations, and their orbits are exactly the old relative-angle classes. Thus the link formulation recovers the original relational content rather than explaining it away.

This is an explicit model of a comparator, not a derivation of a physical gauge connection, spacetime transport or a laboratory operation from zero. If the two internal frames were not actually independent in the physical constitution, the use of this redundancy would need independent justification. Conversely, putting the link in by hand does not itself supply the physical–experiential identity.

## 3. The resolution includes the real recorded and stationary model

Equip the two direction spheres with normalized area and the link with normalized Haar measure. Their product pushes forward to `du/2` for u: for any fixed L and n, a uniformly distributed m has uniform relative cosine. The new gauge-invariant vector-valued Hilbert sector consists of functions of u. It is isometric to the same scalar-angle sector used in the [earlier sphere lift](ZERO_SYMMETRY_POINT_SPHERE_QUANTUM_PLENITUDE.md). The enlargement is therefore a frame description of that model, not an independent claim that a new degree of freedom has been observed.

The actual original echo vectors, sign-controlled record dressing, discrete angular-copy pair constraint and clock-dependent purified apparatus can all be represented as the same functions of u as before. Since the frame change leaves u and its bin unchanged, it leaves the **actual old records and pair signs** unchanged rather than switching B or rewriting the reservoir. It also commutes with the old tick dynamics and reference-clock shift, which act on the record/apparatus factors rather than on these frame coordinates. The stationary history remains a stationary, gauge-invariant history, and the pair constraints and both local magnitude operators are preserved on it.

The tests evaluate the actual complex old/R vectors for two source labels, both sign branches, four angular bins and several clock blocks, together with a corresponding actual apparatus prefix. The all-label and all-tick claims for the factorized construction use the previously tested source-span and clock-prefix results plus the fact that the new frame action does not change u; they are not an additional dense full-reservoir simulation. At this stage the frame action treats the old record factors as scalar spectators; a theory that identifies them with nontrivial frame representations must specify and test their own transformation laws.

This resolves the local invariance problem **as a reference-frame problem**. It does not turn the preceding active u-changing rotations into gauge transformations: configurations with different u remain different physical relational configurations in this model.

## 4. The meta-level: why zero and symmetry do not yet determine a measure

The new gauge group is not transitive across the complete configuration space. Its orbits are labeled by u. Compact-group invariance gives a unique normalized orbit measure **within each fixed u orbit**, but an invariant probability on the whole space is a mixture of those orbit measures with an arbitrary probability law `ν(du)` on the orbit space. Equivalently, a gauge-invariant density can be any suitable nonnegative function of u. Gauge symmetry removes arbitrary frame coordinates; it does not remove actual relations.

There is a constructive canonical route to `ν=du/2`. On the *kinematical configuration space*, allow an independent rotation of each direction and an independent left translation of L. This compact product action is transitive, so its unique normalized invariant probability is the product of the two normalized round areas and normalized Haar measure. Its pushforward is `du/2`; no finite nonzero angular parameter needs to be selected within that specified structure. But this larger action changes u and is not a symmetry of the individual magnitude observable. It is a **kinematical measure-selection principle**, not a consequence of frame gauge or proof of a dynamical symmetry of the whole. It uses the given round geometry, link group and product action, which would themselves have to follow from the point–sphere constitution. Maximizing entropy also depends on a reference measure and does not avoid that question.

An exact counterexample keeps the old coarse records while changing the continuum magnitude distribution. For `|ε|<1`, use the strictly positive gauge-invariant density

```text
ρ_ε(u)=1+ε cos(2πu)         relative to du/2.
```

It has full support, respects the earlier negative-band reflection `u↦−1−u`, and gives the same probability `1/4` in each N=4 bin as the uniform law. Therefore it gives the same reduced state of the original old records, discrete pair copies, purified apparatus and clock after the angular variables are traced out: in each bin the relevant vector-valued history is the same, and the integrals of the two densities over that bin agree. This holds for coherent source-label and clock superpositions, not just diagonal tick statistics. Yet a continuum-sensitive observable distinguishes the states:

```text
⟨u²⟩_ε = 1/3 + ε/(2π²),      ⟨u²⟩_0 = 1/3.
```

Thus both have the same zero pair total and coarse recorded history, while `H₁²=κ²u²` has different expectations for the `|u|` law. The code checks the bin integrals, the exact second-moment formula, the actual old/pair/clock sector construction and an off-diagonal clock control: the unnormalized tick-0/tick-10 carrier–apparatus overlap is `9/256` for both laws, before the uniform clock normalization; it survives the q=2 reference trace. The equality of the *full reduced density operators* follows from the piecewise-constant history and those bin integrals; no enormous density matrix is materialized. These are alternative formal states of this model, not a claim that they are genuinely distinct possible complete realities.

The logical point is sharper than “we have not found a distribution.” On the constrained sector `H₁+H₂=0` is the **zero operator**, so every unitary preserves that sum; it cannot by itself select an action, a magnitude law, a state, or an incidence measure. Zero total is compatible with rich internal structure, but this algebraic zero is not yet an explanation of why this particular structure exists. Nor is a zero vector in a Hilbert space a normalized physical state. It would be a category mistake either to equate the ontological zero proposal with that vector or to refute the proposal by doing so.

## 5. A second meta-control: abstract symmetry can be tailored to a state

Even asking for a transitive `SO(3)×SO(3)` representation is insufficient if its physical action is unspecified. For the positive ρ above, set

```text
h(u)=u + ε sin(2πu)/(2π),       h'(u)=ρ_ε(u)>0.
```

Keeping m and the tangent azimuth fixed, h is a bijective change of relative angle. Including the square root of its Jacobian gives a unitary T on the same spherical Hilbert space, with `T 1=√ρ_ε`. If P is the original independent-rotation pullback, then

```text
P_g^(ε) = T P_g T†
```

is another strongly continuous representation of the same abstract group, and it fixes `√ρ_ε`. T commutes with common rotations but its conjugated independent action is **not** the original bare geometrical rotation of the directions. The code verifies the inverse map, the Jacobian norm, group composition on a complex wave, and invariance of the nonuniform wave; the same wave fails the original bare independent rotation. The existing record/pair dressing D gives the analogous construction `D T P_g T† D†`; clock-prefix conjugation carries it to the stationary history. Its admissibility as a symmetry of physical observables is a separate question.

So one cannot derive an objective no-preference law merely from the words “there exists a symmetry group” or from the invariance of an adapted state. The **action on observables**, its physical meaning, and the measure or inner product are part of the claim. This also explains why the previous fixed-action uniform selection was valid but conditional: it did not establish that the fixed action is uniquely selected by the whole's constitution.

An even stronger version of “no arbitrary preference” cannot be implemented by requiring a normalized full-support probability invariant under **every** smooth increasing reparameterization of the open interval. Any interior subinterval can be sent to arbitrarily many disjoint interior subintervals; invariance would give them all the same mass, forcing that mass to zero. Countable covering then gives the entire interior zero mass. Only endpoint-supported probabilities survive. This is a theorem about that particular overstrong invariance demand, not a disproof of necessary plenitude, unnormalized measures, or actualization of measure-zero possibilities. It shows that a normalized measure requires relevant structure, not neutrality under every conceivable relabeling.

## 6. What this contributes to the user's whole

The point with no external space or time can still admit real, internally related differentiation; the comparator and its gauge freedom express the difference between a relationship and a choice of coordinates. Opposite contributions can be real and cancel without individually vanishing. Symmetry need not erase magnitudes, subjects or experiences. Necessary plenitude need not mean that every coordinate description is a different actuality, and a probability density is not the same thing as the existence or number of experiences. A necessarily fixed measure, if derived, would also not by itself imply irreducible chance or determine individual outcomes.

The remaining constitutive question is not whether an unexplained residue is acceptable—it is not. It is whether zero's own constitution determines the comparison structure, admissible dynamics and observables, genuine-possibility domain, actual incidence and its measure, and the intrinsic/extrinsic identity **together**, rather than adding each as an independent postulate. The present result neither proves nor disproves that stronger programme, and it does not assume that a formal counterexample is a genuinely possible whole. It provides a nontrivial target: derive the orbit-space law and physical–experiential rules without making gauge-coordinate neutrality carry a burden it cannot bear.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_relational_link_symmetry_test -v
```

Numerical checks support the explicit finite and sampled identities; the orbit classification, invariant-measure decomposition, full-history factorization and reparameterization obstruction are the analytical arguments stated above.
