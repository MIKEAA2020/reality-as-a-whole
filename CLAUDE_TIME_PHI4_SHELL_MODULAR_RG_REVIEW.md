# Regulated φ⁴ shell flow and modular comparison

## Claim and scope

This follows the [Ising review](CLAUDE_TIME_ISING_MODULAR_RG_INSTRUMENT_REVIEW.md) toward A5/G5's field-theory target. It gives (i) an independently checked one-loop momentum-shell beta function for **four-dimensional Euclidean scalar φ⁴ theory**, (ii) an exact interacting, finite-regulator version of a shell integration, with a provable modular-intertwining obstruction for a particular finite configuration encoding, and (iii) a separate comparison in a **physical canonical two-mode scalar-field algebra** at finite temperature. All are specified, with different regulators and limits kept distinct.

The field-theory and quantum-modular pieces now use the same type of scalar self-interaction, but this is **not yet** a derivation of a physical field-theoretic modular/RG correspondence in a common continuum limit. In particular, the Euclidean encoding's noncommutative matrices are mathematical encoding degrees of freedom, not automatically canonical quantum-field observables; and tracing a spatial oscillator from a thermal density matrix is not the same channel as integrating a four-momentum shell from an Euclidean path integral. The numerical canonical calculation concerns a two-mode truncation, not the universal continuum beta function. None is a new law for emergent time, zero energy or experience.

## 1. A familiar field-theory beta function, obtained from a shell

Consider the real, one-component Euclidean action in four dimensions, with ultraviolet momentum cutoff Λ, positive mass m and stable λ≥0,

```text
S[φ]=∫d⁴x [ (1/2)(∂φ)² + (1/2)m²φ² + (λ/4!)φ⁴ ].
```

Separate φ=ϕ+η into Fourier modes below `Λ/b` and a fast shell `Λ/b<|p|<Λ` (`b>1`). The Wilsonian definition is the exact, generally nonlocal functional relation

```text
exp[−S_eff(ϕ)] = ∫Dη exp[−S(ϕ+η)],
```

up to a ϕ-independent normalization. Work at finite volume and regulated modes first, and expand at λ=0 at fixed cutoff; `m>0` controls the slow zero mode. The following is a **one-loop, zero-external-momentum projection** of the effective action, not an exact finite-coupling solution or a statement that the action remains purely quartic. At order λ the `ϕ²η²` term shifts the mass. Its second cumulant supplies the quartic term:

```text
(λ/4)∫ϕ²η²,          ⟨η(x)²η(y)²⟩_connected = 2 G_>(x−y)²,
λ_eff = λ − (3/2) λ² I_shell + O(λ³) [in the one-loop quartic projection],
I_shell = ∫_(Λ/b<|p|<Λ) d⁴p/(2π)⁴ · 1/(p²+m²)².
```

For constant external ϕ, terms linear in η vanish because the shell excludes p=0; higher operators and momentum-dependent terms are not discarded from the exact `S_eff`. A subsequent RG step must account for the generated terms and its chosen rescaling/renormalization conditions. The order symbol here describes the loop-projected quartic coefficient at fixed finite shell and weak coupling; it is not a global error estimate over large scale changes.

With `k=Λ/b` and the spherical continuum shell,

```text
I_shell = 1/(16π²) [ log((Λ²+m²)/(k²+m²))
                      + m²/(Λ²+m²) − m²/(k²+m²) ].
```

For m=0 *in the shell integral* (or asymptotically m≪k), `I_shell=log b/(8π²)`. Thus, with `ℓ=log b` increasing towards the infrared,

```text
dλ/dℓ = −3λ²/(16π²) + O(λ³),
β_UV(λ)=dλ/d log μ = +3λ²/(16π²) + O(λ³)
```

