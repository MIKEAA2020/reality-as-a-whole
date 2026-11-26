# Joint-report constraints, correlation and calibrated reference transfer

## Result

The [previous pass](ZERO_ECHO_JOINT_QUALITY_AND_OWNERSHIP_REPORTS.md) screened quality and ownership candidates using separate report marginals. Here the complete two-bit report distribution is represented by three rates and tested against a 16-cell latent truth/report polytope. **Arbitrary dependence** between report errors is allowed.

A new, independently justified calibration of the *joint* response can rule out a candidate that passes both earlier marginal checks. The extra exclusion comes from the extra calibration—not from correlation alone. For a general selected population, the same polytope can give a sharper lower bound on jointly neutral, same-owner occurrences than the previous simple union bound. A rational primal/dual control gives an exact example; the general solver uses floating-point linear programming, so its outputs are numerical rather than formal certificates.

The echo and the extra response channel remain models. The reference labels, reporter identity, chosen quality bridge and witness-to-experience link are not established by the circuit or by these calculations. No empirical participant or actual phenomenal calibration was supplied. [Implementation](verification/zero_echo_joint_report_polytope.py), [tests](verification/zero_echo_joint_report_polytope_test.py).

## 1. What the joint table adds—and what it does not

Keep the previous anchor echo, selector `H=−`, and the same aligned reporter, two distinct checkpoints and joint protocol. `D=1` denotes neutral signed valence under a stated bridge; `O=1` denotes the same specified owner at the two checkpoints; `Y,W` are the corresponding affirmative reports. Neutrality does not mean no experience. This is a distribution over selected reporter-runs, not a subject census.

Let

```text
x[d,o,y,w] = P(D=d,O=o,Y=y,W=w),     d,o,y,w ∈ {0,1}.
```

There are 16 nonnegative cells with total one. The three rates `q_y=P(Y=1)`, `q_w=P(W=1)`, and `q_11=P(Y=W=1)` determine all four report-cell probabilities. The earlier four error assumptions become linear inequalities, e.g.

```text
P(Y=1,D=0) ≤ f_y P(D=0),
P(Y=0,D=1) ≤ g_y P(D=1),
P(W=1,O=0) ≤ f_w P(O=0),
P(W=0,O=1) ≤ g_w P(O=1).
```

They apply to the **selected, jointly administered protocol**, and are vacuous when the conditioning mass is zero. They impose no independence of Y and W, of the underlying truths, or of errors and sector selection.

Candidate A (pointer quality) sets `D=0`. Candidate B (type-symmetric quality) has `D=1` on R=−; if the physically justified selected-sector lower bound is L, require `P(D=1)≥L`. P sets `O=1`, F sets `O=0`. These four combinations preserve the original stipulated models; neither family is exhaustive.

An important limitation is that **knowing report correlation alone does not supply a new reference calibration**. With no extra joint-response constraint, a true-rate table satisfying the earlier candidate marginal conditions can be constructed in this outer model: A has `q_y≤f_y`; B has `q_y≥L(1−g_y)`; P has `q_w≥1−g_w`; F has `q_w≤f_w`. For B choose a suitable D assignment conditional on Y; assign W according to the observed joint table. Thus there is no generic candidate separation purely from correlation under those loose assumptions. With finite intervals, jointly enforcing all three rate intervals can still improve on separate marginal screens because one underlying table must satisfy them simultaneously.

## 2. An additional joint-reference premise

Suppose a separately justified, population-matched reference procedure also bounds

```text
P(Y=0 or W=0 | D=1,O=1) ≤ h.
```

This is the probability that **at least one** of the two affirmative responses fails on a genuinely neutral, same-owner target. It is not the probability that *both* fail. It has to be measured or otherwise warranted for that jointly administered protocol and target; individual error bounds do not automatically imply an arbitrarily chosen h. In particular, knowing separate errors are each at most .1 generally only gives the weaker union bound h≤.2 for the same relevant conditional population, if those bounds have actually been shown to hold there. Conditioning on D=O=1 can itself change the error rates, so even that transfer must be justified. If `P(D=1,O=1)=0`, the homogeneous inequality is vacuous.

