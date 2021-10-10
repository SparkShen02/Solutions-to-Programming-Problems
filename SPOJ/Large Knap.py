import sys
from collections import deque

def knap01(N, C):
    bag=[0 for n in range(0,C+1)]
    for i in range(0, N):
        for c in range(C, weights[i]-1, -1):
            bag[c]=max(bag[c], bag[c-weights[i]] + values[i])
    return max(bag)

lines = sys.stdin.read().strip().split('\n')
S, N = map(int, lines[0].split())
i = 1
weights, values = deque(), deque()
for x in range(N):
    v,w = map(int, lines[i].split())
    i += 1
    weights.append(w)
    values.append(v)
    
sys.stdout.write(str(knap01(N, S)))
