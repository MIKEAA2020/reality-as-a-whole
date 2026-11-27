# Lighthouse WP0: a closed-Milne scalar-clock admissibility gate

## Result and scope

A source-level check finds a **sign discrepancy in the cited JT preprint**: its Eqs. 2.19–2.21 give `H_grav = -i cosh(S) ∂_S`, whereas Eqs. 2.22–2.23 write the opposite sign. The related rolling-matter note uses the latter sign while claiming the increasing position motion that follows from the former. This is an explicit convention/equation conflict, not a verdict on the preprint's broader gravitational results. It can be handled by consistently choosing an orientation and corresponding relational observables; no comparison should silently mix the two.

An independently derived homogeneous scalar term gives `p²/(2B)` in the rescaled constraint, with qualifications on the action and scalar zero mode. Under the sign following from the source's earlier canonical definitions, a positive-momentum scalar position increases with `S`. But its positive-momentum **position POVM is not a covariant time POVM for the quadratic Hamiltonian**. An energy-covariant POVM exists with a nontrivial Jacobian; it measures a different quantity. Neither comes with a physical measurement apparatus here.

A concrete normalizable kinematical packet and its **exact positive group-averaged norm** are constructed below for a gravity-clock-plus-homogeneous-scalar truncation. This is a solvable constrained model using source-inspired variables, **not** a completed physical inner product of JT plus the source's full conformal matter. We have not constructed two gravitational crossed products, traces, or entropy differences. The source/related-model gate remains open.

Checks: [10 tests](verification/lighthouse_jt_rolling_clock_gate_test.py). Their numerical examples and symbolic identities are controls, not a verification of the full paper or its quantization. Prior follow-through: [Lighthouse research plan](LIGHTHOUSE_RESEARCH_PLAN_FOLLOW_THROUGH.md).

## 1. Primary source and the exact sign conflict

