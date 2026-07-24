import pandas as pd

data = {
    "Name": ['A','B','C','D','E','F'],
    "Age": [28, 39, 54, 23, 12, 45],
    "Salary": [10000, 20000, 45000, 67000, 62000, 98000],
    "Score": [92, 93, 88, 87, 76, 86]
}

df = pd.DataFrame(data)

avg = df['Score'].mean()
print(avg)
# 87

# max/mean/min/sum