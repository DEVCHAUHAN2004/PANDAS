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

# Merge DataFrames
df_merged_inner = pd.merge(
    df_customers,
    df_orders,
    on="CustomerID",
    how="inner"
)

print(df_merged_inner)
#    CustomerID    Name  OrderAmount
# 0           1  Ramesh          250
# 1           2  Suresh          450

df_merged_left = pd.merge(
    df_customers,
    df_orders,
    on="CustomerID",
    how="left"
)

print(df_merged_left)
#    CustomerID     Name  OrderAmount
# 0           1   Ramesh        250.0
# 1           2   Suresh        450.0
# 2           3  Kalpesh          NaN