For B/P, `P(D=1,O=1)≥L`, so directly

```text
q_11 ≥ L(1−h).
```

This is a simple analytic exclusion rule using the full matched joint response and the extra h premise. More generally, minimize `P(D=1,O=1)` over all 16 cells subject to the confidence intervals and the five homogeneous error constraints. For a candidate test, add its D/O constraints. The LP is an **outer relaxation**: it does not impose every possible echo-sector, timing, apparatus or clock constraint. Infeasibility rules out the candidate under the included assumptions and confidence event; feasibility is not a proof of compatibility with the complete physical model, nor proof of the candidate.

Numerically, the code first minimizes a common nonnegative slack on all inequalities, retaining normalization and positivity. A slack above `10⁻⁸` is reported as a numerical rejection; tiny borderline infeasibilities are indeterminate, and optimization failures raise errors. Even a positive slack is not an exact-arithmetic infeasibility certificate. The analytic inequality above independently verifies the main example's exclusion with a substantial margin.

## 3. Exact sharper positive bound in one case

Take exact report rates `q_y=.82`, `q_w=.90`, `q_11=.77` and independently warranted false-positive bounds `f_y=f_w=.1`. Do **not** assume any miss-rate or joint-response bound for this example. The preceding direct union bound gives `.7125`.

In this case, a stronger exact bound is

```text
t = P(D=1,O=1) ≥ q_11 + (q_y+q_w−2)/9 = 133/180 ≈ .738889.
```

For a check independent of the numerical solver, on each of the 16 atoms define

```text
e_y = (1−D)(Y−1/10),   e_w = (1−O)(W−1/10).
```

Each atom satisfies

```text
D O − Y W − (Y+W−2)/9 + (10/9)(e_y+e_w) ≥ 0.
```

The two calibrated false-positive assumptions give `E[e_y]≤0`, `E[e_w]≤0`, establishing the bound. It is **sharp for these specified rates and bounds**, as shown by the following exact hypothetical distribution, with all unlisted cells zero:

| (D,O,Y,W) | Probability |
|---|---:|
| (0,0,0,0) | 1/20 |
| (0,1,0,1) | 13/100 |
| (0,1,1,1) | 1/50 |
| (1,0,1,0) | 1/20 |
| (1,0,1,1) | 1/90 |
| (1,1,1,1) | 133/180 |

It has the three specified report rates, saturates both false-positive bounds, and attains `t=133/180`. This is a mathematical adversarial table, not observed testimony. The code's general minimum is numerical and subject to its solver tolerances; exact sharpness above is independently certified only for this particular example.

## 4. Finite confidence and nonidentical independent trials

For an extended calibration run use eight separately matched batches for `p,e_−,e_+,f_y,g_y,f_w,g_w,h`. The last counts joint-response failures among independently justified D=O=1 reference targets. Allocate total δ equally to eight one-sided calibration events and three two-sided report-rate events. For batch size n the one-sided radius is `sqrt[log(11/δ)/(2n)]`; the data-rate radius is `sqrt[log(22/δ)/(2N)]`. Clip bounds to [0,1], use the lower p bound and upper error bounds, and obtain L from the previous physical selection formula. The same single simultaneous confidence event covers all four candidate LPs and the general prevalence LP; no additional multiplicity charge is needed merely for inspecting the four on that event.

Hoeffding concentration also applies if trials are **independent within each batch but not identically distributed**. Then the targets are averages of their trial distributions: the latent `x` is the pooled average table and the three report rates are its marginals. Y and W within a trial may be arbitrarily dependent, and the separate batches need not be mutually independent for the union bound. Crucially, reference-batch average errors must still be justified as bounds on the **pooled, condition-weighted** errors of the target table—not merely on an unweighted average of trialwise conditional errors. The L bound must refer to the same pooled selected population; if selection probabilities vary, the preselection mixture must use the selection-weighting appropriate to that target. Neither condition follows from concentration alone.

