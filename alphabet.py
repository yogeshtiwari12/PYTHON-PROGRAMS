n = int(input("enter num :"))
for i in range(65,65+n):
    for j in range(65,i):
        print(chr(j),end = " ")
    print()
