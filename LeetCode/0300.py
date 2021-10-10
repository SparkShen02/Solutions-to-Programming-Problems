class Solution:
    '''
    dp[i] = length of the longest increasing subsequence that ends with nums[i]
    dp[i] = 1 + max of dp[j] such that 0 <= j < i and nums[i] > nums[j]
    Time complexity: O(n^2), Space complexity: O(n). 
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            max_dp_j = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    max_dp_j = max(max_dp_j, dp[j])
            dp[i] = 1 + max_dp_j
        return max(dp)
