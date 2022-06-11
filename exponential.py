from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(scale = 2, size=1000), hist=False)

plt.show()