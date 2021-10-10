import math
nums=int(input())
for i in range(nums):
    num=int(input())
    x=2
    sumOfDivisors=1
    while (x<math.sqrt(num)):
        if (num%x==0):
            sumOfDivisors+=x+num/x
        x+=1
    if (x==math.sqrt(num)):
        sumOfDivisors+=1
    if (sumOfDivisors<num):
        print(str(num)+" is a deficient number.")
    if (sumOfDivisors==num):
        print(str(num)+" is a perfect number.")
    if (sumOfDivisors>num):
        print(str(num)+" is an abundant number.")
    


    
