# A finite-window, unsharp volume-and-orientation record

**Result.** Within the existing homogeneous [dust-clock orientation model](DUST_ORIENTATION_RECORD.md), an explicitly specified three-outcome POVM can jointly report a **finite-resolution log-volume window** and a coarse expanding/contracting label, retaining an outside-window outcome. A bounded, idealized dust-driven control implements its complete square-root instrument, including poststates and a positive relational dust-energy bound. For the two previously specified normalizable preparations with identical initial volume distributions and opposite mean-volume slopes, the model calculation gives the correct window-and-orientation label about `0.89937` of the time, the opposite label about `0.000776`, and outside about `0.09986`.

This is a **conditional model calculation**, not a laboratory result, a sharp joint measurement, or a general accuracy claim. The measurement is anchored to a specified dust reading, not triggered at an unknown crossing; its labels are noisy and its window is broad. The qutrit control is deliberately nonlocal, uses ideal dust and a gravitational spectral code, and is not derived from a localized covariant detector. This is also a different quantization from the earlier oscillator-pointer scattering construction. It does not solve the problem of time or pass B7.

## 1. The same dust sector, and what is being measured

Retain all assumptions and units from [the prior dust-orientation note](DUST_ORIENTATION_RECORD.md): the subcritical scalar band `|p_phi|<=0.1`, Friedrichs radial sector with `Lambda=-0.75`, and the invariant code of `n=6,...,15`. The ideal dust coordinate `tau` is an internal reference; a normalizable finite dust-clock packet is not supplied. In `y=log r` the physical radial measure is `dy`, the dilation operator is `D=-i partial_y`, and `V=a³=r²=exp(2y)`. For the free dust-time evolution `d<V>/d tau=-(3/4)<D>` on the declared domain. Thus a negative-D label is called “expanding” in this orientation, and a positive-D label “contracting.” This correspondence is to the **free instantaneous mean slope**, not to an already-existing sharp classical history through the measurement.

For `s=0.25`, define normalized Gaussian phase-space states

    <y|q,k> = (pi s²)^(-1/4) exp[-(y-q)²/(2s²)+iky],
    integral dq dk/(2pi) |q,k><q,k| = I.

Take the **readout-label** window `W=[0.5,1.5]`. Its nominal volume-label interval is `exp(2W)=[2.718...,20.086...]`; the actual volume is not asserted to be sharply inside it. The full-space effects are

    F_E = integral_(q in W,k<0) dq dk/(2pi) |q,k><q,k|,
    F_C = integral_(q in W,k>0) dq dk/(2pi) |q,k><q,k|,
    F_0 = I-F_E-F_C.

All are positive and sum to I by the coherent-state resolution. Their joint output is an **unsharp POVM**; it is not a joint PVM for noncommuting volume and D. Restrict the first two effects to the calibrated code, fiberwise over p:

    E_E = P_code F_E P_code,     E_C = P_code F_C P_code,
    E_0 = I_code-E_E-E_C.

Outside the code, the later constructed register remains in the `0` outcome. On a code input these effects have exactly the same probabilities as the full Gaussian POVM. The input p packet and pointer measurement are specified; no probability distribution over all dust times is introduced.

## 2. What the finite-resolution labels guarantee

The q marginal is a Gaussian-smeared position reading: conditional on a position-basis value y, q has standard deviation `s/sqrt(2)=0.176777`. If a state is supported entirely outside `[0,2]` in y, the probability of obtaining a q label in `[0.5,1.5]` is at most

    (1/2) erfc(0.5/s) = 0.00233887.

This is a bound on the **position marginal** for that support condition, not a claim that an unmeasured sharp position and the sign label possess a joint pre-existing value. Equivalently, outside the expanded volume interval `[1,exp(4)]` the stated spatial support guarantee applies. Gaussian tails are retained, not silently set to zero.

The k marginal is the true D spectrum convolved with a Gaussian of standard deviation `1/(sqrt(2)s)`. For any state whose D spectral support lies wholly in `D<=-8`, the probability of an erroneous positive-k label—even before restricting to W—is at most

    (1/2) erfc(8s) = 0.00233887,

and conversely for `D>=8`. Because the windowed wrong-sign effect is bounded by the whole-q wrong-sign effect, the same upper bound applies to the corresponding wrong **joint** outcome under that spectral-support assumption. It is not a general bound for arbitrary states or a guarantee after postselecting on window acceptance.

The actual previous matched preparations are not assumed to have exact `|D|>=8` support. Their analytic moment bounds, `|<D>|>21.10` and `<D²><483.3`, imply by Cantelli that their weight on the wrong or low-magnitude side of `-8`/`+8` is less than `0.1817`. Splitting the diagonal D marginal at that threshold yields a conservative wrong-joint-label bound below `0.1841`. This bound is much weaker than the numerical probabilities below. It compares the POVM label to the **declared preparation orientation**; it does not postulate a simultaneous sharp volume and D measurement.

## 3. A complete finite dust-controlled instrument

Let the pointer start in qutrit state `|0>`; use `|1>` and `|2>` for E and C. On the finite code define square-root Kraus operators

    K_0 = sqrt(E_0),  K_E = sqrt(E_E),  K_C = sqrt(E_C).

