import pandas as pd

df = pd.read_csv('SampleSuperstore.xlsx - Orders.csv', encoding='latin1')

print(df.info())

# <class 'pandas.DataFrame'>
# RangeIndex: 9994 entries, 0 to 9993
# Data columns (total 21 columns):
#  #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   Row ID         9994 non-null   int64  
#  1   Order ID       9994 non-null   str    
#  2   Order Date     9994 non-null   str    
#  3   Ship Date      9994 non-null   str    
#  4   Ship Mode      9994 non-null   str    
#  5   Customer ID    9994 non-null   str    
#  6   Customer Name  9994 non-null   str    
#  7   Segment        9994 non-null   str    
#  8   Country        9994 non-null   str    
#  9   City           9994 non-null   str    
#  10  State          9994 non-null   str    
#  11  Postal Code    9994 non-null   int64  
#  12  Region         9994 non-null   str    
#  13  Product ID     9994 non-null   str    
#  14  Category       9994 non-null   str    
#  15  Sub-Category   9994 non-null   str    
#  16  Product Name   9994 non-null   str    
#  17  Sales          9994 non-null   float64
#  18  Quantity       9994 non-null   int64  
#  19  Discount       9994 non-null   float64
#  20  Profit         9994 non-null   float64
# dtypes: float64(3), int64(3), str(15)
# memory usage: 1.6 MB
# None


import pandas as pd

data = {
  "Name":['A','B','C'],
  "Age":[10,20,30],
  "City":['Delhi','Noida','Shamli']
}
df = pd.DataFrame(data)
print(df.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 3 entries, 0 to 2
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Name    3 non-null      str  
#  1   Age     3 non-null      int64
#  2   City    3 non-null      str  
# dtypes: int64(1), str(2)
# memory usage: 204.0 bytes
# None