import pandas as pd

data = {
    "Name": ['A','B','C','D','E','F'],
    "Age": [28, 39, 54, 23, 12, 45],
    "Salary": [10000, 20000, 45000, 67000, 62000, 98000],
    "Score": [92, 93, 88, 87, 76, 86]
}

df = pd.DataFrame(data)

df.sort_values(by='Age',ascending=True,inplace=True)
print(df)
#   Name  Age  Salary  Score
# 4    E   12   62000     76
# 3    D   23   67000     87
# 0    A   28   10000     92
# 1    B   39   20000     93
# 5    F   45   98000     86
# 2    C   54   45000     88

df.sort_values(by=['Age','Salary'],ascending=[True,False],inplace=True)
print(df)
#   Name  Age  Salary  Score
# 4    E   12   62000     76
# 3    D   23   67000     87
# 0    A   28   10000     92
# 1    B   39   20000     93
# 5    F   45   98000     86
# 2    C   54   45000     88
