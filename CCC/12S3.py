import sys
input=sys.stdin.readline
numOfSensors=int(input())
reading=dict()
for i in range(numOfSensors):
    read=int(input())
    if(read not in reading):
        reading[read]=1;
    else:
        reading[read]+=1
frequency=list(reading.items())
frequency=[(reading,read) for (read,reading) in frequency]##(frequency,reading)
frequency.sort(reverse=True)##descending
firstF=frequency[0][0]
secondF=0
firstFre=[]
secondFre=[]
for item in frequency:
    if item[0]!=firstF:
        secondF=item[0]
        break
for item in frequency:
    if item[0]==firstF:
        firstFre.append(item[1])
    if item[0]==secondF:
        secondFre.append(item[1])
    if item[0]!=firstF and item[0]!=secondF:
        break
if len(firstFre)>1:
    firstFre.sort()
    print(abs(firstFre[-1]-firstFre[0]))
elif len(firstFre)==1 and len(secondFre)==1:
    print(abs(firstFre[0]-secondFre[0]))
elif len(firstFre)==1 and len(secondFre)>1:
    secondFre.sort()
    print(max(abs(firstFre[0]-secondFre[0]),abs(firstFre[0]-secondFre[-1])))
    
