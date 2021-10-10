"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: milk3
"""
fin = open ('milk3.in', 'r')
fout = open ('milk3.out', 'w')

def findNext(node):
    #a-b, b-a, a-c, c-a, b-c, c-b
    res = []
    
    num = min(node[0], B - node[1])
    res.append((node[0]-num, node[1]+num, node[2]))

    num = min(node[1], A - node[0])
    res.append((node[0]+num, node[1]-num, node[2]))

    num = min(node[0], C - node[2])
    res.append((node[0]-num, node[1], node[2]+num))

    num = min(node[2], A - node[0])
    res.append((node[0]+num, node[1], node[2]-num))

    num = min(node[1], C - node[2])
    res.append((node[0], node[1]-num, node[2]+num))

    num = min(node[2], B - node[1])
    res.append((node[0], node[1]+num, node[2]-num))

    return res

res = []
A, B, C = map(int, fin.readline().strip().split(' '))
toVisit, visited = [], []
toVisit.append([0, 0, C])
while toVisit:
    cur = toVisit.pop()
    if cur[0] == 0:
        if cur[2] not in res:
            res.append(cur[2])
    visited.append(cur)
    for a in findNext(cur):
        if a not in visited and a not in toVisit:
            toVisit.append(a)
res.sort()

result=''
for i in range(len(res)):
    if i != len(res)-1:
        result+=str(res[i])+' '
result+=str(res[len(res)-1])

fout.write (result + '\n')
fout.close()
