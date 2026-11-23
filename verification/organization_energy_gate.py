#!/usr/bin/env python3
"""Analytic Maxwell continuity control for organization-weighted exchange.

Fixed background; externally specified conserved charge and incidence currents.
The marker is not an established subject or experience law.
"""
import math


def fields(t,x,a=.4,b=.3):
    if not 0 <= a < 1 or not 0 < b < 1: raise ValueError('require 0<=a<1 and 0<b<1')
    u=1+b*math.sin(t/2)*math.cos(x)
    chi=1+a*math.cos(x-t/2)
    dt_u=(b/2)*math.cos(t/2)*math.cos(x)
    dt_chi=(a/2)*math.sin(x-t/2)
    dx_chi=-a*math.sin(x-t/2)
    return u,chi,dt_u,dt_chi,dx_chi


def numerical_integrals(points=256,a=.4,b=.3):
    if points<4: raise ValueError('grid too small')
    dx=2*math.pi/points; dt=4*math.pi/points
    unweighted=weighted=correction=0.
    for ti in range(points):
        t=(ti+.5)*dt
        for xi in range(points):
            x=(xi+.5)*dx
            u,chi,dt_u,dt_chi,dx_chi=fields(t,x,a,b)
            unweighted+=dt_u*dx*dt
            weighted+=chi*dt_u*dx*dt
            correction-=u*dt_chi*dx*dt
    return {'unweighted':unweighted, 'weighted':weighted, 'correction':correction,
            'analytic_weighted':a*b*math.pi**2}
