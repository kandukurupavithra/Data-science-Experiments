import pandas as pd
url = "https://github.com/mwaskom/seaborn-data/raw/master/iris.csv"
df = pd.read_csv(url)
print("First five rows of the dataset")
print(df.head())
print("\nDataset Information")
print(df.info())
print("\nNumber of rows and columns")
print(df.shape)