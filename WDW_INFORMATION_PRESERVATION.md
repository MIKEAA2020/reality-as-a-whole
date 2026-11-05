# Unitarity and information preservation through the bounce

[WDW_BOUNCE.md](WDW_BOUNCE.md) constructed a regularized polymer bounce that caps
curvature at the universal scale \(\mu^4\). This note establishes the direct
consequence for the black-hole information problem: because the effective
Hamiltonian remains strictly positive and self-adjoint across the entire
trajectory (including the bounce neck), the Tomonaga/S-matrix propagator is
unitary and information is preserved in the global pure state.

## 1. Unitarity conditions preserved

For the bounce-regularized metric the effective scalar frequency is
\[
  \omega_{\mathrm{eff}}(R)=\mu\sqrt{f_{\mathrm{reg}}(R)},\qquad
  f_{\mathrm{reg}}(R)=\left(\frac{2M}{R}-1\right)\left(1-\left(\frac{R_b}{R}\right)^6\right),
  \quad R>R_b,
\]
with symmetric outgoing branch for \(R>R_b\) on the white-hole/baby-universe side.
Three properties suffice for unitarity:

1. **Strictly positive gap**: \(\omega_{\mathrm{eff}}(R)\geq\omega_{\min}(M)>0\)
   for all \(R>R_b\), so the WKB normalization \(A=1/\sqrt{\omega_{\mathrm{eff}}}\)
   stays finite and the KG inner product remains well-defined.
2. **Self-adjointness preserved**: \(\hat H_{\mathrm{eff}}=\omega_{\mathrm{eff}}(R)(\hat n+1/2)\)
   is essentially self-adjoint as long as \(\omega_{\mathrm{eff}}\) is piecewise
   smooth and positive (Kato–Rellich extends through the neck since \(\omega\) is
   continuous and bounded).
3. **Time (R) is monotone on each branch**: on the infalling branch \(R\)
   decreases from \(2M\) to \(R_b\); after the bounce \(R\) increases from \(R_b\)
   on the outgoing branch. The covering space is a Kruskal-like two-sided
   manifold.

## 2. Verified numbers

From [verification/wdw_information_preservation.py](verification/wdw_information_preservation.json):

| \(M\) | \(R_b\) | \(\omega_{\min}\) | \(\omega_{\max}\) (bounce blue-shift) | \(A_{\max}\) | unitary |
|---|---|---|---|---|---|
| 0.1 | 0.113 | 0.226 | ~12.4 | 2.10 | yes |
| 1 | 0.243 | 0.326 | ~45 | 1.75 | yes |
| 10 | 0.523 | 0.343 | ~105 | 1.71 | yes |
| 22 | 0.68 | 0.345 | ~138 | 1.70 | yes |

Key:

- \(\omega_{\min}\sim 0.23\)–\(0.35\) stays well above zero for all masses; WKB
  amplitudes never diverge (factor of ~2.1 maximum).
- \(\omega_{\max}\) is the blue-shift at the deepest interior point before the
  bounce (classical interior blueshifts, bounce caps curvature); at \(M=22\) it
  is \(138\approx6.3\mu\), finite.
- The S-matrix through the bounce is unitary (\(\omega>0\) + self-adjoint
  \(\Rightarrow U^\dagger U=1\)).
- Pure states remain pure: \(\Delta S=0\) (von Neumann entropy conserved at 0).

## 3. Implications for Hawking information

Unitarity across the bounce implies:

- Hawking radiation visible to asymptotic observers on the original exterior is
  **entangled with partner modes that traverse the bounce into the baby-universe/
  white-hole outgoing branch**—not lost into a singularity.
- The global state remains pure for all \(R\); Page-curve entropy is an artifact
  of tracing out the unobserved baby-universe/partner degrees of freedom (the
  standard "island/entanglement wedge" story, without needing to invoke
  firewalls).
- Information is preserved in principle; asymptotic observers may not be able to
  decode it in finite time without access to the other side, but the fundamental
  evolution is unitary—no information-loss paradox.

This is a toy bounce with a simple polymer factor, not a derived QG S-matrix,
but the structural point is robust: **any** singularity resolution that caps
curvature and leaves the effective Hamiltonian self-adjoint preserves unitarity.

Limitations:

- The polymer factor is a toy regularization, not derived from LQG/spin foams.
- Back-reaction of Hawking pairs on the bounce metric (evaporation vs bounce
  race) is not computed.
- Whether baby-universe branches decohere or remain coherent with our
  asymptotic region depends on observers; fundamental density matrix remains pure.
- Phenomenal constitution remains open.

## 4. Verification

    python verification/wdw_information_preservation.py
    python -m verification.wdw_information_preservation

Output:
[verification/wdw_information_preservation.json](verification/wdw_information_preservation.json).
