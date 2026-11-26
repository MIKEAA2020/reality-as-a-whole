# Toward one constitution of zero and experience

## The task at full strength

The user's proposal is not merely that zero energy and physical–experiential identity are convenient hypotheses. It is that **reality must be fully intelligible**, and that if zero cannot satisfy that demand, nothing can; likewise, if identity cannot satisfy it, nothing can. Properly understood, the whole must therefore have both features—not as two laws imposed from outside, but as aspects of one self-sufficient constitution.

This note pursues that direction directly. It neither assumes that the whole is an empty scalar nor treats a determination as unexplained simply because it is determinate. The aim is to explain **real local distinctions and experience without an independent remainder**, not to explain them away.

The constructive result is a canonical reference-free way to obtain zero balance and nonzero local differences from a single relational description. A further pointed-description calculation shows how an apparent interchange of the two sides can be a change of labels **without erasing their different local values**. The same construction also supplies an exact challenge: reference independence permits a nonzero global *spread*, so it does not by itself establish that the universe's **physical total energy** is the zero quantity; and its local values do not by themselves establish felt quality.

These are mathematical consequences of the stated premises, not a proof that zero cannot explain reality. The unresolved question is whether a deeper constitution necessitates the premises and identifies the relevant physical and experiential aspects. [Checks](verification/zero_intrinsic_difference_common_constitution_test.py).

## 1. The argument, without weakening it

Let `I` state that the actual whole is fully intelligible, including its actuality, physical organization, real experiences and their relations. This is an ontological demand; it need not mean that a finite human has already written down every fact, or that acquaintance with experience must be exhausted by a verbal description.

Let `Z*` mean: **there is an objectively adequate, true zero-constitution of this actual whole** meeting that demand. Let `D*` mean: **there is an objectively adequate identity constitution of this actual whole** meeting it, without an unexplained metaphysical separation between a particular experience and its physical–relational occurrence. The user's strongest claim may be expressed

```text
I
not Z* → not I
not D* → not I
therefore Z* and D*.
```

The inference is valid by contraposition. It does not require an external chooser or producer. Nor must an identity be analytically obvious in advance. The substantive work lies in justifying both dominance premises and showing **one constitution** in which the zero and identity are jointly intelligible, rather than writing two desired conclusions into separate definitions.

The explicit reference to the **actual** whole matters. If instead `Z*` means only that *some conceivable zero model* could meet the standard, a successful zero model does not by itself show that the actual whole has that nature. The user's intended actual-constitution reading is stronger; it should be defended at that strength rather than silently replaced by the weaker model-compatibility claim. Similarly, incompatibility with an unfinished rival is not a proof that all nonzero or nonidentity rivals fail the user's no-residue standard. Neither point is a proof that such a rival succeeds.

The earlier [direct foundational argument](ZERO_TOTALITY_FOUNDATIONAL_BRIDGE_DIRECT_ARGUMENT.md) set out this target, including the user's reason for treating zero as distinguished against ordinary unexplained finite totals. The new calculation below asks what “no external reference” actually fixes.

## 2. An internal balance derived from differences

Begin with `n≥2` indexed positions in a finite **candidate description** of one whole. Let `x=(x₁,…,xₙ)` be their real coordinates. The indices need not be separately existing substances, particles or subjects. Suppose a common shift

```text
xᵢ → xᵢ+c  for every i
```

is a passive redescription of that same relation: only differences matter. This is an **assumption about what the physical constitution makes redundant**, not a demonstration that every possible energy offset is physically unobservable. Define

```text
x̄ = (1/n) Σᵢ xᵢ,        eᵢ = xᵢ−x̄.
```

Then, for every state and every common shift,

```text
Σᵢ eᵢ = 0,
eᵢ(x+c1) = eᵢ(x),
eᵢ−eⱼ = xᵢ−xⱼ.
```

The balance and the local differences are **one relation**, not a later matching of independently chosen values by an outside agent. For two positions, write `d=x₁−x₂`:

```text
e₁=d/2,        e₂=−d/2,        e₁+e₂=0.
```

For `d≠0`, both contributions are nonzero. The total vanishes because of their common constitution; the difference is not erased by the total. This has the structural form sought in the SR analogy: given the constitution, no additional force makes the balance true.

The algebra alone does not establish that x, the index set, or d is actual, or that e is physical energy. It also does not show why there are exactly n positions, what they represent, or why this description is the actual one. A self-sufficient zero might ultimately ground all of that internally, but the calculation has not derived it from bare `0=0`.

### Why this centering is canonical under definite assumptions

Suppose a linear map `L: Rⁿ→Rⁿ` converts x into local contributions and satisfies:

1. Changing a common reference does not change the contributions: `L(x+c1)=Lx`.
2. Relabelling positions relabels the contributions: `L(Px)=P Lx` for every permutation P.

