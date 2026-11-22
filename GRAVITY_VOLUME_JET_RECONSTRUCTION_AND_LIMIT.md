# Reconstructing the backreacting gravity record from volume-boundary data

**Result.** In the same Einstein–scalar–oscillator model and spectral band `2<=k<=8`, retaining **both** the fixed-volume wavefunction and its volume derivative gives a bounded, injective mathematical representation with a bounded inverse, even at the nodes that defeated value-only evaluation. It can be transported smoothly through every classical turning volume in that band, and the parent gravitational record and a specified two-event sequence are preserved in this representation. An explicitly completed abstract filter–recovery instrument has nonzero, analytically bounded joint success probability.

**Crucial limitation:** this is reconstruction of a generalized wavefunction from its Cauchy data, **not an action-derived measurement of volume or orientation**. The two slots are coherent amplitudes, not independently measured classical branches or values obtainable by reading a single unknown wavefunction. The construction supplies no local apparatus that realizes the required amplitude map, and the rescaling uses a nonlocal-in-scalar-time operator. It therefore does **not** meet the operational turning-clock gate or pass B7. It shows exactly what additional mathematical data evades [the earlier node obstruction](GRAVITY_VOLUME_CLOCK_RECORD_OBSTRUCTION.md), rather than proving that a physical clock has access to it.

The parent action, ordering, continuum, incoming normalization, scalar-frequency sector and asymptotic record from [GRAVITATING_PROPER_TIME_CLOCK.md](GRAVITATING_PROPER_TIME_CLOCK.md) are assumed. No new matter action, independent derivation of quantum gravity, or claim of literature novelty is supplied.

## 1. One physical band, two boundary slots

Use the previous model's `mu=1`, `kappa_0=0.2`, `kappa_1=0.6`, incoming physical amplitudes `a_n(k)`, and `H_B=L²([2,8],dk) tensor C²`. For real continuum-normalized standing modes `f_(n,k)(x)` and incoming phases `u_n(k)` with `|u_n|=1`, define

    g_n(k,b) = f_(n,k)(b) / [sqrt(2k) u_n(k)],
    h_n(k,b) = (partial_x f_(n,k))(b) / [k sqrt(2k) u_n(k)],
    (J_b a)_n(k) = (g_n a_n, h_n a_n).

The first entry is the value-only map from the prior obstruction; the second is its log-volume derivative divided by `k`. The `1/sqrt(2k)` rigging factor is retained. Fourier transformation in scalar time identifies the positive-frequency boundary traces with these amplitudes. The inverse factor `1/k` is bounded on this band, but is a spectral operation, **not** a demonstrated finite-duration local derivative readout.

For each real `k>0` the two entries cannot vanish together: otherwise the unique solution of the second-order Morse ODE with zero value and derivative at `b` would vanish identically. Hence

    d_n(k,b)² = |g_n(k,b)|² + |h_n(k,b)|² > 0.

In particular, at the prior excited-channel node near `k=2.496546`, the value vanishes but `|h_1|≈0.3611`. A root at an isolated k is not itself a normalizable state; the uniform lower bound below applies to normalizable packets throughout the whole band.

## 2. Explicit band-uniform bounds, including the turning region

The dimensionless vector `y=(f,f'/k)` obeys

    y' = k [[0,1],[-1,0]] y + [[0,0],[U_n(x)/k,0]] y,
    U_n(x)=exp(2x)-2 kappa_n exp(x).

The first matrix is skew-adjoint. Grönwall's inequality in both directions, together with the unit-incoming-amplitude asymptote, gives

    sqrt(2/pi) exp[-I_n(b)/k] <= ||y(b)||
        <= sqrt(2/pi) exp[I_n(b)/k],
    I_n(b) = integral_(-infinity)^b |U_n(x)| dx.

The asymptotic norm is `sqrt(2/pi)`: each incoming and outgoing plane component of the normalized real mode has magnitude `1/sqrt(2pi)`. These inequalities do not require a WKB approximation. With `v=exp(b)` and `c=2 kappa`, the integral is exactly

    I(b,kappa) = c v - v²/2                 if v<=c,
                 v²/2 - c v + c²           if v>=c.

