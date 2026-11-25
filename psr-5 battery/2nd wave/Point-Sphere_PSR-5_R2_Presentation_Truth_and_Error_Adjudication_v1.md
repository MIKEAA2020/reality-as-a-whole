# PSR-5 R2 Presentation, Truth, and Error Adjudication v1
## Independent determination of the submitted third battery stage

**Candidate:** \(F_{\rm PSR\text{-}5}\)  
**Frozen packet SHA-256:** `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**Controlling R1 adjudication:** `Point-Sphere_PSR-5_R1_Instantiation_and_Isomorphism_Adjudication_v1.md`  
**R1 SHA-256:** `e4f5e35e90ec6f8db7d68f81c269672eae3745283915d0ee6cb1e6d76a2c6462`  
**Submitted R2 audit:** `uploads/Point-Sphere_PSR-5_R2_Presentation_Truth_and_Error_Audit_v1.md`  
**R2 audit SHA-256:** `98b5d0a0e86c1ea22052de69f7fd1c89eb4653801574d2f776902360965d0056`  
**Scope:** R2 only. R3.a, R3.b, and R3.c are not executed here.

---

## 0. Authorization and actual-locus control

R1 passed in the PSR-5 docket, so R2 is authorized. The submitted audit is source-statically valid:

\[
\mathsf{Authorized}(F_{\rm PSR\text{-}5},R2)
\land
\mathsf{AuditSourceStaticValid}.
\tag{R2-Authorization-and-Static-Pass}
\]

The test concerns the quotient-native orbit individual, not a raw role label. Its bearing condition follows from the actual class and the finite \(Ag\)-orbit:

\[
\mathsf{ActualLocus}
\left(
\iota_{[S_\Sigma],[a]_{S_\Sigma}}
\right).
\tag{Actual-Locus-Pass}
\]

---

## 1. Frozen presentation and match controls

The presentation roles have the declared contents at the same actual orbit locus:

\[
\begin{aligned}
\mathsf{Presents}_{\rm PSR}
\left(p_{[S_\Sigma],p_t},\iota_{[S_\Sigma],[a]_{S_\Sigma}},o_{\rm true}\right)
&\land
\mathsf{Content}(p_{[S_\Sigma],p_t},o_{\rm true}),\\
\mathsf{Presents}_{\rm PSR}
\left(p_{[S_\Sigma],p_e},\iota_{[S_\Sigma],[a]_{S_\Sigma}},o_{\rm false}\right)
&\land
\mathsf{Content}(p_{[S_\Sigma],p_e},o_{\rm false}).
\end{aligned}
\tag{Presentation-Content-Controls}
\]

The true content pattern is exactly the locus pattern:

\[
\mathsf{Pat}(o_{\rm true})
=
\mathsf{LocalPattern}(S_\Sigma,[a]_{S_\Sigma}).
\tag{True-Pattern-Identity}
\]

The false pattern deletes both \(\mathsf{coaccess}\) triples. Since relation-type incidence is preserved by \(\cong_{\rm str}\), a structure with two such triples cannot be isomorphic to one with none:

\[
\mathsf{Pat}(o_{\rm false})
\not\cong_{\rm str}
\mathsf{LocalPattern}(S_\Sigma,[a]_{S_\Sigma}).
\tag{False-Pattern-Nonisomorphism}
\]

---

## 2. Correct/error result

The actual locus, true presentation, and pattern identity yield a correct presentation:

\[
\mathsf{Correct}_{\rm PSR}
\left(p_{[S_\Sigma],p_t},o_{\rm true}\right).
\tag{Correct-Pass}
\]

The false presentation retains actual tokenhood and declared content but lacks a matching pattern. The frozen error definition therefore yields:

\[
\neg\mathsf{Correct}_{\rm PSR}
\left(p_{[S_\Sigma],p_e},o_{\rm false}\right)
\land
\mathsf{Error}_{\rm PSR}
\left(p_{[S_\Sigma],p_e},o_{\rm false}\right).
\tag{Error-Pass}
\]

Thus R2 establishes the required non-entailment within the fixed interface:

\[
\mathsf{ActualLocus}
\land
\mathsf{Presents}_{\rm PSR}
\land
\mathsf{Content}
\not\Rightarrow
\mathsf{Correct}_{\rm PSR}.
\tag{No-Tokenhood-Fit}
\]

The result is invariant under isomorphic carrier-renaming through the frozen orbit and local-pattern transport clauses.

---

## 3. R2 result and next boundary

\[
\boxed{
R2(F_{\rm PSR\text{-}5})
=
\mathsf{Pass}_{\rm restricted\ formal}.
}
\tag{R2-Pass}
\]

This pass validates the named finite presentation/matching interface only:

\[
\mathsf{R2Pass}
\not\Rightarrow
\mathsf{GeneralSemanticRealism},
\qquad
\mathsf{R2Pass}
\not\Rightarrow
\mathsf{NonBrute}(\mathsf{Instantiates}),
\qquad
\mathsf{R2Pass}
\not\Rightarrow
\mathsf{PublicBridgePass}.
\tag{R2-Limits}
\]

R3.a is now the sole next authorized stage. It is not executed here:

\[
\mathsf{Authorized}(F_{\rm PSR\text{-}5},R3.a)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.a).
\tag{R3a-Authorized-Not-Executed}
\]

\[
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.b)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.c).
\tag{No-Later-Execution}
\]
