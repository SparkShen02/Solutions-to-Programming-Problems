debug = False
if debug:
    fin = []
    while True:
        a = input()
        if a != "stop":
            fin.append(a)
        else:
            break
else:
    fin = open('rental.in', 'r').read().strip().split('\n')
    fout = open('rental.out', 'w')

N, M, R = map(int, fin[0].split(' ')) # numCows, numStores, numRents
cows, stores, rents = [], [], []

for i in range(N):
    cows.append(int(fin[i+1]))
cows.sort()
length = len(cows)
for i in range(M):
    amount, price = map(int, fin[N+1+i].split(' '))
    stores.append([price, amount])
stores.sort()
for i in range(R):
    rents.append(int(fin[N+M+1+i]))
rents.sort()

prices = []
i = 1
while cows and i <= len(stores):
    sell = 0
    cow = cows.pop()
    price, amount = stores[-i]
    while cow > amount:
        sell += amount * price
        cow -= amount
        i += 1
        if i > len(stores):
            break
        price, amount = stores[-i]
    if i <= len(stores):
        sell += price * cow
        stores[-i][1] -= cow

    prices.append(sell)

while len(prices) < length:
    prices.append(0)

res = 0
for i in range(1, length+1):
    if i > len(rents):
        break
    sell, rent = prices[-i], rents[-i]
    if rent >= sell:
        prices[-i] = rent

if debug:
    print(sum(prices))
else:
    fout.write(str(sum(prices)) + '\n')
