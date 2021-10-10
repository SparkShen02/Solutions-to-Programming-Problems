"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: crypt1
"""
fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')

def findAll(range1, range2):
    arr = []
    for num in range(range1, range2+1):
        num = str(num)
        judge = True
        for ch in num:
            if ch not in letter:
                judge = False
        if judge:
            arr.append(num)
    return arr

def p1(upp, low):
    upp = int(upp)
    low = int(low[1])
    res = upp * low
    res = str(res)
    if len(res) != 3:
        return False
    for ch in res:
        if ch not in letter:
            return False
    return True

def p2(upp, low):
    upp = int(upp)
    low = int(low[0])
    res = upp * low
    res = str(res)
    if len(res) != 3:
        return False
    for ch in res:
        if ch not in letter:
            return False
    return True

def p3(upp, low):
    upp, low = int(upp), int(low)
    res = upp * low
    res = str(res)
    if len(res) != 4:
        return False
    for ch in res:
        if ch not in letter:
            return False
    return True

fin.readline().strip()
letter = fin.readline().strip().split(' ')
upper = findAll(100, 999)
lower = findAll(10, 99)

res = 0
for upp in upper:
    for low in lower:
        if p1(upp, low) and p2(upp, low) and p3(upp, low):
            print(upp, low)
            res += 1

fout.write (str(res) + '\n')
fout.close()

