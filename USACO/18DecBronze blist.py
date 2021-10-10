"""
ID: kraps
LANG: PYTHON3
TASK: blist
"""
fin = open('blist.in', 'r').read().strip().split('\n')
fout = open('blist.out', 'w')

cows = []
buckets = []
sumOfBuckets = 0
for i in range(int(fin[0])):
    s, t, b = map(int, fin[i+1].split(' '))
    cows.append((s, t, b))
    sumOfBuckets += b
for i in range(sumOfBuckets):
    buckets.append((False, 0))
cows.sort()

for cow in cows:
    start, end, num = cow
    for i in range(num):
        for index in range(len(buckets)):
            bucket = buckets[index]
            if (bucket[0] == True and bucket[1] < start) or (bucket[0] == False):
                buckets[index] = (True, end)
                break

res = 0
for bucket in buckets:
    if bucket[0] == True:
        res += 1
fout.write (str(res) + '\n')
