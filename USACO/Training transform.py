"""
ID: shenyu01
import sys
sys.stderr.write('message')
LANG: PYTHON3
TASK: transform
"""
fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')

def nightyRotation(matrix):
    numRow=len(matrix)
    numCol=len(matrix[0])
    newMatrix=[[0 for n in range(numCol)] for i in range(numRow)]
    for row in range(0, numRow):
        for col in range(0, numCol):
            newMatrix[col][numRow-1-row]=matrix[row][col]
    return newMatrix
def reflection(matrix):
    numRow=len(matrix)
    numCol=len(matrix[0])
    newMatrix=[[0 for n in range(numCol)] for i in range(numRow)]
    for row in range(0, numRow):
        for col in range(0, numCol):
            newMatrix[row][numCol-1-col]=matrix[row][col]
    return newMatrix
def result(str):
    fout.write (str + '\n')
    fout.close()

while True:
    num=int(fin.readline().strip())
    before=[[0 for i in range(num)] for i in range(num)]
    after=[[0 for i in range(num)] for i in range(num)]
    for i in range(num):
        before[i]=list(fin.readline().strip())
    for i in range(num):
        after[i]=list(fin.readline().strip())

    cur=nightyRotation(before)#90
    if cur==after:
        result('1')
        break
    cur=nightyRotation(cur)#180
    if cur==after:
        result('2')
        break
    cur=nightyRotation(cur)#270
    if cur==after:
        result('3')
        break
    cur=reflection(before)#reflection
    if cur==after:
        result('4')
        break
    cur=nightyRotation(cur)#combination
    if cur==after:
        result('5')
        break
    cur=nightyRotation(cur)
    if cur==after:
        result('5')
        break
    cur=nightyRotation(cur)
    if cur==after:
        result('5')
        break
    if before==after:#no change
        result('6')
        break
    result('7')
    break
