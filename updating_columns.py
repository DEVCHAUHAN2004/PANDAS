import pandas as pd

data = {
  "Name":['A','B','C','D','E','F'],
  "Age":[28,67,54,23,12,45],
  "Salary":[10000,20000,45000,67000,62000,98000],
  "Score":[92,93,88,87,76,86]
}
df = pd.DataFrame(data)
# print(df)

df.loc[0,'Salary'] = 25000
print(df)
#   Name  Age  Salary  Score
# 0    A   28   25000     92
# 1    B   67   20000     93
# 2    C   54   45000     88
# 3    D   23   67000     87
# 4    E   12   62000     76
# 5    F   45   98000     86

df.loc[1,'Name'] = 'devil'
print(df)
#     Name  Age  Salary  Score
# 0      A   28   25000     92
# 1  devil   67   20000     93
# 2      C   54   45000     88
# 3      D   23   67000     87
# 4      E   12   62000     76
# 5      F   45   98000     86

df['Salary'] = df['Salary'] * 1.05
print(df)
#     Name  Age    Salary  Score
# 0      A   28   26250.0     92
# 1  devil   67   21000.0     93
# 2      C   54   47250.0     88
# 3      D   23   70350.0     87
# 4      E   12   65100.0     76
# 5      F   45  102900.0     86