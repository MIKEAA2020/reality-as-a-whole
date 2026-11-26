# Can the two quality bridges be distinguished on the echo?

## Result

The [joint occurrence candidate](ZERO_ECHO_OCCURRENCE_QUALITY_INCIDENCE_JOINT_CONSTRAINT.md) left a real choice between a pointer-dependent scalar and a type-symmetric scalar. On the **same** recorded echo, their structural predictions agree when the echo record is positive and differ when it is negative. This pass makes the potential comparison operational without treating a physical bit as an experience.

A conditional result follows: if a separately justified quality witness can distinguish **neutral signed valence** from nonneutral valence and if the selected negative-record population is sufficiently clean, the two proposed bridges imply disjoint witness-rate ranges. The sector selector may be noisy, and its errors need not be independent of witness errors. A finite-shot procedure also allocates confidence to physical selection and witness calibration rather than assuming their rates are known.

This is a **proposed discrimination**, not an observation or proof of a physical–experiential identity. In particular, a structural zero in one candidate is not absence of experience, and its positive counterpart does not erase a negative experience. [Calculations](verification/zero_echo_quality_bridge_discrimination.py) and [tests](verification/zero_echo_quality_bridge_discrimination_test.py).

## 1. Compare two bridges on the same physical state

At the existing anchor, let `M=s`, `J=j`, `R=r` and

```text
N=Q_now=MJ,       K=Q_echo=MJR,       G=|u(u+1)|.
```

For the specified four-bin echo, `G>0` in every supported bin and `P(R=−)=P(R=+)=1/2`. Consider the two **structural** scalars already exposed by the preceding pass:

```text
A: v_A=G M,
B: v_B=G(N+K)/2.
```

Both are odd under the stipulated sign counterpart and invariant under the specified type exchange. Their supported values are

```text
R=+:  v_A=v_B=G s;
R=−:  v_A=G s,    v_B=0.
```

The agreement in the positive sector uses the actual supported J values, not a universal operator identity. Under the physical `1/8` event table, A has positive and negative model values with weights `1/2` each; B has positive and negative values with weights `1/4` each and zero scalar with weight `1/2`. Both signed means are zero. B's vector `(N,K)` remains nonzero in its disagreement sector even though this particular scalar vanishes.

A **phenomenal bridge hypothesis** would have to say why `v_A` or `v_B` equals a particular subject's signed valence in the specified time window, and why zero has the declared *neutral-valence* meaning. Those are alternatives being tested, not consequences of the physical matrices. Neutral valence can still be an experience with other qualities; it is not unconsciousness or nonexistence. The actual negative branch, if identified with suffering, is not removed by aggregate cancellation.

The original saved-J protocol supplies a physical comparison report `H=zJ=R` on its ready supported sector. The new verifier propagates that recorded echo for three original complex source vectors and both pointer signs, and checks that the report identifies precisely the sector where the two structural scalars differ. L, H, their ready states and their control gates remain added resources. Neither H nor the sign pointer is thereby a report of feeling.

## 2. Why sector selection matters

Suppose one selects runs reported as `H=−`, but the physical report has error. In the target population **before H selection**, let

```text
p = P(R=−) ≥ p_L,
P(H=+ | R=−) ≤ e_−,
P(H=− | R=+) ≤ e_+.
```

The p and error bounds must describe the same preparation, time and reporter population. The clean model gives p=`1/2`, but its value is not assumed exact if the source can drift. For `p_L(1−e_−)>0`, the selected negative-sector fraction satisfies

```text
P(R=− | H=−) ≥ L
L = p_L(1−e_−) / [p_L(1−e_−)+(1−p_L)e_+].
```

If this denominator cannot give a positive guarantee, use the conservative bound `L=0`. The formula is monotone in the relevant directions and is sharp when the limiting rates are attained. A separately calibrated B/R measurement, or another independently justified physical reference, is needed to bound these rates; H cannot validate its own ground truth. Any changes to the physical state from obtaining that reference must be accounted for.

## 3. A conditional quality witness

In the selected `H=−` ensemble, suppose a witness Y answers whether the target subject's signed valence is neutral. Let `Y=1` mean neutral, and suppose its error bounds **in that selected population** are

```text
P(Y=1 | truly nonneutral, H=−) ≤ f,
P(Y=0 | truly neutral, H=−)    ≤ g.
```

Use the equivalent joint-probability inequalities when a conditioning event has zero probability. A first-person observation of one's own experience is evidence in its own right; reducing it to a physical bit, aligning it to the model's subject and window, and establishing numerical errors are additional tasks. The proposed finite model provides no such witness or calibration.

Let `q=P(Y=1 | H=−)`. If the phenomenal interpretation of bridge A is true, all selected supported events are nonneutral; if B is true, at least fraction L is neutral. Therefore

```text
A: q ≤ f,
B: q ≥ L(1−g).
```

The inequalities do **not** require independence between physical sector-selection errors and witness errors: f and g are already required to hold after that selection. If `f<L(1−g)`, no single q satisfies both bounds. If the inequalities overlap, this pooled witness rate need not discriminate; other data or stronger assumptions may still do so. Either bridge or both can fail, since the candidates are not exhaustive.

Selection can matter even when the witness is informative in isolation. Take `p_L=.5`, `e_−=e_+=.1`, giving `L=.9`, and set `f=.81`, `g=.1`. Although `f+g=.91<1`, the selected bounds meet at `q=.81`. An allowed A witness with false-neutral rate `.81` and an allowed B witness with sensitivity `.9` and zero false-neutral rate produce that same **pooled selected rate**. This does not assert that their full joint distributions or all possible experiments are identical.

