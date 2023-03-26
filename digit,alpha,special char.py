s = input()
c = c1 = c2 = c3 = c4 = 0
for i in s:
    if i.isalpha():
        c += 1
    elif i.isdigit():
        c1 += 1
    elif i.isspace():
        c2 += 1
    else:
        c3 += 1
print("alphabets = ",c)
print("digits = ",c1)
print("space = ",c2)
print("special char = ",c3)
    
        
