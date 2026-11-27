# Energy-frame alignment does not remove observer deformation

## Finding and scope

The [energy-locked incidence construction](ZERO_TOTALITY_ENERGY_LOCKED_INCIDENCE_CONSTRUCTION.md) is a valid **fixed inertial-frame conditional** balance calculation. Its covariant qualification is essential: aligning incidence with the energy current defined by a moving subject-like frame, transporting a marker, and setting the complete weighted boundary flux to zero do **not** by themselves imply zero integrated exchange. Below is an explicit smooth, periodic Maxwell/source counterexample, with an analytic nonzero sign for sufficiently small amplitudes. This strengthens the warning in the [direct frame audit](ZERO_TOTALITY_DIRECT_FOUNDATIONAL_AND_FRAME_AUDIT.md); it does not invalidate the fixed-frame theorem or establish anything about actual subjects, experience, or whole-level zero energy.

All spacetime here is a specified effective flat background, not a fundamental arena or a derivation of emergent spacetime. Units have c=1, metric signature (−,+,+,+), spatial x is a 2π-periodic ring, and transverse area is one.

## 1. Which velocity is the energy frame?

Let E=(0,E,0), B=(0,0,B), with E>|B|. Put

```text
U=(E²+B²)/2,  S=EB,  R=sqrt(E²−B²),  r=R²/2.
v_lab=S/U,  v_rest=B/E,  gamma=(1−v_rest²)^(−1/2)=E/R.
```

The lab's field-energy current is `(U,S)` and its flow has velocity `v_lab`. The *energy-rest frame* is instead `u^μ=gamma(1,v_rest,0,0)`. In the (t,x) block, `T^{00}=T^{11}=U`, `T^{01}=S`; direct multiplication gives

```text
T^{μν}u_ν=−r u^μ,   C^μ=−T^{μν}u_ν=r u^μ=(ER/2, BR/2, 0, 0).
```

Thus the frame's own energy current has no spatial flux in that frame, and the timelike flow is aligned with u. Except at special points, `v_lab≠v_rest`; using `S/U` as the rest-frame velocity would be an error. This choice is a particular valid eigenframe: electromagnetic stresses can leave additional transverse eigenframe freedom, so no unique subject frame is asserted.

Let `f^ν=F^{νλ}j_λ` be the Lorentz-force density exerted on matter and `∂_μT^{μν}=−f^ν`. For a source current along y, its energy-frame field exchange is `h=f^νu_ν=−j R`. Explicit differentiation yields

```text
h = ∂_μ C^μ + T^{μν} ∂_μ u_ν.
```

Thus, for `u·∂χ=0` and `K=λC` with λ>0,

```text
∫_D χ h = ∮_∂D χ C·dΣ + ∫_D χ T^{μν}∂_μ u_ν.
```

The deformation term is not generally zero even though `C` and `K` align with the frame. A conserved K can be built, on any finite smooth domain here, by positive characteristic transport of λ solving `C·∂λ=−λ∂·C`; it is an auxiliary construction, not a derivation of an experiencing subject. No periodicity of λ is claimed or needed for the weighted **C** boundary condition.

## 2. Original field: a nontrivial partial-interval check

The original example has `E=1+a sin(t) cos(2x)`, `B=−2a cos(t) sin(2x)`, `j=3a cos(t) cos(2x)`, `a=0.1`. It obeys Faraday and Ampère equations, Gauss's laws and `∂tU+∂xS=−jE`. The original construction's lab-flow transport is **not** the rest-frame flow. For the latter choose the same initial marker `χ₀=1+0.4 cos(2x₀)` and transport along `dx/dt=B/E`.

For a material map `x=X(t,x₀)`, Jacobian `J=∂X/∂x₀>0`, and `dJ/dt=(∂xv_rest)J`, the weighted integral is correctly computed as `∫χ₀ J h dt dx₀`, not `∫χ₀ h dt dx₀`. Its flux-balance endpoint term is `∫χ₀[J C⁰(t,X)−C⁰(0,x₀)]dx₀`. The numerical control (64 markers, tight adaptive ODE tolerances) gives, at `t=1.1`, exchange `−0.36832475`, deformation `−0.29423336`, and boundary change `−0.07409139`; exchange minus deformation agrees with that change. These values are numerical checks, not exact constants.

