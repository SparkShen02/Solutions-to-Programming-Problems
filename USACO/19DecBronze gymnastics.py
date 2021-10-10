fin = open("gymnastics.in", "r").read().strip().split("\n")
fout = open("gymnastics.out", "w")

K, N = map(int, fin[0].strip().split())
consistent = set()

for i in range(1, 1+K):
    cows = fin[i].strip().split()
    for j in range(N-1):
        for k in range(j+1, N):
            if i==1:
                consistent.add((cows[j], cows[k]))
                continue
            if (cows[k], cows[j]) in consistent:
                consistent.remove((cows[k], cows[j]))
fout.write("{}\n".format(len(consistent)))
