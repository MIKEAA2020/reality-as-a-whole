# Imperfect support flags: the calibration root

## Result

The preceding [coherent readout](ZERO_TWO_WINDOW_SUPPORT_AND_COHERENT_READOUT.md) replaced an assumed packet-span restriction with an **ideal** outside-span flag. This continuation allows false positives and missed outside events. Given a justified *uniform* bound on the missed-flag probability, it derives a finite-shot bound that also accounts for outside events contaminating the accepted tomography data. In a simulated 100,000-shot-per-batch example, the bound on the original history-distribution error is about **0.226** at 95% confidence.

The deeper limitation is that a uniform missed-flag bound is not established by checking finitely many outside states. A concrete alternative detector passes a calibration on one outside state yet makes another outside state exactly indistinguishable from a state inside the span, while the two states predict very different original clock histories. In the continuum, any finite collection of finite-shot reference calibrations leaves arbitrarily weakly tested outside directions. The detector model or additional physical constraints must therefore justify the uniform bound; it cannot be inferred just from a few successful examples.

These are statements about specified quantum instruments and statistical assumptions, not a demonstration of a physical clock or an impossibility theorem for all calibration methods. [Verification](verification/zero_two_window_imperfect_support_flag_test.py) supplies the finite regulated examples.

## 1. A noisy flag model

Keep the same two-packet isometry B, support projector `P=BB†`, complement `Q=I−P`, four tetrahedral inside effects `F_j` and fixed, uncorrelated logical h preparation as in the [preceding report](ZERO_TWO_WINDOW_SUPPORT_AND_COHERENT_READOUT.md). On the geometry–apparatus factor, allow the *reported* five-outcome POVM

```text
G_j = (1−f) B F_j B† + S_j,       j=1,…,4,
G_flag = f P + Q − S,             S=Σ_j S_j,
0 ≤ S ≤ β_max Q,                   S_j ≥ 0 supported on Q,
f_min ≤ f < 1.
```

The inside state has a uniform flag false-positive probability f, independent of its qubit direction. An outside state can have arbitrary label statistics and miss probability up to β_max. The POVM is block diagonal in P/Q; this matters: it makes the inside labels a mixture of the projected-state distribution and missed-outside labels even when the input has P–Q coherence. This is a specific detector-error class, not the most general noisy instrument. Reference states, four inside-label calibrations, fixed h and stable independent copies remain assumptions.

For input ρ define `λ=Tr(Qρ)` and q as its flag probability. Positivity and the stated operator bound imply

```text
q ≥ f_min + (1−β_max−f_min) λ.
```

For N unknown-state trials with k flags, form the same one-sided upper bound `q_U` as in the previous report:

```text
q_H = min[1, k/N + sqrt(log(12/α)/(2N))],
q_0 = 1−(α/12)^(1/N)  if k=0, otherwise 1,
q_U = min(q_H,q_0).
```

The two failure budgets α/12 sum to α/6. When `q_U<f_min`, the assumed model is inconsistent on that confidence event and the procedure aborts. If `d=1−β_max−f_min>0`, otherwise use the trivial upper bound:

```text
λ_U = min[1, max(0,(q_U−f_min)/d)]  if d>0;   λ_U=1 otherwise.
```

The accepted inside labels are contaminated by missed outside events. If their outside fraction is γ, then on the same event

```text
γ ≤ γ_U = min[1, β_max λ_U/(1−q_U)]   when q_U<1;
γ_U=1 otherwise.
```

This bound permits any distribution of missed outside labels. It uses the assumption that the four P-block label probabilities are all scaled by the **same** `1−f`, so conditioning on acceptance does not distort the reference qubit distribution. Arbitrary state-dependent false positives or off-diagonal P–Q detector effects require another analysis.

## 2. Finite-shot prediction bound

Use four independently prepared reference batches `z+`, `z−`, `x+`, `y+` and the unknown batch. Permit false flags even in the reference batches; discard flagged runs and use their accepted inside labels, aborting if a batch has no accepted observations. Calculate `ĉ`, `L̂`, `r̂`, `e_c` and `e_L` from those accepted outcomes exactly as in the prior report. Allocate failure probability α/6 to each of the five inside-label concentration events and α/6 to the flag bound. If `L̂` has full column rank, the projected Bloch estimator has radius

```text
R = min[2, (e_target+e_c+e_L+sqrt(2) γ_U)/σ_min(L̂)].
```

