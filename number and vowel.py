a = input("enter str = ")
count = 0
count2 = 0
for i in range(len(a)):
     if(a[i]=='a'or a[i]=='e'or a[i]=='i'or a[i]=='o' or a[i]== 'u'):
           count += 1
     elif(a[i]>='1' and a[i]<='9'):
            count2 +=1

print("vowel are = ",count)
print("vowel are = ",count2)
