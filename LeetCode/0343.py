class Solution:
    '''
    dp[s] = the max product of any positive integers that sum to s
    dp[s] = max(dp[s-num] * num for num from 1 to s-1)
    Time complexity: O(n^2), Space complexity: O(n). 
    '''
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0 for i in range(n+1)]
        dp[1], dp[2], dp[3] = 1, 2, 3

        for s in range(4, n+1):
            dp[s] = max([dp[s-num] * num for num in range(1, s)])
        
        return dp[n]
