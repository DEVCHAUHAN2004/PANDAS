import pandas as pd

data = {
    "Name": ['A','B','C','D','E','F'],
    "Age": [28, None, 54, 23, 12, 45],
    "Salary": [10000, 20000, 45000, 67000, 62000, 98000],
    "Score": [92, 93, 88, 87, 76, 86]
}

df = pd.DataFrame(data)

# new_df = df.interpolate(method='linear', axis=0)

# print(new_df)

df['Age'] = df['Age'].interpolate(method='linear')
print(df)
#   Name   Age  Salary  Score
# 0    A  28.0   10000     92
# 1    B  41.0   20000     93
# 2    C  54.0   45000     88
# 3    D  23.0   67000     87
# 4    E  12.0   62000     76
# 5    F  45.0   98000     86

