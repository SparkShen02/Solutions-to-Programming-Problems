int(input())
occupied1=[]
occupied2=[]
num=0
for i in range(2):
    parking=list(input())
    for a in range(0,len(parking)):
        if(i==0):
            if(parking[a]=="C"):
                occupied1.append(1)
            else:
                occupied1.append(0)
        if(i==1):
            if(parking[a]=="C"):
                occupied2.append(1)
            else:
                occupied2.append(0)
for a in range(0,len(occupied1)):
    if(occupied1[a]==occupied2[a]==1):
        num+=1
print(num)
