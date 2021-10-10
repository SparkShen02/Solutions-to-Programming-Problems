"""
ID: kraps
LANG: PYTHON3
TASK: backforth
"""
fin = open('backforth.in', 'r').read().strip().split('\n')
fout = open('backforth.out', 'w')

def A_to_B():
    res = []
    for situation in cur:
        bucketA = situation[0][1]
        bucketB = situation[1][1]
        for i in range(len(bucketA)):
            bucket = bucketA[i]
            capacityA = situation[0][0]
            capacityB = situation[1][0]
            newA = bucketA[:]
            newB = bucketB[:]
            newA.pop(i)
            newB.append(bucket)
            capacityA -= bucket
            capacityB += bucket
            res.append( ( (capacityA, newA), (capacityB, newB) ) )
    return res
def B_to_A():
    res = []
    for situation in cur:
        bucketA = situation[0][1]
        bucketB = situation[1][1]
        for i in range(len(bucketB)):
            bucket = bucketB[i]
            capacityA = situation[0][0]
            capacityB = situation[1][0]
            newA = bucketA[:]
            newB = bucketB[:]
            newB.pop(i)
            newA.append(bucket)
            capacityA += bucket
            capacityB -= bucket
            res.append( ( (capacityA, newA), (capacityB, newB) ) )
    return res

cur = [ ( (1000, list(map(int, fin[0].split(' ')))), (1000, list(map(int, fin[1].split(' ')))) ) ]

#TUE
cur = A_to_B()
#WED
cur = B_to_A()
#THU
cur = A_to_B()
#FRI
cur = B_to_A()

res = []
count = 0
for each in cur:
    if each[0][0] not in res:
        res.append(each[0][0])
        count += 1

fout.write (str(count) + '\n')
