"""Independent exact spot checks of claims in the supplied constitutive transcript.

Requires SymPy. These are new checks, not the unavailable release scripts.
Run: python verification/constitutive_checks.py
"""
import itertools
import json
import sympy as s

I = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
Z = s.diag(1, -1)
kron = s.kronecker_product
I4 = s.eye(4)
results = {}

# Mermin-Peres operator contexts and all deterministic assignments.
square = [[kron(X,I), kron(I,X), kron(X,X)],
          [kron(I,Z), kron(Z,I), kron(Z,Z)],
          [kron(X,Z), kron(Z,X), kron(Y,Y)]]
contexts = square + [[square[r][c] for r in range(3)] for c in range(3)]
signs = [1, 1, 1, 1, 1, -1]
for ctx, sign in zip(contexts, signs):
    assert ctx[0]*ctx[1]*ctx[2] == sign*I4
    assert all(a*b == b*a for a,b in itertools.combinations(ctx,2))
max_satisfied, max_score = 0, -6
for vals in itertools.product([-1,1], repeat=9):
    prods = [s.prod(vals[3*r+c] for c in range(3)) for r in range(3)]
    prods += [s.prod(vals[3*r+c] for r in range(3)) for c in range(3)]
    signed = [a*b for a,b in zip(prods, signs)]
    max_satisfied = max(max_satisfied, signed.count(1))
    max_score = max(max_score, sum(signed))
assert (max_satisfied, max_score) == (5,4)
results['magic_square'] = {'valuations':512, 'max_contexts':5, 'classical_bound':4, 'quantum_value':6}

# Real quantum counterexample: all real symmetric product effects agree.
YY = kron(Y,Y)
rp, rm = (I4+YY)/4, (I4-YY)/4
for rho in [rp,rm]:
    assert rho == rho.T and s.trace(rho) == 1
    assert all(v >= 0 for v in rho.eigenvals())
for a,b in itertools.product([I,X,Z], repeat=2):
    assert s.trace((rp-rm)*kron(a,b)) == 0
E = (I4+YY)/2
assert s.trace(rp*E) == 1 and s.trace(rm*E) == 0
results['real_local_tomography_counterexample'] = 'passed: 9 product-basis statistics agree; joint effect gives 1 versus 0'

# Rank-dimension identities: formal same-family rank n^2 comparison only.
n = s.symbols('n', integer=True, positive=True)
dims = {'real': n*(n+1)/2, 'complex':n**2, 'quaternionic':n*(2*n-1)}
expected = {'real':n**2*(n-1)**2/4, 'complex':0, 'quaternionic':-2*n**2*(n-1)**2}
for name,D in dims.items():
    delta = s.expand(D.subs(n,n**2)-D**2)
    assert s.simplify(delta-expected[name]) == 0
results['rank_dimension_identities'] = {name:str(s.factor(D.subs(n,n**2)-D**2)) for name,D in dims.items()}

# Connected four-node diffusion with internal edges 1 and cross edges epsilon.
e = s.symbols('epsilon', positive=True)
L = s.Matrix([[1+2*e,-1,-e,-e],[-1,1+2*e,-e,-e],[-e,-e,1+2*e,-1],[-e,-e,-1,1+2*e]])
P = s.Matrix([[1,1,0,0],[0,0,1,1]])
LM = s.Matrix([[2*e,-2*e],[-2*e,2*e]])
assert P*L == LM*P
assert L.eigenvals() == {s.Integer(0):1,4*e:1,2+2*e:2}
results['macro_dynamics'] = {'intertwining':'PL = LM P', 'eigenvalues':['0','4 epsilon','2+2 epsilon (twice)']}

# Fisher binary metric and symmetric-noise contraction.
p,q = s.symbols('p q', positive=True)
u = 2*s.asin(s.sqrt(p))
assert s.simplify(s.diff(u,p)**2-1/(p*(1-p))) == 0
r = q+(1-2*q)*p
# Nonnegative on p in (0,1), q in [0,1].
assert s.simplify(r*(1-r)-(1-2*q)**2*p*(1-p)-q*(1-q)) == 0
results['binary_fisher_geometry'] = 'coordinate identity and noise contraction identity passed'

# Bounded rootless recurrence: n to n+k, not an actuality proof.
k = s.symbols('k', integer=True, positive=True)
y = s.symbols('y')
f = lambda t:(1+t)/2
v = y
for j in range(1,9):
    v = f(v)
    assert s.simplify(v-(1+(y-1)/2**j)) == 0
results['rootless_recurrence'] = 'exact iterate identity checked for k=1..8; boundedness gives unique all-ones solution'

# Complex multiplication from Jordan and commutator products.
for a,b in itertools.product([I,X,Y,Z], repeat=2):
    jordan = (a*b+b*a)/2
    psi = s.I*(a*b-b*a)/2
    assert jordan-s.I*psi == a*b
results['jordan_commutator_product'] = '16 basis pairs passed'

# Qubit cone determinant identity.
t,x,y,z = s.symbols('t x y z', real=True)
assert s.expand((t*I+x*X+y*Y+z*Z).det()) == t**2-x**2-y**2-z**2
results['qubit_lorentz_cone'] = 'determinant identity passed; no spacetime identification inferred'

# Bell and mixed marginals and partial transpose.
bell = s.Matrix([1,0,0,1])/s.sqrt(2)
rho = bell*bell.T
marginal = s.Matrix(2,2,lambda a,b:sum(rho[2*a+j,2*b+j] for j in range(2)))
assert marginal == I/2 and s.trace(rho*rho) == 1
assert s.trace((I4/4)**2) == s.Rational(1,4)
pt = s.Matrix(4,4,lambda i,j:rho[2*(i//2)+(j%2),2*(j//2)+(i%2)])
assert min(pt.eigenvals()) == -s.Rational(1,2)
results['bell_checks'] = 'equal single-party marginals; distinct purities; partial transpose eigenvalue -1/2'

print(json.dumps({'scope':'independent exact spot checks; not verification of release code or universal reconstruction theorems', 'results':results},indent=2))
