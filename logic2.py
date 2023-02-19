a = []
count = 0
size = int(input("enter list size = "))
for i in range(size):
    val = int(input())
    a.append(val)
max1 = max(a)
for i in range(1,max1+1):
    if i not in a:
       print(i)