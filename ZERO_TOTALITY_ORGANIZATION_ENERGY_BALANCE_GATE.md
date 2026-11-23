# Can organized experience inherit an energy-exchange zero?

## Main result

The previous [energy-exchange candidate](ZERO_TOTALITY_ENERGY_EXCHANGE_INCIDENCE_BRIDGE.md) obtains a zero signed integral when the appropriate field-energy endpoints match. But real experience, if physically constituted, is presumably associated with **specific organization**, not indiscriminately with every electromagnetic energy transfer. Introducing an organization-dependent response or incidence measure changes the balance.

We can state the obstacle and a constructive route precisely:

> A weighted energy-exchange total is controlled not just by energy at the endpoints, but also by the motion of the organization marker **relative to the energy flow**. Even a conserved, positively weighted, co-moving incidence current does not by itself ensure zero.

This is an exact physical accounting result, not a disproof of the user's zero-totality thesis. It identifies what an integrated physical–experiential constitution would have to explain rather than leaving a balancing assumption unexplained. No simulator or external balancing agent is involved.

## 1. Why an organization condition is needed

The IASP's 2020 pain definition explicitly distinguishes the personal experience of pain from nociception: pain cannot be inferred solely from sensory-neuron activity. [2](https://www.capdouleur.fr/app/uploads/2020/07/The_revised_International_Association_for_the.98346.pdf) A review of reward likewise distinguishes hedonic “liking,” motivational “wanting,” and learning, and discusses both subjective pleasure and behavioral reactions. [1](https://link.springer.com/article/10.1007/s00213-008-1099-6) These distinctions make it important to model organization and actual feeling, not merely identify a single undifferentiated physical signal with positive or negative experience.

