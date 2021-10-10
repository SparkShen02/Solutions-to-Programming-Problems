"""
ID: kraps
LANG: PYTHON3
TASK: mixmilk
"""
def threeSteps():
    global c1, c2, c3, m1, m2, m3
    # pour 1 to 2
    num = min(m1, c2 - m2)
    m1 -= num
    m2 += num
    # pour 2 to 3
    num = min(m2, c3 - m3)
    m2 -= num
    m3 += num
    # pour 3 to 1
    num = min(m3, c1 - m1)
    m3 -= num
    m1 += num

fin = open ('mixmilk.in', 'r')
fout = open ('mixmilk.out', 'w')
lines = fin.read().strip().split('\n')

c1, m1 = map(int, lines[0].split(' '))
c2, m2 = map(int, lines[1].split(' '))
c3, m3 = map(int, lines[2].split(' '))

for i in range(33):
    threeSteps()

# 100th step
# pour 1 to 2
num = min(m1, c2 - m2)
m1 -= num
m2 += num

fout.write (str(m1) + '\n')
fout.write (str(m2) + '\n')
fout.write (str(m3) + '\n')
