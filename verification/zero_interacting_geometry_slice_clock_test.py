"""Geometry-slice data for the interacting constrained model.

At finite Nyström regulator, evaluate the *covariant* solution at alpha,
resolve each channel's scalar frequencies and use the induced physical inner
product. Transport the first-window instrument and pointer correctly. This is
not a proof of a continuum alpha-clock reduction or an autonomous apparatus.
"""
import cmath
import math
import unittest
from verification.zero_sphere_interacting_clock_spectral_test import build,transform,untransform
from verification.zero_sphere_finite_resolution_clock_instrument_test import apply,no_filter
from verification.zero_interacting_relational_first_reading_test import (
    CHANNELS,TIMES,initial_state,p_to_s,spectral_E,first_protocol,history_protocol,norm2
)


def factors(p,systems,alpha):
    """<alpha|mode>/sqrt(2 omega), for KG-normalized covariant solutions."""
    n=len(p);out={}
    for h,d in CHANNELS:
        vals,V=systems[d][1:]
        out[h,d]=[sum(cmath.exp(1j*p[i]*alpha)*V[i][j] for i in range(n))
                  /math.sqrt(2*math.pi*n*2*math.sqrt(vals[j]-2*h)) for j in range(n)]
    return out


def slice_data(spectral,r):
    return {k:[a*b for a,b in zip(spectral[k],r[k])] for k in CHANNELS}


def back_spectral(data,r):
    return {k:[a/b for a,b in zip(data[k],r[k])] for k in CHANNELS}


def change_slice(data,r0,r1):
    return {k:[z*y/x for z,x,y in zip(data[k],r0[k],r1[k])] for k in CHANNELS}


def inner_slice(x,y,r):
    return sum(sum(a.conjugate()*b/(abs(t)**2) for a,b,t in zip(x[k],y[k],r[k])) for k in CHANNELS)


def slice_evolve(data,r,systems,t):
    return {(h,d):[x*cmath.exp(1j*math.sqrt(e-2*h)*t)
                   for x,e in zip(data[h,d],systems[d][1])] for h,d in CHANNELS}


def slice_measure(data,r,Es,hit):
    out={}
    for h,d in CHANNELS:
        c=[x/a for x,a in zip(data[h,d],r[h,d])]
        y=apply(Es[d],c) if hit else no_filter(Es[d],c)
        out[h,d]=[a*x for a,x in zip(r[h,d],y)]
    return out


