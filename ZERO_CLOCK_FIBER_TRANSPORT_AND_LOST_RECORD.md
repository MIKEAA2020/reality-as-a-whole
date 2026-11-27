# Transporting the retained clock instrument: what is exact and what is lost

## Result

The [previous pass](ZERO_RETAINED_CLOCK_INSTRUMENT_AMBIGUITY.md) defined a particular clock-neutral instrument for the **same** two-window cursor-memory model, but did not identify its connection to the earlier scalar-time reduced instrument. We now derive that connection exactly.

For that specified operation, if its mathematical orbit-label environment is retained, a fiber-dependent unitary carries the **whole** clock–apparatus–reference output into a scalar-slice description. After the specified identification and partial trace, its reduced output is **exactly** the earlier clock-smeared scalar instrument, for every original-system/reference input with the stipulated independently prepared R clock and ready apparatus. This includes both memory outcomes and arbitrary untouched reference entanglement. It closes a concrete derivation gap in the earlier reduced-output convention.

The result is not yet the desired full R-relative quantum-clock switch: the fiber coordinate is an auxiliary dilation label, not an operational R reading, and an ideal scalar clock has been gauge-fixed rather than retained as a normalizable quantum subsystem. The proof is an exact consistency relation between two descriptions of **one chosen instrument**, not an independently quantized gravitational equivalence or proof that the mathematical instrument is physically realizable. Retaining and transporting the dilation is a stronger data requirement than keeping the recorded memory outcome alone.

## 1. Fixed model, fixed operation

Take exactly the positive-frequency constrained model and notation from the [second-clock report](ZERO_TWO_WINDOW_SECOND_PHYSICAL_CLOCK.md). A is the entire original two-window system, massive cursor, flags and memory. R is the separately prepared semibounded clock. An arbitrary reference X is untouched. Write

```text
U_A(t)=exp(iH_A t),      U_R(t)=exp(iK_R t),
U(t)=U_A(t)⊗U_R(t)⊗I_X,
A_m=Π_m⊗√E_R(B)⊗I_X,
K_m(t)=ℓ^(−1/2) U(t)† A_m U(t),     m=0,1.
```

B is the finite reading bin of length ℓ; the old scalar positive-frequency branch is used and the R clock is a noninteracting added subsystem. All operators here are bounded except the self-adjoint generators of the strongly continuous unitaries. Define the maps on the trace-class input space by

```text
T_m(ρ)=∫ dt K_m(t)ρK_m(t)†,
F_m=∫ dt K_m(t)†K_m(t),       Σ_m F_m=I.
```

The integration and equality are understood as in the prior weak/quadratic-form construction. Positivity and completeness make `V: ψ↦{K_m(t)ψ}_{m,t}` an isometry into the direct integral `C²⊗L²(R,dt;H_A⊗H_R⊗H_X)`. For mixed inputs use `VρV†`. The outcome m may be read classically; the environment carrying t may either remain quantum or be traced. It is an explicit **mathematical dilation**, not evidence that an observer has access to an absolute scalar time or that a physical lab can read its label.

## 2. Exact transport on the entire dilation

Define the unitary on the direct integral by pointwise multiplication:

```text
(D f)_m(t) = U(t) f_m(t),          (D†f)_m(t)=U(t)† f_m(t).
```

Strong continuity makes D measurable and unitary, with no assumption of a normalizable uniform time state. For each input vector, every m and almost every t,

```text
(DVψ)_m(t) = ℓ^(−1/2) A_m U(t)ψ.                 (1)
```

This is an **exact intertwining of the whole retained dilation**, including R, A, X and all cross-t coherences. For mixed states the transported output is `DVρV†D†`. If m has already been recorded, dephase the m register on both sides; D is block diagonal in m, so the equality survives.

For any bounded subsequent POVM element O on that same retained dilation, the probability computed with `DVρV†D†` and O equals the probability computed with `VρV†` and `D†OD`. This includes joint distributions for the first m and any fixed subsequent instrument, provided **the entire subsequent operation**, including its record, is transported. These are representation identities for the same physical input and selected operation; comparing the same numerical matrix O on both sides would generally be a different question.

Equation (1) is not by itself a quantum-reference-frame switch from scalar time to a conditional R frame. D is controlled by the **mathematical** orbit label and is not shown to be an accessible, gauge-invariant laboratory operation. Applying D as physical feed-forward would require an implementation and a record, rather than being a free passive change. It also includes the ideal scalar-clock gauge choice: no φ/R entanglement in an independent normalizable kinematical history is reconstructed here.

## 3. Exact derivation of the scalar-smeared reduced instrument

Suppose the input has the independent-clock form

```text
ρ_AX ⊗ |β⟩⟨β|_R,
```

with factors reordered as needed. X may be entangled with all of A. Let

```text
q_B(t) = ⟨β|U_R(t)† E_R(B) U_R(t)|β⟩ / ℓ ≥ 0,
∫_R q_B(t)dt = 1.
```

The last equality is the clock-covariance/POVM identity, not a flat prior. Trace the orbit-label environment and R **after** applying D, retain m and A⊗X. Equation (1), factorization of the input, and cyclicity of the partial trace give

```text
S_m(ρ_AX)
  = ∫ dt q_B(t) (Π_m⊗I_X) (U_A(t)⊗I_X) ρ_AX
                       (U_A(t)†⊗I_X) (Π_m⊗I_X).        (2)
```

The right-hand side is a complete CP instrument. It retains the entire A, including cursor, flags and memory, at the slice-specific identification; its trace gives the earlier relational effect's outcome probability. If A starts with the **same fixed cursor/flag/memory ready state as the prior scalar instrument**, and one then traces those ancillas, (2) becomes

