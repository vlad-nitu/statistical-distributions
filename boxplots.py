import matplotlib.pyplot as plt
import numpy as np


# Creating dataset
np.random.seed(10)
data1 = np.random.geometric(p = 0.3, size = 1000)
data2 = np.random.exponential(size  = 1000, scale = 2)
data3 = np.random.uniform(-2, 2, 100)
data4 = np.random.standard_t(df = 3, size = 1000)
data5 = np.random.normal(0, 1, size = 1000)
data6 = np.random.binomial(10, 1/2, size = 1000)
map = {
    'Geo': data1,
    'Exp': data2,
    'U': data3,
    'T-distr': data4,
    'N(0,1)': data5,
    'Bin': data6
}
fig, ax = plt.subplots()
ax.boxplot(map.values())
ax.set_xticklabels(map.keys())

#
plt.ylim(-5, 15)

# show plot
plt.show()




