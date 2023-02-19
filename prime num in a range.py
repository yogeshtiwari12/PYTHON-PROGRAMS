x = int(input())
y = int(input())
for i in range(x,y+1):
    for j in range(2,i+1):
        if(i%j==0):
            break
    if(i==j):
            print(j)
            