Permutation equivariance forces every diagonal matrix entry of L to be a common d and every off-diagonal entry to be a common o: permutations can carry any diagonal entry to any other and any ordered off-diagonal pair to any other. Common-shift invariance requires `d+(n−1)o=0`. Therefore

```text
L = α (I−J/n),       α=d−o,
(Lx)ᵢ = α(xᵢ−x̄),
```

where J is the all-ones matrix. Thus all such linear maps are the **same centered difference map up to one common scale**; their contributions automatically sum to zero. If the contribution scale is independently fixed so that local differences have their intended units and magnitude, α is fixed. If not, setting `α=1` is a normalization, not a physical discovery. The result does not assume a preferred position and does not require a separate balancing partner to be chosen.

Equal weighting is part of this particular symmetry. With independently fixed positive weights `wᵢ`, the analogous construction uses `x̄_w=Σwᵢxᵢ/Σwᵢ` and yields `Σwᵢ(xᵢ−x̄_w)=0`. It is covariant when the weights move with the labels, but **different weights give different local values**. If weights represent subject incidence or energy measure, the actual rule for them still needs to be derived or justified; our use of equal weights does not fix it.

## 3. A pointed whole: relabelling need not erase local difference

For the two-position case let `a=d/2` and let `p∈{0,1}` identify the currently considered local position in the representation. Define the local relational value

```text
v(a,p) = (−1)^p a.
```

Under a passive exchange of position labels, **both** the coordinate orientation and the pointed label change:

```text
(a,p) → (−a,1−p).
```

Then

```text
v(−a,1−p) = v(a,p),
v(a,0)+v(a,1)=0.
```

This resolves an apparent conflict. One need not choose an externally privileged label for the whole, yet a pointed relation can retain a definite positive or negative value. The label swap does **not** turn an already identified negative local value into a positive one, because the point being described is relabelled too. In contrast, flipping `a` while holding an independently fixed point unchanged is a different operation and may alter the physical relation; whether it is a symmetry of the actual whole must be argued separately.

There are two different pointed classes for nonzero a, distinguished by v. This does not mean two independent subjects have been derived: p is an index for a modeled local position, and neither a subject nor an experiential occurrence is supplied by that fact. It does show how **genuine local differentiation can be compatible with a zero total and passive relabelling**, without assuming that one subject's suffering disappears because a total balances.

The same distinction is important in the existing [gauge-constrained echo pair](ZERO_GAUGE_CONSTRAINED_ANGULAR_PAIR.md): its gauge constraint supplies opposite model observables on the physical sector, while the old K sign is itself a physical observable. This abstract relabelling exercise does **not** reclassify that K sign as gauge, derive the echo, or establish that its two constrained carrier factors are independent subjects.

## 4. The same structure as an experiential candidate

A stronger candidate now says: the **same pointed internal occurrence** described by `v(a,p)` has a real qualitative character, rather than generating another nonphysical object. In an intentionally restricted binary example, it might propose

```text
v>0: one designated positive contrast,
v<0: one designated negative contrast.
```

This is a noncausal identity proposal, not a conclusion of the preceding algebra. In particular, it does not say every physical sign is an experience, that opposite values are two independent subjects, or that positive character compensates the reality or moral importance of suffering. A first-person anchor is evidence *from within* reality, not an external substance supplying the quality.

Relabelling alone does not choose this proposed identification. On the same pointed physical description, `v`, `−v`, and the constant zero map are all invariant under the passive label swap. If positive, negative and neutral have independently fixed qualitative meanings, they are distinct proposed assignments for `a≠0`. If we instead rename the qualitative labels and transport every associated interpretation consistently, that is merely a change of description. The distinction parallels the earlier [coordinate-equivalence analysis](ZERO_SR_ECHO_COORDINATE_EQUIVALENCE_AND_CONTENT.md): a numerical difference need not be a difference in reality, but a genuine difference in lived quality cannot be made equivalent just by changing notation.

This is the remaining **identity selection** problem. The proposed fully intelligible constitution must explain why a particular subject's actual quality is the specific relational occurrence, and how that occurrence, its access, persistence and incidence belong together. Its answer need not be an outside psychophysical law or a process that produces an extra feeling. It must nevertheless do more than name one invariant numerical map “experience.” The recent [subject–quality–access circuit](CONSTITUTIVE_SUBJECT_QUALITY_ACCESS_CIRCUIT.md) exhibits why a physical output alone cannot establish its own experiential interpretation.

## 5. The important control: zero balance does not select every global quantity

The same two-position structure contains the nonnegative, reference-independent separation

```text
D = |x₁−x₂| = |e₁−e₂| = 2|a|.
```

It is unchanged by common shifts and by swapping labels. It is nonzero whenever the relational structure is nontrivial, even though `e₁+e₂=0`. It also has the same units as x: this is not just a trick involving a different dimensional quantity.