For any fixed `b_max>=0`, put `I_* = max_n I(b_max,kappa_n)`. Since the integral is increasing in b, for every `0<=b<=b_max`, both channels and the whole band,

    L = exp(-I_*)/(8pi) <= d_n(k,b)² <= H = exp(I_*)/(2pi).

The inequalities use `k_min=2`, `k_max=8` and `d²=||y||²/(2k)`. Thus `J_b` is bounded above and below, with a bounded inverse **on its image**, uniformly over the stated chart. No sampled minimum is used in this proof.

Concrete conservative bounds:

| Chart | `I_*` | `L` | `H` | `L/H` |
|---|---:|---:|---:|---:|
| `b=0` | 0.7 | 0.01976 | 0.32050 | 0.06165 |
| `0<=b<=1` | 2.76722 | 0.002500 | 2.53283 | 0.000987 |
| `0<=b<=b_*` | 33.88449 | `7.65e-17` | `8.27e13` | `9.25e-31` |

Here `b_*=log(0.6+sqrt(8²+0.6²))≈2.15437` is the largest classical turning log-volume over both channels and the band. The chart `[0,b_*]` contains **all** their classical turning points; `[0,1]` contains both turns for `k` near 2, but not every turn in the band. The full-chart success lower bound is so weak as to be operationally uninformative; it is an existence bound, not an estimate of a feasible rate. Other bands, `k` near zero, the full oscillator spectrum, other orderings, and quantum clocks outside this declared domain are not covered.

## 3. A common-space chart and the same records

Let `D_b=(J_b†J_b)^(1/2)`; it multiplies channel n by `d_n`. Its spectrum lies in `[sqrt(L),sqrt(H)]`. The polar isometry

    V_b = J_b D_b^(-1),       V_b† V_b = I_(H_B),
    P_b = V_b V_b†

embeds the physical sector in the two-slot output space. `V_b` and the transition `V_c V_b†` are bounded and continuous in b on this chart, including b values equal to the classical turning volumes. Their algebraic action does not divide by the classical `p_x` or `dV/dT`. This says the **Cauchy-data representation** is regular; it does not supply a physical clock Hamiltonian in volume or erase the classical two-crossing problem.

For any bounded physical/root effect `F`, transport the *same* event as

    F^(b) = V_b F V_b† on P_b,

with the orthogonal complement retained as a separate outside-image outcome when an output-space POVM is desired. For a root state `rho`, `Tr[V_b rho V_b† F^(b)]=Tr[rho F]`. For a supplied sequence of bounded complete root instruments `K_j`, transport each as `V_(b_j) K_j V_(b_j)†` and insert the image-to-image transitions. Their product telescopes to `V_(b_last) K_last ... K_1`, preserving every corresponding joint probability, post-state and failure label. This is a representation identity, not a construction of the `K_j` from an apparatus.

A concrete internal control uses the parent's asymptotic record `F_±=U†|±><±|U` and the oscillator number projectors `P_0,P_1`. Prepare the **specified** packet `a(k)=h(k)U(k)†|+>` (as in the previous note), measure number, then the same `F_±`. Every one of the four `(n,±)` outcomes has probability `1/4`, in the root representation and in each transported image representation. This is a sequential *supplied* record test; it is not an assertion that the Hamiltonian autonomously triggers either measurement at a volume crossing. The transport preserves any additional reference system because `V_b†V_b=I`.

## 4. A complete abstract recovery, with its real cost

Let `H` and `L` be the analytic squared-norm bounds for a chosen chart. The bounded Kraus operator

    A_b = J_b/sqrt(H)

can be completed by an explicitly retained failure `A_fail=(I-A_b†A_b)^(1/2)`. If its output lies in the two-slot space, a second, successful recovery is

    R_b = sqrt(L) D_b^(-1) V_b†,
    R_b A_b = sqrt(L/H) I.

