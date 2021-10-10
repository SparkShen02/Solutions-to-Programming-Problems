import math
nums=int(input())
for i in range(nums):
    number=int(input())
    factor=[1,number]
    x=2
    while (x<math.sqrt(number)):
        if (number%x==0):
            factor.insert(int(len(factor)/2),x)
            factor.insert(int(len(factor)/2)+1,number/x)
        x+=1
    sum=[]
    sub=[]
    correct=0
#    for a in range(int(len(factor)/2)-1):##0,1,2
#        for x in range(int((len(factor)-2*a)/2)-1):##0,1,2 0,1 0
#            sum.append(factor[x+1]+factor[-x-2])
#        for y in sum[a:]:
#            if(factor[-a-1]-factor[a])==y:
#                correct+=1
#    if(correct!=0):
#        print(str(number)+" is nasty")
#    else:
#        print(str(number)+" is not nasty")
    for x in range(int(len(factor)/2)):
        sum.append(factor[x]+factor[-x-1])
        sub.append(factor[-x-1]-factor[x])
    for i in range(len(sum)):
        for x in range(len(sub)):
            if (sum[i]==sub[x]):
                correct+=1
    if (correct!=0):
        print(str(number)+" is nasty")
    else:
        print(str(number)+" is not nasty")
    
