class Solution:
    '''
    Dynamic programming. 
    dp[n] = the number of possible sequences that add up to n
    dp[n] = sum(dp[n-num] for num in nums)
    Time complexity: O(target*len(nums)), Space complexity: O(target). 
    '''
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for n in range(target+1)]
        dp[0] = 1
        for n in range(1, target+1):
            for num in nums:
                if n-num >= 0:
                    dp[n] += dp[n-num]
        return dp[target]
