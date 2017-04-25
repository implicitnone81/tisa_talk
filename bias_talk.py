#!/usr/bin/env python

# So notebook will show plot in browser
get_ipython().magic('matplotlib inline')

# Import the necessary modules.
import numpy as np
import matplotlib.pyplot as plt

# p is probability of success in the binomial distribution
p = 0.05
sample_sizes = [10, 100, 1000, 10000, 100000]
replicates = 1000
# List container for total biases.
biases = []

for n in sample_sizes:

    bias = np.empty(replicates)
    for i in range(replicates):

        true_sample = np.random.normal(size=n)
        negative_values = true_sample<0
        missing = np.random.binomial(1, p, n).astype(bool)
        observed_sample = true_sample[~(negative_values & missing)]
        
        # Without bias.
        #observed_sample = true_sample

        bias[i] = observed_sample.mean()

    biases.append(bias)

# Select a style sheet for plot.
#plt.style.use('fivethirtyeight')
plt.style.use('ggplot')

fig, ax = plt.subplots( nrows=1, ncols=1, figsize=(12,10) ) 

# Create object "violins". This is so we can change the color in the loop.
violins = ax.violinplot(biases, showmeans=False, showextrema=False, showmedians=False)
for i, pc in enumerate(violins['bodies']):
    # Grab the color in the cycle "color". This is a change in Python3.5.
    color = list(plt.rcParams['axes.prop_cycle'])[i]['color']
    pc.set_facecolor(color)
    pc.set_edgecolor('k')

# Label the first bin an empty string to it skips the origin.
sample_sizes.insert(0,'')
ax.set_xticklabels(sample_sizes)

ax.set_title( 'Introduce Bias in a Standard Normal Distribution' )
ax.set_ylabel( 'Bias' )
ax.set_xlabel( 'Sample Size' )
plt.show()

