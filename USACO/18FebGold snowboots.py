class UFDS:
    def __init__(self,n):
        self.group = [i for i in range(n)]
        self.size = [1 for i in range(n)] 
    def findRoot(self, index):
        while self.group[index] != index:
            index = self.group[index]
        return index
    def union(self, u, v):
        a = self.findRoot(u)
        b = self.findRoot(v)
        if a != b:
            self.group[b] = a
            self.size[a] += self.size[b]
        return self.size[a] # size of current set

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
    fin = open('snowboots.in', 'r').read().strip().split('\n')
    fout = open('snowboots.out', 'w')

N, B = map(int, fin[0].split())
line = list(map(int, fin[1].split()))
tiles = [(line[i], i) for i in range(N)] # (depth, index)
boots = [] # (detph, step, index)
for i in range(B):
    a, b = map(int, fin[2+i].split())
    boots.append((a, b, i))

no = [False for i in range(N)] # True说明当前的tile不能走
res = [-1 for i in range(B)] # 0 or 1
connectedTiles = UFDS(N)

tiles.sort(reverse = True)
boots.sort(reverse = True)

pos = 0 # 第几个tile
maxDis = 0 # 连续不能走的长度的最大值
for i in range(B): # i表示第几个boot
    curBoot = boots[i]
    while True:
        curTile = tiles[pos]
        if curBoot[0] < curTile[0]:
            dis = 1 # 当前不能连续走的长度
            
            curInd = curTile[1]
            no[curInd] = True
            if no[curInd-1]: dis = connectedTiles.union(curInd, curInd-1)
            if no[curInd+1]: dis = connectedTiles.union(curInd, curInd+1)
            
            maxDis = max(maxDis, dis)
            pos += 1
        else:
            break
    
    if curBoot[1] <= maxDis:
        res[curBoot[2]] = '0'
    else:
        res[curBoot[2]] = '1'
        
for i in range(B):
    if debug:
        print(res[i])
    else:
        fout.write(res[i] + '\n')