```text
∫ dt q_B(t) (I_m,t⊗id_X)(ρ_SX) = (J_m,B⊗id_X)(ρ_SX).    (3)
```

This is exactly the J defined in the earlier report, now derived from the specified retained-output dilation and scalar-fiber identification. `q_B(t)=w_B(r−t)` for the normalized clock packet and symmetric bin used there. Both outcomes and all real t are included; no postselection on the finite retention window occurs. Consequently the [earlier conditional model bound](ZERO_TWO_WINDOW_SECOND_PHYSICAL_CLOCK.md) below 0.0394 applies to this **specific transported and reduced output** under its stated preparation, domain and comparator assumptions, including arbitrary X.

Crucially, (2) is **not** generally the result of simply tracing R from T_m at the common initial-data anchor. T uses `U† A_m U`; S uses `A_m U` in each fiber. The different slice identifications matter. Thus no contradiction with the previous report's warning about effect/instrument ambiguity arises. The finite check demonstrates a case where the uncorrected and fiber-identified retained outputs differ.

## 4. Correlations change the formula, but not the dilation identity

For an arbitrary joint input `ρ_ARX`, including R–apparatus or R–reference correlations, (1) remains exact. However, the product formula (2) cannot be assumed. Set

```text
E_t = U_R(t)† E_R(B) U_R(t),
α_t = ℓ^(−1) Tr_R[(I_AX⊗√E_t) ρ_ARX (I_AX⊗√E_t)].
```

α_t is a positive trace-class operator on A⊗X, defined almost everywhere, with `∫ Tr α_t dt=1`. Using the commuting tensor factors and partial-trace cyclicity,

```text
S_m(ρ_ARX) = ∫ dt (Π_m⊗I_X)(U_A(t)⊗I_X) α_t
                       (U_A(t)†⊗I_X)(Π_m⊗I_X).      (4)
```

For a product clock α_t equals `q_B(t)ρ_AX`, recovering (2). For correlated states it can have a **different conditional apparatus/reference state at each t**, not a single state multiplied by a scalar clock-resolution kernel. The finite control explicitly exhibits this failure of factorization. The earlier 0.0394 bound was proved only for its independent clock and fixed-ready-ancilla family; it is not extended to correlated clock preparations by (4).

This distinction is essential if a clock interacts with the apparatus or shares its preparation history. Equation (4) is for the **noninteracting** Hamiltonian used here, even though the initial state can be correlated. An interacting R requires a different dynamical analysis.

## 5. What discarding the label really loses

The fiber unitary D acts on the **retained t environment**, not just on T_m(ρ). Therefore one may not infer the complete output `DVρV†D†` merely by knowing the marginal T_m(ρ). Whether a restricted later observable or slice-reduced map can nevertheless be recovered from the marginal depends on the instrument and input domain; it requires its own proof. For a sharp finite clock, for example, t may be redundantly encoded in the retained clock and individual classical t values can sometimes be recovered. This does not recover arbitrary coherence between t values after the environment has been traced.

The finite test makes the loss concrete. It uses the prior two-window grid's actual P/Q sectors but an explicitly different eight-step cyclic clock and unitary gate. On two pure inputs differing only by the sign of a coherence between clock labels 0 and 2:

* the complete instrument outputs with the m register retained but the orbit environment traced are **identical**;
* in the coherent Stinespring output, even after dephasing the m register, their trace distance is `1/√2`.

Thus no operation on the identical reduced outputs can recreate those two distinct environment-retaining outputs. This is a precise finite-model counterexample to universal recovery after discarding the dilation. It does **not** show that a direct map between every pair of particular reduced clock frames is impossible, or that a physical observer necessarily has access to the environment. Before the m dephasing the two full isometric outputs are orthogonal; that stronger number includes coherence between different m labels and is not the advertised classical-record experiment.

## 6. Verification and scope

The [finite control](verification/zero_two_window_clock_fiber_transport_test.py) verifies the unitary fiber identity, normalization, a transported subsequent projector on each labeled branch, exact product-state reduced formula with an entangled reference, non-factorization for a clock-correlated input, and the lost-coherence witness. It compresses the actual finite-grid P/Q sectors into two selected states; its cyclic gate and finite clock are **not** the earlier continuum massive-cursor dynamics or the positive-energy R clock. Its matrix checks illustrate, rather than prove, the operator identities above.

The derivation in sections 2–4 uses the earlier continuum clock POVM normalization and the fixed chosen instrument. It supplies an exact reduction identity for that model; it does not identify the chosen orbit-dilated measurement with a local autonomous R-clock reader. Nor does it derive a physical energy cost, an interacting or turning clock, full quantum gravity, cosmic energy, a subject, lived succession or the common constitution.

**Next target:** replace the formal orbit-label dilation with a concrete internal clock/readout interaction, or show which gauge-invariant retained observables allow a clock-switch map without access to that label. Construct an R-relative conditional output including finite-bin backaction and no-reading outcomes, then compare the same subsequent operations on an explicitly defined overlapping domain. Do not infer this switch merely from (1) or (3).

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=verification:. \
 python -m unittest verification.zero_two_window_clock_fiber_transport_test \
 verification.zero_two_window_retained_clock_instrument_test \
 verification.zero_two_window_second_clock_test \
 verification.zero_two_window_cursor_instrument_test -v
```

This transport is an application of standard unitary equivalence and measurement dilation, not a claim of priority over quantum-clock reference-frame literature or of a solution to the general problem of time. Relevant prior work includes [Höhn and Vanrietvelde's clock-neutral constrained framework](https://arxiv.org/abs/1810.04153) and [Höhn, Smith and Lock's equivalence of relational approaches under spectral assumptions](https://arxiv.org/abs/2007.00580); neither citation by itself establishes a physical implementation of the particular instrument here.
