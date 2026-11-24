# Zero as origin and limit: the linked article and the sphere proposal

## What the article says

Shashwat Kamlapure's [“Zero: The Number That Created Everything”](https://medium.com/@shashwat942313/zero-the-number-that-created-everything-b000304ce1b4), 1 October 2025, is a short personal account of zero as a **place-value marker, coordinate origin, calculus limit and binary symbol**. Its “created everything” claim concerns the development of mathematical and technological tools. It does **not** present a zero-energy-universe calculation, a theory of quantum gravity, or the user's experiential zero proposal. [1](https://medium.com/@shashwat942313/zero-the-number-that-created-everything-b000304ce1b4)

The useful connection is not that the symbol zero literally produced reality. It is that a zero-valued point can be associated with **direction-sensitive local relations**. That suggests a formal bridge between the article's calculus discussion and the user's point–sphere picture. Below we construct such a bridge, connect it to the earlier dual-pair state and the actual five-ray quantum probabilities, and check a nontrivial interface cost.

The article's mathematical roles should remain distinct. In decimal notation a zero digit can mark an empty place; a coordinate origin depends on the chosen coordinates unless a physical structure picks it out; and the limit in a derivative is not a literal physical journey of a quantity “never quite reaching nothing.” Binary zero and one are representational values; both may be implemented by physical states. None of these facts by itself proves that the whole universe has zero energy or that zero is literal nonexistence.

## 1. Zero value and directional information

For a differentiable function f with `f(0)=0`, its directional derivative is

```text
D_v f(0) = lim_(t→0) [f(tv)−f(0)]/t = ∇f(0)·v.
```

The value at the point is zero, while its directional response need not be. In three dimensions, unit directions v form an S². Reversing v reverses the first-order response. For example, `f(x)=a·x` and `f(x)=0` both vanish at the origin, but the first has response `a·v` and the second has response zero.

This is a useful **representation** of the user's proposal: one projection can be zero while a separately retained internal directional structure distinguishes opposite responses. It does not establish that an undifferentiated mathematical zero automatically contains a gradient, three dimensions or a sphere. The derivative presupposes a function and a domain. Nor does reversing a directional derivative automatically reverse physical energy or felt valence.

It is also related to, but not identical with, the existing [point–sphere blow-up](ZERO_POINT_INTERNAL_SPHERE_CONSTITUTION.md), where direction germs are retained as a spherical boundary projecting to one point. Neither construction needs an external time in which a point becomes a sphere.

## 2. A finite algebraic version

Instead of a limit, consider the real first-order jet algebra

```text
J = R[ε₁,ε₂,ε₃]/(εᵢεⱼ = 0 for all i,j).
```

Its elements have the form `a₀+Σaᵢεᵢ`. The projection `π(a₀+Σaᵢεᵢ)=a₀` sends all three distinct ε directions to zero. Yet `εᵢ≠0` in J. For a differentiable f, the formal first-order expression is

```text
f(0+ε·v) = f(0)+Σᵢ (∂ᵢf)(0) vᵢ εᵢ.
```

This is a finite algebraic encoding of first derivatives. The ε's are **formal nilpotents**, not ordinary nonzero real numbers and not evidence that physical distances or times are literally infinitesimal. The projection is a zero **scalar component**, not automatically an energy sum or nonexistence. As in the blow-up, the three-dimensional structure is supplied by the construction.

### A quantum constraint on taking the analogy literally

There is a useful exact obstruction to identifying one ε directly with a nonzero ordinary quantum observable. If a self-adjoint operator A satisfies `A²=0`, then for every vector ψ,

```text
||Aψ||² = ⟨ψ,A²ψ⟩ = 0,
```

so A=0. Nonzero nilpotent **non-self-adjoint** operators do exist. This does not rule out the point–sphere idea; it says a literal self-adjoint nilpotent is not a nonzero quantum observable in this standard Hilbert-space setting.

For example, on a four-dimensional space with basis `|0⟩,|1⟩,|2⟩,|3⟩`, set

```text
Nᵢ = |0⟩⟨i|,             NᵢNⱼ=0,
Xᵢ = Nᵢ+Nᵢ†.
```

The Nᵢ are nonzero and represent the three formal jet generators as algebra elements; the self-adjoint Xᵢ are nonzero, but `Xᵢ²≠0`. In particular, the measurable Hermitian directions require the adjoints and the larger operator algebra, which are extra structure rather than a consequence of bare zero.

For a real direction `n=(n₁,n₂,n₃)` define `X_n=ΣnᵢXᵢ`. The model has

```text
Tr(X_n X_m)=2 n·m,          X_(−n)=−X_n.
```

Under a rotation R, the unitary `U_R=1⊕R` carries `X_n` to `X_(Rn)`. A separate internal parity `diag(1,−1,−1,−1)` reverses all Xᵢ. Thus directions and sign reversal are **relations within the declared model**, not an externally chosen axis. The assumed three-dimensional representation and its rotation group are not themselves derived, and this SO(3) covariance is not a recovery of a Lorentzian spacetime.

## 3. An exact zero state determined by three directional balances

The directional construction connects to our earlier [identity pairing](ZERO_NECESSARY_PLENITUDE_SIGN_PAIRING.md). On the four-level space and its paired copy, define

```text
Qᵢ = Xᵢ⊗I − I⊗Xᵢᵀ,
|Φ₄⟩ = (1/2) Σ_(a=0)^3 |a⟩⊗|a⟩.
```

Then **each** Qᵢ annihilates `|Φ₄⟩`. The three Qᵢ need not commute, yet they possess this common zero state. In fact, for these specified Xᵢ the common zero state is unique up to phase:

1. In vectorized form, `Qᵢ|M⟩=0` says `XᵢM=MXᵢ`.
2. `ΣXᵢ²=I+2|0⟩⟨0|`; hence the Xᵢ generate `|0⟩⟨0|`.
3. Products `Xᵢ|0⟩⟨0|Xⱼ` generate every `|i⟩⟨j|`, and the other matrix units follow similarly. Therefore the Xᵢ generate the full 4×4 matrix algebra, whose commutant consists only of scalar matrices.
4. Consequently M is a multiple of I and the normalized solution is `|Φ₄⟩`.

Equivalently, the positive constraint `C=ΣQᵢ²` has a single zero eigenstate. Its finite spectrum is `0` once, `2` eleven times, `6` three times and `8` once. The gap is 2 in the chosen units. This is a genuine conditional advance beyond saying that many states can have a zero average: **these particular three operator balances determine one complete pure state**.

For unit n, the local X_n has eigenvalues `−1,0,0,+1`. In the identity pair a simultaneous measurement of X_n on the first factor and `−X_nᵀ` on the second gives opposite values and exact zero sum; the individual `+1` and `−1` values each have Born probability 1/4, and zero has probability 1/2. This statement concerns one chosen direction's joint measurement, not simultaneous sharp values of all noncommuting directions or actual experiential incidences.

The word **conditional** matters. The dual factor, three Xᵢ, their operator-equality constraints, dimension and scale were specified. The proof does not show that zero as such necessitates them, that Qᵢ are physical energy, or that a charge constraint is the universe's objective energy. Nor does it identify the signs with felt pleasure and suffering. It does offer a sharply stated candidate: directional equal-and-opposite relations can select a whole state uniquely *once the relevant relations are justified*.

## 4. Connection to the actual five-ray sphere—and an interface cost

**Encoded continuation:** [an exact three-balance sphere record](ZERO_THREE_BALANCE_ENCODED_SPHERE_RECORD.md) constructs a larger, locally conserving encoded realization of the same five-ray table. It does not establish a conserving dilation of the original bare-state readout.

The same `|Φ₄⟩` can be factored as two qubit identity pairs. A local unitary on one paired qubit turns the first pair into the singlet used in our [five-ray construction](ZERO_SPHERE_CONSERVATION_RECORD_CURRENT_SINGLE_SYSTEM.md); the second qubit pair is a spectator. Transport the Qᵢ and C by the same unitary. On the first pair use the prior actual triple effects `Fᵢ=qᵢ(I+nᵢ·σ)` with

```text
q=(1/8,2/5,19/40),
```

and Bob's previously specified spin axis. Standard Born calculations give the same ideal table:

```text
                 Bob +       Bob −
sphere 1          3/40        1/20
sphere 2          1/10        3/10
sphere 3         13/40        3/20.
```

This is a concrete mathematical link from the directional-balance state to the prior sphere statistics, **given** the factorization, local unitary, effects, Born rule and state. It does not derive those inputs, actual outcomes or incidence weights from zero.

There is a consequential cost: the straightforward local Lüders instrument that produces this ideal table does **not** preserve all three Qᵢ constraints on the original two-factor system. On the normalized three outcome states, the expectation of transported `C=ΣQᵢ²` is respectively

```text
1,       7/4,       553/361,
```

and the unselected outcome-weighted expectation is `59/38`, rather than zero. The specified C is nonnegative and initially exactly zero, so this is not merely a change of description or an unobserved sign convention. It is a calculation for this local instrument and these Qᵢ, not a no-go theorem against all conserving measurements.

To maintain such balances through an operational record, an apparatus/reference and its contribution to the **relevant constraints** must be included. Our finite [energy-conserving sphere interface](ZERO_DUAL_PAIR_SPHERE_ENERGY_CONSERVING_INSTRUMENT.md) explicitly conserves one chosen additive charge; it has not been shown to conserve all three directional Qᵢ. The follow-up [work–subject integration](ZERO_ENERGY_SPHERE_WORK_SUBJECT_INCIDENCE.md) similarly uses a stipulated zero charge and does not by itself solve this new three-constraint interface. This is a concrete next test rather than an assumption that the constructions automatically combine.

## 5. Implication for the user's proposal

The article offers a helpful image: zero need not be the end of a mathematical description. The calculation above makes a stronger but still conditional point: a zero-valued projection can coexist with a sphere of directional responses, and three chosen paired balances can uniquely fix a nontrivial entangled state. It does not turn mathematical zero into an external creator or claim that a function literally evolves out of nothing.

For necessary plenitude, this is a candidate route—not proof—that opposite internal aspects are actual in one self-subsistent whole and cancel without erasing their local distinctions. To establish it as the user's account, the dimensionality, algebra, dual pairing, actual physical and experiential incidence, signed quantity and operational interfaces must follow from zero's own constitution rather than be independent inputs. In particular, nonzero suffering would remain locally felt even if a justified whole-level sum were zero.

The specific next question is whether the three directional balances can be extended to a physical apparatus while retaining the sphere's finite-reference records and the strict locality/report constraints. A negative result for one instrument would not refute plenitude; a successful construction would still have to explain why its experiential organization is actual and why its complete energy includes all interactions.

## Reproduce

```sh
python -m pip install --target .arena/python-deps numpy  # if needed
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_article_jet_dual_pair_test -v
```

The tests check the derivative example, jet-operator identities, rotations and sign reversal, uniqueness and spectrum of the paired constraints, the five-ray table, and the local-readout disturbance. The uniqueness proof is analytical; the finite eigenspectrum is verified numerically. These tests do not establish gravity, an experiential subject or the metaphysical thesis.