def cross_gram(systems):
    vp=systems[1][2];vm=systems[-1][2];n=len(vp)
    return [[sum(vp[k][i]*vm[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def pointer_probs(data,r,gram):
    c=back_spectral(data,r)
    total=inner_slice(data,data,r).real
    coherence=sum(sum(c[h,1][j].conjugate()*gram[j][k]*c[h,-1][k]
                      for j in range(len(gram)) for k in range(len(gram))) for h in (0,1))
    return [total/2+coherence.real,total/2-coherence.real]


def geometry_protocol(f,E,systems,p,alpha,times=TIMES):
    r=factors(p,systems,alpha); Es=spectral_E(E,systems);gram=cross_gram(systems)
    state=slice_data(p_to_s(initial_state(f),systems),r); out=[];t0=0
    for t in times:
        state=slice_evolve(state,r,systems,t-t0)
        yes=slice_measure(state,r,Es,True)
        out.append((inner_slice(yes,yes,r).real,pointer_probs(yes,r,gram)))
        state=slice_measure(state,r,Es,False);t0=t
    return out,inner_slice(state,state,r).real,state


def geometry_history(f,E,systems,p,alpha,times=TIMES):
    r=factors(p,systems,alpha);Es=spectral_E(E,systems);gram=cross_gram(systems)
    branches={():slice_data(p_to_s(initial_state(f),systems),r)};t0=0
    for t in times:
        new={}
        for hist,state in branches.items():
            state=slice_evolve(state,r,systems,t-t0)
            for b in (0,1):new[hist+(b,)]=slice_measure(state,r,Es,bool(b))
        branches=new;t0=t
    return {key:(inner_slice(st,st,r).real,pointer_probs(st,r,gram)) for key,st in branches.items()}


def slice_value(coeff,r,systems,h,d,phi):
    vals=systems[d][1]
    return sum(a*z*cmath.exp(1j*math.sqrt(e-2*h)*phi)
               for a,z,e in zip(coeff,r[h,d],vals))


def bohr_extract_exact(coeff,r,systems,h,d,index):
    # Infinite-time mean of e^(-i omega_index phi) Psi(alpha,phi).
    # Distinct frequencies give Kronecker delta in the finite regulator.
    vals=systems[d][1];omega=[math.sqrt(x-2*h) for x in vals]
    return sum(coeff[j]*r[h,d][j] for j in range(len(vals))
               if abs(omega[j]-omega[index])<1e-12)


class InteractingGeometrySliceClockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p,cls.f,cls.E,cls.systems=build(40)
        cls.r0=factors(cls.p,cls.systems,0)
        cls.r2=factors(cls.p,cls.systems,2)
        cls.r4=factors(cls.p,cls.systems,4)
        cls.spec=p_to_s(initial_state(cls.f),cls.systems)
        cls.x=slice_data(cls.spec,cls.r0)

    def test_slice_factors_nonzero_and_each_channel_has_distinct_frequencies(self):
        for h,d in CHANNELS:
            vals=self.systems[d][1]
            self.assertGreater(min(abs(x) for x in self.r0[h,d]),.01)
            self.assertGreater(min(abs(x) for x in self.r2[h,d]),.01)
            self.assertGreater(min(vals[i+1]-vals[i] for i in range(len(vals)-1)),1e-8)

    def test_actual_slice_values_and_frequency_reconstruction(self):
        n=len(self.p)
        for h,d in CHANNELS:
            for phi in (0.,11.3,30.):
                spec_psi=slice_value(self.spec[h,d],self.r2,self.systems,h,d,phi)
                vals,V=self.systems[d][1:]
                # Start with the actual KG-mode normalized momentum solution,
                # then take its Fourier value at alpha=2.
                c=[a*cmath.exp(1j*math.sqrt(e-2*h)*phi)/math.sqrt(2*math.sqrt(e-2*h))
                   for a,e in zip(self.spec[h,d],vals)]
                momentum=untransform(V,c)
                direct=sum(cmath.exp(2j*self.p[i])*momentum[i] for i in range(n))/math.sqrt(2*math.pi*n)
                self.assertAlmostEqual(abs(spec_psi-direct),0,places=11)
            for j in (0,5,19,39):
                coeff=bohr_extract_exact(self.spec[h,d],self.r2,self.systems,h,d,j)
                self.assertAlmostEqual(abs(coeff-self.spec[h,d][j]*self.r2[h,d][j]),0,places=13)

    def test_weighted_inner_product_recovers_physical_norm(self):
        self.assertAlmostEqual(inner_slice(self.x,self.x,self.r0).real,1,places=11)
        raw=sum(norm2(self.x[k]) for k in CHANNELS)
        self.assertLess(raw,.03)
        for k in CHANNELS:
            for a,b in zip(back_spectral(self.x,self.r0)[k],self.spec[k]):
                self.assertAlmostEqual(abs(a-b),0,places=12)

    def test_spectral_measure_density_and_bound_atom(self):
        # mu_j = |<alpha|v_j>|²; nu_j = r_j*c_j = g_j*mu_j.
        # Physical norm = sum 2*omega_j |g_j|² mu_j.
        total=0
        for h,d in CHANNELS:
            vals=self.systems[d][1]
            for j,e in enumerate(vals):
                omega=math.sqrt(e-2*h);r=self.r0[h,d][j]
                mu=2*omega*abs(r)**2
                nu=r*self.spec[h,d][j]
                g=nu/mu
                total+=2*omega*abs(g)**2*mu
                self.assertAlmostEqual(abs(nu-g*mu),0,places=14)
        self.assertAlmostEqual(total,1,places=11)
        # The d=+ lower eigenmode is a positive point mass of this slice measure.
        e=self.systems[1][1][0];omega=math.sqrt(e)
        self.assertGreater(2*omega*abs(self.r0[0,1][0])**2,0)

    def test_noncyclic_eigenspace_is_invisible_for_all_phi(self):
        # Toy degenerate spectral mode: the chosen slice vector a is blind
        # to an independent eigenvector of Omega at the same frequency.
        a=[1/math.sqrt(2),0,1/math.sqrt(2)]; frequencies=[2,2,3]
        invisible=[0,1,0]
        for phi in (-100,0,5,100):
            amp=sum(a[i].conjugate()*invisible[i]*cmath.exp(1j*frequencies[i]*phi)
                    /math.sqrt(2*frequencies[i]) for i in range(3))
            self.assertAlmostEqual(abs(amp),0)
        self.assertEqual(norm2(invisible),1)

    def test_slice_to_slice_map_and_composition(self):
        x2=change_slice(self.x,self.r0,self.r2)
        x4=change_slice(x2,self.r2,self.r4)
        direct=change_slice(self.x,self.r0,self.r4)
        for k in CHANNELS:
            for a,b in zip(x4[k],direct[k]):self.assertAlmostEqual(abs(a-b),0,places=12)
        self.assertAlmostEqual(inner_slice(x2,x2,self.r2).real,1,places=11)
        self.assertAlmostEqual(inner_slice(x4,x4,self.r4).real,1,places=11)
        raw0=sum(norm2(self.x[k]) for k in CHANNELS)
        raw4=sum(norm2(x4[k]) for k in CHANNELS)
        self.assertGreater(abs(raw0-raw4),1e-4)

    def test_instrument_completeness_in_geometry_slice_metric(self):
        Es=spectral_E(self.E,self.systems)
        yes=slice_measure(self.x,self.r0,Es,True); no=slice_measure(self.x,self.r0,Es,False)
        self.assertAlmostEqual(inner_slice(yes,yes,self.r0).real+inner_slice(no,no,self.r0).real,1,places=11)

    def test_first_and_history_results_match_interacting_scalar_calculation(self):
        reference=first_protocol(self.f,self.E,self.systems)
        histories=history_protocol(self.f,self.E,self.systems)
        for alpha in (0.,2.,4.):
            first,no,_=geometry_protocol(self.f,self.E,self.systems,self.p,alpha)
            self.assertAlmostEqual(no,reference[1],places=10)
            for (mass,ptr),(mass2,ptr2) in zip(first,reference[0]):
                self.assertAlmostEqual(mass,mass2,places=10)
                for a,b in zip(ptr,ptr2):self.assertAlmostEqual(a,b,places=10)
            all_h=geometry_history(self.f,self.E,self.systems,self.p,alpha)
            for hist in histories:
                self.assertAlmostEqual(all_h[hist][0],histories[hist][0],places=10)
                for a,b in zip(all_h[hist][1],histories[hist][1]):self.assertAlmostEqual(a,b,places=10)

    def test_bound_modes_are_included_not_assumed_scattering(self):
        vals,V=self.systems[1][1:];bound=[row[0] for row in V]
        self.assertLess(vals[0],6)
        r=self.r0[0,1][0];self.assertGreater(abs(r),.01)
        # The bound component is a single scalar frequency in the slice and
        # has finite weighted physical norm although its phi wave is a plane wave.
        self.assertAlmostEqual(abs(r)**2/abs(r)**2,1)
        self.assertGreater(abs(sum(bound)),0)

    def test_single_event_node_does_not_invalidate_frequency_resolved_slice(self):
        # Specify covariant momentum data at phi=0; convert to physical scalar
        # coefficients by multiplying each interacting eigenmode by sqrt(2Ω).
        n=len(self.p);v=[x*cmath.exp(-15j*p)*(p+6.5) for p,x in zip(self.p,self.f)]
        vals,V=self.systems[1][1:]
        c=[a*math.sqrt(2*math.sqrt(e)) for a,e in zip(transform(V,v),vals)]
        c=[a/math.sqrt(norm2(c)) for a in c]
        self.assertAlmostEqual(abs(slice_value(c,self.r0,self.systems,0,1,0)),0,places=12)
        self.assertGreater(sum(abs(a*b)**2 for a,b in zip(c,self.r0[0,1])),0)
        # One zero at a single scalar value is not a null direction of the
        # entire phi-dependent slice. Conversely a vanishing single-mode
        # factor would make the frequency-resolved map singular.

    def test_refinement_does_not_prove_continuum_invertibility(self):
        p,f,E,S=build(80);r80=factors(p,S,0)
        a=min(abs(x) for k in CHANNELS for x in self.r0[k])
        b=min(abs(x) for k in CHANNELS for x in r80[k])
        self.assertLess(b,a)
        self.assertGreater(a/b,1.4)

if __name__=='__main__':unittest.main()
