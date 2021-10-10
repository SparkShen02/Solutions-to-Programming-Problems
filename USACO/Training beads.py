"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: beads
"""
fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')
fin.readline()

def findString(a, b):
    index=0
    count=-1
    notChange=True
    while True:
        if string[index]!="w":
            count+=1
        if count==a and notChange:
            index1=index
            notChange=False
        if count==b:
            index2=index
            break
        index+=1
    while index2<len(string)-1 and string[index2+1]=="w":
        index2+=1
    while index1>0 and string[index1-1]=="w":
        index1-=1
    return index2-index1+1

string=fin.readline().strip()
if 'r' not in string or 'b' not in string:
    fout.write(str(len(string)) + '\n')
    fout.close()
else:
    leng=len(string)
    string+=string
    print(string)
    advance=""
    maxLength=-1
    for ch in string:
        if ch!="w":
            advance+=ch
    length=[]
    for i in range(0, len(advance)):
        countChange=0
        start=i
        while start<len(advance)-1 and countChange<=1:
            if advance[start]==advance[start+1]:
                start+=1
            else:
                countChange+=1
                start+=1
        if start==len(advance)-1 and countChange<=1:
            start+=1
        length=findString(i,start-1)
        if length>maxLength:
            maxLength=length

    fout.write (str(min(maxLength, leng)) + '\n')
    fout.close()
