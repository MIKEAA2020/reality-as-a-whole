"""Repeated Lüders window instrument on the autonomous two-memory model.

The checkpoint instrument is externally scheduled in scalar time; its bits
are not exact crossing counts. The exact continuum slice transport and the
finite-window instability argument are discussed in the accompanying note.
"""
import itertools
import unittest
import numpy as np
from verification.zero_autonomous_two_window_records_test import make_model, initial
from verification.zero_two_window_finite_record_clock_test import root_data, sqrt_effect

TIMES = (30., 40., 50.)
END = 100.


def history_branches(model, vals, V, state, times=TIMES, basis='momentum'):
    """Return unnormalized final branch vectors indexed by ordered click bits."""
    n = len(model[0]); omega = np.sqrt(vals); E = model[2][1]
    ks = [np.kron(np.eye(8), sqrt_effect(np.eye(n)-E)),
          np.kron(np.eye(8), sqrt_effect(E))]
    if basis == 'spectral':
        v = V.conj().T @ state
        operators = [V.conj().T @ k @ V for k in ks]
        def advance(x, dt): return np.exp(1j*omega*dt)*x
    elif basis == 'momentum':
        v = state
        operators = ks
        def advance(x, dt): return V @ (np.exp(1j*omega*dt) * (V.conj().T @ x))
    else:
        raise ValueError(basis)
    branches = {(): v}; last = 0.
    for t in times:
        result = {}
        for hist, x in branches.items():
            before = advance(x, t-last)
            for b in (0, 1):
                result[hist+(b,)] = operators[b] @ before
        branches = result; last = t
    return {hist: advance(x, END-last) for hist, x in branches.items()}


def final_table(branches, n, V=None):
    table = np.zeros((2,)*len(next(iter(branches))) + (2,2))
    for hist, state in branches.items():
        if V is not None: state = V @ state
        p = abs(state.reshape(2,2,2,n))**2
        table[hist] = p.sum(axis=(0,3))
    return table


def full_table(model, state=None, times=TIMES, basis='momentum'):
    n = len(model[0]); v = initial(model).ravel() if state is None else state
    tables = []
    for h in (0,1):
        vals, V = root_data(model,h)
        branches = history_branches(model, vals, V, v, times, basis)
        tables.append(final_table(branches, n, V if basis == 'spectral' else None))
    return sum(tables)/2


def first_masses(table):
    return np.array([table[1,:,:].sum(),table[0,1,:].sum(),
                     table[0,0,1].sum(),table[0,0,0].sum()])


class TwoWindowRecordedHistoriesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = make_model(24)
        cls.table = full_table(cls.model)

    def test_complete_histories_and_first_hit_coarse_grain(self):
        self.assertAlmostEqual(self.table.sum(), 1, places=11)
        self.assertTrue(np.all(self.table >= 0))
        first = first_masses(self.table)
        self.assertAlmostEqual(first.sum(),1,places=11)
        self.assertGreater(first[-1], .1)
        self.assertGreater(sum(self.table[h].sum() for h in itertools.product((0,1),repeat=3)
                               if sum(h)>=2), .01)
        # First hit with discarded later results matches stopping immediately:
        n=len(self.model[0]); state=initial(self.model).ravel(); accum=[]
        for h in (0,1):
            vals,V=root_data(self.model,h); omega=np.sqrt(vals)
            def u(x,dt): return V@(np.exp(1j*omega*dt)*(V.conj().T@x))
            E=self.model[2][1];K=[np.kron(np.eye(8),sqrt_effect(np.eye(n)-E)),np.kron(np.eye(8),sqrt_effect(E))]
            x=state; prev=0; masses=[]
            for t in TIMES:
                x=u(x,t-prev);y=K[1]@x;masses.append(np.vdot(y,y).real);x=K[0]@x;prev=t
            masses.append(np.vdot(x,x).real);accum.append(masses)
        np.testing.assert_allclose(first, np.mean(accum,axis=0), atol=2e-12)

    def test_fresh_bit_dilation_is_unitary(self):
        n = len(self.model[0]); E = self.model[2][1]
        k0 = sqrt_effect(np.eye(n)-E); k1 = sqrt_effect(E)
        W = np.block([[k0, -k1], [k1, k0]])
        self.assertLess(np.linalg.norm(W.conj().T@W-np.eye(2*n)), 1e-12)
        self.assertLess(np.linalg.norm(k0@k0+k1@k1-np.eye(n)), 1e-12)

    def test_reference_n80_history_probabilities(self):
        table = full_table(make_model(80))
        np.testing.assert_allclose(first_masses(table),
                                   [.35052924, .10918684, .01200832, .52827561],
                                   atol=8e-9)
        self.assertAlmostEqual(sum(table[h].sum() for h in itertools.product((0,1),repeat=3)
                                   if sum(h)>=2), .06513749782317707, places=10)

    def test_all_spectral_branches_and_final_states_transport(self):
        n=len(self.model[0]);v=initial(self.model).ravel()
        for h in (0,1):
            vals,V=root_data(self.model,h)
            a=history_branches(self.model,vals,V,v)
            b=history_branches(self.model,vals,V,v,basis='spectral')
            for hist in a:
                self.assertLess(np.linalg.norm(a[hist]-V@b[hist]),1e-12)
            np.testing.assert_allclose(final_table(a,n),final_table(b,n,V),atol=1e-13)

    def test_intervention_not_just_a_relabeling(self):
        # Compare a readout at 40 with and without the preceding measurement.
        only40 = full_table(self.model,times=(40.,)).sum(axis=(1,2))
        after30 = self.table.sum(axis=(0,2,3,4))
        self.assertGreater(abs(only40[1]-after30[1]), .002)
        with_records = self.table.sum(axis=(0,1,2))
        no_probe=[];n=len(self.model[0]);v=initial(self.model).ravel()
        for h in (0,1):
            vals,V=root_data(self.model,h)
            x=V@(np.exp(1j*np.sqrt(vals)*END)*(V.conj().T@v))
            no_probe.append((abs(x.reshape(2,2,2,n))**2).sum(axis=(0,3)))
        self.assertGreater(np.max(abs(with_records-sum(no_probe)/2)),.001)

    def test_receding_and_grid_controls(self):
        back = full_table(make_model(24,x0=15.))
        self.assertLess(1-back[0,0,0].sum(), .01)
        refined = full_table(make_model(40))
        self.assertLess(np.max(abs(refined-self.table)), .0003)

    def test_bound_complement_coherence_is_retained(self):
        n=len(self.model[0]);v=initial(self.model).ravel();vals,V=root_data(self.model,0)
        out=(vals < 6-1e-10) | (vals > 49/6+1e-10)
        self.assertGreater(np.count_nonzero(out),0)
        pb=V[:,out]@(V[:,out].conj().T@v);q=v-pb
        self.assertGreater(np.linalg.norm(pb),1e-5)
        def outcome(x):
            branches=history_branches(self.model,vals,V,x)
            return final_table(branches,n)[0,0,0].sum()
        full=outcome(v);dephased=outcome(pb)+outcome(q)
        self.assertGreater(abs(full-dephased),1e-6)

if __name__=='__main__': unittest.main()
