"""A coherent Slater rotation between a filled negative and empty positive mode."""
import cmath
import math
import importlib.util
from pathlib import Path
s=importlib.util.spec_from_file_location('coherent_packet_reference',Path(__file__).resolve().parents[1]/'wilson_wavepacket_composite'/'model.py')
p=importlib.util.module_from_spec(s);s.loader.exec_module(p)
w=p.w


def parameters(a,n,theta,phase):
    w.parameters(a,n,1.)
    if a*4>=math.pi or not math.isfinite(theta) or not 0<=theta<=math.pi/2 or not math.isfinite(phase):raise ValueError('Require 4a<pi, angle in [0,pi/2], and finite phase')


def matrix(theta=math.pi/4,phase=.3):
    parameters(.1,1,theta,phase);s,c=math.sin(theta),math.cos(theta);z=s*c*cmath.exp(1j*phase)
    return ((s*s,z),(z.conjugate(),-s*s))


def packet(mode,x,t=0.,a=None,j=0,component=0,energy_action=False,steps=600):
    if mode not in (0,1) or component not in (0,1) or not isinstance(j,int) or j<0 or not math.isfinite(x) or not math.isfinite(t):raise ValueError('Invalid packet argument')
    if a is not None:parameters(a,1,0,0)
    def f(k):
        q=k if mode==0 else -(k+1)
        e=2*math.sin(a*q/2)/a if a is not None else q
        spin=(math.cos(a*q/4) if component==0 else math.sin(a*q/4)) if a is not None else (1 if component==0 else 0)
        return p.amplitude(k)*spin*(1j*q)**j*(e if energy_action else 1)*cmath.exp(1j*(q*x-e*t))
    return p.integral(f,steps)/math.sqrt(2*math.pi)


def B(i,j):return p.integral(lambda k:p.amplitude(k)*(k if i==0 else k+1)**j)/math.sqrt(2*math.pi)
def D(i,j,t):return B(i,j+2)/32+abs(t)*B(i,j+3)/24


def kernel(x,y,t=0.,a=None,theta=math.pi/4,phase=.3):
    M=matrix(theta,phase)
    return sum(M[i][j]*packet(i,x,t,a)*packet(j,y,t,a).conjugate() for i in (0,1) for j in (0,1))


def target(x,t=0.,theta=math.pi/4,phase=.3):
    M=matrix(theta,phase)
    return sum(M[i][j]*packet(i,x,t,j=1)*packet(j,x,t).conjugate() for i in (0,1) for j in (0,1)).imag


def terms(a,n,x,t=0.,theta=math.pi/4,phase=.3):
    parameters(a,n,theta,phase);h=a*n;plus,minus=x+h/2,x-h/2
    linear=w.shape(n)*kernel(plus,minus,t,a,theta,phase).imag/h
    wedge=packet(0,plus,t,a)*packet(1,minus,t,a)-packet(1,plus,t,a)*packet(0,minus,t,a)
    determinant=-math.pi*math.sin(theta)**2*abs(wedge)**2
    return linear,determinant


def current(a,n,x,t=0.,theta=math.pi/4,phase=.3):return sum(terms(a,n,x,t,theta,phase))


def covariance(a,n,x,t=0.,theta=math.pi/4,phase=.3):
    parameters(a,n,theta,phase);sites=(x+a*n/2,x-a*n/2);base=w.same_chirality_covariance(a,n)
    return tuple(tuple(base[i][j]+a*kernel(sites[i],sites[j],t,a,theta,phase) for j in (0,1)) for i in (0,1))


def error_bound(a,n,t=0.,theta=math.pi/4,phase=.3):
    parameters(a,n,theta,phase);M=matrix(theta,phase);h=a*n;Q=0.;disp=0.;T=0.
    for i in (0,1):
        for j in (0,1):
            v=abs(M[i][j]);Q+=v*(B(i,3)*B(j,0)+3*B(i,2)*B(j,1)+3*B(i,1)*B(j,2)+B(i,0)*B(j,3))/48
            disp+=v*(D(i,1,t)*B(j,0)+B(i,1)*D(j,0,t));T+=v*B(i,1)*B(j,0)
    G=math.pi*math.sin(theta)**2*h*h*(B(0,0)*B(1,1)+B(1,0)*B(0,1))**2
    return w.shape(n)*(h*h*Q+a*a*disp)+(w.shape(n)-1)*T+G


def local_energy(a,x,t=0.,theta=math.pi/4,phase=.3):
    parameters(a,1,theta,phase);M=matrix(theta,phase)
    return sum(M[i][j]*packet(j,x,t,a,component=c).conjugate()*packet(i,x,t,a,component=c,energy_action=True) for i in (0,1) for j in (0,1) for c in (0,1)).real


def total_energy(a=None,theta=math.pi/4):
    parameters(a if a is not None else .1,1,theta,0)
    return math.sin(theta)**2*p.integral(lambda k:p.amplitude(k)**2*((2*math.sin(a*k/2)/a+2*math.sin(a*(k+1)/2)/a) if a is not None else 2*k+1))
