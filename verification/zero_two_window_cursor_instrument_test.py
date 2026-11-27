"""Outcome instrument and backaction for the autonomous cursor reader.

Finite-grid chiral-comparator controls use the actual old Ω and Q. The
massive-cursor continuum bound and physical preparation assumptions are in
ZERO_TWO_WINDOW_CURSOR_INSTRUMENT_AND_BACKACTION.md; numerical controls do
not establish them or a quantum-gravity clock switch.
"""
import math
import unittest
import numpy as np
from scipy.integrate import solve_ivp

from verification.zero_two_window_autonomous_support_dynamics_test import system
from verification.zero_two_window_redundant_flag_hold_test import collective_y
from verification.zero_two_window_autonomous_cursor_reader_test import (
    N,G,A,WIDTH,V,MASS,KAPPA,C,T0,END,RET,pulse_scaled,error_bounds)


def channel_budget(T=RET):
    K,_,pulse,_=error_bounds()
    dyn=N*G*C*T*T/2
    disp=T*K/(2*MASS)
    # A normalized ideal Q-record environment is slightly different from the
    # unnormalized flag branch; its Stinespring distance is ≤sqrt(2)*eta.
    eta=math.sin(G*A/V)**N
    return dyn+pulse+disp+math.sqrt(2)*eta


def trace_distance(a,b):
    z=(a-b);z=(z+z.conj().T)/2
    return float(np.sum(abs(np.linalg.eigvalsh(z)))/2)


def regulated_instrument(h=0,offset=0.,strength=1.,output_time=RET):
    """Construct two input columns, returning output vectors and controls.

    Single-position chiral comparison, grid 4, actual two-window operators.
    The unbounded massive cursor and wavepacket are not numerically evolved.
    """
    _,B,P,Q,O,_=system(4,h)
    dim=len(Q);S=collective_y(N);sy=np.array([[0,-1j],[1j,0]])
    H=np.kron(O,np.eye(N+1))+G*np.kron(Q,S)
    vals,W=np.linalg.eigh(H)
    oval,ow=np.linalg.eigh(O)
    rng=np.random.default_rng(2026)
    outside=Q@(rng.normal(size=dim)+1j*rng.normal(size=dim))
    outside/=np.linalg.norm(outside)
    basis=np.column_stack((B[:,0],outside))
    ready=np.zeros(N+1);ready[0]=1
    flag=np.ones(N+1);flag[0]=0
    center=T0-offset/V; tbegin=center-WIDTH/V; after=output_time-(center+WIDTH/V)
    if after<0: raise ValueError('output time must be after the pulse')

    def evolve(psi):
        z=np.kron(psi,ready)
        z=W@(np.exp(1j*vals*tbegin)*(W.conj().T@z))
        state=np.zeros((dim,N+1,2),complex);state[:,:,0]=z.reshape(dim,N+1)
        def rhs(u,y):
            a=y.reshape(dim,N+1,2)
            free=(H@a.reshape(dim*(N+1),2)).reshape(dim,N+1,2)
            read=(a*flag[None,:,None])@sy.T
            return (1j*((WIDTH/V)*free+strength*KAPPA*pulse_scaled(u)*read)).ravel()
        r=solve_ivp(rhs,(-1,1),state.ravel(),method='DOP853',rtol=2e-10,atol=1e-12)
        if not r.success:raise RuntimeError(r.message)
        post=r.y[:,-1].reshape(dim*(N+1),2)
        return (W@(np.exp(1j*vals*after)[:,None]*(W.conj().T@post))).reshape(dim,N+1,2)
    vectors=np.stack([evolve(basis[:,j]) for j in range(2)])
    UO=(ow*np.exp(1j*oval*output_time))@ow.conj().T
    return vectors,basis,UO


def branch(vectors,rho,m):
    a=vectors[:,:,:,m]
    return np.einsum('aik,ab,bjk->ij',a,rho,a.conj(),optimize=True)


def target(basis,UO,rho,m):
    u=UO@basis[:,m]
    return rho[m,m]*np.outer(u,u.conj())


class CursorInstrumentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vectors,cls.basis,cls.U=regulated_instrument()

    def test_all_input_columns_form_a_complete_instrument(self):
        v=self.vectors.reshape(2,-1)
        np.testing.assert_allclose(v.conj()@v.T,np.eye(2),atol=4e-10)
        for rho in (np.eye(2)/2,np.array([[.5,.5],[.5,.5]]),
                    np.array([[.3,.2j],[-.2j,.7]])):
            out=[branch(self.vectors,rho,m) for m in (0,1)]
            self.assertAlmostEqual(sum(np.trace(x).real for x in out),1.,places=9)
            for x in out:
                np.testing.assert_allclose(x,x.conj().T,atol=1e-12)
                self.assertGreater(np.linalg.eigvalsh(x)[0],-1e-12)

    def test_full_state_channel_budget_larger_than_probability_only_budget(self):
        d=channel_budget();_,previous,pulse,disp=error_bounds()
        self.assertLess(d,.0662)
        self.assertGreater(d,previous+pulse+disp)
        self.assertLess(2*d,.1324)

    def test_both_joint_branch_states_match_lueders_comparator(self):
        d=channel_budget()
        for rho in (np.eye(2)/2,np.array([[.5,.5],[.5,.5]]),
                    np.array([[.3,.2j],[-.2j,.7]])):
            actual=[branch(self.vectors,rho,m) for m in (0,1)]
            ref=[target(self.basis,self.U,rho,m) for m in (0,1)]
            distance=sum(trace_distance(x,y) for x,y in zip(actual,ref))
            self.assertLess(distance,d+1e-9)
            self.assertLess(abs(np.trace(actual[1]).real-rho[1,1].real),.01849)

    def test_coherent_superposition_has_inevitable_system_backaction(self):
        rho=np.array([[.5,.5],[.5,.5]])
        actual=sum((branch(self.vectors,rho,m) for m in (0,1)))
        incoming=self.U@self.basis@rho@self.basis.conj().T@self.U.conj().T
        self.assertGreaterEqual(trace_distance(actual,incoming),.5-channel_budget()-1e-9)
        expected=sum((target(self.basis,self.U,rho,m) for m in (0,1)))
        self.assertAlmostEqual(trace_distance(expected,incoming),.5,places=11)

    def test_sector_inputs_and_conditional_results(self):
        d=channel_budget()
        for m in (0,1):
            rho=np.diag([1. if j==m else 0. for j in (0,1)])
            b=branch(self.vectors,rho,m);p=np.trace(b).real
            self.assertGreater(p,1-.000343)
            normalized=b/p
            ideal=target(self.basis,self.U,rho,m)
            self.assertLess(trace_distance(normalized,ideal),2*d/(1-d)+1e-9)

    def test_no_coupling_gives_no_memory_click(self):
        vec,_,_=regulated_instrument(strength=0.)
        rho=np.array([[.5,.5],[.5,.5]])
        self.assertLess(np.trace(branch(vec,rho,1)).real,1e-20)


if __name__=='__main__':unittest.main()
