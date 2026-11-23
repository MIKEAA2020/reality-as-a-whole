# Evolving the coupled zero-charge gravity and clock candidate

## Result

I evolved the [previously constructed Einstein–gauge–matter–clock initial data](ZERO_TOTALITY_COVARIANT_GAUGE_CLOCK_FRAMEWORK.md) rather than stopping at their constraints. In a declared planar-symmetry reduction, the **nonlinear classical field equations** produce changing local charge density and changing geometry. The integrated gauge charge stays numerically near zero, while the Hamiltonian, momentum and Gauss constraint residuals decrease by approximately a factor of 16 when the spatial grid is doubled.

The local scalar clock remains timelike at every sampled grid point and time in the run. At a symmetry-marked location, the proper charge density changes from `+1` to approximately `−0.568` while the local clock reading advances from `0` to about `1.788`. This is calculated field dynamics, not a claim that anyone experiences these values.

A second comparison follows the same marked location to the **same scalar-clock reading**, `T=1`. In the gravitating run its proper charge density is about `0.0831`; in a fixed-metric, `κ=0` decoupling control it is about `0.2132`. This is a concrete difference in the specified model, including the different constraint-compatible initial extrinsic curvatures. It is not an experimental prediction for our universe, or evidence that the valence hypothesis is true.

The computation is a bounded classical numerical investigation, not a derivation of the underlying action from zero or a solution of all physics. The important progress is that the candidate now has a nontrivial **coupled evolution**, independently checked constraints and a clock-relative comparison, not merely a static example.

## 1. Model and reduction

The underlying covariant action and its exact initial data are specified in [the candidate](ZERO_TOTALITY_COVARIANT_GAUGE_CLOCK_FRAMEWORK.md): Einstein gravity, a massless charged real doublet χ, an Abelian gauge field and a free scalar clock T. Here we take its particular `L=2π`, `e=1`, `m=0` data and `κ=0.02`, in normalized illustrative units. The initial geometry is intrinsically flat with nonzero constant extrinsic curvature; it is **not** flat spacetime with its matter stress ignored. We choose the expanding sign `K=-sqrt(15κ/2)`.

For this run use the symmetry-reduced metric

```text
ds² = -dt² + exp(2u(t,x)) dx² + exp(2v(t,x))(dy²+dz²),
K^x_x=k_x,       K^y_y=K^z_z=k_y,
```

with periodic x and all fields independent of y,z. The gauge potential and electric-field density have only x-components; the magnetic field vanishes in this sector. We use unit lapse, zero shift and `A₀=0` as **coordinate/gauge choices** in the effective covariant theory. The scalar T is evolved as matter and used below as a clock. This is not a claim that the universe has a fundamental preferred foliation. The symmetry reduction excludes general three-dimensional perturbations and gravitational-wave polarizations.

Define `a=exp(u)`, `b=exp(v)`, `V_s=a b²` and `D_x χ=∂_xχ-A_x Jχ`, with `J(χ₁,χ₂)=(-χ₂,χ₁)`. For these conventions, the evolution includes

```text
u_dot=-k_x,                       v_dot=-k_y,
χ_dot=π/V_s,                      π_dot=D_x[(b²/a) D_xχ],
A_x_dot=(a/b²) E,                 E_dot=(b²/a)(D_xχ)·Jχ,
T_dot=p_T/V_s,                    (p_T)_dot=∂_x[(b²/a) T_x],
(T_x)_dot=∂_x(p_T/V_s).
```

The last equation evolves the clock gradient alongside T. Their discrete derivative mismatch is measured as an additional numerical check. Here `E` is the canonical field density, and the local charge density in these coordinates is `q=π·Jχ`. Charge conservation follows from the continuum equations; the discretization need not satisfy every continuum product identity exactly.

For reproducibility, define

```text
P = (|π|²+p_T²)/V_s²,
G = (|D_xχ|²+T_x²)/a²,
E_p² = (E/b²)²,
energy_density = (P+G+E_p²)/2,
S_x = (P+G-E_p²)/2,
S_y = (P-G+E_p²)/2,       S = S_x+2S_y.
```

