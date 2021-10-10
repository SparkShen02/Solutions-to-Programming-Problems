def knap01(N, C):
    bag=[0 for n in range(0,C+1)]
    for i in range(0, N):
        for c in range(C, weights[i]-1, -1):
            bag[c]=max(bag[c], bag[c-weights[i]] + values[i])
    return max(bag)

S, N = map(int, input().split())
weights, values = [], []
for i in range(N):
    w,v = map(int, input().split())
    weights.append(w)
    values.append(v)
print(knap01(N, S))
    
