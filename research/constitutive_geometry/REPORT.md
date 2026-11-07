# Step 43 — An explicit candidate geometry for physical–phenomenal constitution

## Direct answer

**An explicit partial candidate can be constructed. A justified complete physical–phenomenal constitution has not been constructed.**

This step supplies physical response probabilities, a derived distinguishability metric, coordinate transformations, channel transformations, and an independently falsifiable proposed relation to phenomenal similarity. It also implements the physical measurement protocol through the existing workspace and checks source/monitor and report/access dissociations.

The missing identification is not concealed: statistical distinguishability is not already experience, and an access mechanism is not already a subject-selection law. The candidate is local, calibration-dependent, and restricted to an independently anchored episode domain. It does not discover qualitative occurrence, an absolute quality map, subject boundaries, or ultimate actuality.

This develops the earlier [contrast-covariance proposal](../contrast_covariance/REPORT.md) using differential geometry and exact channel results, rather than merely renaming it. The mathematical ingredients are standard information geometry and probability theory, not new consciousness laws.

**33 tests pass.** The full runner now passes **1,149 tests across 43 folders**. These check the specified constructions, not the truth of the constitutive hypothesis.

## 1. What the SR analogy does and does not license

The productive lesson from special relativity is that a relation can be constitutive rather than an added force. But its geometry, physical interpretation, and measurement operations all matter.

A chart change is not a new object or a new observer token. Similarly, a change of coordinates on one neural/physical state cannot manufacture a subject. A lossy recording channel is not a coordinate change. Nor does a physical intervention merely redescribe the same occurrence.

The present metric is a statistical state-space metric, **not a Lorentzian spacetime metric**. Its transformations are not Lorentz boosts. Nothing here identifies a subject with a frame or an experience with a spacetime foliation. Any relativistic implementation must additionally respect its actual spacetime localization and physical clocks; this finite construction does not supply a relativistic field theory.

## 2. The underlying physical specification

Let P denote an actual process with state, dynamics, causal connections, and physically permitted interventions. Fix a domain W of content-related processes by independently identifying a candidate access mechanism. This is a restricted modeling choice, not a discovered universal subject selector.

Let theta parameterize a smooth family of physical states or response propensities. Fix a measurement protocol A, including its reset procedure, timing, response channel, and intervention rules. It yields

    q_A(o | theta),

where o is the full observed response record. These probabilities come from the stipulated physical model or, in a scientific application, would have to be independently estimated and validated. They are not assigned from desired phenomenal labels.

The full physical object is P together with its declared intervention structure; a response distribution alone is not assumed constitutively complete. A passive recorder and a causally active source can have identical marginal distributions and geometry while differing physically.

The implementation starts with two independent binary proposal propensities x and y, with 0 < x,y < 1. A record (a,b) has probability

    q(a,b | x,y) = x^a (1-x)^(1-a) y^b (1-y)^(1-b).

The workspace adapter uses TWO RESET TRIALS: one visual proposal with binary value a, followed by one auditory proposal with value b. Each is passed through the existing realized workspace. The pair is an experimental record, **not a stipulated single episode or a two-content conscious field**. The source labels and parameters are properties of the toy protocol, not identified human modalities or qualities.

This explicit temporal qualification prevents the product distribution from silently solving phenomenal togetherness.

**Parameter provenance matters.** In this implementation x and y control the proposal-generating ensemble; they are not the workspace's momentary `Content` values. The computed tensor is therefore a calibration/response geometry of the specified experiment, not already an intrinsic geometry of one workspace token. To apply the bridge below to neural or phenomenal states, one must independently establish that the chosen response parameters track the relevant intrinsic state rather than merely the distribution of external inputs. The code does not establish that correspondence.

## 3. Derive the metric instead of supplying a similarity table

For a regular finite-outcome response family with fixed support, define

    g_ij(theta) = sum_o [partial_i q(o|theta) partial_j q(o|theta)] / q(o|theta).

This is the Fisher information tensor. It quantifies local distinguishability of the specified physical response distributions. It is positive semidefinite because for every tangent v,

    v^T g v = sum_o [v dot grad q(o|theta)]^2 / q(o|theta) >= 0.

It is a genuine positive-definite metric only where the parameters are locally identifiable. Singular channels produce null directions; they do not automatically erase experience.

Its connection with statistical discrimination can also be expressed by the local expansion

    KL(q_theta || q_(theta+dtheta))
        = (1/2) dtheta^T g(theta) dtheta + higher-order terms,

under the stated smoothness and support conditions. Choosing statistical distinguishability as phenomenally relevant remains an extra hypothesis; this expansion does not establish that relevance.

For the two-response product family, the independent centered scores have zero cross expectation. Therefore

    ds^2 = dx^2/[x(1-x)] + dy^2/[y(1-y)].

At x = 1/4 and y = 1/3, the exact matrix is

    g = [[16/3, 0],
         [0,    9/2]].

