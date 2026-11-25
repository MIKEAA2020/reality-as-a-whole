# PSR-5 R3.a Phenomenal-Interface Adjudication v1
## Independent determination of the submitted phenomenal-interface stage

**Candidate:** \(F_{\rm PSR\text{-}5}\)  
**Frozen packet SHA-256:** `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**Controlling R2 adjudication:** `Point-Sphere_PSR-5_R2_Presentation_Truth_and_Error_Adjudication_v1.md`  
**R2 SHA-256:** `fc67203e788c1fcbbc2c48b9b4cf13f5528bcc805606a3efae2c6126268ae3ea`  
**Submitted R3.a audit:** `uploads/Point-Sphere_PSR-5_R3a_Phenomenal_Interface_Audit_v1.md`  
**R3.a audit SHA-256:** `eb068c9f3e960ba9929d3a1ed0e71cc4bc8862bad0668497034ff5a26f8340ae`  
**Scope:** R3.a only. R3.b and R3.c are not executed here.

---

## 0. Authorization and actual controls

R2 passed in the PSR-5 docket, so R3.a is authorized. The submitted audit is source-statically valid:

\[
\mathsf{Authorized}(F_{\rm PSR\text{-}5},R3.a)
\land
\mathsf{AuditSourceStaticValid}.
\tag{R3a-Authorization-and-Static-Pass}
\]

Both positive and negative controls are actual quotient-native finite loci, not a contrast between an actual case and a merely coded nonactual case:

\[
\mathsf{ActualLocus}
\left(
\iota_{[S_\Sigma],[a]_{S_\Sigma}}
\right)
\land
\mathsf{ActualLocus}
\left(
\iota_{[S_\Sigma],[d]_{S_\Sigma}}
\right).
\tag{Actual-Positive-and-Negative-Controls}
\]

---

## 1. Positive phenomenal-interface control

At \(a\), the two pain-quality phenomenal roles have bidirectional coaccess, strict precedence, distinct typed event inputs, and an output to the hosted action role. Therefore:

\[
\mathsf{IntegratedRec}(S_\Sigma,a,\mathsf{pain})
\land
\mathsf{PhenStruct}([S_\Sigma],[a]_{S_\Sigma},\mathsf{pain}).
\tag{Positive-Structural-Control}
\]

The positive case also has the separate actual experiential token and realization relation:

\[
\mathsf{ActualExperience}(\xi_a)
\land
\mathsf{Qualia}(\xi_a,\mathsf{pain})
\land
\mathsf{ExpRealizes}
\left(
\xi_a,
\iota_{[S_\Sigma],[a]_{S_\Sigma}},
\mathsf{pain}
\right).
\tag{Positive-Experience-Control}
\]

Hence the full frozen conjunction is met:

\[
\mathsf{Phenomenal}_{\rm PSR}
\left(
\iota_{[S_\Sigma],[a]_{S_\Sigma}},
\mathsf{pain}
\right).
\tag{Positive-Phenomenal-Result}
\]

---

## 2. Actual negative control

At the actual locus \([d]\), the two pain-quality \(Ph\)-roles have no coaccess edges. The structural integrated condition fails. In addition, no actual experience token realizes pain at that locus:

\[
\neg\mathsf{IntegratedRec}(S_\Sigma,d,\mathsf{pain})
\land
\neg\exists\xi\,[
\mathsf{ActualExperience}(\xi)
\land
\mathsf{ExpRealizes}
\left(
\xi,
\iota_{[S_\Sigma],[d]_{S_\Sigma}},
\mathsf{pain}
\right)
].
\tag{Negative-Double-Control}
\]

Thus the negative phenomenal result follows under the frozen definition:

\[
\neg\mathsf{Phenomenal}_{\rm PSR}
\left(
\iota_{[S_\Sigma],[d]_{S_\Sigma}},
\mathsf{pain}
\right).
\tag{Negative-Phenomenal-Result}
\]

---

## 3. R3.a result and boundary

The contrast is not produced by a \(Ph\)-role name, a quality label, or nonactuality alone. It uses both an actual structural integration control and a distinct actual experiential bearer/realization relation. Therefore:

\[
\boxed{
R3.a(F_{\rm PSR\text{-}5})
=
\mathsf{Pass}_{\rm restricted\ formal}.
}
\tag{R3a-Pass}
\]

The pass is strictly interface-bounded. \(\mathsf{ActualExperience}\), \(\mathsf{Qualia}\), and \(\mathsf{ExpRealizes}\) remain primitive declared residuals; R3.a neither derives them from structure nor confirms consciousness:

\[
\mathsf{R3.aPass}
\not\Rightarrow
\mathsf{DerivedFromStructure}(\mathsf{ExpRealizes}),
\qquad
\mathsf{R3.aPass}
\not\Rightarrow
\mathsf{Confirmed}(\mathsf{GenuinePhenomenality}),
\qquad
\mathsf{R3.aPass}
\not\Rightarrow
\mathsf{NoSelectorResidue}.
\tag{R3a-Limits}
\]

R3.b is now the only next authorized operation. It is not executed here:

\[
\mathsf{Authorized}(F_{\rm PSR\text{-}5},R3.b)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.b)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.c).
\tag{R3b-Authorized-Not-Executed}
\]