For this particular source, `v_rest=cos(t) f(x,sin(t))`, so trajectories retrace when parameterized by sin(t); marker and Jacobian return after 2π. The full-cycle exchange and deformation are each numerically zero. This special retracing is not a general cancellation theorem.

## 3. A periodic whole-cycle counterexample

Choose smooth periodic q and let

```text
E=1+(q'/2) cos(2x),   B=q sin(2x),
j=−(q''/2+2q) cos(2x),
q(t)=−2a cos(t)+d sin(3t).
```

The field equations and `∂tU+∂xS=−jE` hold identically. Take `χ=1`, which is positive and transported by the energy-frame flow. E, B, u and C are periodic in both t and x, so the **complete weighted C-boundary flux is exactly zero** over `[0,2π]×S¹`. Nevertheless the energy-frame exchange is

```text
W(a,d)=−∫₀²π∫₀²π j sqrt(E²−B²) dx dt.
```

For `a=d=s>0` sufficiently small, this is strictly negative. In fact it is negative for every `0<s≤1/4000`, as follows. Set `e=(q'/2)cos(2x)`, so `E=1+e`; for `s≤1/100`, `|e|≤(5/2)s`, `|B|≤3s`, `|j|≤(11/2)s`, and `E>|B|`. Uniformly,

```text
sqrt((1+e)²−B²) = 1+e−B²/2+eB²/2 + remainder,
|remainder| ≤ B²e²/[2(1−|e|)]
               + B⁴/[8((1+e)²−B²)^(3/2)] < 41 s⁴.
```

The first term's integral vanishes spatially; `∫je` vanishes over a period since it is a total derivative; the `jB²` term vanishes spatially. The remaining fourth-order term uses `∫₀²π cos²(2x)sin²(2x)dx=π/4` and

```text
∫₀²π [−(q''/2+2q)] (q'/2) q² dt = 4πa³d.
W(a,d) = −(π²/2)a³d + remainder in the integrated expression.
```

For a=d=s, the integrated remainder has absolute value `<902π²s⁵`, strictly smaller than `(π²/2)s⁴` at `s≤1/4000`. Hence `W(s,s)<0` rigorously. The test also checks the symbolic trigonometric coefficient and rational bound. For a larger illustrative, non-certified numerical choice `(a,d)=(0.1,0.04)`, periodic grid quadrature gives `W≈−0.0001992795690`, stable across 64–256 points per dimension; this numerical figure is separate from the small-amplitude proof. Because the boundary term vanishes, its deformation integral equals W. The lab-frame unweighted exchange over the same periodic cycle is zero by Poynting's theorem: the signed exchange is frame-dependent, not an invariant scalar independent of the selected observer field.

## 4. Implications and remaining obligations

This identifies a precise extra condition for self-frame cancellation: not just alignment and vanishing weighted boundary flux, but also vanishing of `∫χ T^{μν}∂_μu_ν` (or an independently derived compensating term). A Killing observer provides a sufficient local deformation cancellation because T is symmetric, though normalization and other assumptions must still be checked. The counterexample has an externally prescribed source, positive electromagnetic field energy, and an engineered auxiliary incidence; it is neither a closed material system nor a counterexample to the framework's proposed whole-level physical zero. An actual organization, its current and weighting, the relevant field-plus-matter/gravitational energy, emergent spacetime and boundary conditions must all still be derived. A nonzero or zero toy integral is not evidence of felt valence or an inference to a universal subject.

Focused executable controls: [energy-frame review tests](verification/zero_energy_frame_deformation_review_test.py). Symbolic and numerical checks support the calculations; the explicit remainder argument above, not the grid alone, establishes the small-amplitude sign.
