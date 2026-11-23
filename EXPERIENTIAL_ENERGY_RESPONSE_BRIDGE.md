# A candidate bridge from energy differences to signed experience

## Proposal and result

The [normalized-response candidate](EXPERIENTIAL_SCORE_INVARIANT_CANDIDATE.md) left its variation unspecified. A more definite **conditional** bridge is to take a familiar energy-dependent statistical family and ask whether its normalized response could also be an experiential contribution:

> In a specified physical organization, the signed experiential contribution of an occurrence is the negative of its energy's deviation from the internally weighted mean, divided by the corresponding energy standard deviation.

If the relevant weights are normalized, this proposed contribution has zero weighted mean and unit weighted square. Local energy values can all be positive while the contributions have both signs. Thus the proposal avoids the obstruction to simply identifying signed experience with nonnegative local matter energy. It does so by relating experience to **relative energy**, not by proving that physical energy and experience are identical or that the universe's global energy is zero.

The proposed experiential identification is an extra hypothesis: a low-energy state is not known to be pleasant, a high-energy state is not known to be suffering, and a probability of a physical state is not automatically a measure of actual experience. The finite canonical ensemble below is a concrete physical **analogy and conditional mathematical model**, not a theory of the universe or a completed self-subsistent constitution.

## 1. Derivation from a specified energy-dependent distribution

Consider finitely many indexed configurations with real energies `E_i`, and assume the same fixed energies as `beta` varies. Suppose their distribution has the canonical form

```text
p_i(beta) = exp(-beta E_i) / Z(beta),
Z(beta) = sum_j exp(-beta E_j).
```

For a physical thermal canonical ensemble `beta=1/(k_B T)` with positive temperature, under its usual equilibrium assumptions. Here beta is a parameter of comparison, not an external time. Actual thermal systems have conditions and environments that must be specified; this finite example does not imply that the universe as a whole is a canonical ensemble or has an external heat bath.

Set `mu=sum_i p_i E_i` and `sigma^2=sum_i p_i (E_i-mu)^2`. Differentiating yields

```text
s_i = d log(p_i)/d beta = -(E_i-mu),
I   = sum_i p_i s_i^2 = sigma^2.
```

When `sigma>0`, the normalized response is therefore

```text
u_i = -(E_i-mu)/sigma,
sum_i p_i u_i = 0,
sum_i p_i u_i^2 = 1.
```

The conditional **experiential hypothesis** is that these same `u_i` are signed felt contributions, with positive u pleasant and negative u suffering, and that the same `p_i` correctly weights their actual incidence. Under that identity hypothesis, the weighted experiential mean is zero. If a finite total incidence measure is `M>0` with weights `M p_i`, the corresponding sum is also zero. Neither the phenomenal identity nor that incidence measure follows from the canonical calculation.

A mixed occurrence might contain separately represented positive and negative components; a net u alone would not capture both. Neutral experience can be represented at `E_i=mu`, but `u_i=0` does not constitute an experience. Subject boundaries and which configurations have experiences must be fixed independently of these equations.

## 2. Exact example: positive energies, signed response

Use a unit in which

```text
E = (1,2,3),                 beta = ln(2),
p = (4/7, 2/7, 1/7),       mu = 11/7,
sigma^2 = 26/49,
s = (4/7,-3/7,-10/7),      u = (4,-3,-10)/sqrt(26).
```

All three stipulated energies are positive. The weighted response has total zero, but no permutation of the three raw response values reverses their signs: a pointwise opposite counterpart is unnecessary. The mean energy is positive, `11/7`; this is not a zero-energy universe example. The finite checks use exact rational arithmetic for p, mu, sigma squared and s, and floating-point calculations only for the canonical exponential and normalized square root.

The example also makes a sharp distinction: a negative response means that, holding the energy spectrum fixed, that configuration's probability decreases as beta increases. Whether it is actually associated with a negative experience is a **separate empirical and constitutional question**. The response's sign never makes a subject's suffering nonexistent or morally erased.

## 3. What is and is not invariant

For this fixed non-gravitational canonical family, a common shift `E'_i=E_i+C` leaves p, `E_i-mu`, sigma and u unchanged at the same beta; the mean energy shifts by C. A uniform positive rescaling `E'_i=a E_i`, accompanied by `beta'=beta/a`, also leaves p and u unchanged. This makes the candidate sensitive to **relative** energies rather than the chosen common energy origin or units.

These transformations are algebraic properties of the specified canonical probabilities, not a general assertion that absolute energy is physically irrelevant: shifts of the energy or vacuum term can have gravitational significance. Nor is sigma a local object in this finite model: it depends on the whole distribution. Its status as an intrinsic feature, and its interpretation in a larger or gravitationally constrained system, would need to be explained. At `sigma=0`, u is undefined, not evidence that experience is absent.

Swapping the orientation of the parameter changes the sign of the normalized score. Choosing positive u as pleasure and negative u as suffering is therefore an oriented identification, not a result of the mathematical normalization. A physical definition of beta provides an orientation for this model, but it does not provide a reason why that orientation has the proposed phenomenal meaning.

## 4. A real physical hypothesis, and its nontrivial risks

