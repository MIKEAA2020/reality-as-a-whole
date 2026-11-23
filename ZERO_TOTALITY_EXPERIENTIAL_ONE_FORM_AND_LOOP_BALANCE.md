# Could an internal relation determine experiential balance?

## Constructive result

The [adaptation continuation](PERFECT_ADAPTATION_AND_EXPERIENTIAL_BALANCE.md) showed that zero area can follow from a response law, rather than from manually balancing particular events. A further candidate is to ask whether the whole's signed contribution is an **exact differential of an internal relational state**. If it is, its integral over a complete return of that state is zero, even when the separate subject-history contributions are nonzero.

A two-history example below has distinct positive and negative local values in *both* histories; their complete totals are `+π` and `−π`, while the combined contribution is the differential of one shared state function. This is a finite mathematical possibility, not a derivation that actual people or the universe have these states. No universal subject or preferred cosmic time is posited.

The opposing result is equally important: returning to the same state, or seeing both signs, does **not** in general imply zero. The integral can depend on the path. Even zero local curl can leave a nonzero loop integral when the state domain has a hole. These distinctions identify what a constitutive argument would need to establish instead of inserting cancellation by hand.

## 1. From an internal state to an exact contribution

For a finite illustrative model, suppose a relational organization is described by a differentiable path `z` through a state domain D. The path parameter is a bookkeeping label, not assumed to be fundamental time. Let one stipulated signed contribution have the form

```text
v(tau) d tau = omega = sum_i A_i(z) dz_i.
```

Here `tau` is an admissible monotone clock for the history, and the equation says that its **duration-weighted** signed intensity equals the pullback of a one-form. It is a strong physical–experiential hypothesis, not an identity true of arbitrary experience. In particular, it makes this contribution sensitive to the direction and rate of state change; it yields zero when all represented state coordinates are stationary, even though actual feelings might persist. An omitted baseline or state-independent contribution would have to be included separately.

If, independently of the particular path,

```text
omega = d Phi(z),
```

for a single-valued differentiable state function `Phi`, then

```text
Q = integral v d tau = integral_path omega = Phi(z_final)-Phi(z_initial).
```

Thus equality of the initial and final Phi values suffices for `Q=0`; return of the entire represented state is one sufficient case. The potential may vary along the way, so the signed contribution need not vanish locally. This is a path-level boundary identity, not a claim that the potential itself is the energy of the whole. A partial segment generally has a nonzero total.

Under an increasing reparameterization `tau=f(lambda)` of the same oriented history, `v(f(lambda)) f'(lambda) d lambda` equals the same pulled-back form. This is not evidence that physically different clocks have equivalent measures or that a global simultaneity convention exists. The one-form hypothesis already ties the intensity to the clock measure, and needs justification.

