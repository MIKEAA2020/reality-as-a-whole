# PSR-5 R1 Instantiation and Isomorphism Adjudication v1
## Independent determination of the submitted second battery stage

**Candidate:** \(F_{\rm PSR\text{-}5}\)  
**Frozen packet SHA-256:** `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**Controlling R0 adjudication:** `Point-Sphere_PSR-5_R0_Global_Model_and_Locality_Adjudication_v1.md`  
**R0 SHA-256:** `5528f8b6a924573f1411cc241d3a78bbb6010f239c7e567e9fb624331c80e36c`  
**Submitted R1 audit:** `uploads/Point-Sphere_PSR-5_R1_Instantiation_and_Isomorphism_Audit_v1.md`  
**R1 audit SHA-256:** `99a107d38befa9d971a84fa89298446371ba9ac9be4f36bc4e546893f13562d1`  
**Scope:** R1 only. R2, R3.a, R3.b, and R3.c are not executed here.

---

## 0. Authorization and source controls

R0 passed in the separate PSR-5 docket, so R1 is authorized. The submitted audit is UTF-8 and passes display-pair and TeX-grouping checks:

\[
\mathsf{Authorized}(F_{\rm PSR\text{-}5},R1)
\land
\mathsf{AuditSourceStaticValid}.
\tag{R1-Authorization-and-Static-Pass}
\]

---

## 1. Class-native instantiation controls

The primitive extension is exact and applies to isomorphism classes:

\[
\mathsf{Instantiates}^{\mathfrak M}
=
\{[S_\Sigma],[S_\Phi]\},
\qquad
\mathsf{ActualStruct}([S])
\iff
\mathsf{Instantiates}([S]).
\tag{Actuality-Extension}
\]

The four frozen controls consequently yield:

\[
\begin{array}{c|c|c}
\textbf{control class} & \textbf{candidate status} & \textbf{actual status}\\
\hline
[S_\Sigma] & \mathsf{StructCand}_{\rm raw}(S_\Sigma) & \mathsf{ActualStruct}\\
[S_\Phi] & \mathsf{StructCand}_{\rm raw}(S_\Phi) & \mathsf{ActualStruct}\\
[S_{\rm with}] & \mathsf{StructCand}_{\rm raw}(S_{\rm with}) & \neg\mathsf{ActualStruct}\\
[S_{\rm noncand}] & \neg\mathsf{StructCand}_{\rm raw}(S_{\rm noncand}) & \neg\mathsf{ActualStruct}
\end{array}
\tag{R1-Control-Table}
\]

These statuses follow only from the declared raw grammar and class-level instantiation extension. They do not follow from macro spelling, code length, structural elegance, observation, a local pattern, or physical-target behavior.

---

## 2. Nonvacuous isomorphism control

The alias branch supplies a concrete carrier-renaming test. Since

\[
\mathsf N(0)=100,
\tag{N-Zero}
\]

the accepted alias code

\[
1110\,\mathsf N(0)\mathsf N(0)
=
1110100100
\tag{Sigma-Alias-Code}
\]

denotes the zeroth carrier permutation of \(S_\Sigma\). It is a decoded structure isomorphic to \(S_\Sigma\), hence lies in the same quotient class:

\[
[\pi_0(S_\Sigma)]
=
[S_\Sigma].
\tag{Sigma-Alias-Class}
\]

Likewise, every valid alias of any macro structure is a carrier-renaming that preserves each declared field. Thus for every \(h:S\cong_{\rm str}T\):

\[
S\cong_{\rm str}T
\Longrightarrow
[S]=[T]
\Longrightarrow
\left(
\mathsf{ActualStruct}([S])
\leftrightarrow
\mathsf{ActualStruct}([T])
\right).
\tag{Actuality-Invariance}
\]

This establishes R1's class-native invariance requirement without treating a raw label or alias code as an actuality selector.

---

## 3. R1 result and next boundary

The exact instantiation extension is transparent over the frozen controls and invariant under the nonvacuous alias representation test:

\[
\boxed{
R1(F_{\rm PSR\text{-}5})
=
\mathsf{Pass}_{\rm restricted\ formal}.
}
\tag{R1-Pass}
\]

This pass validates only transparency and quotient invariance of a stipulated extension:

\[
\mathsf{R1Pass}
\not\Rightarrow
\mathsf{NonBrute}(\mathsf{Instantiates}),
\qquad
\mathsf{R1Pass}
\not\Rightarrow
\mathsf{NoSelectorResidue}.
\tag{R1-Limits}
\]

R2 is now the only next authorized operation, and no later test is executed:

\[
\mathsf{Authorized}(F_{\rm PSR\text{-}5},R2)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R2).
\tag{R2-Authorized-Not-Executed}
\]

\[
\bigwedge_{b\in\{R3.a,R3.b,R3.c\}}
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},b).
\tag{No-Later-Execution}
\]