If the same stated energy family and orientation were independently identified with experiential intensity, this candidate would make stronger claims than merely `sum p_i u_i=0`:

- For that same distribution, if `E_i<E_j`, then `u_i>u_j`; equally energetic configurations have the same predicted scalar u. Thus, if a defensible independent phenomenal measure established different signed values for two configurations of identical E in the stipulated domain, the exact identification would fail.
- At a fixed configuration i across a change of beta, both mu and sigma can change. The model predicts its new u from the *full* distribution, not just its energy. It makes no general claim that a particular configuration's u increases monotonically with beta.
- A well-defined configuration above mu has negative u. If independently established as purely positive in the sense the model intends, it is a counterexample to this version. Unknown or noisy reports, changed subject identity and invalid ensemble assumptions must not be treated as such decisive evidence without analysis.

These consequences can in principle distinguish the proposed mapping from an arbitrary fitted post-hoc zero. They are not evidence that it is true. In actual physical and biological systems, the energy level alone generally does not determine phenomenal valence: the same broad physical energy can be compatible with many organizational and contextual differences. The candidate's simple identification is deliberately strong and could fail while a more general energy–experience constitution remains possible.

To investigate ethically, one could first specify a restricted system, physical state partition, energy model, equilibrium conditions and beta; independently collect non-harmful experiential reports or other predeclared proxies; and compare the predicted ordering and relative responses against competing mappings on held-out observations. Reports and proxies have noise, depend on interpretation, and do not directly reveal another subject's qualitative state. Do not change the energy definition, domain or weights to secure the target balance after inspecting results. A failed fit rejects the specified mapping under the maintained measurement and model assumptions, not the zero-totality thesis as a whole; a good fit is not proof of phenomenal identity or metaphysical necessity.

## 5. A mean over alternatives is not automatically the actual total

The canonical p_i ordinarily describes the probabilities of alternative microstates in a specified ensemble. Its zero weighted mean is an ensemble identity. It does **not** show that all alternatives are actually experienced, that individual occurrences are weighted by p_i, or that a finite realized history has exactly the expected proportions. For example, if the stipulated system occurs only once and occupies state 1, the realized score is positive, not zero; its expected score over alternatives is zero.

A defensible whole-history inference would require independent justification that the actual experiential incidence measure really is the same p (up to an overall positive factor), for the relevant whole and domain. An infinite collection introduces further questions of normalizability, convergence, physical clock relations and measure; an average, an infinite total and cancellation of divergent positive/negative parts are not equivalent. No fundamental foliation is assumed or derived.

## 6. Does this bridge the two global zeros?

No. Algebraically,

```text
sum_i p_i u_i = 0      but      sum_i p_i E_i = mu,
```

and mu can be nonzero, as in the example. The vanishing response is generated by **centering relative to the same distribution**; it is not a Hamiltonian, gravitational or cosmological energy constraint. A gravitational, boundary or other term could enter a more complete physical account, but cannot be added solely as `-mu` and counted as an explanation without an independently specified principle and physical meaning.

This result does not deny the user's stronger idea that everything is energy in a global, objective sense or that an energy-based formulation might be fundamental. It identifies what this particular attempted bridge achieves and what it does not: a relationship between signed relative energy and a candidate signed experiential quantity, not their global identity. A substantive account would have to derive the physical quantity and relevant constraints, the experiential mapping, actual subject incidence and the appropriate whole-level measure from the same constitution.

The underlying normalized-response identity already allows any zero-mean signed vector to be represented by a suitable formal tangent. Here the canonical family selects a tangent **if its energies and beta are independently specified**. If instead the energies are reverse-engineered from desired experiential scores, the proposal merely repackages the desired balance. For uniform weights at beta zero, any zero-mean score can be reproduced by setting `E_i=C-s_i`; the zero does not, by itself, select this energy spectrum.

## 7. Foundational status and next task

The positive candidate is more explicit than a generic analogy: a single fixed energy-dependent organization gives a definite common relative scale and a zero weighted signed response, without forcing nonnegative energies to be signed. Its conditional predictions make clear what could count against this particular mapping.

But no proof here derives the canonical ensemble, physical energies, parameter, phenomenal identity, subject plurality, incidence measure or actual zero-totality from zero itself. These may ultimately be unified by a self-subsistent constitution, but merely writing the identities does not establish that unity. Equally, failure of this simple thermal bridge would not establish that no zero-residue experiential constitution is possible. The next task is to investigate whether a more general, relationally defined energy–experience mapping can avoid making phenomenal character depend solely on a single energy level, while still giving independent, non-fitted implications.

## Verification

`python -m unittest verification.experiential_energy_response_test -v` checks the canonical score derivation numerically, the exact rational example, transformation invariance, zero variance, the difference between expectation and a single realized occurrence, and reconstruction of a balanced score at uniform weights. The tests do not establish actual experiences, the universe's physical energy or self-subsistence.

Related: [normalized experiential response](EXPERIENTIAL_SCORE_INVARIANT_CANDIDATE.md), [the previous energy obstruction](EXPERIENTIAL_ZERO_CANDIDATE_AND_ENERGY_BRIDGE.md), and [FLRW energy and constraint](ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md).
