# Independent continuum certificate and conditional cursor improvement

## Result

The previous [continuum recheck](ZERO_TWO_WINDOW_CONTINUUM_CERTIFICATE_RIGOR_REVIEW.md) tightened the commutator and single-flag bounds but reused the earlier exact rational Gram calculation. A [separate implementation](verification/zero_two_window_independent_gram.py) now reconstructs **all four** truncated residual-Gram entries with ordinary complex rational polynomial coefficients, independently bounds the analytic truncation error using a different telescoping order, and independently bounds packet overlap by reducing the trigonometric argument. It reproduces the exact Gram entries and the same continuum thresholds

```text
||[Θ_h,Q]|| < 0.412,        single-flag miss/false flag < 0.0266.
```

This is independent **code and arithmetic**, not an independent scientific model or a machine-checked proof: both implementations use the same specified kernels, Taylor orders, Machin identity and underlying continuum/operator hypotheses. Agreement catches representation and arithmetic errors but cannot eliminate a shared wrong premise or interpretation.

**Correction to the prior review's next step:** a later [autonomous cursor reader](ZERO_TWO_WINDOW_AUTONOMOUS_CURSOR_READER.md) and its [complete instrument and backaction analysis](ZERO_TWO_WINDOW_CURSOR_INSTRUMENT_AND_BACKACTION.md) already exist. The original single flag is reversible, but the later, *different* constraint conditionally transfers its information to a memory for a finite interval. They do not establish permanent retention, physical locality or an actual clock switch. The earlier recheck overlooked these continuations; they must not be described as if no transfer model had been constructed.

Conditionally importing the earlier cursor analysis and substituting the tighter commutator certificate gives the sharper **finite-horizon memory probability** bounds

```text
false record on P < 0.000332,       missed record on Q < 0.000332.
```

These improve the earlier `<0.000343` estimates for the same stipulated cursor model. The full postmeasurement-channel bound is a different quantity and is **not** replaced by this probability bound.

## 1. Exact independent polynomial calculation

For an ordinary monomial basis, the new code separately constructs

```text
packet:     (1/4−t²) Σ_(k=0)^40 (±15i t)^k/k!,
kernel:     π_mid^−1 [Σ_(k=0)^32 (−ia d)^k/k!]
             [Σ_(j=0)^12 (−d²/2)^j/j!]
             [Σ_(j=0)^12 (−1)^j (2d)^(2j) 2/(2j+1)!],
```

where `d=t−s`, `a∈{−5,0,5}`, and `π_mid` is the exact rational midpoint of the same Machin interval as before. It expands `(t−s)^n` by the binomial theorem, integrates ordinary monomials over the band, forms the three orthogonal residual components and evaluates their Gram inner products with explicit complex conjugation. Unlike the earlier program it does not store coefficients as rational multiples of `i^k` or import its polynomial helpers.

The comparison test imports the two **finished results** and checks exact rational equality, including both diagonal entries and both conjugate off-diagonal entries. The following decimals merely identify those exact rational values:

```text
G̃₊₊ =  0.16829295865429145,    G̃₋₋ = 0.16828756003955347,
G̃₊₋ = −0.00083228167317271 − 0.00066955750135921 i.
```

Both diagonal imaginary parts are exactly zero in the computation. The companion [tests](verification/zero_two_window_independent_gram_test.py) include simple hand-solvable kernel/moment and conjugation controls, so exact comparison is not the only test. All calculations use standard-library integer and rational arithmetic; no numerical mesh enters the certificate.

## 2. Independent bounds, common hypotheses

Let `e_p,e_g,e_s` bound the phase, Gaussian and sinc truncations on `|d|≤1`; let `δ_π=1/π_lo−1/π_hi`. By replacing phase first, then Gaussian, then sinc, and using `1/π<1/3`, `|G|≤1`, `|S|≤2`, we obtain the alternative uniform kernel error

```text
E_K ≤ [2e_p + 2(1+e_p)e_g + (1+e_p)(1+e_g)e_s]/3
      + δ_π(1+e_p)(1+e_g)(2+e_s).
```

The code computes these quantities independently from factorial expressions and encloses π with exact rational alternating series. On the unit-length band this kernel bound controls the operator by Hilbert–Schmidt. Using the normalized packet envelope and `||Θ₀−7.046||<4`, the same decomposition into exact-versus-truncated packet and exact-versus-truncated kernel yields

```text
η_alt = 4e_f + (18/5) E_K (1+e_f) < 10^−11.
```

For the overlap, the new implementation reduces `15=5π−y` with `0<y<1`. Alternating real Taylor polynomials bound `sin y` and `cos y` at rational interval endpoints; monotonicity gives

```text
|⟨f₊,f₋⟩| < 0.002176356 < 11/5000.
```

The number `0.002176356` here is a **rounded-up descriptive bound**; the exact program checks the stronger rational endpoint against `11/5000`. This is a different numerical enclosure route from Taylor expansion directly at 15. With the Gram entry bounds and this overlap, the program verifies the previous `<0.412` threshold using fractions. The square-root/Duhamel flag implication is as in the prior review; it has not been recast as a formal proof assistant theorem.

## 3. Conditional transfer to the existing cursor reader

The reader uses eight flags, `g=100`, a prescribed cursor packet with `a=b=10^−6`, `v=1`, `m=10^16`, and the corrected right-moving preparation `exp(−imvx)`. It adds a cursor, memory and interaction to a **new** constraint. The original proof derives, through the finite retention horizon, an amplitude error comprising noncommutation before the pulse ends, finite-pulse error and massive-cursor dispersion, plus a tiny comparator blank amplitude. We **inherit** those functional-analytic and domain estimates here; they are not independently proved by recomputing the commutator.

With `c_* = 0.412/(2×1.3)`, `T_end=π/200+2×10^−6`, and π bounded by the exact rational `3.1416`, the new rational check gives

```text
D_sys ≤ 400 c_* T_end²       < 0.015644,
D_pulse ≤ π·800·10^−6        < 0.002514,
D_disp < 0.0000528,       η_flag < 10^−31,
D_sys + D_pulse + D_disp + η_flag < 0.01821,
(D_sys + D_pulse + D_disp + η_flag)² < 0.000332.
```

Consequently, **if** the cursor report's comparison hypotheses, preparation, analytic domain controls and dispersion/pulse bounds hold, the P false-record and Q missed-record probabilities are each below `0.000332` over its stated finite readout interval. The output follows from the full-vector triangle inequality, not from averaging selected states. It includes arbitrary initial P/Q-sector states and logical h correlations under the report's fixed ready-ancilla and factorized cursor assumptions. An arbitrary coherent P–Q input needs the cursor report's coherent-state inequality rather than a naive mixture of the two error probabilities.

The initial momentum, large mass and energy scale, synchronized packet, global Q coupling, chosen clock, ancillas and readout are stipulated. The derived probability is not an empirical observation, permanent memory, whole-level energy zero, or experienced succession. A full independent review of the cursor's unbounded-operator domain estimates and its complete instrument remains a separate task; the finite regulator does not prove them.

## 4. Next gates

Independently audit the cursor derivative, domain and Duhamel estimates, including the corrected propagation sign; examine the complete instrument's poststate bound and whether the improved commutator can tighten it without conflating channel error with record probability. Then test a genuinely distinct clock for the same physical instrument. The present framework treats space and time as non-fundamental constructs and experience as intrinsic; neither a chosen scalar parameter nor a memory bit derives effective spacetime, identifies a subject, or constitutes a particular felt quality.
