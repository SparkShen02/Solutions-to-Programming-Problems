def findAll(num):
    a = 1
    b = num-1
    res = []
    while a != b and b != a-1:
        res.append((a,b))
        a += 1
        b-= 1
    return res

'''
辗转相除法。两数为a, b (a > b)，求它们最大公约数:

设 d 为 a 和 b 的公约数，a = xd, b = yd。
设 r = a % b，则 a = zb + r。
r = a - zb = xd - yzd = (x-yz)d，说明 d 也是 r 的公约数。

设 d 为 b 和 r 的公约数，b = xd, r = xd。
设 r = a % b，则 a = zb + r。
a = xzd + xd = (xz+x)d，说明 d 也是 a 的公约数。

所以，a 和 b 的公约数也是 b 和 a%b 的公约数，反之同理。a, b 以及 b, a%b 有着相同的公约数集，
说明 a 和 b 的最大公约数也是 b 和 a%b 的最大公约数。
'''
def computeGCD(x, y): 
   while y != 0: 
       x, y = y, x % y 
   return x 

num = int(input())
if num == 3:
    print('1 2')
else:
    all = findAll(num)
    for i in range(len(all)-1, -1, -1):
        a, b = all[i]
        if i == 0:
            print(str(a) + ' ' + str(b))
            break
        if computeGCD(a,b) == 1:
            print(str(a) + ' ' + str(b))
            break
