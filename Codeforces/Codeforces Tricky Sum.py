for i in range(int(input())):
    num = int(input())
    res = (1 + num) * num // 2
    a = 0
    while 2**a <= num:
        res -= 2**a * 2
        a += 1
    print(res)

