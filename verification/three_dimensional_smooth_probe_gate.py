#!/usr/bin/env python3
"""3D smooth-switching, first-order pair and finite-cutoff order controls.

Numerical calculations are controls, not proofs of the infinite sums or the
full nonperturbative 3D instrument. Requires requirements-field-probe.txt.
"""
import json
from math import exp, expm1, factorial, pi, sqrt
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
import two_field_spacetime_probe as old

V=(2*pi)**3
D=old.D
A=old.A
Y=old.Y
T=old.T
MA=old.MA
MB=old.MB


def spectral_functions(max_n):
    x,wx=old.quadrature(D,256)
    t,wt=old.quadrature(A,256)
    n=np.arange(max_n+1)
    g=np.cos(np.outer(n,x))@wx
    # Entire even temporal transform, evaluated by power-series coefficients.
    coeff=np.array([(-1.)**j*float(np.dot(wt,t**(2*j)))/factorial(2*j) for j in range(13)])
    def shat(freq):
        return np.polynomial.polynomial.polyval(np.asarray(freq)**2,coeff)
    test=np.linspace(0,30,41)
    assert np.max(np.abs(shat(test)-(np.cos(np.outer(test,t))@wt)))<1e-12
    return g,shat


def labels(N):
    a=np.arange(-N,N+1)
    k=np.stack(np.meshgrid(a,a,a,indexing='ij'),axis=-1).reshape(-1,3)
    r2=np.sum(k*k,axis=1)
    return k,np.sqrt(r2+MA*MA),np.sqrt(r2+MB*MB)


def first_order_pairs(N):
    k,oa,ob=labels(N);G,shat=spectral_functions(2*N)
    norm2=weighted=0.
    for start in range(0,len(k),64):
        p=k[start:start+64,None,:]+k[None,:,:]
        spatial=np.prod(G[np.abs(p)],axis=2)/V
        freq=oa[start:start+64,None]+ob[None,:]
        amp2=(spatial*shat(freq))**2/(4*oa[start:start+64,None]*ob[None,:])
        norm2+=float(np.sum(amp2));weighted+=float(np.sum(freq*amp2))
    return {'N':N,'modes_per_field':len(k),'first_order_pair_norm_squared':norm2,
            'quadratic_vacuum_energy_coefficient':weighted}


def switched_derivative_bound_controls(pair_rows):
    # Numerical quadrature of ||b_a^(r)||_1 using an exact polynomial
    # recurrence for derivatives of exp(-1/(1-u²)). Not interval-certified.
    from numpy.polynomial import Polynomial as Poly
    u=Poly([0,1]);tpoly=Poly([1,0,-1]);P=Poly([1.])
    polys=[P]
    for r in range(4):
        P=tpoly*tpoly*P.deriv()+4*r*u*tpoly*P-2*u*P
        polys.append(P)
    z,w=np.polynomial.legendre.leggauss(512)
    t=1-z*z; raw=np.exp(-1/t);Z=float(np.dot(w,raw))
    norms=[float(np.dot(w,raw*np.abs(polys[r](z))/t**(2*r))/(A**r*Z)) for r in range(5)]
    assert abs(norms[0]-1)<1e-12
    assert abs(norms[1]-2*exp(-1)/(A*Z))<.02
    N=6;_,oa,ob=labels(N)
    z_a4=float(np.sum(oa**(-4)));z_b4=float(np.sum(ob**(-4)))
    pair_upper=norms[3]**2*z_a4*z_b4/(4*2**6*V**2)
    z_a5=float(np.sum(oa**(-5)));z_b5=float(np.sum(ob**(-5)))
    energy_upper=norms[4]**2*(z_a4*z_b5+z_a5*z_b4)/(4*2**8*V**2)
    actual=next(row for row in pair_rows if row['N']==N)
    assert actual['first_order_pair_norm_squared']<=pair_upper
    assert actual['quadratic_vacuum_energy_coefficient']<=energy_upper
    return {'quadrature_approx_switch_derivative_L1':norms,
            'N':N,'finite_cube_pair_majorant_r3':pair_upper,
            'finite_cube_energy_majorant_r4':energy_upper}


