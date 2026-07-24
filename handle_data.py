import pandas as pd

data = {
  "Name":['A','None','C','D','E','F'],
  "Age":[28,None,54,23,12,45],
  "Salary":[10000,None,45000,67000,62000,98000],
  "Score":[92,None,88,87,76,86]
}
df = pd.DataFrame(data)
# print(df)

print(df.dropna(axis=0,inplace=True))
print(df)
#   Name   Age   Salary  Score
# 0    A  28.0  10000.0   92.0
# 2    C  54.0  45000.0   88.0
# 3    D  23.0  67000.0   87.0
# 4    E  12.0  62000.0   76.0
# 5    F  45.0  98000.0   86.0

print(df.fillna(0,inplace=True))
print(df)
#   Name   Age   Salary  Score
# 0    A  28.0  10000.0   92.0
# 2    C  54.0  45000.0   88.0
# 3    D  23.0  67000.0   87.0
# 4    E  12.0  62000.0   76.0
# 5    F  45.0  98000.0   86.0
