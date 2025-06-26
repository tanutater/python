import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.randn(100)

# Compute histogram by hand
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)

# Find which bin each x falls into
i = np.searchsorted(bins, x)
np.add.at(counts, i, 1)

# Plot manually computed histogram using step
plt.step(bins, counts, where='mid', label='Manual Histogram')

# Plot using built-in histogram for comparison
plt.hist(x, bins, histtype='step', label='plt.hist')

plt.legend()
plt.show()