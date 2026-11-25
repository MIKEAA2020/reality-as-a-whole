# A parity exchange from an exact zero-charge condition

## Result

The previous [minimal-reference model](ZERO_MINIMAL_INVARIANT_REFERENCE_DYNAMICS.md) imposed a parity-flipping interaction. This round replaces that explicit flip requirement with an **exact conserved, pairwise zero charge** and solves for the interactions allowed by stated symmetries.

Introduce a second, compensating reference qubit Q for the parity qubit P, and require

```text
C = X_P + X_Q = 0,           [H,C] = 0.
```

Within the specified class of Hermitian bilinear P–Q interactions, simultaneous permutation symmetry, charge conservation and an explicit antiunitary symmetry leave only

```text
H = a X_P X_Q + (b/2)(Y_P Y_Q + Z_P Z_Q) Y_V.
```

On `C=0`, the first term is `−aI`. Thus, **up to a scalar and coupling strength**, the only nontrivial allowed dynamics are the second term: it exchanges the two opposite P–Q charge signs while retaining exact zero. The parity flip is a consequence of this particular constrained operator solve, not separately imposed.

This is a substantive dependency reduction, but not yet a derivation from zero alone. The charge, compensator, symmetry action, antiunitary, bilinear interaction class, neutral state and nonzero coupling remain explicit inputs. The charge is not identified with physical cosmic energy or signed experience.

Verifier: [verification/zero_neutral_exchange_from_balance_test.py](verification/zero_neutral_exchange_from_balance_test.py).

**Plenitude continuation:** [a single zero whole containing frozen and changing couplings](ZERO_PLENITUDE_COUPLINGS_AND_MEASURE.md) retains all integer couplings coherently, including zero, and tests whether full support and sign symmetry determine the measure or relational predictions.

## 1. From the four-state reference to an explicitly balanced pair

The previous construction had a two-dimensional multiplicity reference R, a parity reference P and the two-dimensional spin-zero multiplicity V. Here add a qubit Q and define

```text
C = X_P+X_Q,
P₀ = I−C²/4 = (I−X_P X_Q)/2.
```

The `C=0` subspace has the two basis states `|+−⟩_PQ` and `|−+⟩_PQ`, where ± denote X eigenvalues. The two local signed values are always opposite on this subspace. This is a zero **eigencondition**, not just an average.

The kinematic R–P–Q reference now has eight states rather than four. On the constrained `C=0` support, P–Q has only two states, so the active reference dimension is again four. This is consistent with the preceding minimality theorem; it does not make Q or the neutral-sector constraint free.

The same `S₄` action is used as before: R carries D*, V carries the two-dimensional zero-spin multiplicity D, odd permutations act by X on P, and Q is a group singlet. All these representations, as well as C itself, are stipulated. C is invariant under the group.

## 2. The operator solve: balance produces exchange

Take a **general Hermitian interaction bilinear in P and Q**, with any Pauli factor on V:

```text
H_int = Σ_{a,b∈{X,Y,Z}, c∈{I,X,Y,Z}} h_abc σ_P^a σ_Q^b σ_V^c,
```

with real `h_abc`. This is the complete 36-real-parameter space of such bilinears; single-factor terms and couplings to R or other systems are deliberately excluded. Impose:

1. Invariance under the simultaneous permutation representation.
2. Exact conservation `[H_int,C]=0`.
3. Invariance under the specified antiunitary `Θ = X_Q K`, where K is complex conjugation in the displayed real representation bases: `Θ H_int Θ⁻¹=H_int`.

The verification computes the full linear constraint matrix. Its rank is **34**, leaving a two-dimensional solution space exactly spanned by

```text
X_P X_Q,
(Y_P Y_Q + Z_P Z_Q) Y_V / 2.
```

On P₀ the first is `−I`. The second, call it `H_ex`, satisfies

```text
H_ex² = P₀,          [H_ex,C]=0,
{H_ex,X_P}=0,        {H_ex,X_Q}=0.
```

It therefore changes `|+−⟩` into `|−+⟩` and vice versa, with a corresponding action on V. The opposite signed values are exchanged **together**; the total remains exactly zero. The anticommutation relations are outputs of the solve, not conditions used in it.

There are important qualifications:

- `b=0` is allowed and gives no nontrivial evolution in the neutral sector. The equations do **not** force a nonzero coupling.
- The scalar term does not change normalized system observables at a fixed relational reading. It can affect comparisons involving a separately fixed clock energy; removing it from a clock constraint requires shifting the clock consistently, not declaring objective energy irrelevant.
- Without the Θ condition the solution space is three-dimensional. In addition to the two displayed terms it contains `(Y_P Z_Q−Z_P Y_Q)Y_V/2`, which is Θ-odd. Thus Θ genuinely narrows the answer.
- Θ is an antiunitary of this finite representation; it has not been derived as physical time reversal of the full laboratory or cosmology.
- Allowing self-terms, R-dependent interactions, higher-body terms or a different charge can allow further Hamiltonians. The result's uniqueness is exactly as broad as the displayed class and assumptions.

