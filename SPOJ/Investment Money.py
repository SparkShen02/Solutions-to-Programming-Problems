def knapComplete(N,C):
    bag=[0 for i in range(0,C+1)]
    for i in range(0, N):
        for c in range(weights[i], C+1):
            bag[c] = max(bag[c], bag[c-weights[i]] + values[i])
    return max(bag)

for i in range(int(input())):
    money, years = map(int, input().split())
    weights, values = [], []
    n = int(input())
    for j in range(n):
        a, b = map(int, input().split())
        weights.append(a)
        values.append(b)

    for k in range(years):
        money += knapComplete(n, money)

    print(money)
