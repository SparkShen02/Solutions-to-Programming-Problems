import math
def isPrime(num):
    count = 0
    for i in range(1, int(math.sqrt(num))+1):
        if count > 2:
            break
        if (num % i) == 0: 
            count += 1
            if num%i != i:
                count += 1
    if count == 2:
        return True
    return False

n = int(input())
res = []
for i in range(n):
    num = int(input())
    j = 2
    while j <= num*2:
        fir = j
        sec = num*2 - j
        if isPrime(fir) and isPrime(sec):
            res.append(fir)
            res.append(sec)
            break
        j += 1

i = 0
while i < n*2:
    print(str(res[i]) + ' ' + str(res[i+1]))
    i+=2
