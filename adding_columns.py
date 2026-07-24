import pandas as pd

data = {
  "Name":['A','B','C','D','E','F'],
  "Age":[28,67,54,23,12,45],
  "Salary":[10000,20000,45000,67000,62000,98000],
  "Score":[92,93,88,87,76,86]
}
df = pd.DataFrame(data)
# print(df)

df['Bonus'] = df['Salary'] * 0.1
print(df)
#   Name  Age  Salary  Score   Bonus
# 0    A   28   10000     92  1000.0
# 1    B   67   20000     93  2000.0
# 2    C   54   45000     88  4500.0
# 3    D   23   67000     87  6700.0
# 4    E   12   62000     76  6200.0
# 5    F   45   98000     86  9800.0

print("by using insert method")
df.insert(0,'Employee_id',[1,2,3,4,5,6])
print(df)
# by using insert method
#    Employee_id Name  Age  Salary  Score   Bonus
# 0            1    A   28   10000     92  1000.0
# 1            2    B   67   20000     93  2000.0
# 2            3    C   54   45000     88  4500.0
# 3            4    D   23   67000     87  6700.0
# 4            5    E   12   62000     76  6200.0
# 5            6    F   45   98000     86  9800.0



