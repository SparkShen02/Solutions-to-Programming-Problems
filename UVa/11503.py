class UFDS:##imagining a tree node
    def __init__(self,n):
        self.parents=[n for n in range(n)]
        self.ranks=[0 for n in range(n)]
        self.size_of_trees=[1 for n in range(n)]
    def findRoot(self,index):
        cur_index = index
        while self.parents[index]!=index:
            index=self.parents[index]
        self.parents[cur_index] = index
        return index
    def union(self,u,v):##insert an edge
        a=self.findRoot(u)
        b=self.findRoot(v)
        if a!=b:
            if self.ranks[a] == self.ranks[b]:
                self.parents[a] = b
                self.ranks[b] += 1
                self.size_of_trees[b] += self.size_of_trees[a]

            elif self.ranks[a] > self.ranks[b]:
                self.parents[b] = a
                self.size_of_trees[a] += self.size_of_trees[b]

            else:
                self.parents[a] = b
                self.size_of_trees[b] += self.size_of_trees[a]
    def sizeOfCurrentTree(self, u):
        return self.size_of_trees[self.findRoot(u)]


for i in range(int(input())):
    n = int(input())

    i = 0
    names = set()
    connected_names = []

    for j in range(n):
        nameA, nameB = input().split()
        names.add(nameA)
        names.add(nameB)
        connected_names.append((nameA, nameB))
        
    keys = dict()
    i = 0
    for name in names:
        keys[name] = i
        i += 1

    test = UFDS(len(names))
    for (nameA, nameB) in connected_names:
        test.union(keys[nameA], keys[nameB])
        print(test.sizeOfCurrentTree(keys[nameA]))

        
