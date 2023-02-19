a  = []
size = int(input("enter size = "))
print("enter elelment ")
for i in range(size):
  val = int(input(""))
  a.append(val)
print("list is = ",a)

index = int(input("enter index = "))
value = int(input("enter value = "))
a.insert(index-1,value)
print("list is = ",a)
