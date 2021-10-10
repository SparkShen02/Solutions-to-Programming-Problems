def ok(wait): # 可以在每只牛的等待时间都不大于wait的情况下送完全部牛
    bus = 0 # mininum number of buses needed to transport all the cows
    i = 0 # current cow
    while i < numOfCows:
        j = i  # cow i and cow j are in the same bus
        while j < numOfCows and i + cowsEachBus > j:
            if cows[j] - cows[i] > wait:
                break
            j += 1
        bus += 1
        i = j
    return bus <= numOfBuses

fin = open("convention.in", "r")
fout = open("convention.out", "w")

# N, M, C
numOfCows, numOfBuses, cowsEachBus = map(int, fin.readline().strip().split(' '))
cows = list(map(int, fin.readline().strip().split(' ')))
cows.sort()

low = 0
high = 1000000000
while low < high:
    mid = (low + high) // 2
    if ok(mid):
        high = mid
    else:
        low = mid + 1

fout.write (str(high) + '\n')
fout.close()
