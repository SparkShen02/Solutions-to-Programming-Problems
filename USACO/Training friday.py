"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: friday
"""
fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

normal=[3,0,3,2,3,2,3,3,2,3,2,3]
leap=[3,1,3,2,3,2,3,3,2,3,2,3]
day=6
week=[0]*7

N=int(fin.readline().strip())
for i in range(N):
    year=1900+i
    for a in range(12):
        day=day%7
        week[day]+=1
        if (year%4==0 and year%100 is not 0) or year%400 is 0:
            day+=leap[a]
        else:
            day+=normal[a]
result=str(week[-1])
for i in range(0, 6):
    result+=" "+str(week[i])

fout.write(result + "\n")
    
