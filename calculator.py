print("\n\n")
print("*********************WELCOME IN CALCULATOR************************")

print("Addition : 1")
print("subtraction : 2")
print("Multiplicat : 3")
print("Divide : 4")
print("Power : 5")
print("\n")
print("***************CALCULATOR******************")

x = int(input("enter first num : "))
ch =(input("enter operator   : "))
y = int(input("enter second num  : "))

print("\n\n")
print("*******************************************")

if(ch=='1'):
    print("addition  = ",x+y)
elif(ch=='2'):
    print("subtraction = ",x-y)
elif(ch=='3'):
    print("multiplicaton  = ",x*y)
elif(ch=='4'):
    print("divide  = ",x/y)
elif(ch=='5'):
    print("power = ",x**y)
else:
    print("ENTER VALID OPERATOR ")

