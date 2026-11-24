# Q–desics, mean geometry and the confined sphere: a conditional test

## Source and result

Benjamin Koch, Ali Riahinia and Ángel Rincón, [“Geodesics in quantum gravity,” *Physical Review D* **112**, 084056 (2025)](https://doi.org/10.1103/w1sd-v69d), published 22 October 2025, propose a **working hypothesis** for test-particle motion on a quantum gravitational background. With affine parameter λ, their q–desic equation uses

    d²x^β/dλ² + ⟨Γ̂^β_{μν}⟩ (dx^μ/dλ)(dx^ν/dλ) = 0.

The comparison is to a geodesic of the mean metric ḡ = ⟨ĝ⟩, with connection Γ(ḡ). The operations of taking an expectation and constructing the nonlinear connection need not commute. In the paper's setup the metric is an operator, the trajectory a classical field, and the metric is a fixed background without particle backreaction. The authors assume an inverse metric operator and apply Weyl ordering. The concrete example uses a static spherically symmetric canonical-gravity construction; radial null motion and circular orbits give state-dependent corrections. Moment parameters and admissibility constraints matter, and the illustrative orbital curves are not fits to data. There is no observed q–desic effect in this paper, nor an established dark-matter explanation.

This is not a change of coordinates or clock by itself. Nor is it our [autonomous constrained FLRW detector](ZERO_SPHERE_AUTONOMOUS_CONSTRAINED_DETECTOR.md), which involves a dynamical geometry, a clock and a detector in a constrained model. Comparing the two requires a defined relational observable in a common model.

## An exact, deliberately limited bridge

The following calculation is **our toy model, not a reproduction of the paper's solution**. Tensor the actual sphere-record system of [the preceding domain report](ZERO_DOMAIN_SECTOR_CLOCK_RECOVERABILITY.md) with an independent three-level geometry register Q with values −1, 0, +1. The sphere-record states Ψ+ and Ψ− are orthogonal and have the same confined record density. Compare

    state I  = |Ψ+⟩ ⊗ |0⟩,
    state II = |Ψ−⟩ ⊗ (|−1⟩ + |+1⟩)/√2.

Assign a diagonal metric family, on 0 ≤ r < 4, in units with ε=1/4:

    ds²_q = (1 + ε r q) dt² − dr² − r² dΩ².

Use a regular angular patch and r>0 for spherical-coordinate computations. Every lapse is positive in the stated region. This is a finite-dimensional **stipulation**, not a constructed physical state satisfying Einstein's equations, a cosmological constraint, or quantum gravity. The same construction works with a classical equal mixture of ±1; the effect does not demonstrate specifically quantum coherence.

The two states have the same mean metric, Minkowski in spherical coordinates, since ⟨Q⟩=0. They also have the same confined record restriction. Nevertheless, applying the paper's operator-connection prescription gives

    ⟨Γ̂^t_{tr}⟩_I  = 0,
    ⟨Γ̂^t_{tr}⟩_II = − ε²r/[2(1−ε²r²)].

At r=1 this is −1/30 for II, whereas Γ^t_tr(ḡ)=0 for both. In contrast, Γ^r_tt=εq/2 averages to zero. The geometry register is chosen independently of the sphere record: the example does not derive a geometric effect from the sphere, establish a coupling between them, or prove an additional realm. It shows that *even retaining the mean metric as well as the confined record density* need not retain an operator connection expectation. Our previous code-recovery theorem concerns information invisible to a particular subsystem; this nonlinear moment comparison is a distinct mechanism.

### A useful algebraic caution about the paper

In Sec. V B, Eq. (81), the published paper writes the connection of the mean metric using ⟨ĝ⁻¹⟩. But in general (⟨ĝ⟩)⁻¹ ≠ ⟨ĝ⁻¹⟩. At r=1 above, ⟨A⁻¹⟩=16/15 whereas ⟨A⟩⁻¹=1. For a commuting lapse A the precise identity is

    ⟨Γ^t_tr⟩ − Γ^t_tr(⟨g⟩)
      = 1/2 [ Cov(A⁻¹,A′) + ⟨A′⟩(⟨A⁻¹⟩ − ⟨A⟩⁻¹) ].

Here Cov uses ⟨A⁻¹A′⟩−⟨A⁻¹⟩⟨A′⟩. A separate simple example A±=1+κr±δ, with κ=δ=1/4 and r=1, has zero component covariance (A′ is constant) but a nonzero difference 1/240 due to averaging the inverse. Thus vanishing that component covariance **alone** does not generally suffice. This is a check of the displayed general algebra, not a claim that the paper's particular orbit or horizon results are false; those would need independent rederivation, including their approximations.

## What happens to a clock?

For radial q–desics in state II, the averaged connection gives r″=0 and

    t″ = [ε²r/(1−ε²r²)] t′r′.

Initialize r=1, r′=1/2, t′=√5/2, t=0 at λ=0. At r=2 (λ=2), integration yields t≈2.34622321, versus t≈2.23606798 for the mean-metric geodesic with identical initial data and λ. This is a **coordinate/affine-parameter comparison**, not a measured relational time or a clock prediction.

There is an important consistency test: the mean-metric norm N=t′²−r′² starts at 1, but for the q–desic

    dN/dλ = 2 ε²r/(1−ε²r²) · t′²r′,

which initially equals 1/12. Thus λ cannot throughout be mean-metric proper time for this trajectory. For a timelike curve one can reparametrize to mean-metric proper time, at the cost of a nonaffine term in its equation. But at a tangent initially null with t′=r′=1, the norm derivative is 2/15; a nonaffine term parallel to the velocity changes it by 2κN=0 and cannot eliminate that initial drift. This does **not** invalidate the authors' admissible backgrounds or prove their null result wrong: our independently stipulated family may not satisfy their field equations or other assumptions. It demonstrates why a relational clock and a null cone must be specified consistently rather than read off automatically from the mean metric and the averaged connection.

## Implication for the point–sphere programme

The constructive lesson is that the whole's internal differentiation might have operational consequences that a lower-resolution geometry cannot represent. But this example supplies **an underdetermination test**, not a derivation of such differentiation from zero: the register, its state and its metric assignment were chosen. In particular, no global zero energy, actual subject, experiential incidence or positive–negative experiential cancellation follows. A zero constraint or mean does not itself erase local suffering or establish its balancing counterpart.

A next physically substantive step would be to define a clock-conditioned connection or a directly relational time-of-flight observable in the *same* constrained geometry–detector model, then compare states with matched relational mean metric but distinct admissible moments. One must specify clock and detector operations, common inverse/operator domains and ordering, physical inner product and constraints, and transport the observables under clock changes. Check causal/clock normalization and include backreaction where the approximation demands it. This does not assume a fundamental preferred foliation. A numerical distinction would still not by itself derive the geometry from the zero point or determine which subjects experience it.

The surface/room analogy is separate: the traveler is the player, not an inhabitant; the surface-restricted position remains A during room travel and becomes B on return. Neither the paper nor the toy metric implies that a confined inhabitant registers off-domain activity.

## Reproducibility

Run `python -m unittest verification.zero_qdesic_sphere_clock_connection_test -v`. The standard-library tests check the actual prior record vectors, exact connection/moment arithmetic, a coherence-versus-mixture control, integrated coordinate trajectory, and clock-normalization diagnostics. They test this finite toy prescription, not physical admissibility or the paper's numerical plots.
