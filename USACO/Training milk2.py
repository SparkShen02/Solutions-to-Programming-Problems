"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: milk2
"""
fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')


intervals=[]
for i in range(int(fin.readline().strip())):
    a, b = map(int, fin.readline().strip().split(" "))
    intervals.append((a,b))
intervals.sort()

merge=[]
merge.append(intervals[0])
for cur in intervals:
    top=merge[-1]
    if cur[0]>top[1]:
        merge.append(cur)
    else:
        tup=(top[0], max(cur[1], top[1]))
        merge[-1] = tup
print(merge)

longestMilk=0
longestIdle=0
for i in range(0, len(merge)):
    if i==0 :
        longestMilk=merge[0][1]-merge[0][0]
        continue
    numMilk=merge[i][1]-merge[i][0]
    numIdle=merge[i][0]-merge[i-1][1]
    if numMilk > longestMilk:
        longestMilk=numMilk
    if numIdle > longestIdle:
        longestIdle=numIdle
    i+=1
result=str(longestMilk)+" "+str(longestIdle)


fout.write (result + '\n')
fout.close()
