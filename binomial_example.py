#!/usr/bin/env python

# So notebook will show plot in browser
get_ipython().magic('matplotlib inline')

# Import the necessary modules.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# Declare variables for three binomial distributions
# Probabilty of success/failure
p = [0.5, 0.7, 0.5]
# Number of trials
n_bi = [20, 20, 40]
# Number of tests
tests = 100

# Call the figure artist.
fig, ax = plt.subplots( nrows=1, ncols=1, figsize=(12,9))

# Use some preloaded style sheets to make plot look nicer.
plt.style.use( 'ggplot' )

# Create loop to generate plot with three samples.
for i in range(len(p)):
    
    sample = np.random.binomial( n_bi[i], p[i], tests )
    
    mu = sample.mean()
    sigma = sample.std()
    
    num_bins = 25
    # Creates a histogram of sample. Set alpha=0 to hide bar plot.
    n, bins, patches = ax.hist( sample, num_bins, normed=1, alpha=0.0  )
    y = mlab.normpdf( bins, mu, sigma)
    ax.plot( bins, y, marker='o', linestyle='' )

ax.set_ylim( 0, 0.25 )
ax.set_xlim( 0, 40.0 )
plt.show()

