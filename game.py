import random
x = int(input("enter num = "))
number = random.randint(10,15)
i=1
while(i<5):
      val = int(input("enter num : "))
      if(val==number):
        print("you win the game in range(10,15)")
        break

      else:
        i+=1
      if not i<3:
           print("you lost game :number is = ",number)
