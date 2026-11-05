# Weak-backreaction relational records for the smooth self-gravitating field clock

The smooth-field model in [SMOOTH_FIELD_CLOCK.md](SMOOTH_FIELD_CLOCK.md) solves the
classical Einstein–multiplet initial constraints, proves flat-limit program
recovery, and gives a fixed-background local field-algebra bridge. It does **not**
by itself control record fidelity through the coupled Einstein evolution. This
continuation gives a constructive, relational bound on internal clock records
read against **asymptotic proper time** in a regime where the geometry stays
close to the constructed time-symmetric initial data.

## 1. What relational interrogation means here

There is no external clock outside gravity. The comparison is between

1. the **internal field phase/program** carried by the smooth scalar multiplet,
   including gravitational dressing;
2. the **asymptotic stationary observer’s proper time** \(T\), defined by the
   asymptotically flat region with lapse \(N\to 1\).

This is relational interrogation, not an appeal to a background coordinate
duration inside the strong-field region.

On the constructed initial slice we use the conformal lapse
\[
  N=\psi^{-2},
\]
consistent with the conformally flat spatial metric \(q_{ab}=\psi^4\delta_{ab}\).
Then \(N\le 1\), and \(N\to 1\) at infinity.

The physical matter Hamiltonian on the slice is
\[
  H_m=\int N\,h_m\,d^3x,
\]
with \(h_m\) the ADM matter density. Because all program energies gravitate, the
lapse factor \(N<1\) inside the dressed field does not disappear; it is part of
the relativistic record.

## 2. The two relational error terms

For the prepared smooth scalar configuration the local internal phase of a mass
eigenstate \(v\) with classical mass
\[
  \mu=v^\dagger M v
\]
advances with proper time at rate \(N\mu\). Relative to asymptotic proper time
\(T\), the gravitational redshift contribution to accumulated phase error is
bounded by
\[
  |\Delta\phi_{\mathrm{redshift}}(T)|\le \mu T\,\langle 1-N\rangle_m,
\]
where \(\langle 1-N\rangle_m\) is the matter-weighted support average of
\(1-N\), not merely the central value. Using the central value gives a valid but
more pessimistic bound.

There is also a spatial-metric/kinetic correction from the curved initial
geometry. On the prepared smooth one-body sector we measure it by
\[
  \delta_{\mathrm{curv}}=
  \frac{|H_m-H_{\mathrm{flat},0}|}{H_{\mathrm{flat},0}},
\]
where \(H_{\mathrm{flat},0}\) is the flat-space matter energy of the same
Gaussian profile. Because \(H_{\mathrm{flat},0}\approx\mu\) for a well-localized
massive preparation up to gradient corrections, this contributes a phase slope
approximately
\[
  |\Delta\phi_{\mathrm{curv}}(T)|\lesssim \mu\,\delta_{\mathrm{curv}}\,T.
\]

Combining both effects for small total phase,
\[
  \epsilon_{\mathrm{record}}(T)\le
  \min\bigl(1,\,\mu T[\langle 1-N\rangle_m+\delta_{\mathrm{curv}}]\bigr). \tag{1}
\]
This is a vector/phase-error proxy on the prepared smooth sector, not a bound on
all excitations and not an exact nonperturbative evolution theorem. It applies
while the geometry remains in the quasistatic weak-backreaction regime around
the constructed initial data.

## 3. Explicit cases

The verifier in
[verification/weak_backreaction_record.py](verification/weak_backreaction_record.py)
reuses the Picard/contraction data from the smooth clock and evaluates both
cases.

### 3.1 Nonlinear binding family from the smooth clock

For the example \(D=12\), \(m_0=20\), program eigenvalue \(22\), \(R_0=20\),
\(\epsilon=0.001\), \(b=0.1\):

- \(\psi(0)=1.0268539009\)
- \(N(0)=0.9483806523\)
- \(E_{ADM}=23.6776572000\)
- \(E_{\mathrm{proper}}=21.5606444944\)
- binding \(E_{ADM}-E_{\mathrm{proper}}=2.1170127056\)
- classical charge \(=1.0966586189\)
- \(\max(1-N)=0.0516193477\)
- \(\langle 1-N\rangle_m=0.0368515043\)
- \(\delta_{\mathrm{curv}}=0.0366601699\)
- total error slope \(\mu[\langle 1-N\rangle_m+\delta_{\mathrm{curv}}]
  =1.6172568327\)

For a \(1\%\) relational record budget this gives
\[
  T_{\mathrm{rel}}\lesssim 0.0061833098
\]
using the averaged bound, or \(0.0051489345\) using the central bound. The
nonlinear self-gravitating configuration has a few-percent dressing, so a
percent-level record budget lasts only a short asymptotic time. That is
physically correct: gravity is not negligible in this family.

### 3.2 Strict weak-backreaction regime

For the same profile with \(\epsilon=3\times10^{-5}\), \(b=4\times10^{-5}\):

- \(\psi(0)=1.0000217819\)
- \(N(0)=0.9999564376\)
- \(E_{ADM}=0.0194060790\)
- \(E_{\mathrm{proper}}=0.0194045846\)
- binding \(=1.4944027900\times10^{-6}\)
- \(\langle 1-N\rangle_m=3.0803546460\times10^{-5}\)
- \(\delta_{\mathrm{curv}}=3.0803591100\times10^{-5}\)
- total error slope \(=0.0013553570\)

For a \(0.1\%\) relational budget,
\[
  T_{\mathrm{rel}}\lesssim 0.7378129752,
\]
with the central bound \(0.6112275202\).

These are not “tiny” merely by numerology; they are the times over which the
asymptotic observer can treat the dressed clock record as approximately faithful
before accumulated gravitational dephasing reaches the chosen budget.

## 4. What this does and does not establish

Supplied here:

- A relational record bound tied to **asymptotic proper time**, not imported
  flat coordinate time.
- Explicit separation of lapse-redshift and spatial-curvature contributions.
- Use of the already constructed smooth Einstein-constraint data; no extra
  regularization.
- Distinction between central worst-case and matter-support-averaged dephasing.

Not supplied:

- A fully nonlinear evolution theorem for all times.
- A global no-collapse or long-time stability statement.
- A quantum Einstein-constraint physical Hilbert space.
- A derivation of the prepared state from the absolute constitution.

The bound is valid only while the geometry remains within the strip around the
constructed quasistatic configuration. It is a real step beyond the flat bound:
the self-gravitating clock is not falsely treated as equivalent to a flat clock,
and the gravitational dressing enters the record error explicitly.

## 5. Verification

Run:

    python verification/weak_backreaction_record.py
    python -m verification.weak_backreaction_record.py

Output:
[verification/weak_backreaction_record.json](verification/weak_backreaction_record.json).
The deterministic pure-Python verifier recomputes the Picard conformal factor,
energies, averaged redshift, curvature energy shift, and both relational time
bounds. It does **not** perform numerical Einstein evolution.
