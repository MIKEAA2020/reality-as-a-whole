# The sphere, a closed plasma, and the experiential balance gate

## Result

The preceding work connected the proposed internal sphere to a two-component state space and a relativistic null cone. The next question was whether **physical dynamics can determine a weighted signed balance**, rather than putting it in by hand.

Here is a concrete result. An exactly solvable, closed, nonrelativistic two-fluid–Maxwell oscillator has:

* nonzero local energy exchange and positive conserved field-plus-matter energy;
* a cyclic state that can be represented as a path on the equator of the same `CP¹`/Bloch sphere;
* zero *unweighted* exchange over a full cycle;
* a positive, state-dependent response factor built entirely from its own fields and currents for which the **weighted exchange is nonzero** over that cycle.

Consequently neither closure, an internal sphere representation, dynamical determination of the response factor, nor a return to the same physical state by themselves imply an experiential zero. Conversely, if the response depends only on the exchanged energy, the weighted exchange is an exact difference and does vanish between matching energy endpoints. This is a constructive necessary test for a candidate physical–experiential bridge, not a proof that such a bridge cannot exist.

The model has no demonstrated subjects: the incidence and felt-valence interpretations below are hypotheses used to test the proposed relation. It does not establish the universe's global energy or experiential total.

## 1. A closed physical system

Take the fixed-background nonrelativistic cold-fluid equations from the [two-fluid work](ZERO_TOTALITY_TWO_FLUID_INCIDENCE_DYNAMICS.md). Use a finite periodic spatial domain, with unit volume, and a homogeneous electric field. In normalized units set

```text
n₊=n₋=1,  q₊=+1,  q₋=−1,  m₊=m₋=2,  ε₀=1.
```

Let the velocities be spatially uniform, `v₊=j/2`, `v₋=−j/2`, and choose `B=0`. Densities are constant by continuity, the charge density is zero and Gauss's law is satisfied. The fluid and Ampère equations reduce exactly **within this nonrelativistic effective model** to

```text
dE/dt = −j,       dj/dt = E.
```

There are no prescribed external currents or external forcing in these equations. For `E(0)=A>0`, `j(0)=0`,

```text
E(t)=A cos t,     j(t)=A sin t,
u_E=E²/2,         u_m=j²/2,
h = du_E/dt = −Ej,
d(u_E+u_m)/dt=0.
```

Here `u_m` is the combined kinetic energy density of the two species; rest energy and gravity are omitted. The constant physical energy density is `A²/2>0`, so it is **not** a zero-total-energy universe. We use `A=0.1` so peak fluid speed is `A/2=0.05` in the chosen velocity units. Relativistic corrections, pressure, collisions and quantum effects are absent. A periodic spatial domain removes spatial boundary fluxes; the selected interval `0≤t≤2π` is one cycle, not an established boundary of all reality.

The exchange `h` is a rate of change of field energy and can have either sign although both field and kinetic energies are nonnegative. It is charge-conjugation even: `E→−E`, `j→−j` leaves `h` unchanged. Identifying that sign with felt valence remains an unproved proposal.

## 2. Connecting the actual orbit to the sphere

Let

```text
n_x=E/A,    n_y=j/A,    n_z=0.
```

Because `E²+j²=A²`, this is a unit vector and traces the equator of `S²`. Equivalently, associate to the state the projective spinor

```text
ψ(t) = (1, exp(it))/√2,       ρ=(I+n·σ)/2.
```

With Pauli convention `σy=[[0,−i],[i,0]]`, this gives `n=(cos t,sin t,0)`. It evolves as a two-level state under `H=σz/2`, up to overall phase. This is an exact **representation of the oscillator's phase** by a Bloch-sphere orbit; it is not evidence that the classical plasma is a qubit, that each sphere point is a subject, or that this orbit yields physical spacetime. The amplitude `A`, an energy scale, is discarded by the projective normalization and must be retained separately. The standard pure-state sphere representation is reviewed in the [Durham quantum information notes](https://www.maths.dur.ac.uk/users/kasper.peeters/qcomp/2023/qubit.html).

Nor does the parameter `t` here derive fundamental time: it is the assumed effective laboratory time of the plasma model. A cyclic path of internal states is not a closed timelike curve.

## 3. Two state-derived responses, different balances

Let `N=n₊+n₋=2` be the conserved matter-number density. **For testing only**, hypothesize that it also measures actual subject incidence and that every unit has the same signed valence

```text
v = χ(E,j) h/N,      Nv=χ(E,j)h.
```

Neither the matter-to-subject identification nor this common-valence identity is derived. The response `χ>0` is a state-dependent factor, not a changing subject density. In particular, constant `N` obeys the matter continuity equations; there is no hidden subject-creation assumption in the algebra. Actual experiential incidence could differ, and the two species need not share a single subject or common valence.

Compare two smooth, positive, charge-conjugation-even factors for `|b|<1` and nonzero `E²+j²`:

```text
χ_flow = 1 + 2bEj/(E²+j²) = 1+b sin(2t),
χ_energy = 1 + b(E²−j²)/(E²+j²) = 1+b cos(2t).
```

Both are functions of the same physical state, bounded between `1−|b|` and `1+|b|`. No prescribed external marker is needed to calculate either. Their choice as a *phenomenal response* is still stipulated; deriving a formula from available physical variables is not the same as demonstrating that nature uses it.

Since `h=−(A²/2) sin(2t)`, direct integration over `0≤t≤2π` yields

```text
∫ h dt                  = 0,
∫ χ_energy h dt         = 0,
∫ χ_flow h dt           = −b π A²/2.
```

