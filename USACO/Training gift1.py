"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

NP=int(fin.readline().strip())
account={}
for i in range(NP):
    name=fin.readline().strip()
    account[name]=0
while True:
    giver=fin.readline().strip()
    if giver=="":
        break
    money, num = map(int, fin.readline().strip().split(" "))
    if num is 0:
        continue
    each=int(money/num)
    rest=money%num
    account[giver]=account[giver]-money+rest
    for i in range(num):
        reciver=fin.readline().strip()
        account[reciver]+=each

for name in account:
    string=name+" "+str(account[name])
    fout.write (string + '\n')
fout.close()