This extension does not handle correlated or adaptively chosen trials. Shared memory, serial drift or common latent noise can invalidate an independent-trial radius. Non-iid independence is a weaker assumption than iid, not a solution to arbitrary trial dependence. Both models also presuppose independently warranted truth references, clock alignment, target/reporter correspondence and transfer across selection and intervention.

## 5. Hypothetical comparisons

For illustration alone, suppose each of the eight calibration batches has 100,000 trials; p has 50,000 negative-sector counts and each error batch has 10,000 error counts. For δ=.05 the resulting bounds include

```text
L ≈ .89284,       h_U ≈ .10519,       L(1−h_U) ≈ .79892.
```

Consider a **hypothetical** N=10,000 table `(k11,k10,k01,k00)=(7200,1000,1800,0)`, so `q̂_y=.82`, `q̂_w=.90`, `q̂_11=.72`. Its three-rate interval radius is about `.01745`, and `q_11` is at most `.73745` on the confidence event. The previous marginal screen retains B/P, while the new reference premise implies `q_11≥.79892`: B/P is excluded, with analytic gap about `.06147`. The relaxed LP reports common slack about `.01622`. Removing the h premise by setting h=1 makes B/P numerically feasible again. All four candidate combinations are excluded in this example; that could indicate a different quality/ownership rule, a failed calibration or another violated premise. The example's reference counts are not empirical evidence.

As a compatible control, use the prior synthetic echo generator with all nominal error rates `.1` and the upper Fréchet coupling. Under B/P it gives the exact selected report table `(11,10,01,00)=(.82,0,.08,.10)`; its conditional joint failure on `D=O=1` is `.1`. A simulated 10,000-run sample with seed 204204 gives `(8198,0,826,976)`. With the same **hypothetical** calibration counts, the LP does not reject B/P and rejects the other three in this example. The simulation explicitly implements a correlated channel; it does not establish such a witness or its experiential truth. The earlier midpoint-coupled synthetic channel is a different joint protocol and must not silently inherit this `.1` h calibration.

## 6. Continue the why-chain

- The new discriminating information is a constraint on a joint response **conditional on a jointly warranted experiential and ownership target**. The physical report table cannot certify that condition by itself; assigning the references via the favored bridge would be circular.
- A joint protocol can change access, response dynamics or memory relative to separate tests. Subject alignment, distinct checkpoints, reference labels and transport between clocks or populations require independent support. Sharing records does not imply a shared subject, nor does one reporter exhaust possible subjects.
- Stronger statistical exclusion distinguishes stipulated candidates under premises; it does not derive actual incidence, the experiential bridge, or the causal constitution of an experiencer. It must not equate neutral scalar with nonexistence or cancel real negative experience against an opposite model contribution.
- The upstream self-sufficient-whole question remains: why this carrier, lawful differentiation, actual subject relation and measure rather than alternatives? The model helps expose dependencies but does not settle necessity, actuality or prove an ultimate explanatory stopping point.

## Next work

- Construct and assess a specific physically realizable joint interface, including correlated backaction, timing, and the transfer conditions that could make an independently justified joint reference meaningful.
- Analyze dependence **between** repeated trials with an explicit predictable-error, martingale or block model and match its estimand to incidence rather than applying an iid bound by default.
- Link the physical selection and reporter protocol to multiple, potentially overlapping subject candidates without treating selected response fractions as a complete census.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_echo_joint_report_polytope_test -v
```

The tests verify the rational certificate, arbitrary latent tables, a correlated echo-channel control, heterogeneous pooled targets, calibration inputs and numerical candidate screening. They do not validate experiential labels, the actual joint interface, physical locality or foundational necessity.
