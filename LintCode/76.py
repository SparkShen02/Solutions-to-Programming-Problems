class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    # dp[i] meanas length of the LIS whose last element is nums[i]
    # dp[i] = max(dp[j]+1) for all j < i, and nums[j] < nums[i]
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1 for i in range(n)]
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
                
        return max(dp)
