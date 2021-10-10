"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: dualpal
"""
fin = open ('dualpal.in', 'r')
fout = open ('dualpal.out', 'w')

def base10to(num, base):#base 2-10
    result=''
    while num!=0:
        remainder=num%base
        result=str(num%base)+result
        num=num//base
    return result

def if_pal(s):
    for i in range(0, len(s)//2):
        if s[i]!=s[-i-1]:
            return False
    return True

N, S = map(int, fin.readline().strip().split(' '))
while N>0:
    S+=1
    count=0
    for base in range(2, 11):
        if if_pal(base10to(S, base)):
            count+=1
        if count==2:
            fout.write (str(S) + '\n')
            N-=1
            break

fout.close()
