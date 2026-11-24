# Full-state geometry data for two autonomous records

**Integrated continuation:** [sphere, targeted memory and experiential candidates](ZERO_INTEGRATED_SPHERE_AUTONOMOUS_INCIDENCE.md) adds a relation-specific third memory, and derives a new conservative 26-slice full-state bound for the changed constraint.

**Related arrow-of-time audit:** [Fukuyama's closed-universe proposal](FUKUYAMA_ORIGIN_TIME_ARROW_SPHERE_AUDIT.md) distinguishes clock-patch changes from entropy and record arrows and compares a separate two-sided record model.

## Main result

The preceding [multichannel analysis](ZERO_TWO_WINDOW_CONTINUUM_GEOMETRY_SLICE.md) established an almost-everywhere **single-slice scattering** reconstruction for the autonomous detector and two memories, but left degenerate bound eigenspaces unresolved. We can now include the entire point spectrum, including possible embedded and threshold eigenstates, without assuming simplicity:

> For the specified two-window model, the complete complex solution data on **almost every ordered 13-tuple of geometry slices** determine the full physical state. The same is true when all 13 slice values are restricted to any nonempty open geometry interval. Between any two such tuples, the corresponding full-state data spaces are unitarily equivalent with their transported physical inner products and observables.

The number 13 is a **rigorous sufficient upper bound**, not a demonstrated minimum; no particular tuple or the single slice α=0 is proved good. Nor does a collection of 13 slice signals equal a single-reading clock. The data include both pointer components, all memory-y and logical h labels, and the complex solution for all real scalar φ. They are not the finite outcomes of an actual measurement.

The new step is a uniform bound on point-eigenspace dimensions. In each memory channel there are at most four eigenvalues below, and at most four above, the respective free band, counted with multiplicity. Any eigenvalue **inside the closed band**, including its endpoints, has multiplicity at most 13. These are bounds, not exact spectral counts; an embedded eigenvalue is not asserted to exist. Combined with the preceding no-singular-continuous result and single-slice scattering theorem, they yield the finite multi-slice reconstruction.

[Verification](verification/zero_two_window_full_slice_test.py) checks constants, finite-grid inequalities, an illustrative degenerate example and transport of the actual detector–memory probabilities. It does not replace the continuum proof.

## 1. Operator and what is being reconstructed

For `I=(−7,−6)`, `T(p)=p²/6`, the conserved memory-y labels `m=(m₁,m₂)∈{−1,+1}²`, and h=0,1, use the previous model

```text
Θ_(h,m)=T−2h+V_m,       Ω_(h,m)=√Θ_(h,m),
V_m=−E_(−5) σ_yᴰ − 1.3(m₁E_0+m₂E_5)P₁ᴰ,
E_a(p,q)=exp[−ia(p−q)] K(p−q),
K(x)=exp(−x²/2)sin(2x)/(πx).
```

Each h,m channel has two pointer components. Θ is bounded below by 0.4 on the full specified sector. Eigenvectors are unaffected by the scalar shift `−2h` and the strictly increasing square root; it suffices to study `H_m=T+V_m`.

The preceding analysis establishes that H_m has the free band `[6,49/6]` as its essential spectrum, that its absolutely continuous spectrum there has multiplicity two, and that there is no singular-continuous component. For almost every α, the two-component full complex slice signal recovers the entire a.c. part. The arguments below concern the remaining point states.

The channel decomposition is only a computational basis: memory-z observables mix the m labels. All labels and interchannel phases are retained in the representation. This is the same physical system, not a new constraint or a set of independently selected outcomes.

## 2. At most four exterior states on each side

The useful window representation is

```text
K(x)=(1/2π)∫_ℝ g(y) exp(ixy)dy,
g(y)=∫_(−2)^2 exp[−(y−r)²/2]/√(2π) dr ≥ 0.
```

Its even moments needed here are

```text
∫g=4,      ∫y²g=28/3,      ∫y⁴g=284/5,      ∫y⁶g=3700/7.
```

Fix either band endpoint `p_*` and write `d(p)=|p−p_*|`. If a component f satisfies `∫_I exp(iap)f(p)dp=0`, the zero integral permits subtracting its endpoint phase in the quadratic form of E_a. Weighted Cauchy–Schwarz gives

```text
⟨f,E_a f⟩ ≤ C ∫_I d(p)|f(p)|²dp,
C = (1/2π) ∫g(y)∫_0^1 [2−2cos(yx)]/x dx dy.
```

This is independent of a and of which endpoint is used. For all real t,

```text
2−2cos t ≤ t²−t⁴/12+t⁶/360.
```

For example, six derivatives reduce the difference between the right and left sides to `2−2cos t≥0`, and its first five derivatives vanish at zero. Substitution of the moments yields the explicit rigorous bound

```text
C ≤ C_* = (14/3 − 71/60 + 185/756)/(2π)
          ≈ 0.593336.
```

Let `f=(f₀,f₁)` and impose four linear conditions:

```text
∫exp(−5ip)f₀(p)dp=0,    ∫exp(−5ip)f₁(p)dp=0,
∫f₁(p)dp=0,               ∫exp(5ip)f₁(p)dp=0.
```

They have codimension at most four. With `w_j²=∫d|f_j|²`, the window inequality and the positive-form Cauchy–Schwarz inequality imply

```text
|⟨f,V_m f⟩| ≤ 2 C_* [2(0.5)w₀w₁ + 1.3w₁²]
              ≤ 2 C_* M ∫d ||f(p)||²dp,
M = [1.3 + √(1.3²+1)]/2 ≈ 1.470061,
2 C_* M ≈ 1.744481 < 2.
```

At the lower edge `T−6≥2d`; at the upper edge `49/6−T≥2d`. Thus, on that codimension-at-most-four subspace, `H_m−6` is strictly positive and `49/6−H_m` is strictly positive. By the min–max principle (or direct dimension counting of negative spectral subspaces), H_m has **at most four eigenvalues below 6 and at most four above 49/6**, counting multiplicity. The previous edge variational argument guarantees at least one on each side.

## 3. A uniform multiplicity bound inside the band

Suppose `H_m f=E f` for `E=T(k)` with `k∈[−7,−6]`. The vector function `G=V_m f` is continuous and differentiable up to the endpoints. Square integrability of f in

```text
[T(p)−T(k)] f(p) = −G(p)
```

forces `G(k)=0`, including at an endpoint. Hence f is an eigenvector with eigenvalue −1 of the Hilbert–Schmidt operator

```text
(B_k f)(p)=∫_I [V_m(p,q)−V_m(k,q)]/[T(p)−T(k)] f(q)dq,
|T(p)−T(k)| ≥ 2|p−k|.
```

The quotient extends continuously through p=k. The derivative bounds below are uniform in p,q and k. Using the moments of g and Cauchy–Schwarz,

```text
|∂_p E_a(p,q)| ≤ L_a,
L_a = √(28/3+4a²)/π,
L_0 ≈ 0.972453,      L_5=L_(−5) ≈ 3.328330.
```

The matrix Frobenius norm of the derivative of V_m is at most

```text
[2 L_5² + 1.3²(L_0+L_5)²]^(1/2).
```

The band has length one, so

```text
||B_k||²_HS ≤ [2L_5²+1.3²(L_0+L_5)²]/4
             ≈ 13.353762 < 14.
```

For an orthonormal family of d eigenvectors of B_k with eigenvalue −1, the Hilbert–Schmidt norm squared is at least d. Therefore `d≤13`. This includes embedded and endpoint eigenvalues and does not require an assumption about their existence or separation. Outside the band each eigenspace has dimension at most four by §2. Consequently **13 is a uniform upper bound on every point-eigenspace dimension** in each h,m channel.

## 4. Why 13 generic slices see every point state

Let `N≤13` be the dimension of any one point eigenspace and choose a basis `v₁,…,v_N`. Each vector-valued slice amplitude is the Fourier transform of a compact-band L² function, hence is entire in α. For any nonzero linear combination v, Fourier uniqueness says its two-component amplitude is not identically zero; at least one component therefore has only isolated real zeros.

Choose slice values successively. If previous evaluations leave a nonzero subspace of the eigenspace invisible, choose a nonzero vector in it. For almost every next α, that vector is visible, so the remaining kernel loses at least one dimension. By induction, N slices suffice for this eigenspace. More precisely, some N-tuple gives full rank; a corresponding minor is a nonzero real-analytic function of the N slice values, whose zero set has Lebesgue measure zero. Thus almost every N-tuple gives full rank. This also holds within any nonempty open interval because a nonzero real-analytic function cannot vanish throughout an open set.

There are at most countably many eigenvalues in a separable Hilbert space and finitely many labelled channels. Intersecting the associated full-measure sets shows that almost every **13-tuple** resolves every point eigenspace simultaneously. Independently, almost every first slice recovers the a.c. part by the previous scattering theorem. The spectral theorem separates the point atoms from the a.c. density even if an eigenvalue is embedded. Hence almost every 13-tuple recovers **the full state**.

This argument does not establish that any particular prescribed 13-tuple is good or that one geometry slice suffices for the bound sector. It gives no uniform condition number: even good tuples can have very unstable inverses.

## 5. Full-state transport and the memory observables

For each h,m channel use a normalized a.c. coefficient `c_ac(E)∈C²` and an orthonormal basis in each point eigenspace with coefficient vector `c_e∈C^(N_e)`. For a good tuple `A=(α₁,…,α₁₃)`, write

```text
b_A,ac(E)=F_A(E)c_ac(E),       b_A,e=D_A(e)c_e.
```

Here `F_A` stacks the two-component continuum slice matrices, including the physical solution normalization, and `D_A` stacks the corresponding bound-eigenfunction evaluations with the same normalization. The former has full column rank almost everywhere and the latter has full column rank at every point eigenvalue. Left inverses on these ranges give

```text
||b_A||²_phys = ∫ ||F_A(E)^+ b_A,ac(E)||² dE
                + Σ_e ||D_A(e)^+ b_A,e||²,
```

where `+` denotes the Moore–Penrose left inverse. The domain consists of data arising from physical states for which this norm is finite; ordinary Euclidean norm on the raw amplitudes is not the physical inner product. If W_A maps the full physical state to its tuple data, the change from good tuple A to good tuple B is

```text
T_(B←A)=W_B W_A⁻¹,         O_A=W_A O W_A⁻¹,
O_B=T_(B←A) O_A T_(B←A)⁻¹.
```

It is unitary between the **transported** data-space inner products. This is an identity for the same physical state and the same operator, not a measurement-induced evolution or a change in couplings. In particular, the complete two-memory z-readout projectors and their probabilities, including all bound–scattering and interchannel coherences, can be represented on either good tuple. One must carry the full operators across h and m channels; computing only channelwise probabilities would lose the coherences.

As a numerical illustration, the independent N=32 finite-grid calculation reconstructs the full evolved state through two 13-slice data sets and reproduces the original two-memory distribution at φ=100:

```text
M₁M₂ = 00,01,10,11:  0.509183, 0.058237, 0.073821, 0.358759.
```

This matches direct evolution at that grid size; it is not a continuum error bound or proof that the particular selected tuples are continuum-good.

## 6. Meaning and limitations

This closes a specific **full-state information problem** for a finite collection of geometry slices in the selected continuum constraint model. It does not show that a single geometry reading works, that an inhabitant can access the full complex signals, that a finite operational clock attains the reconstruction, or that the inverse is stable. It also does not turn geometry into a globally monotonic clock or defeat the bound-state obstruction to a normalized covariant time POVM.

The setup uses an ideal scalar reference, nonlocal band-projected windows and stipulated initial/coupling data. It is not a derivation of full gravity, its constraint algebra, objective total energy, subjects, felt time or the physical–experiential bridge from zero. A confined inhabitant is not identified with the external player/traveler, and nothing here assumes it registers richer-domain activity. Proposed whole-level cancellation would not erase locally felt suffering.

The next clock question is whether the actual bound eigenspaces have rank sufficient on **one** slice, perhaps after proving their exact multiplicities; the 13-slice theorem does not settle that. A separate, larger task is to derive the physical structures and an experiential incidence law from the point–sphere constitution rather than specifying them.

## Reproduce

```sh
python -m pip install --target .arena/python-deps numpy  # if needed
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest verification.zero_two_window_full_slice_test -v
```
