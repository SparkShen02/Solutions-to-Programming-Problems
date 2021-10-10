class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self,n):
        class PriorityQueue:
            def __init__(self):
               self.queue=[]
            def push(self,item,priority):##O(n)
                if len(self.queue)==0:
                    self.queue.append((item,priority))
                else:
                    for i in range(0,len(self.queue)):
                        if item==self.queue[i][0]:
                            break
                        if priority>=self.queue[i][1]:
                            self.queue.insert(i,(item,priority))
                            break
                        if i==len(self.queue)-1:
                            self.queue.append((item,priority))
            def pop(self):##O(1)
                return self.queue.pop(-1)[0]
            def peek(self):
                return self.queue[-1][0]
            def size(self):
                return len(self.queue)
        pq=PriorityQueue()
        pq.push(1,1)
        if n==1:
            return 1
        else:
            for i in range(1,n):
                num=pq.pop()
                pq.push(num*2,num*2)
                pq.push(num*3,num*3)
                pq.push(num*5,num*5)
            return pq.pop()