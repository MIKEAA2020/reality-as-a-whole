# Local constraints and recorded curvature in linearized lattice gravity

**Status:** a restricted, inhomogeneous **linearized** gravitational consistency and instrument construction. A simple periodic central-difference discretization of the standard linearized ADM constraints admits local linearized curvature observables and complete recorded measurements that preserve those constraints. This is a controlled intermediate test, **not** the promised full discrete-gravity construction, a derivation of the interacting Einstein constraint algebra, a relativistic local net, or a solution of the problem of time.

In particular, we do not claim this lattice is Regge calculus, that it follows from a discrete gravitational action, or that it recovers continuum dynamics. Its flat periodic background, lattice, reference coordinates, clock/readout schedule and pointer couplings are supplied. The intended absolute remains timeless and without fundamental spacetime.

## 1. Relation to existing work

The specific next target in [the cross-framework constraints note](CROSS_FRAMEWORK_GRAVITY_CONSTRAINTS.md) was a documented inhomogeneous discrete gravity theory with matter/records and a refinement test. We do **not** yet have that. Instead, the present calculation tests the smallest inhomogeneous interface before attempting the full target.

Standard ADM linearization yields the scalar and vector constraints used below; see [Contreras and Leal](https://arxiv.org/abs/1304.0778). Linearized gravitational curvature is a standard gauge-invariant observable; see [Flanagan and Hughes](https://arxiv.org/abs/gr-qc/0501041) and the [algebraic analysis of linearized gravity](https://arxiv.org/abs/1404.4551). [Dittrich and Höhn](https://doi.org/10.1088/0264-9381/27/15/155001) already construct local first-class constraints for **linearized Regge calculus** and explain their limitations at higher order. We use a different, simpler lattice and claim none of those results as new.

The distinction between linear and full locality matters: [Donnelly and Giddings](https://arxiv.org/abs/1607.01025) analyze gravitational dressing and obstructions to local observables/subsystems. A curvature component at a supplied background coordinate is invariant under the linearized gauge transformations here; this does not turn it into an exactly local diffeomorphism-invariant observable in nonlinear gravity.

## 2. Explicit lattice constraint model

Let the spatial lattice be `(Z/nZ)^3`, with odd `n>=7`, unit lattice spacing and periodic boundary conditions. At each vertex let `h_ij=h_ji` for `1<=i<=j<=3` be six real canonical configuration variables, with independent momenta `p_ij`. Define the central derivative

    (D_i f)(s) = [f(s+e_i)-f(s-e_i)]/2.

Different `D_i` commute and are skew-adjoint for the finite periodic sum. Define symmetric ADM momenta `pi^ii=p_ii` and `pi^ij=p_ij/2` for `i<j`, so the six independent pairs have the standard canonical bracket. The factor 1/2 is important.

For each vertex s set

    H_s = sum_ij D_i D_j h_ij(s) - sum_ij D_j² h_ii(s),
    M_i,s = -2 sum_j D_j pi^ij(s).

These are declared lattice discretizations of the **linearized** Hamiltonian and momentum constraints about a flat background, not the nonlinear lattice Einstein constraints. `H_s` depends only on h and `M_i,s` only on p. Their potentially nonzero mixed Poisson bracket cancels because the derivatives commute; the `H–H` and `M–M` brackets vanish directly. Thus, for arbitrary lattice smearing functions, all these linear constraints commute exactly.

This is an Abelian first-class **linearized** algebra. In full GR the normal-normal bracket instead involves the momentum constraint and a metric-dependent structure function. Linear closure is therefore not proof of the nonlinear hypersurface-deformation algebra or of refoliation invariance. In an expansion H=H^(1)+H^(2)+..., the terms linear in the fields in the full bracket include {H^(1),H^(2)}+{H^(2),H^(1)}; {H^(1),H^(1)}=0 does not test the first-order momentum constraint on the right-hand side. Moreover, central differences do not satisfy the ordinary Leibniz rule, so nonlinear continuum closure does not transfer automatically to this lattice.

## 3. A nontrivial local gauge-invariant curvature

With `x=1`, `y=2`, `z=3`, define the linearized spatial Riemann component

    R_s = 1/2 [D_y D_z h_xz + D_z D_x h_yz
                - D_y D_x h_zz - D_z² h_xy](s).

It depends only on a finite lattice neighbourhood of s. It commutes with every `H_t` since both are functions of h. It also commutes with every `M_i,t`: the generated linear spatial gauge variation is `delta h_ij = D_i xi_j + D_j xi_i`, and the four terms cancel by commuting derivatives. This is invariance under the declared **linear** constraints, not full nonlinear diffeomorphism invariance.

The contrast with a coordinate component is explicit. For the undressed `h_xy(0)` and the specified neighbouring momentum constraint, the verifier finds a Poisson bracket `1/2`, whereas every corresponding bracket for `R_0` vanishes. A coordinate component is therefore not interchangeable with the curvature observable.

The observable is not simply zero on the linearized constraint surface. Take initial data

    h_xy(s)=cos(2pi s_z/n),     other h_ij=0,     all p_ij=0.

The linearized constraints vanish, but

    R_0 = 1/2 sin²(2pi/n) > 0.

At n=9 this is `0.2065879556` in the chosen lattice units. This is a nonzero **kinematical/linearized** TT-like witness, not a prediction for an actual cosmology.

### A consequential global caveat: compact-torus linearization instability

**Follow-up:** [the explicit second-order continuum calculation](TORUS_SECOND_ORDER_GRAVITY_MATTER.md) shows that the time-symmetric vacuum continuum analogue of this witness is obstructed: its integrated quadratic constraint is nonzero. This does not prove an identical statement about a nonlinear completion of the lattice, which was never specified. The follow-up also exhibits a scalar-coupled, altered-momentum family satisfying the local classical constraints through second order only.

The periodic lattice resembles a compact flat torus. On such a symmetric background, first-order constraints can admit perturbations that do **not** extend to exact nonlinear vacuum solutions: second-order integrated/Taub constraints can impose additional restrictions. See [Altas](https://arxiv.org/abs/1808.04722) and [De Vuyst, Eccles, Höhn and Kirklin](https://arxiv.org/abs/2411.19931). The witness above has **not** been shown to satisfy those nonlinear integrability conditions. Thus it demonstrates a nontrivial state of the isolated linear model, not necessarily an admissible tangent to an exact vacuum spacetime. An asymptotically flat setting or a specified background and appropriate boundary terms is a separate, necessary follow-up; simply sending n to infinity does not automatically handle those issues.

## 4. Quantum physical sector and two local records

Quantize the finite lattice canonical variables in the usual finite-dimensional Schrödinger/Weyl representation (each variable is continuous; the Hilbert space is not finite-dimensional). Linear smeared constraints and `R_s` have well-defined self-adjoint realizations. The exact zero canonical brackets imply commuting Weyl groups, so `R_s` strongly commutes with the linearized constraint groups. No product of ill-defined operator distributions is involved at finite n.

For odd n the central derivative symbol `i sin(2pi k_i/n)` vanishes for all three directions only at the zero spatial mode. For each nonzero mode the three momentum constraints and one Hamiltonian constraint are independent. Selecting an independent real constraint basis and using standard finite-dimensional linear symplectic reduction yields

    6n³ - 4(n³-1) = 2(n³-1)+6

unconstrained canonical pairs for the **isolated linear system**. The six zero-mode pairs reflect the vanishing derivative constraints. Thus there are two pairs per nonzero real spatial Fourier degree of freedom, plus the six zero-mode pairs. At n=9 the count is 1,462. The formula is an algebraic mode count, not a proof that all these modes survive nonlinear compact-universe integrability or represent a continuum quantum-gravity Hilbert space. Using even n would add spurious Nyquist derivative zeros; odd n avoids those particular extra zeros.

### Complete pointer instrument

Select two specified sites or real lattice smearings, obtaining self-adjoint observables `R_1,R_2`. Both are linear combinations of h, hence strongly commute with each other and with the **linear** constraint group. Introduce two external-to-the-gravitational-sector pointer pairs `(Q_j,P_j)` in normalized Gaussian ready states

    f_sigma(y)=(2pi sigma²)^(-1/4) exp[-y²/(4sigma²)],   sigma>0.

The specified interaction for each pointer is

    U_j = exp(-i g_j R_j tensor P_j),

with real coupling `g_j`. This shifts pointer position by `g_j R_j`. Each full interaction commutes with every linearized constraint, and `U_1 U_2=U_2 U_1` because the two pointer momenta and the two R operators commute. For complete real-valued position outcomes `y_1,y_2` the system Kraus density is

    K_(y1,y2) = f_sigma(y1-g_1 R_1) f_sigma(y2-g_2 R_2),
    integral dy1 dy2 K_(y1,y2)^* K_(y1,y2) = I.

The equalities follow from the joint spectral theorem and normalized Gaussian density. For any physical density operator in the **reduced linear model**, the two orders have the same *joint* readout probabilities and the same unnormalized conditional post-state for the same outcomes. Finite bins and their complementary outcomes give a complete coarse-grained instrument; no outcome is omitted. The two pointer memories can retain their results if isolation is assumed.

This is an exact **same-slice commuting-instrument** result, not a comparison of two gravitational foliations. We have not derived the coupling from a covariant detector action, represented its stress energy in the constraint, included finite preparation/readout/reset costs, or constructed a relational localization field. The pointer ordering and background positions are supplied. The `h`-only observables commute here even when their support overlaps; this does not mean all local gravitational operations commute, nor does it establish spacelike microcausality at separated times.

## 5. Link back to the other frameworks

- **Quantum computing / records:** the two pointer couplings are an explicit implementation of complete instruments, with memories and correct branch probabilities; no abstract event label is treated as a record by itself.
- **Algebraic locality:** the curvature is a local linear observable on the *supplied spatial lattice*. The resulting commuting same-slice algebra is not yet a spacetime AQFT net or a net of exactly local nonlinear gravitational observables.
- **Causal order:** an operational graph may represent the two commuting interactions as unordered alternatives only once their physical spacetime support and causal interpretation are justified. The lattice itself is not a causal set and the gate sequence is not an emergent clock.
- **Contextual/topos perspective:** the compatible effects generated by these two commuting observables form a valid joint context. This is a restricted context; it does not assign noncontextual sharp values to every gravitational observable or construct a topos-derived dynamics.
- **Clock and time:** no internal clock has been constructed. Ordering interactions by a chosen background coordinate would use input time, not derive it. The measured record is not automatically a clock or experienced succession.

## 6. What the checks cover

Run [verification/linearized_lattice_curvature.py](verification/linearized_lattice_curvature.py); results are in [its JSON](verification/linearized_lattice_curvature.json).

The code uses exact rational stencil coefficients for two lattices, n=7 and n=9. At each size it checks `{H_0,M_i,t}=0` and `{R_0,M_i,t}=0` for all t and i (1,029 and 2,187 site-index combinations respectively); translation invariance extends these coefficient identities to other origins. It checks a nonzero bracket for bare `h_xy`, verifies the TT-like data satisfy the linearized scalar constraint, and compares the nonzero curvature with the analytic formula. The TT trigonometric evaluations are floating point; they are not interval certificates. `H–H` and `M–M` vanish by their h-only/p-only definitions. The mode counts follow from the displayed Fourier argument rather than a numerical matrix-rank calculation. The continuous-pointer instrument is justified analytically by the joint spectral theorem; it is not simulated by the finite stencil checker.

## 7. Next decisive gate

To reach the target originally set, either use the cited linearized Regge construction directly or justify a nonlinear completion of this discretization from an action. In either route:

1. include matter/clock and pointer stress energy in the **same** constraints;
2. handle boundaries and possible linearization-stability constraints before claiming a physical sector;
3. calculate the second-order deformation-bracket/constraint defect and the behaviour under refinement, with correct matching of endpoints and density weights;
4. prove or bound the corresponding same-event instrument probabilities, allowing dressing and nonlocality where required; and
5. recover the required semiclassical gravitational and matter dynamics, not merely closure of an engineered linear algebra.

Those steps are not supplied here. The result is a verified constraint-compatible measurement interface in one linearized regulator, with a particularly important global obstruction identified—not a decisive solution of time.
