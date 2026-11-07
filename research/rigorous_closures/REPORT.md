# Step 42 — Which explanatory debts can actually be closed?

## Direct answer and scope

Three **conditional mathematical subdebts** can be closed rigorously now:

1. the SR rod-length relation used in the analogy;
2. normalized finite perspective weighting and its invariance under mere re-presentation or measure-preserving refinement;
3. the exact condition under which a qualitative assignment depends only on a realized organizational type, rather than on an additional material tag.

These are ordinary mathematical results, not new physics or a discovered consciousness theory. Their proofs close the specified conditional questions. They do not establish the physical–phenomenal identity, the actual perspective measure, or the existence of alternative conscious realizations.

Some other claims can be shown **not to follow from the supplied premises**. Diagnosing an invalid inference is not paying the underlying explanatory debt. The main constitutive and ultimate debts remain open.

## 1. Closed conditionally: the SR geometric calculation

### Given

A rod is at rest in an inertial frame, with stable endpoint worldlines x=0 and x=L₀, L₀>0. Assume the Lorentz transformation, with c=1:

\[
x'=\gamma(x-\beta t),\qquad t'=\gamma(t-\beta x),
\quad |\beta|<1,\quad\gamma=(1-\beta^2)^{-1/2}.
\]

### Proposition

The endpoint separation measured using events simultaneous in the primed frame is L′=L₀/γ.

### Proof

For the two selected endpoint events, Δx=L₀. Primed simultaneity gives

\[
0=\Delta t'=\gamma(\Delta t-\beta L_0),
\quad\text{so}\quad\Delta t=\beta L_0.
\]

Hence

\[
\Delta x'=\gamma(L_0-\beta\Delta t)
=\gamma L_0(1-\beta^2)=L_0/\gamma.
\]

The same transformation preserves Δt²−Δx², by direct expansion. No separate compression force is needed for this comparison. For β=3/5, γ=5/4, and L₀=10, the measured length is exactly 8. ∎

### What is paid

The dependence of the compared coordinate lengths on simultaneity convention and the given geometry is derived, not simply asserted. This provides a concrete example of explanatory work without an additional causal force between two independent quantities.

### What is not paid

The actual world's Lorentzian structure, the existence and dynamics of stable matter, and a constitutive relation to experience are not derived. A physical acceleration is not a coordinate transformation. The analogy does not establish a phenomenal geometry or prove that all reality has no brute residue.

**Status:** the geometric subproblem is closed under explicit physical assumptions; the psychophysical analogy remains a research template.

## 2. Closed conditionally: finite perspective-weighting arithmetic

### Given

A finite domain Ω of already justified actual perspective tokens or observer-moments, with:

- type τᵢ for each i∈Ω;
- nonnegative weights wᵢ;
- evidence likelihoods ℓᵢ=Pr(D|i) in [0,1];
- an adopted sampling interpretation with prior Pr(i)=wᵢ/∑wⱼ;
- positive evidence mass Z=∑wᵢℓᵢ>0.

The reference domain, token identities, weights, and evidence model are **inputs**. The theorem does not supply a phenomenal sensor or justify a sampling principle for our actual self-location.

### Proposition

For a type T,

\[
\Pr(T\mid D)=\frac{\sum_{i:\tau_i=T}w_i\ell_i}
{\sum_iw_i\ell_i}.
\]

### Proof

Bayes' rule gives Pr(i|D)=wᵢℓᵢ/Z after canceling the common prior normalizer. Summing over the type-T atoms gives the result. Nonnegativity and Z>0 make it a valid probability; summing over an exhaustive disjoint type partition gives 1. ∎

### Invariance results

The formula is unchanged by:

1. **common weight rescaling:** wᵢ↦cwᵢ, c>0, because numerator and denominator both scale by c;
2. **bijective re-presentation:** renaming token identifiers and transporting their attributes leaves both sums unchanged;
3. **measure-preserving refinement:** replacing one atom by subatoms of the same type and likelihood with weights summing to its weight preserves both sums.

The third claim concerns a mathematical refinement of the same measure. It does not assert that physically producing more genuine subjects leaves the measure unchanged. If new tokens, types, likelihoods, or total weights change, the posterior can change. A repeated description of one token cannot silently be counted as another token; the domain identity must be settled upstream.

### Dominance theorem

Write A for evidence-weighted mass of T and B for that of its complement. Then

\[
\Pr(T\mid D)>1/2\quad\Longleftrightarrow\quad A>B,
\]

since A+B>0. Thus dominance is evidence-conditioned measure dominance, not raw program-count dominance.

For example, raw type weight 100 with evidence likelihood 1/10000 has evidence mass 1/100, while another type of weight 1 and likelihood 1 has mass 1. The abundant type then has posterior exactly 1/101. ∎

Raw counting is recovered only under further assumptions such as equal unit weights and a specified evidence-compatible domain. Independence of the tokens is not a substitute for a justified sampling rule.

### What is paid

Normalization, conditional dominance, and protection against inflation by purely representational changes are established once the domain, measure, and evidence rule are supplied.

### What is not paid

