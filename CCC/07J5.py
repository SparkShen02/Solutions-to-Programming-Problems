cache={}
def getNextMotels(start):
    global motels,mini,maxi
    result=[]
    for i in range(start+1,len(motels)):
        if mini<=motels[i]-motels[start]<=maxi:
            result.append(i)
    return result
def ways(start):
    global motels,mini,maxi
    if start==len(motels)-1:
        return 1
    if start in cache:
        return cache[start]
    nextMotels=getNextMotels(start)
    if len(nextMotels)==0:
        return 0
    result=sum(ways(nextMotel) for nextMotel in nextMotels)
    cache[start]=result
    return result
motels=[0,990,1010,1970,2030,2940,3060,3930,4060,4970,5030,5990,6010,7000]
mini=int(input())
maxi=int(input())
for i in range(int(input())):
    motels.append(int(input()))
motels.sort()
print(ways(0))


