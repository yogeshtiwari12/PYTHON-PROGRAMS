a  = []
size = int(input("enter size = "))
print("enter elelment ")
for i in range(size):
  val = int(input(""))
  a.append(val)
print("list is = ",a)

flag = 0
value = int(input("enter value = "))
for i in range(size):
    if(a[i]==value):
        flag =1
        break

if(flag ==0):
    print("elelment mot found")
else:

   a.remove(value)
print("list is = ",a)