"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: milk
"""
fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')

total, n = map(int, fin.readline().strip().split())
price = []
amount = {}
result=0
for i in range(n):
    pri, amo = map(int, fin.readline().strip().split())
    price.append(pri)
    if pri in amount:
        amount[pri]+=amo
    else:
        amount[pri] = amo
price.sort()

current=-1
for pri in price:
    if pri==current:
        continue
    current=pri
    if amount[pri] < total:
        total-=amount[pri]
        result+=amount[pri]*pri
    else:
        result+=total*pri
        break
        
fout.write (str(result) + '\n')
fout.close()