With `A=0.1`, `b=1/2`, the last integral is exactly `−π/400 ≈ −0.007853981634`. With `b=−1/2` it has the opposite sign, even though the underlying physical oscillator and its conserved energy are unchanged. Under the hypothetical `N,v` identity these would be signed experiential totals on that interval; the calculation is **not** a measurement of suffering or pleasure.

The physical state has returned to its starting point; the unweighted exchange is zero; the two response functions are well behaved and constructed from the state. These facts do not determine which response describes experience, or even whether this plasma experiences anything.

There is a further physical distinction: under the usual time reversal of this nonrelativistic oscillator, `E` is even and `j` is odd. Thus `χ_energy` is even, but `χ_flow` transforms to the expression with `−b`. The nonzero-cycle result uses a time-direction-sensitive response. Whether such a response is physically or phenomenally appropriate needs a justified arrow, state preparation or microscopic dynamics; it cannot be claimed to follow from this reversible oscillator alone. The example remains a valid counterexample to the weaker claim that state-dependence, positivity and charge-conjugation symmetry alone guarantee balance.

## 4. The exactness condition and why organization matters

Because `h=du_E/dt`, along any physical history

```text
∫ χ h dt = ∫ χ du_E.
```

If the response is a single-valued function of exchanged energy alone, `χ=f(u_E)`, choose `F'(u_E)=f(u_E)`. Then

```text
χ h = dF(u_E)/dt,
∫ χ h dt = F(u_E(final))−F(u_E(initial)).
```

Equal energy endpoints therefore give exact weighted balance. In this oscillator `D=E²+j²=A²` is constant, so along a trajectory `χ_energy=1+b(4u_E/D−1)`, a function of `u_E` alone. Its cycle balance follows from the exact-difference rule, not simply from unweighted energy conservation.

The flow-sensitive response depends on the phase or direction of exchange in addition to `u_E`. At the same `u_E` its value can differ for rising and falling field energy. It therefore need not define a single-valued function of `u_E`; the closed-path integral can be nonzero. More generally, treating `(E,j)` as local coordinates, the one-form `ω=χ(E,j)d(E²/2)` has

```text
dω = E (∂χ/∂j) dj ∧ dE.
```

Where this is nonzero, `ω` is not locally exact. Non-exactness in general does not guarantee a nonzero integral on every particular closed trajectory; for `χ_flow` the explicit calculation above establishes it on this one.

This distinction is useful for the zero programme. An actual experience–energy bridge must explain why the *actual* organization-dependent one-form is exact on the relevant histories, or supply a different physical reason for its total to vanish. Simply requiring `χ>0`, using the same physical state to calculate it, or showing conserved energy does not do that.

## 5. Test of the proposed divergence law

The proposed target is

```text
Σ_s n_s v_s = ∇_μ J^μ.
```

In this homogeneous model, take the tested candidate `Σ n_s v_s=χ_flow h`. Suppose `J` is a single-valued local function of the physical state and its derivatives, with no explicit time dependence or additional nonperiodic hidden state. Every such `J` is periodic on this orbit; its spatial divergence integrates to zero on the spatial torus, and its time-boundary values agree. Therefore its spacetime divergence integrates to zero over one cycle. But `∫χ_flow h dt=−bπA²/2≠0` for `b≠0`.

**Accordingly, this candidate cannot be the divergence of such a current on this orbit.** A current with an explicitly time-dependent, nonperiodic or additional memory variable could evade the restriction, as could changing the proposed valence law or physical domain. Those extra structures would themselves need physical and constitutive justification. This is a conditional obstruction to a particular bridge, not a no-go theorem for zero totality or experience.

For comparison, the unweighted case has `h=∂t u_E`. Multiplication by the response gives the exact identity

```text
χh = ∂t(χ u_E) − u_E ∂tχ.
```

The last term is nonzero in the flow-sensitive example; it is the correction lost by treating a weighted balance as automatic. In an effective curved-spacetime formulation with physical observer field `u`, electromagnetic energy current `C` and exchange `h`, the previous report derives

```text
h = ∇·C + T_EM^(μν) ∇_μ u_ν,
χh = ∇·(χC) − C·∇χ + χ T_EM^(μν) ∇_μ u_ν.
```

Thus response gradients and observer deformation both matter; eliminating either must follow from dynamics or actual boundary conditions. A four-scalar constructed using a material rest-frame `u` is covariant under coordinate changes but still depends on that **physical** congruence. The matter center frame here is a model-defined local frame, not a fundamental preferred foliation. The present oscillator is nonrelativistic and does not prove a relativistic completion, nor that subjects' rest frames coincide with this matter frame.

## 6. What must now be derived

The candidate achievement is sharper than an appeal to cancellation: **balance is equivalent to an exact or otherwise globally cancelling actual weighted contribution**, not just a zero in an unweighted physical ledger. The sphere links this test to the earlier point–sphere work, while the closed two-fluid dynamics removes the earlier independent external-source caveat.

A successful next step must derive from zero's constitution—not choose to make the result work—(i) why such a physical structure and its dynamics are actual, (ii) what constitutes subjects and their incidence, (iii) why their real felt valence has a particular signed physical identity, and (iv) why the complete history and its boundaries enforce the required total. The model neither claims a final no-go nor demonstrates eventual success. It maintains the distinction between a zero whole and nonzero local experiences, if those experiences are actually established.

## Reproduce

```text
python -m verification.sphere_closed_plasma_incidence --steps 64 128 256
python -m unittest verification.sphere_closed_plasma_incidence_test -v
```

The exact integrals are derived above. Fourth-order Runge–Kutta checks give flow-weighted values `−0.0078539714809`, `−0.0078539810301`, and `−0.0078539815973` respectively, approaching `−π/400`; the 256-step maximum physical-energy drift is about `3.89e−12`. Numerical convergence checks the calculation, not its experiential interpretation.
