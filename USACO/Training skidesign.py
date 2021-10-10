"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: skidesign
"""
fin = open ('skidesign.in', 'r')
fout = open ('skidesign.out', 'w')

hills = []
minNum = 100
maxNum = 0
for i in range(int(fin.readline().strip())):
    num = int(fin.readline().strip())
    hills.append(num)
    if num < minNum:
        minNum = num
    if num > maxNum:
        maxNum = num

minCost = 2147483647
for num in range(minNum, min(maxNum, 83)+1):
    cost = 0
    for hill in hills:
        if hill < num:
            #print('hill < num, hill is ' + str(hill))
            cost += (num - hill) ** 2
        if hill > num + 17:
            cost += (hill - num - 17) ** 2
            #print('hill >, hill is ' + str(hill))
    if cost < minCost:
        minCost = cost
    #print(num, cost)

fout.write (str(minCost) + '\n')
fout.close()
