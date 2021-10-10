import sys
from collections import deque

def knap01(N, C):
    bag=[0 for n in range(0,C+1)]
    for i in range(0, N):
        for c in range(C, weights[i]-1, -1): 
            bag[c]=max(bag[c], bag[c-weights[i]] + values[i])
    return max(bag)

lines = sys.stdin.read().strip().split('\n')
index_lines = 1
for i in range(int(lines[0])):
    weights = deque()
    values = deque()
    K, M = map(int, lines[index_lines].split())
    for j in range(M):
        w, v = map(int, lines[index_lines+1].split())
        weights.append(w)
        values.append(v)
        index_lines += 1
    sys.stdout.write("Hey stupid robber, you can get {}.\n".format(knap01(M, K)))
    index_lines += 1
