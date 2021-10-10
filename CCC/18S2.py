import sys
def rotate(arr):
    n = len(arr)
    newArr = [[-1 for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            newArr[i][j] = arr[j][n-i-1]
    return newArr

def output(arr, n):
    for row in arr:
        res = ''
        for num in row:
            res += str(num) + ' '
        sys.stdout.write(res + '\n')

def one(arr): # Each day, all of the ﬂowers grow taller than they were the day before.
    for row in arr: 
        for j in range(len(row)-1):
            if row[j] >= row[j+1]:
                return False
    return True
    
def two(arr): # Flowers are ordered from smallest to largest
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j][i] >= arr[j+1][i]:
                return False
    return True

def judge(arr):
    return one(arr) and two(arr)

inp = sys.stdin.read().strip().split('\n')
n = int(inp[0])
arr = [list(map(int, inp[1+i].split())) for i in range(n)]

if judge(arr):
    output(arr, n)
else:
    for i in range(3):
        arr = rotate(arr)
        if judge(arr):
            output(arr, n)
            break