def diagonal_test(M=96):
    # Lower-bound diagonal k+l=0; sphere cutoffs 4..M.
    q=np.arange(-M,M+1,dtype=np.int64)
    r2=q[:,None,None]**2+q[None,:,None]**2+q[None,None,:]**2
    counts=np.bincount(r2.ravel(),minlength=3*M*M+1)
    z=np.arange(M*M+1,dtype=float)
    oa=np.sqrt(z+MA*MA);ob=np.sqrt(z+MB*MB)
    times,tw=old.quadrature(A,256)
    freq=oa+ob
    chunks=[]
    for start in range(0,len(freq),512):
        chunks.extend(np.cos(np.outer(freq[start:start+512],times))@tw)
    sh=np.array(chunks)
    instant=np.cumsum(counts[:len(z)]/(4*V*V*oa*ob))
    smooth=np.cumsum(counts[:len(z)]*sh*sh/(4*V*V*oa*ob))
    rows=[]
    for N in (4,8,16,32,64,96):
        rows.append({'N':N,'instantaneous_diagonal_HS_squared':float(instant[N*N]),
                     'smooth_switched_diagonal_HS_squared':float(smooth[N*N])})
    return rows


def quadratures3(N,source_center):
    k,oa,ob=labels(N);d=len(k);G,shat=spectral_functions(2*N)
    lookup={tuple(vec):i for i,vec in enumerate(k)}
    used=set();U=np.zeros((d,d),dtype=complex);col=0
    z=lookup[(0,0,0)];U[z,col]=1;col+=1;used.add((0,0,0))
    for v in k:
        key=tuple(v);neg=tuple(-v)
        if key in used:continue
        i,j=lookup[key],lookup[neg]
        U[i,col]=U[j,col]=1/sqrt(2);col+=1
        U[i,col]=-1j/sqrt(2);U[j,col]=1j/sqrt(2);col+=1
        used.update((key,neg))
    assert col==d and np.max(np.abs(U.conj().T@U-np.eye(d)))<1e-13
    s=k[:,None,:]+k[None,:,:]
    gs=np.prod(G[np.abs(s)],axis=2)*np.exp(1j*s[:,:,0]*Y)
    c_complex=(U.T@gs@U)/V
    assert np.max(np.abs(c_complex.imag))<2e-13
    C=c_complex.real
    sf=np.prod(G[np.abs(k)],axis=1)*np.exp(1j*k[:,0]*source_center)
    fs_c=U.T@sf/sqrt(V)
    assert np.max(np.abs(fs_c.imag))<1e-13
    freq_a=np.sqrt(np.sum(k*k,axis=1)+MA*MA)
    freq_b=np.sqrt(np.sum(k*k,axis=1)+MB*MB)
    # U only mixes +k/-k, which have equal frequencies.
    wreal_a=np.real(np.sum(U.conj()*freq_a[:,None]*U,axis=0))
    wreal_b=np.real(np.sum(U.conj()*freq_b[:,None]*U,axis=0))
    return C,wreal_a,wreal_b,fs_c.real,shat


