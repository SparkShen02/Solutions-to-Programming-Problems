from itertools import permutations
cows = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
cons = []
all_per = list(permutations(cows))

fin = open('lineup.in', 'r').read().strip().split('\n')
fout = open('lineup.out', 'w')

for i in range(int(fin[0])):
    line = fin[i+1]
    cur_con = []
    for ch in line.split():
        if ch in cows:
            cur_con.append(ch)
    cons.append(cur_con)

for per in all_per:
    ok = True
    for con in cons:
        a, b = con
        if abs(per.index(a) - per.index(b)) != 1:
            ok = False
    if ok:
        res = per
        break
        
for ch in res:
    fout.write(ch + '\n')
