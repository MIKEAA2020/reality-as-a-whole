# Finite temporal perspectives as conditional WdW states

The global WdW wavefunction \(\Psi(R,\phi)\) is timeless: it satisfies the
constraint \(\hat H\Psi=0\) and never "changes." Finite experienced time
arises relationally by conditioning on the gravitational clock variable
\(R\) reading a particular value. This is the Page–Wootters / relational-QM
perspective, made concrete with our dressed spherical WdW model.

## 1. Conditional states and the Born rule

For the positive-frequency WKB solution
\[
  \Psi(R,\phi)=\frac{1}{\sqrt{H_{\mathrm{eff}}(R)}}\,\psi(\phi,R)\,e^{-i\Phi(R)}
\]
with \(1/\sqrt{H_{\mathrm{eff}}}\) chosen so that the Klein–Gordon norm equals 1
([WDW_INNER_PRODUCT.md](WDW_INNER_PRODUCT.md)), conditioning on clock reading
\(R=R_0\) yields the normalized scalar wavefunction
\[
  \psi_{\mathrm{cond}}(\phi|R=R_0)=\frac{\Psi(R_0,\phi)}{\|\Psi(R_0,\cdot)\|_{\mathrm{KG}}}
  =\psi(\phi,R_0),
\]
i.e. the L2-normalized dressed scalar state. The relational Born probability
density
\[
  P(\phi|R)=|\psi(\phi,R)|^2
\]
reproduces the usual quantum probabilities at internal "time" \(R\), without
any external time parameter.

## 2. Verified numbers

From [verification/relational_perspective.py](verification/relational_perspective.py):

- Conditional norm at \(R=0\): \(1.0000\); at \(R=R_m\): \(1.0000\) (KG
  conservation → normalized conditional states).
- Overlap of ground states at slightly different \(\omega\) (dressed shift):
  \(0.999999998\) — essentially indistinguishable, as the frequency shift is
  \(10^{-5}\).
- Gaussian probability within \(\pm1\sigma\): \(0.6827\) vs textbook
  \(\operatorname{erf}(1/\sqrt2)=0.6827\) — the Born rule is reproduced
  exactly on conditional states.
- Coherent state overlap for displacement \(\alpha=1\) decays as
  \(|\langle\alpha|\alpha e^{-i\omega T}\rangle|=e^{-|\alpha|^2(1-\cos\omega T)}\):

| \(T=l\) | overlap |
|---|---|
| 0 | 1.000 |
| 5.66 | 0.605 |
| 11.33 | 0.222 |
| 16.99 | 0.135 |
| 22.66 | 0.225 (partial revival) |

The overlap oscillates with the dynamical frequency \(\omega=22\) (fast
compared to \(R_m\)), giving the relational observer a changing conditional
state even though the global WdW wavefunction is stationary.

## 3. Significance for the zero-residue constitution

This is the first explicit construction in the repository of a **finite
temporal perspective** from the timeless WdW wavefunction:

- The global state is changeless (constraint equation).
- Internal "time" is areal radius \(R\), a concrete gravitational degree of
  freedom.
- Conditioning on \(R\) yields a normalized quantum state evolving unitarily
  under the Tomonaga flow ([WDW_SELF_ADJOINT.md](WDW_SELF_ADJOINT.md),
  [WDW_MAGNUS_EXACT.md](WDW_MAGNUS_EXACT.md)).
- Relational Born probabilities on conditional states reproduce standard
  quantum predictions without an external clock.
- No "time before time": the global wavefunction is atemporal; temporal
  experience supervenes on relational conditional structure, exactly as
  required by the necessary atemporal self-explication thesis.

Limitations:

- Conditional states are constructed; phenomenal consciousness/what-it-is-like
  is not yet identified with any particular relational conditional structure—
  this is a Hilbert-space skeleton for perspectives, not an answer to the hard
  problem.
- Single-clock (spherical R) model; multi-clock/observer situations require
  relational conditioning on joint systems (extendable via Page–Wootters).
- Strong-field breakdown of the dressed theory ([WDW_STRONG_FIELD_SCALING.md](WDW_STRONG_FIELD_SCALING.md))
  also bounds the regime of these simple relational perspectives.

## 4. Verification

    python verification/relational_perspective.py
    python -m verification.relational_perspective

Output:
[verification/relational_perspective.json](verification/relational_perspective.json).