def response(C,oa,ob,fs,shat,rtol=2e-10):
    d=len(oa)
    source=np.r_[np.zeros(d),fs*shat(oa),np.zeros(2*d)]
    def J(v):return np.r_[v[d:2*d],-v[:d],v[3*d:4*d],-v[2*d:3*d]]
    final=J(source)
    z,w=np.polynomial.legendre.leggauss(128)
    norm=A*np.dot(w,np.exp(-1/(1-z*z)))
    def rhs(t,v):
        chi=old.duration_bump(t)/norm
        if chi==0:return np.zeros_like(v)
        ca,sa=np.cos(oa*t),np.sin(oa*t)/oa
        cb,sb=np.cos(ob*t),np.sin(ob*t)/ob
        qa,pa,qb,pb=np.split(v,4)
        ra=ca*qa+sa*pa;rb=cb*qb+sb*pb
        Ab=C@rb;Ba=C.T@ra
        return chi*np.r_[sa*Ab,-ca*Ab,sb*Ba,-cb*Ba]
    sol=solve_ivp(rhs,(T+A,T-A),final,method='DOP853',rtol=rtol,atol=rtol/100,max_step=.004)
    assert sol.success
    diff=-J(sol.y[:,-1]-final)
    u=np.r_[diff[:d],diff[2*d:3*d]]
    v=np.r_[diff[d:2*d],diff[3*d:]]
    omega=np.r_[oa,ob]
    c=float(np.sum(u*u/(omega*omega)+v*v))
    d0=float(np.sum(u*u/omega+omega*v*v))
    vac_exact=2*sqrt(-expm1(-d0/2))
    vac_bound=min(2.,2*sqrt(d0/2))
    assert vac_exact<=vac_bound+1e-12
    return {'C':c,'D0':d0,'order_trace_bound_E100':min(2.,2*(sqrt(200*c)+sqrt(d0/2))),
            'order_trace_bound_E0':vac_bound,
            'vacuum_unread_joint_fields_order_trace_distance':vac_exact}


def one_dimensional_crosscheck():
    N=3;x,wx=old.quadrature(D,128);b=old.basis(N,x+Y)
    C=(b*wx)@b.T
    oa=old.frequency(N,MA);ob=old.frequency(N,MB)
    fs=old.basis(N,x)@wx;t,tw=old.quadrature(A,128)
    shat=lambda v:np.cos(np.outer(v,t))@tw
    got=response(C,oa,ob,fs,shat)
    previous=old.calc(N)
    assert abs(got['C']-previous['source_response_coefficient_energy_C'])<1e-10
    assert abs(got['D0']-previous['source_response_vacuum_D0'])<1e-10
    return got


def derivative_counterexample():
    # H_int = a†b† + ab,  H_free = number_A+number_B, E=2.
    # For n>=3, the three possible output number states are distinct.
    E=2.;vals=[]
    for n in (3,10,100,10000,1000000):
        p=E/(2*n)
        variance=(1-p)+p*((n+1)**2+n*n)
        slope=2*sqrt(variance)
        vals.append({'n':n,'mean_free_energy':2*n*p,'channel_trace_derivative':slope})
        assert abs(2*n*p-E)<1e-12
    return vals


def main():
    assert Y-2*D>T+2*A
    pair=[first_order_pairs(n) for n in (1,2,3,4,5,6)]
    assert all(a['first_order_pair_norm_squared']<b['first_order_pair_norm_squared'] for a,b in zip(pair,pair[1:]))
    order=[]
    for N in (1,2,3):
        C,oa,ob,fs,hat=quadratures3(N,0.)
        out=response(C,oa,ob,fs,hat)
        out.update({'N':N,'modes_per_field':len(oa),'source_center':0.})
        order.append(out)
    C,oa,ob,fs,hat=quadratures3(2,Y)
    positive=response(C,oa,ob,fs,hat)
    assert positive['D0']>order[1]['D0']
    C,oa,ob,fs,hat=quadratures3(3,0.)
    fine=response(C,oa,ob,fs,hat,rtol=2e-12)
    assert abs(fine['C']-order[-1]['C'])<2e-11
    assert abs(fine['D0']-order[-1]['D0'])<2e-11
    result={'status':'passed','scope':'finite-mode ODE, lattice sum and counterexample arithmetic controls only',
        'minimum_spatial_separation':Y-2*D,'maximum_temporal_separation':T+2*A,
        'first_order_cube_cutoff_pair_sums':pair,'pair_diagonal_sphere_sums':diagonal_test(),
        'finite_cube_derivative_majorant_controls':switched_derivative_bound_controls(pair),
        'finite_mode_3d_order_rows':order,'N3_ode_refinement':fine,
        'nonspacelike_colocated_N2_control':positive,
        'one_dimensional_backward_ode_crosscheck':one_dimensional_crosscheck(),
        'bounded_mean_energy_derivative_counterexample':derivative_counterexample()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
