
start = int(input("enter start range : "))

end  = int(input("enter start range : "))
print()
for i in range(start,end+1):
    fact = 1
    c = i
    for j in range(1,i+1):
        fact *= j
    print("factorial of ",c,"is =",fact) 