Which perspectives exist, how they are individuated, which reference domain applies, why these weights are appropriate, and whether the adopted self-locating probability rule is justified remain open. Infinite domains and quantum histories require additional treatment; this finite classical theorem does not automatically settle their measures.

**Status:** accounting is closed conditionally; the constitutive and measure-selection debts are not.

## 3. Closed as an equivalence theorem: organizational sufficiency is factorization

### Given

A domain R of candidate concrete realizations, a declared organization map O:R→K, and a qualitative assignment E:R→Q. These maps are mathematical inputs, not measured consciousness data.

### Proposition

There exists a map χ:O(R)→Q such that

\[
E=\chi\circ O
\]

if and only if E is constant on every fiber of O:

\[
O(r)=O(s)\quad\Longrightarrow\quad E(r)=E(s).
\]

Where it exists, χ is unique on O(R), though not necessarily on uninstantiated organizational types outside that image.

### Proof

If E=χ∘O, equal O-values have equal E-values by function application. Conversely, if E is constant on each fiber, define χ(k)=E(r) for any r with O(r)=k. Fiber constancy makes the definition independent of the chosen r. Every k in O(R) has such an r, and the equality E(r)=χ(O(r)) follows. Uniqueness holds because each such k has a realizing r. ∎

### Consequence for the substrate argument

If organizational sufficiency holds, two actual realizations with the same O cannot differ phenomenally merely because an additional material tag differs. This is compatible with the requirement that O be concretely instantiated.

The theorem therefore closes a logical point: **requiring actual realization does not itself contradict cross-material organizational sufficiency.** A supplied model with two differently tagged realizations, equal O, and equal E is a logical compatibility witness for those formal conditions.

It does not prove that two actual materials can instantiate the relevant O, that the chosen O is complete, or that E genuinely factors through it in nature. Material differences may change O or expose its inadequacy. The theorem states exactly what organizational sufficiency means and how a specified counterexample would defeat it.

If E describes only a content contrast, the theorem concerns only that contrast. It does not derive episode incidence or subject identity from content invariance. Those targets must be included and justified separately.

**Status:** the relation between sufficiency and substrate neutrality is mathematically settled; whether its premises hold for consciousness is not.

## 4. Rigorously diagnosed, not closed: consistency does not supply actuality

A simple model-theoretic point blocks an inference in the transcript. Let a language describe structures but leave the predicate Actual unconstrained. Take a model with two distinct named candidates a and b. Expand the same underlying model once with Actual={a} and once with Actual={b}. Every sentence of the original language has the same truth value in both expansions, but Actual(a) differs.

Therefore those structural premises alone do not entail which candidate is actual. Adding only “exactly one is actual” does not select between these expansions. The missing actuality constraint has not been derived.

This does not prove that no possible constitutive theory can explain actuality, or that actuality must be an independently primitive predicate in the true ontology. A successful theory might justify a much stronger principle. The point is that the transcript has not supplied it.

Likewise, adding an unconstrained Good predicate does not identify normative goodness with consistency. A named equality or actualization law would be another premise requiring justification, not a consequence of the present structural axioms.

**Status:** the proposed inference is insufficient; the actualizing/axiarchic debt remains unpaid.

## 5. The central debts I cannot rigorously close from the present material

| Debt | Why the current results do not pay it |
|---|---|
| Why an organization is experienced | A functional architecture and an identity assertion do not establish phenomenal sufficiency |
| Why this qualitative character | Neither the integration proxy nor global availability selects a warranted χ |
| Which contents form one episode | No independently justified Γ or co-presentation relation has been supplied |
| Whether the whole is one subject | One reality, holism, and mathematical globality do not establish phenomenal unity |
| How a cosmic subject differentiates into finite subjects | No non-brute decombination law is present; “dissociation” remains a placeholder |
| Which substrates can realize experience | The constitutive basis is not yet known, so material relevance cannot be settled universally |
| Which perspective measure is actual | The weighting theorem requires the measure and justified domain as inputs |
| Whether time or process is fundamental | The order/metric bridges and temporal obstructions are conditional, not an ultimate ontology |
| Why coherence/Good yields this reality | No actualization principle, unique selection, or warranted normative identity is demonstrated |
| Why the foundation itself is intelligible | Calling it necessary or self-grounding does not provide the required explanation |

These are not merely missing test cases in the new code. They require additional physical, phenomenal, or metaphysical premises and warrant. It would be misleading to claim they were closed by increasing a software test count.

## 6. Verification and integration

`model.py` uses exact rational arithmetic for checks of Lorentz transformations and finite weighting, and checks supplied maps for fiber constancy. Sixteen tests cover rod measurements, interval invariance, simultaneity, normalization inputs, posterior invariances and refinements, evidence-conditioned dominance, and successful/failed factorization. `enumeration.json` records exact witnesses.

The general proofs above are the basis for closure. The finite tests check the implementation and examples; they do not prove that the inputs describe actual consciousness, nor do they establish new foundational physics.

**Final assessment:** I can close the specified mathematical relations and conditional accounting rules. I can identify where some proposed deductions fail. I cannot honestly close the transcript's central physical–phenomenal, subject-composition, or ultimate-foundation debts from the present premises.
