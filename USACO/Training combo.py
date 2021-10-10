"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: combo
"""
fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w')

def findAll():
    res = []
    for first in a:
        for second in b:
            for third in c:
                cur = str(first) + ', ' + str(second) + ', ' + str(third)
                if cur not in res:
                    res.append(cur)
    return res
def makeList():
    number = [i for i in range(num)]
    number[0] = num
    return number
def abc(arr):
    if len(number) < 5:
        return [number, number, number]
    res = []
    for each in arr:
        cur = []
        for i in range(each-2, each+3):
            cur.append(number[i])
        res.append(cur)
    return res

num = int(fin.readline().strip())
number = makeList()
number *= 2
list1 = list(map(int, fin.readline().strip().split(' ')))
list2 = list(map(int, fin.readline().strip().split(' ')))

a, b, c = abc(list1)
res1 = findAll()
a, b, c= abc(list2)
res2 = findAll()

for each in res2:
    if each not in res1:
        res1.append(each)

fout.write (str(len(res1)) + '\n')
fout.close()