The scale and sign of b remain unspecified; choosing `b=1` sets the internal phase convention for the example below.

## 3. A symmetric zero history and two matched signs

Let `|Φ⟩_RV` be the canonical invariant multiplicity-reference vector of the prior report, and start with

```text
|ψ₀⟩ = |Φ⟩_RV |+⟩_P |−⟩_Q,
|ψ(θ)⟩ = (cos θ I − i sin θ H_ex)|ψ₀⟩.
```

Every conditional state is invariant under the simultaneous permutation group, remains in `C=0`, and embeds the V factor in the earlier complementary-zero kernel. No external time coordinate is assumed. Since `H_ex²=P₀`, the evolution shown is unitary on the neutral sector; outside it, the cosine formula alone is not a full-space unitary.

Read the signs using

```text
B_P = (I−X_P)/2,          B_Q = (I+X_Q)/2.
```

Both bits are 0 for `X_P=+1,X_Q=−1`, and both are 1 for the opposite assignment. Define also the invariant joint correlation readout `B_corr=I−|Φ⟩⟨Φ|_RV`. For either `B_Q` or `B_corr`, the joint table with B_P at θ is

```text
                    other=0     other=1
B_P=0                cos²θ          0
B_P=1                   0        sin²θ.
```

At `θ=π/4`, both comparisons carry one bit of mutual information; at `π/2` the paired signs have exchanged. The P and Q signed values cancel **in each of these readout branches**, and their sum annihilates the entire coherent state. Their correlation with `B_corr` is a joint relational quantum readout, not evidence that any outcome actually occurs or that either sign is felt valence.

The symmetric history is periodic; the initial state returns up to phase at θ=`π`. The zero constraint does not turn the correlation into a permanent record or make a particular experience disappear.

## 4. A stationary whole with charge zero before selection

The following construction explicitly includes non-neutral kinematic states rather than silently discarding them. Define the partial isometry

```text
W = |+⟩_clock (P₀+H_ex)/2 + |−⟩_clock (P₀−H_ex)/2,
W†W=P₀,              𝒞 = H_ex−Z_clock,
𝒞W=0.
```

W is isometric on the neutral sector and annihilates its orthogonal complement. Let `P_G` project onto simultaneous-permutation invariants and define the commuting positive projectors

```text
Q_charge = I−P₀,
Q_sym    = I−P_G,
Q_clock  = P₀ 𝒞²/4,
Q_ready  = W B_P W†,
H_whole  = Q_charge + Q_sym + Q_clock + Q_ready.
```

Omitted identity factors are understood; `P₀` in Q_clock is extended to the clock. The verifier checks all projector and commutation identities on the full 32-dimensional clock-plus-system space. `H_whole` has a **one-dimensional zero kernel** and unit gap in the displayed units, with zero vector `W|ψ₀⟩`. The unselected whole satisfies both `C=0` and `𝒞=0`, together with the earlier complementary-zero embedding.

The stationary state's clock-reduced statistics for both `(B_P,B_Q)` and `(B_P,B_corr)` are

```text
[[1/2, 0], [0, 1/2]],
```

one bit of mutual information in each specified joint readout. This is not a claim of selected outcomes, persistent memory, or actual subject incidences. The clock, ready-state constraint and the neutral pairing are still inputs; the positive whole constraint is not demonstrated objective whole energy.

## 5. The remaining constructive problem

This step connects the proposed balance principle to dynamics more tightly: **given** the displayed conserved zero charge and interaction class, the nontrivial admissible interaction is an opposite-sign exchange, rather than an independently stipulated one-sided flip. It also gives a concrete way to retain exact zero and record correlations in an unselected whole.

The hardest dependency has moved to why zero requires this charge, a compensator, Θ and the bilinear class—and why the nontrivial coupling must be present. The frozen `b=0` case remains a counterexample to deriving change from the stated symmetry and conservation conditions alone. Nor does physical sign reversal show an opposite actual experience, an incidence measure, or gravitational energy cancellation. A subject's suffering would not be erased by a formal opposite charge.

A next test is whether a necessity or plenitude principle can constrain the *full space of allowed couplings*, including the frozen case, without choosing a coupling from outside or counting redundant mathematical descriptions as actual subjects.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps python -m unittest \
  verification.zero_neutral_exchange_from_balance_test \
  verification.zero_minimal_symmetry_reference_record_test \
  verification.zero_covariant_pairing_reference_history_test -v
```

The six new tests solve all 36 bilinear coefficients, check the symmetry and antiunitary controls, exact charge conservation, the full-space stationary constraint, relational record tables and unselected clock statistics. NumPy is required.
