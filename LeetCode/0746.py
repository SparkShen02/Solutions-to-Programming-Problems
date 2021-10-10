class Solution:
    '''
    f[i] = the min cost to reach the i-th step
    f[i] = min(f[i-1] + cost[i-1], f[i-2] + cost[i-2])
    Time complexity: O(n), Space complexity: O(1). 
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:        
        a = 0 # f[i-1]
        b = 0 # f[i-2]
        for i in range(2, len(cost)+1):
            temp = a
            a = min(a + cost[i-1], b + cost[i-2])
            b = temp
        return a