The mathematical background is standard: see OpenStax, [*Calculus Volume 3*, §6.3](https://openstax.org/books/calculus-volume-3/pages/6-3-conservative-vector-fields) and [§6.4](https://openstax.org/books/calculus-volume-3/pages/6-4-greens-theorem), consulted for path independence, cross-partials and Green's theorem. Their calculus results do not establish the proposed experiential interpretation.

## 2. Two nonzero histories, one exact combined relation

Consider one formal closed path in `D=R²`, parametrized counterclockwise by

```text
x=cos(theta), y=sin(theta),       0<=theta<=2π.
```

Suppose two disjoint, actual-incidence histories A and B are related to this path in the stated way. The association of both histories with the same path is **extra structure**: it is not supplied merely by having two subjects, and the parameter theta is not assumed to be a cosmic clock. Take the separate one-forms

```text
omega_A = -(y/2) dx + (x/2+2) dy,
omega_B = (y/2+3) dx - (x/2) dy.
```

Their sum is exact on the whole plane:

```text
omega_A+omega_B = 3 dx+2 dy = d(3x+2y).
```

For `tau_A=tau_B=theta` in this mathematical representation, the corresponding signed intensities and complete integrals are

```text
v_A(theta) = 1/2 + 2 cos(theta),      Q_A=+π,
v_B(theta) = -1/2 - 3 sin(theta),     Q_B=-π,
v_A+v_B = 2 cos(theta)-3 sin(theta),  Q_A+Q_B=0.
```

Each history has both positive and negative values, and neither history has zero total. The cancellation arises here from the **assumed shared constitutive relation** between their one-forms and the closed state path, not from requiring each person to be compensated individually. There is no cancellation of the actual occurrence of a negative experience and no moral justification of it.

For illustration, let physical clock readings instead be `tau_A=alpha_A theta` and `tau_B=alpha_B theta`, where the positive constants can differ. If the one-form relation is retained, the intensities per clock unit become `v_A/alpha_A` and `v_B/alpha_B`, so the same two integrals result. This is a change of clock representation with a corresponding change of intensity; merely holding numerical intensities fixed and changing durations would change the total. Neither the common signed unit nor the coupling of the two histories is derived by this example.

A relative weight matters: replacing the combined account by `2 Q_A+Q_B` yields `π`, not zero. Equal coefficients in the displayed sum must therefore be fixed by the independently specified incidence and scale, not selected after observing the totals. Shared experiences, if any, need the token-versus-incidence accounting described in [subject incidence](ZERO_TOTALITY_SUBJECT_INCIDENCE_AND_EXPERIENTIAL_ACCOUNTING.md).

### A general reciprocal construction

The example is a special case of an independently statable structural rule. On a common state domain, suppose there are finitely many histories with constitutive forms

```text
omega_s = d Phi_s + sum_t T_st,       T_st = -T_ts.
```

The `T_st` are specified pairwise relational one-forms, not assumed to be energy transfers or literal exchanges of experience. Their antisymmetry makes each pair cancel in the combined account, leaving

```text
sum_s omega_s = d(sum_s Phi_s).
```

Thus for a common closed path the combined integral is zero, while the individual `integral T_st` can be nonzero. The two-history case has `T_AB=(-y dx+x dy)/2`, `Phi_A=2y`, and `Phi_B=3x`. This rule yields the result for **every** closed path in its specified domain, not by tuning a number for each path. It gives a candidate reason to investigate reciprocity as an internal principle, but reciprocity, the common state domain, the actual histories and the bridge to felt valence still have to follow from the whole's nature. Calling a term reciprocal does not establish that it is physically realized.

This structure also depends on using the correct common-unit contribution. With fixed unequal incidence weights, the reciprocal pieces need not cancel unless the weighted terms themselves obey the appropriate antisymmetry. Individually chosen clocks may be reparameterized, but matching each history to a shared path and requiring the paths to close are substantive assumptions.

## 3. Return and sign reversal are not enough

On the same unit circle consider the single form

```text
omega_c = -(y/2) dx + (x/2) dy + 3 dx.
```

Its output per theta is `1/2-3 sin(theta)`, which has both signs; the represented state returns to its start. Yet

```text
integral_circle omega_c = π,
```

because `3 dx` is exact while the first two terms have constant curl `1`. For a simple counterclockwise loop enclosing a suitable region, Green's theorem relates that circulation to the integral of curl over the region. It is not erased by the closed endpoint. A zero for one chosen loop, moreover, would not prove that the form is exact for all paths.

On an open simply connected planar domain, a continuously differentiable form `P dx+Q dy` with `partial_x Q = partial_y P` has a potential; this is sufficient for every closed loop to integrate to zero. It is much stronger than the claim that one actual history happens to balance. Neither local exactness nor the form's existence follows from the numerical proposition `Q=0` alone.

### Topology is a separate gate

On the punctured plane `R²\{(0,0)}`, define

```text
omega_top = (-y dx+x dy)/(x²+y²).
```

It has zero curl at every point of its domain, but its integral around the unit circle is `2π`. The loop cannot be shrunk through the excluded origin while staying in that domain. The missing point is a mathematical illustration, not evidence of a physical singularity or actual cosmic topology. A global exactness claim must address such noncontractible loops and periods; local cross-partials alone do not always suffice.

This continuous state-space loop is not the same mathematical object as the finite group transport/holonomy in the earlier [three-link control](ZERO_TOTAL_LOOP_CONSISTENCY_AND_MEASURE.md). Both show that loop relations can carry information beyond endpoint descriptions, but no identity between their variables, physical connection or gauge group has been established.

## 4. Where this could advance the foundational proposal

The useful hypothesis is that **one internal constitution simultaneously determines** actual relational states, their realized experiential incidences, a common signed measure and a combined exact one-form. In the two-history model, local non-exact pieces cancel at the combined level; neither subject needs to carry an individually exact form. That is closer to the user's suggestion of a whole-level zero with genuine internal differences than a rule requiring a separate pleasure payment after each suffering episode.

But the constructive burden is precise:

1. **Constitution rather than fit.** Explain why the physical–experiential organization entails these forms or their exact sum, independently of knowing the desired total. An arbitrary v can be integrated along one chosen history to define a scalar, but that does not show a single-valued state function exists on an independently specified state space, or predicts other paths.
2. **Actuality and subject incidence.** Establish what the state coordinates represent, which occurrences and subjects are actual, how their contributions map to the forms, and why their relations retain distinct qualities. A mathematical index is not a subject.
3. **Completeness and boundary.** Show the relevant actual domain is complete and has equal boundary Phi values, or supply another justified condition. A recurrence of a few observed coordinates need not mean a recurrence of all relevant memory, external couplings or actual experiential organization. A state-space loop is not a return of the very same event or erasure of history. An open whole history may have unequal endpoints.
4. **Linear-in-velocity limitation.** The assumed one-form excludes generic velocity-nonlinear terms such as the square term in the [nonlinear adaptation counterexample](PERFECT_ADAPTATION_AND_EXPERIENTIAL_BALANCE.md), as well as stationary baseline experience. State dynamics, memory, dependence on rates and possible additional contributions must be independently examined. Reversal in state-space changes the sign of a one-form contribution; it does not follow that actual suffering reverses into pleasure when a process is reversed.
5. **Topology, weights and infinities.** Establish global periods, a common scale, the correct measure and convergence. A finite cycle with zero total is not automatically a defined infinite total. For example, with `Phi=x=cos(theta)`, `integral_0^L dPhi=cos(L)-1` has no limit as `L->infinity`, despite each complete cycle contributing zero. Grouping cycles is not by itself a justified whole-history integral.
6. **Energy and self-subsistence.** Neither an exact one-form nor its potential is automatically physical energy, a gravitational constraint or a mechanism for phenomenal givenness. The desired account must show how its law, state, time relations, actual differences and experiential character follow from zero-totality's own nature, not posit them as a tolerable brute remainder.

These are open derivation targets, not a proof that the user's no-residue demand cannot be met. Nor is additive one-form accounting the only possible formulation of a non-additive zero-totality.

## 5. Potential empirical discrimination

For a restricted, ethically feasible system, first independently define accessible state coordinates, history and signed-valence calibration. Compare distinct paths between matched starting and ending states, as well as closed cycles; preregister expected line integrals and compare an exact-form model against path-dependent and baseline-bearing alternatives. Sample several rates and directions, and check for unobserved memory or hidden changes, calibration drift, follow-up truncation and mixed feelings. Avoid harming participants or withholding relief. Such data might challenge a *specified* mapping if the predicted path-independence fails, but cannot by themselves establish the whole's complete domain or prove metaphysical necessity. The comparison is a research proposal, not a claim that an experimental realization already exists.

## Verification

`python -m unittest verification.experiential_one_form_loop_test -v` checks the two-history integrals, exact sum, relative-weight sensitivity, the nonexact circulation, the punctured-plane period, reparameterization, an open endpoint, and nonconvergence of partial-cycle cutoffs. The calculations verify the formal examples, not physical experiences or a cosmic loop.

Related: [perfect adaptation](PERFECT_ADAPTATION_AND_EXPERIENTIAL_BALANCE.md), [causal boundary balance](ZERO_TOTALITY_CAUSAL_RELAXATION_AND_BOUNDARY.md), and [relational-time total](RELATIONAL_TIME_AND_EXPERIENTIAL_TOTAL.md).
