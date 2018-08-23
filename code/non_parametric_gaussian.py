import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
plt.style.use('fivethirtyeight')


# Fill in some random parameters
mean = np.array([2.3, -1.2])
cov = np.array([[1.3, 0.2], [0.2, 0.4]])

# How much samples do you want to see?
num_samples_scatter = 100
num_samples_histogram = 10**6

# Draw samples for the 2d case
mvn = multivariate_normal(mean, cov)
samples_scatter = mvn.rvs(size=num_samples_scatter)

# All code below is pyplot magic
f, axarr = plt.subplots(1, 2)
axarr[0].scatter(samples_scatter[:, 0], samples_scatter[:, 1], label='2D mvn', c='b')
axarr[0].scatter(np.zeros_like(samples_scatter[:, 0]), samples_scatter[:, 1], label='Second axis of 2D mvn', c='k')
axarr[0].set_xlim([-5, 5])
axarr[0].set_ylim([-5, 5])
axarr[0].set_xlabel('First axis')
axarr[0].set_ylabel('Second axis')
axarr[0].legend()

axarr[1].hist(mvn.rvs(size=num_samples_histogram)[:, 1], density=True, bins=int(np.sqrt(num_samples_histogram)))
axarr[1].set_xlabel('Second axis of scatter')
plt.show()
plt.waitforbuttonpress()
