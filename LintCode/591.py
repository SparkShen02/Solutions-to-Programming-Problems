class ConnectingGraph3:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.group=[n for n in range(n+1)]
        self.size=len(self.group)
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        aa=self.findRoot(a)
        bb=self.findRoot(b)
        if aa!=bb:
            self.group[bb]=aa
            self.size-=1
    """
    @return: An integer
    """
    def query(self):
        return self.size-1
    def findRoot(self,index):
        while self.group[index]!=index:
            index=self.group[index]
        return index