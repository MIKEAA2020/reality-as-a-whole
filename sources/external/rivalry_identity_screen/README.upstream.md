# 2D-Langevin
2D Langevin Inference Using Binocular Rivalry Data
## 1. Data Description

data s005

<img src="images/s005 neural data.png" width="30%">

## 2. pss and brs PCs

PC relationship illustration

<img src="images/13_1.jpg" width="20%">

Data points projected to the 3D PC subspace.

upper: brs data; lower green: brs data; lower blue and red: pss face and object data.

<img src="images/13_2.png" width="100%">

Data points projected on pss PC1 and PC2.

<img src="images/14.png" width="50%">

## 3. Model Initialization

```python

model = Model2D(
        force_model=F_zero,
        p0_model=gaussian(sigma=5.0),
        firing_model=firing_model,
        Np=7,
        Ne=9,
        D=1.0
    )

optimizer = {
        'method': 'adam',
        'n_steps': 200,
        'learning_rate': 1e-1
    }
```

where we use smooth ReLU in the firing model:

<img src="images/15.png" width="30%">

## 4. Inferred Flow Field

### A. From 64 neurons with highest firing rates

<img src="images/16.png" width="60%">

### B. From 64 random neurons

<img src="images/17_1.png" width="50%">

### C. From 32 neurons with highest firing rates

<img src="images/17_2.png" width="50%">

### D. From 64 most selective neurons


<img src="images/19.png" width="60%">

We obtain the joint distribution P(firing_rate, stimulus) and calculate the mutual information

<img src="images/18.png" width="20%">

```python
def mi_rate_binary_class(rate, stim, n_bins=8):
    """
    rate : (n_trials,)  float
    stim : (n_trials,)  0/1
    n_bins: number of bins to discretize rate
    returns
    mi: float
    """
    # 1. discretize rate
    bins = np.quantile(rate, np.linspace(0, 1, n_bins+1))
    # ensure min and max values include boundaries
    bins[0] -= 1e-6
    bins[-1] += 1e-6
    rate_d = np.digitize(rate, bins) - 1   # bins: 0..n_bins-1

    # 2. joint distribution P(r,s)
    joint = np.histogram2d(rate_d, stim, bins=[n_bins, 2])[0]
    joint = joint / joint.sum()            # normalize

    # 3. marginal distributions
    p_r = joint.sum(axis=1)
    p_s = joint.sum(axis=0)

    # 4. mutual information
    mi = 0.0
    for r in range(n_bins):
        for s in range(2):
            if joint[r, s] > 0:
                mi += joint[r, s] * np.log(joint[r, s] / (p_r[r] * p_s[s]))
    return mi / np.log(2)   # convert to bits
```

### Remark: The inferred flow field depends on choice of neurons.

## 5. Posterior Probability Evolution

### A. 64 Highest-firing Neurons in brs

<img src="images/20_1.gif" width="20%"><img src="images/20_2.gif" width="20%"><img src="images/20_3.gif" width="20%">

#### Remark: the probability bump splits in to two sometimes.

### B. 50 Highest-firing Neurons in pss face trials

<img src="images/21_1.gif" width="20%"><img src="images/21_2.gif" width="20%">

#### Remark: Flash sometimes happens in the last frame, sometimes also happens in the middle of the trial.

## 6. Generate Synthetic Data

We take the last iteration of our inferred model, generate one latent trajectory and spike data, get posterior probability from the model and spike data, and finally compare the probability evolution with latent trajectory, which is the ground truth.

For example, we can focus on these snapshots taken aroud 0.1s.

<img src="images/23_1.png" width="50%">

The ground truth trajectory is:

<img src="images/23_2.png" width="30%">

where we can see that the upper probability bump is the correct one.

### Remark: Generated data still show split but no flash. One of the split bumps account for the gound truth.

## 7. Fit {F, f} at the Same Time

64 highest-firing neurons from probe 1:

<img src="images/24_1.png" width="30%"><img src="images/24_2.png" width="50%">

### Remark: Learning F and f at the same time can lead to point-like or ramp tuning functions. Vortices vanish in F.

## 8. New Data Attempts

### s003 data trials

### A. Flow Fields in brs and brn Trials

<img src="images/25.png" width="50%">

### B. PCA in pss trials

<img src="images/26_1.png" width="30%">

#### Remark: Face trials and object trials are no longer separated. It's probably worth checking the trial labels.

### C. Flow Fields in pss Trials

<img src="images/26_2.png" width="50%">

### D. Summary of Variance on pss PC1 and PC2

<img src="images/27.png" width="70%">

## 9. Future Directions

### A. Using ground truth labels in the brn data, check if the posterior probability transitions between vortices correspond to transitions between face and object representations.

### B. By looking at the log likelihood's evolution in different iterations from the test data set, determine learning iterations and which model to choose.

### C. Using Hessian matrix to determine certainties in the flow field.

### D. Applying the inferred framework to more data sets from binocular rivalry task.
