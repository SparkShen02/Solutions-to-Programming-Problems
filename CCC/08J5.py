##you win if there is at least one way to create a losing situation
##you lose if there is no move OR all possible moves lead to a winning situation
def nextStates(a,b,c,d):
    result=[]
    if(a>=2 and b>=1 and d>=2):
        result.append((a-2,b-1,c,d-2))
    if(a>=1 and b>=1 and c>=1 and d>=1):
        result.append((a-1,b-1,c-1,d-1))
    if(c>=2 and d>=1):
        result.append((a,b,c-2,d-1))
    if(b>=3):
        result.append((a,b-3,c,d))
    if(a>=1 and d>=1):
        result.append((a-1,b,c,d-1))
    return result
def isWinning(A,B,C,D):
    if (A,B,C,D) in cache1:
        return cache1[(A,B,C,D)]
    next=nextStates(A,B,C,D)
    for state in next:
        a,b,c,d=state
        if isLosing(a,b,c,d):
            cache1[(A,B,C,D)]=True
            return True
    cache1[(A,B,C,D)]=False
    return False
def isLosing(A,B,C,D):
    if (A,B,C,D) in cache2:
        return cache2[(A,B,C,D)]
    next=nextStates(A,B,C,D)
    if len(next)==0:
        return True
    lose=True
    for state in next:
        a,b,c,d=state
        if not isWinning(a,b,c,d):
            lose=False
    cache2[(A,B,C,D)]=lose
    return lose
for i in range(int(input())):
    A,B,C,D=map(int,input().split(" "))
    cache1={}
    cache2={}
    if isWinning(A,B,C,D):
        print("Patrick")
    else:
        print("Roland")
