distance=list(map(int, input().split(" ")))
for i in range(1,6):
    num1=0
    num2=0
    line=[None]*5
    line[i-1]=0
    if(i-1>0):
        for a in range(2-i,1):
            num1=distance[-a]+num1
            line[-a]=num1
    for a in range(i-1,4):
            num2=distance[a]+num2
            line[a+1]=num2
    for x in range(0,len(line)):
        print(str(line[x])+" ",end="")##no line break
    print()
            