in the usual massless four-dimensional convention. At finite mass the infinitesimal shell has the threshold factor `k⁴/(k²+m²)²`. Classical rescaling contributes no quartic term in exactly four dimensions; field-renormalization corrections enter this beta function beyond one loop. The conventional positive UV coefficient and finite-mass threshold are independently stated in João F. Melo, [*Introduction to Renormalisation*, Eqs. (3.48)–(3.50)](https://arxiv.org/pdf/1909.11099#page=27), arXiv DOI [10.48550/arXiv.1909.11099](https://doi.org/10.48550/arXiv.1909.11099); see also James M. Cline, [*Quantum Field Theory* lecture notes](https://www.physics.mcgill.ca/~jcline/qft1b.pdf). **Access clarification:** the earlier attempt to fetch Melo's HTML URL failed; the beta-function citation was initially supported by a search-engine extract, not a direct full-paper reading. The PDF text extractor subsequently succeeded, and its chunk 10 (containing Eqs. 3.48–3.50) was read directly. The extractor covers at most the first 30 pages, and the complete 67-page paper has not been read. The comparison checks normalization and the reversal of sign between UV and IR conventions, not an all-orders identification of schemes.

## 2. Exact regulated shell analogue in the same interaction

To retain a completely explicit finite example, use a periodic Euclidean lattice with `2⁴=16` sites, lattice spacing one, and keep just the normalized constant and one staggered Fourier mode:

```text
φ_n = (x + (−1)^(n₁) y)/sqrt(V),   V=16,
S(x,y)= (1/2)m²x²+(1/2)M²y²
        + λ/(24V)(x⁴+6x²y²+y⁴),
M²=m²+4κ.
```

Here the kinetic term is `(κ/2) Σ_(n,μ)(φ_(n+μ)−φ_n)²`. This is an interacting **two-mode truncation** of a four-dimensional lattice field regulator; all other Fourier modes have been removed, not integrated out. The staggered mode is the chosen fast sector and the constant mode the slow sector. Summing a finite amplitude grid `Y` exactly gives

```text
S_eff(x)= −log Σ_(y∈Y) exp[−S(x,y)].
```

Treating x as a real variable in the specified polynomial and defining the quartic coefficient by the fourth derivative at x=0 (not by interpolation from only two samples), write `λ_eff=V S_eff''''(0)`. For the λ-dependent normalized fast distribution at x=0, an exact differentiation gives

```text
λ_eff = λ − (3λ²/(4V)) Var_(x=0,λ)(y²).
```

The variance is nonnegative, and is strictly positive when the grid has at least two distinct y² values with nonzero weight. This is an **exact finite-grid relation** in this two-mode truncation, not a continuum beta function. Taking the fast amplitude grid to the real line with Gaussian integration at λ=0, `Var(y²)=2/M⁴`; hence the weak-coupling coefficient becomes

```text
λ_eff = λ − 3λ²/(2VM⁴) + O(λ³).
```

This is precisely the one-loop shell formula with the discrete single-mode replacement `I_shell→1/(VM⁴)`. A full lattice shell contains all retained fast modes and their covariances; the spherical continuum integral in §1 follows only after its own volume/cutoff and momentum limits. The single two-mode number is not a numerical measurement of `3/(16π²)`.

## 3. Exact modular obstruction for a configuration encoding

Choose finite amplitude sets `X={0,a}` and `Y={−b,0,b}` with a,b>0, retaining the action above. Let `p(x,y)=exp[−S(x,y)]/Z`, `p_x=Σ_y p(x,y)`. Encode the classical configurations in orthonormal vectors `|x,y⟩` and use the full matrices `M_X⊗M_Y`, with faithful diagonal density matrix `ρ=diag p` and reduced `ρ_X=diag p_x`. The Schrödinger channel is the partial trace over y. On observables use the natural embedding `ι(A)=A⊗I` and the state-preserving unital completely positive map

```text
R_ρ(B)=ρ_X^(−1/2) Tr_Y[ρ^(1/2) B ρ^(1/2)] ρ_X^(−1/2).
```

For `E=|a⟩⟨0|`, put

```text
Δ_y=S(a,y)−S(0,y)=m²a²/2+λa⁴/(24V)+λa²y²/(4V),
Δ_eff=−log p_a+log p_0,
c_y=sqrt[p(y|a)p(y|0)] > 0.
```

Then `R_ρ(E⊗I)=(Σ_y c_y)E` and, using `σ_s^ρ(B)=ρ^(is)Bρ^(−is)`, the exact difference is

```text
[R_ρ σ_s^ρ ι − σ_(q s)^ρ_X R_ρ ι](E)
 = [Σ_y c_y exp(−isΔ_y) − (Σ_y c_y) exp(−iqsΔ_eff)] E.
```

For λ>0, `Δ_b−Δ_0=λa²b²/(4V)>0`. The positive weights give a strictly positive weighted variance of Δ_y. A sum of these distinct frequencies cannot equal a single frequency for all s: equality of the value and first two derivatives would force that variance to zero. Therefore **no real constant q** makes this specified map intertwine even on this observable for all s. The natural embedding also fails, because full modular phases depend on y whereas the embedded reduced phase does not. At λ=0 the slow and fast factors separate and both comparisons become exact. Isolated parameter values and other channels or algebras are not ruled out.

For the explicit test values `m²=.25`, `κ=.1`, `λ=5`, `a=1.2`, `b=1.4`, `V=16`, the fast-dependent gaps are `(0.4275, 0.207, 0.4275)`; the weighted variance is approximately `0.0121222`. These are regulator-dependent dimensionless figures. The diagonal configuration algebra itself is commutative and has **trivial** modular automorphisms. The off-diagonal E exists only after introducing this mathematical Hilbert-space encoding; it must not be mistaken for a canonical field observable or evidence of physical modular time.

## 4. A separate physical canonical scalar-algebra test

To avoid relying exclusively on that encoding, take a periodic **three-dimensional spatial** `2³` lattice, retain its constant and one staggered spatial mode, and canonically quantize their coordinates x,y. In units ℏ=1 the two-mode Hamiltonian is

```text
H = (p_x²+ω₀²x²)/2 + (p_y²+ω₁²y²)/2
    + λ/(24V_s)(x⁴+6x²y²+y⁴),
V_s=8,   ω₀=.8,   ω₁=sqrt(1.64),   λ=2.
```

Project each oscillator to its first d energy levels. Importantly, the code computes `P x² P` and `P x⁴ P` using additional levels **before** projection, rather than incorrectly equating these with `(P x P)²` and `(P x P)⁴`. Use the finite faithful thermal state `ρ=e^(−βH)/Tr e^(−βH)` at β=.5, its reduced state `ρ_x=Tr_yρ`, the same typed CP coarse map `R_ρ:M_(d²)→M_d`, and observable `A=(P x P)⊗I`. Set `L_ρ(B)=−i[−logρ,B]`.

At d=4 the calculated operator-norm infinitesimal defect is

```text
||R_ρ L_ρ(A) − L_ρ_x R_ρ(A)|| ≈ 0.00020603218.
```

Even after fitting the best **real constant** q to the derivative in Frobenius norm, `||R_ρ L_ρ(A)−q L_ρ_x R_ρ(A)||_F≈0.0002804971`, so this finite model cannot be exactly intertwined by a constant linear reparameterization. A direct finite-s calculation approaches the commutator result. The λ=0 control vanishes to numerical precision. At d=5 the corresponding operator-norm defect is approximately `0.000695219`; these cutoff-dependent position norms **do not establish convergence or divergence**, especially because position is unbounded as d grows. As a separate bounded-observable diagnostic take `B=|0⟩⟨1|+|1⟩⟨0|` on the slow mode (`||B||=1` for every d), embedded with the fast identity. Its defect norms at d=4,6,8 are approximately `0.000290393`, `0.000698593`, `0.000718285`. These few samples still do not prove a cutoff limit; they provide a better-defined observable for pursuing one.

This is a genuine canonical algebra of the specified finite scalar truncation, with a scale-changing operation that discards a spatial mode. However, its partial-trace reduced Gibbs state is not generally Gibbs for the naively projected slow Hamiltonian, and its temperature-dependent modular Hamiltonian `−log ρ_x` is not automatically the Wilsonian action of §1. The exact finite-temperature boundary-state correspondence for this spatial-mode trace is given in §5. Matching it to §1’s four-momentum beta function requires common boundary conditions, regulator and observable/coupling projection; the β-function in §1 is therefore **not claimed to have been calculated by this numerical partial trace**.

## 5. Exact common boundary channel at finite cutoff

There is a precise partial bridge between the two descriptions, without pretending that the spherical shell of §1 is the same operation. For the finite physical Hamiltonian of §4, let `T=exp(−βH/n)` and use any orthonormal slow and fast bases. The exact slow boundary kernel is

```text
K(x_n,x_0) = Σ_(x_1,...,x_(n−1)) Σ_(y_0,...,y_(n−1))
              ∏_(j=0,...,n−1) T[(x_(j+1),y_(j+1)),(x_j,y_j)],
y_n=y_0,      ρ_x=K/Tr K.
```

This follows simply by inserting identities into `T^n=e^(−βH)` and performing the fast partial trace. Integrating/summing **the whole fast spatial worldline** with periodic fast endpoints and the stated slow endpoints gives exactly the canonical reduced thermal state. It is an exact finite-cutoff boundary-state correspondence for this spatial-mode coarse-graining; the test explicitly sums the paths for d=2 and n=3 and independently compares with the matrix partial trace. The individual transfer-kernel terms need not be positive, so this basis sum is not automatically a classical probability or a local Euclidean action. Nor does it identify selective outcomes.

This construction advances the common-channel requirement, but the coupling beta of §1 integrates a **four-momentum** shell, not all Matsubara frequencies of one spatial mode. Relating that beta to the above boundary kernel still needs a matching regulator, a coupling projection of the corresponding influence functional, and appropriate limits. No such equality is asserted here.

## 6. Consequences and next discriminating step

The source's proposed bridge survives as a research question, but it is not an identity of the two flows: a known φ⁴ running coupling coexists with a trivial modular flow on the commutative configuration algebra, and two specific noncommutative finite constructions yield modular mismatch. The positive free limits and explicit variance/cumulant formula tell us what to match and what can obstruct it; none is a no-go for all physical RG schemes.

Next extend the exact finite boundary-kernel correspondence to a regulated canonical scalar field and its thermal Euclidean path integral on the same lattice and time circle. Specify whether the RG removes full spatial worldlines or four-momentum modes, derive the induced observable map and a coupling projection in the same scheme, and compare these with the modular generator using common normalization. Track generated operators, mass and thermal dependence, oscillator cutoff and continuum/volume limits; choose bounded observables or a stated energy-bounded norm before making convergence claims. Independently calibrate any putative physical clock. No part of this calculation derives effective spacetime or gravity, selects an experiential subject, or turns an RG parameter into lived succession.

## Verification

[Focused executable checks](verification/claude_time_phi4_modular_rg_review_test.py) independently verify the lattice mode reduction, exact finite-grid variance formula, Gaussian and shell-integral coefficients, state-preserving map, configuration obstruction, the canonical finite-cutoff comparison and free control, and the exact finite transfer-kernel boundary channel. Numerical execution verifies those models and formulas, not the larger physical programme. The beta-function reference is external; the cumulant and integration here give an independent calculation within the stated approximation.
