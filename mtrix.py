row = int(input("enter row :"))
col = int(input("enter col :"))
m = []

for i in range(row):
    a = []     
    for j in range(col):
        val = int(input(""))
        a.append(val)
    m.append(a)
  
for i in range(row):
    for j in range(col):
        print(m[i][j],end = " ")
    print()
