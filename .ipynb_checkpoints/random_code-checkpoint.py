import scipy.stats as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)
data1 = pd.DataFrame({
    "group": ["A"] * 50 + ["B"] * 50,
    "values": np.random.normal(loc=50, scale=10, size=100)
})

# Extract data for each group
group_a = data1[data1['group'] == 'A']['values']
group_b = data1[data1['group'] == 'B']['values']

# Plot histogram
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(group_a, bins=10, alpha=0.7, label='Group A')
plt.hist(group_b, bins=10, alpha=0.7, label='Group B')
plt.title('Histogram')
plt.legend()
