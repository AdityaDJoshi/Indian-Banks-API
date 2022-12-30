import datetime
from collections import Counter
import os
from numpy import record
import pandas as pd
from IFSC_class import *

a = Student("adi", "07/25/94", "123456789")
print(a.age_calculator())
df = pd.read_csv(os.path.join("static", "ifsc.csv"))
# print(df)
a = df['bank_name'].unique()
# print(len(a))
print(df.iloc[:3])
print(df.iloc[-3:])
stats_df = pd.read_csv(os.path.join("static", "statistics.csv"))
print(len(stats_df))
# b = df['bank_name']
# d = Counter(b)
# print(d)
# print(d.most_common(10))
# l = d.most_common(10)

# for a, b in l:
#     print(a, b)
# print({a: b for a, b in l})

# specifying datatypes

req = df.loc[df['ifsc'] == "AAAA0065010"]
# req = request.json
# print(req)
# print(list(req))
print(req.to_dict(orient='records'))


# def add(x: float, y: float) -> float:
#     if not isinstance(x, float):
#         raise TypeError("x and y variables not of type float")


# print(datetime.datetime.now())

# df = pd.DataFrame([
#     [datetime.datetime.now(), "ABHY0065015", ],
# ],
#     columns=['Timestamp', 'IFSC', ]
# )
# output_path = os.path.join("static", "statistics.csv")
# df.to_csv(output_path, mode='a', header=not os.path.exists(
#     output_path), index=False)

# # Add columns here
# print(df)

# data = pd.Series(['Yes', 'Yes', 'No', 'No'])
# df.insert(3, 'Sold in Bulk2?', data)
# print(df)