The metric is derived from the declared response law. The law itself is stipulated for the example, not deduced from ultimate physics or consciousness.

## 4. Explicit coordinate transformations

Let z be another invertible smooth chart on the same state family, with Jacobian J = dtheta/dz. The probability derivative obeys the chain rule, giving

    g_z = J^T g_theta J.

Thus

    dtheta^T g_theta dtheta = dz^T g_z dz.

This is the invariant line element. Coordinate covariance alone cannot establish the theory: any properly defined tensor metric has that property.

For example, set

    u = x+y,   v = x-y,
    x = (u+v)/2,   y = (u-v)/2.

At the point above,

    J = [[1/2,  1/2],
         [1/2, -1/2]],

    g_(u,v) = [[59/24, 5/24],
               [5/24, 59/24]].

The off-diagonal terms do not indicate a new physical coupling. They arise from the mixed coordinates.

A nonlinear chart makes the geometry even more explicit:

    alpha = 2 arcsin(sqrt(x)),
    beta  = 2 arcsin(sqrt(y)).

Since dx/dalpha = sqrt(x(1-x)) and similarly for y,

    ds^2 = dalpha^2 + dbeta^2.

The intrinsic geometry of this response family is a flat open square (0,pi)^2. Its geodesic distance is the Euclidean distance in these angular coordinates. For example, the distance from (1/4,1/4) to (3/4,3/4) is sqrt(2)*pi/3.

This is a calculated physical-response geometry, not a finding that human experience is a flat square.

## 5. Measurement loss is not a coordinate change

Let K(r|o) be a parameter-independent physical recording channel, with

    q_K(r|theta) = sum_o K(r|o) q(o|theta).

Its Fisher tensor obeys

    g_K <= g

in the positive-semidefinite ordering.

Proof: define the score s(o)=grad log q(o|theta). The recorded score is E[s|r]. The original score has mean zero, and

    g - g_K = E[ Cov(s | r) ],

which is positive semidefinite. Fixed support and a parameter-independent K are essential to the stated argument. If the channel itself changes with theta, its derivative contributes and the theorem cannot be applied as written.

A lossy channel may be rank-deficient; it is not an invertible chart. This directly separates degradation of evidence from physical change to a candidate episode.

## 6. Copies, monitors, and repeated trials

### A faithful copy is not a new independent sample

Append z=a to the record (a,b). The joint law is

    q(a,b,z|theta) = q(a,b|theta) indicator(z=a).

Its Fisher tensor is exactly g. A parameter-independent noisy copy also adds no information when the source record remains available. Treating the source and its faithful copy as independent observations would falsely double information about x.

This is an information-theoretic result, not proof that adding a physical copy never creates another experience. The latter needs a constitution law and token analysis.

### Reading only a noisy monitor contracts the geometry

If z is a bit-flipped copy of a with error e,

    Pr(z=1) = e + (1-2e)x.

The monitor-only tensor has entries

    g_xx = (1-2e)^2 / [Pr(z=1)(1-Pr(z=1))],
    g_xy = g_yy = 0.

At x=1/4 and e=1/4, g_xx=16/15, compared with source g_xx=16/3. At e=1/2, the monitor contains no parameter information. This says nothing by itself about whether the source's experience changes.

### Genuine repetitions scale information

For n independent repetitions, scores add with zero cross expectation, yielding g_n = n*g. Distances in that experiment scale by sqrt(n).

Therefore a naive equation between total experimental Fisher information and intrinsic phenomenal distance is not well-defined without fixing the protocol and normalization. Estimating one fixed single-trial family with more data does not change that family's g; constructing a joint n-trial experiment is a different statistical object. The distinction cannot be hidden in a free scaling factor chosen anew for every comparison.

## 7. Realized-workspace dissociations

The adapter actually routes each proposal through the existing workspace model, rather than only attaching labels to output probabilities.

| Configuration / observation | Derived response geometry | Physical conclusion |
|---|---|---|
| Ordinary action outputs | g | The protocol preserves the binary responses |
| Report disabled, action observed | g | This action evidence does not require report |
| Report disabled, report observed | zero | A failed report channel is uninformative |
| Distribution disabled, action observed | zero | The action pathway no longer receives the content |
| Distribution disabled, report observed | g | Reporting can retain the original response geometry |
| Passive monitor observed | g | A copied marginal can match active-source geometry |
| Passive monitor overridden | action law unchanged | The passive monitor is not the active source |

Direct do(workspace) interventions change memory, action, and comparison. Direct do(monitor) interventions do not change these consumers in this model. Thus active versus copied causal position is represented physically rather than inferred from matching response statistics.

This is a new application of the already stipulated workspace, not new evidence that GWT is the true phenomenal theory.