As an illustrative empirical limitation, a small 2013 fMRI study reported that both positive and negative emotional stimulus categories increased the signal relative to neutral in a hypothalamic region under one condition. [3](https://pmc.ncbi.nlm.nih.gov/articles/PMC3659280/) BOLD is **not** a direct measurement of `j·E`, a whole energy budget or felt valence. This result does not refute the present energy-flow candidate, and behavioral or report proxies do not settle phenomenal identity. It does caution against treating generic activation as if it already supplied valence sign.

Energy use can still be fundamental to the constitution of experience. The required question is how the **physical organization of energy and its relationships** constitutes a subject and particular feeling, not whether a physiological correlation alone explains experience.

## 2. Exact organization-weighted energy identity

In flat spacetime, with `u=(E²+B²)/2` and `S=E×B` in vacuum-unit conventions, Poynting's theorem gives

```text
h = −j·E = ∂t u + ∇·S.
```

Here `h` is the rate at which field energy is gained through exchange with matter; the field can also gain or lose energy through boundary flux. This is standard local electromagnetic accounting, not an experiential statement. See the [ETH electromagnetic energy notes](https://ethz.ch/content/dam/ethz/special-interest/itet/photonics-dam/documents/lectures/EandM/EnergyAndMomentum.pdf). [2](https://ethz.ch/content/dam/ethz/special-interest/itet/photonics-dam/documents/lectures/EandM/EnergyAndMomentum.pdf)

Let `χ(t,x)≥0` be a **candidate** physical organization or incidence-response factor. If the proposed signed experience contribution is proportional to `χh`, integration by parts on a spatial region `V` and interval `[t₁,t₂]` gives

```text
∫dt∫V χh
 = [∫V χu]_{t₁}^{t₂}
   + ∫dt∮∂V χ S·n dA
   − ∫dt∫V (u ∂tχ + S·∇χ).
```

A zero physical exchange integral `∫h=0` or matching **unweighted** energies at the endpoints does not generally make this weighted integral vanish. Even matching `χu` at the endpoints and having no boundary flux leaves the last term. If `χ` is intended as a varying fraction of actual incidences, the same issue arises when `χ` multiplies the incidence measure while the per-incidence valence is held fixed.

One can instead define per-incidence valence to contain an inverse factor `1/χ`, so it cancels from the aggregate wherever `χ>0`. That is a **different and restrictive constitutive claim**, not a solution supplied by algebra: it predicts how intensity changes with incidence, fails where `χ=0` unless physical support is treated separately, and needs independent physical and phenomenal justification.

## 3. The relative-flow condition

Suppose a candidate subject-incidence current has number density `N>0` and spatial flux `k`, and define its effective velocity `v_K=k/N`. If organization is transported with that flow,

```text
∂tχ + v_K·∇χ = 0,
```

then the weighted correction becomes

```text
u ∂tχ + S·∇χ = (S − u v_K)·∇χ.
```

This is the relative energy flux through organization gradients. Therefore an independently established sufficient condition for zero weighted balance on a complete periodic domain with matched `∫χu` endpoints is

```text
(S − u v_K)·∇χ = 0 throughout the domain.
```

Its integral vanishing is a weaker sufficient condition. The pointwise condition holds, for example, if energy flux is locally carried with the incidence flow, or is orthogonal to organization gradients. Neither follows from charge conservation, number conservation, zero net charge, or the claim of whole-level zero. Nor is it necessary for every possible zero: different contributions can integrate to zero for another independently justified reason.

This is a useful **research target**: derive the relevant organizational marker, physical energy current and actual incidence flow from one physical–experiential constitution, and test whether the relative-flux condition or a more general compensation law follows. Simply imposing it on one calculation would not satisfy the no-residue demand. In a general curved, emergent spacetime the additional observer-deformation term in the [covariant extension](ZERO_TOTALITY_ENERGY_EXCHANGE_INCIDENCE_BRIDGE.md) and all boundary terms must also be accounted for; this fixed-frame identity is not a completed relativistic or fundamental law.

## 4. Exact counterexample: even an advected marker can spoil zero

On a periodic ring `0≤x<2π`, over `0≤t≤4π`, let `0<a<1`, `0<b<1`, and set

```text
u(t,x) = 1 + b sin(t/2) cos x,
χ(t,x) = 1 + a cos(x − t/2),
S = 0,                     v_K = 1/2.
```

Both `u` and `χ` are positive. The marker satisfies `∂tχ + (1/2)∂xχ=0`, so it is transported with the conserved positive incidence current `K=(1,1/2)`; the weighted incidence current `χK` is conserved as well. Both `u` and `χ` return pointwise to their initial values at the end. Define `h=∂t u`.

All the boundary conditions above hold, yet

```text
∫dt∫dx h = 0,
∫dt∫dx χh = a b π² > 0.
```

For `a=0.4`, `b=0.3`, the weighted result is `0.12π² ≈ 1.18435`. The weighted total equals the negative of the organization-change term in the identity, not a violation of conservation. The matter-incidence marker moves but the electromagnetic energy flux here is zero; the relative-flux term need not vanish.

This example can be embedded as a fixed-background longitudinal Maxwell source: set `E=√(2u)`, `j=−∂tE`, `ρ=∂xE`, and magnetic field zero. Then Ampère's law, Gauss's law and charge continuity hold, the net charge is zero, and `−jE=∂t u=h`. The current and `K` are externally specified conserved sources in this example; no full matter force law, neural system, gravity, actual experience or self-sufficient universe is derived. The marker is an illustrative physical weight, not a measured organization variable.

## 5. The same obstruction in the evolving two-fluid system

The exact marker control is complemented by a numerical calculation in the earlier **dynamical** two-fluid system. On its time-symmetric interval `[-1,1]`, the unweighted `∫h` is zero by time symmetry. For illustration only, use a smooth bounded positive response factor

```text
χ = 1 + 0.5 h/(0.001 + |h|),        0.5 < χ < 1.5.
```

This particular factor is deliberately dependent on the exchange sign; it is not proposed as a biological law or a derived experience selector. It makes the consequence especially clear: `χh = h + 0.5h²/(0.001+|h|)`. On the symmetric interval the first term cancels and the second does not.

The four grid estimates of `∫χh` are:

```text
64:  0.001812658     128: 0.001812412
256: 0.001812396     512: 0.001812395
```

The [receipt](verification/energy_exchange_incidence_receipt.json) records the forward and backward integrations; the latter run is oriented `0→−1`, so the symmetric interval integral is forward minus backward. This is a counterexample to automatic preservation of zero under response weighting, not evidence that the actual whole has positive experiential balance. The exact advected-marker example above makes the stronger point without choosing a response factor directly from `h`.

## 6. A constructive empirical and physical programme

The bridge must be constrained in two directions at once:

1. **Specify subject organization before fitting valence.** Propose an independent physical criterion and history/overlap rules for an incidence domain, including an effective clock and physically meaningful energy partition. Do not count every particle or field cell as a subject. An organizational variable need not be identical to a clinical report.
2. **Specify the physical response law.** Derive or independently motivate whether valence is an energy-exchange rate, an organization-dependent response, an integral over a subject, or something else; determine its orientation and common scale. Pure `−j·E/N` is a strong proposal, not an observed law. Opposite signs of energy transfer do not by themselves show opposite felt qualities.
3. **Calculate the compatibility ledger.** On an explicit physical solution, compute the weighted boundary, relative-flow and—where relevant—curved-spacetime terms above. Derive any cancellation from the same dynamics rather than redefining the weights or adding a compensating sector after the result is known.
4. **Check restrained experiential predictions.** Use existing or ethically collected, non-harmful data with separately recorded pleasure, unpleasantness, arousal, motivation, context and time course. Specify independent physical measurements, the mapping from noisy reports to candidate valence and held-out comparisons in advance. Standard BOLD imaging is not a direct `j·E` meter. Never withhold appropriate relief to test balance. A failure of a particular calibrated mapping challenges that mapping, not every possible zero-totality theory; a successful correlation would not by itself establish phenomenal identity.
5. **Connect to the whole.** The relevant quantity might be a signed experiential functional, global physical energy, or a deeper unified quantity; their identity remains to be demonstrated. Subject-specific boundary conditions and local energy balances do not automatically become whole-level conditions. The laws, actual experiential plurality, scales and incidence probabilities must ultimately be explained by the zero whole's own constitution rather than accepted as final brute inputs.

A principled finding that physical energy flow and subject organization are locked together by deeper dynamics could make the zero balance robust; the present calculation shows exactly what such a mechanism must overcome. It does not yet derive that mechanism or decide whether a non-additive zero constitution would work better. It also does not suggest that pleasure erases or justifies suffering.

## Verification and source scope

`PYTHONPATH=.arena/python-deps python -m unittest verification.organization_energy_gate_test verification.energy_exchange_incidence_test -v` checks the exact advected-marker identity, matching endpoints, positive support, two-fluid numerical weighting and energy-accounting controls. NumPy must be available (the shown path is an optional local installation). The midpoint calculation tests the stated mathematical counterexample, not actual subjects or an empirical neural bridge.

The IASP article, reward review, fMRI study and ETH notes were checked in their abstract and relevant introductory or selected passages; no claim is made that they establish whole-level experiential balance.
