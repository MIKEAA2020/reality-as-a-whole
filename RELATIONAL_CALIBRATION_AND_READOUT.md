# Physical calibration, field readout and a separate quantum instrument

**Status.** A covariant classical model now includes a sign-reference field and a separate readout field, in addition to the clock, rods, signal, detector and gravity. Their energy belongs to the same Einstein constraints. A controlled linear-amplitude calculation transfers the signal's sign **relative to the reference** into the readout field. Separately, an exact finite-dimensional quantum instrument quantifies how imperfect reference alignment and memory noise limit that information.

These are **two distinct constructions**, not yet a quantization of one another. The field calculation uses a backreacting reference cosmology but does not evolve inhomogeneous nonlinear gravity. The quantum instrument is not derived from the covariant field action, and its probability numbers are not predictions for that field experiment. Neither establishes a durable physical quantum record or refoliation invariance.

Reference-frame twirling and symmetry-limited measurements are established, not new: see [Bartlett, Rudolph and Spekkens](https://arxiv.org/abs/quant-ph/0610030) and [Marvian and Spekkens](https://arxiv.org/abs/1212.3378). For covariant quantum-field probe measurements on a **fixed** spacetime, see [Fewster and Verch](https://arxiv.org/abs/1810.06512). The explicit combined test here is an interface calculation; research priority is not established.

## 1. Add a physical reference and a readout

Start from [the previous action](RELATIONAL_MATTER_DETECTOR_GRAVITY.md) and its signal/detector coupling `lambda W_1(T,theta) Phi chi`. Add a real scalar sign reference `R` and readout field `D`, and use the potential

    V = lambda W_1 Phi chi + g W_2 R chi D
        + kappa (Phi²+chi²+D²)² + kappa_R (R²-v²)²/4,

with kinetic terms `-1/2 (grad R)² -1/2 (grad D)²`, `kappa,kappa_R>0`, fixed `v>0`, and bounded smooth `W_1,W_2` on the clock-and-rod target space. The quartic terms stabilize the potential at large field values. They do not guarantee positivity at every field value. Nothing in the action fixes a coordinate event: the windows are functions of physical reference fields.

For `R=+v` or `-v` homogeneous, its momentum zero, and `D=chi=0` on the initial slice, the added fields and their potential contribute zero to the initial constraint. The previously constructed exact small-amplitude classical initial data therefore still apply. This is an idealized reference: a nonzero homogeneous classical order parameter at a zero of its potential is supplied. It is not a proof that preparing or maintaining a sharp quantum reference costs no energy.

The action has two independent sign symmetries:

    A: (Phi,chi,D) -> (-Phi,-chi,-D),  R unchanged;
    B: (R,D) -> (-R,-D),              Phi and chi unchanged.

Their product flips `(Phi,chi,R)` and leaves D unchanged. Thus, for corresponding sign-related classical initial data and common smooth evolution, the metric, clock and rods are exactly the same while the readout sign is controlled by the **relative** orientation of signal and reference. In particular, simultaneous reversal of both signal and reference leaves D unchanged. This covariance/symmetry argument includes the fields' classical stress-energy; it is not a numerical calculation of their nonlinear evolution.

Whether these internal symmetries are global physical symmetries or gauge redundancies is a separate model choice. D is invariant under the **diagonal** reversal A B, but not under A and B individually. If the full independent sign group is gauged, D's sign is not itself observable and an additional reference/observable specification is needed. We do not silently gauge one subgroup and claim invariance under the whole group.

## 2. Two finite interaction windows

Use the same expanding background, winding rods and scalar clock as in [the sign-information test](RELATIONAL_SIGNAL_GEOMETRY_NO_GO.md), with `f=1/2`, clock momentum `tau=3/2`, and initial `Phi=epsilon cos z`, `chi=D=0`, all their canonical momenta zero. Put `R=v` and its momentum zero. The background satisfies the *full* gravity–reference equations; perturbative metric and reference corrections start at order epsilon². The homogeneous sign reference is at a potential minimum.

In the linear field-amplitude calculation, the first clock-window `0<T<0.4` uses the previously specified pulse

    W_1(T,theta)=F_1(T) [1+cos(theta^3)].

It transfers signal into the zero cosine mode `C` of `chi/epsilon`, with `C=lambda+O(lambda³)` and `C'=O(lambda³)` immediately after the window.

For the second window `[T_a,T_b]=[0.42,0.62]`, define another smooth step `G_2` in the same way as the earlier bump-normalized `G`, and take

    W_2(T,theta)=F_2(T),
    F_2(T)= -tau² G_2''(T)/a(T)^6 inside the window, zero outside.

This second profile is spatially uniform. To leading order in lambda and g, the zero cosine mode `D_0` of `D/epsilon` obeys

    D_0'' = -g v a^6 F_2 C/tau²,
    D_0 = lambda g v G_2(T) + higher coupling orders.

So its post-window displacement is proportional to the product of the sign of the initial signal and that of the physical reference. The pulse is intentionally designed from the known background and first detector response, not derived by optimization or a fundamental principle. The measured quantity here is a global rod-space average, not an implementable local readout.

### Numerical field test

[The verifier](verification/relational_calibrated_readout.py) evolves the coupled signal, detector and readout Fourier modes in clock time, including the reciprocal effect of the readout on chi **within the linear-amplitude approximation**. With `lambda=g=0.01`, `v=1`, ten cosine modes and 3,200 RK4 steps, it finds:

| T | detector mean / epsilon | readout mean / epsilon | readout clock slope / epsilon |
|---:|---:|---:|---:|
| 0.40 | 0.009999865 | 0 | 0 |
| 0.62 | 0.009999411 | 0.00009999858 | -1.23e-9 |
| 0.80 | 0.009997666 | 0.00009999835 | -1.23e-9 |

Single signal or reference sign reversal flips the readout; reversing both leaves it unchanged. Setting g to zero gives zero readout, and halving both couplings reduces the readout by a factor approximately four. Comparing modes 0–7/1,600 steps with modes 0–10/3,200 steps changes the T=0.8 readout by about `6.7e-18`; this does not provide a rigorous global numerical error bound. [The JSON](verification/relational_calibrated_readout.json) contains the actual output.

The small residual slope is not zero, and higher field amplitudes activate nonlinear gravity and the quartic interactions. We have not simulated those effects, controlled the reference's later dynamics, or shown persistent storage. The homogeneous reference has physical stress-energy in the action, but its ideal initial data happen to have zero reference energy; subsequent coupling and fluctuations need not.

## 3. Separate exact quantum calibration and memory test

We now switch explicitly to an **abstract qubit model**, not a quantization of the above field system. Let signal A and reference R each be a qubit. Impose only the simultaneous parity `P=Z_A Z_R`, and let memories `M_1,M_2` be parity-neutral. Given a signal sign `s=+1` or `-1` and reference polarization `0<=r<=1`, prepare before twirling

    rho_A,s = (I+s X_A)/2,       rho_R = (I+r X_R)/2.

With no external diagonal sign orientation, apply the standard group twirl:

    rho_s = [rho_A,s tensor rho_R + P(rho_A,s tensor rho_R)P]/2
          = [I + s r X_A X_R]/4.

The relative observable `X_A X_R` is parity invariant. The two density matrices have trace distance r, so no measurement on this pair can guess s with equal-prior success above `(1+r)/2`. The invariant projective measurement `Pi_±=(I±X_A X_R)/2` attains that bound. If r=0, the two twirled states are identical and no subsequent channel can distinguish them. This is a concrete calibration resource bound, not a universal bound for arbitrary reference states or groups.

### Complete two-memory instrument

Initialize the two memory qubits in `|00>`. An invariant unitary writes the parity result to both:

    U = Pi_+ tensor I_(M1 M2) + Pi_- tensor (X_M1 X_M2).

Then independently flip each memory bit with probability `q`, where `0<=q<=1/2`. For recorded outcome `m=(m1,m2)` and input state rho, define `t(m|k)=(1-q)` for `m=k` and `q` otherwise. The complete system instrument is

    I_(m1,m2)(rho) = sum_(k=0,1) t(m1|k)t(m2|k) Pi_k rho Pi_k,
    Pi_0=Pi_+,  Pi_1=Pi_-.

These are completely positive maps, and summing all four outcomes gives a trace-preserving channel. The two memories record the same underlying projector outcome before their independent noise; they do not provide two independent copies of the original unknown state. Their readout and noise are stipulated channels, not derived from the field action.

For `r=3/5`, `q=1/10`, all joint probabilities are:

| signal | 00 | 01 | 10 | 11 |
|---|---:|---:|---:|---:|
| + | 0.65 | 0.09 | 0.09 | 0.17 |
| - | 0.17 | 0.09 | 0.09 | 0.65 |

The total-variation distance of the two complete outcome distributions is `12/25=0.48`, giving optimal equal-prior success `37/50=0.74`. The general value for these two noisy memories is `r(1-2q)`; ties contain no sign information. Without a polarized reference (`r=0`) it is zero. The optimal result with the noisy memories is smaller than the ideal pair-state bound r, as it should be.

The verifier constructs the twirled two-qubit state and the full four-qubit memory unitary with exact rational matrices, verifies unitarity and all outcome probabilities, and then applies the independent classical bit-flip channels. The result is exact for this finite instrument; it supplies no numerical relation between r and the classical scalar v.

## 4. What remains open

Follow-up: [QUANTUM_FIELD_RECORD_EMBEDDING.md](QUANTUM_FIELD_RECORD_EMBEDDING.md) builds a finite-mode quadratic quantum-field readout controlled by an ideal reference qubit, with a complete two-memory instrument. It yields nearly chance-level success in the selected parameters and still does not quantize the full gravitational model or control the dropped interactions.

- The classical field action gives a **physical calibration mechanism** and exact symmetry relations, but its calculated readout is leading-order, globally averaged and classically noiseless. It is not a complete record instrument.
- The qubit instrument gives complete probabilities and post-selected channels, but its reference, memory, gates and noise are supplied. It has no constructed gravitational constraints, stress-energy, localization, clock resolution or continuum field embedding.
- The two constructions share an operational pattern—relative sign plus a neutral record—but are **not mathematically identified**. Establishing a controlled map from quantized relational field modes to the qubit instrument is the next substantial task.
- A physical readout and stored memory require their own dynamical implementation and backreaction, not merely an additional symbolic pointer. No comparison of the same event across nonlinear gravitational foliations has been made.
- The exact classical symmetry still excludes unique inference of this signed readout from geometry and clock/rods alone in the selected model, under the stated treatment of the sign symmetries. It does not resolve consciousness, the problem of time, or the user's broader zero-residue goal.
