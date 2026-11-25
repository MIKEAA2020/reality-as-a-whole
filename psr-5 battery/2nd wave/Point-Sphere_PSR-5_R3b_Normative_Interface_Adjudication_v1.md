# PSR-5 R3.b Normative-Interface Adjudication v1
## Independent determination of the submitted host-indexed normative stage

**Candidate:** \(F_{\rm PSR\text{-}5}\)  
**Frozen packet SHA-256:** `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**Controlling R3.a adjudication:** `Point-Sphere_PSR-5_R3a_Phenomenal_Interface_Adjudication_v1.md`  
**R3.a SHA-256:** `59dd14f137f87cbeb93c987625b6655521060713d8742179bbf48aab4c821666`  
**Submitted R3.b audit:** `uploads/Point-Sphere_PSR-5_R3b_Normative_Interface_Audit_v1.md`  
**R3.b audit SHA-256:** `e527ab573415dd97d8e33ed7a176bb2710d3d3104338ead810f815723856bd46`  
**Scope:** R3.b only. R3.c is not executed here.

---

## 0. Authorization and host-scoped action domain

R3.a passed in the PSR-5 docket, so R3.b is authorized. The submitted audit is source-statically valid:

\[
\mathsf{Authorized}(F_{\rm PSR\text{-}5},R3.b)
\land
\mathsf{AuditSourceStaticValid}.
\tag{R3b-Authorization-and-Static-Pass}
\]

The action comparison is not global across arbitrary loci. At the actual \([a]\)-orbit, the frozen host relation gives:

\[
\mathsf{ActionsAt}([S_\Sigma],[a]_{S_\Sigma})
=
\{n,b,g\}.
\tag{Host-Scoped-Actions}
\]

Their successors are \(T_{\rm neutral}\), \(T_{\rm bad}\), and \(T_{\rm good}\), respectively, and all three are finite structural candidates. Hence the named actions are feasible.

---

## 1. Veto control

\(T_{\rm bad}\) contains both a prohibited instrumentalization value and a \((\mathsf{pain},3)\) phenomenal value. It therefore fails the veto condition and cannot be choice-eligible, lexicographically selected, or owed at \([a]\):

\[
\neg\mathsf{VetoClear}_{\rm PSR}(T_{\rm bad})
\land
\neg\mathsf{ChoiceEligible}_{\rm PSR}([S_\Sigma],b)
\land
\neg\mathsf{LexMax}_{\rm PSR}([S_\Sigma],[a]_{S_\Sigma},b)
\land
\neg\mathsf{Ought}_{\rm PSR}
\left(
\iota_{[S_\Sigma],[a]_{S_\Sigma}},
 a_{[S_\Sigma],b}
\right).
\tag{Bad-Action-Control}
\]

---

## 2. Matching, value, and lexicographic control

The good successor's presentation content is the frozen \(o_{\rm good}\), whose declared pattern is the good successor's host-local pattern. It follows that:

\[
\mathsf{SuccMatches}(T_{\rm good},Pr)
\land
\mathsf{VetoClear}_{\rm PSR}(T_{\rm good}).
\tag{Good-Content-and-Veto-Control}
\]

The finite value calculation is:

\[
\begin{aligned}
\mathsf{Val}_{\rm PSR}(T_{\rm neutral})&=\langle0,0,0\rangle,\\
\mathsf{Val}_{\rm PSR}(T_{\rm bad})&=\langle0,0,0\rangle,\\
\mathsf{Val}_{\rm PSR}(T_{\rm good})&=\langle1,1,1\rangle.
\end{aligned}
\tag{Finite-Value-Calculation}
\]

Among choice-eligible actions at \([a]\), \(n\) has the neutral successor and \(g\) the good successor; \(b\) is vetoed. Therefore \(g\) is the unique lexicographic maximum and, at the actual host locus, is selected by the frozen \(\mathsf{Ought}\) rule:

\[
\mathsf{LexMax}_{\rm PSR}([S_\Sigma],[a]_{S_\Sigma},g)
\land
\mathsf{Ought}_{\rm PSR}
\left(
\iota_{[S_\Sigma],[a]_{S_\Sigma}},
 a_{[S_\Sigma],g}
\right).
\tag{Good-Action-Control}
\]

---

## 3. R3.b result and final-stage boundary

The good/bad controls satisfy the declared finite, host-indexed normative operation:

\[
\boxed{
R3.b(F_{\rm PSR\text{-}5})
=
\mathsf{Pass}_{\rm restricted\ formal}.
}
\tag{R3b-Pass}
\]

This is not a result for objective normativity, nonbrute value, a public bridge, or selector discharge:

\[
\mathsf{R3.bPass}
\not\Rightarrow
\mathsf{ObjectiveNormativity},
\qquad
\mathsf{R3.bPass}
\not\Rightarrow
\mathsf{PublicBridgePass},
\qquad
\mathsf{R3.bPass}
\not\Rightarrow
\mathsf{NoSelectorResidue}.
\tag{R3b-Limits}
\]

R3.c is now the sole remaining authorized frozen stage. It is not executed here:

\[
\mathsf{Authorized}(F_{\rm PSR\text{-}5},R3.c)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.c).
\tag{R3c-Authorized-Not-Executed}
\]
