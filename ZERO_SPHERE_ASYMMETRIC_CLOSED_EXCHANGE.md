# A zero-balanced, asymmetrical history from closed dynamics

## Result

The user asks whether a zero whole can contain real local differentiation rather than mere absence. The previous closed-plasma calculation showed that a weighted response can fail to balance even when a physical system returns to its starting state. Here we construct the complementary case: **a completely specified, autonomous physical model whose signed exchange balances exactly, although negative values occur twice as often as positive values** under a stated incidence measure.

The result is stronger than simply picking two numbers that add to zero. Both signs, their durations and their unequal magnitudes arise from one closed Hamiltonian trajectory. Its two oscillator phases can also be represented on two internal `S²` state spheres. Its positive component and positive remainder exchange energy with no external forcing.

It remains a *conditional physical–experiential candidate*. The model's conserved total energy is positive, its selected period is not the whole of reality, its internal spheres are representations rather than a derivation from zero, and its degrees of freedom are not established subjects. No experimental prevalence of suffering is inferred.

## 1. One autonomous physical system

Consider two independent canonical oscillator modes, with coordinates and momenta `(q₁,p₁)` and `(q₂,p₂)`, and a time-independent Hamiltonian

```text
H = 1 + (p₁²+q₁²)/2 + (p₂²+4q₂²)/2.
```

Hamilton's equations give `q̇₁=p₁`, `ṗ₁=−q₁`, `q̇₂=p₂`, `ṗ₂=−4q₂`. With initial state `(q₁,p₁,q₂,p₂)=(0,1,0,2)`, the exact solution is

```text
q₁=sin t,  p₁=cos t,
q₂=sin 2t, p₂=2 cos 2t,
H=7/2.
```

The frequencies, initial phases and energy scale are chosen model inputs. This is a closed effective mechanical system, not a derivation of fundamental dynamics, gravity or cosmic zero energy. It needs no externally imposed driving.

## 2. A positive internal energy component

Define one joint component

```text
U = (2+q₁+q₂/2)²/8,     W = H−U.
```

`U≥0`. The complement `W` is also positive on the entire phase space, not merely on the chosen orbit. To check this without assuming it, write `q=(q₁,q₂)`, `p=(p₁,p₂)`,

```text
M = [  3/4  −1/8  ],       q₀ = (32/47, 4/47).
    [ −1/8  63/16 ]

W = (p₁²+p₂²)/2 + (q−q₀)ᵀ M (q−q₀)/2 + 15/47.
```

The leading diagonal `3/4` and determinant `47/16` are both positive, so `M` is positive definite and `W≥15/47`. The cross term in `W` is part of an interaction/partition; the sum `U+W` is the original autonomous Hamiltonian.

This is a mathematically consistent partition into positive energy functions, not proof that nature or a subject singles out this particular partition. The constants and the component are selected to provide a clean example; they are not derived from zero.

## 3. Local exchange and exact zero

On the chosen trajectory, let

```text
V(t) = 2 + sin t + (1/2)sin 2t,
U(t) = V(t)²/8,
h(t) = dU/dt = V(t)[cos t + cos 2t]/4.
```

`V(t)≥1/2`, so the sign of `h` is the sign of

```text
cos t + cos 2t = (2cos t−1)(cos t+1).
```

Except for isolated zeroes, `h>0` for one third of the cycle and `h<0` for two thirds. Specifically, `h<0` for `π/3<t<5π/3` except for the zero at `π`. Since `U(2π)=U(0)`,

```text
∫₀²π h(t)dt = U(2π)−U(0) = 0.
```

This is **zero net exchange** of the selected component over the selected cycle. The physical total `H=7/2` is not zero, and the equality is not by itself a claim about total reality.

The result contains more than an equal sign count. The positive part of the exchange is

```text
∫_(h>0) h dt = U(π/3)−U(5π/3) = 3√3/4,
∫_(h<0) h dt = −3√3/4.
```

Hence the mean positive rate during positive periods is twice the absolute mean negative rate during negative periods. A longer negative duration is exactly offset by a larger average positive magnitude, not by making the negative contribution nonexistent.

## 4. Conditional subject incidence: two thirds versus one third

Suppose—for this model only—that `N>0` is a constant density of actual incidences, the incidence measure is `dμ=N dt`, and the signed felt valence per incidence is `v=h/N`. Then