The mixed spatial Ricci components and ADM evolution in this reduction are

```text
R_x = -2/a² [v_xx+v_x²-u_x v_x],
R_y = -1/a² [v_xx+2v_x²-u_x v_x],
K = k_x+2k_y,
(k_x)_dot = R_x+K k_x - κ[S_x-(S-energy_density)/2],
(k_y)_dot = R_y+K k_y - κ[S_y-(S-energy_density)/2].
```

These are the stated unit-lapse ADM equations, not a new law deduced from zero. For standard ADM constraints and their propagation, I consulted the relevant abstract and selected introductory sections of Shinkai, [*Formulations of the Einstein equations for numerical simulations*](https://arxiv.org/html/0805.0068), arXiv:0805.0068, and the [Gourgoulhon 3+1 notes](https://arxiv.org/abs/gr-qc/0703035); the complete references were not independently audited.

## 2. Constraints and method

For every grid point we monitor

```text
H = R_x+2R_y+K²-k_x²-2k_y² - 2κ energy_density,
M_x = 2 v_x(k_x-k_y)-2 (k_y)_x
      + κ[π·D_xχ+p_T T_x]/V_s,
G_Gauss = ∂_x E-q.
```

These are respectively the geometric Hamiltonian constraint, the nontrivial momentum constraint in the selected sign convention, and the gauge constraint. A vanishing H is not automatically an observable total physical energy. The whole gauge charge is the volume integral of q and is distinct from both H and an independently defined experiential-history total.

The implementation uses periodic **fourth-order centered finite differences** in x and fourth-order Runge–Kutta time stepping, with `dt` chosen from `0.1 dx`. The fields χ and π, geometry, clock, gauge potential and electric density evolve together. It is a free-evolution check: constraints are monitored, not projected back to zero after every step. The scheme uses ordinary finite differences rather than exact lattice-gauge links, so discrete gauge symmetry and the continuum product rule are not exact; their violations must converge away. The direct continuum identities and the exact initial solution are given in the prior report.

At `t=1`, in the same normalized units, the root-mean-square residuals are:

| Grid points | Hamiltonian | Momentum | Gauss |
|---:|---:|---:|---:|
| 64 | `1.193e-6` | `5.239e-7` | `4.282e-5` |
| 128 | `7.559e-8` | `3.331e-8` | `2.704e-6` |
| 256 | `4.742e-9` | `2.091e-9` | `1.694e-7` |

The ratios are roughly 16, consistent with fourth-order convergence over this range. At 256 points, the largest absolute *whole* charge sampled over all time steps is `4.22e-14` in the selected units. The minimum of the clock timelike margin `(p_T/V_s)²-(T_x/a)²`, sampled over all grid points and time steps, remains about `1.333`. These are numerical observations at finite resolution, not proofs of continuum error bounds or of behavior between samples. The initial finite-difference residuals are also nonzero, even though the continuum initial constraints hold exactly.

At the symmetry-marked `x=0` location, the normal-frame charge density `q/V_s` and transverse area factor `exp(2v)` change as follows at 256 points:

```text
initial: T=0,        q/V_s=+1,          exp(2v)=1,
t=1:     T≈1.78778,  q/V_s≈-0.567757,  exp(2v)≈1.244467.
```

The marker is the reflection-symmetric plane selected at the initial time and followed by the chosen normal-coordinate congruence; its positive initial charge distinguishes it from the other reflection plane. It is a useful relational diagnostic, not yet a fully constructed Dirac observable in the unreduced theory. The normal-frame density is the current contracted with the normal to the chosen slices and generally changes with that normal; it is not a fully foliation-invariant scalar specified by the matter alone. A physical experiential proposal would need an independently defined congruence or a covariant replacement. The change in sign is a property of the physical charge model. Interpreting it as pleasantness or suffering additionally requires the unestablished experiential bridge.

## 3. Same clock, gravity versus a control

To avoid comparing only the same coordinate time, the code evolves each case until the scalar clock at the marked location reaches `T=1`. It brackets the crossing and uses fractional RK4 substeps, rather than simply assigning the same t in both runs. At 256 grid points:

| Case | coordinate time at T=1 | proper charge density at marker | transverse area factor |
|---|---:|---:|---:|
| coupled gravity, `κ=0.02` | `0.524066` | `0.083064` | `1.131183` |
| `κ=0` fixed-metric limit | `0.478459` | `0.213242` | `1.000000` |

In both cases the same matter, gauge and clock initial fields and initial spatial metric are used. The gravitational case has the nonzero initial extrinsic curvature required by its constraint; the decoupled limit has zero initial extrinsic curvature and fixed metric. The difference is therefore the effect of the **whole declared comparison**, including that initial expansion and subsequent gravitational evolution—not an isolated measurement of a single causal mechanism. The `κ=0` system is a mathematical fixed-background limit, not another solution of finite-κ Einstein gravity. Parameters are illustrative and not fitted to observations.

As a narrow clock/gauge control, repeating the same evolution with constant lapse `2` for half the coordinate interval gives the same numerical field arrays as lapse `1`, up to roundoff. The implementation also recovers the known homogeneous flat-FLRW massless-scalar solution in a separate test. These are meaningful checks, but constant-lapse rescaling is much weaker than proving equivalence under arbitrary spacetime slicings or solving the quantum problem of time.

## 4. What the result does—and does not—advance

The **physical part** has moved beyond the initial-data construction: in the specified effective equations, real local matter and geometry change while the whole gauge charge remains neutral and the classical constraints converge under refinement. This realizes a concrete version of internal difference with global zero, without assuming an external timekeeper or a cosmic subject. It also supplies a calculated gravity-versus-fixed-background distinction at equal internal clock reading.

The main outstanding steps remain substantive:

- **Actual experience:** the candidate `v_X=α rho_u` is still a hypothesis. A classical gauge charge is not automatically felt valence, and the model has not identified actual subjects or their boundaries. Conservation imposes the regional flux condition discussed in the earlier report; it needs an independently calibrated, physically measurable bridge.
- **Which whole-level zero:** a zero gauge charge and a gravitational Hamiltonian constraint are not automatically the universe's total energy or the integral over all actual experience. The clock-measure and lapse-weighting distinction remains.
- **Physical and observational fit:** planar symmetry, chosen compact topology, the hidden field and its parameters are assumptions. No coupling to Standard Model matter, measured phenomenology, quantum theory, gravitational-wave recovery, cosmological constraints or realistic laboratory system has yet been established.
- **Full self-subsistence:** this effective action, its parameters, the actual initial data, its clock and the experiential identity are not derived from zero's own nature. They are not accepted as a final brute remainder; they are the next derivation targets. We do not reopen the user's settled case against infinity.
- **Numerics:** this is short-time free evolution with standard ADM in a restricted sector. No long-time stability, general three-dimensional well-posedness, continuum convergence theorem, full independent GR solver comparison or global existence is claimed. The present tests are not evidence of a new physical field.

## Reproduction

Run

```text
python verification/evolve_covariant_zero_initial_data.py --grids 64 128 256 --end 1 --clock-target 1
python -m unittest verification.covariant_zero_evolution_test -v
```

The [receipt](verification/covariant_zero_evolution_receipt.json) records the first run. The tests cover constraint convergence, evolving charge and clock, a uniform-lapse comparison, the homogeneous FLRW control and the matched-clock fixed-metric comparison. They test this implementation and stated regime; they do not certify the fundamental framework or the phenomenological bridge.

Related: [covariant gauge and clock candidate](ZERO_TOTALITY_COVARIANT_GAUGE_CLOCK_FRAMEWORK.md), [prior homogeneous FLRW control](ZERO_TOTALITY_FLRW_CONSTRAINT_AND_ENERGY.md), and [relational experiential total](RELATIONAL_TIME_AND_EXPERIENTIAL_TOTAL.md).
