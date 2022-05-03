import pandas as pd

df=pd.read_csv("data-un.csv")
df=df.transpose()
print (df)

df.to_excel("Data.xlsx")
df.to_csv("data.csv")