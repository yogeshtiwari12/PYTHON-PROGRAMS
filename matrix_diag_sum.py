matrix = []
sum1 = 0
row = int(input("enter row : "))
col = int(input("enter col  : "))
for i in range(row):
    a = []
    for j in range(col):
        val = int(input())
        a.append(val)
    matrix.append(a)
    print()
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end  = "  ")
    print()
for i in range(row):
    for j in range(col):
        if(a[i]==a[j]):
            sum1 += matrix[i][j]
print(sum1)
