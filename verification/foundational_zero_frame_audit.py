#!/usr/bin/env python3
"""Exact scope controls for the zero-constraint and energy-frame proposals.

These mathematical controls do not determine actual experience or full reality.
"""
import math


def observer_field_power(rho, electric_x, beta):
    """h=-j^mu F_mu_nu u^nu, for j=(rho,0,0,0), F_10=E_x."""
    if abs(beta)>=1: raise ValueError('observer must be timelike')
    gamma=1/math.sqrt(1-beta*beta)
    return rho*electric_x*gamma*beta


def em_energy_current(electric_y, magnetic_z, beta):
    """C^mu=-T^{mu nu}u_nu for transverse E,B and x-directed observer."""
    if abs(beta)>=1: raise ValueError('observer must be timelike')
    gamma=1/math.sqrt(1-beta*beta)
    energy=(electric_y**2+magnetic_z**2)/2
    poynting=electric_y*magnetic_z
    return gamma*(energy-beta*poynting), gamma*(poynting-beta*energy)


def flrw_data(p_phi, volume=1., kappa=1.):
    if p_phi<=0 or volume<=0 or kappa<=0: raise ValueError('parameters must be positive')
    a=volume**(1/3)
    pa=-math.sqrt(6/kappa)*p_phi/a
    constraint=-kappa*pa**2/(12*a)+p_phi**2/(2*a**3)
    density=p_phi**2/(2*volume**2)
    H=math.sqrt(kappa/3*density)
    curvature=-2*kappa*density
    return {'constraint':constraint,'density':density,'hubble':H,'ricci':curvature}


def ohmic_candidate_valence(electric_rest, conductivity, incidence_density=1., alpha=1.):
    if conductivity < 0 or incidence_density <= 0 or alpha <= 0:
        raise ValueError('require nonnegative conductivity and positive incidence and alpha')
    return -alpha*conductivity*electric_rest**2/incidence_density


def balanced_positive_intensity(negative_probability):
    if not 0<negative_probability<1: raise ValueError('strict probability required')
    return negative_probability/(1-negative_probability)
