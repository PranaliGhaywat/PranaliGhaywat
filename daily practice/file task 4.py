

with open(r"D:\Avish\OneDrive\Desktop\tr\file handling\currency_con.txt") as f:
    lines = f.readlines()

print(lines)


dic1 = {}

for i in lines:
    doc = i.split("\t")
    dic1[doc[0]] = doc[1]       

print(dic1,'\n')


amount = int(input("enter the amount:"))
for j in dic1.keys():
    print(j)


print("Choose a currency from above:")
currency = input()
print("your original amount:", amount)
print("your amount is ", amount*float(dic1[currency]), " in ",currency)

