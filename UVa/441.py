line = input().split()
first = True

while len(line) > 1:
    if first:
        first = False
    else:
        print()

    num = int(line[0])
    for a in range(1, num-4):
        for b in range(a+1, num-3):
            for c in range(b+1, num-2):
                for d in range(c+1, num-1):
                    for e in range(d+1, num):
                        for f in range(e+1, num+1):
                            print(line[a],line[b],line[c],line[d],line[e],line[f])

    line = input().split()
