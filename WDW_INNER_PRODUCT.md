# Wheeler–DeWitt physical inner product for the spherical R-clock

The semiclassical R-clock in [WDW_SPHERICAL_R_CLOCK.md](WDW_SPHERICAL_R_CLOCK.md)
showed that WKB evolution in areal radius recovers the dressed Killing
Hamiltonian. This note proves the next structural point: the physical inner
product for the reduced WdW equation is conserved across gravitational dressing
and reproduces the ordinary scalar Hilbert-space norm after positive-frequency
projection.

## 1. Klein–Gordon probability in internal R time

In proper radial length \(l=\int e^\lambda dR\), the WdW constraint for the
homogeneous/long-wavelength spherical mode has the Klein–Gordon form
\[
  \left(-\frac{\partial^2}{\partial l^2}+\hat H_\phi(l)^2\right)\Psi=0,
\]
where \(\hat H_\phi(l)=\mu e^\nu\sqrt{1-2m_G/R}\) is the dressed scalar
Hamiltonian at radial scale \(l\). The conserved current is
\[
  j_l=\operatorname{Im}\left(\Psi^*\frac{\partial\Psi}{\partial l}\right),
  \qquad
  j_\phi=-\operatorname{Im}\left((4\pi)^2\Psi^*\frac{\partial\Psi}{\partial\phi}\right),
\]
with \(\partial_l j_l+\partial_\phi j_\phi=0\). The physical inner product at
fixed internal “time” \(l\) is
\[
  \langle\Psi_1,\Psi_2\rangle_{\mathrm{phys}}
  =\int j_l[\Psi_1,\Psi_2]\,d\phi.
\]

## 2. WKB amplitude and L2 recovery

For a positive-frequency WKB solution
\[
  \Psi(l,\phi)=A(l)\psi(\phi)\exp\!\left(i\int_0^l H_\phi(l')\,dl'\right),
\]
the derivative is \(\partial_l\Psi=iH_\phi\Psi + (A'/A)\Psi\). Choosing
\[
  A(l)=\frac{1}{\sqrt{H_\phi(l)}}
\]
gives probability density \(j_l=|\psi(\phi)|^2\). Therefore
\[
  \langle\Psi,\Psi\rangle_{\mathrm{phys}}=\int|\psi(\phi)|^2d\phi=1
\]
after normalizing \(\psi\) to unit \(L^2\) norm. The gravitational redshift
factor \(H_\phi\) is exactly compensated by the WKB amplitude \(A\), so the
physical norm is **conserved** across the dressed geometry.

## 3. Verified numbers

From [verification/wdw_inner_product.py](verification/wdw_inner_product.py),
weak-backreaction dressed cloud with Gaussian scalar wavepacket of width
\(\sigma=1/\sqrt{2\mu}\):

- scalar Gaussian \(L^2\) norm: \(1.000000\pm10^{-12}\)
- \(H_\phi=22.0\) at center, \(21.9996\) at \(R_m=22.657\)
- WKB amplitude \(A=1/\sqrt{H_\phi}\) at both slices
- physical probability norm at center: \(1.000000\)
- physical probability norm at \(R_m\): \(1.000000\)
- norm drift: \(0.0\)
- positive-frequency norm positive: true
- mixed positive+negative state (\(\theta=0.01\)) has norm
  \(\cos^2\theta-\sin^2\theta=0.99980\), confirming the indefinite KG metric.

Negative-frequency solutions carry negative Klein–Gordon norm, as expected in the
WdW/KG framework; positive-frequency projection gives the one-particle Hilbert
space of the dressed scalar without external time.

[Relational temporal perspectives](RELATIONAL_PERSPECTIVE.md) uses these
conserved-norm states to construct conditional experienced states at clock
reading \(R\) via Page–Wootters/relational-QM conditioning.

## 4. Significance

This is the first rigorous physical-inner-product statement on the quantum
spherical midisuperspace:

- Time is internal areal/proper-radial length \(l\).
- The conserved inner product is the Klein–Gordon current at fixed \(l\).
- Positive-frequency WKB solutions with \(A=1/\sqrt{H_\phi}\) carry positive
  unit norm equal to the ordinary Schrödinger \(L^2\) norm.
- Gravitational dressing (redshift/compactness) is automatically accounted for
  by the WKB amplitude, preserving probability conservation.

Limitations:

- This is a minisuperspace/homogeneous-mode reduction.
- The WKB approximation is used for amplitude normalization; non-WKB evolution is treated separately. Backreaction of \(\psi\) on the metric is not quantized self-consistently.

[Non-semiclassical WdW harmonic evolution](WDW_HARMONIC_EVOLUTION.md) propagates quadratic-dressed Gaussian states exactly without WKB. Non-spherical modes, strong-field singularities, and phenomenal constitution remain open.

## 5. Verification

Run:

    python verification/wdw_inner_product.py
    python -m verification.wdw_inner_product

Output:
[verification/wdw_inner_product.json](verification/wdw_inner_product.json).
The deterministic pure-Python verifier constructs normalized Gaussian
wavepackets, applies WKB amplitudes at two radial slices with dressed
Hamiltonians, computes the Klein–Gordon probability norm, checks conservation,
and confirms the indefinite metric for positive/negative mixtures.
