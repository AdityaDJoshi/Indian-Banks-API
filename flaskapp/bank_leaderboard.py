from imports import *

df = pd.read_csv(os.path.join("static", "ifsc.csv"))
# print(df)
b = df['bank_name']
d = Counter(b)

print("#########")
print("Number of unique banks", len(df['bank_name'].unique()))
print("#########")
print("top 10 banks")
# print(d.most_common(10))
print("#########")
print("top 10 banks")
print(d)
print(d.most_common()[-10:][::-1])
