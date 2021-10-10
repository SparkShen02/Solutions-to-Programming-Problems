"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

num=['0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
comet = fin.readline().strip()
group = fin.readline().strip()
cometRes=1
groupRes=1

for char in comet:
    cometRes*=num.index(char)
for char in group:
    groupRes*=num.index(char)


if cometRes%47 == groupRes%47:
    fout.write ("GO" + '\n')
else:
    fout.write ("STAY" + '\n')
fout.close()
