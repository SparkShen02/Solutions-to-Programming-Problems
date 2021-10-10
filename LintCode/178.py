class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        class UFDS:##imagining a tree node
            def __init__(self,n):
                self.group=[n for n in range(n)]
                self.size=len(self.group)
            def findRoot(self,index):
                while self.group[index]!=index:
                    index=self.group[index]
                return index
            def union(self,u,v):##insert an edge
                a=self.findRoot(u)
                b=self.findRoot(v)
                if a!=b:
                    self.group[b]=a
                    self.size-=1
            def numOfConnectedComponent(self):##actually the same with how many tree nodes
                return self.size
        tree=UFDS(n)
        for edge in edges:
            if tree.findRoot(edge[0])==tree.findRoot(edge[1]):
                return False
            tree.union(edge[0],edge[1])
        if tree.numOfConnectedComponent()!=1:
            return False
        return True