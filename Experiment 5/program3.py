import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
data=np.random.rand(1000)
sns.histplot(data,kde=True)
plt.title("Histogram and Density")
plt.show()