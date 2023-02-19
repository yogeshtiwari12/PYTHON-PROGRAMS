for n in range(1001):
   sum = 0
   c = n
   while(n>0):
         r = n%10
         sum += (r*r*r)
         n= n//10
   if (c==sum):
      print(c)
