import pandas as pd

# Customer DataFrame
df_customers = pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "Name": ["Ramesh", "Suresh", "Kalpesh"]
})

# Orders DataFrame
df_orders = pd.DataFrame({
    "CustomerID": [1, 2, 4],
    "OrderAmount": [250, 450, 350]
})

df_concat = pd.concat([df_customers,df_orders],axis = 0,ignore_index=True)
print(df_concat)
#   CustomerID     Name  OrderAmount
# 0           1   Ramesh          NaN
# 1           2   Suresh          NaN
# 2           3  Kalpesh          NaN
# 3           1      NaN        250.0
# 4           2      NaN        450.0
# 5           4      NaN        350.0

df_concat = pd.concat([df_customers,df_orders],axis = 1,ignore_index=True)
print(df_concat)
#    0        1  2    3
# 0  1   Ramesh  1  250
# 1  2   Suresh  2  450
# 2  3  Kalpesh  4  350