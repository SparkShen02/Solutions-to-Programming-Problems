import random
def factorial(num):
    result=1
    while num>0:
        result=result*num
        num-=1
    return result
def combination(num,one):
    return int(factorial(num)/(factorial(num-one)*factorial(one)))
for i in range(int(input())):
    result=[]
    num,one=map(int,input().split(" "))
    for x in range(combination(num,one)):
        test=[]
        for a in range(num):
            test.append(0)
        while True:
            already=[]
            test1=test[:]
            for y in range(one):
                ran=random.randint(0,num-1)
                while(ran in already):
                    ran=random.randint(0,num-1)
                test1[ran]=1
                already.append(ran)
            if(test1 not in result):
                test=test1[:]
                break
        result.append(test)
    for l in range(len(result)):
            for leng in range(len(result[l])):
                result[l][leng]=str(result[l][leng])
            result[l]="".join(result[l])
    for l in range(len(result)):
        result[l]=int(result[l],2)
    result.sort()
    result.reverse()
    for l in range(len(result)):
        result[l]=bin(result[l])[2:]
    print("The bit patterns are")
    for ch in result:
        while len(ch)<num:
            ch="0"+ch
        print(ch)
    print()
    
