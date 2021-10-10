nums=int(input())
for i in range(nums):
    numberStr=input()
    num=numberStr
    number=int(numberStr)
    print(number)
    for a in range(len(numberStr)-2):
        delete=numberStr[-1]
        numberStr=numberStr[0:-1]
        number=int(numberStr)
        number-=int(delete)
        numberStr=str(number)
        print(number)
    if(number%11==0):
        print("The number "+num+" is divisible by 11.")
    else:
        print("The number "+num+" is not divisible by 11.")
    print()
