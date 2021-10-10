debug = False
if debug:
    fin = []
    while True:
        string = input()
        if string != 'stop':
            fin.append(string)
        else:
            break
else:
    fin = open('planting.in', 'r').read().strip().split('\n')
    fout = open('planting.out', 'w')

num = int(fin[0])
arr = [0 for i in range(num+1)]

for i in range(num-1):
    a, b = map(int, fin[1+i].split(' '))
    arr[a] += 1
    arr[b] += 1

if debug:
    print(max(arr)+1)
else:
    fout.write(str(max(arr)+1) + '\n')