The decisive limit is constructive: **the same response geometry can occur in a passive monitor and an active workspace, and report geometry can remain intact while workspace distribution fails.** Consequently, Fisher geometry alone is not a subject or episode selector. An identity theory must include relevant actual causal realization, not just the metric.

## 8. The proposed physical–phenomenal bridge

For an independently anchored domain of experience, suppose a phenomenal contrast manifold Phi and its local similarity/discrimination tensor h are specified by an independently justified evidence procedure. Such a procedure is not presently supplied by real data in this repository. Reports are evidence channels with failure modes, not infallible definitions of experience.

Let chi map the independently identified physical state domain to that phenomenal domain. The candidate hypothesis is

    chi^* h = kappa * g_(W,A),

for one fixed positive scale kappa in the declared domain and fixed physically specified protocol A.

This is a **local relational constitution hypothesis**: the candidate process's response geometry constitutes the relational form of the anchored experience. There is no extra brain-to-experience force in this proposal.

For the example, the hypothesis predicts a flat two-dimensional phenomenal contrast geometry, with angular rather than linear dependence on x and y. It predicts particular distance ratios once the calibration, state mapping, and fixed scale are declared. Nonzero intrinsic curvature, incompatible ratios, or different transport of anchored contrasts would reject this restricted hypothesis, if those target facts were independently warranted in the domain.

The chi and h must not be defined after the fact to make the equality true. They need independent constraints, and a fixed kappa cannot be replaced by an arbitrary position-dependent factor whenever predictions fail. Coordinate changes on the same physical state must be transported through chi without creating new experiences.

This equation is a substantive conjecture, not a theorem of Fisher geometry. Other metrics also transform covariantly. No uniqueness argument supplied here makes this metric the only possible phenomenal one.

## 9. What has and has not been constructed

### Constructed

- a physical response family with explicit probabilities and derivatives;
- its derived metric and nonlinear flat coordinates;
- invariant line elements under physical-state reparameterization;
- physically distinct recording-channel transformations and a contraction proof;
- exact copy-versus-independent-repeat distinctions;
- a realized workspace measurement protocol and causal dissociations;
- a restricted phenomenal-geometry hypothesis with separating conditions.

### Not constructed or established

- an independently justified phenomenal tensor from actual subjects;
- a constitutive explanation of why the process is experiential at all;
- an absolute quality identity, rather than relational geometry up to symmetry and calibration;
- the law Gamma selecting episode incidence, temporal extent, or subjects;
- an intrinsic canonical measurement protocol independent of arbitrary experimental choices;
- a universal scale or timescale of phenomenal distance;
- a neural implementation, complete quantum or relativistic extension, or ultimate self-explanation.

The metric retains reflection symmetries such as x -> 1-x. Geometry alone does not identify which absolute quality is present. Independent anchors and a substantive identity argument are still needed, as shown by the earlier relabeling audit.

The two-reset-trial adapter deliberately does not claim that the pair of trials is one subject or one episode. A candidate physical access window could be proposed separately, but declaring it an episode would add the missing composition hypothesis, not derive it. No arbitrary Gamma is inserted here to make the package look complete.

## 10. Verification

`model.py` computes normalized response families, exact rational Fisher matrices, coordinate pullbacks, channel pushforwards, and independent repetitions. Only angular/geodesic evaluations use floating point; their formulas are derived analytically above. Singular boundary points are explicitly excluded from the regular two-parameter domain.

`workspace_adapter.py` reuses the existing workspace implementation with explicit reset-trial semantics. `test_model.py` has 33 checks, including the exact matrices, contraction examples, duplicate and repeat behavior, chart invariance, source/monitor interventions, and report/distribution dissociations. General mathematical statements rest on the derivations, not on finite test coverage.

The diagnostic JSON records exact witnesses. No synthetic state is assigned a consciousness label. These tests add mathematical/software checks, not empirical confirmation of chi or Gamma.

## Verdict

**Yes, the analogy can be developed into explicit candidate mathematics with physical measurement conditions and transformations. No, this construction is not yet an SR-level explanation of experience.**

The most useful result is both positive and restrictive: a calculable local physical–phenomenal geometry conjecture is now available, but matching geometry cannot by itself distinguish an active process from a passive copy, identify absolute qualities, or select subjects. The missing constitutive identification is sharply exposed rather than supplied by nomenclature.

## Protocol-independence constraint on the next theory

[The complete-constitution programme](../../CONSTITUTION_RESEARCH_PROGRAMME.md) derives a stronger channel witness: a known bit-flip channel on the first response remains parameter-identifying but changes g from diag(16/3,9/2) to diag(16/15,9/2). The distortion is not a scalar and cannot be removed by a global unit change. Thus informational completeness alone does not select an intrinsic Fisher metric. This rules out a protocol-independent extension requiring one fixed physical–phenomenal map to match every such measurement metric; it does not refute the declared fixed-protocol conjecture. The additional exact check brings this suite to 33 tests and the full runner to 1,149 tests across 43 folders.
