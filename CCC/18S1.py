import math
import sys

inp = sys.stdin.read().strip().split('\n')

arr = []
n = int(inp[0])
for i in range(n):
    arr.append(int(inp[1+i]))
arr.sort()

res = math.inf
for i in range(1, n-1):
    pre, nex = arr[i-1], arr[i+1]
    curRes = (nex-pre)/2
    res = min(res, curRes)

sys.stdout.write(str(res) + '\n')
