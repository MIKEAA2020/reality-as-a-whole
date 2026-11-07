# A second-order gravity–matter obstruction on the torus

**Result.** The time-symmetric TT-like witness used in [the linearized lattice test](LINEARIZED_LOCAL_GRAVITY_RECORDS.md) has a specific continuum analogue that fails a necessary nonlinear vacuum constraint: its integrated second-order Hamiltonian constraint is strictly positive. No smooth second-order metric correction can remove that zero mode. Adding a massless scalar increases the obstruction. In a different first-order family, a homogeneous trace momentum can balance both contributions; an explicit inhomogeneous second-order correction then solves the **local classical constraints through second order**.

This is an illustrative calculation in standard continuum general relativity, not an exact solution, a discrete refinement, a detector model or a solution of time. The general existence of this compact-background obstruction is established work, notably [Brill and Deser](https://doi.org/10.1007/BF01645610); the purpose here is to calculate it for the previous witness and test a coupled matter correction. We make no claim of research priority for the construction.

A second, distinct result is that the previous fixed-coordinate curvature record fails a nonlinear gauge test: translating the coordinate point changes it, even though it commuted with the linearized constraints. Merely including matter energy does not repair that relational-localization problem.

## 1. Setup and order conventions

Use the continuum three-torus `0 <= x,y,z < 2pi`, flat background metric, zero background momentum and a free massless scalar with zero background value and momentum. Set `16 pi G = 1`, with canonical momentum density `pi^ij` and scalar momentum density `P`. The ADM constraints are

    H = (pi^ij pi_ij - 1/2 pi²)/sqrt(g) - sqrt(g) R[g]
        + P²/(2 sqrt(g)) + sqrt(g) g^ij partial_i phi partial_j phi /2,
    D_i = -2 partial_j(g_ik pi^kj) + pi^jk partial_i g_jk
          + P partial_i phi.

Indices on momenta in H are lowered with g. The sign of the linear scalar constraint here is opposite to the `H_s` convention in the previous lattice report; its zero set is the same. There is no cosmological constant. The calculation concerns initial-data constraints; no time evolution is assumed.

Write formal fields as `g=delta+epsilon h+epsilon² k+...`, `pi=epsilon p+...`, and `phi=epsilon varphi+...`. No factorial is included in the epsilon² coefficient. The previously used continuum analogue is

    h_xy=h_yx=cos(z),   all other h_ij=0,   p=0,   varphi=P=0.

This first-order data obeys the linearized constraints. Its discrete counterpart was tested at finite n in the earlier note; here we analyze the **continuum analogue**, not a claimed nonlinear completion of that lattice.

## 2. Explicit obstruction

For a correction-free metric `g=delta+epsilon h`, the second-order scalar curvature is

    R^(2) = (3/2) sin²(z) - 2 cos²(z).

Thus, at second order in epsilon,

    H^(2) = 2 cos²(z) - (3/2) sin²(z) + H^(1)[k]
    <H^(2)> = 1/4.

Angle brackets denote the normalized spatial average. `H^(1)[k]` is a sum of spatial derivatives, so its integral vanishes for **any smooth periodic second-order correction k**. The first-order gravitational momentum vanishes, so second-order momentum corrections cannot contribute to the quadratic kinetic term at this order. Consequently `1/4=0` is impossible: there is no smooth one-parameter family of exact vacuum initial data with precisely this first-order tangent. This is stronger than saying we have not found one.

The obstruction is due to this compact, symmetric background and chosen tangent; it is not a universal statement that nonzero gravitational waves cannot exist. In particular, permitting a nonzero homogeneous first-order trace momentum changes the tangent and can cancel the charge. On asymptotically flat space, boundary contributions and allowed perturbations differ.

## 3. An explicit scalar-coupled, second-order candidate

Change the first-order data by introducing a homogeneous gravitational momentum and a scalar profile:

    p^ij = alpha delta^ij,
    varphi = beta cos(z),      P = 0,
    k_ij = u(z) delta_ij,
    u(z) = (7-beta²) cos(2z)/32,

and take the second-order momentum and scalar-momentum coefficients to be zero. Real alpha and beta are constants. The momentum is a **density** in the coordinate system used here. It has a nonzero trace; at first order the mean curvature is `K = -3 epsilon alpha/2` in the displayed ADM convention. This family therefore is not a continuation of the previous time-symmetric tangent.

The local second-order Hamiltonian coefficient is

    H^(2)(z) = 2 cos²(z) - (3/2) sin²(z)
               - (3/2) alpha² + (beta²/2) sin²(z) + 2 u''(z).

Its normalized spatial average is

    <H^(2)> = 1/4 + beta²/4 - 3 alpha²/2.

The scalar's gradient energy contributes `beta²/4`. The negative term is the gravitational trace-momentum contribution to the indefinite ADM kinetic form; it is not negative-energy scalar matter. The necessary global balance is

    alpha² = (1+beta²)/6.

With that choice, the displayed `u(z)` removes the remaining `cos(2z)` term, so `H^(2)(z)=0` pointwise. The exact rational checker also verifies all three momentum constraints vanish through order epsilon². The first-order constraints vanish as well. Both signs of alpha give a formal branch. Setting beta to zero leaves a vacuum example with modified homogeneous momentum; setting alpha to zero leaves an unavoidable positive obstruction.

This is more than balancing integrated energies, but less than constructing a full nonlinear solution: we have not shown the order-three and higher constraints are solvable, established an exact one-parameter family, solved the evolution equations, or quantized the model. The scalar is a matter field, **not a detector, memory, or operational clock**. Its coupling is standard minimal coupling, not an apparatus action. The homogeneous expansion variable is supplied initial data, not an external clock for the absolute.

## 4. Why the earlier local record does not yet survive nonlinear gauge symmetry

For the first-order TT metric the previously measured spatial curvature component has continuum value

    R_xzyz(z) = epsilon cos(z)/2 + O(epsilon²).

Take an active spatial diffeomorphism generated by the constant vector `xi = epsilon eta partial_z`. For a constant translation the tensor indices do not rotate, and the coordinate component transforms by its Lie derivative. Consequently

    delta R_xzyz(z_0) = -epsilon² eta sin(z_0)/2 + O(epsilon³).

At `z_0=pi/2`, this is nonzero. On the compact torus the translation is connected to the identity and is generated by the full momentum constraint. Its *linearized* smeared generator vanishes for constant xi, but its next-order generator acts nontrivially on the linearized field. Therefore a fixed-coordinate `R_xzyz(z_0)` is not established as a Dirac observable of the nonlinear system, even though its first-order curvature was invariant under the linearized constraints.

For the former external pointer coupling `exp(-i g R(z_0) P_pointer)`, a gauge-inert pointer at a fixed coordinate does not cancel this variation. The resulting gauge defect is already visible in the classical generator; no conclusion about complete quantum instruments or backreacting detector dynamics follows. A relationally located detector would need a transforming physical reference system, and a complete analysis must include its constraints and stress energy. For established approaches to relative observables see [Brunetti, Fredenhagen and Rejzner](https://arxiv.org/abs/1306.1058); for dressing and locality difficulties see [Donnelly and Giddings](https://arxiv.org/abs/1607.01025). We have not implemented either construction here.

## 5. Verification and scope

Run `python verification/torus_gravity_second_order.py`. [The verifier](verification/torus_gravity_second_order.py) expands the metric inverse, Christoffel symbols, Ricci tensor and scalar curvature through degree two in epsilon using rational polynomial arithmetic. It cross-checks the resulting curvature against a separate two-torus-slicing formula, reduces `cos²+sin²=1`, computes the exact torus average, checks the Hamiltonian after the balance condition, and checks each momentum constraint. It also checks the derivative underlying the translation example. Output is recorded in [verification/torus_gravity_second_order.json](verification/torus_gravity_second_order.json).

The curvature computation is a reproducible algebraic check, not a literature survey or independent computer-algebra proof. The general statement that *arbitrary* periodic second-order corrections cannot alter the zero mode follows analytically from the integrated linear constraint, not from sampling corrections in the code. The program does not construct full solutions, gravitational hypersurface-deformation brackets, physical Hilbert spaces, finite-lattice refinement, or measurement records.

## 6. Consequence for the programme

The subsequent [relational matter detector calculation](RELATIONAL_MATTER_DETECTOR_GRAVITY.md) provides a covariant clock–rod–signal–detector action, a different backreacting background, exact small-amplitude initial-data existence, and a short-time classical response. It does not yet provide a retained record or test the discrete deformation algebra.

1. The previous first-order witness must not be advertised as a nonlinear vacuum state. Its continuum analogue is **ruled out as a smooth exact-vacuum tangent** by the computed zero-mode obstruction.
2. Coupled matter and global gravitational modes cannot be treated independently in a closed universe: in this chosen family the scalar energy changes the required gravitational trace momentum. This is standard constraint physics, now exhibited for the particular test.
3. Linearized gauge invariance and commuting pointer couplings do not establish nonlinear physical observables; a reference system and its gravitational contribution are needed.
4. The next target is an action-based relational detector or clock in a setting with controlled boundaries, followed by the nonlinear bracket, integrability and instrument tests. The present scalar is not that detector. Full discrete gravity, refoliation, emergent spacetime, experience and the timeless absolute remain open.