## 4. A finite-shot plan, including calibration uncertainty

On `N` iid accepted `H=−` runs let k be neutral answers. A two-sided Hoeffding event gives

```text
q̂=k/N,     R_data=sqrt[log(2/δ_data)/(2N)],
q_L=max(0,q̂−R_data),    q_U=min(1,q̂+R_data).
```

On this event, reject A if `q_L>f`; reject B if `q_U<L(1−g)`. Not rejecting a bridge is not proof of it. An observed rate in the gap can reject **both**, warning that the two bridges or the calibration/selection premises are inadequate.

The verifier also implements one concrete joint uncertainty budget. Collect five matched calibration batches for `p`, `e_−`, `e_+`, `f`, `g`, with observed Bernoulli count `k_x` out of `m_x`. For total failure budget δ, allocate `δ/6` to each calibration and `δ/6` to the two-sided witness data event. One-sided Hoeffding bounds are

```text
r_x = sqrt[log(6/δ)/(2m_x)],
p_L = max(0, k_p/m_p − r_p),
e_−, e_+, f, g = min(1, observed rate + corresponding r_x).
```

Insert these bounds into L and the data tests above. A union bound gives at least `1−δ` simultaneous sampling coverage **if** each batch has the stated iid target population and independently justified reference labels. Mutual independence *between* batches is not needed for this union bound. Calibration of f and g presupposes independently justified knowledge of relevant neutral and nonneutral reference experiences; merely using A or B to label the references would be circular. If a required reference batch is unavailable, the code rejects the input rather than declaring its error rate zero.

### Synthetic illustration—not a report from an experiencer

For illustration, the code defines a synthetic iid channel with physical H error rates `.1` in each sector and a neutral witness with false-neutral and missed-neutral rates `.1`. Its conditional selected neutral probabilities are

```text
A: q=0.10,       B: q=0.82.
```

The B rate is `.9×.9 + .1×.1`: its selected ensemble is 90% negative sector, and the synthetic witness has `.9` neutral sensitivity and `.1` false-neutral rate. These channel assumptions are made to generate a numerical control; neither witness error independence nor this exact channel is required for the inequalities in section 3.

Using a reproducible random seed separately for each synthetic case, 1,000 accepted answers give **86** neutral answers under A and **834** under B. Now suppose, separately and hypothetically, five calibration batches each have 100,000 trials: 50,000 negative-sector references for p and 10,000 errors in each of the other four batches. With total `δ=.05` split six ways,

```text
p_L≈.49511,     e_−,e_+,f,g upper bounds≈.10489,
L≈.89326,       B's neutral-rate lower bound≈.79956,
R_data≈.05235.
```

The 86-answer sample yields `[q_L,q_U]≈[.03365,.13835]`, rejecting B but not A on the simultaneous confidence event. The 834-answer sample yields `[.78165,.88635]`, rejecting A but not B. A hypothetical count of 400 yields an interval strictly between the two implied ranges and rejects both. The calibration counts and all error channels are **hypothetical**; there are no experimental data or validated phenomenal reference states here.

## 5. Follow the why-chain

1. **Why choose the negative sector?** There the existing physical signs satisfy `N=−K`, so the type-symmetric scalar is zero while the pointer scalar is nonzero. Outside it the two scalars agree on the stated support. This is a mathematical relation on one carrier, not a decision about feeling.
2. **Why does the report need a selection bound?** H is a physical parity report. Misreporting it mixes the two sectors and can shrink the gap; a strong witness alone need not compensate for an uncharacterized selector.
3. **Why does H not itself answer the quality question?** Its gates compute a record relation, not the semantic fact that a subject feels neutral, positive or negative. Calling H or M “experience” without an independently supported bridge would put the desired conclusion into the premise.
4. **Why can a witness be useful?** Direct first-person evidence and carefully aligned reports may bear on a candidate. The bounds show exactly which claims about error, population and selection would allow this particular comparison; they do not manufacture reference experiences, independent trials or subject ownership. Unreported or inaccessible private subjects are not ruled out by one reporter.
5. **Why these bridges and incidence weights?** Both scalars are functions of an existing finite echo, while the proposed subject and clock-sampling weights remain conditional. Their consistency does not derive the carrier, physical–experiential identity, actual incidence or the selection of one law from a self-sufficient zero. A deeper account must explain which distinctions are intrinsic, how subjects and measures arise together, and why the constitution is actual without invoking an outside temporal cause. The current boundary is not proof of ultimate brute bedrock.

## Continuation: joint quality and ownership

The [next pass](ZERO_ECHO_JOINT_QUALITY_AND_OWNERSHIP_REPORTS.md) puts both witnesses on the same selected reporter-runs, allows correlated errors, and derives a conditional positive joint-truth bound and a finite calibration budget. Synthetic reports do not validate experiential or identity reference labels.

## 6. Next work

- Seek an independently warranted target for the neutral/nonneutral distinction, including the possibility that neither scalar captures the subject's quality; specify its timing, access, reporter correspondence and selection controls.
- Connect this quality comparison with the prior persistence/ownership witness and actual incidence rule, rather than assuming one reporter exhausts all subjects or equating the observed sample fraction with a subject census.
- Transport preparation, sector sensor, witness and all confidence-relevant conditioning between explicit clock descriptions; derive or physically constrain their coupling and resources.

## Reproduce

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_echo_quality_bridge_discrimination_test -v
```

The tests check the actual modeled report sector, exact alternative tables, selection bound, an overlap counterexample, synthetic data and six-way confidence bookkeeping. They do not validate subjective reports, source-state transfer, physical locality, full historical-source survival or foundational necessity.
