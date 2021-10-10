"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: palsquare
"""
fin = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')

def if_pal(s):
    for i in range(0, len(s)//2):
        if s[i]!=s[-i-1]:
            return False
    return True

def base10to(num, base):#base 2-20
    result=''
    BASE=['A','B','C','D','E','F','G','H','I','J','K']
    while num!=0:
        remainder=num%base
        if remainder>=10:
            remainder=BASE[remainder-10]
            result=remainder+result
        else:
            result=str(num%base)+result
        num=num//base
    return result

base=int(fin.readline().strip())
for N in range(1,301):
    num=N*N
    num=base10to(num, base)
    if if_pal(num):
        N=base10to(N, base)
        result=N+" "+str(num)
        fout.write(result + '\n')

fout.close()
