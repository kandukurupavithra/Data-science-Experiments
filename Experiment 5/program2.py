import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.DataFrame({
    'category': ['A', 'B', 'C'],
    'values': [10, 20, 15]
})
sns.barplot(x='category', y='values', data=df)
plt.title("Bar Plot")
plt.show()