`R_b` is a contraction because `D_b²>=L`; its failure operator is `(I-R_b†R_b)^(1/2)` on the entire output space, including `P_b`'s complement. Both stages are complete. For **every** normalized input, including inputs entangled with an untouched reference, the probability of success at both stages is exactly the chosen `L/H`, and the normalized recovered joint state is the original state. No unsuccessful branch is silently discarded when evaluating the complete process. The bound is conservative, and one could choose better certified constants; the table does not establish the actual optimal success rate.

This is a valid mathematical quantum instrument on the declared abstract spaces. Its Kraus operators are **stipulated**, not derived from the original lapse-coupled oscillator action. There is no established finite-volume interaction that implements the two-slot `J_b`, the recovery, its flags, energy cost or reference control. The nominal lower bounds are not experimental success probabilities. The classical chart turns are not automatically covered by a realizable device merely because a bounded mathematical filter exists.

## 5. Why the two slots do not yet solve orientation

The unitary change of slots

    q_in=(g-i h)/sqrt(2),     q_out=(g+i h)/sqrt(2)

approaches the incoming and outgoing plane-wave components in the small-volume free asymptotic region. At finite b it is only a local mathematical decomposition: the potential couples these components, and the labels are not proven eigenvalues of a physical expanding/contracting observable or timestamps of two crossings. Their amplitudes must be kept coherently. In fact, because `f` and `f'` are real and share the same incoming-channel phase, `|q_in|²=|q_out|²` pointwise in this standing-wave model. Assigning those equal weights as independent occurrence probabilities would be an unjustified extra instrument, not a derivation of two separate histories.

A concrete information-loss control underscores this. Take the two orthogonal incoming packets `h(k)U(k)†|+>` and `h(k)U(k)†|->`, with uniform `h` on `[2.49,2.50]`. In the full coherent image their trace distance remains 1. Apply the declared k-dependent detector/reference phase calibration that removes the common incoming and scattering conventions, then **trace both the jet slot and k**. The two remaining oscillator states have trace distance approximately `0.851774`. This is a stipulated coarse graining and calibration, not an unavoidable loss in every implementation. It shows that throwing away the auxiliary information can make distinguishable physical records less distinguishable; the image isometry is not equivalent to its partial trace.

## 6. Verification and what must come next

[The verifier](verification/gravity_volume_jet_reconstruction.py) computes the exact bound expressions, parent Morse modes and first derivatives, checks sampled chart inverses and the transported two-event probabilities, and compares 512/1024-panel quadratures for the coarse-graining witness. [The JSON receipt](verification/gravity_volume_jet_reconstruction.json) records the results. [Five tests](verification/gravity_volume_jet_reconstruction_test.py) check the old node, completed filter/recovery arithmetic, directional slot norm, input domains, and the two-event control. A separate 50-digit `mpmath 1.3.0` evaluation of Whittaker W and its derivative agreed to maximum absolute error `1.09e-14` in 24 sampled combinations of `k`, channel and `b`. Floating-point sampling and quadrature are numerical controls, not proofs of the analytic bound or of the parent continuum model. The analytic full-turning-chart bound is not inferred from the finite-volume numerical samples, which only cover `0<=b<=1`.

The decisive unresolved question is now sharper: can a **finite, gravity-coupled instrument**, on the same physical model and without an external clock, implement an orientation-sensitive crossing record or an equivalent reconstruction while retaining both outcomes, energy accounting and the same joint event? The proposed operation must specify its action, frequency-band and boundary domains, reference resources, errors and failure branches; its reading must distinguish expanding from contracting when claimed. A map merely naming a wavefunction derivative or an auxiliary flag does not pass this test. If a coupled apparatus requires changing the matter content or quantization, equivalence must be shown rather than presumed. **Follow-up:** the [source-coupled gradient-pointer test](GRAVITY_GRADIENT_POINTER_GATE.md) gives one explicit pointer extension and shows that this candidate's additional asymptotic record cancels against a source-matched reference. This is not a universal detector no-go.

B7 remains open, as do full inhomogeneous constraint closure and spacetime emergence (B6/B8), the phenomenal bridge, and the other substantive battery obligations. The external battery's reported preregistration, program, JSON and freeze are still unavailable for replay. No claim of a general solution of time or a passed formal battery follows.
