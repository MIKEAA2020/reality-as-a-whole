#!/usr/bin/env python3
"""Elementary exact controls for proposed BC-MBWI interpretation gates.

Uses standard interference and remote-state-steering facts. The biased ensemble
is a stipulated hypothetical GLOBAL operational rule, not ordinary quantum
mechanics and not a claim about the author's unspecified model or consciousness.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def mix(p, plus, minus):
    return tuple(tuple(p*plus[i][j]+(1-p)*minus[i][j] for j in range(2))
                 for i in range(2))


def main():
    half=F(1,2)
    zplus=((F(1),F(0)),(F(0),F(0)))
    zminus=((F(0),F(0)),(F(0),F(1)))
    xplus=((half,half),(half,half))
    xminus=((half,-half),(-half,half))
    maximally_mixed=((half,F(0)),(F(0),half))
    assert mix(half,zplus,zminus)==mix(half,xplus,xminus)==maximally_mixed

    # Prepare |+> then test X: coherent result is certain. Insert and discard
    # a projective Z record: off-diagonals are removed, X+ becomes 1/2.
    coherent=F(1)
    dephased=half
    assert coherent != dephased

    rows=[]
    for eps in (F(-1,2),F(-1,4),F(-1,10),F(0),F(1,10),F(1,4),F(1,2)):
        p=half+eps
        assert 0<=p<=1
        z=mix(p,zplus,zminus)
        x=mix(p,xplus,xminus)
        p0_z=z[0][0]
        p0_x=x[0][0]
        assert p0_z==half+eps and p0_x==half and p0_z-p0_x==eps
        assert z[0][0]+z[1][1]==x[0][0]+x[1][1]==1
        rows.append({'epsilon':str(eps),'bob_z0_after_z_setting':str(p0_z),
                     'bob_z0_after_x_setting':str(p0_x),'difference':str(p0_z-p0_x)})
    out={'status':'passed','ordinary_unselected_bob_state':'I/2 in both bases',
         'hypothetical_biased_remote_ensemble':rows,
         'interference_control':{'initial_state':'|+>','final_X_plus_coherent':str(coherent),
                                  'final_X_plus_after_unread_Z_record':str(dephased)},
         'scope':'Exact finite qubit arithmetic, not an experiment or a complete theory. Signalling requires controllable spacelike choices, actual altered objective ensemble weights, conditional remote states as stipulated, and accessible Bob records. Subjective conditioning, ordinary postselection with communication, and unspecified BC-MBWI are not shown to signal. The unread record control does not refute all blockworld or definite-event ontologies.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__': main()
