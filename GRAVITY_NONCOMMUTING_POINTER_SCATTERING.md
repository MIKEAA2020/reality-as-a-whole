# A noncommuting, gravitating pointer: a positive scattering signal, not yet a direction record

**Result.** The previous [gradient-pointer test](GRAVITY_GRADIENT_POINTER_GATE.md) found exact cancellation when the pointer energy commuted with its coupling generator. Here a different, explicit **two-level homogeneous pointer** has positive internal energy that does not commute with that generator. Its energy and velocity coupling enter the same gravitational constraint. In an exploratory two-channel scattering calculation, a normalized input packet gives a pointer-flip probability of approximately **0.273729**, versus exactly zero for the energy-matched no-coupling reference. Both final pointer outcomes are retained.

This is a substantive model-conditional signal, but it is **not yet a record of expansion versus contraction**. Each scattering history contains both branches; the output comparison asks whether the coupling was present, not which crossing produced the flip. Preparation and final readout are assumed boundary operations, the model is homogeneous, and the numerical calculation has not been interval-certified. The model adds a spin pointer to the parent oscillator; it is not a passive change of clock and does not pass B7 or solve the problem of time.

## 1. One specified source-coupled model

Keep the parent [gravitating oscillator](GRAVITATING_PROPER_TIME_CLOCK.md) with `mu=1`, oscillator frequency `Omega=0.6`, scalar-clock positive-frequency convention and declared log-volume ordering. In a number sector, `h_D=E_n=Omega(n+1/2)`. Add a finite pointer with Pauli matrices `X,Z` and positive proper-energy operator

    h_A = epsilon (I+Z)/2,        epsilon=0.6.

Its eigenstates `|up>` and `|down>` have energies `epsilon` and `0`. Use the same nonnegative compactly supported `g=G'` as the previous test:

    G=0 for x<=-1, G=A for x>=1,
    G=A(10t³-15t⁴+6t⁵), t=(x+1)/2, otherwise,
    A=0.8.

The declared quantum constraint in the invariant two-level sectors is

    C_g = p_T² - Theta_g,
    Theta_g = (p_x-g(x)X)² + exp(2x) I
              - (4/3) exp(x) [h_D I+h_A],
    p_x=-i partial_x.

The square fixes symmetric ordering, including both `g²` and the derivative-of-g term. The comparison has the **same h_A, same initial pointer, same n and k packet**, but `g=0`. The pointer energy's volume-dependent source is present in *both* theories; comparing to a pointer-free model would confound coupling with gravitational energy.

One reduced action realizing the stated classical symbol uses canonical `(T,p_T)`, `(x,p_x)`, the parent oscillator, and a normalized two-component spin amplitude z with a number constraint:

    I = integral [p_T dot T + p_x dot x + p_q dot q
                  + i z† dot z - lambda(z†z-1) - N_tilde C_class] d tau,
    C_class = p_T² - z†{(p_x-g X)² + exp(2x) I
                   - (4/3) exp(x)[h_D I+h_A]}z.

Here `N_tilde` is the parent's densitized lapse, not an external time. Quantizing the pointer in the one-boson/one-excitation sector turns each bilinear `z†Bz` into the matrix B and gives the declared symmetric operator. This is a particular reduced homogeneous action and quantization, not a derived covariant local detector or proof of uniqueness. No independent preparation, latch, reference or readout Hamiltonian is supplied.

## 2. Why the previous exact cancellation no longer applies

Let `U(x)=exp[iG(x)X]`. As before, `U p_x U†=p_x-gX`, but now `[X,h_A] != 0`. Conjugating the **whole** constraint gives

    U† Theta_g U = p_x² + exp(2x) I
                    - (4/3) exp(x)[E_n I+U† h_A U].

The rotated matrix source differs from `h_A` in the coupling region. The previous pure-gradient equivalence only applied when the matter Hamiltonian commuted with the generator; it cannot be reused here. Conversely, if `epsilon=0`, the source is degenerate and the exact cancellation returns. Setting `A=0` returns the source-matched diagonal reference. Both are explicit controls, not post hoc claims that any noncommuting clock must work.

For fixed n, the transformed matrix potential is Hermitian and bounded below: its negative part is bounded by a constant times `exp(x)`, while `exp(2x)` confines at large x. Declare the self-adjoint lower-bounded realization (equivalently, its Friedrichs form realization). Conjugation supplies the domain for `Theta_g`; the squared scalar constraint uses the joint-spectral domain. The full constraint may have negative **auxiliary** bound modes, which have no real `p_T` solution and are not physical no-click outcomes. The selected physical continuum has `k=-p_T>0`, with both pointer channels asymptotically open as `x -> -infinity` because their source term is proportional to `exp(x)`. The scattering matrix `S_n(k)` is two-by-two and unitary under the model's asymptotic boundary conditions. The norm and `1/(2k)` rigging convention are the parent's, now with a pointer channel index; no uniform prior over scalar time is posited.

## 3. Matched finite-packet test and complete outcomes

Prepare, as a supplied incoming boundary operation,

    n=0,  a(k)=10 on [2,2.01] and 0 elsewhere,  pointer |down>.

The spectral packet has unit norm. The pointer's final `Z` is read only in the outgoing representation. Its two geometry Kraus multipliers are

    M_up(k) = [S_0(k)]_(up,down),
    M_down(k) = [S_0(k)]_(down,down),
    |M_up(k)|²+|M_down(k)|²=1.

