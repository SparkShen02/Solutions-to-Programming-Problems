"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: barn1
"""
fin = open ('barn1.in', 'r')
fout = open ('barn1.out', 'w')

boards, stalls, cows = map(int, fin.readline().strip().split(' '))
length_blank = []
occupied = []

for i in range(cows):
    occupied.append(int(fin.readline().strip()))
occupied.sort()

for i in range(cows):
    if i == 0:
        first = occupied[0]
        curr = first
    elif i == cows-1:
        last = occupied[-1]
        length_blank.append(last - curr)
    else:
        num = occupied[i]
        length_blank.append(num - curr)
        curr = num

res = last - first + 1
length_blank.sort(reverse = True)
for i in range(boards-1):
    if i >= len(length_blank):
        break
    res -= length_blank[i] - 1

fout.write (str(res) + '\n')
fout.close()
