# Physical dynamics for the incidence–probability bridge

## What this continuation accomplishes

The previous [clock–incidence bridge](ZERO_TOTALITY_CLOCK_INCIDENCE_PROBABILITY_BRIDGE.md) introduced a signed current `J` and positive incidence current `K`, but did not construct them dynamically. Here we build both from a single concrete physical system: **two oppositely charged, conserved fluid populations interacting with an electric field**. This is a restricted fixed-background, nonrelativistic plasma model—not emergent spacetime, gravity, a brain, or a physical theory of experience.

The construction yields nontrivial evolving local signed contributions, a positive matter-number current and zero total charge under periodic Gauss law. It also yields an explicit transport equation for the proposed valence per incidence. A numerical evolution checks the equations and shows that the fraction of negative-valued *local-mixture incidences* can change even while their signed total remains zero.

The main new obstruction is equally important: **the same physical fluid configuration supports different incidence and valence interpretations with different probabilities.** Dynamics of charged matter alone does not tell us which, if either, is experience. The charge-to-valence and subject-incidence identities remain substantive hypotheses, as does the relation to physical energy and the self-subsistent zero whole.

## 1. One physical source for both currents

Take a periodic one-dimensional spatial domain `0≤x<2π`, in fixed Minkowski spacetime, with unit transverse area. Let `n_±(t,x)>0` be Eulerian number densities, `u_±` their velocities, `±q` their charges, `m` their equal mass and `E(t,x)` the longitudinal electric field. In units with permittivity and the speed of light set to one, consider the nonrelativistic cold-fluid equations

```text
∂t n_± + ∂x(n_± u_±) = 0,
∂t u_± + u_± ∂x u_± = ±(q/m) E,
∂x E = ρ = q(n_+ − n_−),
∂t E = −j = −q(n_+u_+ − n_−u_−).
```

These are the longitudinal electrostatic sector of Maxwell theory coupled to classical cold fluids in a fixed background, using nonrelativistic fluid momentum equations. They have no pressure, collisions, pair creation or gravity. Continuity preserves Gauss law if it holds initially. Periodicity forces the integrated charge to vanish:

```text
∫ ρ dx = ∫ ∂x E dx = 0.
```

Define the signed and positive currents

```text
J = (ρ, j),
K = (N, k) = (n_+ + n_−, n_+u_+ + n_−u_−).
```

Both satisfy continuity in the continuum. Their common physical origin is now explicit; `K` is a positive **matter-number** current, not yet a subject current. At sampled endpoints in the numerical run below, both species have positive densities and small speeds. Within such a subluminal regime the corresponding four-current sum is future directed, but the equations as used are not a fully covariant relativistic fluid theory and endpoint checks do not prove bounds at all intermediate times.

The local candidate from the preceding report, with the selected effective clock `T=t`, is

```text
v = α ρ/N = α q (n_+ − n_−)/(n_+ + n_−),
dμ = N dx dt.
```

It is bounded by `|v|≤αq` whenever both species' densities are nonnegative. If, and only if, `N dx dt` correctly counts actual experiential incidence, this ratio is independently established as the valence of that incidence, and the relevant domain is complete, the signed experiential total is

```text
Q_X = ∫∫ v dμ = α∫dt ∫dx ρ = 0.
```

Here the support condition is satisfied algebraically: positive species densities imply `N>0` wherever `ρ` is nonzero. But that is support on **charged matter**, not established support on experience. A nonexperiencing plasma cannot be transformed into genuine subjects merely by naming `N` an incidence measure.

## 2. A new local evolution law

The two continuity equations imply, wherever `N>0`,

```text
N(∂t + (k/N)∂x)v = −∂x(αj − vk).
```

This follows from `∂t(Nv)+∂x(αj)=0` and `∂tN+∂xk=0`. The left side follows the number-current flow; the right side is the divergence of signed charge flow relative to that flow. Thus, under the proposed experiential identity, local valence can change through redistribution of positive and negative contributions, while the whole signed flux remains zero.

This is a potentially falsifiable **structural prediction of this model**, not a general law of feeling. It rules out spontaneous local valence change when that relative-flux divergence vanishes, unless additional sources or physics are added. In the real world, valence plausibly depends on organization and dynamics beyond charge density, so this simple mapping faces a high empirical and constitutive bar. Its sign also reverses under charge conjugation, even though no evidence establishes that a change of charge sign reverses felt pleasure and pain.

For the separate simple special case of uniform background density `n_+=n_-=n₀` and small perturbations, linearization gives a plasma oscillation with

```text
ω_p² = 2q²n₀/m,
δρ(x,t) = δρ(x,0) cos(ω_p t)
```

for initially stationary fluids and compatible initial electric field. This is a real physical prediction of the stipulated fluid equations, not an experiential prediction. A small-amplitude numerical control reproduces `cos(√2)` at `t=1` for `q=m=n₀=1`.

## 3. Actual finite dynamical calculation

Choose in dimensionless units `q=m=α=1`, initial velocities zero and

```text
b(x) = 1 + 0.5 cos(2x),
n_±(0,x) = b(x) ± 0.05 cos(2x),
ρ(0,x) = 0.1 cos(2x).
```