The primary source is Blommaert and Chen, [*Time in gravitational subregions and in closed universes*, arXiv:2602.22153v1, §2.1–2.4](https://arxiv.org/html/2602.22153). We inspected those sections, not a complete proof audit. It studies fixed topology, conformal matter and gravitational clock dressing; the closed-universe type-II result is tied to the specified holographic large-universe regime, not generic finite free matter.

With `ħ=1`, it states ([Eqs. 2.18–2.21](https://arxiv.org/html/2602.22153#S2.E19))

```text
[ell,p] = i,   [Phi,k] = i,     p = -i ∂_ell,   Phi = +i ∂_k,
H_grav = -p k - ell Phi,
B = sqrt(ell² + k²),   S = asinh(k/ell),   ell = B/cosh(S),
```

for `ell>0`. The displayed factors commute within each product, so the following sign is unaffected by their ordering. On any smooth `f(S,B)`,

```text
H_grav f = i(k ∂_ell - ell ∂_k) f
         = -i cosh(S) ∂_S f,
H_grav/cosh(S) = -i ∂_S.
```

We used `k∂_ell B-ell∂_k B=0` and `k∂_ell S-ell∂_k S=-B/ell`. By contrast, the source [Eqs. 2.22–2.23](https://arxiv.org/html/2602.22153#S2.E22) write `+i cosh(S)∂_S` and `+i∂_S`. Independently, its canonical brackets give

```text
{S, H_grav/cosh(S)} = +1,   {B,P} = +1,
P = (ell p - k Phi)/B.
```

Thus the first term in the stated symplectic form [Eq. 2.25](https://arxiv.org/html/2602.22153#S2.E25), `dK_grav ∧ dS`, also has the opposite orientation from `dS ∧ dK_grav` for these definitions. The cross brackets vanish. A different definition of `K_grav`, orientation or representation can repair the bookkeeping, but it must also change the associated constraint, evolution and dressing consistently. This calculation is a narrow algebraic finding; it does not establish the authors' intended convention or invalidate the entire crossed-product construction.

The related [WP0-B₂ note](https://github.com/MIKEAA2020/zero-residue-framework-pursuit/blob/beed773b9312a5dda4cbfe8f04cb5ca00d31bbbc/problem-of-time-package/WP0-B2-ROLLING-MATTER.md) repeats `+i∂_S`, but also states `dq/dS=p/B` for the constraint `K_grav+p²/(2B)=0`. Those two statements are incompatible with `[q,p]=i`: the `+i∂_S` convention yields `dq/dS=-p/B` for conditional evolution. It is the sign from Eqs. 2.19–2.21, `-i∂_S`, which yields `+p/B`. This is a correction to that note's gate, not evidence against the existence of a clock.

There is a related label issue in its formula for `|tau_q>`: with `<p|q>=exp(-ipq)/sqrt(2π)` and `q=i∂_p`, its `exp(+ip tau_q)` denotes position `q=-tau_q`. Reversing the label fixes that sign but does not fix the separate covariance issue below.

## 2. Homogeneous matter and the corrected constraint

For the source's closed circle, take `y∼y+1` and ADM metric `ds²=-N²dt²+ell²(dy+N_perp dt)²`. For a **noncompact target-valued**, minimally coupled massless scalar with homogeneous configuration `q(t)` and zero shift contribution,

```text
L_q = ell (dq/dt)²/(2N),   p_q = ell (dq/dt)/N,
S_q = ∫dt [p_q dq/dt - N p_q²/(2ell)],
H_q = p_q²/(2ell).
```

This derives the coefficient with our normalization. The first-order action in the related note includes an extra spatial `sqrt(h)` integral while also calling `p_q` the integrated canonical momentum; as written it does not establish this Hamiltonian without a density/normalization repair. The formula above supplies one consistent repair, not an assertion about its intended density convention.

Using the source's `ell=B/cosh(S)` and dividing the whole integrated constraint by `cosh(S)` yields

```text
C = K_grav + H_rest(B) + p_q²/(2B) = 0,
K_grav = -i ∂_S                         [following Eqs. 2.19–2.21].
```

The classical homogeneous scalar has no spatial momentum density. This is a change to the matter content; it does not show that the original CFT has this zero mode, or that arbitrary inhomogeneous matter is captured by this truncation. Source §2 states a pure-gravity minisuperspace simplification; imposing all matter diffeomorphism constraints, the state/representation, operator ordering and anomalies is an additional task. The curvature equation and dilaton response also require a consistent full solution. Adding `p_q²/(2B)` to the constraint is necessary energy bookkeeping, not by itself a completed backreacted quantum-gravity model.

`B` is a positive **gravitational variable**, not generically a fixed classical number. The scalar Hamiltonian commutes with `B` but not its conjugate `P`: on a suitable core `[P,p_q²/(2B)]=i p_q²/(2B²)`. Thus pure-gravity `P` cannot simply be treated as a conserved observable of the matter-coupled constraint; a consistently dressed operator is needed. Any fixed-`B` comparison is a fiber or approximation, not the entire theory.

For `C=-p_S+H` versus `C=p_S+H` the direction also differs. In the consistent convention just selected, `p_S=-i∂_S`, `C=p_S+p_q²/(2B)` and, on a positive-p momentum branch,

```text
psi(S,p,B) = exp[-i S p²/(2B)] psi(0,p,B),
q(S) = q(0) + (p/B) S,      dq/dS = p/B > 0.
```

Here `q(S)` is the conditional Heisenberg expression, not a globally sharp self-adjoint clock on the positive-momentum subspace. On the full scalar line, `q-(p/B)S` commutes formally with `C`; its positive-momentum compression must be treated as a POVM. The `S`-orientation and origin have been chosen, not physically derived.

If one instead adopts the preprint's displayed `+i∂_S` as the definition of `K_grav` while retaining the plus scalar term, then the corresponding wave is `exp(+i S p²/(2B))` and the sign of the drift reverses. The 10 checks include both cases.

## 3. A clock reading is not automatically a covariant time

At fixed `B>0`, choose the positive-momentum sector `L²(R_+,dp)`. The position measurement compressed to this sector is the normalized POVM

```text
|q>_+ = ∫_0^∞ dp exp(-ipq)|p>/sqrt(2π),
E_q(dq) = |q>_+ <q|_+ dq,       ∫_R E_q(dq) = I_+,
```

in the weak/distributional sense. It is covariant under momentum-generated **position translations**, not under free evolution `U(a)=exp[-i a p²/(2B)]`. Indeed, for a fixed drift `v`, time covariance of a translated position effect would require

```text
(p²-p'²)/(2B) = v(p-p')
```

for all momenta in the support. A nontrivial interval cannot satisfy this with one `v`: different momentum pairs have different average velocities. A narrow momentum packet may approximate a calibrated position clock for a finite range, but that requires a separately proven state- and window-dependent error bound. The position POVM is mathematically valid; calling it an exact covariant *time* POVM is the error.

A different, Hamiltonian-covariant POVM can be constructed. Write `E=p²/(2B)`, `v(p)=p/B`, and define

```text
|t;B> = ∫_0^∞ dp sqrt[p/(2π B)] exp[-i p² t/(2B)] |p>,
E_B(dt)=|t;B><t;B| dt.
```

The map `psi(p) ↦ psi(sqrt(2BE)) sqrt(B/p)` is unitary from `L²(dp)` to `L²(dE)`; Fourier completeness gives `∫ E_B(dt)=I_+`, and `U(a) E_B(dt) U(a)† = E_B(d(t+a))`. At `p=0` the change of variables is interpreted almost everywhere; our packet below stays away from it. This time observable is tied to the quadratic generator, not the scalar's position: classically it is related to `B q/p` up to orientation/origin and ordering. For variable quantum `B`, it is a `B`-controlled/direct-integral POVM. It is a mathematical observable, not an autonomous local clock detector or proof of full gravitational frame equivalence.

## 4. Explicit group averaging in a truncated model

We now **drop `H_rest`**, take `ħ=1`, and declare the auxiliary Hilbert space

```text
H_kin = L²(R_S × R_+_B × R_+_p, dS dB dp),
C = -i ∂_S + p²/(2B).
```

This is a source-inspired homogeneous constrained model with an explicitly chosen measure and ordering, not a derivation of the source's full physical Hilbert space. It uses the positive scalar-momentum branch. The multiplication operator `H=p²/(2B)` is self-adjoint on its natural domain; `-i∂_S` is self-adjoint on its standard domain; as commuting tensor/direct-integral operators their sum is self-adjoint. Use the `S` Fourier convention `psi(S)=∫ exp(ikS) psi_tilde(k) dk/sqrt(2π)`, so `C` multiplies by `k+H`.

Choose

```text
w(B,p) = 2 sin[π(B-7)] sin[π(p-1)]  on 7<B<8, 1<p<2,  and 0 outside,
g(c) = (π a²)^(-1/4) exp[-c²/(2a²)],   a>0,
psi_tilde(k,B,p) = g(k+p²/(2B)) w(B,p).
```

Both factors are normalized, so the kinematical packet is normalized and `p` and `B` remain away from zero. The interval `B>2π` is within the source's stated large-universe range, but the truncated matter here is **not** its large-c holographic CFT; this fact alone does not give a type-III matter algebra or type-II dressed algebra.

Define the Gaussian-regulated group-averaged pairing with `exp(it C)` and `exp(-epsilon t²)`:

```text
<psi,psi>_epsilon = ∫_R dt exp(-epsilon t²) <psi, exp(it C) psi>
                  = 2 sqrt(π)/sqrt(a²+4 epsilon)
      → 2π |g(0)|² ||w||² = 2 sqrt(π)/a > 0.
```

The equality follows by changing `c=k+H`; it holds for the stated full `B,p` wavepacket, not by evaluating a nonnormalizable plane wave. In the distributional limit the rigging map restricts the Fourier wavefunction to `k=-H`; null vectors with zero on-shell trace are quotiented. Multiplying the kinematical vector by `[2π |g(0)|²]^(-1/2)` gives unit physical norm under this declared normalization. The on-shell history is proportional to `exp[-i S H]w(B,p)`.

More generally, for suitable smooth test functions with well-defined square-integrable on-shell traces, the same regulator gives the positive pairing `2π ∫dB dp conj(f_tilde(-H,B,p)) h_tilde(-H,B,p)`. The test-space and measure are part of this construction. Positivity for this truncation does not prove positivity or convergence for arbitrary CFT states, an interacting constraint with anomalies, or the type-III representation in the primary source.

## 5. The zero mode and thermal-state gate

The word “compact” in the related note needs a distinction: the **spatial slice** is a circle; that does not mean the scalar's target is compact. The model above chooses `q∈R` and continuous positive `p`. For this noncompact scalar, `exp[-βp²/(2B)]` is a nonzero multiplication operator on `L²(R,dp)` and is not compact, hence not trace-class. There is no normalized thermal density matrix on the **full zero-mode** Hilbert space of that form. A KMS state on a suitable reduced/derivative algebra, an infrared-regulated construction, or a different representation may still exist; none has been derived here.

If instead the target is compact, `q` is angular and `p=n/R`; the thermal sum is finite, but the reading is periodic and the continuous `p>0` position POVM and globally unwrapped scalar history no longer apply unchanged. For fixed `B,β`, the compact-target partition function scales as `Z_R ~ R sqrt(2πB/β)` as `R→∞`, illustrating the lost noncompact normalization. The zero-mode choice and any associated winding record must be specified before asserting compatibility with the source's bra-ket/KMS state. A positive-momentum restriction, if imposed as a state or algebra restriction, also requires its own compatibility analysis.

## 6. Decision and next gate

- **Passed in the restricted calculation:** consistent scalar Hamiltonian under stated normalization; a monotonic classical branch with the corrected source-derived convention; normalization of two distinct mathematical POVMs; a nonzero positive group-averaged physical norm for one specified truncation and packet.
- **Correct or clarify before importing the related model:** primary-source sign conflict, first-order density convention, reversed position label, and the distinction between a position POVM and an energy-covariant time POVM.
- **Not passed:** embedding in the original conformal matter/KMS representation, full constraints and anomaly/domain treatment, a physical two-clock readout, common relational observables and both dressed gravitational algebras/traces. The packet does not close these gates and the truncation's normalized state is not automatically the source's thermal state.

Next, choose a stated noncompact-scalar infrared prescription or compact-target version and test its matter algebra and KMS compatibility with the source's chosen `B` range. In parallel, compare the two clock prescriptions as **matched POVMs on the same physical state** in this truncation, including finite-bin/no-reading outcomes and conditioning probabilities; only then investigate a CFT extension and dressed algebras. An obstruction in one scalar realization is not a no-go for other clocks. The thermodynamic arrow, Lorentzian recovery and physical–experiential constitution remain distinct open gates.

## Reproduction

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:verification:. \
  python -m unittest verification.lighthouse_jt_rolling_clock_gate_test -v
```

The symbolic tests independently calculate the source-coordinate derivatives and Poisson brackets. Numerical tests check the ADM coefficient, group-average limit, sign of conditional drift, noncovariance, energy-time Jacobian and a compact-target partition-sum control. They do not simulate quantum gravity or establish a cosmological energy balance.
