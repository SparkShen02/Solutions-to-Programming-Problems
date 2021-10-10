"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: namenum
"""
fin = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')
dictionary = open('dict.txt', 'r')

dic=[]
for i in range(5000):
    dic.append(dictionary.readline().strip())

key = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PRS', 'TUV', 'WXY']
arr=[]
for ch in fin.readline().strip():
    arr.append(key[int(ch)])

none=True
for ch in dic:
    correspond=True
    if len(ch)!=len(arr):
        continue
    for i in range(len(ch)):
        if ch[i] not in arr[i]:
            correspond=False
    if correspond:
        none=False
        fout.write (ch + '\n')
        
if none:
    fout.write("NONE" + '\n')
fout.close()
