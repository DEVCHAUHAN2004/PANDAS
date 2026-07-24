import pandas as pd

data = {
  "Name":['A','None','C','D','E','F'],
  "Age":[28,None,54,23,12,45],
  "Salary":[10000,None,45000,67000,62000,98000],
  "Score":[92,None,88,87,76,86]
}
df = pd.DataFrame(data)
# print(df)

print(df.isnull())
#     Name    Age  Salary  Score
# 0  False  False   False  False
# 1  False   True    True   True
# 2  False  False   False  False
# 3  False  False   False  False
# 4  False  False   False  False
# 5  False  False   False  False

print(df.isnull().sum())
# Name      0
# Age       1
# Salary    1
# Score     1
# dtype: int64
