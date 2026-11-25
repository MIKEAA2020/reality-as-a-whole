# PSR-5 R0 Global-Model and Finite-Locality Adjudication v1
## Independent determination of the submitted first battery stage

**Candidate:** \(F_{\rm PSR\text{-}5}\)  
**Frozen packet:** `uploads/Plural_Structural_Realism_Entry_Packet_v5.md`  
**Packet SHA-256:** `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**Submitted R0 audit:** `uploads/Point-Sphere_PSR-5_R0_Global_Model_and_Locality_Audit_v1.md`  
**Audit SHA-256:** `ac0bead7fee5f90ee0913af253b0e5effe43330af28af342a1cf894249e461da`  
**Scope:** R0 only. R1, R2, R3.a, R3.b, and R3.c are not executed here.

---

## 0. Source and authorization controls

PSR-5 had restricted-formal battery admission before this stage, while PSR-4 remains separately closed. The submitted R0 audit is UTF-8 and passes display-pair and TeX-grouping validation:

\[
\mathsf{Authorized}(F_{\rm PSR\text{-}5},R0)
\land
\mathsf{AuditSourceStaticValid}.
\tag{R0-Authorization-and-Static-Pass}
\]

No result from the PSR-4 docket is imported into this fresh candidate:

\[
\mathsf{Closed}_{\rm PSR4\text{-}R0}
\not\Rightarrow
\mathsf{R0Fail}(F_{\rm PSR\text{-}5}).
\tag{Docket-Separation}
\]

---

## 1. Typed global-model check

The candidate separates all bit strings from records before taking the structural quotient:

\[
\mathbf C
=
\mathsf{AcceptedCodeStrings}
\sqcup
\mathsf{RejectedStrings},
\qquad
\mathcal S_{\rm raw}
=
\mathsf{Decode}(\mathsf{AcceptedCodeStrings}),
\qquad
\overline{\mathcal S}
=
\mathcal S_{\rm raw}/\cong_{\rm str}.
\tag{Typed-Global-Carrier}
\]

Thus rejected strings are not treated as raw records and are not inputs to the isomorphism quotient. The finite macro table together with the alias and trivial branches determines a total decode map on the stated accepted language:

\[
\mathsf{Decode}_{\rm PSR\text{-}5}
:\mathsf{AcceptedCodeStrings}
\longrightarrow
\mathcal S_{\rm raw}.
\tag{Total-Decode}
\]

The trivial sequence \(G_n\) supplies an infinite family of fully defined finite records, while every alias has a finite carrier-renaming of a fixed macro record. Therefore the declared global regime is explicit-infinite without the PSR-4 generic-content or value-key gaps:

\[
\boxed{
\mathsf{Defined}
\left(
\mathsf{Decode},
\mathcal S_{\rm raw},
\overline{\mathcal S},
\mathfrak M_{\rm PSR}
\right)
\land
\mathsf{ExplicitInfinite}(\mathfrak M_{\rm PSR}).
}
\tag{Global-Model-Pass}
\]

---

## 2. Actual extensions, finite slice, and closure

The primitive actual structure and experience extensions are exact, quotient-native extensions. They witness actual plurality but remain residual declarations:

\[
\mathsf{Instantiates}^{\mathfrak M}
=
\{[S_\Sigma],[S_\Phi]\},
\qquad
[S_\Sigma]\neq[S_\Phi].
\tag{Actual-Plurality}
\]

\[
\mathsf{DeclaredResidual}
\left(
\mathsf{Instantiates},
\mathsf{ActualExperience},
\mathsf{Qualia},
\mathsf{ExpRealizes}
\right)
\not\Rightarrow
\mathsf{NoSelectorResidue}.
\tag{No-Residual-Credit}
\]

At \(N_\star=3\), every complete code is a macro fixture: the generic alias and trivial forms require a four-bit branch prefix followed by at least one nonempty natural code. The named successor closure is already macro-coded, and the content closure now includes the good successor content:

\[
\mathbf O_\star
=
\{o_{\rm true},o_{\rm false},o_{\rm good}\},
\qquad
\kappa_{T_{\rm good}}(Pr)=o_{\rm good},
\qquad
\mathsf{Pat}(o_{\rm good})
=
\mathsf{LocalPattern}(T_{\rm good},[Ag]_{T_{\rm good}}).
\tag{Closed-Dependencies}
\]

The induced carriers of structural individuals, experience tokens, presentations, actions, local indices, \(V_5\), \(\mathbb Z_7\), and qualities are consequently finite:

\[
\boxed{
\mathsf{FiniteTypedSlice}
\left(
\mathfrak M_{\rm PSR}\upharpoonright N_\star
\right).
}
\tag{Finite-Slice-Pass}
\]

---

## 3. Locality determination

For every frozen stage, all quantifiers and operations range over the named macro fixtures, their finite orbit/experience/presentation/action carriers, the fixed successor and three-content closure, or the fixed finite physical carriers. The relevant global relations are unchanged by the induced restriction.

\[
\boxed{
\mathsf{Verdict}^{\mathfrak M_{\rm PSR}}(b)
\iff
\mathsf{Verdict}^{\mathfrak M_{\rm PSR}\upharpoonright N_\star}(b)
\quad
\left(b\in\{R0,R1,R2,R3.a,R3.b,R3.c\}\right).
}
\tag{Locality-Pass}
\]

This is a finite formal locality finding only. It does not establish empirical realism, consciousness, objective normativity, nonbrute instantiation, a public bridge, or zero residue.

---

## 4. R0 result and next boundary

The frozen R0 requirements are met:

\[
\boxed{
R0(F_{\rm PSR\text{-}5})
=
\mathsf{Pass}_{\rm restricted\ formal}.
}
\tag{R0-Pass}
\]

This makes the next frozen operation eligible, but does not execute it:

\[
\mathsf{Authorized}(F_{\rm PSR\text{-}5},R1)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R1).
\tag{R1-Authorized-Not-Executed}
\]

\[
\bigwedge_{b\in\{R2,R3.a,R3.b,R3.c\}}
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},b).
\tag{No-Later-Execution}
\]

\[
\mathsf{R0Pass}(F_{\rm PSR\text{-}5})
\not\Rightarrow
\mathsf{NoSelectorResidue},
\qquad
\mathsf{R0Pass}(F_{\rm PSR\text{-}5})
\not\Rightarrow
\mathsf{PublicBridgePass},
\qquad
\mathsf{R0Pass}(F_{\rm PSR\text{-}5})
\not\Rightarrow
\mathsf{ZRPass}.
\tag{R0-Limits}
\]
