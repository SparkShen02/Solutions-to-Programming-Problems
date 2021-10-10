class Solution:
    '''
    f[h] = # of distinct ways to climb to height h
    f[h] = f[h-1] + f[h-2]
    In terms of the space needed, instead of a dictionary, we only need two variables that store f[h-1] and f[h-2]. 
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        a = 2 # represents f[h-1]
        b = 1 # represents f[h-2]
        for h in range(3, n):
            temp = a
            a = a + b # f[h] = f[h-1] + f[h-2]
            b = temp
        return a + b