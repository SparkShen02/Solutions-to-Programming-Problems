from heapq import *
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.arr=[]
        self.num=k
    # do intialization if necessary
    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        heappush(self.arr, num)
    """
    @return: Top k element
    """
    def topk(self):
        return nlargest(self.num,self.arr)