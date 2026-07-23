import pandas as pd

data = {
  "Name":['A','B','C','D','E','F'],
  "Age":[28,67,54,23,12,45],
  "Salary":[10000,20000,45000,67000,62000,98000],
  "Score":[92,93,88,87,76,86]
}
df = pd.DataFrame(data)
print(df)

print(df["Name"])
# 0    A
# 1    B
# 2    C
# 3    D
# 4    E
# 5    F

print(df[["Name","Age"]])
#   Name  Age
# 0    A   28
# 1    B   67
# 2    C   54
# 3    D   23
# 4    E   12
# 5    F   45

high_salary = df[df['Salary'] > 30000]
print(high_salary)
#   Name  Age  Salary  Score
# 2    C   54   45000     88
# 3    D   23   67000     87
# 4    E   12   62000     76
# 5    F   45   98000     86

x = df[(df['Salary'] >40000) & (df['Age'] > 20)]
print(x)
#   Name  Age  Salary  Score
# 2    C   54   45000     88
# 3    D   23   67000     87
# 5    F   45   98000     86
