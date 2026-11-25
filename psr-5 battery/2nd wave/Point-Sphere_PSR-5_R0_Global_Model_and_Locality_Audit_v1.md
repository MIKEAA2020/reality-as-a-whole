# PSR-5 R0 Global-Model and Finite-Locality Audit v1
## First executed stage after PSR-5 restricted-formal entry admission

**Candidate:** \(F_{\rm PSR\text{-}5}\)  
**Packet:** `Plural_Structural_Realism_Entry_Packet_v5.md`  
**Packet SHA-256:** `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**Scope:** R0 only. No R1, R2, R3.a, R3.b, or R3.c stage is executed or credited.

---

## 0. Frozen R0 requirement

R0 requires a typed explicit-infinite global model, actual plurality, quotient-native operations, a finite \(N_\star\)-slice containing all named test dependencies, and a declared local/global equivalence for the frozen battery.

\[
R0:\quad \mathfrak M_{\rm PSR}\upharpoonright N_\star.
\tag{R0-CASE}
\]

No new code, content, selector, primitive relation, fixture, or locality convention is introduced by this audit.

---

## 1. Typed explicit-infinite code and structural carriers

The packet explicitly separates strings from decoded records:

\[
\mathbf C=\{0,1\}^{*}
=
\mathsf{AcceptedCodeStrings}
\sqcup
\mathsf{RejectedStrings},
\tag{CODE-PARTITION}
\]

\[
\mathcal S_{\rm raw}
=
\mathsf{Decode}(\mathsf{AcceptedCodeStrings}),
\qquad
\overline{\mathcal S}
=
\mathcal S_{\rm raw}/\cong_{\rm str}.
\tag{TYPED-QUOTIENT}
\]

Rejected strings are neither raw structural records nor inputs to \(\cong_{\rm str}\). This removes the PSR-4 carrier/quotient typing failure.

The total decode map has exactly three accepted forms:

\[
\begin{array}{c|c}
\textbf{code form} & \textbf{decoded output}\\
\hline
000,001,010,011,100,101,110 & \text{the seven fixed macro records}\\
1110\,\mathsf N(i)\mathsf N(r) & \text{a valid finite carrier-renaming }\pi_r(S_i)\\
1111\,\mathsf N(n) & G_n\text{, the finite all-}Si\text{ trivial record}
\end{array}
\tag{TOTAL-DECODE}
\]

All other code strings are rejected. The two generic branches have no content-body, value-key, successor-body, or field-value subgrammar; hence no such branch is underdetermined.

\[
\boxed{
\mathsf{Defined}
\left(
\mathsf{Decode},
\mathcal S_{\rm raw},
\overline{\mathcal S},
\mathfrak M_{\rm PSR}
\right).
}
\tag{GLOBAL-MODEL-PASS}
\]

---

## 2. Primitive extensions and structural plurality

The exact actual structure extension is:

\[
\mathsf{Instantiates}^{\mathfrak M}
=
\{[S_\Sigma],[S_\Phi]\}.
\tag{ACTUAL-STRUCTURES}
\]

The two actual classes are nonidentical by their typed carriers: \([S_\Sigma]\) has \(Ag\)-roles, whereas \([S_\Phi]\) has five \(Si\)-roles and the Ring5 field. The primitive experience extension is also exactly declared:

\[
\mathsf{ActualExperience}^{\mathfrak M}=
\{\xi_a\},
\quad
\mathsf{Qualia}^{\mathfrak M}=
\{(\xi_a,\mathsf{pain})\},
\quad
\mathsf{ExpRealizes}^{\mathfrak M}=
\{(\xi_a,\iota_{[S_\Sigma],[a]_{S_\Sigma}},\mathsf{pain})\}.
\tag{EXPERIENCE-EXTENSION}
\]

These are declared residuals; R0 neither derives nor discharges them.

---

## 3. Exact finite slice and dependency closure

\[
\boxed{N_\star=3.}
\tag{NSTAR}
\]

No complete generic code has length three: the shortest alias code has a four-bit branch prefix and two nonempty natural codes, and the shortest trivial code has a four-bit prefix plus a nonempty natural code. Thus every decoded class with canonical code length at most three is among the macro fixture vocabulary.

Every frozen structural successor is already a three-bit macro:

\[
T_{\rm neutral},
\qquad T_{\rm bad},
qquad T_{\rm good}.
\tag{SUCCESSOR-CLOSURE}
\]

Every content dependency is fixed in:

\[
\mathbf O_\star
=
\{o_{\rm true},o_{\rm false},o_{\rm good}\},
\tag{CONTENT-CLOSURE}
\]

including:

\[
\kappa_{T_{\rm good}}(Pr)=o_{\rm good},
qquad
\mathsf{Pat}(o_{\rm good})
=
\mathsf{LocalPattern}(T_{\rm good},[Ag]_{T_{\rm good}}).
\tag{GOOD-CONTENT}
\]

Hence no R0–R3 dependency escapes the named finite closure. The multi-sorted carriers \(\mathbf I_{N_\star},\mathbf X_{N_\star},\mathbf P_{N_\star},\mathbf A_{N_\star},\mathbf T_{N_\star},V_5,\mathbb Z_7,\mathbf Q\) are finite.

\[
\boxed{
\mathsf{FiniteTypedSlice}
(\mathfrak M_{\rm PSR}\upharpoonright N_\star).
}
\tag{FINITE-SLICE-PASS}
\]

---

## 4. Locality and R0 verdict

Every frozen stage formula ranges only over a named macro structure, its finite orbit/experience/presentation/action carriers, the exact successor/content closure above, and \(V_5\), \(\mathbb Z_7\), or \(\mathbf Q\). The relevant relations in the global model restrict unchanged to the slice.

\[
\boxed{
\mathsf{Verdict}^{\mathfrak M_{\rm PSR}}(b)
\iff
\mathsf{Verdict}^{\mathfrak M_{\rm PSR}\upharpoonright N_\star}(b)
\quad
\bigl(b\in\{R0,R1,R2,R3.a,R3.b,R3.c\}\bigr).
}
\tag{LOCALITY-PASS}
\]

Therefore:

\[
\boxed{
R0(F_{\rm PSR\text{-}5})
=
\mathsf{Pass}_{\rm restricted\ formal}.
}
\tag{R0-PASS}
\]

This validates only the frozen model/slice interface. It does not establish empirical realism, objective normativity, consciousness, nonbrute instantiation, public-bridge success, or zero residue.

Only R1 is authorized next:

\[
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R1)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R2)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.a)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.b)
\land
\neg\mathsf{Executed}(F_{\rm PSR\text{-}5},R3.c).
\tag{NO-LATER-EXECUTION}
\]