The isometry `V_c` and initial embedding `J` into code tensor qutrit are

    V_c psi = K_0 psi tensor |0> + K_E psi tensor |1> + K_C psi tensor |2>,
    J psi = psi tensor |0>.

`V_c†V_c=J†J=I`, and `J†V_c=K_0` is positive. Set `T=J-V_c` and let `P_T` be the orthogonal projection onto the **closure** of its range. The Householder reflection

    U_m = I-2 P_T

satisfies `U_m J=V_c`. Indeed, `T†T=2(I-K_0)` and `T†J=I-K_0`, so `T†(J-T/2)=0` and `P_T J=T/2`. This proof needs no bounded inverse or closed-range assumption. Extend `P_T` by zero outside the code. This explicitly implements the square-root instrument, rather than only naming its effects. In the code the poststate for outcome j is proportional to `K_j rho K_j†`; outcome `0` also retains the entire outside-code sector under the specified extension.

Use the same ideal internal pulse as the previous note:

    U_0(tau)=exp(i A tau),
    h(tau)=E_b I+g(tau) U_0(tau) P_T U_0(tau)†,
    g(tau)=2pi sin²(pi tau) for 0<=tau<=1, else 0,
    E_b=1.

Its area is pi, so the interaction-picture propagator is `exp(-i pi P_T)=U_m`. The actual dust constraint is `C=p_tau-A+h(tau)`, on the transported self-adjoint domain. The effect is anchored at the declared `tau=0`, followed by free propagation to the pointer readout at `tau=1`. All three labels, their probabilities and their state disturbance are part of the instrument. The outside label is a valid outcome, **not** an invented hardware failure probability.

Because `0<=P_T<=I` and the code is invariant under A and this control, the previous source bounds still apply:

    1 <= h(tau) <= 1+2pi,
    10.104436... <= A <= 23.625,
    2.821250... <= A-h(tau) <= 22.625.

These are bounds on the **relational** dust-energy operator on the code, not positive bare-momentum support or a finite dust reference. The geometry-sensitive interaction generally has `[h,A] != 0`; it may exchange gravitational and dust energy. For the example packet its numerical nonselective mean A increases by about `0.00629`, and the end-of-pulse mean `A-h` changes by the same amount because h returns to `E_b I`. No claim is made that the controller's implementation, initialization or reset is free.

The operation is still an extremely strong assumption: `P_T` is an engineered function of Gaussian phase-space effects and code projectors, and the counter-rotation uses A. The Hamiltonian is bounded and mathematically well-defined, but no local apparatus, microscopic interaction or resource for computing and implementing it is derived. The qutrit readout itself is assumed ideal. A finite normalizable reference, real failure model, and robustness to perturbing these controls remain open.

## 4. Worked packet, including the outside outcome

Use the two states from the prior note, each with a normalized uniform p packet on `[-0.1,0.1]`, the same real radial modes and complex-conjugate coefficients. Their initial volume distributions are identical, while their free mean-volume slopes have opposite signs. The numerical Gaussian-POVM calculation gives:

| Preparation | E label in W | C label in W | Outside W |
|---|---:|---:|---:|
| Expanding-slope state | 0.899366 | 0.000776 | 0.099858 |
| Contracting-slope state | 0.000776 | 0.899366 | 0.099858 |

Among accepted window outcomes only, the corresponding-label fraction is approximately `0.99914`; this conditional number must not be confused with the unconditional `0.89937`, and the roughly `10%` outside outcome is not discarded. These values concern **two stipulated state preparations and an ideal mathematical control**. They do not establish general direction-detector accuracy, actual cosmological data, or a participant-level/phenomenal fact.

## 5. Checks and remaining gate

[The calculator](verification/dust_unsharp_volume_orientation.py), [receipt](verification/dust_unsharp_volume_orientation.json), and [tests](verification/dust_unsharp_volume_orientation_test.py) use the pinned [isolated Python requirements](verification/requirements-gravity-spin-pointer.txt). The calculation numerically integrates the Gaussian POVM in the code, checks all three effects' positivity, forms the Householder dilation, and evolves the specified 30-dimensional dust-time control. A separate position-marginal integral checks the Gaussian normalization. At one p value, simultaneous grid/domain refinement changes the maximum effect-matrix entry by `4.1e-6`, the maximum effect-operator norm by `1.4e-5`, and a worked-state outcome by `2.2e-8`; four-versus-eight-panel p integration differs by at most `8.9e-8`. The reflected-pulse state check differs by `3.5e-11`. These are numerical convergence checks, **not** certified total errors; the positivity, completeness and stated Gaussian/support inequalities follow analytically from the exact continuum POVM and specified control.

The next substantive step is not to proclaim a solved clock. It is to replace or justify the highly nonlocal code-dependent controller with a physically specified finite, localized coupling and reference, and to trigger a record at an **unknown** volume crossing while retaining both orientations, noncompletion, measurement disturbance and energy accounting. The resulting quantization must be explicitly related to the earlier backreacting oscillator model before the two constructions are treated as one physical theory. Full inhomogeneous constraint closure, spacetime emergence, the experiential bridge and the rest of the formal battery remain unresolved. The external battery's reported preregistration, code, JSON and freeze have not been supplied for replay.