The extra term arises because the Euclidean distance between two four-outcome probability vectors is at most √2. On the joint confidence event, `||r̂−r_P||≤R`, where `r_P` is the normalized P-projected state. Combining this with the projection trace-distance bound gives

```text
TV(original-history prediction, actual distribution)
 ≤ min[1, sqrt(λ_U)+R/2]
```

with probability at least `1−α`, for the same original history procedure applied to independently prepared copies. The result covers coherent P–Q inputs, but remains conditional on the fixed, uncorrelated h preparation, the error-operator bound, reference states, independent sampling and correctly modeled target procedure. Confidence in shot statistics does **not** establish those premises.

At `β_max=0` and `f_min=0` this reduces to the earlier perfect-flag bound. If `β_max=1` and there is no other detector constraint, the support bound is 1 and the prediction guarantee becomes trivial.

## 3. Noisy-flag simulation and sensitivity

In the N=40 model, choose a pure coherent input with true leakage 0.01, true f=0.005 and true outside-miss probability 0.08. Missed outside events are deliberately biased toward one inside label. Give the estimator the valid assumptions `f_min=0.005` and `β_max=0.10`, with 100,000 independent shots in each of the five batches and seed 9824. The unknown batch has 1,400 flags. At α=0.05:

```text
q_U=0.019235,    λ_U=0.015905,    γ_U=0.001622,
σ_min(L̂)=0.263371,    R=0.200749,
95% TV bound for the original history = 0.226489.
```

The actual modeled error for this realization is about 0.005947. Its true leakage and detector rates are supplied by the simulation, not inferred facts about an experiment. An independent bound on worst-case misses and on false-positive behavior is indispensable. If a bound on f_min is itself estimated, its calibration uncertainty must be added to the confidence budget.

For the same observed counts, taking β_max=0.5 makes the conditional TV bound approximately 0.305; β_max=0.9 makes it approximately 0.852; β_max=1 makes it 1. Smaller guessed β_max values can produce attractive but **invalid** confidence claims if the true detector exceeds them. The verifier also constructs a 20%-leakage example with every outside event missed: falsely assuming β_max=0 returns a tiny support bound, whereas the honest β_max=1 bound is trivial.

## 4. A detector that passes one outside test and misses another

At N=40 let u be the incident packet inside P and let x,y be two mutually orthogonal outside vectors. Choose the same F_j as the tetrahedral construction and set `p_j=⟨u,BF_jB†u⟩`. Define

```text
G_j = B F_j B† + p_j |x⟩⟨x|,
G_flag = Q − |x⟩⟨x|.
```

These five effects are positive and sum to I. The outside test state y flags with probability 1, yet x is **never** flagged and has precisely the same four inside-label probabilities as u. No number of repetitions of this one fixed readout distinguishes u from x. The two preparations nevertheless give original 32-history distributions with TV distance approximately **0.426301**. The model specifies the associated instrument via square roots of the effects; it is a counterexample to an inference from this calibration, not a claim that the proposed real device behaves this way.

This construction generalizes. For any finite set of outside calibration vectors spanning a proper subspace of Q, choose x orthogonal to all of them and construct the same hidden direction. In the infinite-dimensional Q space, even a finite collection of arbitrary mixed calibration states cannot be used with a finite number of trials to establish a **uniform** bound without additional detector structure: for an orthonormal sequence x_n in Q, each trace-class calibration state has `⟨x_n,ρ_i x_n⟩→0`. A detector with a single undetected x_n changes each specified calibration distribution by an arbitrarily small amount, while its worst-case missed-flag probability remains 1. For finitely many fixed batch sizes the joint calibration distributions can therefore be made arbitrarily close. This is an adversarial calibration observation under the allowed POVM class—not a claim that every physical apparatus is adversarial, or that a proven dynamical/operator constraint cannot exclude the defect.

## 5. Why this is the remaining issue

The original weak response could be improved by specifying a global coherent-mode instrument, but its support guarantee now depends on the detector's behavior on **all** outside directions. The empirical examples can test selected modes; an operator-level bound needs an independently justified design, controlled dynamics, a restricted source class, or another validated physical premise. Each is a different route, and simply declaring the instrument perfect transfers rather than explains the burden.

The model still assumes a scalar reference, homogeneous band-projected constraint, logical preparation, detector and source. It does not prove a local autonomous apparatus, general quantum-gravity clock equivalence, actual subjectivity or the derivation of physical–experiential order from zero. The next useful physical question is whether a specified implementable interaction supplies a verifiable error bound on a justified sector, with its resources and backaction retained.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
  verification.zero_two_window_imperfect_support_flag_test -v
```
