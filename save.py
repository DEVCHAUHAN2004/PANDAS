import pandas as pd

data = {
  "Name":['A','B','C'],
  "Age":[10,20,30],
  "City":['Delhi','Noida','Shamli']
}
df = pd.DataFrame(data)
print(df)
#   Name  Age    City
# 0    A   10   Delhi
# 1    B   20   Noida
# 2    C   30  Shamli

# df.to_csv('output.csv',index = False)

# df.to_excel("devil.xlsx")

# df.to_json('output.json',index = False)
