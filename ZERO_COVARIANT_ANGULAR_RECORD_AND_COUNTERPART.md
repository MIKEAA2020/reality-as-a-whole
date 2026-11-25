# Lorentz transport of the coherent angular record

## Why this matters

The [coherent angular quantum echo](ZERO_COHERENT_ANGULAR_SPHERE_ECHO_CONSTRUCTION.md) adds a physical-model record of the scalar cosine `u`. The earlier [celestial structure](ZERO_POINT_CELESTIAL_RELATIONAL_STRUCTURE.md) explains that its uniform direction measure and antipodes are defined relative to a chosen observer. This continuation puts the two into one explicit interface: it transports the distribution, record thresholds and mathematical counterpart between observers, and checks the new bins on the **actual coherent echo vectors**.

A passive coordinate change of a fixed physical observer is not the same thing as asking the same angle question with a different physical observer. We must distinguish them to avoid calling a frame-dependent threshold or symmetry an observer-independent law. The tests in [zero_angular_covariant_access_test.py](verification/zero_angular_covariant_access_test.py) are exact rational calculations plus the original quantum vectors. No detector, localized transmission or actual subject access is thereby constructed.

## 1. The same physical record in different coordinates

Assume an oriented Lorentzian vector space with signature `(+---)`, a future unit timelike observer T, a unit spacelike axis M orthogonal to T, and a future null ray K. Its relative angle cosine is

```text
u = −(K·M)/(K·T).
```

If the coordinates of **all three** vectors are transformed by the same Lorentz transformation, their inner products and u are unchanged. Thus the old record effects `b=sign(u)` and `z=sign(u+1/2)`, as well as functions `g(u)`, have the same value: these are the same physical questions in new coordinates. This is a standard covariant relational construction and does not require a preferred fundamental foliation. The code checks several boosts, axes, signs and rays against direct Minkowski products.

These expressions only assign mathematical observables relative to the assumed T, M and K. They do not show that any confined system physically obtains a record of T, M or K, or that an actual apparatus transforms according to this idealized rule.

## 2. A different physical observer asks different questions

Now choose another unit observer, boosted along the original axis with speed β, with its corresponding unit axis aligned to the boost. For the same null ray, its measured cosine is

```text
v = fβ(u) = (u−β)/(1−βu),        u = (v+β)/(1+βv),     |β|<1.
```

If the original ensemble has `du/2`, the pushforward on the new coordinate is

```text
ρβ(v) dv = (1−β²) / [2(1+βv)²] dv.
```

The original `b` threshold is now at `v=−β`, and the old `z` threshold is at `v=fβ(−1/2)`. If instead the second observer defines its **own** analogous thresholds `b'=sign(v)` and `z'=sign(v+1/2)`, they represent different physical questions on the same rays and need not reproduce the old `(1/2,1/4,1/4)` distribution.

For a concrete exact example `β=1/2`, the new thresholds correspond to `u=1/2` and `u=0`. The three probabilities become

```text
(b',z')=(+,+)    1/4
(b',z')=(−,+)    1/4
(b',z')=(−,−)    1/2.
```

The code computes these intervals and independently evaluates the new projectors on the coherent angular-register weights in three original source histories and both pointer signs, with N=8. Since the new thresholds align with bin boundaries in that case, this is exact at that refinement. Choosing a different observer does not by itself apply a physical transformation to the quantum system, make a new observation, or imply the observer's local access to the register.

## 3. Transporting a sign-reversing counterpart

The original illustrative counterpart `u→−u` preserves `du/2` and exchanges the two old hemispheres. Conjugating this same map by the change of observer gives

```text
Cβ(v) = fβ(−fβ⁻¹(v))
      = −[(1+β²)v+2β]/[1+β²+2βv],
|Cβ'(v)| = (1−β²)²/[1+β²+2βv]².
```

It is an involution, and the measure transforms as

```text
ρβ(Cβ(v)) |Cβ'(v)| = ρβ(v).
```

The transported original sign is `sign(fβ⁻¹(v))`; it reverses under Cβ. The new observer's independently defined `sign(v)` does not generally do so. Conversely, the **new** antipode `v→−v` reverses `sign(v)` but generally does not preserve the pushed-forward density. The sign-reversing integral is still zero when one consistently transports *both* the original sign and its measure; replacing just one by a fresh-frame expression invalidates that argument. The test checks these identities at exact rational points and gives explicit counterexamples to the naive substitution.

This `u→−u` is a mathematical angular sign example, not the actual M-pointer flip of the quantum quality operator, nor a newly established pairing of actual experiential incidences. The original signed-quality pairing depended on a separate sign variable and its invariant distribution. Demonstrating an observer-covariant physical operation and an invariant **actual incidence** measure remains necessary before drawing a conclusion about lived valence.

The echo's different negative-band reflection `h(u)=−1−u` also transports as `fβ∘h∘fβ⁻¹`. Its finite-bin symmetry remains an involution after conjugation; the test transports every midpoint for N=4, 8, 16. A naive reflection in v is generally a different operation. The real quantum swap additionally acts on the original Q, pointer and R degrees of freedom; angular coordinate conjugation alone is not a realization of those gates in spacetime.

## 4. What this contributes and what it requires

Together with the [point–sphere to cone construction](ZERO_POINT_SPHERE_TO_LORENTZ_CONE.md), this gives a consistent dictionary from the common scalar angular quantum register to relational null-direction questions in an assumed local cone: fixed observables are covariant, while actual changes of observer alter thresholds and densities in calculable ways. The matching is conditional; the quantum register is not yet identified with a physical null field, and the cone is not derived from the zero whole. There is no demonstrated dynamics connecting multiple cones, localized access relation, event geometry, foliation-free clock coupling, empirical gravitational law, or incidence/quality law.

The next constructive challenge is to make a single **physical** bearer of the clock, direction, pointer and experience interface, derive its accessible projectors and invariant incidence from the underlying constitution, and test full quantum and actual-bearer controls. That is distinct from treating a coordinate expression as an apparatus. These explicit inputs remain obligations against the no-unexplained-residue aim, not endorsed brute stopping points.

```sh
OPENBLAS_NUM_THREADS=1 PYTHONPATH=.arena/python-deps:. python -m unittest \
 verification.zero_angular_covariant_access_test -v
```
