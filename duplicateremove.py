x = []
y = []
size = int(input("enter size = "))
print("enter element ")
for i in range(size):
               val = int(input(""))
               x.append(val)
print("list is = ",x)

for a in x:
      if a not in y:
            y.append(a)
x = list(y) 
print("list",y)