Therefore the assumptions “no absolute reference,” “no preferred label” and “the whole has internal differences” **do not alone imply that every intrinsic whole-level quantity vanishes**. A zero additive balance and a nonzero invariant spread are simultaneously determined by the same relative description. This is not a counterexample to the user's thesis: D is a *spread*, not an independently identified physical total energy, and the example does not establish a genuine self-sufficient alternative to the actual whole.

It does locate the decisive question: **why is the physically meaningful global energy the additive balanced quantity rather than D or some other invariant?** For a successful zero constitution, this selection could be intrinsic to the dynamics and symmetry; it must not be obtained merely by calling whichever quantity happens to sum to zero “total energy.” An intrinsic nonzero D also shows that a nonzero relational determination is not automatically an independently imposed number; the user's argument against an unexplained nonzero **whole-level energy** must be applied to that particular quantity rather than to every local difference.

A simple zero derived by subtracting the current mean is potentially a bookkeeping convention: *any* finite x has centered values. If the omitted common mode can independently gravitate or otherwise be measured, declaring it gauge discards physical information. If physical energy is additive, couples to gravity, has boundaries or vacuum terms, or is defined by a Hamiltonian generator, a real theory must establish how its physical quantity maps to this internal balance. Its defining reference and coupling cannot be fixed post hoc simply to make the answer zero.

## 6. Contact with physical energy

Two existing routes in the project are more physically specific than the abstract centering map:

- In the [closed FLRW model](ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md), a general-relativistic Hamiltonian constraint vanishes while positive matter energy density and relational evolution exist. It is not automatically a globally measured total gravitational energy.
- In the [Poincaré analysis](ZERO_LORENTZ_ENERGY_ZERO_WHY_CHAIN.md), an appropriately invariant ray in an honest representation of the full connected Poincaré group has vanishing generators, under its explicit assumptions. An actual global symmetry and the identification of its generator with the universe's energy remain to be shown. A spacetime can lack such global symmetry, and Lorentz invariance of a vacuum stress permits an unfixed scalar density.

Where a physical total four-momentum `P^μ` is well defined, saying its **energy is zero in every inertial frame** is stronger than saying energy is zero in one frame: it requires `P^μ=0`. It would still not imply that every local energy density or internal event vanishes. In a general cosmology, however, a global four-momentum or total energy is not guaranteed to exist in that form. The correct steelman is to derive the relevant quantity and the recovery map appropriate to the whole, not assume a particular formula applies everywhere.

The centering theorem and these physical results thus occupy different levels. Bringing them into one proof requires showing why the **actual** gravitational/relational charge is the distinguished zero, how local dynamics and limits are recovered, and why the same underlying constitution has a specified experiential character. No outside cause is demanded, but these connections are not established by reusing the symbol zero.

The [constraint/reference recovery continuation](ZERO_ENERGY_CONSTRAINT_REFERENCE_AND_PHYSICAL_RECOVERY.md) tests this connection in an extended compact FLRW model: a compensated vacuum-term redistribution leaves the full action unchanged, an uncompensated shift changes gravity, and two exact zero-constraint solutions have different positive local and quasi-local energies. The later [intrinsic-identity relational gravity construction](ZERO_EXPERIENCE_INTRINSIC_IDENTITY_RELATIONAL_GRAVITY.md) puts the zero constraint, clock-relative field and candidate quality distinctions in one two-scalar model, and records the user's correction that brute fact and unresolved regress were introduced to rule them out, not to develop them as serious alternatives.

## 7. What would complete the common derivation?

A full-strength answer would show, from one motivated intrinsic principle rather than a catalogue of desired facts:

1. **Actuality and differentiation:** why the self-sufficient whole is actual and has its nontrivial relational organization, rather than assuming either an empty zero or a prepared state.
2. **Physical zero:** why its appropriate, physically defined total energy or more fundamental quantity is zero, including how local matter, gravity, boundaries and relational time are recovered.
3. **Specific experience:** why at least the actually known qualitative distinctions are the intrinsic character of particular occurrences—not a distinct ingredient added to them and not merely labels attached to their states.
4. **Subject and incidence:** why the relevant local occurrences belong to particular subjects and how their persistence, plurality and measure are fixed; no inference of a universal subject or independent subjects from tensor factors alone.
5. **No residue:** why the domain, scale, admissible transformations and physical–experiential relations are themselves intrinsic rather than an independent unexplained selection.

None of these obligations says that real internal differences are objectionable, or that acquaintance needs an external witness. Nor is failure of the present finite model a proof that the project cannot succeed. It is a sharpened program: derive a **single** nature that determines both zero balance and real, specifically differentiated experience, while preserving the first-person datum and successful physics.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=verification:. python -m unittest \
 verification.zero_intrinsic_difference_common_constitution_test \
 verification.zero_gauge_angular_pair_test \
 verification.zero_poincare_energy_why_test -v
```

The new checks verify finite shift/permutation covariance, weighted-centering dependence, the stated class of linear maps, pointed relabelling and nonzero reference-free spread. They do not establish physical cosmic energy, subjective identity, actual subjecthood or full intelligibility.