```text
Q = ∫ v dμ = ∫h dt = 0,
P(v<0) = 2/3,       P(v>0) = 1/3.
```

The corresponding conditional mean absolute magnitudes obey

```text
mean(v | v>0) = 2 mean(−v | v<0),
P(v>0) mean(v | v>0) = P(v<0) mean(−v | v<0).
```

The same factor `1/N` occurs in both means. This realization shows exactly how a suitable zero total can coexist with a majority of negative incidences *if* the proposed physical identity and counting rule hold. It does not establish those assumptions or assign a probability to actual human suffering. A nonuniform incidence measure, different subject clocks, multiple simultaneous facets or a different candidate valence would generally give different results.

In particular, this model does not turn a negative valence into absence: each negative entry is nonzero in the model, and the hypothetical experience would remain locally real. The mathematical compensation is a sum, not a claim that later positive feeling erases an earlier unpleasant episode.

## 5. The sphere and a relational clock

The normalized pairs

```text
n₁=(p₁,q₁,0),       n₂=(p₂/2,q₂,0)
```

are unit vectors along this trajectory, so they trace the equators of two `S²` spheres. The second phase makes two revolutions per first-mode revolution; their relative relation is internally available within the model. The chosen oscillator-time parameter can therefore be expressed locally in terms of the phase of one mode and the other mode compared to it.

This is a representation, not a derivation of two qubits, a Lorentzian spacetime, or experience from the user's zero point. A periodic phase cannot distinguish different cycles by itself: a global elapsed-time count requires further memory or clock structure. There is no assertion of fundamental external time or a preferred cosmic foliation, but this effective Hamiltonian model does assume a time parameter.

## 6. The decisive sign ambiguity

For the complementary positive component,

```text
W=H−U,      dW/dt=−h.
```

If one assigns valence from `dU/dt`, the negative fraction under the stipulated uniform measure is `2/3`. If one instead assigns it from `dW/dt`, it is `1/3`. Both components are nonnegative, both rates derive from the *same* dynamics, and both integrate to zero over the cycle.

Thus a real physical exchange cannot be identified with the sign of pleasure or suffering merely because it is an exchange. A constitutive account must explain why the subject is associated with one organization or direction, rather than silently select the sign yielding a desired result. This is a concrete version of the subject-frame and incidence problem; it is not proof that a physically justified selection is impossible.

There is a related arrow issue. The Hamiltonian laws are time-reversal invariant, but the selected coherent initial state is not invariant under time reversal. Reversing the trajectory changes the sign-duration pattern: the negative fraction for the same `U` becomes `1/3`. The asymmetry here is an initial-state property of the model, not an explanation of the arrow of time or a global preferred temporal direction.

Finally, the earlier [plasma incidence gate](ZERO_SPHERE_CLOSED_PLASMA_INCIDENCE_GATE.md) remains decisive: if real incidence or phenomenal response introduces an additional factor depending on the direction of the physical flow, the weighted history need not balance. This construction uses exactly `Nv=h`; choosing that identity to enforce zero would be circular. The intended theory must **derive** it, or derive a different physically justified cancellation, including its actual subjects and measure.

## 7. What this advances

The combined conclusion is precise:

* A closed physical dynamics can produce positive internal energy components, a zero signed exchange, and a two-to-one negative/positive duration asymmetry simultaneously.
* The detailed intensity distribution—not equal counts—makes this balance possible.
* The *same* whole dynamics permits an opposite signed assignment from the complementary component. Which, if either, is felt cannot be selected by the zero calculation.
* No conclusion about a globally zero physical or experiential quantity follows from a positive-energy oscillator and one completed cycle.

The next constitutive demand is to determine what selects the **subject-side component**, its actual incidence measure and the physical sign of real valence. Without that, even an exact balanced history is a structural possibility rather than the requested identity of physics and experience.

## Verification

```text
python -m verification.zero_sphere_asymmetric_closed_exchange --steps 256 1024 4096
python -m unittest verification.zero_sphere_asymmetric_closed_exchange_test -v
```

The sign fractions and signed integrals are derived analytically above; midpoint estimates approach them. At 4096 samples, the computed negative fraction is `0.66650390625` and the positive and negative integrals are approximately `±1.2990380207` versus exact `±3√3/4`. Tests also verify the positive-definite completion for the complement, total-energy constancy and sign reversal. These checks do not establish actual subjects or phenomenal valence.
