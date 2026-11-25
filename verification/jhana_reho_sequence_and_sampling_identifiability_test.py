"""Exact toy controls motivated by Yang et al. 7T jhana case study.

No participant fMRI, ratings or code are used. The examples establish only
mathematical possibilities and do not diagnose confounding in the actual data.
"""
from fractions import Fraction as Q
import unittest


def ranks(values):
    # Strictly distinct values in each synthetic series: no ties.
    assert len(set(values))==len(values)
    return [1+sum(other<value for other in values) for value in values]


def kendall_w(voxel_series):
    """Kendall concordance across m rankings of n timepoints, no ties."""
    m=len(voxel_series);n=len(voxel_series[0])
    assert all(len(v)==n for v in voxel_series)
    ranked=[ranks(v) for v in voxel_series]
    sums=[sum(row[k] for row in ranked) for k in range(n)]
    center=Q(m*(n+1),2)
    return Q(12)*sum((Q(x)-center)**2 for x in sums)/Q(m*m*(n**3-n))


class JhanaRehoSequenceAndSamplingTests(unittest.TestCase):
    def test_same_concordance_with_arbitrarily_different_voxel_scales(self):
        # 27 voxels; all time courses have eight distinct observations.
        base=list(range(1,9));voxels=[base[:] for _ in range(18)]+[base[::-1] for _ in range(9)]
        transformed=[[(k+1)*x+50+k*k for x in row] for k,row in enumerate(voxels)]
        self.assertEqual(kendall_w(voxels),Q(1,9))
        self.assertEqual(kendall_w(transformed),Q(1,9))
        self.assertNotEqual(sum(map(sum,voxels)),sum(map(sum,transformed)))
        # ReHo is local rank concordance, not mean BOLD amplitude or energy.
        # These are invented BOLD-like sequences, not observed brain data.

    def test_same_sequence_data_with_two_inequivalent_explanations(self):
        # A perfectly ordered fixed schedule is an explicit example, not the
        # real study's variable stage timings. Both laws predict all of these
        # observations exactly, including run-specific offsets.
        data=[(r,stage,stage,3*stage+2+Q(r,10)) for r in range(27) for stage in range(1,7)]
        for r,stage,elapsed,y in data:
            self.assertEqual(y,3*stage+2+Q(r,10))
            self.assertEqual(y,3*elapsed+2+Q(r,10))
        # At a hypothetical second schedule where stage and elapsed differ,
        # the explanations disagree. This is not a feasible protocol claim.
        stage,elapsed,run=2,5,0
        self.assertNotEqual(3*stage+2+Q(run,10),3*elapsed+2+Q(run,10))

    def test_same_pooled_ratings_leave_components_undetermined(self):
        # Illustrates the stated averaging of three formlessness ratings;
        # does not assume that pooled ReHo itself is a linear average.
        a=(2,5,8);b=(5,5,5)
        self.assertEqual(Q(sum(a),3),Q(sum(b),3))
        self.assertNotEqual(a,b)

    def test_cluster_dependence_can_make_segment_count_misleading(self):
        # 2 independent control runs, each split into 8 equally weighted
        # segments with within-run correlation rho. Equal variances assumed.
        # Exact mean variance equals independent-data variance times 1+7rho.
        rho=Q(3,4);design=1+7*rho;n=16
        neff=Q(n,1)/design
        self.assertEqual(neff,Q(64,25))
        self.assertEqual(design,Q(25,4))
        # This is illustrative; neither correlation nor effective N is
        # estimated for the real 2 control runs.

if __name__=='__main__':unittest.main()
