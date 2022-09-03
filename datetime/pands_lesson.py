import pandas as pd
df = pd.read_csv('datetime/pandas.csv')
print(df)
print(df['曜日'].sum("月"))
print(df['金額'].sum())