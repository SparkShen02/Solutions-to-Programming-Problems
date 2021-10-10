def knap01(N, C):
    bag=[0 for n in range(0,C+1)]
    for i in range(0, N):
        for c in range(C, weights[i]-1, -1): 
            bag[c]=max(bag[c], bag[c-weights[i]] + values[i])
    return max(bag)

for i in range(int(input())):
    weights = []
    n, k = map(int, input().split())
    for j in range(n):
        weights.append(sum(list(map(int, input().split()))[1:]))
    values = weights
    print(knap01(n, k))
    print()
