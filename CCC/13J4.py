minute=int(input())
arr=[]
for i in range(int(input())):
    each=int(input())
    arr.append(each)
arr.sort()
sum=0
num=0
for a in arr:
    sum+=a
    if(sum<minute):
        num+=1
    else:
        print(num)
        break