A pointer register can retain the associated orthogonal output labels; geometry poststates are `M_sigma a`, normalized only after conditioning. The two outcomes form a complete **ideal asymptotic** instrument on this prepared-pointer sector. That does not include preparation failures, finite-time detector noncompletion, or an action-derived boundary readout.

The packet probabilities, integrated from the computed amplitudes separately, are:

| Preparation/model | `up` | `down` |
|---|---:|---:|
| `n=0`, `A=0.8`, `epsilon=0.6` | 0.273729 | 0.726271 |
| `n=0`, matched source, `A=0` | 0 | 1 |
| `n=0`, `A=0.8`, degenerate pointer `epsilon=0` | 0 | 1 |
| `n=1`, `A=0.8`, `epsilon=0.6` | 0.343103 | 0.656897 |

The zeroes are exact consequences of the matched diagonal reference and the degenerate pure-gradient case; their numerical values are tiny floating-point residuals. The fourth row is a separate `n=1` preparation with a different gravitating oscillator energy, not a demonstrated measurement of oscillator energy or a coherent-superposition protocol. Its difference illustrates model-specific backreaction sensitivity. None of these numbers are observations or independently validated predictions for our universe.

The presence/absence comparison is a genuine output contrast **in this declared model**, under its assumed incoming and outgoing boundary operations. It is exploratory: no claim is made that the numerical values were registered in an external preregistration or selected independently of this research process. The contrast is much larger than the numerical solver differences below, but those differences are convergence evidence, **not** a rigorous bound on total computational error.

## 4. Exact tail matching and numerical controls

The numerical integration is confined to `-1 <= x <= 1.6`. In the transformed gauge `G` is constant outside the interaction region, so there is no artificial finite-wall or free-tail cutoff:

- For `x<=-1`, each incoming/outgoing channel is the exact Morse Jost solution `exp(ikx-z/2) 1F1(1/2+ik-kappa,1+2ik,z)` and its conjugate, with `z=2exp(x)`. Their derivatives match the interior solution; the Wronskian is `-2ik`.
- For `x>=1`, `U` is constant, so the decaying two-channel basis is a constant rotation of the exact Morse Whittaker modes. Their logarithmic derivatives supply the right boundary condition. The general standing/decaying subspace is propagated inward with QR stabilization of **both** values and derivatives; neither a singular value-only evaluation nor a lost branch is used.

`S` is obtained by matching those two solution subspaces. The exact-tail statement is analytical; the Whittaker functions, ODE integration, matching and packet quadrature are still evaluated numerically. The [code](verification/gravity_noncommuting_pointer.py), [receipt](verification/gravity_noncommuting_pointer.json), [tests](verification/gravity_noncommuting_pointer_test.py) and pinned [isolated dependencies](verification/requirements-gravity-spin-pointer.txt) reproduce the calculation. In the recorded run:

- At the packet midpoint, the source-matched `A=0` amplitudes agree with the parent's analytic Morse amplitudes to `1.05e-10`; the `epsilon=0` pure-gradient control agrees with the corresponding exact scalar result to `9.52e-11`.
- The coupled midpoint scattering unitarity residual is `1.65e-12`. Independently integrated packet outcomes sum to one within `2e-12`.
- Changing solver/tolerance and right matching point changes midpoint amplitudes by at most `1.60e-9` in the declared comparison. Eight- versus sixteen-panel packet probabilities differ by `8.2e-15`.

These checks compare implementations and numerical settings; unitarity alone would not certify a correct scattering phase, and none is an interval proof of the result or an independent audit of the parent constraint. An independently implemented validated integration, domain audit and physical readout construction remain useful.

## 5. Why this does not establish a direction-reading clock

For this pointer, `Z X Z=-X` while `Z h_A Z=h_A`. Thus the **entire** `-A` model is conjugate by Z to the `+A` model, including the asymptotic boundary conventions. For the chosen Z-eigenstate input and Z readout, the flip probability is identical for opposite signs of the coupling. The code checks the stronger matrix identity `S(-A)=Z S(A) Z`. This is a knob-sign control, **not** a proof that time reversal and coupling-sign reversal are the same physical experiment.

More importantly, there is no modeled comparison between two independently anchored events “cross volume b while expanding” and “cross b while contracting.” A nonzero late spin flip could arise from the combined scattering interaction, gravitational energy exchange or phase history, and no latch has selected either crossing. Nor does the output implement the value-and-derivative amplitude map of [the reconstruction](GRAVITY_VOLUME_JET_RECONSTRUCTION_AND_LIMIT.md). Identifying this late spin with a directional crossing bit would change the question rather than solve it.

The next focused gate is a **same-constraint, finite-volume event instrument**: specify an internal trigger or latch and its energy, obtain a joint distribution over expansion/contraction labels and the final record, retain failure and disturbance, and compare it to an energy-matched reference. An operational orientation claim fails if those anchored branch-conditional statistics cannot be defined or do not differ beyond controlled error; the positive asymptotic flip alone does not satisfy that gate. A new apparatus changes the matter content and must not inherit a clock-switch equivalence by assertion.

The B7 time/gravity gate remains open; so do full inhomogeneous constraints and spacetime emergence, the phenomenal bridge and the remaining substantive battery obligations. The external battery's preregistration, code, JSON and freeze were not supplied and cannot be replayed. Passing scripts checks the implemented calculation, not the formal research battery.
