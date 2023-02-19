x = []
size = int(input("enter size :"))
print("enter elemenr :")
for i in range(size):
    val = int(input(""))
    x.append(val)
print("list is = ",x)
print("1.append value")
print("2.remove value")

ch = input("enter task : ")
if ch=='1':
    index = int(input("enter value : "))
    value = int(input("enter value  : "))
    x.insert(index-1,value)
    print("list after insert value = ",x)
elif ch=='2':
    count = 0
    val1 = int(input("enter value : "))
    x.remove(val1)
print("list after remove element = ",x)
               
               
