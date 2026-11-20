import unittest
import numpy as np
from music_appraisal_feasibility import phase_dispersion, features, validate, FS

class FeasibilityTests(unittest.TestCase):
    def test_constant_phase_offset(self):
        t=np.arange(70*FS)/FS
        p=np.array([t,t+1,t,t+2,t,t+3])
        self.assertAlmostEqual(phase_dispersion(p),0,places=12)
    def test_varying_offset(self):
        t=np.arange(70*FS)/FS
        p=np.array([0*t,2*np.pi*t,0*t,2*np.pi*t,0*t,2*np.pi*t])
        self.assertAlmostEqual(phase_dispersion(p),1,places=12)
    def test_reference_changes_features(self):
        t=np.arange(10240)/FS
        trial=np.array([np.sin(2*np.pi*10*t+i*.23)+(.2+i*.07)*np.sin(2*np.pi*20*t+i) for i in range(14)]).T
        a=features(trial,list(range(6)),True); b=features(trial,list(range(6)),False)
        self.assertGreater(np.linalg.norm(np.array(a)-b),.01)
    def test_bad_schema(self):
        with self.assertRaises(ValueError): validate(np.zeros((4,14,30)),np.repeat([1,3,5],10),list(map(str,range(14))),128)
    def test_balanced_baseline(self):
        y=np.repeat([1,3,5],10)
        self.assertAlmostEqual(np.abs(y-3).mean(),4/3)
        self.assertAlmostEqual(np.sqrt(np.square(y-3).mean()),np.sqrt(8/3))
if __name__=='__main__': unittest.main()
