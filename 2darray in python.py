matrix = []
row = int(input("enter row : "))
col = int(input("enter col  : "))
for i in range(row):
    a = []
    for j in range(col):
        val = int(input())
        a.append(val)
    matrix.append(a)
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end = "   ")
    print()
