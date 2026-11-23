"""Exact two-mode conservative oscillator with positive energy components.

The experiential interpretation is a hypothesis, not a physical conclusion.
"""
import argparse
import json
import math


def state(t):
    return math.sin(t), math.cos(t), math.sin(2*t), 2*math.cos(2*t)


def values(t):
    q1,p1,q2,p2=state(t)
    voltage=2+q1+q2/2
    total=1+(q1*q1+p1*p1)/2+(p2*p2+4*q2*q2)/2
    part=voltage*voltage/8
    transfer=voltage*(p1+p2/2)/4
    return total,part,total-part,transfer


def midpoint_summary(steps):
    if steps<=0: raise ValueError('steps must be positive')
    dt=2*math.pi/steps
    positive=negative=0
    plus=minus=0.0
    min_part=min_rest=float('inf')
    max_total_error=0.0
    for i in range(steps):
        t=(i+.5)*dt
        H,U,W,h=values(t)
        min_part=min(min_part,U); min_rest=min(min_rest,W)
        max_total_error=max(max_total_error,abs(H-3.5))
        if h>0:
            positive+=1; plus+=h*dt
        elif h<0:
            negative+=1; minus+=h*dt
    return {'steps':steps,'positive_fraction':positive/steps,
            'negative_fraction':negative/steps,
            'positive_exchange':plus,'negative_exchange':minus,
            'sum_exchange':plus+minus,
            'exact_positive_exchange':3*math.sqrt(3)/4,
            'min_part':min_part,'min_rest':min_rest,
            'max_total_error':max_total_error}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--steps',nargs='+',type=int,default=[256,1024,4096])
    args=parser.parse_args()
    print(json.dumps([midpoint_summary(n) for n in args.steps],indent=2))


if __name__=='__main__': main()