The initial electric field satisfies periodic Gauss law. The effective local-mixture incidence measure has density `N=2b`; its valence is `v=ρ/N`. Under a *separately stipulated* self-location rule proportional to `N`, its initial negative-valence incidence probability is exactly

```text
P(v<0) = 1/2 − 1/(2π) ≈ 0.340845.
```

For a numerical continuation through `t=1`, fourth-order periodic centered differences and RK4 were used. The discrete initial electric field satisfies the **discrete** Gauss law, and the same derivative is used in continuity and Ampère equations. At the two reported endpoints densities are positive and speeds are small; nothing here establishes global regularity, positivity between sampled endpoints, or a late-time solution.

| Grid | `P(v<0)` initially, interpolated | `P(v<0)` at `t=1`, interpolated | Final Gauss RMS | Final valence-transport residual RMS |
|---:|---:|---:|---:|---:|
| 64 | 0.341355 | 0.436769 | `5.91e−16` | `2.27e−6` |
| 128 | 0.340973 | 0.438094 | `8.73e−16` | `1.63e−7` |
| 256 | 0.340877 | 0.438343 | `1.76e−15` | `1.06e−8` |
| 512 | 0.340853 | 0.438409 | `2.73e−15` | `6.68e−10` |

The negative fraction uses piecewise-linear reconstruction of density and sign crossings; its convergence is not fourth order, and the value near `0.4384` is a finite-grid estimate, not an exact result. The un-interpolated sign-cell estimates vary more; the [receipt](verification/two_fluid_incidence_receipt.json) contains both. Near-zero Gauss residual follows the matched discrete conservation structure and is not by itself a continuum-accuracy proof. The transport residual falls roughly fourth order; a smooth weighted-current diagnostic and the finite-time energy drift show compatible convergence across these grids. The evidence is for this short, smooth, fixed-background numerical test only.

For the 512-grid run, initial and final signed totals are approximately `−5.45e−17` and `+1.69e−16`, and the incidence integral is `4π` at both endpoints. Initial versus final maximum sampled species speeds are `0` and `0.03565`; the smallest sampled endpoint density is about `0.4500` initially and `0.4716` finally. The positive electrostatic-plus-kinetic energy per unit transverse area is approximately `0.003927`; the calculation **does not have or establish zero total physical energy**, and omits rest energy and gravity.

## 4. The decisive ambiguity: local mixture or individual carriers?

The same fields support two importantly different hypotheses:

- **Mixture-valued incidence:** assign the same local value `v=αρ/N` to each unit of `N dx` at that position. Under the stipulated incidence-weighted sampling rule, the initial negative fraction is about `34.1%`, and the finite-grid estimate at `t=1` is about `43.84%`. Both positive and negative carrier matter at a location are assigned the *same local mixture value*. This is what the preceding calculation actually means.
- **Carrier-valued incidence:** if each positive carrier has `v=+αq` and each negative carrier has `v=−αq`, the number of each carrier species is conserved and equal here. Under the same per-carrier counting assumption, the negative fraction is **50% throughout**, although their spatial distributions evolve.

In both cases the signed total is `α∫ρ dx=0`. For a local mixture, its signed value is the average of those carrier values, but **a negative local average does not mean every underlying contribution is negative**. Treating that average as the actual valence of every subject is an extra, demanding experiential hypothesis. It could also hide simultaneous positive and negative facets if the physical system actually supports separate experiences. Coarse-graining and actual subject unity therefore cannot be chosen merely to produce a desired probability.

This is not a choice resolved by mathematics alone. We need a principled account of which organization constitutes a single subject and what its experienced valence is. Neither charge sign nor particle density has been shown to be sufficient.

## 5. What the result means for the broader programme

This test turns the previous ratio from a freely specified pair of functions into a relationship between two currents derived from a familiar interacting matter model. It also exposes precisely where the hard step remains: the physical current is electric charge; the positive current counts fluid particles; and the choice of an experiential mapping changes the probability even though both mathematical totals are zero.

A genuinely integrated next theory needs to derive physical/experiential organization and incidence—not assume that electrically charged particles are subjects—and connect it to gravity, emergent spacetime, a justified relational clock, quantum statistics and the whole's physical-energy accounting. The present model does none of that. Its fixed-background positive energy and zero charge demonstrate why **energy, charge and experience cannot be equated merely because one quantity balances**.

The desired no-residue account must ultimately explain the laws, the clock, actual plurality, physical–experiential identity and probability measure from the whole's self-subsistent constitution. This calculation narrows the task and gives checks that a future account must meet; it does not settle whether that full derivation has been achieved. It does not require an external agent, a cosmic subject, or literal simulations.

## Reproduction and checks

NumPy is required for this numerical test. With NumPy available:

```text
python -m verification.two_fluid_incidence_dynamics --grids 64 128 256 512 --end 1
python -m unittest verification.two_fluid_incidence_dynamics_test verification.zero_incidence_clock_probability_test -v
```

The tests cover initial discrete Gauss law and the analytical initial probability, conservation and positivity at the endpoints, distinct mixture/carrier incidence rules, convergence diagnostics, charge-conjugation covariance of the evolution equations, the small-amplitude plasma mode, and invalid inputs. They are regression checks of a specified model, not validation of actual experiences or ultimate self-subsistence.
