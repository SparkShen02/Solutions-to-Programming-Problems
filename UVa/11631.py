def findRoot(index):
    global parents
    cur_index = index
    while parents[index] != index:
        index = parents[index]
    parents[cur_index] = index
    return index

def union(rootA,rootB):
    global ranks, parents
    if ranks[rootA] == ranks[rootB]:
        parents[rootA] = rootB
        ranks[rootB] += 1

    elif ranks[rootA] > ranks[rootB]:
        parents[rootB] = rootA

    else:
        parents[rootA] = rootB

from sys import stdin, stdout
lines = stdin.read().strip().split('\n')
index = 0
while True:
    node, road=map(int,lines[index].split())
    index += 1

    if node==0 and road==0:
        break

    cost, parents, ranks = list(range(road)), dict(), dict()

    for i in range(node):
        parents[i] = i
        ranks[i] = 1

    total=0
    for i in range(road):
        n, m, k=map(int,lines[index].split())
        index += 1
        cost[i] = (k, n, m)
        total += k
    cost.sort(key=lambda R:R[0])

    count = 1
    for c, u, v in cost:
        rootA, rootB = findRoot(u), findRoot(v)
        if rootA != rootB:
            union(rootA,rootB)
            total -= c
            count +=1
            if count == node:
                break
    stdout.write(str(total)+"\n")
    
    
    
