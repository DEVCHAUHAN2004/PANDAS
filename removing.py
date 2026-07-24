import pandas as pd

data = {
  "Name":['A','B','C','D','E','F'],
  "Age":[28,67,54,23,12,45],
  "Salary":[10000,20000,45000,67000,62000,98000],
  "Score":[92,93,88,87,76,86]
}
df = pd.DataFrame(data)
# print(df)

df.drop(columns=['Score','Age'],inplace=True)
print(df)
#   Name  Salary
# 0    A   10000
# 1    B   20000
# 2    C   45000
# 3    D   67000
# 4    E   62000
# 5    F   98000

